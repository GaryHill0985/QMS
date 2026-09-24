# CLAUDE.md — house rules for the SESC Integrated Management System

**Read this file and `SESC-IMS-Master-Register.md` before doing anything in this repository,
and write back to the register before you finish. In the same turn.**

This file holds the rules. The register holds the state. A decision that is not in one of
them did not happen — that lesson is carried over from the JOSCAR project, which lost a
settled decision, built one artefact twice, and has now had two copies of one document
silently drift apart three separate times.

---

## 1. Who

SESC Solutions Ltd, company number 07606236, Unit 19 Melbury Business Park, West Melbury,
Shaftesbury, Dorset SP7 0AF. Roofing, building fabric, mechanical, electrical and renewable
energy works. **Sole director: Steven A Coffen** — the only person who can approve or sign.
Gary Adam Hill is Fractional COO and owns this project. Craig Bartle is Contracts Manager and
holds the Quality Representative, Health and Safety Officer, Environmental Manager and
regulation 7 competent person appointments.

---

## 2. What you may and may not do

**May, without asking:**

- Read anything in this repository, in the TeraBox restore (`~/Documents/TeraBox Restore/SESC/SESC/`), on TeraBox and on the Drive.
- Draft new documents, registers, procedures and forms **as a pull request**.
- Build clause maps, gap reports, audit packs and checklists.
- Correct a demonstrable factual error in a **draft**, recording the correction in the register.

**Must not, ever:**

- **Sign anything, or fill a signature block.**
- Change an **issued** document without an explicit instruction naming the document and version.
- **Merge to `main`.** Every change is reviewed by a named human. An unreviewed AI commit to a
  controlled document is a finding waiting to happen.
- Move, rename or delete anything in the TeraBox restore (`~/Documents/TeraBox Restore/SESC/SESC/`) or on the Drive. The
  13 August 2026 Drive rename incident is the reason. This repository is a **new location**, not a
  reorganisation. **Never write IMS work into the TeraBox restore:** it has no `.git`, may be stale,
  and is read-only reference.
- State a certification, qualification or device capability from memory. Read it off the issuing
  body's own documentation.
- Claim ISO certification of any kind, BS 99001, NFRC membership, OFTEC or RECC currency, or
  Cyber Essentials. **None is held.**

**Approval of a controlled-document change: Steve approves, Gary authors and reviews.
Two named humans, and never Claude.**

---

## 3. The honesty convention — the most valuable thing SESC owns

POL-05 §A31, POL-13 §21, POL-16 Q24, POL-17 §13 and POL-18 §8 each carry a dated, explicit
inventory of the records that **do not exist**, with the date each will be created. POL-17 §13
goes further and distinguishes a true nil return from an absent record.

**Every management-system document in this repository carries one, in a section headed
"Records held, records not yet held".** Where a document asserts something in the present tense,
the record proving it must exist or the sentence moves into the not-yet-held section with a date.

**Never assert in a document something no record supports. If asked to, refuse and say why.**

The company has already had to record, in SESC-REG-01, that professional indemnity was declared
as £5,000,000 against an actual £250,000; that employee numbers were declared as 5, 7, 12, 18
and about 30 in different places; and that turnover was declared as £842,919, £1,000,000 and
£2,400,000. That history is the reason this rule exists.

**Nothing enters this repository carrying a POW, ITC, LARC or Unitspark reference.** Every
borrowed document adopted whole at SESC has had to be withdrawn — a landscaping firm's aspects
register, a fabrication workshop's forty-five COSHH assessments, a typhoon emergency plan, an
H&S Policy 2024 naming unconnected companies. **Borrowed material is used as structure, never
as content.**

---

## 4. House style — non-negotiable

Carried verbatim from the JOSCAR brief §12, because the twenty-one existing documents are
written this way and consistency is auditable.

- **"the Employer"** — never "the Company", never "SESC", in policy body text.
- **"employees & subcontractors"** with an ampersand.
- The **sole-director clause** appears in every governance document, in this form:
  *Where the Employer has only one director, any function reserved to the Board which requires
  independence from a person involved in the matter will be performed by the independent
  professional adviser named in the Approval block.*
- British English. **Numbered paragraphs.** Sentence case body text; letterspaced capitals for
  job titles, document types, locations and footers.
- Arial (Liberation Sans on Linux). Brand red `#ED1D24` as accent only — never body text, never
  large areas. Brand black `#231F20`. **`BRAND-SPEC.md` is authoritative for colour, logo and
  cover geometry. Do not redesign the cover system** — the angle, the two 45° triangles at 37%
  opacity and the control block are settled.
- Six-field control block and an *uncontrolled when printed* footer on every controlled document.
  `OFFICIAL-SENSITIVE` bands head and foot on documents for defence sites, **repeated on every page**.

---

## 5. Document control

- **Series:** `SESC-POL-nn` policies · `SESC-PRO-nn` procedures · `SESC-WI-nn` work instructions ·
  `SESC-REG-nn` registers · `SESC-FRM-nn` forms · `SESC-REC-nn` records · `SESC-TPL-nn` record
  templates · `SESC-CAP-nn` capability sheets · `SESC-CRP-nn` carbon reduction plan ·
  **`SESC-IMS-nn` the Annex SL spine, where `nn` is the clause number it covers (04 to 10).**
- **Next free references, as at 24 September 2026** — `SESC-FRM-01` to `SESC-FRM-05` were taken by
  the record capture forms drafted in the portal session and confirmed by D14. `SESC-FRM-06`
  (toolbox talk), `SESC-FRM-07` (site inspection) and `SESC-WI-01` (how to log a record on site)
  were taken on 24 September 2026 for the Workspace record capture (workstream 1a). All are DRAFTS:
  `SESC-POL-20` · `SESC-PRO-01` · `SESC-WI-02` · `SESC-REG-08` · `SESC-FRM-08` · `SESC-REC-05` ·
  `SESC-TPL-05` · `SESC-CAP-015` · `SESC-IMS-05`.
  **Update this line the moment one is used.**
- **Never renumber an issued document. Never reuse a reference.**
- Everything downstream is generated from front matter — the page-1 control table, headers,
  footers, the site index, the review-due dashboard, the audit pack. **Nobody types a version
  number into a table again.** That is where version drift comes from.
- **File by ID and clause tag, never by folder.** Do not carry the JOSCAR `Documents\2.8 Quality\`
  taxonomy across; that is filing by another company's questionnaire and it has already produced
  filing defects.
- **Amend, never regenerate.** A document is edited in place with its history intact.
  Regenerating loses the revision table, the signature block and the branded cover.

---

## 6. Editions — get these right before writing a word

| Standard | Certify to | The trap |
|---|---|---|
| ISO 9001 | **9001:2015** + Amd 1:2024 | 9001:2026 publishes 16 September 2026. Accredited certification to it is unlikely before mid/late 2027. Certify to :2015 but **write 2026-ready**. |
| ISO 14001 | **14001:2026** | **14001:2015 was withdrawn on 15 April 2026.** Do not build to :2015 and do not accept a :2015 certificate. |
| ISO 45001 | **45001:2018** + Amd 1:2024 | A revision reached DIS ballot 9 August 2026; publication expected 2027. No reason to wait. |
| ISO/IEC 27001 | deferred to 2028+ | Cyber Essentials is taken in its place. For MOD work the contractual gate is DEFCON 658 / Cyber Essentials, not 27001. |

**Writing 2026-ready, which costs nothing now and saves a rebuild later:**

- Address **climate change explicitly and substantively** at 4.1, and interested parties'
  climate-related requirements at 4.2. For a building services contractor a "not relevant"
  conclusion is not defensible.
- Keep **risks and opportunities in separate registers or separate columns, never merged.**
  9001:2026 separates them.
- Carry a short **ethics and quality-culture** statement in the policy and in induction.
- Keep the documented-information structure loose enough to absorb 9001:2026's new Annex A.

**⚠ ISO 14001:2026 has not been read by anyone on this project.** Every 14001 clause reference
held is from the withdrawn :2015 edition. `standards/iso14001-2026.yaml` is marked
`verified: false` throughout and **must not be quoted to a customer or an auditor** until the
edition is bought and read. Do not let the CertiKit v3 toolkit and the :2015 clause map drift
apart silently.

**Language: companies are *certified*; certification bodies are *accredited*. Never write
"ISO 9001 accredited".**

---

## 7. The clause map is the point

Use exact clause numbers. Never cite a clause a document does not genuinely address — a padded
clause map produces a green gap report over an empty system, which is worse than a red one.

**Watch the five ISO 45001 dual "maintain AND retain" clauses — 6.1.2.2, 6.1.3, 6.2.2,
8.1.1 c) and 8.2 — and 10.3 e) "evidence of continual improvement".** These are the most
commonly missed requirements in the whole set, and 45001 is the most document-hungry of the three.

---

## 8. Personal data does not go in git

**Hard boundary.** Git history is immutable and replicated, which is exactly wrong for UK GDPR
erasure and for Article 9 special category data.

**Never in git — encrypted database only:** health surveillance, face-fit results, occupational
health, accident detail naming individuals, individual training records, DBS/BPSS outcomes,
right-to-work scans, disciplinary, grievance and Speak Up reports, diversity monitoring data.

**In git:** policies, procedures, work instructions, form templates; registers of *things*
(risks, assets, equipment, legal requirements); role-based competence *requirements*; supplier
and subcontractor organisations, categories and criteria; aggregate metrics and objectives.

`build/validate.py` fails the build if a file flagged `personal_data: true` or
`classification: confidential` is staged into a tracked path. **Enforced by CI, not by memory.**

---

## 9. Method — one workstream per chat

1. Read this file and `SESC-IMS-Master-Register.md`.
2. Take **one** item. Do not start a second. On the JOSCAR project the *simplest* section took
   a full session.
3. Work it end to end: draft → render → **verify** → write back.
4. **Verification discipline: a script exiting cleanly is not verification.** Render to PDF and
   read a body page *and* the branded cover **as images**. Four known traps live in
   `QinetiQ/JOSCAR/Reference/Section workflow method.md` (in the TeraBox restore, §11) §5 — the Branded TOC field, the signature table
   not being table 1, header text hidden in tables and textboxes, and `set_cell()` style in an
   empty cell.
5. Before finishing, update the register row, add findings, add tasks by owner, and write a
   completion note. **In the same turn.**

---

## 10. The things that are still not true, and must not be written as though they were

As at 18 August 2026:

- **No internal audit has ever been carried out**, under any system, for any period.
- **No management review has been minuted since 10 January 2023.**
- **No nonconformity and corrective action log of the Employer's own has been opened**
  before 31 August 2026.
- **The environmental aspects and impacts register does not exist.** The one held belongs to a
  landscaping firm. This is the defining ISO 14001 document and the highest-priority gap.
- **The compliance obligations register is dated 2020 with dead `Z:\` drive links.**
- **POL-08 Environmental is the only manual carrying no records-not-yet-held section**, and it
  asserts the existence of an aspects register, a legal register, a compliance evaluation, a
  risks & opportunities register, a waste register, an approved contractor register, an
  environmental action plan and an annual data set — **none of which exists.** It is the
  highest-priority document to remediate and the weakest link for ISO 14001.
- **ISO 45001 clause 5.4 worker consultation and participation** requires a mechanism and
  records of it operating, with non-managerial workers. A paragraph in POL-05 will not pass.
  This is the clause 45001 auditors test hardest and the one small firms fail.
- **The directly-employed headcount is disputed** — POL documents say "about thirteen", Gary
  believes eighteen. **Do not state a figure until it is confirmed and dated.**
- **Employers' liability and public liability certificates are recorded at POL-05 Annex C as
  NOT VERIFIED**, and the schedule and the broker letter give different policy numbers.
- **ICO data protection fee: recorded as absent**, but the public register has not been queried.

---

## 11. Where things live

**None of these files is in this repository, and several of the rules above tell you to use them.
Without this section a chat cannot find the document it is being told to obey.**

**From 24 September 2026 the working machine is the MacBook; the MSI Windows laptop is retired from
this project.** The `Desktop\SESC\...` paths used until then are read as the same folders inside the
**TeraBox restore at `~/Documents/TeraBox Restore/SESC/SESC/`**, which is read-only reference (§2). Paths below are macOS paths.
Give Gary **macOS Terminal (zsh)** commands, quote every path (`CLAUDE ISO` contains a space), and put
any interactive command — a passphrase prompt, a first SSH connection — in a block of its own.

| Thing | Location |
|---|---|
| **Architecture and build plan — AUTHORITATIVE for the repo design at §4–§9, and NOT to be re-derived** | `~/Documents/TeraBox Restore/SESC/SESC/ISO/SESC-IMS-Architecture-and-Build-Plan-v1.0.html` |
| **`BRAND-SPEC.md` and `INTERIOR-SPEC.md`** — authoritative for colour, logo, cover geometry and interior page design, cited at §4 above | `~/Documents/TeraBox Restore/SESC/SESC/DOCUMENT DESIGN INSTRUCTIONS CLAUDE/` |
| **The twenty-one signed documents**, to be migrated into `documents/` | `~/Documents/TeraBox Restore/SESC/SESC/QinetiQ/JOSCAR/Documents/` — **filed by JOSCAR questionnaire section. Do not carry that taxonomy forward.** On 18 August 2026 POL-01…04 were recorded as sitting inside `2.7 Environment & Sustainability\2.2 Human Resources\`, a filing defect; **in the TeraBox restore they sit in `Documents/2.2 Human Resources/`** (checked 24 Sep 2026). Confirm which is current before migrating them. |
| **The renderer to port** to `build/render_docx.py`, including **`patch_branded_cover()`** | `~/Documents/TeraBox Restore/SESC/SESC/QinetiQ/JOSCAR/Toolkit/policy_editor.py` |
| **The four rendering traps**, §5 — the Branded TOC field, the signature table not being table 1, header text hidden in tables and textboxes, `set_cell()` style in an empty cell | `~/Documents/TeraBox Restore/SESC/SESC/QinetiQ/JOSCAR/Reference/Section workflow method.md` |
| **The contradiction log** — known cross-document conflicts, do not rediscover them | In `~/Documents/TeraBox Restore/SESC/SESC/QinetiQ/JOSCAR/`: `JOSCAR Master Register.md` §5 · `Reference/Cross-document consistency findings v1.0 - 17 Aug 2026.md` · `Reference/Gary decisions on C2-C8 - 17 Aug 2026.md` |
| **The pre-written gap plan** | POL-05 §A31 · POL-13 §21 · POL-16 Q24 · POL-17 §13 · POL-18 §8 |
| **Standard texts held** | `~/Documents/TeraBox Restore/SESC/SESC/ISO/` — 9001:2015 (**licensed to Unitspark Ltd, single user — clause numbering may be used, clause TEXT may not be reproduced**), 14001:**2015, superseded**, 45001:2018, **BS 99001:2022**. **No 14001:2026 and no 27001 in any form.** |
| **CertiKit demo toolkits** | `~/Documents/TeraBox Restore/SESC/SESC/ISO/` — 9001 v3, 14001 v3 (**built for the 2026 edition**), 45001 v1-3, 27001 v13-1, 22301 v6-3, 20000 v10-1, **Cyber Essentials v7**. Every 27001 reference this project holds comes from the v13-1 guide, not from the standard. |
| **Reusable structure from prior builds — TeraBox, cloud only, no local sync folder** | `POW Environmental Services\Procedures and Registers\` · `Pow Property Developments\...\Forms, registers\{Forms,Policy,Procedures,Registers}` · `ITC CERTIFIED\...\0. Context and Governance\`. **Structure only, never content — see §3.** |
| **This repository** | `github.com/GaryHill0985/QMS`, and the working clone is **`~/Documents/SESC/ISO/CLAUDE ISO/` on the MacBook** (from 24 Sep 2026; previously `Desktop\SESC\ISO\CLAUDE ISO\` on the MSI) |

---

## 12. Rules that were nearly lost in the migration from the project instructions

Recorded here because they exist in no other file in this repository.

1. **The stop rule.** Gary Hill is not the director. **Where a task needs a decision that is
   reserved to the director, say so and stop rather than assuming.** This is wider than signing —
   it covers any decision reserved to the Board, any commitment of money, any acceptance of a
   contractual term, and any statement made to a customer or an insurer.

2. **How to treat the blockers.** The blockers at `SESC-IMS-Master-Register.md` §3 are named so
   that **no chat proposes work that quietly assumes they are closed. None of them is a chat's
   job.** Nothing in Phase 1 depends on them; everything in Phase 3 does.

3. **Signed commits.** The repository requires protected `main`, **signed commits**, and every
   change by pull request with a named human reviewer. Attribution of a controlled-document change
   is an audit point, and retrofitting signatures to history is worthless.

4. **ISO/IEC 27001, in full, so the deferral is not reopened by a chat that has forgotten why.**
   Certify to **27001:2022 + Amd 1:2024** when the time comes. The standard is stable — systematic
   review only, no revision approved — so **there is no penalty for deferring it**. Clause range
   4.1–10.2 plus Annex A controls **A.5.1–A.8.34**. Buy **ISO/IEC 27002:2022** with it; without
   27002 the control set cannot be applied. **The 27001:2013 transition expired 31 October 2025 —
   treat any 2013-era certificate presented by a supplier as worthless**, which is a live rule for
   supplier assessment today, not in 2028. MOD's September 2024 **Def Stan 05-138 ↔ 27001:2022
   mapping** lets 27001 evidence be reused in the Cyber Security Model SAQ — an accelerator, not
   the requirement.

5. **UKAS verification, as a standing rule and not only a register row.** UKAS-accredited only.
   Verify at `ukas.com/find-an-organisation` — Certification Bodies, open the Schedule of
   Accreditation, confirm the standard, **the edition**, and that the scope covers **IAF sector 28,
   construction**. Verify issued certificates at `certcheck.ukas.com`. IAF and ILAC merged into
   **Global ACI** on 1 January 2026 — check Global ACI MRA signatory status, not the old IAF MLA.
   UKAS publishes a list of bodies falsely claiming its accreditation. **An unaccredited
   certificate submitted to JOSCAR is worse than no certificate.**

6. **The gap report definition.** Any clause with no artefact, **or an artefact with zero records
   in the last twelve months**, goes red. That twelve-month staleness rule is the whole point — a
   clause covered by a document nobody has used in a year is not covered.

7. **Why a "not relevant" climate conclusion is not defensible, in six words each:** flooding,
   heat stress, Part L/F, F-gas, embodied carbon flow-down, and MOD net-zero via JOSCAR Zero.

8. **The honesty convention reaches beyond this repository.** Every management-system manual must
   carry a records-not-yet-held section, including the twenty-one legacy documents that are not
   yet migrated. `validate.py` can only warn on files it can see.

9. **The system is the deliverable; the certificates are a consequence.** This is the sentence
   that stops the project optimising for a certificate instead of for a business that works.

10. **Two claims were nearly overstated from memory already.** That is why §2 forbids stating a
    certification, qualification or device capability without reading it off the issuing body's
    own documentation.
