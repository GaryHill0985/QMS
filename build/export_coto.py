#!/usr/bin/env python3
"""
export_coto.py — writes the read-only "SESC COTO Log" workbook from the registers.

Run from the repository root:   python3 build/export_coto.py [--out PATH] [--check]

    --out PATH   where to write the workbook. Default out/SESC-COTO-Log.xlsx (out/ is gitignored:
                 the workbook is a build artefact, never a source, and is never committed).
    --check      after writing, reopen the workbook and compare every data tab's row count with
                 the YAML it came from. Exit 1 on any mismatch.

What it is. James Milligan's CMS COTO Log template (register 2k) is a workbook with the tabs
Parties / Issues / Risk Register / Opp Register / Lists / Risks 27001. Decision D24 keeps SESC's
context data as YAML registers in this repository — one master — and generates this workbook
from them in the template's TAB LAYOUT, so that a consultant or a certification body who expects
a COTO log to look like a workbook gets one that can never drift from the registers.

What it takes from the template, and what it does not (CLAUDE.md 3, 7.2; register F41):
  - STRUCTURE ONLY: the tab names and their order, the one-row-per-item shape, the idea of a
    Lists tab holding the scales. Column headings are SESC's field names, not the template's.
  - NO CONTENT: not one party, issue, risk, opportunity, process name, scale label or list value
    is copied from the template. Every cell comes from registers/*.yaml or from this script's
    own labels.
  - NO "Risks 27001" tab. ISO 27001 is deferred to 2028+ (D1, CLAUDE.md 12.4).

Sources:
  Parties               registers/interested-parties.yaml   SESC-REG-05  one row per REQUIREMENT
  Issues                registers/issues.yaml               SESC-REG-06  one row per issue
  Risk Register         SESC-REG-01 is signed and NOT YET MIGRATED into the repository, so this tab
                        carries its reference and a pointer only, plus the REG-01 risk ids that
                        REG-06 refers to. Rows appear here when REG-01 is migrated.
  Opportunity Register  registers/opportunities.yaml        SESC-REG-08  one row per opportunity
  Lists                 the scales, bands, statuses and value lists read from the registers

The workbook is marked "generated from the repository — do not edit" on its cover and every
sheet is protected. That is a signal, not a security control: anyone can unprotect a sheet in
Excel. The control is that the registers are the master and the workbook is regenerated from
them; a workbook edited by hand is simply wrong the next time this script runs.

Nothing here claims a certification, a membership or an accreditation. Nothing here signs
anything: the registers' approval state is printed as it is in their front matter.
"""

import argparse
import datetime
import os
import subprocess
import sys

try:
    import yaml
except ImportError:
    sys.exit("export_coto.py needs PyYAML:  pip install pyyaml")
try:
    from openpyxl import Workbook, load_workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.workbook.protection import WorkbookProtection
    from openpyxl.worksheet.properties import PageSetupProperties
except ImportError:
    sys.exit("export_coto.py needs openpyxl:  pip install openpyxl")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "registers")

SOURCES = {
    "REG-05": os.path.join(REG, "interested-parties.yaml"),
    "REG-06": os.path.join(REG, "issues.yaml"),
    "REG-08": os.path.join(REG, "opportunities.yaml"),
}

# SESC-REG-01 is signed and lives outside the repository until migrated (register 6 item 7).
# Its control data is taken from registers/documents.yaml (SESC-REG-07) at run time, so that
# nothing about REG-01 is typed here.
REG01_ID = "SESC-REG-01"

# BRAND-SPEC.md: brand black #231F20, brand red #ED1D24 as accent only. Arial.
BLACK = "231F20"
RED = "ED1D24"
GREY = "F2F2F2"
FONT = "Arial"

TITLE = "SESC COTO Log"
BANNER = "GENERATED FROM THE REPOSITORY — DO NOT EDIT. Regenerate with: python3 build/export_coto.py"


# ------------------------------------------------------------------ helpers
def flat(v):
    """Folded YAML scalars carry newlines and double spaces; a cell wants one line of prose."""
    if v is None:
        return ""
    if isinstance(v, (list, tuple)):
        return "; ".join(flat(x) for x in v)
    if isinstance(v, dict):
        return "; ".join(f"{k}: {flat(x)}" for k, x in v.items())
    if isinstance(v, datetime.date):
        return v.isoformat()
    return " ".join(str(v).split())


def load(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def git_head():
    """Short commit of HEAD, read-only. --no-optional-locks so no index.lock is left behind
    (register F17). Never fails the export: the workbook records 'not available' instead."""
    try:
        out = subprocess.run(
            ["git", "--no-optional-locks", "-C", ROOT, "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=10)
        sha = out.stdout.strip()
        if out.returncode == 0 and sha:
            dirty = subprocess.run(
                ["git", "--no-optional-locks", "-C", ROOT, "status", "--porcelain",
                 "--untracked-files=all", "--", "registers"],
                capture_output=True, text=True, timeout=10).stdout.strip()
            return sha + (" + uncommitted changes in registers/" if dirty else "")
    except (OSError, subprocess.SubprocessError):
        pass
    return "not available"


def bias(issue):
    """Derived from the REG-06 row, not typed: what the row actually holds."""
    if issue.get("type") == "determination":
        return "Determination"
    has_r = bool(issue.get("risks"))
    has_o = bool(issue.get("opportunities"))
    if has_r and has_o:
        return "Risk and opportunity"
    if has_r:
        return "Risk"
    if has_o:
        return "Opportunity"
    return "Neither recorded"


# ------------------------------------------------------------------ styling
HDR_FONT = Font(name=FONT, size=10, bold=True, color="FFFFFF")
HDR_FILL = PatternFill("solid", fgColor=BLACK)
BODY_FONT = Font(name=FONT, size=10)
BOLD = Font(name=FONT, size=10, bold=True)
TITLE_FONT = Font(name=FONT, size=14, bold=True, color=BLACK)
BANNER_FONT = Font(name=FONT, size=10, bold=True, color=RED)
NOTE_FONT = Font(name=FONT, size=9, italic=True, color="595959")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTRE = Alignment(horizontal="center", vertical="top", wrap_text=True)


def sheet_head(ws, title, subtitle):
    """Rows 1-2: title and the do-not-edit banner. Row 3 blank. Row 4: column headers."""
    ws["A1"] = title
    ws["A1"].font = TITLE_FONT
    ws["A2"] = BANNER + "   ·   " + subtitle
    ws["A2"].font = BANNER_FONT
    ws.row_dimensions[1].height = 22


def write_table(ws, headers, rows, widths, start_row=4, centre_cols=()):
    for c, h in enumerate(headers, 1):
        cell = ws.cell(start_row, c, h)
        cell.font, cell.fill, cell.alignment, cell.border = HDR_FONT, HDR_FILL, WRAP, BORDER
    ws.row_dimensions[start_row].height = 30
    for r, row in enumerate(rows, start_row + 1):
        for c, v in enumerate(row, 1):
            cell = ws.cell(r, c, v)
            cell.font = BODY_FONT
            cell.alignment = CENTRE if c in centre_cols else WRAP
            cell.border = BORDER
    for c, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.freeze_panes = ws.cell(start_row + 1, 1)
    ws.auto_filter.ref = f"A{start_row}:{get_column_letter(len(headers))}{start_row + max(len(rows), 1)}"


def protect(ws):
    ws.protection.sheet = True
    ws.protection.autoFilter = False   # the reader may still filter and sort
    ws.protection.sort = False
    # print as landscape A4, one page wide, so a printed copy reads as a table, not as strips
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.print_title_rows = "1:4"
    ws.oddFooter.center.text = "SESC COTO Log — generated from the repository — do not edit — page &P of &N"
    ws.oddFooter.center.size = 8


# ------------------------------------------------------------------ tabs
def tab_cover(wb, data, counts, out_rel):
    ws = wb.active
    ws.title = "Cover"
    ws["A1"] = TITLE
    ws["A1"].font = Font(name=FONT, size=20, bold=True, color=BLACK)
    ws["A2"] = "Context of the organisation — interested parties, issues, risks and opportunities"
    ws["A2"].font = Font(name=FONT, size=11, color=BLACK)
    ws["A4"] = BANNER
    ws["A4"].font = Font(name=FONT, size=12, bold=True, color=RED)
    ws["A5"] = ("This workbook is a VIEW generated by build/export_coto.py from the YAML registers in the "
                "QMS repository. The registers are the master copy; this file is not. A change made here "
                "is lost the next time it is generated, and a copy of this file that differs from the "
                "registers is wrong, not a second version.")
    ws["A5"].font = BODY_FONT
    ws["A5"].alignment = WRAP
    ws.merge_cells("A5:F5")
    ws.row_dimensions[5].height = 48

    ws["A7"] = "Generated"
    ws["B7"] = datetime.datetime.now().strftime("%d %B %Y %H:%M")
    ws["A8"] = "Repository commit"
    ws["B8"] = git_head()
    ws["A9"] = "Written to"
    ws["B9"] = out_rel
    for r in (7, 8, 9):
        ws.cell(r, 1).font = BOLD
        ws.cell(r, 2).font = BODY_FONT

    r = 11
    hdr = ["Tab", "Source register", "Title", "Version", "Status", "Owner", "Issued", "Next review", "Rows in this workbook"]
    for c, h in enumerate(hdr, 1):
        cell = ws.cell(r, c, h)
        cell.font, cell.fill, cell.alignment, cell.border = HDR_FONT, HDR_FILL, WRAP, BORDER
    r += 1
    reg01 = data["reg01_meta"]
    lines = [
        ("Parties", "SESC-REG-05", data["REG-05"], f"{counts['parties']} parties / {counts['requirements']} requirement rows"),
        ("Issues", "SESC-REG-06", data["REG-06"], f"{counts['issues']} issues"),
        ("Risk Register", REG01_ID, None, "0 — reference and pointer only; not yet migrated"),
        ("Opportunity Register", "SESC-REG-08", data["REG-08"], f"{counts['opportunities']} opportunities"),
        ("Lists", "—", None, "scales and value lists read from the registers"),
    ]
    for tab, rid, fm, n in lines:
        if fm is not None:
            row = [tab, rid, fm["title"], fm["version"], fm["status"].upper(), fm["owner"],
                   flat(fm["issued"]), flat(fm["next_review"]), n]
        elif rid == REG01_ID:
            row = [tab, rid, reg01.get("title", "Business Risk Register"), flat(reg01.get("version", "")),
                   flat(reg01.get("state", "")).upper(), flat(reg01.get("owner") or "not recorded in SESC-REG-07"),
                   flat(reg01.get("issued", "")), flat(reg01.get("next_review", "")), n]
        else:
            row = [tab, rid, "", "", "", "", "", "", n]
        for c, v in enumerate(row, 1):
            cell = ws.cell(r, c, v)
            cell.font, cell.alignment, cell.border = BODY_FONT, WRAP, BORDER
        r += 1

    r += 1
    notes = [
        "Status is printed from each register's front matter. DRAFT means not approved and not issued; nothing in a draft register has been signed.",
        f"{REG01_ID} Business Risk Register is signed and held outside the repository as a branded PDF. It has not been migrated, so its rows are not here (register 6, item 7).",
        "Risks and opportunities are kept apart by design: risks in SESC-REG-01, opportunities in SESC-REG-08, and the issues in SESC-REG-06 point to both. They are never merged (ISO 9001:2026).",
        "The 'Processes affected' column on the Issues tab is empty: SESC-REG-06 v0.1 does not hold it. It is filled when REG-06 is next revised, not typed here.",
        "There is no ISO 27001 tab. ISO 27001 is deferred to 2028+ and Cyber Essentials is taken in its place (D1).",
        "Every score and pursuit plan in SESC-REG-08 v0.1 is a PROPOSAL for the named owner to confirm; the register says so row by row.",
        "Layout: tab order and one-row-per-item shape follow a consultant's template as structure only. No content was taken from it (CLAUDE.md 7.2).",
        "SESC Solutions Ltd holds no ISO certification of any kind. This workbook is a planning record, not evidence of conformity.",
    ]
    ws.cell(r, 1, "Notes").font = BOLD
    r += 1
    for i, n in enumerate(notes, 1):
        ws.cell(r, 1, f"{i}.").font = BODY_FONT
        ws.cell(r, 1).alignment = Alignment(horizontal="right", vertical="top")
        c = ws.cell(r, 2, n)
        c.font, c.alignment = BODY_FONT, WRAP
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=9)
        ws.row_dimensions[r].height = 30
        r += 1
    for col, w in zip("ABCDEFGHI", (22, 16, 40, 9, 11, 24, 12, 12, 34)):
        ws.column_dimensions[col].width = w
    protect(ws)


def tab_parties(wb, reg05):
    ws = wb.create_sheet("Parties")
    sheet_head(ws, "Interested parties and their requirements",
               f"SESC-REG-05 v{reg05['version']} ({reg05['status']}) — one row per requirement")
    headers = ["Ref", "Interested party", "Int / Ext", "Requirement", "Obligation", "Basis",
               "Evidence", "Status", "Gap", "REG-01 risks", "Party notes"]
    rows = []
    for p in reg05["parties"]:
        notes = []
        for key in ("named", "enforcement_history"):
            if p.get(key):
                notes.append(f"{key.replace('_', ' ').capitalize()}: {flat(p[key])}")
        for key in ("held", "lapsed", "not_held"):
            if p.get(key):
                notes.append(f"{key.replace('_', ' ').capitalize()}: {flat(p[key])}")
        first = True
        for q in p.get("requirements", []):
            rows.append([
                p["ref"], p["party"], flat(p.get("category")).capitalize(),
                flat(q.get("requirement")), flat(q.get("obligation")), flat(q.get("basis")),
                flat(q.get("evidence")), flat(q.get("status")).replace("_", " "),
                flat(q.get("gap") or q.get("note")), flat(p.get("risks")),
                " | ".join(notes) if first else "",
            ])
            first = False
    write_table(ws, headers, rows, [8, 28, 9, 40, 12, 30, 34, 11, 50, 12, 50], centre_cols=(3, 5, 8))
    protect(ws)
    return len(reg05["parties"]), len(rows)


def tab_issues(wb, reg06, reg08):
    ws = wb.create_sheet("Issues")
    sheet_head(ws, "Internal and external issues",
               f"SESC-REG-06 v{reg06['version']} ({reg06['status']}) — one row per issue")
    # map REG-06 issue ref -> REG-08 opportunity refs, so the Issues tab points at the register
    opp_by_source = {}
    for o in reg08["opportunities"]:
        opp_by_source.setdefault(o["source"], []).append(o["ref"])
    headers = ["Ln", "Ref", "Int / Ext", "Category", "Issue", "Bias", "Domains", "Processes affected",
               "Treatment — REG-01 risks", "Opportunities — REG-08", "Owner", "Notes"]
    rows = []
    for n, i in enumerate(reg06["issues"], 1):
        extra = []
        for key in ("risk_note", "note", "status", "milestone", "constraint", "rule",
                    "consequence", "resolution_proposed", "conclusion", "reasoning",
                    "determined_on", "determined_by"):
            if i.get(key):
                extra.append(f"{key.replace('_', ' ').capitalize()}: {flat(i[key])}")
        opps = opp_by_source.get(i["ref"], [])
        n_recorded = len(i.get("opportunities") or [])
        opp_cell = ", ".join(opps)
        if n_recorded and len(opps) != n_recorded:
            opp_cell += f"  (REG-06 records {n_recorded}; REG-08 holds {len(opps)})"
        rows.append([
            n, i["ref"], flat(i.get("type")).capitalize(), flat(i.get("category")), flat(i.get("issue")),
            bias(i), flat(i.get("domains")), "",
            flat(i.get("risks")) or ("—" if i.get("type") != "determination" else ""),
            opp_cell, flat(i.get("owner") or i.get("determined_by")), " | ".join(extra),
        ])
    write_table(ws, headers, rows, [5, 8, 12, 24, 60, 14, 22, 16, 16, 22, 20, 50], centre_cols=(1, 3, 6))
    protect(ws)
    return len(rows)


def tab_risk_pointer(wb, reg01, reg06):
    ws = wb.create_sheet("Risk Register")
    sheet_head(ws, "Business risks — SESC-REG-01", "reference and pointer only")
    refs = sorted({r for i in reg06["issues"] for r in (i.get("risks") or [])},
                  key=lambda s: (s[0], int(s[1:]) if s[1:].isdigit() else 0))
    lines = [
        ("Register", f"{REG01_ID} {reg01.get('title', 'Business Risk Register')}"),
        ("Version", flat(reg01.get("version", "not recorded"))),
        ("State", flat(reg01.get("state", "not recorded")).upper()),
        ("Issued", flat(reg01.get("issued", "not recorded"))),
        ("Next review", flat(reg01.get("next_review", "not recorded"))),
        ("Where it is", "Outside this repository, as a signed branded PDF in the issued document estate; "
                        "its control data above is read from SESC-REG-07 (registers/documents.yaml)."),
        ("Why no rows", f"{REG01_ID} has not been migrated into the repository (register 6, item 7). "
                        "This tab fills with its rows, scored and owned, when it is. Nothing is retyped here, "
                        "because a retyped copy is a second master."),
        ("Referenced from SESC-REG-06", ", ".join(refs) + f"  ({len(refs)} risk ids)"),
        ("Not here by design", "Opportunities. They are in SESC-REG-08 and on the Opportunity Register tab, "
                               "and are never merged with risks."),
    ]
    r = 4
    for k, v in lines:
        a = ws.cell(r, 1, k)
        b = ws.cell(r, 2, v)
        a.font, b.font = BOLD, BODY_FONT
        a.alignment = b.alignment = WRAP
        a.border = b.border = BORDER
        ws.row_dimensions[r].height = 30 if len(v) > 90 else 16
        r += 1
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 110
    protect(ws)
    return 0


def tab_opportunities(wb, reg08):
    ws = wb.create_sheet("Opportunity Register")
    sheet_head(ws, "Opportunities — scored, owned and planned",
               f"SESC-REG-08 v{reg08['version']} ({reg08['status']}) — one row per opportunity; "
               "scores and plans are PROPOSED until confirmed by the owner")
    headers = ["Ln", "Ref", "Source (REG-06)", "Process", "Opportunity", "Likelihood (1-5)", "Benefit (1-5)",
               "Score (L x B)", "Band", "Pursuit plan", "Owner", "Status", "Review date",
               "Record reference", "Confirmed by owner", "Notes"]
    rows = []
    for n, o in enumerate(reg08["opportunities"], 1):
        L, B = int(o["likelihood"]), int(o["benefit"])
        if int(o["score"]) != L * B:
            sys.exit(f"ERROR {o['ref']}: score {o['score']} is not likelihood x benefit ({L} x {B}). Fix the YAML.")
        rows.append([
            n, o["ref"], o["source"], o["process"], flat(o["opportunity"]), L, B, L * B, o["band"],
            flat(o["pursuit_plan"]), o["owner"], o["status"], flat(o["review_date"]),
            flat(o.get("record_ref")), "yes" if o.get("confirmed_by_owner") else "NO — proposed",
            flat(o.get("note")),
        ])
    write_table(ws, headers, rows, [5, 8, 10, 24, 56, 10, 10, 9, 10, 60, 20, 12, 12, 40, 12, 44],
                centre_cols=(1, 3, 6, 7, 8, 9, 12, 13, 15))
    # the three count cells the template's Opp Register keeps in its top-right corner, as formulas
    ws["N1"] = "Open (pursuing / identified)"
    ws["O1"] = f'=COUNTIF(L5:L{4 + len(rows)},"pursuing")+COUNTIF(L5:L{4 + len(rows)},"identified")'
    ws["N2"] = "Realised"
    ws["O2"] = f'=COUNTIF(L5:L{4 + len(rows)},"realised")'
    for ref in ("N1", "N2"):
        ws[ref].font = BOLD
    protect(ws)
    return len(rows)


def tab_lists(wb, reg05, reg06, reg08):
    ws = wb.create_sheet("Lists")
    sheet_head(ws, "Scales and value lists", "read from the registers; nothing here is typed")
    r = 4

    def block(title, pairs):
        nonlocal r
        c = ws.cell(r, 1, title)
        c.font, c.fill = HDR_FONT, HDR_FILL
        ws.cell(r, 2).fill = HDR_FILL
        r += 1
        for k, v in pairs:
            a, b = ws.cell(r, 1, flat(k)), ws.cell(r, 2, flat(v))
            a.font, b.font = BOLD, BODY_FONT
            a.alignment = b.alignment = WRAP
            a.border = b.border = BORDER
            r += 1
        r += 1

    sc = reg08["scoring"]
    block("SESC-REG-08 likelihood", sc["likelihood"].items())
    block("SESC-REG-08 benefit", sc["benefit"].items())
    block("SESC-REG-08 score", [("score", sc["score"])])
    block("SESC-REG-08 bands (proposed)", [(f"{k} (min {v['min']})", v["means"]) for k, v in sc["bands"].items()]
          + [("note", sc.get("bands_note", ""))])
    block("SESC-REG-08 statuses", reg08["statuses"].items())
    block("SESC-REG-08 processes in use",
          [(p, "") for p in sorted({o["process"] for o in reg08["opportunities"]})])
    block("SESC-REG-06 issue types", [(t, "") for t in sorted({i.get("type", "") for i in reg06["issues"]})])
    block("SESC-REG-06 categories", [(t, "") for t in sorted({i.get("category", "") for i in reg06["issues"]})])
    block("SESC-REG-06 domains", [(t, "") for t in sorted({d for i in reg06["issues"] for d in (i.get("domains") or [])})])
    block("SESC-REG-05 obligation types",
          [(t, "") for t in sorted({q.get("obligation", "") for p in reg05["parties"] for q in p.get("requirements", [])})])
    block("SESC-REG-05 requirement statuses",
          [(t, "") for t in sorted({q.get("status", "") for p in reg05["parties"] for q in p.get("requirements", [])})])
    block("Owners named across the three registers",
          [(t, "") for t in sorted({flat(x.get("owner") or x.get("determined_by")) for x in reg06["issues"]}
                                   | {o["owner"] for o in reg08["opportunities"]})])
    ws.column_dimensions["A"].width = 44
    ws.column_dimensions["B"].width = 90
    protect(ws)


# ------------------------------------------------------------------ main
def build(out_path):
    data = {k: load(p) for k, p in SOURCES.items()}
    for key, fm in data.items():
        for f in ("id", "title", "version", "status", "owner", "issued", "next_review"):
            if f not in fm:
                sys.exit(f"ERROR {SOURCES[key]}: front matter lacks '{f}'. Run build/validate.py first.")
    reg07 = load(os.path.join(REG, "documents.yaml"))
    reg01 = next((d for d in reg07.get("documents", []) if d.get("ref") == REG01_ID), {})
    data["reg01_meta"] = reg01

    wb = Workbook()
    counts = {}
    # The cover needs the counts, so the data tabs are built first and the cover filled after.
    cover = wb.active
    counts["parties"], counts["requirements"] = tab_parties(wb, data["REG-05"])
    counts["issues"] = tab_issues(wb, data["REG-06"], data["REG-08"])
    tab_risk_pointer(wb, reg01, data["REG-06"])
    counts["opportunities"] = tab_opportunities(wb, data["REG-08"])
    tab_lists(wb, data["REG-05"], data["REG-06"], data["REG-08"])
    wb.active = 0
    tab_cover(wb, data, counts, os.path.relpath(out_path, ROOT))
    wb.security = WorkbookProtection(lockStructure=True)
    for ws in wb.worksheets:
        ws.sheet_properties.tabColor = RED if ws.title == "Cover" else BLACK

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    wb.save(out_path)
    return counts


def check(out_path, counts):
    """Reopen the written file and compare every data tab with the YAML it came from.
    A script exiting cleanly is not verification; this at least proves the file holds the rows."""
    wb = load_workbook(out_path, read_only=True)
    expected_tabs = ["Cover", "Parties", "Issues", "Risk Register", "Opportunity Register", "Lists"]
    ok = True
    if wb.sheetnames != expected_tabs:
        print(f"FAIL tabs {wb.sheetnames} != {expected_tabs}")
        ok = False
    if "Risks 27001" in wb.sheetnames:
        print("FAIL a Risks 27001 tab exists (D1)")
        ok = False

    def data_rows(name, key_col=1, start=5):
        ws = wb[name]
        n = 0
        for row in ws.iter_rows(min_row=start, values_only=True):
            if row and row[key_col - 1] not in (None, ""):
                n += 1
        return n

    want = {
        "Parties": counts["requirements"],
        "Issues": counts["issues"],
        "Opportunity Register": counts["opportunities"],
    }
    for tab, n in want.items():
        got = data_rows(tab)
        flag = "ok  " if got == n else "FAIL"
        ok &= got == n
        print(f"{flag} {tab:22s} workbook rows {got:3d}  yaml rows {n:3d}")
    parties_in_tab = len({r[1] for r in wb["Parties"].iter_rows(min_row=5, values_only=True) if r[0]})
    flag = "ok  " if parties_in_tab == counts["parties"] else "FAIL"
    ok &= parties_in_tab == counts["parties"]
    print(f"{flag} {'Parties (distinct)':22s} workbook       {parties_in_tab:3d}  yaml       {counts['parties']:3d}")
    rr = wb["Risk Register"]
    pointer = any("not been migrated" in str(c) for row in rr.iter_rows(values_only=True) for c in row if c)
    print(f"{'ok  ' if pointer else 'FAIL'} {'Risk Register':22s} pointer only, no rows: {pointer}")
    ok &= pointer
    cover_banner = any(BANNER in str(c) for row in wb["Cover"].iter_rows(values_only=True) for c in row if c)
    print(f"{'ok  ' if cover_banner else 'FAIL'} {'Cover':22s} carries the do-not-edit banner: {cover_banner}")
    ok &= cover_banner
    wb.close()
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--out", default=os.path.join(ROOT, "out", "SESC-COTO-Log.xlsx"))
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    counts = build(args.out)
    print(f"export_coto.py — wrote {os.path.relpath(args.out, ROOT)}: "
          f"{counts['parties']} parties / {counts['requirements']} requirements, "
          f"{counts['issues']} issues, {counts['opportunities']} opportunities, "
          f"{REG01_ID} as pointer only")
    if args.check:
        return 0 if check(args.out, counts) else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
