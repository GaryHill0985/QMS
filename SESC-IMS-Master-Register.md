# SESC-IMS-Master-Register

**The state of the CLAUDE ISO project. v1.0 · 18 August 2026.**

> **This file did not exist until 18 August 2026**, although `SESC-IMS-Project-Instructions-v1.0.md`
> required every chat to read and write it from 17 August. That is the gap this file closes.
>
> **Every chat reads `CLAUDE.md` and this file before doing anything, and writes back to this file
> before it finishes — in the same turn.** `CLAUDE.md` holds the rules. This file holds the state.
> **A decision that is not in one of them did not happen.**
>
> **⚠ This file lives in ONE place: the repository root.** Do not keep a copy in the Claude
> Project, in the JOSCAR folder or on the Drive. Two copies of one thing have silently drifted
> apart three times on this project — the JOSCAR Master Register on 18 August was found stale
> against disk while carrying the same version number, and a chat drafted wrong findings from it.
> **If you are reading a copy that is not at the repository root, stop and go to the root copy.**

---

## 1. Where the work stands

| | |
|---|---|
| **Phase** | **1 — Foundations.** Started 18 August 2026, ten days early against the plan's 28 August. |
| **Why early** | Phase 0's gate was "JOSCAR submitted, nothing competes with it". All thirty JOSCAR sections read 100% on the evening of 17 August and the portal says *"You are now ready to submit your application."* Submission is held on three insurance attachments only, which is Gary's task and not a build task. Phase 0 is effectively clear. |
| **Certification route** | ISO 9001 + 14001 + 45001 as **one** integrated certification, 2027. ISO 27001 deferred to 2028+, Cyber Essentials taken now in its place. **Adopted. Not to be re-derived.** |
| **Standards editions** | 9001:**2015** (written 2026-ready) · 14001:**2026** · 45001:**2018**. See `CLAUDE.md` §6. |
| **Repository** | `sesc-ims`. Local only as at 18 August 2026 — **not yet pushed to GitHub.** Decision D4 outstanding. |
| **Master document count** | 21 signed (POL-01…19, CRP-01, REG-01) + REG-02, REG-03, REG-04 + REC-01…04 + TPL-01…04. |
| **This repository holds** | 3 controlled source files, 134 clauses across 3 standards, CI passing. |

---

## 2. What changed on 18 August 2026 — session 1 of the QMS build

**Workstream taken:** Scope and Context (gap-register items S01 and S02), end to end.

| Built | Where | Status |
|---|---|---|
| Repository skeleton, `.gitignore`, `README.md` | `sesc-ims/` | Done |
| **`CLAUDE.md`** — house rules, style, doc control, editions, personal-data boundary, and the list of things that are still not true | `sesc-ims/CLAUDE.md` | Done |
| **Clause map as data** — 9001:2015 (62 clauses), 45001:2018 (40), 14001:2026 (32, all `verified: false`) | `standards/*.yaml` | Done |
| Front-matter schema | `standards/front-matter-schema.yaml` | Done |
| **`SESC-IMS-04` Context of the Organisation** — scope statement, issues, interested parties, 4.4, the 8.3 applicability determination, and a records-not-yet-held inventory | `system/4-context.md` | **DRAFT v0.1. Not approved, not issued.** |
| **`SESC-REG-05` Interested Parties Register** — 15 parties, 43 requirements, each with obligation type, evidence and gap | `registers/interested-parties.yaml` | Draft v0.1 |
| **`SESC-REG-06` Issues Register** — 30 issues, risks and opportunities in **separate fields**, 9 of them climate | `registers/issues.yaml` | Draft v0.1 |
| **`build/validate.py`** + CI workflow — front matter, clause refs, dates, house style, and the personal-data guard | `build/`, `.github/workflows/` | Done, and **tested against a deliberately broken file: all 9 guards fire and the build exits 1.** |
| This register | repository root | Done |

**Decisions taken this session, recorded so no chat reverses them:**

1. **A new document series, `SESC-IMS-nn`, for the Annex SL spine**, where `nn` is the clause
   number it covers — IMS-04 context through IMS-10 improvement. The alternative was to number the
   scope document `SESC-POL-20`, which would have filed a scope statement as a policy. **Gary to
   confirm or overturn.**
2. **Clause 4 is written once for all three standards**, not three times. Three context documents
   would produce three scopes and is four systems in one folder.
3. **ISO 9001 clause 8.3 is IN SCOPE and no non-applicability is claimed.** The determination rests
   on POL-16 Q4 §19, POL-16 Annex B's seven-year design record retention, SESC-CAP-008, and the
   insurer's own-design-build declaration at 80% of turnover. See `system/4-context.md` Part 7.
4. **Climate change is determined to be a relevant issue**, expressly and substantively, with
   eight issues behind the determination. Recorded at `registers/issues.yaml` CLI-00 to CLI-08.
5. **Headcount is not stated anywhere in this repository** until one figure is established from the
   payroll with the date it changed.

---

## 3. Blockers — the four, restated with what has actually moved

| # | Blocker | Position at 18 August 2026 |
|---|---|---|
| B1 | Appoint the independent professional adviser | **CLOSED ON NAMING.** Simon Davies FCCA of Rapture Accounts Limited, confirmed 17 August. **NOT CLOSED ON DOCUMENTS: twenty documents still carry a blank adviser row and their branded PDFs must be rebuilt.** A name typed into a `.docx` does not reach a PDF already rendered. |
| B2 | Sign the twenty-one documents | **CLOSED.** All 21 signed; every signature verified individually against the rendered PDF at 130 dpi on 17 August 2026. |
| B3 | Zero operating history | **OPEN, and it is the long pole.** The first quarter in which the Assurance Calendar is fully operated is the quarter ending 30 September 2026. A certification body wants roughly three months of the system running, one full internal audit round and one management review before Stage 2. |
| B4 | The ISO 14001 edition problem | **OPEN. The Employer does not hold ISO 14001:2026 and nobody on this project has read it.** Every 14001 clause reference held is carried from the withdrawn :2015 edition. **Buy it before writing any EMS document.** |
| B5 | A second competent person | **OPEN.** No internal auditor is trained. Book two onto the CQI/IRCA two-day course for November 2026, ~£1,130–£1,255 inc VAT each. |
| B6 | Workspace 2-step verification | **UNVERIFIED.** Recorded as off on 17 August. Five minutes. Nobody has confirmed it since. |

---

## 4. Open decisions — Gary's and Steve's, not a chat's

| # | Decision | Owner | Position |
|---|---|---|---|
| D1 | Certification route and scope | Gary | **Settled.** 9001+14001+45001 integrated 2027; 27001 2028+. Roofing IS in scope, and the insurance schedule must be fixed to match. |
| D2 | Certification body | Steve | **Open.** Three written quotes. Ask in writing: *"Have you completed your UKAS accreditation extension for ISO 14001:2026, and if not, which tranche and what decision date?"* Also ask for the body's own effective-personnel calculation and for SSIP deemed-to-satisfy inside the scope. |
| D3 | Internal auditor — train or buy | Steve | **Open.** Train two, buy in the first cycle for independence. |
| D4 | Git host and approver | Gary | **OPEN AND NOW BLOCKING.** The repository exists locally and is not pushed anywhere. GitHub private, protected `main`, required review. **Steve approves, Gary authors and reviews. Write it down before commit one.** |
| D5 | Independent professional adviser | Steve | **Closed on naming** — see B1. |
| D6 | Buy the standards | Steve | **OPEN.** ISO 14001:2026 not held in any form. ISO/IEC 27001:2022 not held in any form. The 9001:2015 PDF held is licensed to Unitspark Ltd, single user. Buy own copies. |
| D7 | BS 99001:2022 | Gary | **Deferred.** UKAS accreditation is still a pilot with four CBs and no completion date, and BS 99001 references ISO 9001:2015 which is superseded next month. |
| **D8** | **The design carve-out for the standard quotation** | **Steve** | **NEW, AND THE ISO 9001 SCOPE TURNS ON IT.** The capability statements and the quotation contradict each other. Proposed wording at `system/4-context.md` ¶57. Nothing is applied to any customer-facing document until it is approved or replaced. |
| **D9** | **The `SESC-IMS-nn` series for the Annex SL spine** | **Gary** | **NEW.** Confirm or overturn — see §2 decision 1. |

---

## 5. Findings raised this session

| # | Finding | Severity | Owner |
|---|---|---|---|
| F1 | `SESC-IMS-Master-Register.md` did not exist despite the project instructions requiring every chat to read and write it. Two sessions ran without it. | High — it is the control against the drift that has already bitten three times | Closed by this file |
| F2 | **The project instructions and the project memory are both out of date.** They record all 21 documents as unsigned and the adviser as unappointed. Both were closed on 17 August. A chat starting from either would draft wrong findings. | High | Memory updated this session. **`SESC-IMS-Project-Instructions-v1.0.md` still needs correcting at §4.1 and §4.2.** |
| F3 | Next-free-reference line in the project instructions is stale: it says `SESC-REG-02` is free, but REG-02, REG-03 and REG-04 are all issued. | Medium | Corrected in `CLAUDE.md` §5. Correct the instructions file too. |
| F4 | **Two conditions precedent of the Employer's insurance are unmet** — portable appliance testing, and the monthly self-inspection of composite panel premises. This is a larger exposure than any certificate. | **High** | Steve / Health and Safety Officer |
| F5 | **Two climate-related risks have no entry in SESC-REG-01** — heat stress (CLI-02) and flooding of Unit 19 or a site (CLI-03). | Medium | Contracts Manager, at the next register review |
| F6 | **No SESC-REG-01 risk covers "no internal audit and no management review has ever happened"**, which is the single longest pole in the certification timetable. | Medium | Managing Director, at the next register review |
| F7 | ICO registration is recorded as absent **because no SESC record shows one — not because the public register was queried.** That is an unverified absence, not a verified one. Query it first. | Medium | Gary |
| F8 | The waste carrier registration number CBDL569181 appears only at POL-19 Annex A, and **the tier has not been confirmed.** Construction and demolition waste is excluded from the own-waste exemption, so **upper tier is required even carrying only the Employer's own waste.** | Medium | Environmental Manager |
| F9 | **`NICEIC Consumer Protection Survey NIC13190`** — hot water, heating, ASHP and PV, certificated since 11 December 2024 — **appears in no project document.** Decide whether it belongs in the IMS scope. | Low | Gary |

---

## 6. What happens next — one workstream per chat, in this order

| Order | Workstream | Why this order | Est. |
|---|---|---|---|
| 1 | **Push the repository to GitHub**, protect `main`, require review, and record D4. | Everything after this should be a pull request. Doing it later means rewriting history. | 30 min, Gary |
| 2 | **Port `policy_editor.py` to `build/render_docx.py`** and render `SESC-IMS-04` to a branded PDF, then **read the cover and a body page as images**. | Renderer parity is the Phase 1 gate. Four known traps live in `Reference\Section workflow method.md` §5. | 1 session |
| 3 | **`SESC-IMS-05` Leadership**, including the integrated IMS policy that supersedes the three separate policy statements, and the 45001 clause 5.4 worker consultation mechanism. | 5.4 is the clause 45001 auditors test hardest and it is entirely absent. | 1 session |
| 4 | **The environmental aspects and impacts register, built from SESC's own activities.** | **The defining ISO 14001 document and the highest-priority gap in the system.** The one held belongs to a landscaping firm. Blocked on buying 14001:2026 (D6). | 1–2 sessions |
| 5 | **The compliance obligations register**, replacing the 2020 register with dead drive links. | 14001 6.1.3 and 45001 6.1.3 are both dual maintain-AND-retain. | 1 session |
| 6 | **The four core procedures** — document control (7.5), internal audit (9.2), management review (9.3), nonconformity and corrective action (10.2). | The procedures the certification body asks for first, and which no SESC document currently provides. | 2 sessions |
| 7 | **Migrate POL-16 into the repository end to end** as the reference implementation, then the remaining twenty. | Do one and verify it before bulk migration. | 1 + 2 sessions |
| 8 | **The records layer** — form schemas, mobile capture, and records accumulating weekly **by someone other than Gary.** | This is the clock everything else waits on, and it is the real gate on Stage 2. | Phase 2 |

---

## 7. Rules that must survive every chat

1. **Never assert in a document something no record supports.** If asked to, refuse and say why.
2. **Nothing enters this system carrying a POW, ITC, LARC or Unitspark reference.** Borrowed
   material is structure, never content.
3. **No chat signs anything, fills a signature block, or merges to `main`.**
4. **Companies are certified; certification bodies are accredited.** Never "ISO 9001 accredited".
5. **A script exiting cleanly is not verification.** Render to PDF and read the pages as images.
6. **Update this file before the chat finishes. In the same turn.**

---

## 8. Revision history

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 18 August 2026 | Claude, for G A Hill | Created. Closes finding F1. Records the QMS build session 1: repository, clause map, `SESC-IMS-04`, `SESC-REG-05`, `SESC-REG-06`, validator and CI. |
