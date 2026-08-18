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

- Read anything in this repository, in `Desktop\SESC`, on TeraBox and on the Drive.
- Draft new documents, registers, procedures and forms **as a pull request**.
- Build clause maps, gap reports, audit packs and checklists.
- Correct a demonstrable factual error in a **draft**, recording the correction in the register.

**Must not, ever:**

- **Sign anything, or fill a signature block.**
- Change an **issued** document without an explicit instruction naming the document and version.
- **Merge to `main`.** Every change is reviewed by a named human. An unreviewed AI commit to a
  controlled document is a finding waiting to happen.
- Move, rename or delete anything in `Desktop\SESC` or on the Drive. The 13 August 2026 Drive
  rename incident is the reason. This repository is a **new location**, not a reorganisation.
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
- **Next free references, as at 18 August 2026:**
  `SESC-POL-20` · `SESC-PRO-01` · `SESC-WI-01` · `SESC-REG-07` · `SESC-FRM-01` · `SESC-REC-05` ·
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
   `JOSCAR\Reference\Section workflow method.md` §5 — the Branded TOC field, the signature table
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
