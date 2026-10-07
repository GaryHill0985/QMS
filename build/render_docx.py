#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_docx.py — the branded renderer for the SESC Integrated Management System.

    python3 build/render_docx.py system/4-context.md            # DOCX only
    python3 build/render_docx.py system/4-context.md --pdf      # DOCX and PDF (needs LibreOffice)
    python3 build/render_docx.py system/4-context.md --pdf --out "Claude outputs"

Output goes to out/render/ by default. out/, *.docx and *.pdf are gitignored: a
rendered file is a build artefact, never source.

Requires: python-docx, PyYAML, Pillow, numpy; LibreOffice (soffice) for --pdf.
Fonts: Arial, or Liberation Sans on Linux (metrically identical).

WHERE THIS CAME FROM
    Ported on 24 September 2026 (workstream 2) from the JOSCAR toolkit's
    policy_editor.py and the cover generator sesc_cover.py, both read-only in the
    TeraBox restore. policy_editor.py EDITS an existing branded .docx in place.
    This file does two jobs:

    1. GENERATE a branded .docx from a Markdown source with YAML front matter
       (render()). The control block, the cover's six fields, the running header
       and the footer are all generated from the front matter. NOBODY TYPES A
       VERSION NUMBER. The page geometry, the header and footer bars, the
       watermark, the headings, the tables and the cover reproduce the signed
       branded POL-16 v1.2 run for run. BRAND-SPEC.md and INTERIOR-SPEC.md are
       authoritative. The cover is NOT redesigned: make_cover() below is
       sesc_cover.make_cover() with its geometry unchanged. With the red
       triangle at the original 37% it reproduced the POL-16 v1.2 cover to a
       mean difference of 0.24 on a 0-765 scale. Since 24 September 2026 (D21)
       the red triangle runs at 70%; the white wedge stays at 37%.

    2. AMEND a legacy branded .docx in place (the "amend API" at the bottom:
       replace_runs, append_para, add_contents_entry, set_cell, find_signature_table,
       patch_header_footer_text, patch_branded_cover). This is what the migration
       of the twenty-one signed documents will need, because CLAUDE.md §5 says
       amend, never regenerate.

THE RENDERING TRAPS — Section workflow method.md §5, plus the fifth (F27)
    1. The Branded TOC field. A Word TOC field shows its cached result, which
       goes stale the moment a heading changes. render() does NOT use a field.
       The contents list is generated from the source headings on every build.
       add_contents_entry() remains for amending legacy documents that have one.
    2. The signature table is not table 1. Never address a table by index.
       find_signature_table() finds it by its first-column label.
    3. Header text hidden in tables and textboxes. The generated header and
       footer ARE tables. patch_header_footer_text() rewrites the raw
       word/header*.xml and word/footer*.xml, which the paragraph API cannot see.
    4. set_cell() style in an empty cell. python-docx's add_run() in an empty
       cell produces a run with no formatting, which renders in the default face.
       set_cell() here clones the formatting of a styled neighbour, or applies the
       house cell format, so an empty cell never falls back to Times or Calibri.
    5. (F27, F34) Numbered paragraphs restart at 1 after a table, or are
       renumbered. A Markdown renderer treats an indented continuation as a code
       block or restarts an ordered list after a table. render() never uses
       Markdown list numbering or Word auto-numbering. The number the source
       carries is written into the paragraph as literal text.
       build/test_render_docx.py compares every printed number with the source.

WHAT render() WILL NOT DO
    * Fill a signature block. It prints what the source holds. If a signature
      row carries anything while the front matter status is not "approved", it
      refuses to render (SignatureError).
    * Insert an image from the source. There is no image syntax.
    * Carry a footer typed into the source. A trailing "*SESC Solutions Ltd · ...*"
      line is dropped because the footer is generated, and the build FAILS if the
      version typed in it disagrees with the front matter.
"""
import argparse, copy, datetime, io, os, re, shutil, subprocess, sys, tempfile, zipfile
from pathlib import Path

import yaml
from docx import Document
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn
from docx.shared import Twips

ROOT = Path(__file__).resolve().parent.parent
ASSETS = Path(__file__).resolve().parent / "assets"

# ---------------------------------------------------------------- house style
# BRAND-SPEC.md §2 and INTERIOR-SPEC.md. Do not change casually.
RED, BLACK, GREY, HAIRLINE, LABEL_FILL, CALLOUT_FILL = (
    "ED1D24", "231F20", "6A6A6A", "D8D8DC", "F4F4F5", "FBF2F1")
FONT = "Arial"
# Page geometry read from the signed branded POL-16 v1.2 (twips).
PAGE_W, PAGE_H = 11906, 16838
MARGIN_LR, MARGIN_TOP, MARGIN_BOTTOM, HDR_FTR = 1077, 1474, 1361, 567
TEXT_W = PAGE_W - 2 * MARGIN_LR          # 9752
NUM_IND = 460                            # hanging indent of a numbered paragraph
# Footer contact line, INTERIOR-SPEC.md "Page furniture".
FOOTER_LEFT = "SESC Solutions Ltd · 01747 445 509 · sescsolutions.co.uk"
UWP = "Uncontrolled when printed"

SERIES = {"POL": "POLICY", "PRO": "PROCEDURE", "WI": "WORK INSTRUCTION",
          "REG": "REGISTER", "FRM": "FORM", "REC": "RECORD", "TPL": "RECORD TEMPLATE",
          "CAP": "CAPABILITY STATEMENT", "CRP": "CARBON REDUCTION PLAN",
          "IMS": "MANAGEMENT SYSTEM"}
STD_LABEL = {"iso9001": "ISO 9001", "iso14001": "ISO 14001", "iso45001": "ISO 45001"}


class RenderError(Exception):
    pass


class SignatureError(RenderError):
    pass


# =========================================================== front matter
def read_source(path):
    text = Path(path).read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise RenderError(f"{path}: no YAML front matter")
    end = text.find("\n---", 3)
    fm = yaml.safe_load(text[3:end])
    body = text[end + 4:]
    for f in ("id", "title", "version", "status", "owner", "approver", "classification"):
        if not fm.get(f):
            raise RenderError(f"{path}: front matter has no '{f}'")
    return fm, body


def long_date(d):
    if isinstance(d, str):
        d = datetime.date.fromisoformat(d)
    return f"{d.day} {d.strftime('%B %Y')}"


def load_org():
    cfg = yaml.safe_load((ROOT / "portal" / "config.yaml").read_text(encoding="utf-8"))
    return cfg["organisation"]


# ============================================================ source parser
# Block types: h1, h2, para (plain), num, sub, cont, quote, callout, table, title
_NUM = re.compile(r"^(\d+)\.\s+(.*)$")
_SUB = re.compile(r"^(\([a-z]{1,4}\))\s+(.*)$")


def _indent(line):
    return len(line) - len(line.lstrip(" "))


def parse_blocks(body):
    """Line-based parser for the house Markdown. Deliberately NOT a Markdown
    library: every Markdown list renderer re-numbers ordered lists (trap 5)."""
    lines = body.split("\n")
    # drop a source-typed footer after the final horizontal rule
    blocks, i, in_num = [], 0, False
    n = len(lines)

    def gather(start, pred):
        j, out = start, []
        while j < n and lines[j].strip() and pred(lines[j]):
            out.append(lines[j])
            j += 1
        return out, j

    while i < n:
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1
            continue
        ind = _indent(line)
        if s == "---":
            blocks.append({"t": "hr"})
            in_num = False
            i += 1
            continue
        if s.startswith("#"):
            level = len(s) - len(s.lstrip("#"))
            text = s[level:].strip()
            blocks.append({"t": {1: "title", 2: "h1"}.get(level, "h2"), "text": text})
            in_num = False
            i += 1
            continue
        if s.startswith(">"):
            raw, i = gather(i, lambda l: l.strip().startswith(">"))
            paras, cur = [], []
            for l in raw:
                t = l.strip()[1:].strip()
                if not t:
                    if cur:
                        paras.append(" ".join(cur)); cur = []
                else:
                    cur.append(t)
            if cur:
                paras.append(" ".join(cur))
            blocks.append({"t": "quote" if (in_num and ind >= 3) else "callout",
                           "paras": paras})
            continue
        if s.startswith("|"):
            raw, i = gather(i, lambda l: l.strip().startswith("|"))
            rows = []
            for l in raw:
                cells = [c.strip() for c in l.strip().strip("|").split("|")]
                if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c) and any(cells):
                    continue
                rows.append(cells)
            blocks.append({"t": "table", "rows": rows, "indent": in_num and ind >= 3})
            continue
        m = _NUM.match(line) if ind == 0 else None
        if m:
            raw, i = gather(i + 1, lambda l: _indent(l) >= 2 and not _SUB.match(l.strip())
                            and not l.strip().startswith(("|", ">")))
            blocks.append({"t": "num", "n": int(m.group(1)),
                           "text": " ".join([m.group(2)] + [r.strip() for r in raw])})
            in_num = True
            continue
        m = _SUB.match(s)
        if m and ind >= 2:
            raw, i = gather(i + 1, lambda l: _indent(l) > ind and not _SUB.match(l.strip()))
            blocks.append({"t": "sub", "label": m.group(1),
                           "text": " ".join([m.group(2)] + [r.strip() for r in raw])})
            continue
        raw, i = gather(i + 1, lambda l: not l.strip().startswith(("|", ">", "#")))
        text = " ".join([s] + [r.strip() for r in raw])
        blocks.append({"t": "cont" if (in_num and ind >= 3) else "para", "text": text})
    return blocks


def strip_source_footer(blocks, fm):
    """A footer typed into the source is dropped — the footer is generated. The
    build fails if the version typed in it disagrees with the front matter."""
    if blocks and blocks[-1]["t"] == "para" and blocks[-1]["text"].startswith("*SESC Solutions Ltd"):
        typed = blocks[-1]["text"]
        m = re.search(r"\bv(\d+\.\d+)\b", typed)
        if m and m.group(1) != str(fm["version"]):
            raise RenderError(f"the footer typed into the source says v{m.group(1)}; "
                              f"the front matter says {fm['version']}. Fix the source.")
        return blocks[:-1], typed
    return blocks, None


def revision_row(blocks, version):
    """The revision-history row for this version: (date, author) or None."""
    for b in blocks:
        if b["t"] != "table" or not b["rows"]:
            continue
        head = [c.lower() for c in b["rows"][0]]
        if head[:2] == ["version", "date"]:
            for r in b["rows"][1:]:
                if strip_md(r[0]) == str(version):
                    return strip_md(r[1]), strip_md(r[2]) if len(r) > 2 else ""
    return None


# ============================================================ inline markdown
def strip_md(s):
    return re.sub(r"[*`]", "", s).strip()


def inline_runs(text):
    """-> [(chunk, bold, italic, code)]. ** bold, * italic, *** both, ` code."""
    out, buf = [], []
    bold = ital = code = False
    i = 0
    def flush():
        if buf:
            out.append(("".join(buf), bold, ital, code)); buf.clear()
    while i < len(text):
        c = text[i]
        if c == "`":
            flush(); code = not code; i += 1; continue
        if code:
            buf.append(c); i += 1; continue
        if text.startswith("***", i):
            flush(); bold = not bold; ital = not ital; i += 3; continue
        if text.startswith("**", i):
            flush(); bold = not bold; i += 2; continue
        if c == "*":
            flush(); ital = not ital; i += 1; continue
        buf.append(c); i += 1
    flush()
    return out


# ============================================================== XML helpers
def el(tag, attrs=None, *children):
    e = OxmlElement(tag)
    for k, v in (attrs or {}).items():
        e.set(qn(k), str(v))
    for c in children:
        if c is not None:
            e.append(c)
    return e


def rpr(size=19, bold=False, italic=False, color=BLACK, caps=False, spacing=None, code=False):
    r = el("w:rPr")
    face = "Courier New" if code else FONT
    r.append(el("w:rFonts", {"w:ascii": face, "w:hAnsi": face, "w:cs": face}))
    r.append(el("w:b", {"w:val": "1" if bold else "0"}))
    r.append(el("w:i", {"w:val": "1" if italic else "0"}))
    if caps:
        r.append(el("w:caps", {"w:val": "1"}))
    if spacing is not None:
        r.append(el("w:spacing", {"w:val": spacing}))
    r.append(el("w:color", {"w:val": color}))
    r.append(el("w:sz", {"w:val": size}))
    r.append(el("w:szCs", {"w:val": size}))
    return r


def run(text, **kw):
    r = el("w:r")
    r.append(rpr(**kw))
    parts = text.split("\t")
    for k, part in enumerate(parts):
        if k:
            r.append(el("w:tab"))
        if part:
            t = el("w:t")
            t.text = part
            t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
            r.append(t)
    return r


def ppr(before=0, after=80, line=360, ind_left=None, hanging=None, tab=None, jc=None,
        keep_next=False, border_bottom=None, keep_lines=False):
    p = el("w:pPr")
    if keep_next:
        p.append(el("w:keepNext"))
    if keep_lines:
        p.append(el("w:keepLines"))
    if border_bottom:
        b = el("w:pBdr")
        b.append(el("w:bottom", {"w:val": "single", "w:sz": border_bottom[0],
                                 "w:space": "2", "w:color": border_bottom[1]}))
        p.append(b)
    if tab is not None:
        tabs = el("w:tabs")
        tabs.append(el("w:tab", {"w:val": "left", "w:pos": tab}))
        p.append(tabs)
    p.append(el("w:spacing", {"w:before": before, "w:after": after, "w:line": line,
                              "w:lineRule": "auto"}))
    if ind_left is not None:
        a = {"w:left": ind_left}
        if hanging:
            a["w:hanging"] = hanging
        p.append(el("w:ind", a))
    if jc:
        p.append(el("w:jc", {"w:val": jc}))
    return p


def para(runs, **kw):
    p = el("w:p")
    p.append(ppr(**kw))
    for r in runs:
        p.append(r)
    return p


def md_runs(text, size=19, color=BLACK, bold=False, italic=False):
    return [run(chunk, size=size, color=color, bold=b or bold, italic=i or italic, code=c)
            for chunk, b, i, c in inline_runs(text)]


# ================================================================ builders
def heading(text, level):
    """H1: 'Part 1 — Title' -> red 'Part 1', black ' — Title', 17pt caps, red rule.
    H2: '3.1 Title' -> red '3.1', black title, 12pt caps. As POL-16 v1.2."""
    text = strip_md(text)
    m = re.match(r"^((?:Part|Annex|Appendix)\s+[A-Z0-9]+)(\s+—\s+.*)$", text) if level == 1 \
        else re.match(r"^(\d+(?:\.\d+)+)(\s+.*)$", text)
    lead, rest = (m.group(1), m.group(2)) if m else ("", text)
    if level == 2 and m:
        rest = "  " + rest.strip()
    size = 34 if level == 1 else 24
    runs = []
    if lead:
        runs.append(run(lead, size=size, bold=True, color=RED, caps=True))
    runs.append(run(rest, size=size, bold=True, color=BLACK, caps=True))
    if level == 1:
        return para(runs, before=280, after=80, line=252, keep_next=True,
                    border_bottom=("20", RED)), lead, rest
    return para(runs, before=240, after=40, line=252, keep_next=True), lead, rest


def contents_entry(lead, rest, level):
    runs = []
    if level == 1:
        if lead:
            runs.append(run(lead, size=17, bold=True, color=RED, caps=True))
        runs.append(run(rest if lead else rest.strip(), size=17, bold=True, caps=True))
        return para(runs, after=100, line=276, ind_left=0)
    runs.append(run(lead, size=17, color=RED))
    runs.append(run(rest, size=17))
    return para(runs, after=40, line=276, ind_left=200)


def _cell(width, fill=None):
    tc = el("w:tc")
    pr = el("w:tcPr")
    pr.append(el("w:tcW", {"w:type": "dxa", "w:w": width}))
    if fill:
        pr.append(el("w:shd", {"w:val": "clear", "w:color": "auto", "w:fill": fill}))
    tc.append(pr)
    return tc


def _cell_para(text, kind):
    """kind: head | label | value | value_bold"""
    if kind == "head":
        runs = [run(strip_md(text), size=16, bold=True, color="FFFFFF", caps=True, spacing=6)]
    elif kind == "label":
        runs = [run(strip_md(text), size=17, bold=True, color=GREY)]
    else:
        runs = md_runs(text, size=17, bold=(kind == "value_bold"))
    return para(runs, after=0, line=300)


def _tbl(widths, indent=0, borders=HAIRLINE, border_sz=4):
    t = el("w:tbl")
    pr = el("w:tblPr")
    pr.append(el("w:tblW", {"w:type": "dxa", "w:w": sum(widths)}))
    if indent:
        pr.append(el("w:tblInd", {"w:type": "dxa", "w:w": indent}))
    b = el("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        b.append(el(f"w:{side}", {"w:val": "single", "w:sz": border_sz, "w:space": "0",
                                  "w:color": borders}))
    pr.append(b)
    pr.append(el("w:tblLayout", {"w:type": "fixed"}))
    mar = el("w:tblCellMar")
    for side, w in (("top", 60), ("left", 100), ("bottom", 60), ("right", 100)):
        mar.append(el(f"w:{side}", {"w:w": w, "w:type": "dxa"}))
    pr.append(mar)
    t.append(pr)
    g = el("w:tblGrid")
    for w in widths:
        g.append(el("w:gridCol", {"w:w": w}))
    t.append(g)
    return t


def _widths(rows, total, label_cols=()):
    ncol = max(len(r) for r in rows)
    lens = []
    for c in range(ncol):
        L = [len(strip_md(r[c])) for r in rows if c < len(r)]
        lens.append(max(8, min(60, max(L) if L else 8)))
    w = [total * x / sum(lens) for x in lens]
    # never narrower than the longest word in the column (8pt caps ~ 125 twips a letter)
    floor = []
    for c in range(ncol):
        words = [wd for r in rows[:1] if c < len(r) for wd in strip_md(r[c]).split()]
        floor.append(max([900] + [len(wd) * 125 + 260 for wd in words]))
    w = [max(f, x) for f, x in zip(floor, w)]
    s = sum(w)
    w = [int(x * total / s) for x in w]
    w[-1] += total - sum(w)
    return w


SIG_LABELS = ("signature", "signed")


def table(rows, indent=False, status="draft"):
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    label_table = not any(strip_md(c) for c in rows[0])      # empty header -> label/value
    body = rows[1:] if label_table else rows
    total = TEXT_W - (NUM_IND if indent else 0)
    if label_table and ncol == 4:
        widths = [int(total * 0.22), int(total * 0.28), int(total * 0.22)]
        widths.append(total - sum(widths))
    else:
        widths = _widths(body, total)
    t = _tbl(widths, indent=NUM_IND if indent else 0)
    keep_whole = label_table and len(body) <= 8
    for ri, r in enumerate(body):
        tr = el("w:tr")
        trpr = el("w:trPr")
        trpr.append(el("w:cantSplit"))
        is_sig = strip_md(r[0]).lower().startswith(SIG_LABELS)
        if is_sig:
            trpr.append(el("w:trHeight", {"w:hRule": "atLeast", "w:val": 520}))
            if any(strip_md(c) for c in r[1:]) and status != "approved":
                raise SignatureError(
                    "the source carries content in a signature row while the front matter "
                    f"status is '{status}'. The renderer never fills a signature block.")
        head = (ri == 0 and not label_table)
        if head:
            trpr.append(el("w:tblHeader"))
        tr.append(trpr)
        for ci, c in enumerate(r):
            if head:
                kind, fill = "head", BLACK
            elif label_table and ci in (0, 2):
                kind, fill = "label", LABEL_FILL
            else:
                kind, fill = "value", None
            tc = _cell(widths[ci], fill)
            cp = _cell_para(c, kind)
            if keep_whole and ri < len(body) - 1:          # keep a label table on one page
                cp.find(qn("w:pPr")).insert(0, el("w:keepNext"))
            tc.append(cp)
            tr.append(tc)
        t.append(tr)
    return t


def callout(paras_md, indent=False, quote=False):
    """Blockquote. Top-level: the INTERIOR-SPEC callout (1.5pt red border, tint).
    Inside a numbered paragraph: a quoted passage, red rule on the left only."""
    w = TEXT_W - (NUM_IND if indent else 0)
    t = el("w:tbl")
    pr = el("w:tblPr")
    pr.append(el("w:tblW", {"w:type": "dxa", "w:w": w}))
    if indent:
        pr.append(el("w:tblInd", {"w:type": "dxa", "w:w": NUM_IND}))
    b = el("w:tblBorders")
    for side in ("top", "left", "bottom", "right"):
        if quote and side != "left":
            b.append(el(f"w:{side}", {"w:val": "nil"}))
        else:
            b.append(el(f"w:{side}", {"w:val": "single", "w:sz": 24 if quote else 12,
                                      "w:space": "0", "w:color": RED}))
    pr.append(b)
    pr.append(el("w:tblLayout", {"w:type": "fixed"}))
    mar = el("w:tblCellMar")
    for side, v in (("top", 100), ("left", 160), ("bottom", 60), ("right", 160)):
        mar.append(el(f"w:{side}", {"w:w": v, "w:type": "dxa"}))
    pr.append(mar)
    t.append(pr)
    g = el("w:tblGrid"); g.append(el("w:gridCol", {"w:w": w})); t.append(g)
    tr = el("w:tr"); trpr = el("w:trPr"); trpr.append(el("w:cantSplit")); tr.append(trpr)
    tc = _cell(w, LABEL_FILL if quote else CALLOUT_FILL)
    for ptxt in paras_md:
        tc.append(para(md_runs(ptxt, size=18), after=80, line=312))
    tr.append(tc); t.append(tr)
    return t


def spacer(after=120):
    return para([], after=after, line=240)


def page_break():
    p = el("w:p")
    r = el("w:r"); r.append(el("w:br", {"w:type": "page"})); p.append(r)
    return p


# ====================================================== header and footer
def _bar_cell(width, text_runs, jc=None, ind=None):
    tc = _cell(width, BLACK)
    p = el("w:p")
    pp = el("w:pPr")
    pp.append(el("w:spacing", {"w:before": 0, "w:after": 0}))
    if ind:
        pp.append(el("w:ind", ind))
    if jc:
        pp.append(el("w:jc", {"w:val": jc}))
    p.append(pp)
    for r in text_runs:
        p.append(r)
    tc.append(p)
    return tc


def _field(instr, size):
    kw = dict(size=size, bold=True, color="FFFFFF", spacing=8)
    out = []
    r = el("w:r"); r.append(rpr(**kw)); r.append(el("w:fldChar", {"w:fldCharType": "begin"})); out.append(r)
    r = el("w:r"); r.append(rpr(**kw)); it = el("w:instrText"); it.text = f" {instr} "
    it.set("{http://www.w3.org/XML/1998/namespace}space", "preserve"); r.append(it); out.append(r)
    r = el("w:r"); r.append(rpr(**kw)); r.append(el("w:fldChar", {"w:fldCharType": "separate"})); out.append(r)
    out.append(run("1", **kw))
    r = el("w:r"); r.append(rpr(**kw)); r.append(el("w:fldChar", {"w:fldCharType": "end"})); out.append(r)
    return out


def _bar_table(left_w, right_w, left_runs, right_runs, keyline):
    t = el("w:tbl")
    pr = el("w:tblPr")
    pr.append(el("w:tblW", {"w:type": "dxa", "w:w": left_w + right_w}))
    pr.append(el("w:tblInd", {"w:w": -MARGIN_LR, "w:type": "dxa"}))
    b = el("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        if side == keyline:
            b.append(el(f"w:{side}", {"w:val": "single", "w:sz": 18, "w:space": "0", "w:color": RED}))
        else:
            b.append(el(f"w:{side}", {"w:val": "none", "w:sz": 0, "w:space": "0"}))
    pr.append(b)
    pr.append(el("w:tblLayout", {"w:type": "fixed"}))
    mar = el("w:tblCellMar")
    for side, v in (("top", 120), ("left", 0), ("bottom", 120), ("right", 0)):
        mar.append(el(f"w:{side}", {"w:w": v, "w:type": "dxa"}))
    pr.append(mar)
    t.append(pr)
    g = el("w:tblGrid")
    g.append(el("w:gridCol", {"w:w": left_w})); g.append(el("w:gridCol", {"w:w": right_w}))
    t.append(g)
    tr = el("w:tr")
    tr.append(_bar_cell(left_w, left_runs, ind={"w:left": MARGIN_LR}))
    tr.append(_bar_cell(right_w, right_runs, jc="right", ind={"w:right": MARGIN_LR}))
    t.append(tr)
    return t


def _marking_para(marking):
    return para([run(marking, size=20, bold=True, caps=True, spacing=40)],
                 after=60, before=0, line=240, jc="center")


def header_xml(hdr, fm, marking, wm_rid):
    left = f"{fm['id']} · V{fm['version']} — {fm['title']}"
    right = "Draft — not issued" if fm["status"] == "draft" else (
        "In review — not issued" if fm["status"] == "in-review" else header_right(fm))
    kw = dict(size=14, bold=True, color="FFFFFF", caps=True, spacing=11)
    root = hdr._element
    for c in list(root):
        root.remove(c)
    if marking:
        root.append(_marking_para(marking))
    root.append(_bar_table(8344, 3561, [run(left, **kw)], [run(right, **kw)], "bottom"))
    # watermark: sesc-logo-dark at 7% on white, 374.4pt wide, 259.2pt from the top (POL-16)
    p = para([], after=0, before=0, line=240)
    r = el("w:r")
    r.append(parse_xml(
        '<w:pict xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        '<v:shape id="sesc_wm" type="#_x0000_t75" style="position:absolute;width:374.4pt;'
        'height:159.7pt;z-index:-251658752;mso-position-horizontal:center;'
        'mso-position-horizontal-relative:page;mso-position-vertical:absolute;'
        'mso-position-vertical-relative:page;margin-top:259.2pt" stroked="f" filled="f">'
        f'<v:imagedata r:id="{wm_rid}" o:title="SESC"/></v:shape></w:pict>'))
    p.append(r)
    root.append(p)


def header_right(fm):
    m = re.match(r"SESC-IMS-(\d{2})", fm["id"])
    if m:
        # SESC-IMS-00 is the manual, the overview ahead of the clause chapters 04-10 (D21).
        return "IMS · Manual" if m.group(1) == "00" else f"IMS · Clause {int(m.group(1))}"
    return SERIES.get(fm["id"].split("-")[1], "")


def footer_xml(ftr, marking):
    kw = dict(size=13, bold=True, color="FFFFFF", spacing=8)
    root = ftr._element
    for c in list(root):
        root.remove(c)
    right = [run(UWP, caps=True, **kw), run("  ·  ", **kw)] + _field("PAGE", 13) + \
        [run(" OF ", **kw)] + _field("NUMPAGES", 13)
    root.append(_bar_table(6904, 5001, [run(FOOTER_LEFT, caps=True, **kw)], right, "top"))
    root.append(_marking_para(marking) if marking else para([], after=0, line=240))


# ==================================================================== cover
# sesc_cover.make_cover(), constants UNCHANGED (BRAND-SPEC §4). Returns a PIL image.
def make_cover(doc_type, project, location, control_rows, header_note="", marking=None):
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    W, H, MARGIN, EDGE = 2480, 3508, 236, 150
    BLK, RD, GRY, INK = (35, 31, 32), (237, 29, 36), (106, 106, 106), (17, 17, 17)
    RULE, RULE_LIGHT = (150, 150, 150), (176, 176, 176)
    LINE_LEFT, LINE_RIGHT, RULE_T = 870, 730, 16
    # Opacities (BRAND-SPEC §4, as amended 24 Sep 2026 / decision D21): the white
    # wedge stays at 37%; the RED triangle runs at 70%. At 37% brand red over the
    # cover's light ground averages #E3979B and reads as pink (Steve Coffen, 2 Sep
    # 2026). 88% and solid were shown and rejected: red is accent only, and above
    # ~88% the triangle becomes a solid panel over a quarter of the page.
    WHITE_ALPHA = 95                     # 37%
    RED_ALPHA = 179                      # 70%
    RED_APEX, WHITE_APEX = (1050, 410), (1500, 1850)
    SCALE, OFFSET, CUT = 1.4, 100, 2400
    paths = {"bold": ["/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
                      "/Library/Fonts/Arial Bold.ttf",
                      "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                      "C:/Windows/Fonts/arialbd.ttf"],
             "regular": ["/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
                         "/Library/Fonts/Arial.ttf",
                         "/System/Library/Fonts/Supplemental/Arial.ttf",
                         "C:/Windows/Fonts/arial.ttf"]}

    def font(weight, size):
        for p in paths[weight]:
            if Path(p).exists():
                return ImageFont.truetype(p, size)
        raise RenderError("No Arial or Liberation Sans found. Install fonts-liberation.")

    def tracked(d, xy, text, fnt, fill, track=0, anchor="ls"):
        widths = [d.textlength(c, font=fnt) for c in text]
        x, y = xy
        if anchor == "rs":
            x -= sum(widths) + track * max(len(text) - 1, 0)
        for c, w in zip(text, widths):
            d.text((x, y), c, font=fnt, fill=fill, anchor="ls")
            x += w + track

    hero = Image.open(ASSETS / "sesc-3d-background.jpg").convert("RGB")
    base_h = int(W * hero.height / hero.width)
    sw, sh = int(W * SCALE), int(base_h * SCALE)
    art = hero.resize((sw, sh), Image.LANCZOS).crop(((sw - W) // 2, 0, (sw - W) // 2 + W, sh))
    plate = np.vstack([np.repeat(np.asarray(art)[0:1, :, :], OFFSET, axis=0), np.asarray(art)])
    total = OFFSET + sh
    ys, xs = np.mgrid[0:total, 0:W]
    line = LINE_LEFT - (LINE_LEFT - LINE_RIGHT) * xs / W
    tt = np.clip((ys - line) / (total - line), 0, 1)
    prof = np.where(ys < line, 1.0, 0.30 * (1 - tt) ** 1.5)
    a = plate.astype(np.float64) / 255.0
    rgb = np.power(a, 0.88)
    lum = (0.2126 * rgb[:, :, 0] + 0.7152 * rgb[:, :, 1] + 0.0722 * rgb[:, :, 2])[:, :, None]
    rgb = np.where(prof[:, :, None] < 1.0, rgb * 0.65 + lum * 0.35, rgb)
    bg = np.clip((rgb * prof[:, :, None] + (1 - prof[:, :, None])) * 255, 0, 255).astype(np.uint8)[:CUT]

    def aa_polygon(canvas, points, colour, alpha=255):
        xs_ = [p[0] for p in points]; ys_ = [p[1] for p in points]
        x0, y0 = max(int(min(xs_)) - 2, 0), max(int(min(ys_)) - 2, 0)
        x1, y1 = min(int(max(xs_)) + 2, canvas.width), min(int(max(ys_)) + 2, canvas.height)
        if x1 <= x0 or y1 <= y0:
            return
        w, h = x1 - x0, y1 - y0
        ss = max(2, min(8, int((48_000_000 / max(w * h, 1)) ** 0.5)))
        mask = Image.new("L", (w * ss, h * ss), 0)
        ImageDraw.Draw(mask).polygon([((px - x0) * ss, (py - y0) * ss) for px, py in points], fill=255)
        mask = mask.resize((w, h), Image.BOX)
        if alpha != 255:
            mask = mask.point(lambda v: v * alpha // 255)
        layer = Image.new("RGBA", (w, h), tuple(colour) + (0,))
        layer.putalpha(mask)
        canvas.alpha_composite(layer, (x0, y0))

    canvas = Image.new("RGB", (W, H), (255, 255, 255))
    canvas.paste(Image.fromarray(bg), (0, 0))
    canvas = canvas.convert("RGBA")
    ax, ay = RED_APEX
    pts = [(ax + ay, 0), (W, 0)]
    exit_y = ay + (W - ax)
    pts += [(W, exit_y)] if exit_y < CUT else [(W, CUT), (ax + (CUT - ay), CUT)]
    pts.append((ax, ay))
    aa_polygon(canvas, pts, RD, RED_ALPHA)
    wx, wy = WHITE_APEX
    aa_polygon(canvas, [(0, wy - wx), (wx, wy), (0, wy + wx)], (255, 255, 255), WHITE_ALPHA)
    aa_polygon(canvas, [(0, LINE_LEFT), (W, LINE_RIGHT), (W, LINE_RIGHT + RULE_T),
                        (0, LINE_LEFT + RULE_T)], RD)
    canvas = canvas.convert("RGB")
    d = ImageDraw.Draw(canvas)
    logo = Image.open(ASSETS / "sesc-logo-reversed.png")
    lw = 620
    lg = logo.resize((lw, int(lw / (logo.width / logo.height))), Image.LANCZOS)
    canvas.paste(lg, (EDGE, 130), lg)
    tracked(d, (W - EDGE, 340), doc_type[0], font("bold", 112), (255, 255, 255), 4, "rs")
    if len(doc_type) > 1:
        tracked(d, (W - EDGE, 450), doc_type[1], font("regular", 78), (255, 255, 255), 16, "rs")
    tracked(d, (W - EDGE, 578), "SESC SOLUTIONS LTD", font("regular", 38), (255, 230, 230), 6, "rs")
    if header_note:
        tracked(d, (W - EDGE, 636), header_note, font("regular", 38), (255, 230, 230), 6, "rs")
    d.text((MARGIN, 1600), project[0], font=font("bold", 118), fill=BLK, anchor="ls")
    if len(project) > 1:
        d.text((MARGIN, 1725), project[1], font=font("bold", 118), fill=BLK, anchor="ls")
    d.rectangle([MARGIN, 1785, MARGIN + 380, 1801], fill=RD)
    tracked(d, (MARGIN, 1890), location, font("regular", 48), GRY, 6)
    y0, rh, split = 2400, 100, MARGIN + 800
    y1 = y0 + rh * len(control_rows)
    d.rectangle([MARGIN, y0, W - MARGIN, y1], outline=RULE, width=3)
    d.line([split, y0, split, y1], fill=RULE, width=2)
    for i, (label, value) in enumerate(control_rows):
        y = y0 + i * rh
        if i:
            d.line([MARGIN, y, W - MARGIN, y], fill=RULE_LIGHT, width=2)
        tracked(d, (MARGIN + 36, y + rh // 2 + 10), label, font("regular", 30), GRY, 4)
        d.text((split + 36, y + rh // 2 + 12), value, font=font("regular", 38), fill=INK, anchor="ls")
    d.rectangle([MARGIN, 3290, W - MARGIN, 3298], fill=RD)
    footer = f"SESC SOLUTIONS LTD  •  {' '.join(doc_type)}  •  UNCONTROLLED WHEN PRINTED"
    tracked(d, (MARGIN, 3370), footer, font("regular", 30), GRY, 3)
    if marking:
        for band_y in (0, H - 60):
            d.rectangle([0, band_y, W, band_y + 60], fill=(30, 30, 30))
            tracked(d, (W // 2 - 240, band_y + 42), marking, font("regular", 34), (255, 255, 255), 6)
    return canvas, font


def wrap_title(title, font_fn, max_w=1950):
    """Split the title over at most two cover lines, as POL-16 does."""
    from PIL import Image, ImageDraw
    d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    f = font_fn("bold", 118)
    if d.textlength(title, font=f) <= max_w and len(title) <= 22:
        return (title,)
    words = title.split()
    best = None
    for k in range(1, len(words)):
        a, b = " ".join(words[:k]), " ".join(words[k:])
        wa, wb = d.textlength(a, font=f), d.textlength(b, font=f)
        if wa <= max_w and wb <= max_w:
            score = abs(wa - wb) + (0 if wa <= wb else 200)
            if best is None or score < best[0]:
                best = (score, (a, b))
    if best is None:
        raise RenderError(f"title {title!r} does not fit the cover in two lines")
    return best[1]


def watermark_png():
    import numpy as np
    from PIL import Image
    b = np.array(Image.open(ASSETS / "sesc-logo-dark.png").convert("RGBA")).astype(float)
    alpha = b[..., 3:] / 255.0
    on_white = b[..., :3] * alpha + 255 * (1 - alpha)
    out = 255 - (255 - on_white) * 0.07                       # 7% opacity (INTERIOR-SPEC)
    buf = io.BytesIO()
    Image.fromarray(np.clip(out, 0, 255).astype("uint8"), "RGB").save(buf, "PNG")
    buf.seek(0)
    return buf


# ================================================================ controls
def control_fields(fm, blocks):
    """Everything the cover and the page-3 control table print, from the front
    matter. For a draft, nothing is printed that implies issue or approval."""
    status = fm["status"]
    version = str(fm["version"])
    rev = revision_row(blocks, version)
    if fm.get("revised"):
        rev_date = long_date(fm["revised"])
        if rev and rev[0] != rev_date:
            raise RenderError(f"front matter revised {rev_date} disagrees with the revision "
                              f"history row for {version}: {rev[0]}")
    elif rev:
        rev_date = rev[0]
    else:
        raise RenderError(f"no revision date for version {version}: add 'revised:' to the "
                          "front matter or a revision history row for this version")
    prepared = fm.get("prepared_by") or (rev[1] if rev else "")
    if not prepared:
        raise RenderError("no author: add 'prepared_by:' to the front matter")
    issued = status in ("approved", "superseded")
    return {
        "reference": fm["id"],
        "title": fm["title"],
        "version": version,
        "status": status,
        "revision": version if issued else f"{version} — {status.upper()}, NOT ISSUED",
        "revision_date": rev_date,
        "owner": fm["owner"],
        "prepared_by": prepared,
        "approved_by": fm["approver"] if issued else f"Not yet approved ({fm['approver']})",
        "issue_date": long_date(fm["issued"]) if issued else "Not issued",
        "next_review": long_date(fm["next_review"]) if issued else "Set on issue",
        "classification": str(fm["classification"]).capitalize(),
        "marking": "OFFICIAL-SENSITIVE" if fm.get("official_sensitive") else None,
    }


def cover_note(fm):
    m = re.match(r"SESC-IMS-(\d{2})", fm["id"])
    stds = "  ·  ".join(STD_LABEL[k] for k in (fm.get("clauses") or {}) if k in STD_LABEL)
    if m:
        lead = "MANUAL" if m.group(1) == "00" else f"CLAUSE {int(m.group(1))}"
        return f"{lead}  //  {stds}".upper()
    return stds.upper()


# ================================================================== render
def render(src, out_dir=None, pdf=False):
    src = Path(src)
    fm, body = read_source(src)
    blocks = parse_blocks(body)
    blocks, typed_footer = strip_source_footer(blocks, fm)
    titles = [b for b in blocks if b["t"] == "title"]
    if titles and fm["title"] not in titles[0]["text"]:
        raise RenderError(f"the source title {titles[0]['text']!r} does not carry the front "
                          f"matter title {fm['title']!r}")
    cf = control_fields(fm, blocks)
    org = load_org()
    out_dir = Path(out_dir or ROOT / "out" / "render")
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{fm['id']}-v{cf['version']}" + ("" if cf["status"] in ("approved", "superseded")
                                                else f"-{cf['status'].upper()}")
    docx_path = out_dir / f"{stem}.docx"

    doc = Document()
    body_el = doc.element.body
    for c in list(body_el):
        if c.tag != qn("w:sectPr"):
            body_el.remove(c)
    sect_final = body_el.find(qn("w:sectPr"))

    def add(e):
        sect_final.addprevious(e)

    # ---- cover, its own section, zero margins, no header or footer
    series = fm["id"].split("-")[1]
    img, font_fn = make_cover(
        doc_type=(SERIES.get(series, "DOCUMENT"),),
        project=wrap_title(fm["title"], lambda w, s: _font_for(w, s)),
        location="SHAFTESBURY, DORSET",
        header_note=cover_note(fm),
        marking=cf["marking"],
        control_rows=[("DOCUMENT OWNER", cf["owner"]),
                      ("DOCUMENT REFERENCE", cf["reference"]),
                      ("REVISION", cf["revision"]),
                      ("REVISION DATE", cf["revision_date"]),
                      ("PREPARED BY", cf["prepared_by"]),
                      ("APPROVED BY", cf["approved_by"])])
    buf = io.BytesIO(); img.save(buf, "PNG"); buf.seek(0)
    cover_rid, _ = doc.part.get_or_add_image(buf)
    p = para([], after=0, before=0, line=240, ind_left=0)
    r = el("w:r")
    r.append(parse_xml(
        '<w:pict xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        '<v:shape id="sesc_cover" type="#_x0000_t75" style="position:absolute;left:0;top:0;'
        'width:595.28pt;height:841.89pt;z-index:-251657728;mso-position-horizontal:left;'
        'mso-position-horizontal-relative:page;mso-position-vertical:top;'
        'mso-position-vertical-relative:page" stroked="f">'
        f'<v:imagedata r:id="{cover_rid}" o:title="SESC cover"/></v:shape></w:pict>'))
    p.append(r)
    add(p)
    # the section break paragraph that closes the cover section
    sb = el("w:p"); spr = el("w:pPr")
    cover_sect = copy.deepcopy(sect_final)
    spr.append(cover_sect); sb.append(spr); add(sb)

    # ---- contents, generated (trap 1: no TOC field)
    add(heading("Contents", 1)[0])
    for b in blocks:
        if b["t"] in ("h1", "h2"):
            _, lead, rest = heading(b["text"], 1 if b["t"] == "h1" else 2)
            add(contents_entry(lead, rest, 1 if b["t"] == "h1" else 2))
    add(page_break())

    # ---- page 3: registration line and the control table, from front matter
    reg = (f"Registered in England & Wales, company number {org['company_number']}  ·  "
           f"{' '.join(str(org['registered_office']).split())}")
    add(para([run(reg, size=16, color=GREY)], after=200, line=276,
             border_bottom=("6", HAIRLINE)))
    ctl = [["", "", "", ""],
           ["Document reference", f"**{cf['reference']}**", "Version", f"**Version {cf['revision']}**"],
           ["Document title", cf["title"], "Revision date", cf["revision_date"]],
           ["Document owner", cf["owner"], "Issue date", cf["issue_date"]],
           ["Approved by", cf["approved_by"], "Next review", cf["next_review"]],
           ["Prepared by", cf["prepared_by"], "Classification", cf["classification"]]]
    add(table(ctl, status=cf["status"]))
    add(spacer(200))

    # ---- body
    prev = None
    for k, b in enumerate(blocks):
        t = b["t"]
        nxt = blocks[k + 1]["t"] if k + 1 < len(blocks) else None
        # a paragraph that introduces a quote or a table stays on its page
        keep = nxt in ("quote", "table") and t in ("num", "cont", "sub")
        if t in ("hr", "title"):
            continue
        if t == "h1":
            add(heading(b["text"], 1)[0])
        elif t == "h2":
            add(heading(b["text"], 2)[0])
        elif t == "num":
            add(para([run(f"{b['n']}.\t", size=19, bold=True)] + md_runs(b["text"]),
                     after=80, line=360, ind_left=NUM_IND, hanging=NUM_IND, tab=NUM_IND,
                     keep_next=keep))
        elif t == "sub":
            add(para([run(f"{b['label']}\t", size=19, bold=True)] + md_runs(b["text"]),
                     after=80, line=360, ind_left=2 * NUM_IND, hanging=NUM_IND, tab=2 * NUM_IND,
                     keep_next=keep))
        elif t == "cont":
            add(para(md_runs(b["text"]), after=80, line=360, ind_left=NUM_IND, keep_next=keep))
        elif t == "para":
            add(para(md_runs(b["text"], italic=(prev is None)), after=120, line=360))
        elif t == "table":
            add(table(b["rows"], indent=b["indent"], status=cf["status"]))
            add(spacer(80))
        elif t == "callout":
            add(callout(b["paras"]))
            add(spacer(80))
        elif t == "quote":
            add(callout(b["paras"], indent=True, quote=True))
            add(spacer(80))
        prev = t

    # ---- sections: [0] cover, [1] body
    secs = doc.sections
    cover_s, body_s = secs[0], secs[1]
    for s in (cover_s, body_s):
        s.page_width, s.page_height = Twips(PAGE_W), Twips(PAGE_H)
    cover_s.top_margin = cover_s.bottom_margin = cover_s.left_margin = cover_s.right_margin = Twips(0)
    cover_s.header_distance = cover_s.footer_distance = Twips(0)
    body_s.top_margin, body_s.bottom_margin = Twips(MARGIN_TOP), Twips(MARGIN_BOTTOM)
    body_s.left_margin = body_s.right_margin = Twips(MARGIN_LR)
    body_s.header_distance = body_s.footer_distance = Twips(HDR_FTR)
    body_s.start_type = WD_SECTION.NEW_PAGE
    cover_s.header.is_linked_to_previous = False
    cover_s.footer.is_linked_to_previous = False
    body_s.header.is_linked_to_previous = False
    body_s.footer.is_linked_to_previous = False
    wm_rid, _ = body_s.header.part.get_or_add_image(watermark_png())
    header_xml(body_s.header, fm, cf["marking"], wm_rid)
    footer_xml(body_s.footer, cf["marking"])

    cp = doc.core_properties
    cp.title = f"{fm['id']} {fm['title']} v{cf['version']}"
    cp.author = cf["prepared_by"]
    cp.subject = "SESC Integrated Management System"
    cp.comments = f"Generated by build/render_docx.py from {src.as_posix()}. Do not edit; edit the source."
    doc.save(docx_path)
    result = {"docx": docx_path, "fields": cf, "typed_footer_dropped": typed_footer}
    if pdf:
        result["pdf"] = to_pdf(docx_path, out_dir)
    return result


_FONT_CACHE = {}


def _font_for(weight, size):
    from PIL import ImageFont
    paths = {"bold": ["/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
                      "/Library/Fonts/Arial Bold.ttf",
                      "/System/Library/Fonts/Supplemental/Arial Bold.ttf"],
             "regular": ["/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
                         "/Library/Fonts/Arial.ttf",
                         "/System/Library/Fonts/Supplemental/Arial.ttf"]}
    for p in paths[weight]:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    raise RenderError("No Arial or Liberation Sans found. Install fonts-liberation.")


def soffice():
    for c in ("soffice", "libreoffice", "/Applications/LibreOffice.app/Contents/MacOS/soffice"):
        p = shutil.which(c) or (c if os.path.exists(c) else None)
        if p:
            return p
    return None


def to_pdf(docx_path, out_dir):
    exe = soffice()
    if not exe:
        raise RenderError("LibreOffice (soffice) not found: cannot render PDF")
    with tempfile.TemporaryDirectory() as prof:
        subprocess.run([exe, f"-env:UserInstallation=file://{prof}", "--headless",
                        "--convert-to", "pdf", "--outdir", str(out_dir), str(docx_path)],
                       check=True, capture_output=True, timeout=240)
    pdf = Path(out_dir) / (Path(docx_path).stem + ".pdf")
    if not pdf.exists():
        raise RenderError("LibreOffice produced no PDF")
    return pdf


# ============================================================== amend API
# Ported from policy_editor.py for amending the legacy branded .docx estate in
# place (CLAUDE.md §5: amend, never regenerate). See its CHANGE LOG, carried
# forward here in summary: the letter counter resets at a heading; the footer
# issue date is replaced with the version; substitution is run by run so the
# PAGE / NUMPAGES fields survive. VERIFY AFTER EVERY RUN: render to PDF and read
# a body page and the branded cover as images.
W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _all_paragraphs(doc):
    for p in doc.paragraphs:
        yield p
    for tb in doc.tables:
        for row in tb.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    yield p


def replace_runs(doc, pairs, must_all_hit=True):
    """Replace exact substrings run by run. Raises on a needle that hits nothing,
    because a silent no-op is how a wrong document gets issued."""
    counts = {old: 0 for old, _ in pairs}
    for p in _all_paragraphs(doc):
        for r in p.runs:
            for old, new in pairs:
                if old in r.text:
                    counts[old] += r.text.count(old)
                    r.text = r.text.replace(old, new)
    missed = [o for o, c in counts.items() if c == 0]
    if must_all_hit and missed:
        raise RenderError("replace_runs found NOTHING for: " + ", ".join(map(repr, missed)))
    return counts


def append_para(doc, startswith, text, bold=False):
    for p in doc.paragraphs:
        if p.text.strip().startswith(startswith) and p.runs:
            src = p.runs[-1]
            new_r = copy.deepcopy(src._r)
            for t in new_r.findall(W_NS + "t") + new_r.findall(W_NS + "br"):
                new_r.remove(t)
            rp = new_r.find(W_NS + "rPr")
            if rp is None:
                rp = OxmlElement("w:rPr"); new_r.insert(0, rp)
            for tag in ("b", "bCs"):
                for e in rp.findall(W_NS + tag):
                    rp.remove(e)
            b = OxmlElement("w:b"); b.set(qn("w:val"), "1" if bold else "0"); rp.append(b)
            t = OxmlElement("w:t"); t.text = text
            t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve"); new_r.append(t)
            src._r.addnext(new_r)
            return 1
    raise RenderError(f"append_para: no paragraph starts with {startswith!r}")


def add_contents_entry(doc, after_startswith, text):
    """Legacy branded documents carry a cached TOC field (trap 1). A new heading
    does not appear in it until F9, so add the line explicitly."""
    for p in doc.paragraphs:
        if p.text.strip().startswith(after_startswith):
            new = copy.deepcopy(p._p)
            for r in new.findall(W_NS + "r")[1:]:
                new.remove(r)
            rs = new.findall(W_NS + "r")
            if rs:
                for t in rs[0].findall(W_NS + "t"):
                    t.text = ""
                rs[0].findall(W_NS + "t")[0].text = text if rs[0].findall(W_NS + "t") else None
            p._p.addnext(new)
            return 1
    raise RenderError(f"add_contents_entry: no entry starts with {after_startswith!r}")


def set_cell(cell, text):
    """Trap 4. An empty cell has no run to inherit from, and add_run() gives a run
    with NO formatting, which renders in the default face. Clone the formatting of
    the nearest styled run in the same row, else apply the house cell format."""
    par = cell.paragraphs[0]
    if par.runs:
        par.runs[0].text = text
        for r in par.runs[1:]:
            r.text = ""
        return
    donor = None
    tr = cell._tc.getparent()
    for tc in tr.findall(W_NS + "tc"):            # prefer a value cell (unshaded)
        shaded = tc.find(f"{W_NS}tcPr/{W_NS}shd") is not None
        for r in tc.iter(W_NS + "r"):
            if r.find(W_NS + "rPr") is not None and (donor is None or not shaded):
                donor = r.find(W_NS + "rPr")
                if not shaded:
                    break
    new_r = par.add_run(text)._r
    old = new_r.find(W_NS + "rPr")
    if old is not None:
        new_r.remove(old)
    rp = copy.deepcopy(donor) if donor is not None else rpr(size=17)
    for tag in ("b", "bCs"):
        for e in rp.findall(W_NS + tag):
            rp.remove(e)
    b = OxmlElement("w:b"); b.set(qn("w:val"), "0"); rp.insert(1, b)
    new_r.insert(0, rp)


def find_signature_table(doc):
    """Trap 2. Never table 1: POL-10/11/12 carry a content table there."""
    for tb in doc.tables:
        for row in tb.rows:
            first = row.cells[0].text.strip().lower()
            if first.startswith(SIG_LABELS):
                return tb
    return None


def patch_header_footer_text(docx_path, pairs):
    """Trap 3. Header and footer text inside a table or textbox is invisible to
    python-docx's paragraph API. Rewrite word/header*.xml and word/footer*.xml.
    pairs: [(regex, replacement)]. Returns the number of parts changed."""
    z = zipfile.ZipFile(docx_path)
    items = {n: z.read(n) for n in z.namelist()}
    z.close()
    touched = 0
    for n in list(items):
        if re.search(r"word/(header|footer)\d*\.xml$", n):
            s = items[n].decode("utf-8")
            s2 = s
            for pat, rep in pairs:
                s2 = re.sub(pat, rep, s2)
            if s2 != s:
                items[n] = s2.encode("utf-8")
                touched += 1
    if touched:
        with zipfile.ZipFile(docx_path, "w", zipfile.ZIP_DEFLATED) as zo:
            for n, b in items.items():
                zo.writestr(n, b)
    return touched


def patch_branded_cover(docx_path, new_revision, new_date, font_size=38):
    """The legacy branded cover is a full-page 2480x3508 PNG at word/media/image1.png;
    REVISION and REVISION DATE are pixels. Finds the six value-column text bands,
    whites out rows 3 and 4 and redraws them. Refuses unless exactly six bands
    are found, so a changed template is never painted over."""
    import numpy as np
    from PIL import Image, ImageDraw
    z = zipfile.ZipFile(docx_path)
    items = {n: z.read(n) for n in z.namelist()}
    z.close()
    key = "word/media/image1.png"
    if key not in items:
        return "no cover image — not a Branded copy?"
    im = Image.open(io.BytesIO(items[key])).convert("RGB")
    a = np.array(im)
    sub = a[2250:3100, 1000:2420]
    dark = sub.mean(axis=2) < 140
    rows = np.where(dark.any(axis=1))[0]
    if not len(rows):
        return "no text found in the cover value column"
    bands, start, prev = [], rows[0], rows[0]
    for r in rows[1:]:
        if r - prev > 6:
            bands.append((start, prev)); start = r
        prev = r
    bands.append((start, prev))
    if len(bands) != 6:
        return f"expected 6 rows, found {len(bands)} — cover template changed, ABORTED"
    d = ImageDraw.Draw(im)
    fnt = _font_for("regular", font_size)
    for idx, new in ((2, new_revision), (3, new_date)):
        top, bot = bands[idx][0] + 2250, bands[idx][1] + 2250
        seg = dark[bands[idx][0]:bands[idx][1] + 1]
        x0 = int(np.where(seg.any(axis=0))[0][0]) + 1000
        d.rectangle([x0 - 25, top - 22, x0 + 520, bot + 22], fill=(255, 255, 255))
        d.text((x0, top + 26), new, font=fnt, fill=(17, 17, 17), anchor="ls")
    buf = io.BytesIO(); im.save(buf, "PNG"); items[key] = buf.getvalue()
    with zipfile.ZipFile(docx_path, "w", zipfile.ZIP_DEFLATED) as zo:
        for n, b in items.items():
            zo.writestr(n, b)
    return f"cover patched to {new_revision} / {new_date}"


# ===================================================================== CLI
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("source", nargs="+", help="Markdown source(s) with front matter")
    ap.add_argument("--pdf", action="store_true", help="also render PDF with LibreOffice")
    ap.add_argument("--out", default=None, help="output folder (default out/render)")
    a = ap.parse_args(argv)
    rc = 0
    for s in a.source:
        try:
            r = render(s, a.out, a.pdf)
        except RenderError as e:
            print(f"FAIL  {s}: {e}")
            rc = 1
            continue
        print(f"OK    {s} -> {r['docx']}" + (f" and {r['pdf']}" if r.get("pdf") else ""))
        if r["typed_footer_dropped"]:
            print("      note: a footer typed into the source was dropped (the footer is generated)")
    return rc


if __name__ == "__main__":
    sys.exit(main())
