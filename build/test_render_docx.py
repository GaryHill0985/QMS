#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_render_docx.py — tests for build/render_docx.py.

    python3 build/test_render_docx.py            # from the repository root

The PDF tests need LibreOffice (soffice) and poppler (pdftotext). Where either is
missing they are reported as SKIPPED — never as passed. A skipped PDF test is
not verification; neither is a passing one on its own. Read the pages as images.

What is tested, and why:
  * F27 / F34 — every paragraph number and sub-paragraph label PRINTED in the
    PDF, and every one written into the DOCX, equals the source, in order. The
    source numbers are read straight off the Markdown lines, independently of
    the renderer's parser, so a parser bug cannot mark its own homework.
  * Requirement 1 — the control block, header and footer come from the front
    matter: a fixture whose version string appears nowhere in its body still
    prints that version in the header and control table.
  * Requirement 3 — "Uncontrolled when printed" in the footer, with the PAGE and
    NUMPAGES fields intact; OFFICIAL-SENSITIVE only when the front matter asks.
  * Requirement 4 — the signature block renders empty, no image other than the
    cover and the watermark is embedded, and a draft with a filled signature row
    is refused.
  * The four §5 traps: no TOC field; the signature table found by label not by
    index; header text inside a table is reached; set_cell() in an empty cell
    keeps the house face.
"""
import os, re, shutil, subprocess, sys, tempfile, textwrap, unittest, zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import render_docx as R  # noqa: E402
from docx import Document  # noqa: E402

IMS04 = ROOT / "system" / "4-context.md"
LEFT_MARGIN_PT = R.MARGIN_LR / 20.0                  # 53.85 pt
SUB_X_PT = (R.MARGIN_LR + R.NUM_IND) / 20.0          # 76.85 pt


def source_numbers(path):
    """Numbered paragraphs and sub-paragraph labels, read straight off the source
    lines. Front matter, tables and blockquotes are not paragraphs."""
    text = Path(path).read_text(encoding="utf-8")
    body = text[text.find("\n---", 3) + 4:]
    seq = []
    for line in body.split("\n"):
        m = re.match(r"^(\d+)\.\s", line)
        if m:
            seq.append(m.group(1) + ".")
            continue
        m = re.match(r"^\s{2,}(\([a-z]{1,4}\))\s", line)
        if m:
            seq.append(m.group(1))
    return seq


def docx_numbers(docx_path):
    seq = []
    for p in Document(docx_path).paragraphs:
        if p.runs:
            m = re.match(r"^(\d+\.|\([a-z]{1,4}\))\t$", p.runs[0].text)
            if m and p.runs[0].bold:
                seq.append(m.group(1))
    return seq


def pdf_numbers(pdf_path):
    """Labels printed at the paragraph-number and sub-label positions, each followed
    on the same line by text at the hanging indent. The second condition is what
    tells a paragraph label from the same characters sitting in a table cell."""
    out = subprocess.run(["pdftotext", "-bbox", str(pdf_path), "-"], capture_output=True,
                         text=True, check=True).stdout
    seq = []
    for page in out.split("<page ")[1:]:
        words = [(float(x), float(y), w) for x, y, w in
                 re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)"[^>]*>([^<]*)</word>', page)]
        found = []
        for x, y, w in words:
            if re.fullmatch(r"\d+\.", w):
                at, text_x = LEFT_MARGIN_PT, SUB_X_PT
            elif re.fullmatch(r"\([a-z]{1,4}\)", w):
                at, text_x = SUB_X_PT, SUB_X_PT + R.NUM_IND / 20.0
            else:
                continue
            if abs(x - at) >= 2.0:
                continue
            # text_x + 16: a leading symbol such as the warning sign has no text layer
            if any(abs(ny - y) < 2.0 and text_x - 2.0 < nx < text_x + 16.0 for nx, ny, _ in words):
                found.append((y, w))
        seq += [w for _, w in sorted(found)]            # top to bottom = reading order
    return seq


def part_text(docx_path, pattern):
    with zipfile.ZipFile(docx_path) as z:
        return "".join(z.read(n).decode("utf-8") for n in z.namelist() if re.search(pattern, n))


def xml_text(xml):
    return "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", xml))


FIXTURE = textwrap.dedent("""\
    ---
    id: SESC-PRO-99
    title: Renderer Test Procedure
    version: "7.4"
    status: approved
    owner: Contracts Manager
    approver: Managing Director
    issued: 2026-01-05
    revised: 2026-01-05
    prepared_by: G A Hill
    next_review: 2027-01-05
    classification: internal
    official_sensitive: {os}
    clauses:
      iso9001: ["7.5.1"]
    ---

    # SESC-PRO-99 · Renderer Test Procedure

    ## Part 1 — Purpose

    1. First paragraph. Nothing in this body names the version.

       | Column | Other |
       |---|---|
       | a | b |

    2. Second paragraph, after a table, which must print as 2 and not as 1.

       (a) a sub-paragraph;

       (b) another.

    ## Part 2 — Approval

    | | | | |
    |---|---|---|---|
    | **Approved by** | Steven A Coffen, Managing Director | **Date** | |
    | **Signature** | {sig} | | |
    """)


def write_fixture(d, os_flag="false", sig="", status=None, footer=None):
    txt = FIXTURE.format(os=os_flag, sig=sig)
    if status:
        txt = txt.replace("status: approved", f"status: {status}")
    if footer:
        txt += "\n---\n\n" + footer + "\n"
    p = Path(d) / "fixture.md"
    p.write_text(txt, encoding="utf-8")
    return p


class TestIMS04(unittest.TestCase):
    """Renders the real SESC-IMS-04 once."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        cls.pdf_ok = bool(R.soffice()) and bool(shutil.which("pdftotext"))
        cls.res = R.render(IMS04, cls.tmp, pdf=cls.pdf_ok)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def test_source_has_numbers(self):
        seq = source_numbers(IMS04)
        self.assertGreater(len([s for s in seq if s.endswith(".")]), 60)

    def test_docx_numbers_equal_source(self):
        """F27/F34 at the DOCX level: every number the renderer wrote."""
        self.assertEqual(docx_numbers(self.res["docx"]), source_numbers(IMS04))

    def test_pdf_numbers_equal_source(self):
        """F27/F34 at the PRINTED level: every number on the PDF page."""
        if not self.pdf_ok:
            self.skipTest("LibreOffice or pdftotext not installed — PDF numbering NOT checked")
        printed = pdf_numbers(self.res["pdf"])
        src = source_numbers(IMS04)
        self.assertEqual(printed, src,
                         f"printed {len(printed)} labels, source has {len(src)}")

    def test_numbers_are_the_source_numbers_not_a_count(self):
        """The source is sequential today; a gap must survive, not be closed up."""
        seq = [int(s[:-1]) for s in source_numbers(IMS04) if s.endswith(".")]
        self.assertEqual(seq, list(range(1, len(seq) + 1)))

    def test_no_toc_field(self):
        """Trap 1: the contents list is generated, not a stale cached TOC field."""
        self.assertNotIn("TOC \\o", part_text(self.res["docx"], r"word/document\.xml$"))

    def test_header_and_footer_from_front_matter(self):
        hdr = xml_text(part_text(self.res["docx"], r"word/header\d*\.xml$"))
        self.assertIn("SESC-IMS-04 · V0.3 — Context of the Organisation", hdr)
        self.assertIn("Draft — not issued", hdr)
        ftr_xml = part_text(self.res["docx"], r"word/footer\d*\.xml$")
        self.assertIn("Uncontrolled when printed", xml_text(ftr_xml))
        self.assertIn(" PAGE ", ftr_xml)
        self.assertIn(" NUMPAGES ", ftr_xml)
        self.assertNotIn("OFFICIAL-SENSITIVE", hdr + xml_text(ftr_xml))

    def test_draft_claims_no_issue_or_approval(self):
        f = self.res["fields"]
        self.assertEqual(f["issue_date"], "Not issued")
        self.assertTrue(f["approved_by"].startswith("Not yet approved"))
        self.assertIn("DRAFT", f["revision"])
        self.assertEqual(f["revision_date"], "24 September 2026")

    def test_signature_block_empty(self):
        doc = Document(self.res["docx"])
        tb = R.find_signature_table(doc)
        self.assertIsNotNone(tb, "approval table not found by label")
        for row in tb.rows:
            label = row.cells[0].text.strip().lower()
            if label.startswith("signature"):
                self.assertEqual([c.text.strip() for c in row.cells[1:]], ["", "", ""])
            if label.startswith(("approved by", "reviewed by")):
                self.assertEqual(row.cells[3].text.strip(), "", f"date filled on {label!r}")
            if label.startswith("reviewed by"):
                self.assertEqual(row.cells[1].text.strip(), "")

    def test_only_cover_and_watermark_images(self):
        with zipfile.ZipFile(self.res["docx"]) as z:
            media = [n for n in z.namelist() if n.startswith("word/media/")]
        self.assertEqual(len(media), 2, media)

    def test_source_footer_dropped(self):
        self.assertTrue(self.res["typed_footer_dropped"])
        body = xml_text(part_text(self.res["docx"], r"word/document\.xml$"))
        self.assertNotIn("Uncontrolled when printed", body)


class TestFixture(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_version_comes_from_front_matter(self):
        src = write_fixture(self.tmp)
        body = src.read_text().split("\n---\n", 1)[1]
        self.assertNotIn("7.4", body)
        res = R.render(src, self.tmp)
        hdr = xml_text(part_text(res["docx"], r"word/header\d*\.xml$"))
        self.assertIn("SESC-PRO-99 · V7.4 — Renderer Test Procedure", hdr)
        self.assertIn("Version 7.4", xml_text(part_text(res["docx"], r"word/document\.xml$")))
        self.assertEqual(res["fields"]["issue_date"], "5 January 2026")

    def test_numbers_survive_a_table(self):
        res = R.render(write_fixture(self.tmp), self.tmp)
        self.assertEqual(docx_numbers(res["docx"]), ["1.", "2.", "(a)", "(b)"])

    def test_a_gap_in_the_source_survives(self):
        """Mutation check on the check: if the renderer counted instead of copying,
        a source numbered 1, 2, 5 would print 1, 2, 3 and this would fail."""
        src = write_fixture(self.tmp)
        src.write_text(src.read_text().replace("2. Second paragraph", "5. Second paragraph"))
        res = R.render(src, self.tmp)
        self.assertEqual(docx_numbers(res["docx"]), ["1.", "5.", "(a)", "(b)"])
        self.assertEqual(docx_numbers(res["docx"]), source_numbers(src))

    def test_official_sensitive_only_on_request(self):
        res = R.render(write_fixture(self.tmp, "true"), self.tmp)
        hdr = xml_text(part_text(res["docx"], r"word/header\d*\.xml$"))
        ftr = xml_text(part_text(res["docx"], r"word/footer\d*\.xml$"))
        self.assertIn("OFFICIAL-SENSITIVE", hdr)
        self.assertIn("OFFICIAL-SENSITIVE", ftr)
        res2 = R.render(write_fixture(self.tmp, "false"), self.tmp)
        both = xml_text(part_text(res2["docx"], r"word/(header|footer)\d*\.xml$"))
        self.assertNotIn("OFFICIAL-SENSITIVE", both)

    def test_filled_signature_on_draft_refused(self):
        src = write_fixture(self.tmp, sig="S Coffen", status="draft")
        with self.assertRaises(R.SignatureError):
            R.render(src, self.tmp)

    def test_typed_footer_must_match(self):
        src = write_fixture(self.tmp, footer="*SESC Solutions Ltd · SESC-PRO-99 v7.3 · Uncontrolled when printed*")
        with self.assertRaises(R.RenderError):
            R.render(src, self.tmp)

    def test_trap2_signature_table_by_label(self):
        res = R.render(write_fixture(self.tmp), self.tmp)
        doc = Document(res["docx"])
        tb = R.find_signature_table(doc)
        self.assertIsNot(tb._tbl, doc.tables[0]._tbl, "table 0 is the control table")
        self.assertIsNot(tb._tbl, doc.tables[1]._tbl)

    def test_trap3_header_text_in_table_is_reached(self):
        res = R.render(write_fixture(self.tmp), self.tmp)
        doc = Document(res["docx"])
        # the paragraph API cannot see it ...
        hp = " ".join(p.text for s in doc.sections for p in s.header.paragraphs)
        self.assertNotIn("V7.4", hp)
        # ... the XML pass can
        n = R.patch_header_footer_text(res["docx"], [(r"V7\.4", "V7.5")])
        self.assertGreaterEqual(n, 1)
        self.assertIn("V7.5", xml_text(part_text(res["docx"], r"word/header\d*\.xml$")))

    def test_trap4_set_cell_empty_cell_keeps_house_face(self):
        res = R.render(write_fixture(self.tmp), self.tmp)
        doc = Document(res["docx"])
        tb = R.find_signature_table(doc)
        cell = tb.rows[0].cells[3]
        self.assertEqual(cell.text, "")
        R.set_cell(cell, "5 January 2026")
        rpr = cell.paragraphs[0].runs[0]._r.find(R.W_NS + "rPr")
        self.assertIsNotNone(rpr, "empty-cell run has no formatting")
        fonts = rpr.find(R.W_NS + "rFonts")
        self.assertEqual(fonts.get(R.qn("w:ascii")), "Arial")


class TestCoverOpacity(unittest.TestCase):
    """D21 (24 Sep 2026): the red triangle runs at 70%, the white wedge at 37%.
    Sampled below the diagonal rule, where the handover note measured it:
    37% averages #E3979B (pink); 70% averages about #E8575C."""

    def test_red_triangle_is_seventy_percent(self):
        import numpy as np
        img, _ = R.make_cover(("POLICY",), ("Test",), "SHAFTESBURY, DORSET", [("A", "b")] * 6)
        a = np.array(img).astype(float)
        red = a[1300:1500, 2250:2400].reshape(-1, 3).mean(0)
        target = np.array([0xE8, 0x57, 0x5C])
        pink = np.array([0xE3, 0x97, 0x9B])
        self.assertLess(np.abs(red - target).max(), 12, f"red triangle samples {red.round()}")
        self.assertGreater(np.abs(red - pink).max(), 40, "red triangle is back at 37% (pink)")


if __name__ == "__main__":
    unittest.main(verbosity=2)
