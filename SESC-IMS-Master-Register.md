# SESC-IMS-Master-Register

**The state of the CLAUDE ISO project. v1.10 · 24 September 2026.**

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
| **Why early** | Phase 0's gate was "JOSCAR submitted, nothing competes with it". All thirty JOSCAR sections read 100% on the evening of 17 August and the portal says *"You are now ready to submit your application."* Submission is held on three insurance attachments only, which is Gary's task and not a build task. Phase 0 is effectively clear. **Since then JOSCAR has been fully approved and Phase 0 is closed — see §2d.** |
| **Certification route** | ISO 9001 + 14001 + 45001 as **one** integrated certification, 2027. ISO 27001 deferred to 2028+, Cyber Essentials taken now in its place. **Adopted. Not to be re-derived.** |
| **Standards editions** | 9001:**2015** (written 2026-ready) · 14001:**2026** · 45001:**2018**. See `CLAUDE.md` §6. |
| **Repository** | **`github.com/GaryHill0985/QMS`**, pushed 18 August 2026, commit `d3782f7`. The working clone was `Desktop\SESC\ISO\CLAUDE ISO\` on the MSI; **from 24 September 2026 it is `~/Documents/SESC/ISO/CLAUDE ISO/` on the MacBook** — see §2d. **D4 CLOSED.** |
| **Master document count** | 21 signed (POL-01…19, CRP-01, REG-01) + REG-02, REG-03, REG-04 + REC-01…04 + TPL-01…04. |
| **This repository holds** | 3 controlled source files, 134 clauses across 3 standards, CI passing. |

### 1.1 The phase plan, and the principle that governs it

**Phase gates are about records accumulating, not build speed.** A phase is not passed by
finishing the work in it; it is passed when the evidence the next phase needs actually exists.

| Phase | Window | Gate to pass |
|---|---|---|
| 0 | to 27 Aug 2026 | JOSCAR submitted. **CLOSED — JOSCAR fully approved, registered supplier 10101706 (recorded 24 Sep 2026, §2d).** |
| 1 | **Sep – Nov 2026** (started 18 Aug, early) | Adviser appointed **and named in all 21 documents with the PDFs rebuilt**. Repo, clause map, renderer parity, all 21 documents migrated. **A branded PDF built from the repo is indistinguishable from the current one.** CI green. Audit pack generates, mostly red. |
| 2 | **Nov 2026 – Feb 2027** | Registers populated with real SESC data, not templates. **Records being created weekly by someone other than Gary.** |
| 3 | **Feb – Apr 2027** | One complete internal audit round across all three standards, and one minuted management review, on the record. Cyber Essentials certified. Gap report substantially green. |
| 4 | **Apr – Jul 2027** | Stage 1, then Stage 2. Certificates. |
| 5 | **2028+** | **Cyber Essentials Plus if demanded** · ISO 27001 as a scope extension · **BS 99001 when a Building-Safety-Act bid asks for it.** |

**⚠ How much live operating history Stage 2 needs is NOT ESTABLISHED.** The project has carried
two different figures — "4+ months" and "roughly three months" — and **neither is sourced.**
ISO/IEC 17021-1 has not been read by anyone on this project; what is understood is that it
requires Stage 1 to evaluate whether internal audits and a management review have been planned
and performed, rather than setting a numeric minimum. **Treat both figures as market practice, not
requirement. Ask each certification body in writing what it requires and record the answer**
(D2). Until then, plan on four months, because planning on three and being told four costs a
quarter.

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

## 2a. What changed later on 18 August 2026 — session 2

**Trigger:** Gary pushed the repository to GitHub using Claude Code, which raised two doubts
worth taking seriously — untracked empty directories, and whether `CLAUDE.md` had dropped
anything from `SESC-IMS-Project-Instructions-v1.0.md`. **It had. Six things existed nowhere else.**

| Done | Detail |
|---|---|
| **D4 CLOSED** | `github.com/GaryHill0985/QMS`, HTTPS remote, credentials via Windows Credential Manager, repo-local only. `CLAUDE ISO` is now the working clone. |
| **`.gitignore` defect fixed** | It excluded `records/attachments/`, which silently swallowed the `.gitkeep` — so `records/attachments/` would not have existed for anyone cloning. Now negated. `.gitkeep` added to `documents/` and `forms/`. |
| **Loose planning files explicitly ignored** | The four planning files and the zip now have a named `.gitignore` block with a comment, so `git status` is clean and nothing is committed by accident. **But that means GitHub is not backing them up — see D10.** |
| **`CLAUDE.md` §11 "Where things live" added** | The single most consequential loss: **nothing in the repo recorded the path to the Architecture & Build Plan, to `BRAND-SPEC.md`, to the twenty-one documents, or to `policy_editor.py`** — while the rules told chats to use all four. A chat could not find the document it was told to obey. |
| **`CLAUDE.md` §12 added** | The ten rules that survived nowhere else: the stop rule; how to treat blockers; **signed commits**; the full ISO 27001 position including the 2013-certificate rule and ISO/IEC 27002:2022; the UKAS verification procedure as a standing rule; the twelve-month gap-report staleness rule; the six climate reasons; that the honesty convention reaches the unmigrated documents; and "the system is the deliverable, the certificates are a consequence". |

**A full migration audit was run** — every substantive statement in the project instructions
checked against the new set. Result: 31 dropped, 8 weakened, 8 contradicted, and a long list
carried. **All of the dropped and weakened items are now closed.** The eight contradictions are
all cases where the old file is stale and the new set is right — see F11.

---

## 2b. GitHub controls put in place — 18 August 2026, session 2 continued

**All of D4 is now done, not just the push.** Configured through the browser with Gary present.

| Control | Setting | Why |
|---|---|---|
| Ruleset | **"Protect main - controlled documents"**, id 20986828, **Active**, target = default branch (`main`), **bypass list empty** | Named so its purpose is legible to an auditor, not just to a developer |
| Restrict deletions | On | `main` cannot be deleted |
| Block force pushes | On | History cannot be rewritten. **This is the control that makes signed commits worth anything** — an unforgeable signature on a rewritable history proves little |
| Require a pull request before merging | On, **required approvals = 0** | **No commit can reach `main` except through a pull request with a visible diff.** Approvals is 0 rather than 1 because GitHub forbids self-approval and 1 would deadlock a single-collaborator repository. **See D12 — this is the sole-director problem in a new place** |
| Require signed commits | On | Enabled only AFTER the key existed. Enabling it first would have rejected the next push |

**Commit signing on MSI.** ed25519 SSH key at `~/.ssh/id_ed25519_signing`, `gpg.format=ssh`, `commit.gpgsign=true`, added to GitHub under **Signing keys** (a separate list from authentication keys — the wrong list fails silently and every commit shows *Unverified*). Fingerprint `SHA256:5IUWBrgogowui5I6MXWcc9uYYQPIvcUKVTAb9Waw18Y`.

**⚠ Recorded honestly, because the honesty convention applies to this system too:**

1. **The signing key has NO passphrase.** Git Bash does not run `ssh-agent` by default, so a passphrase would prompt on every commit, and the realistic outcome of that is signing gets switched off within a week — a rule written and not operated. The key is protected by Windows file permissions on a single-user machine instead. **This is a deliberate trade-off, not an oversight.** Revisit if the machine is ever shared or if a second person commits.
2. **Commits `47e27ac` and `d3782f7`, and everything before 18 August 2026, are UNSIGNED.** Signing history retroactively is worthless — the value is in the unbroken chain from a stated date. **That date is 18 August 2026.**
3. **"Vigilant mode" is NOT enabled** on the GitHub account. It would mark every unsigned commit attributed to Gary as *Unverified*, including the two above and every commit in every other repository. Available at `github.com/settings/keys` if wanted.

**⚠ THE WORKING PRACTICE HAS CHANGED. There are no more direct pushes to `main`.** Every change — including a change to this register — now goes: branch → commit (signed) → push → pull request → merge. That is the control operating, not an obstacle to it.

---

## 2c. The QMS portal — 18 August 2026, session 2b

**Ran in parallel with session 2 and overwrote two of its files. Both restored. See F16 — the
lesson is recorded there and the method rules at §7 now cover it.**

**Gary's brief:** the Evidence Pack HTML format, the evidence index against the policies, and
what needs to be actioned and when — ideally an application the SESC team can access, add to,
edit, organise, retrieve and use in an audit, by permission.

**Stage 1 is a generated portal, not an application, and the reasoning is recorded because it
will be challenged later:**

1. A static site generated from this repository is the only option that does not make document
   control **worse**. Git already gives every change an author, a date and a reason, and
   `git checkout <sha> && python3 build/build_portal.py` reproduces any past state. A
   database-backed application must have all of that built, and built badly it becomes a system
   in which a controlled document can be changed silently — a self-inflicted major
   nonconformity against 7.5.3.
2. **Generation is why the Evidence Pack works.** Its own line — *an item leaves this list when
   the file is on disk, not when someone decides it does not matter* — holds only because
   nobody can type into it. An editable status field turns a gap report into a self-assessment.
3. A hosted application holding accident, training and conflicts records is a new information
   asset: a DPIA against POL-14, a controller/processor decision, an entry on SESC-REC-01,
   restore evidence for POL-15 and access review evidence for POL-13. Five obligations fed and
   no certificate earned, while **B3 zero operating history** is the actual long pole.
4. It is not a dead end. **What forces stage 2 is record capture, not policy editing** — an
   operative logging a near miss at 19:00 from a phone is the one thing a folder cannot do, and
   near-miss records are exactly what 45001 will want twelve months of. The five form schemas
   are fixed now so that nothing has to be migrated later.

| Built | Where | Status |
|---|---|---|
| `build/build_portal.py` and `build/portal_theme.py` — the generator and the house look | `build/` | Done |
| **The portal — 31 pages, four audience builds** | `site/` (gitignored, generated) | Regenerate with `python3 build/build_portal.py` |
| `portal/config.yaml` — organisation facts and the audience model | `portal/` | Done |
| **`SESC-REG-07` Document Register** — the 45-document legacy estate, every one `clause_map: pending` | `registers/documents.yaml` | **Draft v0.1.** Decision D13 |
| `portal/obligations.yaml` — SESC-REG-02 as data, 23 scheduled + 6 event-driven | `portal/` | Done |
| `portal/actions.yaml` — 38 items, mirroring §3, §4 and §5 of this register | `portal/` | Done |
| `portal/records-index.yaml` — record metadata only, so §12.6's staleness rule is computable | `portal/` | Done |
| **`SESC-FRM-01` Near Miss and Hazard Report** | `forms/` | **Draft v0.1.** Decision D14 |
| **`SESC-FRM-02` Accident and Incident Report** | `forms/` | **Draft v0.1** |
| **`SESC-FRM-03` Training and Competence Record** | `forms/` | **Draft v0.1** |
| **`SESC-FRM-04` Supplier and Subcontractor Evaluation** | `forms/` | **Draft v0.1** |
| **`SESC-FRM-05` Nonconformity and Corrective Action** | `forms/` | **Draft v0.1** |

**The headline the portal computes, and it is not flattering: 0 of 134 clauses are evidenced.
33 are addressed by a draft; 101 by nothing at all.** Correct and deliberate. A clause counts
only where a controlled file declares it in front matter **and** a record sits behind it inside
twelve months — the gap report definition at `CLAUDE.md` §12.6, now implemented rather than
merely written down. **No clause was inferred from a document title**, which is why the
twenty-one signed policies contribute nothing until they are migrated. The number moves for the
first time when POL-16 comes in.

**Audiences are distribution, not authentication.** Four builds — controller, approver,
contributor, auditor — each generated with what that audience must not see left out. Handing
over the auditor folder is a real control; it is not access control and no page claims it is.
Nothing bearing on conformity is hidden from the auditor build; what is withheld is commercial
decision-making and the project's own management. **The known-gap list IS published to the
auditor build, deliberately** — a supplier that has found a gap, dated it and named an owner is
in a different position from one that has not.

## 2d. What changed between 18 August and 24 September 2026

**No session wrote to this register between 18 August and 24 September 2026 (F21).** This section
catches it up. It was prepared on 24 September as `SESC-IMS-Master-Register-v1.5-update.md` in the
TeraBox restore (`ISO/_Claude Project setup 24 Sep 2026/`), from Gary's answers in a Cowork session
and from files in the TeraBox restore, and merged here the same day. **That file is now superseded
and is not a second register.**

| Item | Position at 24 Sep 2026 | Source |
|---|---|---|
| **JOSCAR** | **Fully approved.** Registered supplier 10101706. Certificate and badge files are in `JOSCAR\Certificates & Logos\`; the certificate carries the date 1 September 2027. **Phase 0 is closed.** | Gary, 24 Sep; certificate file |
| **QinetiQ on PI and ISO 27001** | QinetiQ approved without raising either. **This does not answer F12. The question was never asked.** It lowers the priority but does not close it. | Gary, 24 Sep |
| **Why now** | Steve and Craig are pushing certification for future tenders and clients. **No fixed external date.** | Gary, 24 Sep |
| **Certification route** | Unchanged: 9001 + 14001 + 45001 integrated; 27001 deferred. | — |
| **ISO 9001:2026** | **Published September 2026.** The plan to certify to :2015 and write 2026-ready stands until the certification body advises otherwise. See new D16. | Published sources, SGS, Sept 2026 |
| **Records home (stopgap)** | **Google Workspace**, chosen by Gary to start the operating-history clock now. Migrates to the SESC Platform (Supabase) later. See new D15. | Gary, 24 Sep |
| **Certification body conversation** | **Meeting with James Milligan (isocertification.uk.com), originally week commencing 28 Sep 2026, now 6 October 2026** (Gary, 24 Sep). See F20 before that meeting. | Gary, 24 Sep |
| **Standards / quotes** | Gary reports certification body quotes or standards activity. **Which standards were bought, and which editions, is not yet recorded.** Record against D6 and B4. | Gary, 24 Sep — to confirm |
| **Working machine moved to the MacBook** | **Gary's decision, 24 Sep 2026.** The MSI Windows laptop is retired from this project. The working clone is now `~/Documents/SESC/ISO/CLAUDE ISO/` on the MacBook, a fresh clone of `GaryHill0985/QMS`. A TeraBox restore of `ISO/` and `QinetiQ/JOSCAR/` also sits on the MacBook at `~/Documents/TeraBox Restore/SESC/SESC/`. It has no `.git`, so it is **reference only**. | Gary, 24 Sep |
| **D13 recovered from the TeraBox restore** | **The D13 change and register v1.4 had never reached GitHub** — `main` still held register v1.3. Recovered on 24 Sep 2026 from the TeraBox copy of `CLAUDE ISO` and committed from the MacBook as **`4b9648d`** (*"D13: document register moves to registers/documents.yaml as SESC-REG-07; register v1.4 (recovered from TeraBox restore)"*), merged to `main` as PR #2, merge commit `616e203`. **This is the first commit made from the MacBook.** Checked in this session: every tracked file in the clone now matches the TeraBox copy; the only differences are untracked files — see F24. | `git log`, 24 Sep; comparison of clone against TeraBox copy |
| **Claude Project** | New project "SESC IMS" set up with instructions v2.0. **Retire the CLAUDE ISO project** once it is running. | 24 Sep |

---

## 2e. Workstream 1a — Google Workspace record capture, 24 September 2026

**Taken:** 1a only. 1b (SESC-IMS-04 v0.3) is left for the next chat, under the one-workstream rule.
**Built in the repository and ready for review. Nothing has been built in Google Workspace yet.**
Running the build is Gary's job (see the tasks below).

| Built | Where | Status |
|---|---|---|
| **`SESC-FRM-06` Toolbox Talk Record.** It captures what the team raised and the response, so it evidences a 45001 5.4 participation mechanism operating. **It does not cover 5.4 on its own, and it says so** (`clause_note`). | `forms/SESC-FRM-06-toolbox-talk-record.yaml` | **Draft v0.1** |
| **`SESC-FRM-07` Site Inspection.** One integrated walk-round covering safety, environment and workmanship. Cites 9.1.1 of all three standards and nothing else. | `forms/SESC-FRM-07-site-inspection.yaml` | **Draft v0.1** |
| **`SESC-FRM-01…05` amended to v0.2.** Every form gets `correction_of`, so a correction is a new entry that points at the original (D15). FRM-01, 02 and 05 get an optional `job_ref`, so every record attaches to a job, a person or an organisation. Each has a revision history. **They are drafts, so amending them is permitted. None is issued.** | `forms/` | **Draft v0.2** |
| **`SESC-WI-01` How to Log a Record on Site.** A one-page site sheet, then a control section, "Records held, records not yet held", and an approval block that is **left unsigned**. **Must not be posted until the form links and QR codes are added.** | `documents/SESC-WI-01-how-to-log-a-record.md` | **Draft v0.1** |
| **The Forms generator.** `export_forms.py` reads the YAML and writes one Apps Script file. `Code.gs` builds, for each form: the Form, a protected response sheet, `_field_map` (question to schema key), `_record_refs` (FRM-nn-0001 references, each marked test or live), a submit trigger, optional email alerts that carry no content, and an index of links. It also provides `markGoLive`, `clockStart` for the B3 date, and `exportRecordsIndex`, which gives metadata only for `portal/records-index.yaml`. **It never rebuilds a form that is already built.** | `build/workspace_forms/` | Done, not yet run |
| **Setup runbook**, in order: the Admin console and 2SV, the Shared Drive, export, decisions, build, **checks by hand**, go-live, the monthly export, and the known limits | `build/workspace_forms/README.md` | Done |
| `CLAUDE.md` §5 next-free line: FRM-06, FRM-07 and WI-01 taken | `CLAUDE.md` | Done |

**Verification, and what it does not cover:**

1. `build/validate.py` passes with 0 errors. The new warnings are the expected 14001 `verified: false` ones. One note: FRM-06 cites 45001 5.4, which the clause map flags CRITICAL, and FRM-06 carries its own clause note.
2. `export_forms.py` produced seven forms. Five schemas have `file` fields, which are reported as needing to be added by hand.
3. **The generator was run against a mock of Google's services, not against Google.** It built 7 forms, 7 triggers and the index. A second run skipped all seven. Every sheet was protected down to the owner. Two FRM-02 entries after go-live became `FRM-02-0002` and `FRM-02-0003`, and the second recorded that it corrects `FRM-02-0001`. The pre-go-live test entry was marked `test` and left out of the export. The alert email carried the RIDDOR answer and no content. When `setPublished` and `setRequireLogin` were removed from the mock, the build carried on and logged 14 `CHECK BY HAND` lines. **A mock proves the logic. It does not prove that Google accepts every call.** README §6 is the real test, and it is Gary's.
4. **SESC-WI-01 was rendered to PDF and read as images.** Page 1, the site sheet, fits on one A4 page. **This was a draft preview render, not the branded renderer**, which is workstream 2. See F27.

**Tasks by owner, from this session:**

| Owner | Task | By |
|---|---|---|
| Gary | B6: enforce 2SV on every account with access, and record the date at B6. **Before the build.** | before the build |
| Gary | Create the `SESC Records` Shared Drive with named members only (README §2) | before the build |
| Gary | Decide D18 (photos) and D19 (who needs a sign-in). Set `CONFIG` to match. | before the build |
| Gary | Run README §3, §6 and §7. Record every `CHECK BY HAND` line. Record the go-live date here. | target 9 Oct 2026 |
| Gary | Send the form links to the next chat, which adds the QR codes to WI-01 | after go-live |
| Gary | **B3: record the first live record date** from `clockStart` | first live record |
| Gary | Review and merge the 1a pull request. **Claude does not merge.** | — |
| Health and Safety Officer | Give the WI-01 briefing as the first toolbox talk on FRM-06 | first talk after go-live |
| Contracts Manager | Start FRM-03 and FRM-04 entries for current staff cards and current subcontractors | from go-live |
| Next chat | 1b: SESC-IMS-04 v0.3, citing the Markel PI schedule `AHG015566` 2026-27 (in the TeraBox restore at `QinetiQ/JOSCAR/Insurance Docs/`) for D17. **Read every page of the schedule first.** | next chat |
| Later chat | `portal/actions.yaml` is still sourced from register v1.4. Resync it against this register. | Phase 1 |

**Completion note.** Record capture is designed, generated and documented, and nothing about it
is claimed as operating. The B3 clock has **not** started. It starts on the date of the first
**live** record in Workspace, and only Gary can make that happen by running README §6–§7.
Every record keeps its schema key, so moving to the SESC Platform needs no re-keying. Photos
and the sign-in model are the two open choices, recorded at D18 and D19.

---

## 3. Blockers — the four, restated with what has actually moved

| # | Blocker | Position at 18 August 2026, updated 24 September 2026 |
|---|---|---|
| B1 | Appoint the independent professional adviser | **CLOSED ON NAMING.** Simon Davies FCCA of Rapture Accounts Limited, confirmed 17 August. **NOT CLOSED ON DOCUMENTS: twenty documents still carry a blank adviser row and their branded PDFs must be rebuilt.** A name typed into a `.docx` does not reach a PDF already rendered.<br><br>**Nine documents route an actual control through that person and are the priority order for the rebuild: POL-02, POL-03, POL-11, POL-13, POL-16, POL-17, POL-18, POL-19 and REG-01.** POL-13 §21(j) and POL-17 §66 concede the gap in terms. CRP-01 has no such row. **POL-05 carries three separate approval rows and only the third is blank — Simon Davies goes in the third row and nowhere near the first**, which is Craig Bartle as regulation 7 competent person. |
| B2 | Sign the twenty-one documents | **CLOSED.** All 21 signed; every signature verified individually against the rendered PDF at 130 dpi on 17 August 2026. |
| B3 | Zero operating history | **OPEN, and it is the long pole.** The first quarter in which the Assurance Calendar is fully operated is the quarter ending 30 September 2026. A certification body wants roughly three months of the system running, one full internal audit round and one management review before Stage 2.<br><br>**24 Sep 2026: still the long pole. The first record entered into the Workspace forms (D15) is the date the clock starts. Record that date here when it happens.** No date recorded yet.<br><br>**24 Sep 2026, workstream 1a:** the forms generator is built in the repository (§2e), but **not yet run in Workspace. The clock has not started.** Only a **live** record counts: `markGoLive` separates setup tests from records, and `clockStart` gives the date. |
| B4 | The ISO 14001 edition problem | **OPEN. The Employer does not hold ISO 14001:2026 and nobody on this project has read it.** Every 14001 clause reference held is carried from the withdrawn :2015 edition. **Buy it before writing any EMS document.**<br><br>**24 Sep 2026:** Gary reports standards activity, but what was bought is not yet recorded. **Update this row once D6 is recorded.** |
| B5 | A second competent person | **OPEN.** No internal auditor is trained. Book two onto the CQI/IRCA two-day course for November 2026, ~£1,130–£1,255 inc VAT each. |
| B6 | Workspace 2-step verification | **UNVERIFIED.** Recorded as off on 17 August. Five minutes. Nobody has confirmed it since.<br><br>**24 Sep 2026: it now matters twice**, because the records stopgap (D15) puts personal data in Workspace. Verify on every account with access and record the date here.<br><br>**24 Sep 2026:** this is now step 1 of `build/workspace_forms/README.md`. The build is not to be run until it is done. |

---

## 4. Open decisions — Gary's and Steve's, not a chat's

| # | Decision | Owner | Position |
|---|---|---|---|
| D1 | Certification route and scope | Gary | **Settled.** 9001+14001+45001 integrated 2027; 27001 2028+. Roofing IS in scope, and the insurance schedule must be fixed to match. |
| D2 | Certification body | Steve | **Open.** Three written quotes. Ask in writing: *"Have you completed your UKAS accreditation extension for ISO 14001:2026, and if not, which tranche and what decision date?"* Also ask for the body's own effective-personnel calculation, for SSIP deemed-to-satisfy inside the scope, and **for how much live operating history it requires before Stage 2** (see §1.1).<br><br>**24 Sep 2026: now in motion.** First conversation: James Milligan (isocertification.uk.com), **now 6 October 2026** (moved from week commencing 28 Sep). **Read F20 first.** The requirement for **three written quotes stands.** Add F20's questions to the written questions above — who issues the certificate; whether that body is UKAS-accredited for 9001:2015, 14001:2026 and 45001:2018 with IAF 28 in scope; whether it, or anyone linked to it, has consulted on SESC's system — and D16's edition question. **Engaging a certification body is Steve's decision.**<br><br>**The cost basis, recorded so it is not re-derived — and its caveat, recorded so it is not repeated as fact.** Three standards integrated: ~13 audit days before reduction, **£7k–£13k** of CB fees in year one. All four: ~18 days, **£12k–£20k**. SESC's largest single contract is about £50,000. **⚠ Those figures assume an effective personnel count of 16–25 (IAF MD 5 base 3.0 / 4.5 / 5.5 = 13.0 days). SESC's payroll mean is about thirteen, which falls in the 11–15 band, where the base figures are lower and were NOT read from the source. And the pricing is triangulated from UK vendor sources, not quoted.** Three written quotes settle it. |
| D3 | Internal auditor — train or buy | Steve | **Open.** Train two, buy in the first cycle for independence. |
| D4 | Git host and approver | Gary | **FULLY CLOSED 18 Aug 2026.** `github.com/GaryHill0985/QMS`. Ruleset **"Protect main - controlled documents"** (id 20986828), **Active**, targeting `main`, bypass list empty, **four rules: restrict deletions · require a pull request before merging · block force pushes · require signed commits.** Commit signing configured on MSI with an ed25519 SSH key added to GitHub as a **Signing Key** (`SHA256:5IUWBrgogowui5I6MXWcc9uYYQPIvcUKVTAb9Waw18Y`). Steve approves, Gary authors and reviews — see D12.<br><br>**24 Sep 2026 — commit signing moved to the MacBook.** New ed25519 key `~/.ssh/id_ed25519_sesc`, registered on GitHub as both an Authentication key and a Signing key. **This key HAS a passphrase**, held in the macOS keychain. That reverses the §2b trade-off, which existed only because Git Bash on Windows had no ssh-agent. **Fingerprint: `SHA256:e17PhFZEmyBE1JG4LR51Du2P9Ozr5M8LJCuNTulCBwI`** (ED25519, 256-bit, comment `garyadamhill@outlook.com`), read by Gary with `ssh-keygen -lf ~/.ssh/id_ed25519_sesc.pub` on 24 Sep 2026. **The MacBook's first commit is `4b9648d`, the D13 recovery.** Local `git log` cannot check signatures, because `gpg.ssh.allowedSignersFile` is not configured on the MacBook. **Confirmed by Gary on GitHub, 24 Sep 2026: `4b9648d` and the v1.5 commit `b167f32` both show Verified.** The unbroken signed chain therefore continues from 18 August 2026 across the change of machine. **The MSI signing key (`SHA256:5IUWBrgogowui5I6MXWcc9uYYQPIvcUKVTAb9Waw18Y`) was removed from GitHub by Gary on 24 Sep 2026.** |
| D5 | Independent professional adviser | Steve | **Closed on naming** — see B1. |
| D6 | Buy the standards | Steve | **OPEN.** ISO 14001:2026 not held in any form. ISO/IEC 27001:2022 not held in any form. The 9001:2015 PDF held is licensed to Unitspark Ltd, single user. Buy own copies — **and ISO/IEC 27002:2022 with 27001, because without 27002 the Annex A control set cannot be applied.**<br><br>**24 Sep 2026:** Gary reports standards activity. **Record here which standards have been bought, the edition and the licensee** — not yet recorded.<br><br>**Checked 24 Sep 2026 against the PDFs in the TeraBox restore `ISO/` folder (the same files are in the Claude Project knowledge): the Employer holds no licensed copy of its own of any standard.** ISO 9001:2015 and ISO 14001:**2015 (withdrawn)** both read *"Licensed to Unitspark Ltd / Tamsin Horne … ISO Store Order OP-248594 / Downloaded 2017-11-07 · Single user licence only, copying and networking prohibited"*. BS ISO 45001:2018 and BS 99001:2022 show no licensee in their text layer, so whose licence they carry is **not established**. **ISO 14001:2026 is still not held in any form (B4).** Buying the Employer's own copies — at least 14001:2026 and 9001 — is a spending decision and **Steve's**.<br><br>**24 Sep 2026, reported by Gary: the Employer will purchase its own copies, starting with ISO 14001:2026.** Not yet bought. Record the order date, edition and licensee here when it is; B4 closes on purchase **and** reading. |
| D7 | BS 99001:2022 | Gary | **Deferred.** UKAS accreditation is still a pilot with four CBs and no completion date, and BS 99001 references ISO 9001:2015 which is superseded next month. **Revisit when a Building-Safety-Act bid asks for it. A copy of BS 99001:2022 is already held at `Desktop\SESC\ISO\`.** |
| **D8** | **The design carve-out for the standard quotation** | **Steve** | **NEW, AND THE ISO 9001 SCOPE TURNS ON IT.** The capability statements and the quotation contradict each other. Proposed wording at `system/4-context.md` ¶58. Nothing is applied to any customer-facing document until it is approved or replaced.<br><br>**Gary's position, 24 Sep 2026: SESC takes design responsibility for heat pumps and solar PV** (within its certification schemes). This matches the carve-out proposed at SESC-IMS-04 ¶58: heat loss calculation, emitter and heat pump sizing, MCS solar PV design in; all other design out. **Status: direction given; Steve's formal approval of the ¶58 wording is still required.** Then apply it to the standard quotation and CAP-008. Clause 8.3 stays in scope. See F22.<br><br>**Steve agreed by phone on 24 Sep 2026, reported by Gary.** No written record yet; his signature on SESC-IMS-04 v0.3 makes it formal. **The carve-out as agreed does not cover ventilation design — see D17.** |
| **D9** | **The `SESC-IMS-nn` series for the Annex SL spine** | **Gary** | **NEW.** Confirm or overturn — see §2 decision 1. |
| **D10** | **Should the four planning files be tracked in the repo?** | **Gary** | **NEW.** `SESC-IMS-Project-Instructions-v1.0.md`, the Readiness & Gap Analysis, the Gap Register xlsx and the review copies sit untracked in the clone, so **GitHub is not backing them up and the only copy is the laptop.** Options: move them into a `planning/` folder and track them, or leave them and accept the backup risk. Moving files inside `Desktop\SESC` is reserved to Gary. |
| **D12** | **Should Steve be a collaborator on the repository?** | **Gary** | **NEW, and it is the sole-director problem again.** `CLAUDE.md` says *"Steve approves, Gary authors and reviews. Two named humans."* **Required approvals on the ruleset is set to 0, because GitHub will not let a person approve their own pull request and 1 would deadlock a solo repository.** So the PR gate and the diff exist, but the second human does not. **Adding Steve as a collaborator and raising required approvals to 1 is what makes the rule operable** — exactly as appointing Simon Davies made the Board-independence clause operable. Until then the two-human rule is written and not operated, which is the failure pattern POL-08 is marked down for. |
| **D11** | **Are fire doors and mould & damp remediation named trades for the certificate scope?** | **Steve** | **NEW, and it changes the scope statement.** The project instructions describe the business as "M&E, roofing, **mould and damp remediation, fire doors** and renewables". The signed policies say "roofing, building fabric, mechanical, electrical and renewable energy works" and name neither. **A Building-Safety-Act-adjacent trade omitted from a scope statement is a finding.** If they are carried out, they are named at IMS-04 ¶14.<br><br>**Gary's position, 24 Sep 2026: mould & damp remediation is IN scope; fire doors are OUT.** Amend SESC-IMS-04 ¶14 to name mould & damp remediation, and remove fire doors from any scope wording (¶16 currently raises both). **Steve to confirm on approval of IMS-04.** The signed policies do not name mould & damp; add it at their next revision.<br><br>**Steve agreed by phone on 24 Sep 2026, reported by Gary.** No written record yet; his signature on SESC-IMS-04 v0.3 makes it formal. **Mould & damp is in scope as REMEDIATION ONLY:** SESC does not yet survey or diagnose (Gary, 24 Sep). Investigation is added to the scope only once the survey qualification Gary intends to obtain (PCA) is actually held — not claimed before then. Wording for ¶14: *"… and mould and damp remediation services …"*. |
| **D13** | **The document register becomes `SESC-REG-07`** | **Gary** | **CLOSED 18 Aug 2026 — Gary's decision.** The legacy document estate moved from `portal/documents.yaml` to `registers/documents.yaml` with front matter and is now validated on every push. It claims clause **7.5.3** of all three standards and nothing else — it is a register, not the document control PROCEDURE, which does not exist (G9). **Draft v0.1, not approved.** `CLAUDE.md` §5 now reads `SESC-REG-08` as next free.<br><br>**Recovered 24 Sep 2026.** This change and register v1.4 were made on the MSI on 18 August but never reached GitHub. Recovered from the TeraBox restore and committed from the MacBook as **`4b9648d`**, merged as PR #2 (merge `616e203`). See §2d and F24. |
| **D14** | **`SESC-FRM-01` to `FRM-05` confirmed for the record capture forms** | **Gary** | **CLOSED 18 Aug 2026 — Gary's decision.** The five references stand: near miss, accident/incident, training and competence, supplier evaluation, nonconformity and corrective action. **All five remain DRAFTS and none is issued.** `CLAUDE.md` §5 reads `SESC-FRM-06` as next free. |
| **D15** | **Records stopgap on Google Workspace** | **Gary** | **NEW, CLOSED 24 Sep 2026 — Gary's decision.** Rules: one Form per FRM schema; responses to Sheets in a restricted Shared Drive with named access only; 2SV on every account with access (B6); responses treated as append-only, a correction being a new entry referencing the original; metadata only into `portal/records-index.yaml`; **personal data never in git.** Migrates to the SESC Platform (Supabase) later, so field names stay aligned with `forms/SESC-FRM-01…05`.<br><br>**Implemented 24 Sep 2026 in the repository, not yet in Workspace (§2e).** Alignment is carried by a `_field_map` sheet per form. Append-only rests on sheet protection plus version history, and **it is not tamper-proof: the owning account and Shared Drive Managers can still edit.** That is stated in README §10. |
| **D16** | **Which ISO 9001 edition to certify to** | **Gary, via D2** | **NEW.** :2026 is now published. Ask the certification body whether it can certify to :2026 within SESC's window and what transition it expects. Until it answers, build to :2015 + Amd 1:2024 and write 2026-ready (`CLAUDE.md` §6). **Record the answer here.** |
| **D17** | **Ventilation design in mould & damp work** | **Steve** | **NEW 24 Sep 2026.** Gary confirms SESC specifies ventilation (for example extractor fans) as part of mould & damp remediation. That is design, and it sits **outside** the D8 carve-out, which names only heat loss, emitter and heat pump sizing and MCS solar PV. The ¶58 wording would therefore exclude design SESC actually does — the same contradiction D8 was raised to fix. **Two options:** (a) extend ¶58 to include ventilation specification for mould & damp remediation, which brings it under clause 8.3 and needs professional indemnity cover that extends to it — **check the policy schedule, do not assume**; or (b) stop specifying ventilation and have it specified by others. Option (a) matches what SESC does. **A contractual term and an insurance question: Steve's decision.** Resolve before IMS-04 v0.3 goes to Steve for signature.<br><br>**24 Sep 2026, reported by Gary: option (a) — ventilation specification for mould & damp remediation goes into the ¶58 carve-out, and the Employer's professional indemnity insurance covers it.** The schedule page or endorsement that shows the cover is **not yet cited here** — cite it when IMS-04 v0.3 is drafted, because ¶58 asserts PI cover and the honesty convention needs the record behind it. Formal approval by Steve's signature on IMS-04 v0.3. **Found 24 Sep 2026, not yet read:** `Markel PI AHG015566 - policy schedule 2026-27.pdf` in `QinetiQ/JOSCAR/Insurance Docs/` and `Evidence Pack/03 Insurance/` of the TeraBox restore. 1b reads every page of it and cites the page. |
| **D18** | **Photographs and attachments on the record forms** | **Gary** | **NEW 24 Sep 2026.** Five schemas carry a `file` field. Apps Script cannot create a file upload question (F25). A Google community guide says upload questions force sign-in and **do not work for a form held on a Shared Drive**. Options: (a) **photos are filed by hand** in a `Record photos` folder on the Shared Drive, named by record reference, which is the default written into WI-01 ¶4; (b) add upload questions by hand to the domain-sign-in forms, **only if** testing shows uploads work on the Shared Drive; (c) wait for the SESC Platform. **Tell site nothing different from WI-01 until this is decided.** |
| **D19** | **Who needs an SESC sign-in to submit** | **Gary** | **NEW 24 Sep 2026.** Default in `Code.gs`: FRM-01 and FRM-02 **open**, with no sign-in (the near miss is anonymous by design). FRM-03…07 need a **domain sign-in**, with the verified email recorded. **If supervisors hold no SESC account, FRM-06 and FRM-07 must be open too.** Record the choice here before the build. |

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
| F10 | **`.gitignore` excluded `records/attachments/`, silently swallowing its `.gitkeep`** — the directory would not have existed on a fresh clone. `documents/` and `forms/` were untracked for the same reason. Found by Claude Code at push. | Medium — a build that breaks on checkout | **Closed this session.** |
| F11 | **`SESC-IMS-Project-Instructions-v1.0.md` is now actively wrong in five places** and would mislead any chat that reads it: it says the 21 documents are unsigned, that the adviser is unappointed, that `SESC-REG-02` is the next free reference, that headcount is "around 13–20" (which its own successor rule forbids stating), and that the EL certificate is not held. | **High** | **Now safe to retire — the migration gaps are closed. Do not delete until D10 is settled.** |
| F12 | **The QinetiQ question was never asked and has no owner.** *"Is ISO 27001 a requirement or a scoring advantage at SESC's tier?"* Five minutes to their supply chain team. **It is the one answer that could reverse D1.** Until answered, the plan stands.<br><br>**24 Sep 2026:** QinetiQ approved JOSCAR without raising PI or ISO 27001. **That does not answer this finding — the question was never asked.** It lowers the priority; it does not close it. | Medium | Gary |
| F13 | **Neither figure for pre-Stage-2 operating history is sourced** — see §1.1. | Medium | Gary, via D2 |
| F14 | **All commits before 18 August 2026 are unsigned**, and the signing key carries no passphrase. Both are deliberate and both are recorded at §2b rather than left for an auditor to find.<br><br>**24 Sep 2026:** the no-passphrase point applies only to the MSI key. The MacBook key that replaced it has a passphrase (D4). | Low, if stated | Recorded |
| F15 | **The "two named humans" approval rule is not yet operable** — required approvals is 0 and Steve is not a collaborator. The control exists on paper only. | **Medium** | Gary, via D12 |
| F16 | **⚠ TWO SESSIONS WORKED ON THIS REPOSITORY AT ONCE ON 18 AUGUST, AND ONE OVERWROTE THE OTHER.** A Claude Code session built a portal generator (`build/build_portal.py`, `portal/*.yaml`, README changes) between 11:59 and 12:12. **In the process `registers/interested-parties.yaml` was reverted from v0.2 back to the v0.1 committed content, silently losing three restorations** — the first-aid needs assessment obligation, the "an unaccredited certificate submitted to JOSCAR is worse than no certificate" line, and Sovereign Housing named against IP-02. Found only because a file expected to be modified did not appear in `git status`. **This is the fourth time on this project that two copies of one thing have drifted.** | **High** | v0.2 restored. **Rule below.** |
| F17 | **A stale `.git/index.lock` blocked `git add` and `git commit`**, so a branch was pushed with no commits on it. Cause: a `git status` run through the device bridge, which cannot remove its own lock file. **Do not run git commands against the working clone through the device bridge.** | Medium | Closed — lock removed, rule recorded at §7.7 |
| F18 | **`SESC-REG-02` §8(a) does not reconcile with its own tables.** It states eleven of twenty-nine recurring obligations have never been done. The tables hold **23 scheduled** obligations, of which **15 have never been done**, plus 6 event-driven triggers. Correct at the next reissue. | Low | Gary |
| F19 | **Document owner is not recoverable for any of the 45 legacy documents.** The value exists in every PDF control table; the Evidence Pack extraction did not capture it and no machine-readable copy exists. **Until a document has a named owning ROLE, nobody is accountable for reviewing it** — and `SESC-REG-07` now carries an empty owner column that proves it. | Medium | Gary |
| F20 | **Check accreditation and impartiality before the James Milligan meeting.** James is SESC's retained external H&S adviser (POL-05 Annex C) and is named as internal SHEQ Manager in SESC-CPP-001. The JOSCAR brief §4 records a "Subcontractor Performance Review (**ISO Certification Ltd**)" scored 10/10 by the supplier about itself, and the Architecture Plan §11 item 6 calls it an "unaccredited-looking ISO Certification Ltd relationship that will not satisfy a defence customer". **Whether isocertification.uk.com is that business has not been established.** The website could not be read on 24 Sep (TLS certificate verification failure). **Before any commitment:** who issues the certificate; is that body UKAS-accredited for 9001:2015, 14001:**2026** and 45001:2018 with IAF 28 in scope; and has that body, or anyone linked to it, consulted on SESC's system? A body cannot certify a system it helped build. **The stop rule applies: engaging a certification body is Steve's decision.** | **High** | Gary, before the meeting on **6 Oct 2026** |
| F21 | **The Master Register was not updated between 18 August and 24 September 2026**, although JOSCAR approval, D8, D11 and the records route all moved in that time. | Medium | **Closed by this v1.5 merge.** |
| F22 | **The design carve-out has not yet reached the standard quotation.** Until it does, quotations still exclude all design while SESC designs heat pump and solar PV systems. | Medium | Steve / Gary |
| F23 | **`CLAUDE.md` §11 gives Windows paths (`Desktop\SESC\...`)** that no longer exist on the working machine, and the handover's "Give Gary Git Bash syntax" rule no longer applies. Correct §11 to the MacBook paths by PR — **a separate commit from this one** (§7.8). The Claude Project instructions v2.0 already carry the Mac paths and zsh syntax.<br><br>**Closed 24 Sep 2026** by a separate commit on the same branch as register v1.7: `CLAUDE.md` §2, §9.4 and §11 now give macOS paths into the TeraBox restore and the MacBook clone, with the zsh rule. Every §11 path was checked to exist on the MacBook. **One correction found:** POL-01…04 sit in `QinetiQ/JOSCAR/Documents/2.2 Human Resources/` in the TeraBox restore, not nested under `2.7 Environment & Sustainability` as recorded on 18 August — confirm which is current before migrating them. | Medium | **Closed** |
| F25 | **The record forms cannot capture photographs as built.** Apps Script's `Form` class documents no method for adding a file upload question (checked 24 Sep 2026). A Google Docs Editors community guide, which is **not Google's own documentation**, says uploads force sign-in and are not possible for forms on a Shared Drive. The gap is recorded row by row in each `_field_map` as `NOT CREATED`, not hidden. | Medium | Gary, via D18 |
| F26 | **`SESC-FRM-02` Accident and Incident Report has no "reported by" field.** On an open form, nothing records who raised an accident report. RIDDOR and the investigation will want to know. **Not changed in this session**, because whether to capture it, and how given that witness names are deliberately kept out, is a design choice. | Medium | Health and Safety Officer / Gary, at FRM-02 v0.3 |
| F27 | **Renderer trap for workstream 2: numbered paragraphs restart at 1 after a table.** When SESC-WI-01 was rendered with plain Markdown, ¶3–6 printed as 1–4, and ¶7 onward restarted too. The `sane_lists` extension fixed it in the preview. `build/render_docx.py` must keep the source numbering. Add this to the four traps in `Section workflow method.md` §5. | Medium | Workstream 2 |
| F28 | **Google says forms created by API after 30 June 2026 start unpublished and receive no responses** (Forms API "API changes" guide). Whether this applies to Apps Script `FormApp.create` was not confirmed. `Code.gs` publishes where the method exists, and README §6.5 makes checking **Published** in the editor mandatory. | Medium | Gary, at build |
| F24 | **Before the MSI was retired, it was the only home of any unpushed work and of the untracked planning files (D10).** **Confirmed in part on 24 Sep 2026: the D13 change and register v1.4 had never been pushed**, and were recovered from the TeraBox restore as `4b9648d`. A comparison of the clone against the TeraBox copy of `CLAUDE ISO` on 24 Sep found every tracked file identical. **Present only in the TeraBox restore, not in the clone:** the D10 planning and review files (`SESC-IMS-Project-Instructions-v1.0.md`, `SESC-IMS-Readiness-and-Gap-Analysis-v1.0.html`, `SESC-IMS-Gap-Register-v1.0.xlsx`, `SESC-IMS-04-Context-of-the-Organisation-v0.2-REVIEW.html`, `SESC-Business-System-Project-Brief.md`, `SESC-Business-System-Project-Handover-v1.0.md`) and `sesc-ims-portal-2026-08-18.zip`. **What the TeraBox copy cannot show is anything on the MSI newer than the backup, or on an unpushed branch.** Record here whether the MSI was checked before retirement, and the date — or that it was not.<br><br>**Closed 24 Sep 2026: Gary confirmed the MSI was checked before retirement and nothing is outstanding.** | Medium | **Closed** |

---

## 6. What happens next — one workstream per chat, in this order

**From 24 September 2026, 1a and 1b come first; the existing order then resumes at 2.**

| Order | Workstream | Why this order | Est. |
|---|---|---|---|
| ~~1~~ | ~~Push to GitHub, protect `main`, require PR review, require signed commits~~ — **ALL DONE 18 Aug 2026.** See §2b. Remaining question is D12, whether Steve becomes a collaborator. | Everything now arrives as a pull request. | Done |
| **1a** | **NEW 24 Sep 2026 — Google Workspace record capture** (D15): Forms for FRM-01…05 plus toolbox talk and site inspection, the Shared Drive, and a one-page "how to log it" for site. **Repository side DONE 24 Sep 2026 (§2e): FRM-06, FRM-07, WI-01 and the generator. Workspace side is Gary's: README §2–§7.** | **Starts the B3 clock. Nothing else moves the certification date as much.** | 1 session + Gary's build |
| **1b** | **NEW 24 Sep 2026 — `SESC-IMS-04` v0.3** (currently draft v0.2): name mould & damp remediation at ¶14, apply the D8 carve-out **with D17 (ventilation) resolved**, remove fire doors, then submit to Steve. | The scope statement is the first thing a certification body reads. | 1 session |
| 2 | **Port `policy_editor.py` to `build/render_docx.py`** and render `SESC-IMS-04` to a branded PDF, then **read the cover and a body page as images**. | Renderer parity is the Phase 1 gate. Four known traps live in `Reference\Section workflow method.md` §5. | 1 session |
| 3 | **`SESC-IMS-05` Leadership**, including the integrated IMS policy that supersedes the three separate policy statements, and the 45001 clause 5.4 worker consultation mechanism. | 5.4 is the clause 45001 auditors test hardest and it is entirely absent. | 1 session |
| 4 | **The environmental aspects and impacts register, built from SESC's own activities.** | **The defining ISO 14001 document and the highest-priority gap in the system.** The one held belongs to a landscaping firm. Blocked on buying 14001:2026 (D6). | 1–2 sessions |
| 5 | **The compliance obligations register**, replacing the 2020 register with dead drive links. | 14001 6.1.3 and 45001 6.1.3 are both dual maintain-AND-retain. | 1 session |
| 6 | **The four core procedures** — document control (7.5), internal audit (9.2), management review (9.3), nonconformity and corrective action (10.2). | The procedures the certification body asks for first, and which no SESC document currently provides. | 2 sessions |
| 7 | **Migrate POL-16 into the repository end to end** as the reference implementation, then the remaining twenty. | Do one and verify it before bulk migration. | 1 + 2 sessions |
| 8 | **The records layer** — form schemas, mobile capture, and records accumulating weekly **by someone other than Gary.** | This is the clock everything else waits on, and it is the real gate on Stage 2. **The Workspace stopgap is pulled forward to 1a (D15); the SESC Platform build stays here.** | Phase 2 |

---

## 7. Rules that must survive every chat

1. **Never assert in a document something no record supports.** If asked to, refuse and say why.
2. **Nothing enters this system carrying a POW, ITC, LARC or Unitspark reference.** Borrowed
   material is structure, never content.
3. **No chat signs anything, fills a signature block, or merges to `main`.**
4. **Companies are certified; certification bodies are accredited.** Never "ISO 9001 accredited".
5. **A script exiting cleanly is not verification.** Render to PDF and read the pages as images.
6. **Update this file before the chat finishes. In the same turn.**
7. **One session at a time on this repository.** Two sessions working the same clone on 18 August
   silently reverted a file (F16). Before starting work, run `git status` and read it — **a file
   you expected to be modified and which is not, is evidence that something overwrote you.**
   And **never run git commands against the working clone through the device bridge**: it cannot
   remove its own `.git/index.lock` and will block the next commit (F17).
8. **Commit one workstream per commit.** A commit message that describes one thing while carrying
   another makes history untrustworthy, which is the whole reason the history exists.

---

## 8. Revision history

| Version | Date | Author | Change |
|---|---|---|---|
| 1.10 | 24 September 2026 | Claude, for G A Hill | **Workstream 1a, repository side.** New §2e. New `SESC-FRM-06` Toolbox Talk Record and `SESC-FRM-07` Site Inspection (draft v0.1). `SESC-FRM-01…05` amended to v0.2, adding `correction_of` and, where a job applies, `job_ref`. New `SESC-WI-01` How to Log a Record on Site (draft v0.1). New `build/workspace_forms/` generator and runbook. `CLAUDE.md` §5: next free references are now FRM-08 and WI-02. B3, B6 and D15 updated. D17: PI schedule located, not yet read. New D18 (photos) and D19 (sign-in). New findings F25–F28. **Not yet run in Workspace. The B3 clock has not started.** |
| 1.9 | 24 September 2026 | Claude, for G A Hill | **Correction to the v1.6 row.** The first drafting of v1.6 was **not** lost or overwritten. It was committed at 14:58 on 24 Sep 2026 as `18c9979` onto the `register-v1.5` branch, after PR #3 had already merged that branch, so it never reached `main` and left a stray pull request open. The re-applied draft was committed as `2cfb96d` and merged as PR #4. The two differ only in the v1.6 revision note. The stray pull request from `register-v1.5` is closed without merging. **Lesson: after a pull request is merged, start the next change from an up-to-date `main` on a new branch — never commit onto a branch that has already been merged.** |
| 1.8 | 24 September 2026 | Claude, for G A Hill | D17: option (a) — ventilation specification into the ¶58 carve-out, PI cover confirmed by Gary; schedule citation still to be added. D6: decision to purchase the Employer's own copies, 14001:2026 first; not yet bought. |
| 1.7 | 24 September 2026 | Claude, for G A Hill | F23 closed — `CLAUDE.md` §2, §9.4 and §11 moved to macOS paths, committed separately on the same branch. F24 closed on Gary's confirmation. F20: the James Milligan meeting moves to 6 October 2026. D6: licence position of the standards held recorded — none licensed to the Employer, 9001 and 14001:2015 licensed to Unitspark Ltd. D8 and D11: Steve agreed by phone on 24 Sep 2026, reported by Gary; mould & damp in scope as remediation only. New D17: ventilation design in mould & damp work falls outside the D8 carve-out. |
| 1.6 | 24 September 2026 | Claude, for G A Hill | D4: MacBook signing key fingerprint recorded (`SHA256:e17PhFZEmyBE1JG4LR51Du2P9Ozr5M8LJCuNTulCBwI`); Gary confirmed on GitHub that `4b9648d` and `b167f32` show Verified. MSI signing key removed from GitHub, 24 Sep 2026 (Gary). v1.5 merged as PR #3 (`7746188`). **A first drafting of this v1.6 change was made in the working clone and was no longer there when Gary came to commit it — cause not established; re-applied (see §7.7).** F14 updated: the no-passphrase point now applies to the retired MSI key only. |
| 1.5 | 24 September 2026 | Claude, for G A Hill | Merged `SESC-IMS-Master-Register-v1.5-update.md`. New §2d: JOSCAR approved (Phase 0 closed); 9001:2026 published; records stopgap on Google Workspace (D15); D8 and D11 positions from Gary; new D16; working machine moved from the MSI to the MacBook, with a passphrase-protected signing key; findings F20–F24; §6 re-ordered to put record capture (1a) and IMS-04 v0.3 (1b) first. New Claude Project instructions v2.0. **Also recorded: the D13 recovery from the TeraBox restore on 24 Sep 2026, commit `4b9648d`, merged as PR #2 (`616e203`) — the first commit from the MacBook.** §1 status rows and F12 brought up to date. Corrected the update file's statement that this v1.5 commit would be the first from the MacBook. |
| 1.4 | 18 August 2026 | Claude, for G A Hill | Session 2b, the QMS portal. New §2c. `build/build_portal.py`, `build/portal_theme.py`, `portal/*`, 31 pages across four audience builds, and the §12.6 twelve-month staleness rule implemented. **D13 and D14 closed on Gary's decision** — the document register becomes `SESC-REG-07` and `SESC-FRM-01…05` stand. New findings F18, F19. Next free references now `SESC-REG-08` and `SESC-FRM-06`. |
| 1.0 | 18 August 2026 | Claude, for G A Hill | Created. Closes finding F1. Records the QMS build session 1: repository, clause map, `SESC-IMS-04`, `SESC-REG-05`, `SESC-REG-06`, validator and CI. |
| 1.3 | 18 August 2026 | Claude, for G A Hill | F16 — concurrent-session overwrite found and `registers/interested-parties.yaml` v0.2 restored. F17 — stale index.lock from the device bridge. Two new rules at §7.7 and §7.8. Portal generator built by a parallel Claude Code session noted and left intact. |
| 1.2 | 18 August 2026 | Claude, for G A Hill | GitHub controls completed — ruleset "Protect main - controlled documents" Active with four rules, and commit signing configured. New §2b. D4 fully closed. New decision D12 (Steve as collaborator, so the two-human rule is operable) and findings F14, F15. **Direct pushes to `main` are no longer possible.** |
| 1.1 | 18 August 2026 | Claude, for G A Hill | Session 2. D4 closed — repo live at `github.com/GaryHill0985/QMS`. Full migration audit of the project instructions against the repo: 31 dropped items and 8 weakened ones closed by adding `CLAUDE.md` §11 and §12. `.gitignore` defect fixed (F10). Phase plan restored at §1.1 with the unsourced-operating-history caveat. Nine adviser-dependent documents added to B1. Cost basis and its caveat added to D2. New decisions D10, D11; new findings F10–F13. |
