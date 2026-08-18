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
```

## Layout

```
system/       the Annex SL spine, clauses 4–10, written ONCE for all three standards
documents/    SESC-POL-nn, SESC-PRO-nn, SESC-WI-nn
registers/    SESC-REG-nn as YAML
forms/        SESC-FRM-nn schemas
standards/    the clause map as data, plus the front-matter schema
build/        validate.py, and (to come) render_docx.py, render_site.py, audit_pack.py
records/      SQLite + attachments — gitignored, see CLAUDE.md
```

## Status

**Phase 1, started 18 August 2026.** See `SESC-IMS-Master-Register.md` for state.

Read `CLAUDE.md` before changing anything.
