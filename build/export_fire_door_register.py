#!/usr/bin/env python3
"""
export_fire_door_register.py — writes the working "SESC-REG-13 Fire Door Asset and Install
Register" workbook from the register's columns.

Run from the repository root:   python3 build/export_fire_door_register.py [--out PATH] [--check]

    --out PATH   where to write the workbook. Default out/SESC-REG-13-Fire-Door-Register.xlsx
                 (out/ is gitignored: the workbook is a build artefact, never a source).
    --check      after writing, reopen the workbook and compare its header row with the columns
                 in the YAML. Exit 1 on any mismatch.

What it is. registers/fire-door-assets.yaml (SESC-REG-13) holds the COLUMNS of the register,
issued empty, each keyed to the fire_door_assets column it becomes in the SESC Platform (D20).
Rows name the installer and the client's site, so the WORKING register with rows lives in the
records store, not in git (CLAUDE.md 8). This script writes that working copy from the columns,
so that it can never carry a column the register does not, and so that the day the Platform
takes the table the headings and the keys already match.

Unlike build/export_coto.py, the Register sheet is NOT read-only: rows are entered in it by the
Contracts Manager (SESC-PRO-08 paragraph 34). The header row and the Columns and About sheets
are locked; the data rows are unlocked. That is a signal, not a security control.

Nothing here claims a certification. The About sheet says the Employer holds none.
"""
import argparse
import datetime
import os
import subprocess
import sys

try:
    import yaml
except ImportError:
    sys.exit("export_fire_door_register.py needs PyYAML:  pip install pyyaml")
try:
    from openpyxl import Workbook, load_workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Protection, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation
    from openpyxl.worksheet.properties import PageSetupProperties
except ImportError:
    sys.exit("export_fire_door_register.py needs openpyxl:  pip install openpyxl")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(ROOT, "registers", "fire-door-assets.yaml")
DATA_ROWS = 1000           # unlocked rows below the header
HEADER_ROW = 4

BLACK, RED, FONT = "231F20", "ED1D24", "Arial"
HDR_FONT = Font(name=FONT, size=10, bold=True, color="FFFFFF")
HDR_FILL = PatternFill("solid", fgColor=BLACK)
BODY = Font(name=FONT, size=10)
BOLD = Font(name=FONT, size=10, bold=True)
TITLE = Font(name=FONT, size=14, bold=True, color=BLACK)
BANNER_FONT = Font(name=FONT, size=10, bold=True, color=RED)
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")


def flat(v):
    if v is None:
        return ""
    if isinstance(v, (list, tuple)):
        return "; ".join(flat(x) for x in v)
    if isinstance(v, datetime.date):
        return v.isoformat()
    return " ".join(str(v).split())


def git_head():
    try:
        out = subprocess.run(["git", "--no-optional-locks", "-C", ROOT, "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True, timeout=10)
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return "not available"


def page_setup(ws, footer):
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.oddFooter.center.text = footer
    ws.oddFooter.center.size = 8


def write_register(wb, reg):
    ws = wb.active
    ws.title = "Register"
    cols = reg["columns"]
    ws["A1"] = f"{reg['id']}  Fire Door Asset and Install Register"
    ws["A1"].font = TITLE
    ws["A2"] = (f"Version {reg['version']} — {reg['status'].upper()}   ·   Owner: {reg['owner']}   ·   "
                "Columns generated from registers/fire-door-assets.yaml — do not add, rename or reorder a column here. "
                "One row per door, from its SESC-FRM-12. This working copy lives in the records store, never in git.")
    ws["A2"].font = BANNER_FONT
    ws["A2"].alignment = WRAP
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=min(len(cols), 12))
    ws.row_dimensions[2].height = 30
    for c, col in enumerate(cols, 1):
        cell = ws.cell(HEADER_ROW, c, col["label"] + (" *" if col.get("required") else ""))
        cell.font, cell.fill, cell.alignment, cell.border = HDR_FONT, HDR_FILL, WRAP, BORDER
        cell.protection = Protection(locked=True)
        width = max(14, min(42, len(col["label"]) * 0.9))
        ws.column_dimensions[get_column_letter(c)].width = width
    ws.row_dimensions[HEADER_ROW].height = 42
    # rows the register already holds (the repository copy holds none)
    rows = reg.get("doors") or []
    for r, door in enumerate(rows, HEADER_ROW + 1):
        for c, col in enumerate(cols, 1):
            ws.cell(r, c, flat(door.get(col["key"]))).font = BODY
    # unlock the data rows, add validation and borders
    for c, col in enumerate(cols, 1):
        letter = get_column_letter(c)
        rng = f"{letter}{HEADER_ROW + 1}:{letter}{HEADER_ROW + DATA_ROWS}"
        if col["type"] == "select" and col.get("options"):
            dv = DataValidation(type="list", formula1='"' + ",".join(flat(o) for o in col["options"]) + '"',
                                allow_blank=True, showErrorMessage=True,
                                errorTitle=col["label"], error="Choose one of the listed values.")
            ws.add_data_validation(dv)
            dv.add(rng)
        if col["type"] == "date":
            dv = DataValidation(type="date", allow_blank=True, showErrorMessage=True,
                                errorTitle=col["label"], error="Enter a date.")
            ws.add_data_validation(dv)
            dv.add(rng)
        for r in range(HEADER_ROW + 1, HEADER_ROW + DATA_ROWS + 1):
            cell = ws.cell(r, c)
            cell.protection = Protection(locked=False)
            cell.font, cell.alignment, cell.border = BODY, WRAP, BORDER
            if col["type"] == "date":
                cell.number_format = "DD/MM/YYYY"
    ws.freeze_panes = ws.cell(HEADER_ROW + 1, 3)
    ws.auto_filter.ref = f"A{HEADER_ROW}:{get_column_letter(len(cols))}{HEADER_ROW + DATA_ROWS}"
    ws.protection.sheet = True
    ws.protection.autoFilter = False
    ws.protection.sort = False
    ws.protection.formatRows = False
    ws.print_title_rows = f"{HEADER_ROW}:{HEADER_ROW}"
    page_setup(ws, f"{reg['id']} — working register — page &P of &N")
    return len(rows)


def write_columns(wb, reg):
    ws = wb.create_sheet("Columns")
    ws["A1"] = "Columns — the schema, from registers/fire-door-assets.yaml"
    ws["A1"].font = TITLE
    ws["A2"] = "These keys are the column names in the SESC Platform table fire_door_assets (D20). A key is never renamed."
    ws["A2"].font = BANNER_FONT
    hdr = ["Key", "Label", "Type", "Required", "Options", "Maps to", "Help"]
    for c, h in enumerate(hdr, 1):
        cell = ws.cell(HEADER_ROW, c, h)
        cell.font, cell.fill, cell.alignment, cell.border = HDR_FONT, HDR_FILL, WRAP, BORDER
    for r, col in enumerate(reg["columns"], HEADER_ROW + 1):
        vals = [col["key"], col["label"], col["type"], "yes" if col.get("required") else "",
                flat(col.get("options")), col.get("maps_to", ""), flat(col.get("help"))]
        for c, v in enumerate(vals, 1):
            cell = ws.cell(r, c, v)
            cell.font, cell.alignment, cell.border = BODY, WRAP, BORDER
    for c, w in enumerate((26, 40, 10, 10, 40, 36, 60), 1):
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.freeze_panes = ws.cell(HEADER_ROW + 1, 1)
    ws.protection.sheet = True
    page_setup(ws, f"{reg['id']} — columns — generated — page &P of &N")


def write_about(wb, reg, out_rel, n_rows):
    ws = wb.create_sheet("About")
    ws["A1"] = f"{reg['id']} — about this workbook"
    ws["A1"].font = TITLE
    lines = [
        ("Register", f"{reg['id']}  {flat(reg['title'])}"),
        ("Version", f"{reg['version']} — {reg['status'].upper()}"),
        ("Owner / approver", f"{reg['owner']} / {reg['approver']}"),
        ("Issued / next review", f"{flat(reg['issued'])} / {flat(reg['next_review'])}"),
        ("Procedure", flat(reg.get("parent_document"))),
        ("Generated", datetime.datetime.now().strftime("%d %B %Y %H:%M")),
        ("Repository commit", git_head()),
        ("Written to", out_rel),
        ("Rows carried from the repository", str(n_rows) + "  (the repository copy is issued empty)"),
        ("Where rows live", "This working copy, in the records store. Never the repository: a row names the installer and the client's site (CLAUDE.md 8)."),
        ("Certification", "SESC Solutions Ltd holds no third-party certification for fire door installation and no ISO certification. Nothing in this workbook states or implies one."),
        ("Rule", "The YAML register is the master for the COLUMNS; this workbook is the master for the ROWS until the SESC Platform takes them. Do not change a heading here."),
    ]
    for r, (k, v) in enumerate(lines, 3):
        ws.cell(r, 1, k).font = BOLD
        c = ws.cell(r, 2, v)
        c.font, c.alignment = BODY, WRAP
    ws.column_dimensions["A"].width = 34
    ws.column_dimensions["B"].width = 110
    ws.protection.sheet = True
    page_setup(ws, f"{reg['id']} — about — page &P of &N")


def check(path, reg):
    wb = load_workbook(path)
    ws = wb["Register"]
    got = [ws.cell(HEADER_ROW, c).value for c in range(1, len(reg["columns"]) + 1)]
    want = [c["label"] + (" *" if c.get("required") else "") for c in reg["columns"]]
    extra = ws.cell(HEADER_ROW, len(reg["columns"]) + 1).value
    if got != want or extra:
        print("CHECK FAILS: the header row does not match the columns in the register.")
        for g, w in zip(got, want):
            if g != w:
                print(f"   got {g!r}  want {w!r}")
        if extra:
            print(f"   extra column after the last: {extra!r}")
        return 1
    print(f"CHECK OK: {len(want)} columns match registers/fire-door-assets.yaml.")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--out", default=os.path.join(ROOT, "out", "SESC-REG-13-Fire-Door-Register.xlsx"))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    with open(SOURCE, encoding="utf-8") as fh:
        reg = yaml.safe_load(fh)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    out_rel = os.path.relpath(a.out, ROOT)
    wb = Workbook()
    n = write_register(wb, reg)
    write_columns(wb, reg)
    write_about(wb, reg, out_rel, n)
    wb.save(a.out)
    print(f"Wrote {out_rel}: {len(reg['columns'])} columns, {n} row(s) from the repository copy.")
    return check(a.out, reg) if a.check else 0


if __name__ == "__main__":
    sys.exit(main())
