#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_form.py — prints a SESC-FRM schema as a branded A4 form.

    python3 build/render_form.py forms/SESC-FRM-09-fire-door-pre-installation-survey.yaml
    python3 build/render_form.py forms/SESC-FRM-1*.yaml --pdf        # DOCX and PDF (needs LibreOffice)
    python3 build/render_form.py forms/SESC-FRM-11-*.yaml --out "Claude outputs"

Output goes to out/forms/ by default. out/, *.docx and *.pdf are gitignored: a printed form is
a build artefact, never source. THE YAML IS THE SOURCE (CLAUDE.md 5). Change the schema and
re-render; never edit the .docx.

Why this exists. The record capture forms SESC-FRM-01 to 08 are built as Google Forms from
their schemas (build/workspace_forms/). The fire door forms SESC-FRM-09 to 14 need to work
printed on A4 and on a tablet, with photograph prompts, tick boxes and a gap table, on a site
where the Workspace forms cannot take photographs (D18). This script prints the same schema
that the Workspace exporter and, later, the SESC Platform read, so the field KEYS on paper, on
the tablet and in the database are the same and nothing is re-keyed (D15, D20).

What it reads from the schema, over and above what export_forms.py reads:
    section      on a field — groups fields under a heading, in order of first appearance
    photo_stage  on a file field — prints the photograph prompt with the file-name pattern
    print        at the top level — per: what one copy covers; gap_table: the ten gap rows
                 printed as one table (SESC-FRM-11); photo_stages: listed in the header
    statement, certification_note, inspection_checks — printed verbatim where present

What it will not do. It prints no value into any field. It fills no signature. It carries the
header, footer and control line from the front matter, so NOBODY TYPES A VERSION NUMBER.
"""
import argparse
import sys
from pathlib import Path

import yaml
from docx import Document
from docx.oxml.ns import qn
from docx.shared import Twips

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render_docx as R  # noqa: E402

ROOT = R.ROOT
BOX = "☐"          # ballot box
LABEL_W = 3700
ENTRY_W = R.TEXT_W - LABEL_W


def flat(v):
    return " ".join(str(v).split()) if v is not None else ""


# ------------------------------------------------------------------ cells
def _tr(cant_split=True, height=None):
    tr = R.el("w:tr")
    pr = R.el("w:trPr")
    if cant_split:
        pr.append(R.el("w:cantSplit"))
    if height:
        pr.append(R.el("w:trHeight", {"w:hRule": "atLeast", "w:val": height}))
    tr.append(pr)
    return tr


def label_cell(field):
    tc = R._cell(LABEL_W, R.LABEL_FILL)
    runs = [R.run(flat(field["label"]), size=17, bold=True, color=R.GREY)]
    if field.get("required"):
        runs.append(R.run(" *", size=17, bold=True, color=R.RED))
    tc.append(R.para(runs, after=0, line=260))
    if field.get("help"):
        tc.append(R.para([R.run(flat(field["help"]), size=14, italic=True, color=R.GREY)],
                         after=0, line=240))
    return tc


def entry_cell(field, width=ENTRY_W):
    t = field["type"]
    tc = R._cell(width)
    if t in ("select", "multiselect"):
        runs = []
        for k, o in enumerate(field.get("options") or []):
            if k:
                runs.append(R.run("     ", size=18))
            runs.append(R.run(f"{BOX} {flat(o)}", size=18))
        tc.append(R.para(runs, after=0, line=300))
    elif t == "date":
        tc.append(R.para([R.run("____ / ____ / ________", size=18, color=R.GREY)], after=0, line=300))
    elif t == "file":
        stage = field.get("photo_stage", "")
        name = f"JOBNO_DOORID_{stage}_YYYYMMDD.jpg" if stage else "named with the record reference"
        tc.append(R.para([R.run(f"{BOX} Taken     {BOX} Filed as ", size=18),
                          R.run(name, size=18, code=True),
                          R.run("  in Fire Doors/<Door ID>/", size=18)], after=0, line=300))
    elif t == "number":
        tc.append(R.para([R.run("", size=18)], after=0, line=300))
    else:
        tc.append(R.para([R.run("", size=18)], after=0, line=300))
    return tc


def row_height(field):
    return {"textarea": 1300, "multiselect": 700, "select": 520, "file": 520}.get(field["type"], 480)


def fields_table(fields):
    t = R._tbl([LABEL_W, ENTRY_W])
    for f in fields:
        tr = _tr(height=row_height(f))
        tr.append(label_cell(f))
        tr.append(entry_cell(f))
        t.append(tr)
    return t


def gap_table(spec, by_key):
    """SESC-FRM-11: ten gap rows as one table — position, measured, pass/fail."""
    widths = [4000, 2300, R.TEXT_W - 6300]
    t = R._tbl(widths)
    tr = _tr()
    for w, h in zip(widths, ("Position", "Measured (mm)", "Within the manufacturer's tolerance")):
        tc = R._cell(w, R.BLACK)
        tc.append(R._cell_para(h, "head"))
        tr.append(tc)
    tr.find(qn("w:trPr")).append(R.el("w:tblHeader"))
    t.append(tr)
    for label, key in spec["rows"]:
        f = by_key.get(key, {"label": label, "type": "number"})
        tr = _tr(height=480)
        tc = R._cell(widths[0], R.LABEL_FILL)
        tc.append(R.para([R.run(flat(label), size=17, bold=True, color=R.GREY)], after=0, line=260))
        tr.append(tc)
        tr.append(R._cell(widths[1]))
        tr[-1].append(R.para([R.run("", size=18)], after=0, line=300))
        tc = R._cell(widths[2])
        tc.append(R.para([R.run(f"{BOX} Pass     {BOX} Fail", size=18)], after=0, line=300))
        tr.append(tc)
        t.append(tr)
    return t


# ------------------------------------------------------------------ render
def render(src, out_dir=None, pdf=False):
    src = Path(src)
    fm = yaml.safe_load(src.read_text(encoding="utf-8"))
    for k in ("id", "title", "version", "status", "owner", "fields"):
        if not fm.get(k):
            raise R.RenderError(f"{src}: schema has no '{k}'")
    status = fm["status"]
    out_dir = Path(out_dir or ROOT / "out" / "forms")
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{fm['id']}-v{fm['version']}" + ("" if status in ("approved", "superseded") else f"-{status.upper()}") + "-form"
    docx_path = out_dir / f"{stem}.docx"
    org = R.load_org()
    pr = fm.get("print") or {}
    gap = pr.get("gap_table")
    gap_keys = {k for _, k in (gap or {}).get("rows", [])}
    by_key = {f["key"]: f for f in fm["fields"]}

    doc = Document()
    body = doc.element.body
    for c in list(body):
        if c.tag != qn("w:sectPr"):
            body.remove(c)
    sect = body.find(qn("w:sectPr"))
    add = sect.addprevious

    # ---- title and control line, from the front matter
    add(R.heading(f"{fm['id']} — {fm['title']}", 1)[0])
    issued = status in ("approved", "superseded")
    control = (f"Form {fm['id']}  ·  Version {fm['version']}"
               + ("" if issued else f" — {status.upper()}, NOT ISSUED")
               + f"  ·  Owner: {fm['owner']}"
               + (f"  ·  Under {fm['parent_document']}" if fm.get("parent_document") else "")
               + (f"  ·  One per {flat(fm['one_per'])}" if fm.get("one_per") else ""))
    add(R.para([R.run(control, size=15, color=R.GREY, caps=True, spacing=6)], after=120, line=260,
               border_bottom=("6", R.HAIRLINE)))
    if fm.get("purpose"):
        add(R.para([R.run(flat(fm["purpose"]), size=17, italic=True, color=R.GREY)], after=120, line=280))
    if fm.get("statement"):
        add(R.callout([f"**Statement of installation.** {flat(fm['statement'])}"]))
        add(R.spacer(60))
    if fm.get("certification_note"):
        add(R.para([R.run(flat(fm["certification_note"]), size=16, bold=True)], after=120, line=270))
    if pr.get("photo_stages"):
        add(R.para([R.run("Photographs on this form: " + ", ".join(pr["photo_stages"])
                          + ".  File name JOBNO_DOORID_Sxx_YYYYMMDD.jpg, filed in Fire Doors/<Door ID>/ the same day.",
                          size=16, bold=True)], after=120, line=270))

    # ---- sections
    order, groups = [], {}
    for f in fm["fields"]:
        if f["key"] in gap_keys:
            continue
        s = f.get("section", "Fields")
        if s not in groups:
            order.append(s); groups[s] = []
        groups[s].append(f)
    for s in order:
        add(R.heading(s, 2)[0])
        fields = groups[s]
        split = None
        if gap and gap_keys and gap.get("before_key") in {f["key"] for f in fields}:
            split = next(i for i, f in enumerate(fields) if f["key"] == gap["before_key"])
        if split is None:
            add(fields_table(fields))
        else:
            # the gap table sits between the tolerance boxes and the pass/fail summary
            add(fields_table(fields[:split]))
            add(R.spacer(60))
            add(R.para([R.run("Measured with the door closed and latched. Copy the manufacturer's tolerance "
                              "into the boxes above before measuring.", size=16, italic=True, color=R.GREY)],
                       after=60, line=260))
            add(gap_table(gap, by_key))
            add(R.spacer(60))
            add(fields_table(fields[split:]))
        add(R.spacer(80))

    # ---- inspection checks (SESC-FRM-13) and guidance
    ic = fm.get("inspection_checks")
    if ic:
        add(R.heading("What a routine inspection checks", 2)[0])
        for item in ic.get("items", []):
            add(R.para([R.run(f"{BOX}  {flat(item)}", size=18)], after=40, line=280))
        add(R.spacer(80))
    if fm.get("guidance"):
        add(R.heading("How to use this form", 2)[0])
        for g in fm["guidance"]:
            add(R.para([R.run("•  ", size=18), *R.md_runs(flat(g), size=18)], after=40, line=280,
                       ind_left=R.NUM_IND, hanging=R.NUM_IND))
    add(R.para([R.run("* required.  A record is never edited or deleted; a correction is a new entry "
                      "that points at the original (D15).  Completed forms are held as the schema's "
                      "completed_record says, never in the repository.", size=14, italic=True, color=R.GREY)],
               before=120, after=0, line=240))

    # ---- page, header, footer
    s = doc.sections[0]
    s.page_width, s.page_height = Twips(R.PAGE_W), Twips(R.PAGE_H)
    s.top_margin, s.bottom_margin = Twips(R.MARGIN_TOP), Twips(R.MARGIN_BOTTOM)
    s.left_margin = s.right_margin = Twips(R.MARGIN_LR)
    s.header_distance = s.footer_distance = Twips(R.HDR_FTR)
    marking = "OFFICIAL-SENSITIVE" if fm.get("official_sensitive") else None
    wm_rid, _ = s.header.part.get_or_add_image(R.watermark_png())
    R.header_xml(s.header, fm, marking, wm_rid)
    R.footer_xml(s.footer, marking)

    cp = doc.core_properties
    cp.title = f"{fm['id']} {fm['title']} v{fm['version']} — form"
    cp.author = fm.get("owner", "")
    cp.subject = f"SESC Integrated Management System — {org['legal_name']}"
    cp.comments = f"Generated by build/render_form.py from {src.as_posix()}. Do not edit; edit the schema."
    doc.save(docx_path)
    result = {"docx": docx_path, "fields": len(fm["fields"]), "sections": len(order)}
    if pdf:
        result["pdf"] = R.to_pdf(docx_path, out_dir)
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("schema", nargs="+", help="forms/SESC-FRM-*.yaml")
    ap.add_argument("--pdf", action="store_true", help="also render PDF with LibreOffice")
    ap.add_argument("--out", default=None, help="output folder (default out/forms)")
    a = ap.parse_args(argv)
    rc = 0
    for s in a.schema:
        try:
            r = render(s, a.out, a.pdf)
        except (R.RenderError, yaml.YAMLError, KeyError) as e:
            print(f"FAIL  {s}: {e}")
            rc = 1
            continue
        print(f"OK    {s} -> {r['docx']} ({r['fields']} fields, {r['sections']} sections)"
              + (f" and {r['pdf']}" if r.get("pdf") else ""))
    return rc


if __name__ == "__main__":
    sys.exit(main())
