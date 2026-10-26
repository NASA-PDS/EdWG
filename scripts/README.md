# EdWG Scripts

Helper scripts for maintaining Editorial Working Group content. Each script is
a standalone command-line tool; this page documents how to run each one.

| Script | Purpose |
| ------ | ------- |
| [`en_tools_tracker.py`](#en_tools_trackerpy) | Generate PDS4 `Product_Resource` labels for PDS tools and services from a spreadsheet |

## en_tools_tracker.py

Reads a spreadsheet describing PDS tools and services and writes one PDS4
`Product_Resource` label per row. Each label has the logical identifier
`urn:nasa:pds:context:resource:<tool>` and is named
`<node>_<tool>_v<version>.xml`.

### Requirements

- Python 3.9 or later
- No third-party packages; the script uses only the Python standard library

### Input

The input is one of:

- a local `.csv` file
- a local `.tsv` (or `.tab`) file
- the URL of a Google Sheet that is shared with "anyone with the link"

For a Google Sheet, the tab named by the `gid` in the URL is used; without a
`gid`, the first tab is used. For an Excel workbook, export the tools tab
(for example, `Tools and Services`) as CSV and pass that file.

The first row must contain these column headers (column order does not matter):

| Column | Required | Notes |
| ------ | -------- | ----- |
| `node / org` | yes | One of the nodes listed [below](#nodes). `Community` is treated as `EN`. Lowercased for the file name. |
| `Tool / Service Name` | yes | Lowercased, spaces become `_`, other characters outside `a-z 0-9 . _ -` are dropped. |
| `URL` | yes | |
| `Release Date` | no | Written as-is (`YYYY-MM-DD`) when present; omitted when blank. |
| `Resource Type` | yes | Comma-separated for multiple values. |
| `Resource Subtype` | no | Comma-separated for multiple values. |
| `Interface Type` | no | Comma-separated for multiple values. |
| `Description` | yes | |
| `Internal Reference` | no | Semicolon-separated LIDs (see [References](#references)). |
| `Applicable to All PDS4 Data?` | yes | `yes`, `true`, `y` or `1` (any case) means true; anything else is false. |

Other columns, including `status` and `Version ID`, are not used. Every row is
processed regardless of its status.

Rows in which every column above is empty are ignored, so trailing blank rows in
a spreadsheet export are harmless. Rows with a missing required value, an
unknown node, an unusable tool name, a malformed `Internal Reference`, or a
logical identifier already used by an earlier row are reported and skipped; the
remaining rows are still processed.

#### Nodes

The `node / org` value selects the node's context product, which every label
references with reference type `service_to_node`:

| `node / org` | Node context product |
| ------------ | -------------------- |
| `ATM` | `urn:nasa:pds:context:node:node.atmos` |
| `EN`, `Community` | `urn:nasa:pds:context:node:node.en` |
| `GEO` | `urn:nasa:pds:context:node:node.geoscience` |
| `IMG` | `urn:nasa:pds:context:node:node.imaging` |
| `NAIF` | `urn:nasa:pds:context:node:node.naif` |
| `PPI` | `urn:nasa:pds:context:node:node.ppi-ucla` |
| `PSA` | `urn:nasa:pds:context:node:node.psa` |
| `RMS` | `urn:nasa:pds:context:node:node.rings` |
| `SBN` | `urn:nasa:pds:context:node:node.sbn` |

To support another node, add it to `NODE_LIDS` in `en_tools_tracker.py`.

#### References

Each `Internal Reference` LID adds a reference whose type depends on the LID:

| LID form | Reference type |
| -------- | -------------- |
| `urn:<agency>:<archive>:context:<type>:<name>` (any agency and archive, optionally with `::<version>`) | `service_to_<type>`, e.g. `service_to_instrument` |
| `urn:<agency>:<archive>:<name>` (a bundle) | `service_to_bundle` |

A LID that matches neither form causes the row to be skipped. A LID that
repeats, including the node's own LID, is referenced once.

### Usage

Run from the root of the repository.

```bash
INPUT_FILE="<path-to-tools.tsv>"
python3 scripts/en_tools_tracker.py "${INPUT_FILE}"
```

From a Google Sheet. Quote the URL so the shell does not interpret `&` or `#`:

```bash
SHEET_URL="<google-sheet-url>"
python3 scripts/en_tools_tracker.py "${SHEET_URL}"
```

To choose the output directory and schema:

```bash
INPUT_FILE="<path-to-tools.tsv>"
OUTPUT_DIR="<output-directory>"
SCHEMA_FILE="<path-to-PDS4_PDS_1R00.xsd>"
python3 scripts/en_tools_tracker.py "${INPUT_FILE}" -o "${OUTPUT_DIR}" -x "${SCHEMA_FILE}"
```

### Options

| Option | Default | Description |
| ------ | ------- | ----------- |
| `input_file` | | Local CSV/TSV file or Google Sheets URL (required). |
| `-o`, `--output-dir` | `toolsResources` | Directory for the generated labels. It is created if it does not exist. |
| `--pds-version` | `1R00` | PDS4 information model version in the `1R00` form. Sets the schema and schematron file names and the `information_model_version` (`1R00` is `1.27.0.0`). |
| `-x`, `--schema` | | Path to a PDS4 schema `.xsd`. Its file name replaces `PDS4_PDS_<pds-version>` in the schema references and its `version` attribute becomes the `information_model_version`. |

### Updating existing labels

If the output directory already contains a label with the same logical
identifier, the script compares it with the label it would generate, ignoring
the `version_id` and the `Modification_History`:

- **No differences:** an info message is printed and the file is left alone.
  Re-running with unchanged data never creates a new version.
- **Differences:** a diff is printed and the script asks whether to replace the
  old label.
  - Answering `y` prompts for a change description, then writes a new label with
    the minor version incremented (`1.0` to `1.1`) and a new
    `Modification_Detail` entry ahead of the earlier history. The old label is
    renamed with a `.DELETED` suffix.
  - Any other answer leaves the old label in place.

Labels in the output directory that are not `Product_Resource` products are
ignored. An unreadable or malformed `.xml` file in the output directory stops
the run.

### Exit status

| Status | Meaning |
| ------ | ------- |
| `0` | Every row was processed (created, updated, unchanged, or declined). |
| `1` | One or more rows were skipped because of errors. |
| `2` | The run could not start or continue (unreadable input, missing column headers, invalid `--pds-version` or `--schema`, unreadable output directory, or a changed label that needs a decision when no terminal input is available). |

### Testing

The tests use only the Python standard library and need no network access. Run
them from the root of the repository:

```bash
python3 -m unittest discover -s scripts/tests -v
```

They cover input parsing, label contents, the update workflow, and error
handling, and compare one generated label with a reviewed copy in
`scripts/tests/data/expected/`. The fixture `scripts/tests/data/sample_register.csv`
has the same layout as the tools register, including blank rows, extra columns,
non-NASA and bundle LIDs, special characters, and rows that must be rejected.

One test also validates every generated label against the PDS4 schema. It is
skipped unless `xmllint` is installed and `PDS4_PDS_XSD` names a
`PDS4_PDS_1R00.xsd` that includes `pds4_wide_applicability_flag`:

```bash
PDS4_PDS_XSD="<path-to-PDS4_PDS_1R00.xsd>"
export PDS4_PDS_XSD
python3 -m unittest discover -s scripts/tests -v
```

To check a real register end to end, generate the labels into a scratch
directory and validate them:

```bash
INPUT_FILE="<path-to-register.csv>"
SCRATCH_DIR="$(mktemp -d)"
SCHEMA_FILE="<path-to-PDS4_PDS_1R00.xsd>"
python3 scripts/en_tools_tracker.py "${INPUT_FILE}" -o "${SCRATCH_DIR}"
for label in "${SCRATCH_DIR}"/*.xml; do
    xmllint --noout --schema "${SCHEMA_FILE}" "${label}" || echo "INVALID: ${label}"
done
```

### Troubleshooting

- **Missing column headers for a Google Sheet:** the sheet is probably not shared
  with "anyone with the link", so the export returned a sign-in page instead of
  CSV.
- **`CERTIFICATE_VERIFY_FAILED` when fetching a Google Sheet:** the Python
  installation lacks the system CA certificates. Fix the installation rather
  than disabling verification: with the python.org installer on macOS, run the
  bundled `Install Certificates.command`; with Homebrew, reinstall Python with
  `brew reinstall python`.
