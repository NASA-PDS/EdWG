#!/usr/bin/env python3
import argparse
from datetime import date
import difflib
import os
import re
import ssl
import xml.etree.ElementTree as ET
import pandas as pd

# Global SSL Workaround for macOS Python installations
ssl._create_default_https_context = ssl._create_unverified_context

# The XML template block with default PDS4_PDS settings
RESOURCE_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="https://pds.nasa.gov/pds4/pds/v1/PDS4_PDS_1R00.sch" schematypens="http://purl.oclc.org/dsdl/schematron"?>
<Product_Resource xmlns="http://pds.nasa.gov/pds4/pds/v1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://pds.nasa.gov/pds4/pds/v1 https://pds.nasa.gov/pds4/pds/v1/PDS4_PDS_1R00.xsd">
    <Identification_Area>
        <logical_identifier>urn:nasa:pds:context:resource:LID_REPLACE</logical_identifier>
        <version_id>1.0</version_id>
        <title>TOOL_REPLACE</title>
        <information_model_version>1.27.0.0</information_model_version>
        <product_class>Product_Resource</product_class>
MOD_HISTORY_REPLACE
    </Identification_Area>
    <Archive_Resource>
        <name>TOOL_REPLACE</name>
        <version_id>1.0</version_id>
        <url>URL_REPLACE</url>
        <release_date>DATE_REPLACE</release_date>
        <resource_type>TYPE_REPLACE</resource_type>
        <resource_subtype>SUBTYPE_REPLACE</resource_subtype>
        <interface_type>INTERFACE_REPLACE</interface_type>
        <pds4_wide_applicability_flag>APPLICABILITY_REPLACE</pds4_wide_applicability_flag>
        <description>DESC_REPLACE</description>
    </Archive_Resource>
    <Reference_List>
        <Internal_Reference>
            <lid_reference>urn:nasa:pds:context:node:NODE_REPLACE</lid_reference>
            <reference_type>service_to_node</reference_type>
        </Internal_Reference>
        <Internal_Reference>
            <lid_reference>REF_REPLACE</lid_reference>
            <reference_type>service_to_CONTEXTPRODUCT_TYPE_REPLACE</reference_type>
        </Internal_Reference>
    </Reference_List>
</Product_Resource>"""

EXPECTED_HEADERS = [
    "status",
    "node / org",
    "Tool / Service Name",
    "URL",
    "Release Date",
    "Resource Type",
    "Resource Subtype",
    "Interface Type",
    "Description",
    "Internal Reference",
    "Applicable to All PDS4 Data?"
]

def convert_google_sheet_url(url):
    """Converts a standard Google Sheets sharing URL into a direct CSV export URL."""
    if "docs.google.com/spreadsheets" in url:
        match = re.search(r'/d/([a-zA-Z0-9-_]+)', url)
        if match:
            spreadsheet_id = match.group(1)
            return f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv"
    return url

def load_input_data(input_path):
    """Reads data from a Google Sheets URL, local CSV, or local TSV file."""
    if input_path.startswith("http://") or input_path.startswith("https://"):
        csv_url = convert_google_sheet_url(input_path)
        return pd.read_csv(csv_url)
    
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if input_path.lower().endswith(('.tsv', '.tab')):
        return pd.read_csv(input_path, sep='\t')
    return pd.read_csv(input_path)

def parse_schema_info(schema_path):
    """Extracts the root name and version attribute from the specified XSD schema file."""
    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    schema_root_name = os.path.splitext(os.path.basename(schema_path))[0]
    
    try:
        tree = ET.parse(schema_path)
        root = tree.getroot()
        schema_version = root.attrib.get("version")
    except Exception as e:
        raise ValueError(f"Failed to parse schema XML file '{schema_path}': {e}")

    if not schema_version:
        raise ValueError(f"Could not find 'version' attribute in schema file '{schema_path}'")

    return schema_root_name, schema_version

def split_multi_value(val, delimiter=","):
    """Splits multi-valued fields safely using a specified delimiter."""
    if pd.isna(val) or str(val).strip() == "":
        return []
    return [v.strip() for v in str(val).split(delimiter) if v.strip()]

def derive_information_model_version(pds_version):
    """Derives information model version string from --pdsVersion."""
    if len(pds_version) < 4:
        raise ValueError(f"Invalid pdsVersion '{pds_version}': must be at least 4 characters long.")

    c1 = pds_version[0]
    c2 = pds_version[1]
    c3 = pds_version[2]
    c4 = pds_version[3]

    if c2.isalpha():
        v2 = (ord(c2.upper()) - ord('A') + 1) + 9
    else:
        v2 = int(c2)

    return f"{c1}.{v2}.{c3}.{c4}"

def create_initial_modification_history(mod_date=None):
    """Creates initial Modification_History block for v1.0."""
    if not mod_date:
        mod_date = date.today().isoformat()
    return (
        "        <Modification_History>\n"
        "            <Modification_Detail>\n"
        f"                <modification_date>{mod_date}</modification_date>\n"
        "                <version_id>1.0</version_id>\n"
        "                <description>Initial version.</description>\n"
        "            </Modification_Detail>\n"
        "        </Modification_History>"
    )

def append_modification_detail(old_xml_content, new_version, description, mod_date=None):
    """Prepends a new Modification_Detail entry to the top of Modification_History."""
    if not mod_date:
        mod_date = date.today().isoformat()

    new_detail = (
        "        <Modification_Detail>\n"
        f"            <modification_date>{mod_date}</modification_date>\n"
        f"            <version_id>{new_version}</version_id>\n"
        f"            <description>{description}</description>\n"
        "        </Modification_Detail>"
    )

    mod_hist_match = re.search(r'<Modification_History>(.*?)</Modification_History>', old_xml_content, re.DOTALL)

    if mod_hist_match:
        inner_history = mod_hist_match.group(1)
        updated_inner = f"\n{new_detail}" + inner_history
        return f"        <Modification_History>{updated_inner}        </Modification_History>"
    else:
        init_detail = (
            "        <Modification_Detail>\n"
            f"            <modification_date>{mod_date}</modification_date>\n"
            "            <version_id>1.0</version_id>\n"
            "            <description>Initial version.</description>\n"
            "        </Modification_Detail>"
        )
        return (
            "        <Modification_History>\n"
            f"{new_detail}\n"
            f"{init_detail}\n"
            "        </Modification_History>"
        )

def strip_modification_history(xml_str):
    """Strips Modification_History block from XML content for comparison."""
    return re.sub(r'\s*<Modification_History>.*?</Modification_History>', '', xml_str, flags=re.DOTALL)

def find_existing_xml_by_lid(output_dir, target_lid):
    """Searches output_dir for an existing XML file matching target_lid."""
    if not os.path.exists(output_dir):
        return None

    for fname in os.listdir(output_dir):
        if fname.endswith(".xml") and not fname.endswith(".DELETED"):
            fpath = os.path.join(output_dir, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    content = f.read()
                lid_match = re.search(r'<logical_identifier>(.*?)</logical_identifier>', content)
                if lid_match and lid_match.group(1).strip() == target_lid:
                    ver_match = re.search(r'<Identification_Area>.*?<version_id>(.*?)</version_id>', content, re.DOTALL)
                    ver_id = ver_match.group(1).strip() if ver_match else "1.0"
                    return fpath, fname, content, ver_id
            except Exception:
                continue
    return None

def are_xml_equal(xml_str1, xml_str2):
    """Compares two XML strings ignoring Modification_History."""
    s1 = strip_modification_history(xml_str1)
    s2 = strip_modification_history(xml_str2)
    try:
        c1 = ET.canonicalize(s1, strip_text=True)
        c2 = ET.canonicalize(s2, strip_text=True)
        return c1 == c2
    except Exception:
        return s1.strip() == s2.strip()

def bump_minor_version(version_str):
    """Increments minor version number (e.g. '1.0' -> '1.1')."""
    parts = version_str.split('.')
    if len(parts) >= 2:
        try:
            parts[1] = str(int(parts[1]) + 1)
            return ".".join(parts)
        except ValueError:
            pass
    return f"{version_str}.1"

def update_identification_version(xml_content, new_version):
    """Updates Identification_Area/version_id in the XML content string."""
    def repl(match):
        block = match.group(0)
        return re.sub(r'<version_id>.*?</version_id>', f'<version_id>{new_version}</version_id>', block, count=1)
    
    return re.sub(r'<Identification_Area>.*?</Identification_Area>', repl, xml_content, flags=re.DOTALL)

def print_diffs(old_content, new_content, old_filename, new_filename):
    """Prints unified diff between old and new XML contents (without Modification_History)."""
    old_stripped = strip_modification_history(old_content)
    new_stripped = strip_modification_history(new_content)
    
    old_lines = old_stripped.splitlines(keepends=True)
    new_lines = new_stripped.splitlines(keepends=True)
    diff = difflib.unified_diff(old_lines, new_lines, fromfile=old_filename, tofile=new_filename)
    
    print(f"\n--- Differences for {old_filename} vs {new_filename} ---")
    diff_output = "".join(list(diff))
    if diff_output:
        print(diff_output)
    else:
        print("  (Only version metadata changed)")
    print("-" * 50)

def main():
    # 1. Setup Command-Line Argument Parsing
    parser = argparse.ArgumentParser(
        description="Generate PDS4 XML Resource files from a Google Spreadsheet or local CSV/TSV file.",
        epilog="  where <inputFile> is a local CSV or TSV file or the URL of a google sheet",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("inputFile", metavar="<inputFile>", type=str, help="Path to local CSV/TSV file or Google Sheets URL.")
    parser.add_argument("-o", "--output_dir", type=str, default="toolsResources/", help="Output directory for XML files (default: toolsResources/)")
    parser.add_argument("-x", "--schema", type=str, help="Path to schema XSD file (e.g. PDS4_PDS_1R00.xsd)")
    parser.add_argument("--pdsVersion", type=str, default="1R00", help="PDS version string (default: 1R00)")

    args = parser.parse_args()

    # Determine base XML template with pdsVersion and schema overrides
    template_str = RESOURCE_TEMPLATE
    info_model_version = derive_information_model_version(args.pdsVersion)

    template_str = template_str.replace("1R00", args.pdsVersion)
    template_str = re.sub(
        r'<information_model_version>[^<]+</information_model_version>',
        f'<information_model_version>{info_model_version}</information_model_version>',
        template_str
    )

    if args.schema:
        schema_root, schema_version = parse_schema_info(args.schema)
        template_str = template_str.replace(f"PDS4_PDS_{args.pdsVersion}", schema_root)
        template_str = re.sub(
            r'<information_model_version>[^<]+</information_model_version>',
            f'<information_model_version>{schema_version}</information_model_version>',
            template_str
        )

    # 2. Fetch and Validate Input Data
    try:
        df = load_input_data(args.inputFile)
    except Exception as e:
        raise ValueError(f"Failed to read input source. Error: {e}")

    actual_headers = list(df.columns)
    missing_headers = [h for h in EXPECTED_HEADERS if h not in actual_headers]
    if missing_headers:
        raise ValueError(f"Input data is missing required column headers: {missing_headers}")

    os.makedirs(args.output_dir, exist_ok=True)

    # 3. Process Rows
    for idx, row in df.iterrows():
        node_raw = str(row["node / org"]).strip() if pd.notna(row["node / org"]) else ""
        toolV = str(row["Tool / Service Name"]).strip() if pd.notna(row["Tool / Service Name"]) else ""
        urlV = str(row["URL"]).strip() if pd.notna(row["URL"]) else ""
        applicableV = str(row["Applicable to All PDS4 Data?"]).strip() if pd.notna(row["Applicable to All PDS4 Data?"]) else ""
        descV = str(row["Description"]).strip() if pd.notna(row["Description"]) else ""

        type_list = split_multi_value(row["Resource Type"], delimiter=",")
        subtype_list = split_multi_value(row["Resource Subtype"], delimiter=",")
        interface_list = split_multi_value(row["Interface Type"], delimiter=",")
        lidref_list = split_multi_value(row["Internal Reference"], delimiter=";")

        missing_fields = []
        if not toolV:
            missing_fields.append("Tool / Service Name")
        if not node_raw:
            missing_fields.append("node / org")
        if not urlV:
            missing_fields.append("URL")
        if not type_list:
            missing_fields.append("Resource Type")
        if not descV:
            missing_fields.append("Description")
        if not applicableV:
            missing_fields.append("Applicable to All PDS4 Data?")

        if missing_fields:
            row_label = f"'{toolV}'" if toolV else f"Row {idx + 2}"
            print(f"Error: {row_label} is missing required field(s): {', '.join(missing_fields)}. Skipping XML creation.")
            continue

        pds4_wide_app = "true" if applicableV.lower() in ["yes", "true", "y", "1"] else "false"

        has_release_date = pd.notna(row["Release Date"]) and str(row["Release Date"]).strip() != ""
        dateV = str(row["Release Date"]).strip() if has_release_date else ""

        temp_tool = toolV.lower().replace(" ", "_")
        toolLowerV = re.sub(r'[^a-z0-9._-]', '', temp_tool)
        
        if node_raw.lower() == "community":
            nodeV = "en"
        else:
            nodeV = node_raw.lower()

        # 4. XML Template Manipulation
        xml_content = template_str
        
        xml_content = xml_content.replace("LID_REPLACE", toolLowerV)
        xml_content = xml_content.replace("TOOL_REPLACE", toolV)
        xml_content = xml_content.replace("URL_REPLACE", urlV)
        xml_content = xml_content.replace("DESC_REPLACE", descV)
        xml_content = xml_content.replace("NODE_REPLACE", nodeV)
        xml_content = xml_content.replace("APPLICABILITY_REPLACE", pds4_wide_app)
        xml_content = xml_content.replace("MOD_HISTORY_REPLACE", create_initial_modification_history())

        if has_release_date:
            xml_content = xml_content.replace("DATE_REPLACE", dateV)
        else:
            xml_content = re.sub(r'\s*<release_date>DATE_REPLACE</release_date>\n?', '\n', xml_content)

        type_xml_blocks = [f"<resource_type>{t}</resource_type>" for t in type_list]
        xml_content = xml_content.replace("<resource_type>TYPE_REPLACE</resource_type>", "\n        ".join(type_xml_blocks))

        if subtype_list:
            subtype_xml_blocks = [f"<resource_subtype>{st}</resource_subtype>" for st in subtype_list]
            xml_content = xml_content.replace("<resource_subtype>SUBTYPE_REPLACE</resource_subtype>", "\n        ".join(subtype_xml_blocks))
        else:
            xml_content = re.sub(r'\s*<resource_subtype>SUBTYPE_REPLACE</resource_subtype>\n?', '\n', xml_content)

        if interface_list:
            interface_xml_blocks = [f"<interface_type>{it}</interface_type>" for it in interface_list]
            xml_content = xml_content.replace("<interface_type>INTERFACE_REPLACE</interface_type>", "\n        ".join(interface_xml_blocks))
        else:
            xml_content = re.sub(r'\s*<interface_type>INTERFACE_REPLACE</interface_type>\n?', '\n', xml_content)

        ref_template_pattern = (
            "        <Internal_Reference>\n"
            "            <lid_reference>REF_REPLACE</lid_reference>\n"
            "            <reference_type>service_to_CONTEXTPRODUCT_TYPE_REPLACE</reference_type>\n"
            "        </Internal_Reference>"
        )

        ref_xml_blocks = []
        for r in lidref_list:
            colons = r.split(":")
            contextproduct_type = colons[-2] if len(colons) >= 2 else "unknown"
            
            block = (
                "        <Internal_Reference>\n"
                f"            <lid_reference>{r}</lid_reference>\n"
                f"            <reference_type>service_to_{contextproduct_type}</reference_type>\n"
                "        </Internal_Reference>"
            )
            ref_xml_blocks.append(block)

        joined_ref_blocks = "\n".join(ref_xml_blocks)
        xml_content = xml_content.replace(ref_template_pattern, joined_ref_blocks)

        target_lid = f"urn:nasa:pds:context:resource:{toolLowerV}"

        # 5. Check Output Directory for Existing XML with same logical_identifier
        existing_info = find_existing_xml_by_lid(args.output_dir, target_lid)

        if existing_info:
            old_filepath, old_filename, old_content, old_version = existing_info

            # Compare XML ignoring Modification_History
            if are_xml_equal(old_content, xml_content):
                print(f"Info: No changes for file {old_filename}")
                continue
            else:
                # Bump minor version number
                new_version = bump_minor_version(old_version)
                xml_content = update_identification_version(xml_content, new_version)
                
                new_filename = f"{nodeV}_{toolLowerV}_v{new_version}.xml"

                # Display diffs excluding Modification_History
                print_diffs(old_content, xml_content, old_filename, new_filename)
                confirm = input(f"Replace old file '{old_filename}' with '{new_filename}'? [y/N]: ").strip().lower()

                if confirm in ['y', 'yes']:
                    change_desc = input("Enter description of change [Updated resource details.]: ").strip()
                    if not change_desc:
                        change_desc = "Updated resource details."

                    # Update Modification_History with prepended entry
                    updated_mod_history = append_modification_detail(old_content, new_version, change_desc)
                    xml_content = re.sub(r'        <Modification_History>.*?</Modification_History>', updated_mod_history, xml_content, flags=re.DOTALL)

                    # Rename old file to append .DELETED
                    os.rename(old_filepath, f"{old_filepath}.DELETED")
                    
                    # Write new version file
                    new_filepath = os.path.join(args.output_dir, new_filename)
                    with open(new_filepath, "w", encoding="utf-8") as f:
                        f.write(xml_content)
                    print(f"Updated: '{old_filename}' marked as .DELETED, created '{new_filename}'")
                else:
                    print(f"Skipped updating '{old_filename}'")
                    continue
        else:
            # New file creation (default version_id 1.0)
            filename = f"{nodeV}_{toolLowerV}_v1.0.xml"
            file_path = os.path.join(args.output_dir, filename)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(xml_content)

    print(f"\nSuccess: XML processing complete. Files generated in '{args.output_dir}'")

if __name__ == "__main__":
    main()
