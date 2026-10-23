"""Tests for enToolsTracker.py.

Run from the repository root:

    python3 -m unittest discover -s scripts/tests -v

The tests need no network access. Schema validation of the generated labels
runs only when ``xmllint`` is installed and PDS4_PDS_XSD names a PDS4_PDS_1R00
schema file; otherwise that test is skipped.
"""
from __future__ import annotations

import contextlib
import csv
import datetime
import io
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest import mock

TESTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS_DIR.parent))

import enToolsTracker as ett  # noqa: E402

SAMPLE_REGISTER = TESTS_DIR / "data" / "sample_register.csv"
EXPECTED_DIR = TESTS_DIR / "data" / "expected"
PDS_NS = "{http://pds.nasa.gov/pds4/pds/v1}"
HEADERS = ["status", *ett.REQUIRED_HEADERS]


class FixedDate:
    """Stand-in for datetime.date with a constant today()."""

    @staticmethod
    def today() -> datetime.date:
        return datetime.date(2026, 1, 15)


def make_row(**overrides: str) -> dict[str, str]:
    """A complete, valid spreadsheet row, with selected cells replaced."""
    row = {
        "status": "ToDo",
        "node / org": "RMS",
        "Tool / Service Name": "Example Tool",
        "URL": "https://tool.example.org/",
        "Release Date": "",
        "Resource Type": "Service",
        "Resource Subtype": "",
        "Interface Type": "",
        "Description": "An example tool.",
        "Internal Reference": "",
        "Applicable to All PDS4 Data?": "False",
    }
    row.update(overrides)
    return row


class WorkDirTestCase(unittest.TestCase):
    """Provides a scratch directory and helpers for running the tool."""

    def setUp(self) -> None:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.out = self.tmp / "out"
        patcher = mock.patch.object(ett, "date", FixedDate)
        patcher.start()
        self.addCleanup(patcher.stop)

    def write_sheet(self, *rows: dict[str, str], name: str = "sheet.csv") -> Path:
        path = self.tmp / name
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(rows)
        return path

    def run_tool(self, sheet: Path, *extra: str, answers: tuple[str, ...] = ()) -> int:
        """Run the tool, answering prompts with ``answers``; returns the status."""
        args = ett.parse_args([str(sheet), "-o", str(self.out), *extra])
        with mock.patch("builtins.input", side_effect=list(answers)):
            with contextlib.redirect_stdout(io.StringIO()):
                with self.assertLogs(ett.logger, level="INFO"):
                    return ett.run(args)

    def labels(self) -> list[str]:
        return sorted(path.name for path in self.out.iterdir())

    def parse(self, filename: str) -> ET.Element:
        return ET.parse(self.out / filename).getroot()


class GoogleSheetUrlTests(unittest.TestCase):
    BASE = "https://docs.google.com/spreadsheets/d/SHEET_ID/export"

    def test_gid_in_query_is_kept(self):
        url = "https://docs.google.com/spreadsheets/d/SHEET_ID/edit?gid=42"
        self.assertEqual(ett.google_sheet_csv_url(url), f"{self.BASE}?format=csv&gid=42")

    def test_gid_in_fragment_is_kept(self):
        url = "https://docs.google.com/spreadsheets/d/SHEET_ID/edit?usp=sharing#gid=7"
        self.assertEqual(ett.google_sheet_csv_url(url), f"{self.BASE}?format=csv&gid=7")

    def test_no_gid_exports_first_tab(self):
        url = "https://docs.google.com/spreadsheets/d/SHEET_ID/edit"
        self.assertEqual(ett.google_sheet_csv_url(url), f"{self.BASE}?format=csv")

    def test_other_urls_are_unchanged(self):
        url = "https://example.org/tools.csv"
        self.assertEqual(ett.google_sheet_csv_url(url), url)


class VersionTests(unittest.TestCase):
    def test_information_model_version(self):
        cases = {"1R00": "1.27.0.0", "1G00": "1.16.0.0", "1A00": "1.10.0.0", "1900": "1.9.0.0"}
        for pds_version, expected in cases.items():
            with self.subTest(pds_version):
                self.assertEqual(ett.derive_information_model_version(pds_version), expected)

    def test_invalid_pds_version(self):
        for bad in ("1R0", "1r00", "", "1RR00", "XR00"):
            with self.subTest(bad), self.assertRaises(ett.SchemaError):
                ett.derive_information_model_version(bad)

    def test_bump_minor_version(self):
        self.assertEqual(ett.bump_minor_version("1.0"), "1.1")
        self.assertEqual(ett.bump_minor_version("1.9"), "1.10")
        self.assertEqual(ett.bump_minor_version("2.3"), "2.4")

    def test_bump_rejects_malformed_version(self):
        for bad in ("abc", "1", "1.0.0", ""):
            with self.subTest(bad), self.assertRaises(ett.ExistingResourceError):
                ett.bump_minor_version(bad)


class ReferenceTests(unittest.TestCase):
    def test_context_lids_of_any_archive(self):
        cases = {
            "urn:nasa:pds:context:instrument:mro.hirise": "instrument",
            "urn:esa:psa:context:instrument_host:spacecraft.mex": "instrument_host",
            "urn:isro:isda:context:investigation:mission.ch1": "investigation",
            "urn:kari:kpds:context:investigation:mission.kplo": "investigation",
            "urn:nasa:pds:context:target:satellite.earth.moon": "target",
            "urn:nasa:pds:context:instrument:mro.hirise::1.0": "instrument",
        }
        for lid, expected in cases.items():
            with self.subTest(lid):
                self.assertEqual(ett.reference_product_type(lid), expected)

    def test_bundle_lids(self):
        self.assertEqual(ett.reference_product_type("urn:nasa:pds:relab"), "bundle")
        self.assertEqual(ett.reference_product_type("urn:nasa:pds:relab::2.0"), "bundle")

    def test_invalid_lids(self):
        for bad in ("urn:bogus", "not-a-lid", "urn:nasa:pds", "urn:nasa:pds:context:x"):
            with self.subTest(bad):
                self.assertIsNone(ett.reference_product_type(bad))


class ParseRecordTests(unittest.TestCase):
    def test_valid_row(self):
        record = ett.parse_record(
            make_row(
                **{
                    "Tool / Service Name": "My Tool (v2)",
                    "Resource Type": "Library, Service",
                    "Resource Subtype": "Search Tool,",
                    "Interface Type": "REST API",
                    "Release Date": "2024-05-01",
                    "Applicable to All PDS4 Data?": "YES",
                }
            )
        )
        self.assertEqual(record.slug, "my_tool_v2")
        self.assertEqual(record.lid, "urn:nasa:pds:context:resource:my_tool_v2")
        self.assertEqual(record.resource_types, ("Library", "Service"))
        self.assertEqual(record.resource_subtypes, ("Search Tool",))
        self.assertEqual(record.interface_types, ("REST API",))
        self.assertEqual(record.release_date, "2024-05-01")
        self.assertTrue(record.applicable_to_all)

    def test_applicability_values(self):
        for value, expected in (("True", True), ("y", True), ("1", True),
                                ("False", False), ("no", False), ("maybe", False)):
            with self.subTest(value):
                row = make_row(**{"Applicable to All PDS4 Data?": value})
                self.assertEqual(ett.parse_record(row).applicable_to_all, expected)

    def test_status_is_ignored(self):
        for status in ("", "Example", "Done - GitHub", "ToDo", "anything"):
            with self.subTest(status):
                self.assertEqual(ett.parse_record(make_row(status=status)).slug, "example_tool")

    def test_node_lids(self):
        cases = {
            "RMS": "node.rings", "GEO": "node.geoscience", "IMG": "node.imaging",
            "NAIF": "node.naif", "PPI": "node.ppi-ucla", "SBN": "node.sbn",
            "EN": "node.en", "Community": "node.en",
        }
        for node, suffix in cases.items():
            with self.subTest(node):
                record = ett.parse_record(make_row(**{"node / org": node}))
                self.assertEqual(record.node_lid, f"urn:nasa:pds:context:node:{suffix}")

    def test_community_files_use_en_prefix(self):
        self.assertEqual(ett.parse_record(make_row(**{"node / org": "Community"})).node, "en")

    def test_unknown_node_is_rejected(self):
        with self.assertRaisesRegex(ett.RowError, "unknown 'node / org'"):
            ett.parse_record(make_row(**{"node / org": "PDS/SBN"}))

    def test_all_missing_fields_are_reported(self):
        row = make_row(
            **{"Tool / Service Name": "", "URL": "", "Description": "",
               "Resource Type": " , ", "Applicable to All PDS4 Data?": ""}
        )
        with self.assertRaises(ett.RowError) as caught:
            ett.parse_record(row)
        message = str(caught.exception)
        for column in ("Tool / Service Name", "URL", "Description", "Resource Type",
                       "Applicable to All PDS4 Data?"):
            self.assertIn(column, message)

    def test_name_without_usable_characters(self):
        with self.assertRaisesRegex(ett.RowError, "no usable LID characters"):
            ett.parse_record(make_row(**{"Tool / Service Name": "!!!"}))

    def test_invalid_reference_is_rejected(self):
        with self.assertRaisesRegex(ett.RowError, "urn:bogus"):
            ett.parse_record(make_row(**{"Internal Reference": "urn:bogus"}))

    def test_literal_na_and_none_are_kept(self):
        record = ett.parse_record(
            make_row(**{"Tool / Service Name": "NA", "Description": "None"})
        )
        self.assertEqual((record.name, record.description), ("NA", "None"))

    def test_blank_rows(self):
        self.assertTrue(ett.is_blank_row({}))
        self.assertTrue(ett.is_blank_row({"status": "ToDo", "URL": "  ", "Version ID": "9"}))
        self.assertFalse(ett.is_blank_row({"URL": "https://x.example"}))


class LoadRowsTests(WorkDirTestCase):
    def test_bom_and_padded_headers(self):
        path = self.tmp / "bom.csv"
        header = ",".join(f" {h} " for h in HEADERS)
        path.write_bytes(f"\ufeff{header}\n".encode("utf-8"))
        self.assertEqual(ett.load_rows(str(path)), [])

    def test_tsv_is_split_on_tabs(self):
        path = self.tmp / "tools.tsv"
        path.write_text("\t".join(HEADERS) + "\n" + "\t".join(make_row().values()) + "\n")
        (row,) = ett.load_rows(str(path))
        self.assertEqual(row["Tool / Service Name"], "Example Tool")

    def test_extra_columns_are_ignored(self):
        rows = ett.load_rows(str(SAMPLE_REGISTER))
        self.assertEqual(len(rows), 7)

    def test_missing_headers(self):
        path = self.tmp / "bad.csv"
        path.write_text("a,b\n1,2\n")
        with self.assertRaisesRegex(ett.InputDataError, "missing required column headers"):
            ett.load_rows(str(path))

    def test_empty_file(self):
        path = self.tmp / "empty.csv"
        path.write_text("")
        with self.assertRaises(ett.InputDataError):
            ett.load_rows(str(path))

    def test_missing_file(self):
        with self.assertRaises(ett.InputDataError):
            ett.load_rows(str(self.tmp / "absent.csv"))


class BuildResourceTests(unittest.TestCase):
    SCHEMA = ett.SchemaSettings("PDS4_PDS_1R00", "1.27.0.0")

    def build(self, **overrides: str) -> ET.Element:
        record = ett.parse_record(make_row(**overrides))
        history = [ett.modification_detail("1.0", "Initial version.", "2026-01-15")]
        return ett.build_resource(record, self.SCHEMA, "1.0", history)

    def test_special_characters_are_escaped_and_round_trip(self):
        description = 'R&D <b>"quoted"</b> & more'
        root = self.build(Description=description, URL="https://x.example/?a=1&b=2")
        reparsed = ET.fromstring(ett.render_label(root, self.SCHEMA))
        archive = reparsed.find(f"{PDS_NS}Archive_Resource")
        self.assertEqual(archive.findtext(f"{PDS_NS}description"), description)
        self.assertEqual(archive.findtext(f"{PDS_NS}url"), "https://x.example/?a=1&b=2")

    def test_release_date_only_when_present(self):
        tag = f"{PDS_NS}Archive_Resource/{PDS_NS}release_date"
        self.assertIsNone(self.build().find(tag))
        self.assertEqual(self.build(**{"Release Date": "2024-05-01"}).findtext(tag), "2024-05-01")

    def test_archive_resource_element_order(self):
        root = self.build(
            **{"Release Date": "2024-05-01", "Resource Type": "Library, Service",
               "Resource Subtype": "Search Tool", "Interface Type": "REST API"}
        )
        archive = root.find(f"{PDS_NS}Archive_Resource")
        self.assertEqual(
            [child.tag.removeprefix(PDS_NS) for child in archive],
            ["name", "version_id", "url", "release_date", "resource_type", "resource_type",
             "resource_subtype", "interface_type", "pds4_wide_applicability_flag", "description"],
        )

    def test_node_reference_first_and_not_repeated(self):
        node_lid = "urn:nasa:pds:context:node:node.rings"
        root = self.build(
            **{"Internal Reference": f"{node_lid};urn:nasa:pds:context:instrument:mro.hirise;"
                                     "urn:nasa:pds:context:instrument:mro.hirise"}
        )
        references = [
            (ref.findtext(f"{PDS_NS}lid_reference"), ref.findtext(f"{PDS_NS}reference_type"))
            for ref in root.iter(f"{PDS_NS}Internal_Reference")
        ]
        self.assertEqual(
            references,
            [(node_lid, "service_to_node"),
             ("urn:nasa:pds:context:instrument:mro.hirise", "service_to_instrument")],
        )

    def test_comparison_ignores_version_and_history(self):
        record = ett.parse_record(make_row())
        first = ett.build_resource(
            record, self.SCHEMA, "1.0", [ett.modification_detail("1.0", "Initial version.")]
        )
        later = ett.build_resource(
            record, self.SCHEMA, "1.7",
            [ett.modification_detail("1.7", "Edited."), ett.modification_detail("1.0", "x")],
        )
        self.assertEqual(ett.comparable_form(first), ett.comparable_form(later))

    def test_comparison_detects_content_change(self):
        self.assertNotEqual(
            ett.comparable_form(self.build()),
            ett.comparable_form(self.build(Description="Different.")),
        )


class SampleRegisterTests(WorkDirTestCase):
    """End-to-end run on a register shaped like the real one."""

    def test_sample_register(self):
        status = self.run_tool(SAMPLE_REGISTER)

        # Two rows are bad (unknown node; duplicate LID), so the status is 1.
        self.assertEqual(status, 1)
        self.assertEqual(
            self.labels(),
            ["en_community_tool_v1.0.xml", "geo_na_v1.0.xml", "rms_example_viewer_v1.0.xml"],
        )

    def test_blank_rows_are_not_errors(self):
        with self.assertLogs(ett.logger, level="ERROR") as logs, \
                contextlib.redirect_stdout(io.StringIO()):
            ett.run(ett.parse_args([str(SAMPLE_REGISTER), "-o", str(self.out)]))
        errors = "\n".join(logs.output)
        self.assertIn("Row 7: unknown 'node / org'", errors)
        self.assertIn("duplicates the LID of row 2", errors)
        self.assertNotIn("Row 5", errors)
        self.assertNotIn("Row 6", errors)
        self.assertEqual(len(logs.output), 2)

    def test_matches_golden_label(self):
        self.run_tool(SAMPLE_REGISTER)
        name = "rms_example_viewer_v1.0.xml"
        self.assertEqual(
            (self.out / name).read_text(encoding="utf-8"),
            (EXPECTED_DIR / name).read_text(encoding="utf-8"),
        )

    def test_literal_na_row_is_generated(self):
        self.run_tool(SAMPLE_REGISTER)
        root = self.parse("geo_na_v1.0.xml")
        self.assertEqual(root.findtext(f"{PDS_NS}Identification_Area/{PDS_NS}title"), "NA")
        self.assertEqual(
            root.findtext(f"{PDS_NS}Archive_Resource/{PDS_NS}description"), "None"
        )

    def test_labels_are_well_formed_pds4_resources(self):
        self.run_tool(SAMPLE_REGISTER)
        for name in self.labels():
            with self.subTest(name):
                root = self.parse(name)
                self.assertEqual(root.tag, f"{PDS_NS}Product_Resource")
                lid = root.findtext(f"{PDS_NS}Identification_Area/{PDS_NS}logical_identifier")
                self.assertTrue(lid.startswith(ett.RESOURCE_LID_PREFIX))

    @unittest.skipUnless(
        shutil.which("xmllint") and os.environ.get("PDS4_PDS_XSD"),
        "set PDS4_PDS_XSD to a PDS4_PDS_1R00.xsd path and install xmllint",
    )
    def test_labels_validate_against_pds4_schema(self):
        self.run_tool(SAMPLE_REGISTER)
        for name in self.labels():
            with self.subTest(name):
                result = subprocess.run(
                    ["xmllint", "--noout", "--schema", os.environ["PDS4_PDS_XSD"],
                     str(self.out / name)],
                    capture_output=True, text=True, check=False,
                )
                self.assertEqual(result.returncode, 0, result.stderr)


class UpdateLifecycleTests(WorkDirTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.v1 = self.write_sheet(make_row(), name="v1.csv")
        self.v2 = self.write_sheet(make_row(Description="Reworded."), name="v2.csv")
        self.assertEqual(self.run_tool(self.v1), 0)

    def test_rerun_with_same_data_changes_nothing(self):
        before = (self.out / "rms_example_tool_v1.0.xml").read_bytes()
        self.assertEqual(self.run_tool(self.v1), 0)  # no prompt: input() is not answered
        self.assertEqual(self.labels(), ["rms_example_tool_v1.0.xml"])
        self.assertEqual((self.out / "rms_example_tool_v1.0.xml").read_bytes(), before)

    def test_accepted_update_bumps_version_and_keeps_history(self):
        self.assertEqual(self.run_tool(self.v2, answers=("y", "Reworded description")), 0)
        self.assertEqual(
            self.labels(), ["rms_example_tool_v1.0.xml.DELETED", "rms_example_tool_v1.1.xml"]
        )
        root = self.parse("rms_example_tool_v1.1.xml")
        ident = root.find(f"{PDS_NS}Identification_Area")
        self.assertEqual(ident.findtext(f"{PDS_NS}version_id"), "1.1")
        details = [
            (d.findtext(f"{PDS_NS}version_id"), d.findtext(f"{PDS_NS}description"))
            for d in ident.iter(f"{PDS_NS}Modification_Detail")
        ]
        self.assertEqual(details, [("1.1", "Reworded description"), ("1.0", "Initial version.")])
        self.assertEqual(
            root.findtext(f"{PDS_NS}Archive_Resource/{PDS_NS}description"), "Reworded."
        )

    def test_blank_change_description_uses_default(self):
        self.run_tool(self.v2, answers=("y", ""))
        ident = self.parse("rms_example_tool_v1.1.xml").find(f"{PDS_NS}Identification_Area")
        first = next(ident.iter(f"{PDS_NS}Modification_Detail"))
        self.assertEqual(first.findtext(f"{PDS_NS}description"), "Updated resource details.")

    def test_no_new_version_after_an_update_when_data_is_unchanged(self):
        self.run_tool(self.v2, answers=("y", "Reworded"))
        for _ in range(2):
            self.assertEqual(self.run_tool(self.v2), 0)  # would prompt if it saw a change
        self.assertEqual(
            self.labels(), ["rms_example_tool_v1.0.xml.DELETED", "rms_example_tool_v1.1.xml"]
        )

    def test_second_update_bumps_again(self):
        v3 = self.write_sheet(make_row(Description="Third."), name="v3.csv")
        self.run_tool(self.v2, answers=("y", "second"))
        self.run_tool(v3, answers=("y", "third"))
        self.assertIn("rms_example_tool_v1.2.xml", self.labels())

    def test_declined_update_leaves_files_alone(self):
        self.assertEqual(self.run_tool(self.v2, answers=("n",)), 0)
        self.assertEqual(self.labels(), ["rms_example_tool_v1.0.xml"])

    def test_update_without_terminal_input_fails_cleanly(self):
        args = ett.parse_args([str(self.v2), "-o", str(self.out)])
        with mock.patch("builtins.input", side_effect=EOFError), \
                contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(ett.InteractionError):
                ett.run(args)
        self.assertEqual(self.labels(), ["rms_example_tool_v1.0.xml"])

    def test_failed_rename_rolls_back_new_label(self):
        args = ett.parse_args([str(self.v2), "-o", str(self.out)])
        with mock.patch("builtins.input", side_effect=["y", "x"]), \
                mock.patch.object(Path, "rename", side_effect=OSError("denied")), \
                contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(ett.ExistingResourceError):
                ett.run(args)
        self.assertEqual(self.labels(), ["rms_example_tool_v1.0.xml"])

    def test_description_with_backslashes_and_markup_is_preserved(self):
        self.run_tool(self.v2, answers=("y", r"fixed C:\path \d & <b>"))
        ident = self.parse("rms_example_tool_v1.1.xml").find(f"{PDS_NS}Identification_Area")
        first = next(ident.iter(f"{PDS_NS}Modification_Detail"))
        self.assertEqual(first.findtext(f"{PDS_NS}description"), r"fixed C:\path \d & <b>")


class OutputDirectoryTests(WorkDirTestCase):
    def test_unrelated_xml_is_ignored(self):
        self.out.mkdir()
        (self.out / "other.xml").write_text("<Other/>")
        self.assertEqual(self.run_tool(self.write_sheet(make_row())), 0)
        self.assertIn("rms_example_tool_v1.0.xml", self.labels())

    def test_malformed_xml_stops_the_run(self):
        self.out.mkdir()
        (self.out / "broken.xml").write_text("<oops")
        with self.assertRaises(ett.ExistingResourceError):
            ett.run(ett.parse_args([str(self.write_sheet(make_row())), "-o", str(self.out)]))

    def test_two_labels_with_one_lid_stop_the_run(self):
        self.run_tool(self.write_sheet(make_row()))
        shutil.copy(self.out / "rms_example_tool_v1.0.xml", self.out / "copy.xml")
        with self.assertRaisesRegex(ett.ExistingResourceError, "share the LID"):
            ett.run(ett.parse_args([str(self.write_sheet(make_row())), "-o", str(self.out)]))

    def test_deleted_files_are_not_active_labels(self):
        self.run_tool(self.write_sheet(make_row()))
        label = self.out / "rms_example_tool_v1.0.xml"
        label.rename(label.with_name(label.name + ".DELETED"))
        self.run_tool(self.write_sheet(make_row()))
        self.assertEqual(
            self.labels(), ["rms_example_tool_v1.0.xml", "rms_example_tool_v1.0.xml.DELETED"]
        )


class SchemaOptionTests(WorkDirTestCase):
    def test_schema_file_sets_names_and_model_version(self):
        xsd = self.tmp / "PDS4_PDS_1S00.xsd"
        xsd.write_text(
            '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1.28.0.0"/>'
        )
        self.run_tool(self.write_sheet(make_row()), "-x", str(xsd))
        text = (self.out / "rms_example_tool_v1.0.xml").read_text(encoding="utf-8")
        self.assertIn("PDS4_PDS_1S00.sch", text)
        self.assertIn("PDS4_PDS_1S00.xsd", text)
        self.assertIn("<information_model_version>1.28.0.0</information_model_version>", text)

    def test_pds_version_option(self):
        self.run_tool(self.write_sheet(make_row()), "--pdsVersion", "1P00")
        text = (self.out / "rms_example_tool_v1.0.xml").read_text(encoding="utf-8")
        self.assertIn("PDS4_PDS_1P00.xsd", text)
        self.assertIn("<information_model_version>1.25.0.0</information_model_version>", text)

    def test_schema_without_version_attribute(self):
        xsd = self.tmp / "bad.xsd"
        xsd.write_text('<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"/>')
        with self.assertRaises(ett.SchemaError):
            ett.parse_schema_info(xsd)


class MainTests(WorkDirTestCase):
    def test_exit_status_0_when_every_row_is_processed(self):
        sheet = self.write_sheet(make_row())
        with self.assertLogs(ett.logger, level="INFO"):
            self.assertEqual(ett.main([str(sheet), "-o", str(self.out)]), 0)

    def test_exit_status_1_when_a_row_fails(self):
        sheet = self.write_sheet(make_row(URL=""))
        with self.assertLogs(ett.logger, level="INFO"):
            self.assertEqual(ett.main([str(sheet), "-o", str(self.out)]), 1)

    def test_exit_status_2_for_unusable_input(self):
        with self.assertLogs(ett.logger, level="ERROR"):
            self.assertEqual(ett.main([str(self.tmp / "absent.csv"), "-o", str(self.out)]), 2)


if __name__ == "__main__":
    unittest.main()
