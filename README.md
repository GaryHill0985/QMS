# sesc-ims

The Integrated Management System of **SESC Solutions Ltd** (company number 07606236),
built to **ISO 9001:2015**, **ISO 14001:2026** and **ISO 45001:2018** as one system.

**Nothing in this repository is certified.** No certification body has assessed SESC.
Every document says so, and any statement to the contrary is wrong.

## What this is

Three layers, deliberately kept apart (Architecture & Build Plan §3):

| Layer | What | Where | Lifecycle |
|---|---|---|---|
| 1 Documents | Policies, procedures, work instructions, form templates | `system/`, `documents/`, `forms/` — Markdown + YAML front matter | ~40 files, monthly, approved before issue |
| 2 Registers | Risk, aspects, legal, assets, suppliers, competence, interested parties, objectives | `registers/` — YAML, so changes diff and are attributable | Data with a review cycle. **Never a Word table.** |
| 3 Records | Inspections, NCRs, toolbox talks, training, audits, reviews | `records/ims.db` — **not committed** | Thousands of rows, created daily |

The centre of gravity is layer 3. SESC does not have a document problem — twenty-one
good policies exist, all signed. What did not exist until August 2026 was a single
completed attendance record. Certification bodies issue certificates against records.

## The clause map

Every document, register and form declares in its front matter which clauses of which
standards it satisfies. From that one relation the build derives the audit pack, the
live gap report, reverse impact analysis and PQQ answers — with no human effort.

```
python3 build/validate.py          # CI gate: front matter, clause refs, review dates, personal data
python3 build/build_portal.py      # generate site/ — four audience builds
```

## The portal

`site/` is the management system as a thing you can open. Start at `site/index.html`.

**It is generated, not maintained.** Every page is written by `build/build_portal.py` from the
files above. Nobody can change a status by typing into it, and that is the point — a coverage
figure somebody can type over is a self-assessment, and self-assessments drift green. Change the
source and re-run. Never patch `site/`; the next run overwrites it.

Nine pages: an overview computed from the repository, the full 134-clause map with what declares
each clause, the document register across both estates, SESC-REG-05 and REG-06, the SESC-REG-02
assurance calendar sorted by what is due, one action list drawn from blockers, decisions,
findings and gaps, five record-capture forms, and an audit mode answering the twelve questions
an assessor actually asks.

It applies the gap report definition at `CLAUDE.md` §12.6 — **a clause covered by a document
nobody has used in a year is not covered** — using `portal/records-index.yaml`, which holds
record metadata only and never record content.

**Four builds, one repository.** `controller`, `approver`, `contributor`, `auditor` — each
generated separately with the content that audience must not see left out, so the auditor folder
is a folder you can hand to an auditor. **These are distribution audiences, not logins.** A
generated site cannot authenticate anybody and this one does not pretend to.

```
python3 build/build_portal.py --audience auditor     # just that build
python3 build/build_portal.py --asof 2026-12-01      # what it will look like then
git checkout <sha> && python3 build/build_portal.py  # what it looked like then
```

That last line is document control and the audit trail, and neither had to be written.

## Layout

```
system/       the Annex SL spine, clauses 4–10, written ONCE for all three standards
documents/    SESC-POL-nn, SESC-PRO-nn, SESC-WI-nn
registers/    SESC-REG-nn as YAML
forms/        SESC-FRM-nn schemas
standards/    the clause map as data, plus the front-matter schema
portal/       source data for the portal — config, the legacy estate, SESC-REG-02, actions, records index
build/        validate.py, build_portal.py, portal_theme.py, and (to come) render_docx.py
site/         THE PORTAL — generated, four audience builds. Never edited by hand.
records/      SQLite + attachments — gitignored, see CLAUDE.md
```

## Status

**Phase 1, started 18 August 2026.** See `SESC-IMS-Master-Register.md` for state.

Read `CLAUDE.md` before changing anything.
