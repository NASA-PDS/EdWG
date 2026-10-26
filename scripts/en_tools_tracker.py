#!/usr/bin/env python3
"""Generate PDS4 Product_Resource labels from a spreadsheet of PDS tools.

The input is a CSV or TSV file, or the URL of a Google Sheet, with one tool or
service per row. One label is written per row, named
``<node>_<tool>_v<version>.xml``, with the logical identifier
``urn:nasa:pds:context:resource:<tool>``.

If the output directory already holds a label for the same logical identifier,
the two are compared ignoring the version and the modification history. When
they differ, the user is asked whether to replace the old label with a new one
whose minor version is bumped. The old label is kept with a ``.DELETED``
suffix.
"""
from __future__ import annotations

import argparse
import copy
import csv
import difflib
import enum
import io
import logging
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import date
from pathlib import Path

PDS_NS = "http://pds.nasa.gov/pds4/pds/v1"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
SCHEMA_BASE_URL = "https://pds.nasa.gov/pds4/pds/v1"
SCHEMATRON_NS = "http://purl.oclc.org/dsdl/schematron"

ET.register_namespace("", PDS_NS)
ET.register_namespace("xsi", XSI_NS)

DEFAULT_PDS_VERSION = "1R00"
DEFAULT_OUTPUT_DIR = Path("toolsResources")
REQUEST_TIMEOUT_SECONDS = 30
INDENT = "    "

RESOURCE_LID_PREFIX = "urn:nasa:pds:context:resource:"
NODE_LID_PREFIX = "urn:nasa:pds:context:node:"

# The "status" column may be present in the sheet but is not used.
REQUIRED_HEADERS = (
    "node / org",
    "Tool / Service Name",
    "URL",
    "Release Date",
    "Resource Type",
    "Resource Subtype",
    "Interface Type",
    "Description",
    "Internal Reference",
    "Applicable to All PDS4 Data?",
)

TRUE_VALUES = frozenset({"yes", "true", "y", "1"})

# Lowercased "node / org" value -> identifier of the node's context product.
NODE_LIDS = {
    "atm": "node.atmos",
    "en": "node.en",
    "geo": "node.geoscience",
    "img": "node.imaging",
    "naif": "node.naif",
    "ppi": "node.ppi-ucla",
    "psa": "node.psa",
    "rms": "node.rings",
    "sbn": "node.sbn",
}
NODE_ALIASES = {"community": "en"}

PDS_VERSION_PATTERN = re.compile(r"(\d)([0-9A-Z])(\d)(\d)")
VERSION_ID_PATTERN = re.compile(r"(\d+)\.(\d+)")
# urn:<agency>:<archive>:context:<product type>:<name>, optionally with ::<vid>
CONTEXT_LID_PATTERN = re.compile(
    r"urn:[^:\s]+:[^:\s]+:context:(?P<product_type>[^:\s]+):[^:\s]+(?:::\S+)?"
)
# urn:<agency>:<archive>:<bundle>, optionally with ::<vid>
BUNDLE_LID_PATTERN = re.compile(r"urn:[^:\s]+:[^:\s]+:[^:\s]+(?:::\S+)?")
GOOGLE_SHEET_ID_PATTERN = re.compile(r"/spreadsheets/d/([A-Za-z0-9_-]+)")

logger = logging.getLogger("en_tools_tracker")


class ToolsTrackerError(Exception):
    """Base class for errors raised by this script."""


class InputDataError(ToolsTrackerError):
    """The input spreadsheet could not be read or has the wrong columns."""


class SchemaError(ToolsTrackerError):
    """The PDS version or schema file is unusable."""


class ExistingResourceError(ToolsTrackerError):
    """An existing label in the output directory is unusable."""


class InteractionError(ToolsTrackerError):
    """A decision is needed from the user but stdin is not interactive."""


class RowError(ToolsTrackerError):
    """A single spreadsheet row cannot be turned into a label."""


class Outcome(enum.Enum):
    CREATED = "created"
    UPDATED = "updated"
    UNCHANGED = "unchanged"
    DECLINED = "declined"
    FAILED = "failed"


@dataclass(frozen=True)
class SchemaSettings:
    """Schema name (without extension) and information model version."""

    name: str
    information_model_version: str


@dataclass(frozen=True)
class ToolRecord:
    """One validated spreadsheet row."""

    name: str
    slug: str
    node: str
    url: str
    description: str
    applicable_to_all: bool
    release_date: str
    resource_types: tuple[str, ...]
    resource_subtypes: tuple[str, ...]
    interface_types: tuple[str, ...]
    references: tuple[tuple[str, str], ...]  # (lid, referenced product type)

    @property
    def lid(self) -> str:
        return f"{RESOURCE_LID_PREFIX}{self.slug}"

    @property
    def node_lid(self) -> str:
        return f"{NODE_LID_PREFIX}{NODE_LIDS[self.node]}"


@dataclass
class ExistingResource:
    """A label already present in the output directory."""

    path: Path
    root: ET.Element
    version_id: str


# --------------------------------------------------------------------------
# Input
# --------------------------------------------------------------------------


def google_sheet_csv_url(url: str) -> str:
    """Return the CSV export URL for a Google Sheets URL.

    The ``gid`` of the sheet tab, if any, is preserved so the tab the user
    pointed at is the one exported. Other URLs are returned unchanged.
    """
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc != "docs.google.com":
        return url
    match = GOOGLE_SHEET_ID_PATTERN.search(parsed.path)
    if not match:
        return url

    query = {"format": "csv"}
    for params in (parsed.query, parsed.fragment):
        gid = urllib.parse.parse_qs(params).get("gid")
        if gid:
            query["gid"] = gid[0]
            break
    export_url = f"https://docs.google.com/spreadsheets/d/{match.group(1)}/export"
    return f"{export_url}?{urllib.parse.urlencode(query)}"


def fetch_text(url: str) -> str:
    """Download a text document over HTTP(S)."""
    try:
        with urllib.request.urlopen(url, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            return response.read().decode("utf-8-sig")
    except (urllib.error.URLError, TimeoutError, UnicodeDecodeError) as err:
        raise InputDataError(f"Unable to fetch {url}: {err}") from err


def load_rows(source: str) -> list[dict[str, str]]:
    """Read the spreadsheet rows from a URL, CSV file or TSV file."""
    is_url = source.lower().startswith(("http://", "https://"))
    if is_url:
        text = fetch_text(google_sheet_csv_url(source))
        delimiter = ","
    else:
        path = Path(source)
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeDecodeError) as err:
            raise InputDataError(f"Unable to read {path}: {err}") from err
        delimiter = "\t" if path.suffix.lower() in {".tsv", ".tab"} else ","

    reader = csv.DictReader(
        io.StringIO(text, newline=""), delimiter=delimiter, restval=""
    )
    if reader.fieldnames is None:
        raise InputDataError("Input data is empty.")
    reader.fieldnames = [name.strip() for name in reader.fieldnames]

    missing = [h for h in REQUIRED_HEADERS if h not in reader.fieldnames]
    if missing:
        hint = (
            " Check that the Google Sheet is shared with 'anyone with the link'."
            if is_url
            else ""
        )
        raise InputDataError(
            f"Input data is missing required column headers: {missing}.{hint}"
        )
    return list(reader)


# --------------------------------------------------------------------------
# Schema settings
# --------------------------------------------------------------------------


def derive_information_model_version(pds_version: str) -> str:
    """Convert a version such as ``1R00`` into ``1.27.0.0``.

    The second character is a digit, or a letter where ``A`` means 10.
    """
    match = PDS_VERSION_PATTERN.fullmatch(pds_version)
    if not match:
        raise SchemaError(
            f"Invalid --pds-version '{pds_version}': expected a digit, a digit or "
            "capital letter, and two digits (e.g. 1R00)."
        )
    major, minor, patch, build = match.groups()
    if minor.isalpha():
        minor = str(ord(minor) - ord("A") + 10)
    return f"{major}.{minor}.{patch}.{build}"


def parse_schema_info(schema_path: Path) -> tuple[str, str]:
    """Return the schema name and ``version`` attribute of an XSD file."""
    try:
        root = ET.parse(schema_path).getroot()
    except (OSError, ET.ParseError) as err:
        raise SchemaError(f"Unable to read schema file '{schema_path}': {err}") from err

    version = root.get("version")
    if not version:
        raise SchemaError(
            f"Could not find 'version' attribute in schema file '{schema_path}'"
        )
    return schema_path.stem, version


def resolve_schema(pds_version: str, schema_path: Path | None) -> SchemaSettings:
    """Combine ``--pds-version`` and ``--schema`` into the settings to use."""
    pds_version = pds_version.upper()
    name = f"PDS4_PDS_{pds_version}"
    model_version = derive_information_model_version(pds_version)
    if schema_path is not None:
        name, model_version = parse_schema_info(schema_path)
    return SchemaSettings(name, model_version)


# --------------------------------------------------------------------------
# Spreadsheet rows
# --------------------------------------------------------------------------


def split_values(value: str, delimiter: str) -> tuple[str, ...]:
    """Split a multi-valued cell, dropping blank entries."""
    return tuple(part.strip() for part in value.split(delimiter) if part.strip())


def make_slug(name: str) -> str:
    """Build the lowercase identifier fragment for a tool name."""
    return re.sub(r"[^a-z0-9._-]", "", name.lower().replace(" ", "_"))


def reference_product_type(lid: str) -> str | None:
    """Return the referenced product type, or None if ``lid`` is not usable.

    Context products give their own type (``instrument``, ``investigation``...)
    and any other LID with the ``urn:<agency>:<archive>:<name>`` shape is a
    bundle.
    """
    match = CONTEXT_LID_PATTERN.fullmatch(lid)
    if match:
        return match.group("product_type")
    if BUNDLE_LID_PATTERN.fullmatch(lid):
        return "bundle"
    return None


def is_blank_row(row: Mapping[str, str]) -> bool:
    """True when every column the script reads is empty."""
    return not any((row.get(header) or "").strip() for header in REQUIRED_HEADERS)


def parse_record(row: Mapping[str, str]) -> ToolRecord:
    """Validate one spreadsheet row. Raises RowError describing every problem."""

    def cell(column: str) -> str:
        return (row.get(column) or "").strip()

    name = cell("Tool / Service Name")
    node = cell("node / org").lower()
    url = cell("URL")
    description = cell("Description")
    applicable = cell("Applicable to All PDS4 Data?")
    resource_types = split_values(cell("Resource Type"), ",")

    required = {
        "Tool / Service Name": name,
        "node / org": node,
        "URL": url,
        "Resource Type": resource_types,
        "Description": description,
        "Applicable to All PDS4 Data?": applicable,
    }
    problems = []
    missing = [column for column, value in required.items() if not value]
    if missing:
        problems.append(f"missing required field(s): {', '.join(missing)}")

    node = NODE_ALIASES.get(node, node)
    if node and node not in NODE_LIDS:
        problems.append(
            f"unknown 'node / org' value '{node}' "
            f"(known: {', '.join(sorted(NODE_LIDS))})"
        )

    slug = make_slug(name)
    if name and not slug:
        problems.append("'Tool / Service Name' has no usable LID characters")

    references = []
    for lid in split_values(cell("Internal Reference"), ";"):
        product_type = reference_product_type(lid)
        if product_type:
            references.append((lid, product_type))
        else:
            problems.append(f"'Internal Reference' value '{lid}' is not a valid LID")

    if problems:
        raise RowError("; ".join(problems))

    return ToolRecord(
        name=name,
        slug=slug,
        node=node,
        url=url,
        description=description,
        applicable_to_all=applicable.lower() in TRUE_VALUES,
        release_date=cell("Release Date"),
        resource_types=resource_types,
        resource_subtypes=split_values(cell("Resource Subtype"), ","),
        interface_types=split_values(cell("Interface Type"), ","),
        references=tuple(references),
    )


# --------------------------------------------------------------------------
# XML construction
# --------------------------------------------------------------------------


def pds_tag(name: str) -> str:
    """Qualify an element name with the PDS namespace."""
    return f"{{{PDS_NS}}}{name}"


def add_element(parent: ET.Element, name: str, text: str) -> ET.Element:
    element = ET.SubElement(parent, pds_tag(name))
    element.text = text
    return element


def modification_detail(
    version_id: str, description: str, mod_date: str | None = None
) -> ET.Element:
    """Build a Modification_Detail element."""
    detail = ET.Element(pds_tag("Modification_Detail"))
    add_element(detail, "modification_date", mod_date or date.today().isoformat())
    add_element(detail, "version_id", version_id)
    add_element(detail, "description", description)
    return detail


def build_resource(
    record: ToolRecord,
    schema: SchemaSettings,
    version_id: str,
    history: Sequence[ET.Element],
) -> ET.Element:
    """Build a Product_Resource element tree for a record."""
    root = ET.Element(
        pds_tag("Product_Resource"),
        {
            f"{{{XSI_NS}}}schemaLocation": (
                f"{PDS_NS} {SCHEMA_BASE_URL}/{schema.name}.xsd"
            )
        },
    )

    ident = ET.SubElement(root, pds_tag("Identification_Area"))
    add_element(ident, "logical_identifier", record.lid)
    add_element(ident, "version_id", version_id)
    add_element(ident, "title", record.name)
    add_element(ident, "information_model_version", schema.information_model_version)
    add_element(ident, "product_class", "Product_Resource")
    mod_history = ET.SubElement(ident, pds_tag("Modification_History"))
    mod_history.extend(history)

    archive = ET.SubElement(root, pds_tag("Archive_Resource"))
    add_element(archive, "name", record.name)
    add_element(archive, "version_id", "1.0")
    add_element(archive, "url", record.url)
    if record.release_date:
        add_element(archive, "release_date", record.release_date)
    for resource_type in record.resource_types:
        add_element(archive, "resource_type", resource_type)
    for subtype in record.resource_subtypes:
        add_element(archive, "resource_subtype", subtype)
    for interface_type in record.interface_types:
        add_element(archive, "interface_type", interface_type)
    add_element(
        archive,
        "pds4_wide_applicability_flag",
        "true" if record.applicable_to_all else "false",
    )
    add_element(archive, "description", record.description)

    references = ET.SubElement(root, pds_tag("Reference_List"))
    # The node comes first; a repeated LID is only referenced once.
    reference_targets = {record.node_lid: "node"}
    for lid, product_type in record.references:
        reference_targets.setdefault(lid, product_type)
    for lid, product_type in reference_targets.items():
        reference = ET.SubElement(references, pds_tag("Internal_Reference"))
        add_element(reference, "lid_reference", lid)
        add_element(reference, "reference_type", f"service_to_{product_type}")

    return root


def pretty_xml(root: ET.Element) -> str:
    """Serialize an element tree with indentation, without a prolog."""
    clone = copy.deepcopy(root)
    ET.indent(clone, space=INDENT)
    return ET.tostring(clone, encoding="unicode")


def render_label(root: ET.Element, schema: SchemaSettings) -> str:
    """Serialize a Product_Resource with its XML declaration and schematron."""
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<?xml-model href="{SCHEMA_BASE_URL}/{schema.name}.sch" '
        f'schematypens="{SCHEMATRON_NS}"?>\n'
        f"{pretty_xml(root)}\n"
    )


# --------------------------------------------------------------------------
# Comparison and versioning
# --------------------------------------------------------------------------


def identification_area(root: ET.Element) -> ET.Element:
    ident = root.find(pds_tag("Identification_Area"))
    if ident is None:
        raise ExistingResourceError("Product has no Identification_Area")
    return ident


def without_history(root: ET.Element) -> ET.Element:
    """Return a copy of the tree with the Modification_History removed."""
    clone = copy.deepcopy(root)
    ident = identification_area(clone)
    for history in ident.findall(pds_tag("Modification_History")):
        ident.remove(history)
    return clone


def comparable_form(root: ET.Element) -> str:
    """Canonical XML of a label, ignoring its version and history."""
    clone = without_history(root)
    version = identification_area(clone).find(pds_tag("version_id"))
    if version is not None:
        version.text = ""
    return ET.canonicalize(ET.tostring(clone, encoding="unicode"), strip_text=True)


def bump_minor_version(version_id: str) -> str:
    """Increment the minor part of a version, e.g. ``1.0`` -> ``1.1``."""
    match = VERSION_ID_PATTERN.fullmatch(version_id)
    if not match:
        raise ExistingResourceError(
            f"Cannot bump version_id '{version_id}': expected <major>.<minor>"
        )
    major, minor = match.groups()
    return f"{major}.{int(minor) + 1}"


def format_diff(
    old_root: ET.Element, new_root: ET.Element, old_name: str, new_name: str
) -> str:
    """Unified diff of two labels, ignoring the modification history."""
    old_lines = pretty_xml(without_history(old_root)).splitlines(keepends=True)
    new_lines = pretty_xml(without_history(new_root)).splitlines(keepends=True)
    return "".join(
        difflib.unified_diff(old_lines, new_lines, fromfile=old_name, tofile=new_name)
    )


# --------------------------------------------------------------------------
# Output directory
# --------------------------------------------------------------------------


def load_existing(output_dir: Path) -> dict[str, ExistingResource]:
    """Index the labels in ``output_dir`` by logical identifier."""
    existing: dict[str, ExistingResource] = {}
    if not output_dir.is_dir():
        return existing

    for path in sorted(output_dir.glob("*.xml")):
        try:
            root = ET.parse(path).getroot()
        except (OSError, ET.ParseError) as err:
            raise ExistingResourceError(f"Unable to read {path}: {err}") from err
        if root.tag != pds_tag("Product_Resource"):
            continue

        ident = identification_area(root)
        lid = (ident.findtext(pds_tag("logical_identifier")) or "").strip()
        version_id = (ident.findtext(pds_tag("version_id")) or "").strip()
        if not lid or not version_id:
            raise ExistingResourceError(
                f"{path} lacks a logical_identifier or version_id"
            )
        if lid in existing:
            raise ExistingResourceError(
                f"{existing[lid].path.name} and {path.name} share the LID {lid}"
            )
        existing[lid] = ExistingResource(path, root, version_id)
    return existing


def write_new_label(path: Path, content: str) -> None:
    """Write a label, refusing to overwrite an existing file."""
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(content)
    except OSError as err:
        raise ExistingResourceError(f"Unable to write {path}: {err}") from err


def ask(prompt: str) -> str:
    """Read a line from the user; fails clearly when stdin is not interactive."""
    try:
        return input(prompt).strip()
    except EOFError as err:
        raise InteractionError(
            "An existing label differs from the spreadsheet and needs a "
            "decision, but no input is available. Run interactively."
        ) from err


def confirm(prompt: str) -> bool:
    return ask(prompt).lower() in {"y", "yes"}


def previous_history(old_root: ET.Element) -> list[ET.Element]:
    """Copy the Modification_Detail entries of an existing label."""
    details = identification_area(old_root).findall(
        f"{pds_tag('Modification_History')}/{pds_tag('Modification_Detail')}"
    )
    if details:
        return [copy.deepcopy(detail) for detail in details]
    return [modification_detail("1.0", "Initial version.")]


def update_existing(
    record: ToolRecord,
    schema: SchemaSettings,
    output_dir: Path,
    current: ExistingResource,
) -> ExistingResource | None:
    """Offer to replace an existing label. Returns None if declined."""
    new_version = bump_minor_version(current.version_id)
    new_path = output_dir / f"{record.node}_{record.slug}_v{new_version}.xml"

    proposed = build_resource(record, schema, new_version, [])
    print(f"\n--- Differences for {current.path.name} vs {new_path.name} ---")
    print(format_diff(current.root, proposed, current.path.name, new_path.name))
    print("-" * 50)

    question = f"Replace old file '{current.path.name}' with '{new_path.name}'? [y/N]: "
    if not confirm(question):
        return None
    change = ask("Enter description of change [Updated resource details.]: ")
    history = [modification_detail(new_version, change or "Updated resource details.")]
    history.extend(previous_history(current.root))

    updated = build_resource(record, schema, new_version, history)
    write_new_label(new_path, render_label(updated, schema))
    retired_path = current.path.with_name(f"{current.path.name}.DELETED")
    try:
        current.path.rename(retired_path)
    except OSError as err:
        new_path.unlink()
        raise ExistingResourceError(f"Unable to rename {current.path}: {err}") from err
    logger.info(
        "Updated: '%s' marked as .DELETED, created '%s'",
        current.path.name,
        new_path.name,
    )
    return ExistingResource(new_path, updated, new_version)


def process_record(
    record: ToolRecord,
    schema: SchemaSettings,
    output_dir: Path,
    existing: dict[str, ExistingResource],
) -> Outcome:
    """Create, update or leave alone the label for one record."""
    candidate = build_resource(
        record, schema, "1.0", [modification_detail("1.0", "Initial version.")]
    )
    current = existing.get(record.lid)

    if current is None:
        path = output_dir / f"{record.node}_{record.slug}_v1.0.xml"
        write_new_label(path, render_label(candidate, schema))
        existing[record.lid] = ExistingResource(path, candidate, "1.0")
        return Outcome.CREATED

    if comparable_form(current.root) == comparable_form(candidate):
        logger.info("No changes for file %s", current.path.name)
        return Outcome.UNCHANGED

    replacement = update_existing(record, schema, output_dir, current)
    if replacement is None:
        logger.info("Skipped updating '%s'", current.path.name)
        return Outcome.DECLINED
    existing[record.lid] = replacement
    return Outcome.UPDATED


# --------------------------------------------------------------------------
# Command line
# --------------------------------------------------------------------------


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate PDS4 Product_Resource labels from a Google Sheet or a "
            "local CSV/TSV file."
        ),
    )
    parser.add_argument(
        "input_file",
        help="Path to a local CSV/TSV file or a Google Sheets URL.",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory for XML files (default: %(default)s)",
    )
    parser.add_argument(
        "-x",
        "--schema",
        type=Path,
        help="Path to the schema XSD file (e.g. PDS4_PDS_1R00.xsd)",
    )
    parser.add_argument(
        "--pds-version",
        default=DEFAULT_PDS_VERSION,
        help="PDS version string (default: %(default)s)",
    )
    return parser.parse_args(argv)


def run(args: argparse.Namespace) -> int:
    """Generate the labels. Returns the process exit status."""
    schema = resolve_schema(args.pds_version, args.schema)
    rows = load_rows(args.input_file)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    existing = load_existing(args.output_dir)

    outcomes: Counter[Outcome] = Counter()
    seen_rows: dict[str, int] = {}
    for row_number, row in enumerate(rows, start=2):  # row 1 is the header
        if is_blank_row(row):
            continue
        label = f"Row {row_number}"
        try:
            record = parse_record(row)
            label = f"'{record.name}' (row {row_number})"
            if record.lid in seen_rows:
                raise RowError(f"duplicates the LID of row {seen_rows[record.lid]}")
            seen_rows[record.lid] = row_number
            outcome = process_record(record, schema, args.output_dir, existing)
        except RowError as err:
            logger.error("%s: %s. Skipping.", label, err)
            outcome = Outcome.FAILED
        outcomes[outcome] += 1

    summary = ", ".join(f"{outcomes[o]} {o.value}" for o in Outcome)
    logger.info("Processing complete in '%s': %s", args.output_dir, summary)
    return 1 if outcomes[Outcome.FAILED] else 0


def main(argv: Sequence[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        return run(parse_args(argv))
    except ToolsTrackerError as err:
        logger.error("%s", err)
        return 2


if __name__ == "__main__":
    sys.exit(main())
