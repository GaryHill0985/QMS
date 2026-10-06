# SESC-IMS-Master-Register

**The state of the CLAUDE ISO project. v1.14 · 6 October 2026.**

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
| **This repository holds** | 3 controlled source files, 134 clauses across 3 standards, CI passing. **From 24 Sep 2026: a branded renderer, `build/render_docx.py`, with its tests (§2g).** |

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

## 2f. Workstream 1b — SESC-IMS-04 v0.3, 24 September 2026

**Taken:** 1b only. Started once PR #9 (workstream 1a) was confirmed merged to `main` as `4490e88`,
with a tree identical to `e948de4`. **`SESC-IMS-04` is DRAFT v0.3, not approved and not issued.
The approval block is untouched and unsigned.** Steve's signature on v0.3 is what makes D8, D11
and D17 formal, **and the ventilation element of D17 cannot be signed until F29 is resolved.**

| Changed in `system/4-context.md` | Detail |
|---|---|
| ¶14 scope statement (D11) | Names *"… and mould and damp remediation services …"*, as remediation only. The design element now reads as the carve-out: heat loss calculation, emitter and heat pump sizing, MCS solar PV design, and ventilation specification for mould and damp remediation. |
| ¶7, ¶16 (D11) | ¶7 names the trade. ¶16 is rewritten: no survey or diagnosis claimed until the survey qualification is held. **Fire doors are removed from all scope wording.** They survive only in the revision history. ¶16(a) records that the liability business description does not name mould and damp (F30). |
| ¶58, ¶59 (D8, D17) | The carve-out covers the four design activities. Clause 8.3 stays in scope, and no non-applicability is claimed. ¶58(b)–(d) cite the PI record page by page. **¶58(d) records that cover for ventilation specification is NOT shown,** and forbids the words "hold professional indemnity cover" for ventilation in any customer-facing document until the insurer or broker confirms in writing. |
| ¶18 | The design reference now points at ¶58 rather than "within the scope of the schemes held". |
| ¶31, ¶56(d) | Citations added: the schedule (pages 2–3) and the Statement of Fact (page 2). The retroactive date is not on the schedule. It is on the Statement of Fact. |
| **Demonstrable errors corrected** (F33) | ¶1: D16 edition position added. ¶33: asserted the content of ISO 14001:2026, which nobody has read. ¶39: quoted 30 Sep 2026 as the start of operation, against B3. ¶50–¶51: stated that records live in an encrypted database, when the position is the Workspace stopgap (D15), which is not yet operating. ¶50: the repository was named `sesc-ims`. The v0.2 note cited F17 for the overwrite, which is F16. The 0.2 revision row was missing. The footer read v0.1. |
| Part 8 | New records held (g) PI schedule and Statement of Fact, and (h) the broker letter of 6 Aug 2026. Rows (b), (h), (m), (n) and (q) updated. **(h), (m) and (n) were past their due dates.** (h) is re-dated to the go-live target of 9 Oct 2026. (m) and (n) carry a *proposed* 31 Oct 2026 for the owner to confirm. New rows (r) to (v), each dated. |

**The PI record, read in full on 24 Sep 2026.** `Markel PI AHG015566 - policy schedule 2026-27.pdf`
(TeraBox restore `QinetiQ/JOSCAR/Insurance Docs/`, identical by MD5 to the Evidence Pack copy)
has **3 pages**, read as images. Page 1: *Design & constructs professional risks combined
policy*, period 28-04-2026 to 27-04-2027, *"Cover provided: As shown in section of cover 1"*.
Page 2: professional liability, limit £250,000, excess £1,000, UK. D&O, entity defence and cyber
are all *"Not Insured"*. Page 3: aggregate costs-inclusive endorsement, covering civil liability
*"committed during the carrying out of your professional services"*. **No page defines
"professional services" or names any design activity, mould and damp, or ventilation.** Because of
that, the Statement of Fact of 20-04-2026 (**4 pages**, read as images) was also read. Page 2: 80%
own-design, retroactive date 28 April 2025, electrical engineering 80%. Page 3: heating and
ventilation engineering 20%, and *"Sola Panel Installation, air source heat pumps included in
heating engineering"*. **Mould and damp remediation is not declared.** The broker letter
(`PL IP24BCONT00022472100.pdf`, 2 pages, text layer read in full) was read for ¶16(a).

**Verification.** `build/validate.py` passes: 0 errors, and the one warning for this file is the
expected 14001 `verified: false`. A **draft review preview** was rendered to
`Claude outputs/SESC-IMS-04-v0.3-DRAFT-preview.pdf` (15 pages). The scope page (p3), the ¶58 page
(p11) and p2 and p12 were read as images. The first preview render reproduced F27: source ¶13
printed as "14.". The preview script was changed to render each numbered paragraph with its source
number, and all 67 paragraph numbers were then checked against the source. **This is not the
branded render. That is workstream 2.**

**Tasks by owner, from this session:**

| Owner | Task | By |
|---|---|---|
| **Steve** | **F29 / IMS-04 Part 8(u): obtain the insurer's or broker's written confirmation that PI AHG015566 covers ventilation specification in mould and damp remediation, and the policy wording that defines "professional services". Or take D17 option (b).** Steve's decision. The chat stopped on this point. | before signing v0.3; target 30 Sep 2026 |
| Steve | F30 / Part 8(r): written confirmation that the EL/PL policies respond to mould and damp remediation | 31 Oct 2026 |
| Steve | F31: correct the PI Statement of Fact with the insurer (trade, number of directors, activities). **A statement to an insurer, so Steve's.** | as soon as possible |
| Steve | Review and sign SESC-IMS-04 v0.3 (D8, D11, D17), once F29 is settled | 30 Sep 2026 |
| **Gary** | **F35: decide whether `GaryHill0985/QMS` should be private, and set it.** A repository setting, so Gary's. | before the next push |
| Gary | Review and merge the 1b pull request. **Claude does not merge.** | — |
| Gary | Part 8(s): give the job references for mould and damp remediation work already done | 31 Oct 2026 |
| Accounts Manager | F32 and Part 8(m): reconcile the EL and PL documents | 31 Oct 2026 (proposed) |
| Workstream 2 | F34: `render_docx.py` must print source paragraph numbers, and its test must check them all | workstream 2 |
| Later chat | After approval: apply the carve-out to the standard quotation and SESC-CAP-008 (F22) | after approval |
| Later chat | New workstream 1c, the SESC Platform record capture section (D20). **Not this chat.** | next platform session |

**Completion note.** IMS-04 v0.3 names mould and damp remediation, drops fire doors and carries
the four-activity design carve-out, with clause 8.3 in scope. Every PI statement in it now points
at a page. **The one thing it cannot do is say that PI covers ventilation specification, because
the schedule does not show it.** That gap is recorded at ¶58(d), Part 8(u) and F29, and it is
Steve's to close before he signs. Also recorded this session: D20 (Workspace forms are a stopgap,
and the Platform record capture section is to be built as soon as possible), and F35 (the
repository is public).

---

## 2g. Workstream 2 — the branded renderer, and SESC-IMS-04 v0.3 rendered, 24 September 2026

**Taken:** workstream 2 only. **Started once `main` was confirmed to contain PR #10.** Checked read-only
in the clone (`git --no-optional-locks`): `main` and `origin/main` both at **`02650c7`** (*Merge pull request #10 from
GaryHill0985/workstream-1b-ims04-v0.3*), parents `4490e88` and `3965225`. The merge tree `f34d1eb` is identical
to the tree of `3965225`, so nothing was changed in the merge. **`a082eff` (workstream 1b) and `3965225`
(register v1.11) both carry SSH signatures; Gary confirmed both show *Verified* on GitHub, 24 Sep 2026.** Local
`git log` still shows them as `N`, because `gpg.ssh.allowedSignersFile` is not configured on the MacBook (see D4).
`02650c7` carries GitHub's own web-flow signature. The GitHub API could not be reached from this session, so the
*Verified* status rests on Gary's check, not on this chat's.

**`SESC-IMS-04` was not changed.** It is still draft v0.3, and its approval block is still unsigned.

| Built | Where | Status |
|---|---|---|
| **`build/render_docx.py`**: ported from `policy_editor.py` and `sesc_cover.py` (TeraBox restore, read-only, not modified). **It generates** a branded DOCX from a Markdown source: the cover's six fields, the page-3 control table, the running header (`ID · Vn.n — Title`) and the footer are **all generated from front matter. No version number is typed anywhere.** **It also keeps** the amend-in-place API for the legacy estate: `replace_runs`, `append_para`, `add_contents_entry`, `set_cell` (trap 4 fixed), `find_signature_table` (trap 2), `patch_header_footer_text` (trap 3) and `patch_branded_cover()`. | `build/` | Done |
| Brand assets copied from `DOCUMENT DESIGN INSTRUCTIONS CLAUDE/`: `sesc-3d-background.jpg`, `sesc-logo-reversed.png`, `sesc-logo-dark.png`. SESC's own brand files, not borrowed material. | `build/assets/` | Done |
| **`build/test_render_docx.py`**, 19 tests. **F27/F34: every paragraph number and sub-paragraph label is compared with the source, both as written into the DOCX and as printed in the PDF** (read from the PDF text layer by position, so a table cell holding "(a)" is not counted). The source numbers are read straight off the Markdown lines, not through the renderer's parser. A mutation test confirms that a source numbered 1, 2, 5 prints 1, 2, 5. The other tests cover: front matter drives the header and control table; *uncontrolled when printed* with PAGE/NUMPAGES intact; OFFICIAL-SENSITIVE only on `official_sensitive: true`; the signature block renders empty; a draft with a filled signature row is **refused**; a typed footer that disagrees with the front matter fails the build; and the four §5 traps. | `build/` | **19/19 pass on the MacBook**, including the PDF test |
| `standards/front-matter-schema.yaml`: two optional fields, `revised` (date of this version) and `prepared_by`. Where they are absent, the renderer takes both from the revision-history row for the current version. **IMS-04 does not carry them, and was not edited to add them.** | `standards/` | Done |
| `.gitignore`: `.DS_Store` (F36) | root | Done |
| A `render` job for CI, running the renderer tests. **Not applied:** `.github/workflows/ci.yml` is protected against writes from this session (F37). | `Claude outputs/ci.yml.workstream-2` | **Gary to copy in** |

**How the renderer behaves on a draft.** For a draft, nothing is printed that implies issue or approval. The
cover and control table read *REVISION 0.3 — DRAFT, NOT ISSUED* · *Issue date: Not issued* · *Approved by: Not yet
approved (Managing Director)* · *Next review: Set on issue*. The header's right-hand side reads *DRAFT — NOT
ISSUED*. The revision date (24 September 2026) and the author (*G A Hill (drafted by Claude)*) come from Annex B
row 0.3. The contents page is generated from the headings. **No TOC field is used (trap 1).** The source's own
typed footer line (*"…v0.3…"*) is dropped, after checking that its version agrees with the front matter (F40).

**Rendered and verified — IMS-04 v0.3.** `Claude outputs/SESC-IMS-04-v0.3-DRAFT.docx` and `.pdf`, **21 pages**,
rendered on the MacBook with LibreOffice. Both are untracked (`*.pdf` and `*.docx` are gitignored). **Read as images:**
the cover (p1), the contents (p2), the control page (p3), the scope page with ¶14 (p6), the ¶58 page (p15), and the
approval and annex pages (p19–21). Each was compared side by side with the signed branded **POL-16 v1.2**
(`QinetiQ/JOSCAR/Documents/2.8 Quality/Branded/Signed/`, pages 1, 3, 4 and 5).

1. **Cover.** `make_cover()` is `sesc_cover.make_cover()` with its constants unchanged. Given POL-16's own field
   values, it reproduces the POL-16 cover PNG to a **mean difference of 0.24 on a 0–765 scale**. The only differing
   pixels are in rows 3–4, which were patched in POL-16 by `patch_branded_cover()`. **The cover was not redesigned.**
   The IMS-04 cover reads MANAGEMENT SYSTEM · CLAUSE 4 // ISO 9001 · ISO 14001 · ISO 45001 · *Context of the
   Organisation*. The six fields read as above. That wording is a reference to the standards, not a certification claim.
2. **Interior.** It uses POL-16's page geometry (A4; margins 1077/1474/1361; header and footer 567 twips), its
   full-bleed black header and footer bars with the 18-eighths red keyline, and its heading, numbered-paragraph and
   table formats run for run. The watermark matches POL-16's embedded image to a mean difference of 0.43.
3. **¶14 scope page.** The scope statement renders whole, as an indented quote kept with ¶14. **¶58 page:** the
   carve-out quote, then (a) to (d), with ¶58(d)'s warning intact.
4. **Approval block (Part 9).** Kept on one page. *Reviewed by*, all three *Date* cells and the *Signature* row are
   **empty**. Nothing was filled.
5. **Differences from POL-16, recorded rather than hidden.** The contents page has no page numbers and no "press F9"
   note, because it is not a field. Body tables have slightly more cell padding than POL-16's. The ⚠ in ¶58(d) prints
   as a colour glyph from a fallback font. Page breaks differ slightly between the container render and the MacBook
   render, because of font metrics. **Full parity, meaning "a branded PDF built from the repo is indistinguishable
   from the current one", can only be shown on a migrated signed document. That is workstream 7 (POL-16).** It is
   not claimed here.
6. **OFFICIAL-SENSITIVE** was rendered on a test fixture and read as images. The bands appear at head and foot of the
   cover and of every interior page. With the flag off, no marking appears.

**`build/validate.py` on the clone:** 0 errors, 10 warnings (all the expected 14001 `verified: false`), 3 notes. BUILD PASSES.

### 2g.1 Recommendation: add the F27 trap to `Section workflow method.md` §5

**Not applied. The TeraBox restore is read-only (CLAUDE.md §2).** When that file is next maintained, add this as a
fifth bullet under §5:

> **Numbered paragraphs restart, or get renumbered, after a table (F27, F34).** A Markdown renderer treats an
> indented continuation as a code block, and restarts an ordered list after a table, or after anything else that
> interrupts the list. SESC-WI-01 printed ¶3–6 as 1–4, and SESC-IMS-04 printed ¶13 as "14.". **Never use Markdown
> list numbering or Word auto-numbering for controlled paragraphs. Write the source number into the paragraph as
> literal text,** as the signed documents already do (`"1."` + tab, bold), and test every printed number against the
> source: `build/test_render_docx.py`.

`CLAUDE.md` §9.4 also says "four known traps". It should say five, and point to `build/render_docx.py`. That is a
`CLAUDE.md` change, so it goes by PR in a later chat, not this one.

### 2g.2 Status carried forward, as given by Gary on 24 Sep 2026

- **F29 (Steve): no change.** No written confirmation from the insurer or broker, and D17 option (b) has not been
  taken. The ventilation element of IMS-04 v0.3 still cannot be signed. Target 30 Sep 2026 stands.
- **F35 (Gary): still public, decision open.** The repository remains public. This register, now carrying F29–F31
  and F39, is readable by anyone. The recommendation stands: decide before the next push.

**Tasks by owner, from this session:**

| Owner | Task | By |
|---|---|---|
| **Gary** | **F36:** unstage the `.DS_Store` found staged in the index at the start of this session (`git restore --staged .DS_Store`). The commands below do it. | before the commit |
| **Gary** | **F37:** copy `Claude outputs/ci.yml.workstream-2` over `.github/workflows/ci.yml` (the commands below do it), then check that the `render` job goes green on the pull request. | with this PR |
| **Gary** | Review and merge the workstream 2 pull request. **Claude does not merge.** | — |
| **Gary** | **F35:** decide whether the repository goes private | before the next push |
| **Steve** | **F29:** unchanged, see §2f | 30 Sep 2026 |
| Gary | Optional: set `gpg.ssh.allowedSignersFile`, so that local `git log --show-signature` can check signatures without relying on GitHub (D4) | when convenient |
| Later chat | `CLAUDE.md` §9.4: five traps, with a pointer to `build/render_docx.py` (2g.1) | by PR |
| Later chat | **F39:** correct `portal/config.yaml`: the trades line, and the 30 Sep 2026 "date to quote" milestone | Phase 1 |
| Later chat (IMS-04 v0.4) | **F40:** remove the typed footer line. Consider adding `revised:` and `prepared_by:` to the front matter. | at v0.4 |
| Workstream 7 | Migrate POL-16 and render it with `render_docx.py`. **That is the parity test proper** (Phase 1 gate). | Phase 1 |

**Completion note.** The renderer exists, generates every control field from front matter, prints the source's
paragraph numbers and proves it on the printed page, and leaves the signature block empty. IMS-04 v0.3 renders to
a 21-page branded PDF that sits beside POL-16 on the same cover and interior system. **Nothing was signed, merged or
issued. IMS-04 was not edited.** Two things this chat could not do from here: write `ci.yml` (F37), and verify
signatures on GitHub itself. Both are with Gary. F29 remains the one thing standing between IMS-04 v0.3 and
Steve's signature.

---

## 2h. Pre-meeting review, 5 October 2026 — James Milligan's Dropbox template set

**Taken:** a read of James Milligan's email of 26 September 2026 (*"ISO Company Management System - Drop Box"*,
to Steve, cc Gary) and of the shared folder he refers to, which Gary duplicated to `~/Documents/SESC/SESC
Solutions Limited/` (173 files, 20 numbered folders plus `To be Allocated`). Every `.docx`, `.doc`, `.xlsx` and
`.xls` in it was opened and text-extracted; the CMS Manual, the H&S Policy Manual, the folder guides, the four
core procedures, the COTO log, the legal register, the aspects register, the NC-CAR log, the supplier list,
the calibration log and the toolbox-talk index were read. **Nothing in the repository was changed by this
session except this register. Nothing was uploaded to Dropbox.**

**What James proposes.** He has set up a template document system on his own Dropbox subscription, offers it
as *"the document builder"* from which SESC can later *"download and transfer all over to whatever system you
use"* — or, alternatively, that SESC gives him access to its own system and *"we build to that"*. He asks for
every existing SESC document and process to be dropped into a `To be uploaded` folder, which he will file.
The job he describes is to go through each folder and *"make each document your own"* — logo and description.
This is to be discussed at the meeting on **6 October 2026, 11:00**.

**What the set is.** A generic consultant's template CMS, not a certification body's. The evidence:

| | Found | Where |
|---|---|---|
| Provenance | *"Folder contents guide: green is provided by ISO Cert …"* — 32 control-table rows read `ISO Certification Ltd \| Reviewed by:`; the H&S Policy Manual template names *"James Milligan TechIOSH, ISO Certification Limited"* as the contracted H&S consultant; the supplier-list template's only real row is `ISO Certification Limited, james.milligan@isocertification.uk.com, 07808 666380, Bournemouth`, entered 2019. **This answers F20's open question: isocertification.uk.com is James's business**, now trading as The Milco Group Ltd (company 15837992, Shaftesbury) per his signature. | `0. Contents/`, `1. Context…/CMS Health and Safety Policy Manual.docx`, `8. Approved Suppliers/` |
| Third-party content | **93 toolbox talks carry `HCPL-TBT-nnn` document numbers**, index dated 6 July 2021 — another company's controlled documents. 92 of 128 `.docx` files mention HCPL. | `20. Health and Safety/Toolbox Talks WORKING ON/Generic/` |
| Editions | The manual and policies cite **ISO 14001:2015 (withdrawn 15 April 2026)**; the Generic Risk Assessments still cite ISO 9001:2008 and ISO 14001:2004. No 2026-edition content anywhere. | `CMS Manual.docx` ¶ Scope; `Generic Risk Assessments.docx` |
| Template state | `ADD ADDRESS`, `ADD SCOPE WORDING`, `LARGE COMPANY LOGO HERE`; demo data — a forklift at "Acme Calibration Labs", a supplier disapproved because *"They poisoned us at Xmas party"*, "attorney" and "CPA" in the COTO log (US-origin template); the quality policy promises *"to make the management of our customer's compliance an easy and enjoyable experience"*, which is a compliance consultancy's policy, not a contractor's. | throughout |
| Style | "The Company" 291 times; "the Employer" once. No numbered paragraphs. No control block of SESC's form. **No "Records held, records not yet held" section in any document.** | throughout |
| Aspects register | Office-based generic (lighting, photocopying, company cars, furniture). Not a contractor's. **Does not close §6 item 4**, which stays blocked on buying 14001:2026. | `13. Aspects and Impacts/` |
| Legal register | 111 rows, typed by topic, with links and a "last reviewed" date of 1 January 2026 on every row. **Useful as structure for §6 item 5** (SESC's own is dated 2020 with dead `Z:\` links) — every row still has to be evaluated against SESC's actual activities before any of it is SESC's. | `14. Legal and Regulatory Requirements/` |
| Internal audit model | Procedure stage 1: *"Audits completed by trained and independent auditors, such as ISO Certification Limited."* The consultant who supplies the documents also audits them. Bears on D3 and B5. | `7. …/CMS Procedure - Internal Audit.doc` |
| Scope creep | COTO log carries a `Risks 27001` tab (v1 01/08/2024). ISO 27001 is deferred (D1, CLAUDE.md §12.4). | `CMS COTO Log.xlsx` |
| Empty folders | 2, 4, 5, 6, 10, 11, 12, 15, 16, 18 (with 16 sub-folders), 19 — the records folders are empty, as they must be. The folder taxonomy itself is a reasonable picture of what an auditor expects to be shown. | — |

**What this changes, and what it does not.**

1. **The architecture does not change.** The repository stays the single master (CLAUDE.md §5, §7.7). IDs, clause
   tags, front-matter-generated control blocks, the honesty convention and the Workspace record capture all
   stand. James's "give me access and we build to that" is the one option that fits the master-copy rule; his
   Dropbox is an **inbox and a transfer folder, never a second master** — two copies of one thing have drifted
   four times on this project already.
2. **D2 was mis-framed.** The 6 October meeting is a **consultant** conversation, not the certification body
   conversation. Who certifies is still open, and the impartiality question in F20 now has a sharper form:
   *which UKAS-accredited body does James intend SESC to use, is he an agent, reseller or auditor for it, and
   has it accepted that he built the system?* A body cannot certify a system it, or anyone linked to it, built.
3. **Borrowed material is structure, never content** (§7.2) applies to the whole set. **`HCPL` joins POW, ITC,
   LARC and Unitspark** on the list of references that never enter the repository. What *is* worth taking as
   structure: the 20-folder evidence taxonomy as an auditor-facing **view** that the portal could generate
   (never as the filing system); the legal register's topic typing for §6 item 5; the four core procedures'
   stage / responsibility / control / record layout for §6 item 6; and the toolbox-talk **titles only** as a
   topic list for `SESC-FRM-06`.
4. **His edition position is a competence test.** The templates are built to 14001:2015. Ask him directly about
   14001:2026 and 9001:2026 and record the answer at D16 and B4.
5. **Personal data does not go to his Dropbox.** It is a store under a third party's subscription and control.
   Accident detail naming people, individual training records, DBS and right-to-work material stay in Workspace
   under POL-14 (CLAUDE.md §8). Nothing from `Insurance Docs/`, no file marked `CONTAINS PERSONAL DATA`, and
   not this register.
6. **The stop rule.** Whether SESC engages James as its ISO consultant, on what terms, and for what fee, is
   **Steve's decision**. This session proposes nothing on that.

**What goes into `To be uploaded`, if Gary decides to upload anything before the meeting** — issued documents
only, from the TeraBox restore `QinetiQ/JOSCAR/Documents/*/Branded/`: the 21 signed PDFs (POL-01…POL-19,
CRP-01, REG-01) and REG-02 Assurance Calendar. `SESC-IMS-04 v0.3` may go in **only clearly marked DRAFT and
unsigned**, because it is the scope statement he will otherwise invent from his manual's `ADD SCOPE WORDING`
— Gary's call; it carries the Part 8 inventory of records not yet held, including the insurance gaps F29–F31.
**Not uploaded:** REG-03, REC-01…04, TPL-01…04, anything in `2.13 Licences/Individual technician registrations/`,
`Insurance Docs/`, `CLAUDE.md`, this register, the forms YAML, the Workspace sheets.

**Questions for the meeting** (recorded here so the answers have somewhere to go):

| # | Question | Record the answer at |
|---|---|---|
| Q1 | Which certification body do you intend SESC to use, and is it UKAS-accredited for ISO 9001:2015, **ISO 14001:2026** and ISO 45001:2018 with IAF sector 28 in scope? | D2 |
| Q2 | What is your relationship with that body — agent, reseller, contracted auditor, none? Has it accepted in writing that the consultant who built the system is not its auditor? | F20 |
| Q3 | Your templates cite ISO 14001:2015, withdrawn in April 2026. What is your plan for 14001:2026, and for 9001:2026? | B4, D16 |
| Q4 | How much live operating history does that body require before Stage 2? Will you get it in writing? | §1.1, F13 |
| Q5 | Who carries out the internal audits — you, or SESC's own trained auditors? If you, who audits the documents you wrote? | D3, B5 |
| Q6 | Your toolbox talks are numbered HCPL. Whose are they, and are they licensed for SESC to adopt? | F41 |
| Q7 | The Dropbox is on your subscription. Who else has access, is 2-step verification enforced, and what happens to SESC's copies if the engagement ends? Is there a data-processing agreement? | F45 |
| Q8 | SESC's master copy is a version-controlled repository with generated control blocks and a records layer in Workspace. Will you work to that ("we build to that"), with Dropbox as the transfer folder? | §2h.1 |
| Q9 | What are you proposing commercially — scope, fee, duration? | **Steve** |

**Tasks by owner, from this session:**

| Owner | Task | By |
|---|---|---|
| Gary | Take Q1–Q9 to the meeting; record every answer in this register the same day | 6 Oct 2026 |
| Gary | Decide whether to upload the issued PDFs (and IMS-04 v0.3 as DRAFT) to `To be uploaded` before 11:00 | 6 Oct 2026 |
| Gary | Do not give James write access to the repository or the Workspace Shared Drive before Steve has decided the engagement | — |
| **Steve** | **Decide whether SESC engages The Milco Group Ltd as ISO consultant, and on what terms (Q9).** Nothing is committed at the meeting. | after 6 Oct |
| Gary | Verify the body named at Q1 on `ukas.com` (schedule: standard, edition, IAF 28) before any further step | after the meeting |
| Later chat (§6 item 5) | Read James's legal register as a *structural* seed for the compliance obligations register. Every obligation re-evaluated against SESC's activities. No row copied. | Phase 1 |
| Later chat (§6 item 6) | The four core procedures may use the stage / responsibility / control / record layout. Content is SESC's. | Phase 1 |
| Later chat | `CLAUDE.md` §3 and §7.2: add `HCPL` to the forbidden-reference list, by PR | next PR |

**Completion note.** The email was read in full; the folder was inventoried and every Office file in it opened, with the key documents read. The set is a generic ISO Certification Ltd
template kit, built to the withdrawn 14001 edition, carrying another company's controlled documents, and
holding no records. It confirms that James is the consultant side of this, not the certifying side, which
makes the impartiality question answerable and moves "who certifies" back to Steve as an open decision.
SESC's plan does not change; its master stays where it is. Nothing was signed, uploaded, merged or committed.

---

## 2i. Outcome of the James Milligan meeting, 6 October 2026

**Source: Gary's account of the meeting, given the same afternoon. Nothing below is signed or contracted. Every
commitment of money, and the choice of certification body, remains Steve's (stop rule).**

| Item | Position reported by Gary, 6 Oct 2026 | Recorded at |
|---|---|---|
| **First deliverable** | James asks for the **CMS Manual** first, using his template (`1. Context of the Organisation/CMS Manual.docx`) as the starting point; he will review and suggest changes. He said himself that this template, and many others in his folder, may not be relevant to SESC. | D21 |
| **Stage 1 target** | **Stage 1 assessment by the end of October 2026.** This brings Stage 1 forward from Phase 4 (Apr–Jul 2027) to Phase 1. | §2i.2, D22 |
| **Internal auditor** | **James Milligan.** | D3 |
| **External auditor / certification body** | **Stephen Lloyd of PJR** (Perry Johnson Registrars). | D2 |
| **Fire risk assessment** | James can carry out the premises fire risk assessment. His initial walk-round flagged twelve items to put right before it, and before Stage 2. | §2i.3, F49 |

### 2i.1 PJR, checked against UKAS on 6 October 2026

Read from the UKAS schedule of accreditation **0105, Perry Johnson Registrars, Inc (Troy, Michigan), Issue 046,
22 April 2026** (`ukas.com/download-schedule/0105/ManagementSystems`):

- **ISO 9001:2015, IAF 28 Construction: Full.**
- **ISO 45001:2018, IAF 28 Construction: Limited — "Construction excluding demolition as primary activity".** SESC
  does not demolish as a primary activity, so the limit does not appear to bite. **Confirm with PJR.**
- **ISO 14001: the schedule lists ISO 14001:2015 only, IAF 28 Construction: Full. No ISO 14001:2026 appears.**
- The schedule lists no UK office. Whether Stephen Lloyd audits under PJR Inc's UKAS accreditation or under another
  PJR entity's is **not established. Ask.**

**PJR is UKAS-accredited (Gary's understanding, confirmed by the schedule above).** **What this means.** PJR is UKAS-accredited for SESC's sector on two of the three standards at the editions planned.
On ISO 14001 it is not yet accredited to the 2026 edition, which `CLAUDE.md` §6 says SESC must certify to. Either
PJR extends its accreditation to 14001:2026 in time, or SESC certifies to 14001:2015 during the transition and
upgrades, **which `CLAUDE.md` §6 currently forbids.** That rule was written from the project's understanding of the
withdrawal and has not been checked against the IAF transition arrangements for 14001:2026. **It is a decision for
Gary and Steve, made on PJR's written answer, and recorded at B4.** Do not change `CLAUDE.md` §6 until then.

### 2i.2 Stage 1 by end of October — what it requires, and what it does not

Stage 1 is a readiness review, not certification. Findings at Stage 1 are normal and are closed before Stage 2.
What remains true: **Stage 2 needs operating history — records, one internal audit round and a minuted management
review** (§1.1). Bringing Stage 1 forward does not bring certification forward unless the records exist.

What PJR is likely to look for at Stage 1 (confirm the list with Stephen Lloyd in writing — not read from PJR's own
documents): the scope statement; the policy; the manual or equivalent; the environmental aspects and compliance
obligations registers; hazard identification; objectives; and evidence that internal audit and management review are
planned. **Against that, at 6 Oct 2026:** IMS-04 v0.3 (scope) is unsigned, held on F29–F31; there is no aspects
register of SESC's own; the compliance obligations register is the 2020 one; no internal audit programme exists; no
management review is scheduled; the Workspace forms are not live. **Three and a half weeks.** Ask PJR the maximum
interval it allows between Stage 1 and Stage 2, so that an early Stage 1 does not have to be repeated.

### 2i.3 Premises fire safety — items flagged by James before the fire risk assessment

Unit 19 Melbury Business Park. **Reported by Gary, 6 Oct 2026, from James's walk-round.** Items 1–11 given at the
meeting; item 12 added by Gary the same afternoon; items 13 and 14 added by Gary on 6 Oct 2026. **Every item that costs money is Steve's to approve.** None is
claimed as done.

| # | Item | Owner | Status |
|---|---|---|---|
| FS-01 | Muster point established and signed | Steve / Craig | Open |
| FS-02 | Sufficient emergency lighting from the office to the muster point | Steve | Open |
| FS-03 | Emergency lighting above each exit door | Steve | Open |
| FS-04 | Emergency lighting internally: front office door and end of corridor | Steve | Open |
| FS-05 | 5 L water and 2 kg CO2 extinguishers installed, wall-fixed beside the office entrance / fire exit, and commissioned | Steve | Open |
| FS-06 | Fire compartmentation: fill holes in the ceiling around the office where necessary | Steve / Craig | Open |
| FS-07 | Which doors must be fire doors | **James** to confirm | Open |
| FS-08 | Fire blanket in the kitchen | Craig | Open |
| FS-09 | Sanitary bin in the toilet (welfare, not fire) | Craig | Open |
| FS-10 | Illuminated exit (green running man) sign above the kitchen door and other necessary doors | Steve | Open |
| FS-11 | Smoke detectors in the necessary rooms | Steve | Open |
| FS-12 | Electrical cupboard in Scott's office to be boxed off | Steve / Craig | Open |
| FS-13 | Self-closing devices (door closers) fitted to every door confirmed as a fire door at FS-07 | Steve | Open — follows FS-07 |
| FS-14 | Establish the fire detection and alarm category for the office under BS 5839-1 (M, L1–L5, P1–P2). **Set by the fire risk assessment, not chosen in advance.** Decides the scope of FS-11 (smoke detectors) and any alarm upgrade | James, through the FRA; Steve approves the works | Open |

**Fire doors here are premises fire safety, not a trade SESC sells.** D11 (fire doors out of the certification
scope) is unaffected.

**Tasks by owner, from this section:**

| Owner | Task | By |
|---|---|---|
| **Steve** | Confirm PJR as certification body (D2) and James as internal auditor (D3), and approve the fire safety spend (FS-01…12) | before any contract |
| Gary | Ask PJR in writing: 14001 edition and 2026 extension date; which PJR entity holds the accreditation Stephen Lloyd audits under; the Stage 1 document list; the maximum Stage 1–Stage 2 interval; the operating history wanted before Stage 2; James's relationship to PJR (Q2) | this week |
| Gary | D21: decide the CMS Manual's reference and how it relates to IMS-04, then draft it — **in SESC's house style, from SESC's facts, with James's template as a heading checklist only** | next chat |
| **Steve** | Buy the Employer's own ISO 14001 (edition per PJR's answer) and ISO 9001 — the aspects register cannot be built without it (B4, D6) | now |
| **Steve** | F29–F31: broker's written answer, so IMS-04 can be signed before Stage 1 | before Stage 1 |
| Gary | Run the Workspace forms build (README §2–§7) — the records clock is now on the critical path for Stage 2 | this week |
| Craig | Log FS-01…12 as records (FRM-05 or the fire log) as each is closed, with date and evidence | as closed |
| James | Confirm FS-07; carry out the premises fire risk assessment once FS items are closed | per Steve's engagement |

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
| D2 | Certification body | Steve | **Open.** Three written quotes. Ask in writing: *"Have you completed your UKAS accreditation extension for ISO 14001:2026, and if not, which tranche and what decision date?"* Also ask for the body's own effective-personnel calculation, for SSIP deemed-to-satisfy inside the scope, and **for how much live operating history it requires before Stage 2** (see §1.1).<br><br>**24 Sep 2026: now in motion.** First conversation: James Milligan (isocertification.uk.com), **now 6 October 2026** (moved from week commencing 28 Sep). **Read F20 first.** The requirement for **three written quotes stands.** Add F20's questions to the written questions above — who issues the certificate; whether that body is UKAS-accredited for 9001:2015, 14001:2026 and 45001:2018 with IAF 28 in scope; whether it, or anyone linked to it, has consulted on SESC's system — and D16's edition question. **Engaging a certification body is Steve's decision.**<br><br>**5 Oct 2026: the 6 October meeting is a CONSULTANT conversation, not the certification body conversation** (§2h). James Milligan is offering to build SESC's documents from his ISO Certification Ltd template kit on his Dropbox. Which body certifies is still open and still needs three written quotes. Record James's answer to Q1 here.<br><br>**6 Oct 2026 (Gary, after the meeting): PJR — Perry Johnson Registrars, auditor Stephen Lloyd — to be the certification body.** UKAS schedule 0105 issue 046 (22 Apr 2026) read the same day: 9001:2015 and 45001:2018 IAF 28 in scope (45001 limited to construction excluding demolition as primary activity); **14001 at :2015 only.** See §2i.1. **Steve's decision to confirm; no written quote recorded; the three-quote requirement has not been met.**<br><br>**The cost basis, recorded so it is not re-derived — and its caveat, recorded so it is not repeated as fact.** Three standards integrated: ~13 audit days before reduction, **£7k–£13k** of CB fees in year one. All four: ~18 days, **£12k–£20k**. SESC's largest single contract is about £50,000. **⚠ Those figures assume an effective personnel count of 16–25 (IAF MD 5 base 3.0 / 4.5 / 5.5 = 13.0 days). SESC's payroll mean is about thirteen, which falls in the 11–15 band, where the base figures are lower and were NOT read from the source. And the pricing is triangulated from UK vendor sources, not quoted.** Three written quotes settle it. |
| D3 | Internal auditor — train or buy | Steve | **Open.** Train two, buy in the first cycle for independence.<br><br>**6 Oct 2026 (Gary): James Milligan to be the internal auditor.** That buys independence from SESC staff. **It does not give independence from James's own work:** he is to review the CMS Manual and carry out the fire risk assessment, and ISO 9001 and ISO 45001 9.2.2 c) want auditors who do not audit their own work. Agree with James which areas someone else audits. **B5 (a second competent person inside SESC) is not closed by this.** Steve to confirm. |
| D4 | Git host and approver | Gary | **FULLY CLOSED 18 Aug 2026.** `github.com/GaryHill0985/QMS`. Ruleset **"Protect main - controlled documents"** (id 20986828), **Active**, targeting `main`, bypass list empty, **four rules: restrict deletions · require a pull request before merging · block force pushes · require signed commits.** Commit signing configured on MSI with an ed25519 SSH key added to GitHub as a **Signing Key** (`SHA256:5IUWBrgogowui5I6MXWcc9uYYQPIvcUKVTAb9Waw18Y`). Steve approves, Gary authors and reviews — see D12.<br><br>**24 Sep 2026 — commit signing moved to the MacBook.** New ed25519 key `~/.ssh/id_ed25519_sesc`, registered on GitHub as both an Authentication key and a Signing key. **This key HAS a passphrase**, held in the macOS keychain. That reverses the §2b trade-off, which existed only because Git Bash on Windows had no ssh-agent. **Fingerprint: `SHA256:e17PhFZEmyBE1JG4LR51Du2P9Ozr5M8LJCuNTulCBwI`** (ED25519, 256-bit, comment `garyadamhill@outlook.com`), read by Gary with `ssh-keygen -lf ~/.ssh/id_ed25519_sesc.pub` on 24 Sep 2026. **The MacBook's first commit is `4b9648d`, the D13 recovery.** Local `git log` cannot check signatures, because `gpg.ssh.allowedSignersFile` is not configured on the MacBook. **Confirmed by Gary on GitHub, 24 Sep 2026: `4b9648d` and the v1.5 commit `b167f32` both show Verified.** The unbroken signed chain therefore continues from 18 August 2026 across the change of machine. **The MSI signing key (`SHA256:5IUWBrgogowui5I6MXWcc9uYYQPIvcUKVTAb9Waw18Y`) was removed from GitHub by Gary on 24 Sep 2026.** |
| D5 | Independent professional adviser | Steve | **Closed on naming** — see B1. |
| D6 | Buy the standards | Steve | **OPEN.** ISO 14001:2026 not held in any form. ISO/IEC 27001:2022 not held in any form. The 9001:2015 PDF held is licensed to Unitspark Ltd, single user. Buy own copies — **and ISO/IEC 27002:2022 with 27001, because without 27002 the Annex A control set cannot be applied.**<br><br>**24 Sep 2026:** Gary reports standards activity. **Record here which standards have been bought, the edition and the licensee** — not yet recorded.<br><br>**Checked 24 Sep 2026 against the PDFs in the TeraBox restore `ISO/` folder (the same files are in the Claude Project knowledge): the Employer holds no licensed copy of its own of any standard.** ISO 9001:2015 and ISO 14001:**2015 (withdrawn)** both read *"Licensed to Unitspark Ltd / Tamsin Horne … ISO Store Order OP-248594 / Downloaded 2017-11-07 · Single user licence only, copying and networking prohibited"*. BS ISO 45001:2018 and BS 99001:2022 show no licensee in their text layer, so whose licence they carry is **not established**. **ISO 14001:2026 is still not held in any form (B4).** Buying the Employer's own copies — at least 14001:2026 and 9001 — is a spending decision and **Steve's**.<br><br>**24 Sep 2026, reported by Gary: the Employer will purchase its own copies, starting with ISO 14001:2026.** Not yet bought. Record the order date, edition and licensee here when it is; B4 closes on purchase **and** reading. |
| D7 | BS 99001:2022 | Gary | **Deferred.** UKAS accreditation is still a pilot with four CBs and no completion date, and BS 99001 references ISO 9001:2015 which is superseded next month. **Revisit when a Building-Safety-Act bid asks for it. A copy of BS 99001:2022 is already held at `Desktop\SESC\ISO\`.** |
| **D8** | **The design carve-out for the standard quotation** | **Steve** | **NEW, AND THE ISO 9001 SCOPE TURNS ON IT.** The capability statements and the quotation contradict each other. Proposed wording at `system/4-context.md` ¶58. Nothing is applied to any customer-facing document until it is approved or replaced.<br><br>**Gary's position, 24 Sep 2026: SESC takes design responsibility for heat pumps and solar PV** (within its certification schemes). This matches the carve-out proposed at SESC-IMS-04 ¶58: heat loss calculation, emitter and heat pump sizing, MCS solar PV design in; all other design out. **Status: direction given; Steve's formal approval of the ¶58 wording is still required.** Then apply it to the standard quotation and CAP-008. Clause 8.3 stays in scope. See F22.<br><br>**Steve agreed by phone on 24 Sep 2026, reported by Gary.** No written record yet; his signature on SESC-IMS-04 v0.3 makes it formal. **The carve-out as agreed does not cover ventilation design — see D17.**<br><br>**24 Sep 2026, workstream 1b:** applied at SESC-IMS-04 v0.3 ¶58, with ¶14 and ¶18 aligned: heat loss, emitter and heat pump sizing, MCS solar PV design, and (from D17) ventilation specification for mould and damp remediation. **Clause 8.3 stays in scope, and no non-applicability is claimed.** Status: **drafted, awaiting Steve's signature on v0.3.** The standard quotation and CAP-008 follow approval (F22). |
| **D9** | **The `SESC-IMS-nn` series for the Annex SL spine** | **Gary** | **NEW.** Confirm or overturn — see §2 decision 1. |
| **D10** | **Should the four planning files be tracked in the repo?** | **Gary** | **NEW.** `SESC-IMS-Project-Instructions-v1.0.md`, the Readiness & Gap Analysis, the Gap Register xlsx and the review copies sit untracked in the clone, so **GitHub is not backing them up and the only copy is the laptop.** Options: move them into a `planning/` folder and track them, or leave them and accept the backup risk. Moving files inside `Desktop\SESC` is reserved to Gary. |
| **D12** | **Should Steve be a collaborator on the repository?** | **Gary** | **NEW, and it is the sole-director problem again.** `CLAUDE.md` says *"Steve approves, Gary authors and reviews. Two named humans."* **Required approvals on the ruleset is set to 0, because GitHub will not let a person approve their own pull request and 1 would deadlock a solo repository.** So the PR gate and the diff exist, but the second human does not. **Adding Steve as a collaborator and raising required approvals to 1 is what makes the rule operable** — exactly as appointing Simon Davies made the Board-independence clause operable. Until then the two-human rule is written and not operated, which is the failure pattern POL-08 is marked down for. |
| **D11** | **Are fire doors and mould & damp remediation named trades for the certificate scope?** | **Steve** | **NEW, and it changes the scope statement.** The project instructions describe the business as "M&E, roofing, **mould and damp remediation, fire doors** and renewables". The signed policies say "roofing, building fabric, mechanical, electrical and renewable energy works" and name neither. **A Building-Safety-Act-adjacent trade omitted from a scope statement is a finding.** If they are carried out, they are named at IMS-04 ¶14.<br><br>**Gary's position, 24 Sep 2026: mould & damp remediation is IN scope; fire doors are OUT.** Amend SESC-IMS-04 ¶14 to name mould & damp remediation, and remove fire doors from any scope wording (¶16 currently raises both). **Steve to confirm on approval of IMS-04.** The signed policies do not name mould & damp; add it at their next revision.<br><br>**Steve agreed by phone on 24 Sep 2026, reported by Gary.** No written record yet; his signature on SESC-IMS-04 v0.3 makes it formal. **Mould & damp is in scope as REMEDIATION ONLY:** SESC does not yet survey or diagnose (Gary, 24 Sep). Investigation is added to the scope only once the survey qualification Gary intends to obtain (PCA) is actually held — not claimed before then. Wording for ¶14: *"… and mould and damp remediation services …"*.<br><br>**24 Sep 2026, workstream 1b:** applied at SESC-IMS-04 v0.3 ¶7, ¶14 and ¶16, as remediation only, with no survey or diagnosis claimed. Fire doors removed from all scope wording. **The liability business description does not name mould and damp (F30), and that is recorded at ¶16(a).** Status: **drafted, awaiting Steve's signature on v0.3.** |
| **D13** | **The document register becomes `SESC-REG-07`** | **Gary** | **CLOSED 18 Aug 2026 — Gary's decision.** The legacy document estate moved from `portal/documents.yaml` to `registers/documents.yaml` with front matter and is now validated on every push. It claims clause **7.5.3** of all three standards and nothing else — it is a register, not the document control PROCEDURE, which does not exist (G9). **Draft v0.1, not approved.** `CLAUDE.md` §5 now reads `SESC-REG-08` as next free.<br><br>**Recovered 24 Sep 2026.** This change and register v1.4 were made on the MSI on 18 August but never reached GitHub. Recovered from the TeraBox restore and committed from the MacBook as **`4b9648d`**, merged as PR #2 (merge `616e203`). See §2d and F24. |
| **D14** | **`SESC-FRM-01` to `FRM-05` confirmed for the record capture forms** | **Gary** | **CLOSED 18 Aug 2026 — Gary's decision.** The five references stand: near miss, accident/incident, training and competence, supplier evaluation, nonconformity and corrective action. **All five remain DRAFTS and none is issued.** `CLAUDE.md` §5 reads `SESC-FRM-06` as next free. |
| **D15** | **Records stopgap on Google Workspace** | **Gary** | **NEW, CLOSED 24 Sep 2026 — Gary's decision.** Rules: one Form per FRM schema; responses to Sheets in a restricted Shared Drive with named access only; 2SV on every account with access (B6); responses treated as append-only, a correction being a new entry referencing the original; metadata only into `portal/records-index.yaml`; **personal data never in git.** Migrates to the SESC Platform (Supabase) later, so field names stay aligned with `forms/SESC-FRM-01…05`.<br><br>**Implemented 24 Sep 2026 in the repository, not yet in Workspace (§2e).** Alignment is carried by a `_field_map` sheet per form. Append-only rests on sheet protection plus version history, and **it is not tamper-proof: the owning account and Shared Drive Managers can still edit.** That is stated in README §10.<br><br>**24 Sep 2026: confirmed as a stopgap only — see D20.** |
| **D16** | **Which ISO 9001 edition to certify to** | **Gary, via D2** | **NEW.** :2026 is now published. Ask the certification body whether it can certify to :2026 within SESC's window and what transition it expects. Until it answers, build to :2015 + Amd 1:2024 and write 2026-ready (`CLAUDE.md` §6). **Record the answer here.** |
| **D17** | **Ventilation design in mould & damp work** | **Steve** | **NEW 24 Sep 2026.** Gary confirms SESC specifies ventilation (for example extractor fans) as part of mould & damp remediation. That is design, and it sits **outside** the D8 carve-out, which names only heat loss, emitter and heat pump sizing and MCS solar PV. The ¶58 wording would therefore exclude design SESC actually does — the same contradiction D8 was raised to fix. **Two options:** (a) extend ¶58 to include ventilation specification for mould & damp remediation, which brings it under clause 8.3 and needs professional indemnity cover that extends to it — **check the policy schedule, do not assume**; or (b) stop specifying ventilation and have it specified by others. Option (a) matches what SESC does. **A contractual term and an insurance question: Steve's decision.** Resolve before IMS-04 v0.3 goes to Steve for signature.<br><br>**24 Sep 2026, reported by Gary: option (a) — ventilation specification for mould & damp remediation goes into the ¶58 carve-out, and the Employer's professional indemnity insurance covers it.** The schedule page or endorsement that shows the cover is **not yet cited here** — cite it when IMS-04 v0.3 is drafted, because ¶58 asserts PI cover and the honesty convention needs the record behind it. Formal approval by Steve's signature on IMS-04 v0.3. **Found 24 Sep 2026, not yet read:** `Markel PI AHG015566 - policy schedule 2026-27.pdf` in `QinetiQ/JOSCAR/Insurance Docs/` and `Evidence Pack/03 Insurance/` of the TeraBox restore. 1b reads every page of it and cites the page.<br><br>**24 Sep 2026, workstream 1b: READ, all three pages, and it DOES NOT SHOW the cover.** The schedule covers professional liability, £250,000 aggregate costs-inclusive, for *"your professional services"* (p3 endorsement), but no page defines professional services or names any design activity. The Statement of Fact of 20-04-2026 (four pages, read) declares heating and ventilation engineering at 20% (p3), but **not mould and damp remediation.** **Gary's report that PI covers ventilation specification is therefore not supported by the record held.** IMS-04 v0.3 ¶58(d) says so. It forbids the "hold PI cover" wording for ventilation until the insurer or broker confirms in writing, and records the gap at Part 8(u). **D17 is OPEN on this point, and it is Steve's:** get written confirmation (and the policy wording), or take option (b). The chat stopped here. See F29. |
| **D18** | **Photographs and attachments on the record forms** | **Gary** | **NEW 24 Sep 2026.** Five schemas carry a `file` field. Apps Script cannot create a file upload question (F25). A Google community guide says upload questions force sign-in and **do not work for a form held on a Shared Drive**. Options: (a) **photos are filed by hand** in a `Record photos` folder on the Shared Drive, named by record reference, which is the default written into WI-01 ¶4; (b) add upload questions by hand to the domain-sign-in forms, **only if** testing shows uploads work on the Shared Drive; (c) wait for the SESC Platform. **Tell site nothing different from WI-01 until this is decided.** |
| **D19** | **Who needs an SESC sign-in to submit** | **Gary** | **NEW 24 Sep 2026.** Default in `Code.gs`: FRM-01 and FRM-02 **open**, with no sign-in (the near miss is anonymous by design). FRM-03…07 need a **domain sign-in**, with the verified email recorded. **If supervisors hold no SESC account, FRM-06 and FRM-07 must be open too.** Record the choice here before the build. |
| **D20** | **Workspace forms are a stopgap only, and the SESC Platform record capture section is built as soon as possible** | **Gary** | **NEW, CLOSED 24 Sep 2026: Gary's decision.** The Google Workspace forms (D15) stay as a stopgap only, to start the B3 clock. **A record capture section of the SESC Platform is to be built as soon as possible,** because the forms: (1) **cannot take photographs** (D18, F25); (2) **are not tamper-proof**, since the owning account and Shared Drive Managers can still edit (D15, README §10); and (3) **cannot prove who submitted an open form** (D19, F26). §6 item 8 is brought forward as **workstream 1c**. The Platform build is a separate workstream, not the 1b chat's. Field names stay aligned with `forms/SESC-FRM-01…07`, so nothing is re-keyed. Recorded at SESC-IMS-04 v0.3 ¶51. |
| **D21** | **The CMS Manual: its reference, and how it relates to SESC-IMS-04…10** | **Gary** | **NEW 6 Oct 2026.** James asks for the CMS Manual first. SESC already has IMS-04 (clause 4) and the `SESC-IMS-nn` spine for clauses 4–10. Options: (a) one **Integrated Management System Manual** as the top document, citing IMS-04…10 and the policies rather than repeating them; (b) the manual **is** the spine, IMS-04…10 as its chapters. Either way it is written in house style from SESC's facts; James's template is a heading checklist only (§7.2, F41). **Decide before drafting, and take the reference from §5 in the same turn.** |
| **D22** | **Stage 1 by end of October 2026** | **Steve** | **NEW 6 Oct 2026, agreed at the meeting (Gary).** Replaces Phase 4's Stage 1 window. Stage 2 still waits on records (§1.1). §2i.2, F50. |
| **D23** | **Site inspections in iAuditor (SafetyCulture)?** | **Gary, then Steve (spend)** | **NEW 6 Oct 2026.** James recommends iAuditor for Craig's site visits. SESC already has `SESC-FRM-07` Site Inspection for Workspace, with the Platform to follow (D15, D20). Using iAuditor as well would make a **third** place records live. Options: (a) iAuditor for site inspections, its template built field for field from FRM-07 so records export and migrate without re-keying; (b) stay with Workspace FRM-07 now and the Platform later. **Before choosing, read from SafetyCulture's own documentation: cost per user, export format, data location, and whether records are append-only.** A subscription is Steve's spend. |

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
| F20 | **Check accreditation and impartiality before the James Milligan meeting.** James is SESC's retained external H&S adviser (POL-05 Annex C) and is named as internal SHEQ Manager in SESC-CPP-001. The JOSCAR brief §4 records a "Subcontractor Performance Review (**ISO Certification Ltd**)" scored 10/10 by the supplier about itself, and the Architecture Plan §11 item 6 calls it an "unaccredited-looking ISO Certification Ltd relationship that will not satisfy a defence customer". **Whether isocertification.uk.com is that business has not been established.** The website could not be read on 24 Sep (TLS certificate verification failure). **Before any commitment:** who issues the certificate; is that body UKAS-accredited for 9001:2015, 14001:**2026** and 45001:2018 with IAF 28 in scope; and has that body, or anyone linked to it, consulted on SESC's system? A body cannot certify a system it helped build. **The stop rule applies: engaging a certification body is Steve's decision.**<br><br>**5 Oct 2026, from James's own template set (§2h): isocertification.uk.com IS James's business** — his templates name *"James Milligan TechIOSH, ISO Certification Limited"* and carry `james.milligan@isocertification.uk.com`; he now trades as The Milco Group Ltd (15837992). **He is the consultant, not a certification body.** The question becomes: which UKAS-accredited body does he intend, what is his link to it, and has it accepted that the builder is not the auditor. Q1–Q2 at §2h. | **High** | Gary, at the meeting on **6 Oct 2026**; then **Steve** |
| F21 | **The Master Register was not updated between 18 August and 24 September 2026**, although JOSCAR approval, D8, D11 and the records route all moved in that time. | Medium | **Closed by this v1.5 merge.** |
| F22 | **The design carve-out has not yet reached the standard quotation.** Until it does, quotations still exclude all design while SESC designs heat pump and solar PV systems. | Medium | Steve / Gary |
| F23 | **`CLAUDE.md` §11 gives Windows paths (`Desktop\SESC\...`)** that no longer exist on the working machine, and the handover's "Give Gary Git Bash syntax" rule no longer applies. Correct §11 to the MacBook paths by PR — **a separate commit from this one** (§7.8). The Claude Project instructions v2.0 already carry the Mac paths and zsh syntax.<br><br>**Closed 24 Sep 2026** by a separate commit on the same branch as register v1.7: `CLAUDE.md` §2, §9.4 and §11 now give macOS paths into the TeraBox restore and the MacBook clone, with the zsh rule. Every §11 path was checked to exist on the MacBook. **One correction found:** POL-01…04 sit in `QinetiQ/JOSCAR/Documents/2.2 Human Resources/` in the TeraBox restore, not nested under `2.7 Environment & Sustainability` as recorded on 18 August — confirm which is current before migrating them. | Medium | **Closed** |
| F25 | **The record forms cannot capture photographs as built.** Apps Script's `Form` class documents no method for adding a file upload question (checked 24 Sep 2026). A Google Docs Editors community guide, which is **not Google's own documentation**, says uploads force sign-in and are not possible for forms on a Shared Drive. The gap is recorded row by row in each `_field_map` as `NOT CREATED`, not hidden. | Medium | Gary, via D18 |
| F26 | **`SESC-FRM-02` Accident and Incident Report has no "reported by" field.** On an open form, nothing records who raised an accident report. RIDDOR and the investigation will want to know. **Not changed in this session**, because whether to capture it, and how given that witness names are deliberately kept out, is a design choice. | Medium | Health and Safety Officer / Gary, at FRM-02 v0.3 |
| F27 | **Renderer trap for workstream 2: numbered paragraphs restart at 1 after a table.** When SESC-WI-01 was rendered with plain Markdown, ¶3–6 printed as 1–4, and ¶7 onward restarted too. The `sane_lists` extension fixed it in the preview. `build/render_docx.py` must keep the source numbering. Add this to the four traps in `Section workflow method.md` §5. **24 Sep 2026: closed in `build/render_docx.py`. Source numbers are written as literal text, and `build/test_render_docx.py` checks every printed number. The recommendation for §5 is at §2g.1.** | Medium | **Closed (workstream 2)**; §5 wording is a recommendation only |
| F28 | **Google says forms created by API after 30 June 2026 start unpublished and receive no responses** (Forms API "API changes" guide). Whether this applies to Apps Script `FormApp.create` was not confirmed. `Code.gs` publishes where the method exists, and README §6.5 makes checking **Published** in the editor mandatory. | Medium | Gary, at build |
| F24 | **Before the MSI was retired, it was the only home of any unpushed work and of the untracked planning files (D10).** **Confirmed in part on 24 Sep 2026: the D13 change and register v1.4 had never been pushed**, and were recovered from the TeraBox restore as `4b9648d`. A comparison of the clone against the TeraBox copy of `CLAUDE ISO` on 24 Sep found every tracked file identical. **Present only in the TeraBox restore, not in the clone:** the D10 planning and review files (`SESC-IMS-Project-Instructions-v1.0.md`, `SESC-IMS-Readiness-and-Gap-Analysis-v1.0.html`, `SESC-IMS-Gap-Register-v1.0.xlsx`, `SESC-IMS-04-Context-of-the-Organisation-v0.2-REVIEW.html`, `SESC-Business-System-Project-Brief.md`, `SESC-Business-System-Project-Handover-v1.0.md`) and `sesc-ims-portal-2026-08-18.zip`. **What the TeraBox copy cannot show is anything on the MSI newer than the backup, or on an unpushed branch.** Record here whether the MSI was checked before retirement, and the date — or that it was not.<br><br>**Closed 24 Sep 2026: Gary confirmed the MSI was checked before retirement and nothing is outstanding.** | Medium | **Closed** |
| F29 | **The PI record does not show cover for ventilation specification in mould and damp remediation.** Markel schedule AHG015566 2026-27 (3 pp) covers *"your professional services"* without defining them. The Statement of Fact (4 pp) does not declare mould and damp remediation. The policy wording is not held. D17 was recorded on Gary's report that PI covers it, and that report has no record behind it yet. **Recorded at IMS-04 v0.3 ¶58(d) and Part 8(u). Not written as covered.** | **High**, because it blocks the ventilation element of v0.3 | **Steve** |
| F30 | **The EL/PL business description does not name mould and damp remediation.** The broker letter of 6 Aug 2026 lists alarm installation, electrical, plumbing and heating, solar panels, and roofing (by bona fide subcontractors only). Naming the trade in the ISO scope while the liability policy does not name it is a finding on one page, like ¶15(a) for roofing. Recorded at IMS-04 ¶16(a) and Part 8(r). | **High** | **Steve** |
| F31 | **The PI Statement of Fact of 20 Apr 2026 does not match the Employer.** It gives the trade as *"Electrical Contractor"* and **the number of directors as 2**, when the Employer has a sole director. Its employee and turnover figures are not reconciled to payroll or accounts. It declares no roofing and no mould and damp work. And it gives the basis of limit as *"Any one claim"*, while the schedule endorsement makes it aggregate. The Statement of Fact itself says that failure to correct it *"may make your policy voidable"*. **This is a statement to an insurer, so under the stop rule it is Steve's.** Not repeated in IMS-04, which states no headcount or turnover. | **High** | **Steve** |
| F32 | **`EL IP25BCONT00022472100.pdf` and `PL IP24BCONT00022472100.pdf` in `Insurance Docs/` are byte-identical** (MD5 `31ca4113…`). Both are the broker letter of 6 Aug 2026, not policy documents. The PL filename says `IP24B…` while the letter gives `IP24A…`. Feed this into IMS-04 Part 8(m). | Low | Accounts Manager |
| F33 | **IMS-04 v0.2 carried statements stale against this register:** 14001:2026 content asserted, the operating start date quoted as 30 Sep 2026, an encrypted records database described as existing, the wrong finding number, a missing revision row, a v0.1 footer, and three Part 8 due dates passed. **All corrected in v0.3 and listed in its Annex B.** | Low | **Closed in v0.3** |
| F34 | **F27 reproduced on IMS-04.** A plain Markdown render printed ¶13 as "14.". The preview was fixed by rendering each numbered paragraph with its source number, and all 67 were checked. **`render_docx.py` must do the same, and its test must compare every printed number with the source.** **24 Sep 2026: done.** All 99 labels on IMS-04 (67 paragraph numbers, 32 sub-labels) are checked against the source, in the DOCX and on the printed PDF: 19/19 tests pass. | Medium | **Closed (workstream 2)** |
| F35 | **The repository `github.com/GaryHill0985/QMS` is PUBLIC** (GitHub API, 24 Sep 2026: `"private": false`, `"visibility": "public"`). Anyone can read this register and every draft, including the insurance positions, the gap inventories and F31, and CLAUDE.md §8 personal-data rules then depend entirely on the validator. Found because the device shell cloned it over HTTPS with no credentials. **Making it private is a repository setting, so Gary's.** It does not affect signed commits or the ruleset. **24 Sep 2026 (Gary): still public, decision open.** | **High** | **Gary** |
| F36 | **`.DS_Store` was staged in the clone's index** (`git status` showed `A  .DS_Store`) when this session started. Nothing in `.gitignore` excluded it, so the next `git commit -a` or `git add .` would have committed Finder metadata. `.gitignore` now excludes it. **It must still be unstaged by hand.** | Low | Gary, before the workstream 2 commit |
| F37 | **`.github/workflows/ci.yml` cannot be written from a Cowork session** (the device bridge refuses: a protected file). The renderer tests are therefore not in CI until Gary copies `Claude outputs/ci.yml.workstream-2` into place. A control Claude cannot change without Gary is arguably the right way round. | Low | Gary |
| F38 | **`issued:` on a draft does not mean issued.** IMS-04 v0.3 is a draft that has never been issued, yet its front matter carries `issued: 2026-08-18` (the first-draft date), because the schema requires the field. The renderer prints *Not issued* for any draft, so no document says otherwise. But the schema should say what `issued` means before a first issue, or allow it to be empty for a draft. | Low | Gary, at the next schema change |
| F39 | **`portal/config.yaml` is stale against this register.** Its `trades` line omits mould and damp remediation (D11). Its milestone for 30 Sep 2026 says *"The date to quote when asked when the management system started working"*. That contradicts B3, and IMS-04 ¶39 was corrected for the same statement in v0.3 (F33). The portal publishes it, including to the auditor build. | **Medium** | Later chat |
| F40 | **IMS-04's source ends with a typed footer carrying "v0.3".** That is the kind of typed version number CLAUDE.md §5 forbids. The renderer drops it, and fails the build if its version ever disagrees with the front matter, so it cannot drift silently. Remove it at v0.4. | Low | Later chat, at IMS-04 v0.4 |
| **F41** | **James Milligan's template set carries another company's controlled documents.** 93 toolbox talks are numbered `HCPL-TBT-nnn` (index dated 6 July 2021) and 92 of 128 `.docx` files reference HCPL. 32 control rows read "ISO Certification Ltd". Under §7.2 none of it enters the repository as content. **Add `HCPL` to the forbidden-reference list in `CLAUDE.md` §3 and §7.2.** | **High** | Later chat, by PR |
| **F42** | **James's templates are built to ISO 14001:2015, withdrawn 15 April 2026**, and his Generic Risk Assessments still cite ISO 9001:2008 and 14001:2004. A consultant proposing to build SESC's EMS has not updated for the edition SESC must certify to. Ask (Q3) and record at B4 / D16. | **High** | Gary, at the meeting |
| **F43** | **F20's open question is answered by James's own documents: isocertification.uk.com is his business.** He is a consultant (now The Milco Group Ltd), not a certification body. The impartiality risk therefore sits with whichever body he introduces, not with him directly — unless he audits for it. Q1–Q2. | Medium | Gary → Steve |
| **F44** | **James's internal audit procedure names "ISO Certification Limited" as the independent auditor** — the consultant who supplies the documents audits them. Acceptable to some certification bodies, weak evidence of independence for ISO 45001 9.2.2 c) and 9001 9.2.2 c), and it leaves B5 (a second competent person at SESC) exactly where it is. | Medium | Steve, via D3 |
| **F45** | **The Dropbox is a third-party-controlled store on James's subscription.** No personal data (CLAUDE.md §8, POL-14), no insurance documents and not this register go to it. If SESC uses it for anything beyond transfer, a data-processing arrangement and 2-step verification on every account are needed — and access ends when the engagement ends. Q7. | Medium | Gary |
| **F46** | **James's option (a), "use this as the document builder, then transfer", would create a second master.** Four drift incidents on this project say no. His option (b), "give me access and we build to that", fits CLAUDE.md §5 and §7.7 — but no access is given before Steve decides the engagement (Q8, Q9). | Medium | Gary → Steve |
| **F47** | **Workstream 2 was never committed, and the v1.12 row misattributes PR #10.** `git status` on 5 Oct 2026 showed `build/render_docx.py`, `build/test_render_docx.py` and `build/assets/` untracked, `.gitignore` and `standards/front-matter-schema.yaml` modified and unstaged, and the register modified — with `main` up to date with `origin/main`. `git show --stat 02650c7` lists only `SESC-IMS-Master-Register.md` and `system/4-context.md`: **PR #10 is workstream 1b.** So `main` holds register v1.11, and register v1.12 and the whole of workstream 2 existed only in the working tree for eleven days. The v1.12 row is corrected below. The `.DS_Store` of F36 was also still staged. Found by §7.7: a file expected to be committed, and which was not. | **High** | Gary — commit workstream 2 and the register as two commits on one branch, 5 Oct 2026 |
| **F48** | **PJR's UKAS schedule (0105, issue 046, 22 Apr 2026) does not list ISO 14001:2026.** `CLAUDE.md` §6 requires 14001:2026 and forbids a :2015 certificate. Either PJR extends in time, or the rule is revisited on PJR's written answer. Also not established: which PJR entity's accreditation Stephen Lloyd audits under (the schedule lists no UK office). §2i.1. | **High** | Gary → Steve |
| **F49** | **No fire risk assessment for the Employer's own premises (Unit 19) was found in the project records searched on 6 Oct 2026** (the register, the JOSCAR evidence pack, POL-05, REG-02). POL-05 ¶119 and ¶142 cover fire risk per project, through the RAMS. **Confirmed by Gary, 6 Oct 2026: SESC does not currently have a fire risk assessment for its premises.** That is a legal duty under the Regulatory Reform (Fire Safety) Order 2005 now, before it is an ISO 45001 8.2 point, so it should not wait for the ISO timetable. James's walk-round items FS-01…12 are at §2i.3. Item FS-12 (electrical cupboard) sits beside F4 (PAT testing as an insurance condition precedent). | **High** | Steve / Craig |
| **F50** | **Stage 1 is targeted for end of October 2026, but the scope statement is unsigned (F29–F31), no aspects register of SESC's own exists, no internal audit programme or management review is scheduled, and no live record exists.** Stage 1 can still run and raise findings; Stage 2 cannot pass without operating history. Ask PJR the Stage 1 document list and the maximum Stage 1–Stage 2 interval. §2i.2. | **High** | Gary |
| **F51** | **Craig Bartle's NEBOSH qualification is not on the record.** Gary believes Craig holds a current NEBOSH qualification (6 Oct 2026). No certificate has been read on this project; the only NEBOSH qualification recorded is James Milligan's NGC. **Read Craig's certificate (award, grade, date) before any document names it.** NEBOSH certificates do not expire, so whether it is current means whether his CPD and role-relevant training are current. Craig is already named across the signed documents as Quality Representative, H&S Officer, Environmental Manager and regulation 7 competent person; **he reviews and is named, but only Steve signs** (D12, CLAUDE.md §2). His certificate is personal data: it is held in Workspace under POL-14, never in git. | Medium | Craig → Gary |

---

## 6. What happens next — one workstream per chat, in this order

**From 24 September 2026, 1a and 1b come first; the existing order then resumes at 2.**

| Order | Workstream | Why this order | Est. |
|---|---|---|---|
| ~~1~~ | ~~Push to GitHub, protect `main`, require PR review, require signed commits~~ — **ALL DONE 18 Aug 2026.** See §2b. Remaining question is D12, whether Steve becomes a collaborator. | Everything now arrives as a pull request. | Done |
| **1a** | **NEW 24 Sep 2026 — Google Workspace record capture** (D15): Forms for FRM-01…05 plus toolbox talk and site inspection, the Shared Drive, and a one-page "how to log it" for site. **Repository side DONE 24 Sep 2026 (§2e): FRM-06, FRM-07, WI-01 and the generator. Workspace side is Gary's: README §2–§7.** | **Starts the B3 clock. Nothing else moves the certification date as much.** | 1 session + Gary's build |
| **1b** | **NEW 24 Sep 2026 — `SESC-IMS-04` v0.3.** **DRAFTED 24 Sep 2026 (§2f):** mould & damp named at ¶14, D8 + D17 carve-out at ¶58, fire doors removed. **With Steve for F29 (PI cover for ventilation), then signature.** | The scope statement is the first thing a certification body reads. | Done, awaiting Steve |
| **1c** | **NEW 24 Sep 2026 (D20) — the record capture section of the SESC Platform**, brought forward from item 8: photos, tamper-evident append-only records, and an authenticated submitter, with field names aligned with `forms/SESC-FRM-01…07`. **A separate workstream. Its own chat.** | The Workspace forms cannot take photos, are not tamper-proof, and cannot prove who submitted an open form. | Platform sessions |
| ~~2~~ | **DONE 24 Sep 2026 (§2g).** **Port `policy_editor.py` to `build/render_docx.py`** and render `SESC-IMS-04` to a branded PDF, then **read the cover and a body page as images**. | Renderer parity is the Phase 1 gate. Four known traps live in `Reference\Section workflow method.md` §5. | 1 session |
| 3 | **`SESC-IMS-05` Leadership**, including the integrated IMS policy that supersedes the three separate policy statements, and the 45001 clause 5.4 worker consultation mechanism. | 5.4 is the clause 45001 auditors test hardest and it is entirely absent. | 1 session |
| 4 | **The environmental aspects and impacts register, built from SESC's own activities.** | **The defining ISO 14001 document and the highest-priority gap in the system.** The one held belongs to a landscaping firm. Blocked on buying 14001:2026 (D6). | 1–2 sessions |
| 5 | **The compliance obligations register**, replacing the 2020 register with dead drive links. | 14001 6.1.3 and 45001 6.1.3 are both dual maintain-AND-retain. | 1 session |
| 6 | **The four core procedures** — document control (7.5), internal audit (9.2), management review (9.3), nonconformity and corrective action (10.2). | The procedures the certification body asks for first, and which no SESC document currently provides. | 2 sessions |
| 7 | **Migrate POL-16 into the repository end to end** as the reference implementation, then the remaining twenty. | Do one and verify it before bulk migration. | 1 + 2 sessions |
| 8 | **The records layer** — form schemas, mobile capture, and records accumulating weekly **by someone other than Gary.** | This is the clock everything else waits on, and it is the real gate on Stage 2. **The Workspace stopgap is pulled forward to 1a (D15). The Platform's record capture section is pulled forward to 1c (D20).** What stays here is records accumulating weekly. | Phase 2 |

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
| 1.14 | 6 October 2026 | Claude, for G A Hill | **Outcome of the James Milligan meeting** (Gary's account). New D23 (iAuditor for site inspections) and F51 (Craig's NEBOSH certificate not yet read). New §2i: PJR / Stephen Lloyd as certification body (D2), James as internal auditor (D3), CMS Manual first (new D21), Stage 1 by end Oct 2026 (new D22), premises fire safety items FS-01…14. PJR's UKAS schedule 0105 read: 14001 at :2015 only (F48). No premises fire risk assessment found (F49). Stage 1 readiness gaps (F50). **Nothing signed, contracted or committed.** |
| 1.13 | 5 October 2026 | Claude, for G A Hill | **Pre-meeting review of James Milligan's Dropbox template set.** New §2h. The email of 26 Sep 2026 read; all 173 files inventoried, every Office file opened and text-extracted, the key documents read. The set is a generic ISO Certification Ltd template kit built to 14001:2015, carrying 93 HCPL-numbered toolbox talks and no records. F20 updated: isocertification.uk.com confirmed as James's business; he is the consultant, not a certification body. D2 re-framed: 6 Oct is a consultant conversation; who certifies stays open. New findings F41–F46. Nine meeting questions Q1–Q9 and an upload list recorded at §2h. **Nothing uploaded, signed, merged or committed; no other file changed.** **Then, from `git status`: F47 — workstream 2 and register v1.12 were never committed; PR #10 was 1b. v1.12 row annotated.** |
| 1.12 | 24 September 2026 | Claude, for G A Hill | **Workstream 2.** New §2g. `build/render_docx.py` ported from `policy_editor.py` and `sesc_cover.py`, with the control block, header and footer generated from front matter. `build/test_render_docx.py` (19 tests) checks every printed paragraph number against the source (F27 and F34 closed). Brand assets added to `build/assets/`. Optional `revised` and `prepared_by` added to the front-matter schema. `.DS_Store` added to `.gitignore`. IMS-04 v0.3 rendered to a 21-page branded DOCX and PDF, read as images, and compared with signed POL-16 v1.2. **IMS-04 not edited, nothing signed.** The F27 trap recommended for `Section workflow method.md` §5 (§2g.1); the TeraBox file was not edited. **PR #10 recorded as merged at `02650c7`; `a082eff` and `3965225` Verified on GitHub (Gary).** ~~That PR is workstream 1b; this workstream 2 and this v1.12 were NOT committed on 24 Sep 2026 — see F47, found 5 Oct 2026.~~ F29: no change. F35: still public, decision open. New findings F36–F40. |
| 1.11 | 24 September 2026 | Claude, for G A Hill | **Workstream 1b.** New §2f. `SESC-IMS-04` amended in place to **draft v0.3**: D11 (mould & damp remediation named, as remediation only; fire doors removed), D8 + D17 carve-out at ¶58, with the PI record cited page by page. **The PI schedule does not show cover for ventilation specification. The chat stopped on that point (F29, Steve).** D8, D11 and D17 rows updated. D15 updated. **New D20: Workspace forms are a stopgap only, and the Platform record capture section is built as soon as possible (Gary). §6 item 8 brought forward as 1c.** New findings F29–F35, including **F35: the repository is public.** PR #9 (1a) confirmed merged as `4490e88`. |
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
