# SESC-IMS-Master-Register

**The state of the CLAUDE ISO project. v1.18 · 7 October 2026.**

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
| **This repository holds** | 3 controlled source files, 134 clauses across 3 standards, CI passing. **From 24 Sep 2026: a branded renderer, `build/render_docx.py`, with its tests (§2g).** **From 6 Oct 2026: `SESC-IMS-00` IMS Manual, draft v0.1 (§2j).** **From 7 Oct 2026: `SESC-REG-08` Opportunity Register, draft v0.1, and `build/export_coto.py`, the generated COTO Log workbook (§2l).** **From 7 Oct 2026, workstream 3: `SESC-IMS-05` Leadership, draft v0.1, with the integrated policy statement and the 45001 5.4 mechanism, and `SESC-FRM-08` Worker Consultation Record, draft v0.1 (§2m).** **From 7 Oct 2026 the project has three sources only: `~/Documents/SESC/ISO/`, GitHub `QMS`, and the Drive for record capture (§2n, `CLAUDE.md` §11).** |

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

## 2j. Workstream — `SESC-IMS-00` Integrated Management System Manual, draft v0.1, 6 October 2026

**Taken:** the D21 drafting workstream only. Gary's instruction *"Draft SESC-IMS-00, the IMS Manual, per D21"*
confirms the reference proposed at D21. **`SESC-IMS-00` is DRAFT v0.1, not approved and not issued. The approval
block at Part 11 is empty.** Nothing else in the system was changed except as listed below.

**State of the clone at the start (read-only `git --no-optional-locks status`):** branch `register-v1.14`,
tracking `origin/register-v1.14` at `48ddbba`, with **`SESC-IMS-Master-Register.md` modified and uncommitted**
and `Claude outputs/` untracked. Per §7.7 this is recorded, not assumed: the working-tree register (v1.14 with
FS-13, FS-14 and F51) is newer than the committed v1.14, and this session built on the working-tree copy.
**Gary to confirm that the uncommitted v1.14 additions are his and commit them before, or with, this change.**

| Built | Where | Status |
|---|---|---|
| **`SESC-IMS-00` Integrated Management System Manual.** Option (a) of D21: one manual on top of the spine. 68 numbered paragraphs in eleven Parts plus three annexes. Parts 3–9 walk clauses 4–10 in the heading order of James Milligan's template manual (used as a **heading checklist only**; no sentence, list or table was taken from it). Each Part says how the Employer meets the requirement and points to IMS-04, the signed policies, the registers and the forms; where nothing exists it says so. Part 10 is the dated inventory of 23 records and documents not yet held, (a)–(w). Annex B is the **document map**: every clause of the three standards against the document that addresses it today, or *not yet* with the Part 10 reference. The scope statement is reproduced verbatim from IMS-04 ¶14. | `system/0-manual.md` | **Draft v0.1** |
| **Clause map claimed: 4.4 (9001 4.4.1, 4.4.2) and 7.5.1, all three standards — and nothing else.** The manual describes the system and its processes, and defines the documented information the system consists of and how it is controlled. It does **not** claim 5.3 although it summarises roles, because IMS-04 ¶11 and the policies are the authoritative statements; Annex A says so. | front matter | — |
| **Renderer: `header_right()` and `cover_note()` handle `IMS-00`.** Without the change the header printed *IMS · Clause 0* and the cover *CLAUSE 0 // …*. Now *IMS · Manual* and *MANUAL // ISO 9001 · ISO 14001 · ISO 45001*. Clause chapters 04–10 unchanged. **Two tests added** (`TestIMS00Labels`); 22/22 pass on the MacBook. | `build/render_docx.py`, `build/test_render_docx.py` | Done |
| `CLAUDE.md` §5: the series rule now names `SESC-IMS-00`; the next-free line records it as taken on 6 Oct 2026. | `CLAUDE.md` | Done |

**Facts the manual states, and their sources.** Every present-tense statement traces to IMS-04 v0.3 (identity,
governance, roles at ¶11, scope at ¶14, the 8.3 determination, Part 8), to this register (what does not exist:
no audit ever, no management review since 10 Jan 2023, no aspects register, 2020 obligations register, no NC log,
forms not live, no premises FRA — F49, waste tier unconfirmed — F8, standards not held — D6/B4), or to
`registers/documents.yaml` (the titles and versions of the 21 signed documents and REG-02…04, REC-01…04,
CAP-002…014). **Where the manual points into a signed policy it names the document and, only where this register
already records the section (POL-16 Annex B and Annex C, POL-05 Annex C, POL-19 Annex A), the section.** Four
sentences drafted from assumption about the content of POL-05, POL-08 and POL-14 were caught on review and
rewritten before render. Headcount, turnover and PI limit appear nowhere. **PJR and James Milligan's proposed
roles are not named in the manual**: the certification body and the internal auditor are "proposed, before the
Managing Director" (Part 10 (u), (w)), because neither is decided (D2, D3, stop rule). James is named only in
the role he already holds, retained external H&S adviser, from IMS-04 ¶11.

**Verification.**

1. `build/validate.py`: **0 errors**, 11 warnings (the expected 14001 `verified: false`, now including
   `system/0-manual.md`), 3 notes. BUILD PASSES.
2. `python3 -m unittest build.test_render_docx`: **22/22 pass**, including the two new IMS-00 tests and the
   IMS-04 printed-number test.
3. Rendered on the MacBook with `build/render_docx.py --pdf` to `Claude outputs/ims00/SESC-IMS-00-v0.1-DRAFT.docx`
   and `.pdf`: **20 pages** (cover + 19). **All 68 source paragraph numbers print in order** (checked from the PDF
   text layer against the Markdown; 68 = 68, no gaps, no restarts).
4. **Read as images:** the cover (p1), the control page (p3), the process table ¶19 (p6), the Part 10 table
   (p15), the approval block and Annex A (p17) and the Annex B document map (p18). Cover: MANAGEMENT SYSTEM ·
   *MANUAL // ISO 9001 · ISO 14001 · ISO 45001*, six fields reading *0.1 — DRAFT, NOT ISSUED* · *Not yet approved
   (Managing Director)* · *G A Hill (drafted by Claude)*. Control table: *Issue date: Not issued*, *Next review: Set
   on issue*. **Approval block: Reviewed by, all three Dates and Signature are empty.** The status banner and the
   "holds no ISO certification" callout render as the red-keyline callout.
5. **Two cosmetic defects, not fixed:** the Group column of the ¶19 table wraps *Manage-ment* over two lines, and
   the Annex B header wraps *CLAUS-E*. Both are column-width effects of the renderer's `_widths()` on six-column
   tables. Recorded as F54; fix in the renderer, not by shortening the words.

**Not done, deliberately.** The manual was not uploaded to James's Dropbox (F45, F46; Gary's call — it may go
to `To be uploaded` **only clearly marked DRAFT**, which the file is on every page). Nothing was committed:
Claude does not run git against the clone (§7.7). `Claude outputs/ims00/` holds the render plus twenty page PNGs
and a LibreOffice lock file; all gitignored, none needed after Gary has looked at the PDF.

**Tasks by owner, from this session:**

| Owner | Task | By |
|---|---|---|
| **Gary** | Confirm the uncommitted register v1.14 working-tree additions are his; then commit this workstream as **two commits on one branch** (§7.8): (1) `system/0-manual.md` + renderer + tests + `CLAUDE.md` §5; (2) register v1.15. Commands below. **Claude does not merge.** | this week |
| Gary | Read the 20-page PDF in `Claude outputs/ims00/` end to end before it goes anywhere. | before sending |
| Gary | Send IMS-00 v0.1 to James Milligan for his review, **as a DRAFT**, with IMS-04 v0.3 DRAFT alongside — he asked for the manual first (§2i). Record his comments here; changes go in as v0.2 by PR. | after commit |
| Gary | Decide whether the manual goes into the Dropbox `To be uploaded` folder (F45/F46) or by email. | with the above |
| **Steve** | Review IMS-00 v0.1 Part 10 — it is the list of what he will be asked for at Stage 1 — and confirm or re-date the rows marked *proposed*. **Signature follows IMS-04's, not before.** | before Stage 1 |
| Later chat | F54: `_widths()` for six-column tables. | with the next renderer change |
| Later chat | IMS-05 Leadership (§6 item 3) is now the next spine document: the integrated policy statement and the 5.4 mechanism. Part 10 (c) and (d) of the manual depend on it. | next chat |
| Later chat | When IMS-05…10 are issued, IMS-00 Annex B rows move from the policies to the spine, by PR, as a new version. The front-matter `review_trigger` says so. | each spine issue |

**Completion note.** The manual exists as a 20-page branded draft that claims two clauses, points to everything
else, and carries a 23-row dated inventory of what is not yet there. It names no headcount, no turnover, no
insurance limit, no certification body and no certification. The renderer now knows what `IMS-00` is, and
proves it in a test. The approval block is empty, nothing was committed, and the clone's branch carried an
uncommitted register when this session began — that last point is Gary's to resolve before this change is added
on top.

---

## 2k. Review — James Milligan's CMS H&S Policy Manual and COTO Log templates, 6 October 2026

**Taken:** a read of the two remaining files in `1. Context of the Organisation` (`CMS Health and Safety Policy
Manual.docx`, 1,313 paragraphs, 34 sections and four appendices; `CMS COTO Log.xlsx`, six sheets: Parties, Issues,
Risk Register, Opp Register, Lists, Risks 27001), after Gary asked for SESC versions of both. **Same chat as §2j,
analysis only — nothing was built, under the one-workstream rule.** The device link dropped mid-read; the read of
POL-05 below is from its contents page and the lead sentence of each of its 175 paragraphs, **not all 32 pages**.

**Finding on both: SESC's version already exists, and a new document from either template would be a second
master.**

| Template | SESC already holds | What the template adds |
|---|---|---|
| H&S Policy Manual | **SESC-POL-05 v1.1**, signed, 32 pp: Part 1 statement, Part 2 O1–O7, Part 3 A1–A31, Annexes A–D including A31 records-not-yet-held. Every template section maps to a POL-05 section or a separate signed policy (POL-08, POL-11, POL-06) except **four candidates with no named section found: housekeeping (9.0), DSE (18.0), young persons (19.0), electricity at work (29.0)**. The template still carries fabrication-workshop content (lathes, metalworking fluid, machine guarding) and the adviser's CV as an appendix. | Nothing as content. The four candidates go to POL-05 v1.2 **after a full read of all 32 pages**. |
| COTO Log | Parties → **SESC-REG-05** (15 parties, 43 requirements with obligation type, evidence and gap — richer than the template's three columns). Issues → **SESC-REG-06** (30 issues; risks and opportunities in separate fields). Risk Register → **SESC-REG-01** (signed, 26 scored risks). Risks 27001 → out of scope (D1). | **A scored opportunity register with a pursuit plan and status, kept apart from risks** — which 9001:2026 wants and REG-06 holds only as a field. Also the Issues sheet's *processes affected* and *treatment* columns, which would tie REG-06 to the process model at IMS-00 ¶19. Demo rows ("attorney", "CPA", "Acme Calibration Labs") and "ISO Certification Ltd" control rows confirm §7.2: structure only. |

**Decisions taken by Gary this session:** D24 and D25 below.

**Delivered:** `Claude outputs/SESC - POL-05 against the CMS H&S Policy Manual template - 6 Oct 2026.md` — a one-page
section-by-section map for James, marking the four candidates as candidates, not findings, and saying what POL-05
has that the template lacks.

**Tasks by owner, from this section:**

| Owner | Task | By |
|---|---|---|
| Gary | Send James the **signed** POL-05 v1.1 PDF (`QinetiQ/JOSCAR/Documents/2.6 Health & Safety/Branded/Signed/`) with the comparison note, as SESC's H&S Policy Manual. Not the template filled in. | with IMS-00 |
| Next chat (**workstream 2b**) | **D24:** `SESC-REG-08` Opportunity Register as YAML, with a scoring scale, pursuit plan, owner and status; a `build/export_coto.py` that writes a read-only *SESC COTO Log* workbook from REG-01 (when migrated), REG-05, REG-06 and REG-08 in the template's tab layout, marked *generated — do not edit*. Take REG-08 from `CLAUDE.md` §5 in that chat and update the next-free line. REG-01 is not yet in the repository, so the first export carries its reference and a pointer, not its rows. | next chat |
| Later chat (POL-05 v1.2) | **D25:** read all 32 pages of POL-05; confirm or close the four candidates (housekeeping, DSE, young persons, electricity at work) and the two to-confirms (visitors to Unit 19; skin surveillance in A22); add mould and damp remediation to ¶2 (D11); reference the premises FRA from A25 once it exists (F49). Amend in place as v1.2 by PR; Steve signs. | after James's review |
| James | Review POL-05 v1.1 and the four candidates; say what would not satisfy 45001 at Stage 1 | per engagement |

**Completion note.** Both templates read in full; both found to duplicate documents SESC already holds. Nothing
built, nothing uploaded, nothing changed in the system except this register. The one structural idea worth taking,
an opportunity register, is queued as workstream 2b with its reference to be taken in that chat.

---

## 2l. Workstream 2b — `SESC-REG-08` Opportunity Register and `build/export_coto.py`, 7 October 2026

**Taken:** workstream 2b only (D24). **Started once `main` was confirmed to contain PR #14.** Read-only
`git --no-optional-locks log` in the clone: `main` at **`965535b`** (*Merge pull request #14 from
GaryHill0985/workstream-ims00-manual*), parents `a4ab77f` (register v1.15–v1.16) and `c71f25c` (IMS-00 draft
v0.1, renderer labels, `CLAUDE.md` §5); `git ls-tree main` lists `system/0-manual.md`. Working tree clean apart
from the untracked `Claude outputs/` folder. **F53 is therefore CLOSED by that merge** — the v1.14 additions
(FS-13, FS-14, F51) are in `a4ab77f`. Nothing else in the system was changed except as listed below.

| Built | Where | Status |
|---|---|---|
| **`SESC-REG-08` Opportunity Register.** Reference taken from `CLAUDE.md` §5 in the same change. **Ten rows, every one seeded from an opportunity already recorded in `SESC-REG-06` v0.1** — the ten `opportunities:` bullets across EXT-02 (2), EXT-05, EXT-07, CLI-04, CLI-05, CLI-07, INT-03 and INT-09 (2) become OPP-01…OPP-10, each carrying its `source`. **Nothing was invented, and no candidate row exists**: the register defines a `candidate` status for any opportunity not taken from REG-06, and v0.1 holds none. Each row: process (from IMS-00 ¶19, itself a draft), likelihood 1–5 × benefit 1–5 = score, band, pursuit plan, owner, status, review date, record reference. **Every score and plan is marked `confirmed_by_owner: false`** and the header says they are proposals. A pursuit plan is written only where a recorded decision or document gives one (D1, D2, D8, D11, D17, D21, F29, F30, CLAUDE.md §3, §2c); otherwise it reads *not yet defined* and names the role that defines it. Risks stay in REG-01 and are never held here. Carries a *Records held, records not yet held* block (three absent records, dated) and a revision history. | `registers/opportunities.yaml` | **Draft v0.1** |
| **Clause map claimed: 6.1.1 of all three standards, and nothing more.** Not 6.1.2, not 6.2 (an opportunity with a plan is not an objective with a measure), not 10.3 (nothing here has produced evidence of improvement). The file header says why. | front matter | — |
| **Scoring scale.** 1–5 likelihood × 1–5 benefit, the same shape as REG-01's likelihood × impact, so the two registers read alike without being merged. **Bands (pursue ≥ 15, evaluate 8–14, hold ≤ 7) are proposed for Steve to confirm on approval**, and the YAML says so. Scores in v0.1: two at 20 (OPP-07 decarbonisation, OPP-08 the honesty convention), one at 16 ×2, one at 15, five at 9–12. | `scoring:` block | proposed |
| **`build/export_coto.py`.** Writes the read-only *SESC COTO Log* workbook from REG-05, REG-06 and REG-08 to `out/SESC-COTO-Log.xlsx` (`out/` is gitignored — a build artefact, never committed). Tabs, in the template's order: **Cover** (banner *GENERATED FROM THE REPOSITORY — DO NOT EDIT*, generation time, HEAD commit read with `--no-optional-locks` plus a flag if `registers/` has uncommitted changes, a source table with each register's version and status, eight notes) · **Parties** (REG-05, one row per requirement) · **Issues** (REG-06, with *Bias* derived from what each row holds and an *Opportunities — REG-08* column pointing at OPP refs) · **Risk Register** (**REG-01 reference and pointer only**, control data read from REG-07 at run time, plus the 21 REG-01 risk ids REG-06 refers to) · **Opportunity Register** (REG-08) · **Lists** (the scales, bands, statuses and value lists, all read from the registers). **No Risks 27001 tab (D1).** Every sheet is protected and the workbook structure locked — a signal, not a security control, and the cover says so. `--check` reopens the file and compares every data tab's row count with the YAML. | `build/export_coto.py` | Done |
| **Structure from the template, no content (§7.2, F41).** Read from `CMS COTO Log.xlsx` (`~/Documents/SESC/SESC Solutions Limited/1. Context of the Organisation/`, access granted for this chat): the six tab names, the one-row-per-item shape, the Lists-tab idea, and that the Opp Register scores probability × benefit with a pursuit plan and a status. **Column headings are SESC's field names. Not one party, issue, risk, opportunity, process, scale label or list value was copied.** The template's benefit sub-columns, likelihood wording, process list and demo rows were not carried. | — | — |
| `CLAUDE.md` §5: next-free line records `SESC-REG-08` as taken on 7 Oct 2026 under D24; next free register is `SESC-REG-09`. | `CLAUDE.md` | Done |

**Verification.**

1. `build/validate.py`: **0 errors**, 12 warnings (the expected 14001 `verified: false`, now including
   `registers/opportunities.yaml`), 3 notes. BUILD PASSES. 14 controlled files.
2. `python3 build/export_coto.py --check`: Parties 44 = 44, Issues 30 = 30, Opportunity Register 10 = 10,
   15 distinct parties = 15, Risk Register pointer only, Cover banner present. **Counted independently with
   `grep`** on the YAML: 44 `- requirement:` lines, 15 `IP-` refs, 30 issue refs, 10 `OPP-` refs, and **10
   opportunity bullets in REG-06** — so REG-08 holds exactly the opportunities REG-06 records.
3. **The workbook was opened** (openpyxl: six tabs in the right order, all protected) **and rendered** with
   LibreOffice to a 12-page landscape PDF (`Claude outputs/coto/`), **read as images**: the cover (p1), the
   Parties tab (p2), the Issues tab (p5), the Risk Register pointer (p7), the Opportunity Register (p8, both
   halves) and the Lists tab (p9). Every column prints, the banner is on every tab, and the footer reads
   *generated from the repository — do not edit — page n of 12*. The first render printed as 44 strip pages
   because the fit-to-width setting had not reached the file (F56); fixed and re-rendered.
4. **F55 found by the count:** this register's §2 row and the REG-05 title say *43 requirements*; REG-05 v0.2
   holds **44**. The F16 restoration added the first-aid needs assessment requirement at IP-06. 44 is right.

### 2l.1 IMS-00 Part 10 (a)–(w) reconciled against §6 and the task tables; `portal/actions.yaml` resynced

**Added by Gary mid-chat as task 5.** Every row of IMS-00 v0.1 Part 10 ¶63 was checked for a home in §3–§6 and
in the tasks-by-owner tables of §2e–§2k. **Thirteen of twenty-three had an owner and a date in a task table.
Ten did not, in whole or in part — four of them (j, k, l, s) appeared nowhere in this register** — and are
added below as tasks by owner, and to `portal/actions.yaml` as new gaps G10–G17 with G1, G2 and G6 updated.
Dates are IMS-00's, *proposed* where it says so; nothing is re-dated here.

| Part 10 | Already recorded at | Gap in the tables |
|---|---|---|
| (a) standards | B4, D6 | — |
| (b) signed IMS-04 and the insurance records | D17, F29–F31, §2f Steve tasks | — |
| (c) integrated policy statement and IMS-05 | §6 item 3 only | **No owner task.** Added: COO drafts, Steve signs, 31 Oct 2026 (proposed). G16 |
| (d) 5.4 mechanism with records | REG-05 IP-01, G6 | **Task table holds only the first toolbox talk.** Added: H&S Officer, mechanism in IMS-05, 31 Oct 2026. G6 updated |
| (e) premises FRA | F49, FS-01…14, §2i tasks | — |
| (f) aspects register | §6 item 4, G4 | — |
| (g) compliance obligations register | §6 item 5, G5 | — |
| (h) minuted management review | G2, CLAUDE.md §10 | **No owner task, and overdue against 30 Sep.** Added: Steve, 31 Oct 2026 (proposed). G2 updated |
| (i) NC/CA log | G3, go-live tasks | — |
| (j) environmental and OH&S objectives | **nowhere** | **Overdue against 30 Sep; absent from every table.** Added: Steve, 31 Oct 2026 (proposed). New G10 |
| (k) calibration register | **nowhere** | Added: Contracts Manager, 30 Nov 2026 (proposed). New G11 |
| (l) role-based competence register | **nowhere** | Added: Contracts Manager, 30 Nov 2026 (proposed). New G12 |
| (m) induction and toolbox talk records | §2e H&S Officer and Contracts Manager tasks | — |
| (n) first live record | B3, §2e Gary tasks | — |
| (o) PRO-01 and the core procedures | §6 item 6, G9 | — |
| (p) quotation and CAP-008 | F22 | — |
| (q) approved supplier register | REG-05 IP-12 (overdue 30 Sep), §2e Contracts Manager FRM-04 task | **Register itself has no task.** Added: Contracts Manager, 30 Nov 2026 (proposed). New G13 |
| (r) waste carrier tier | F8 | — (overdue; F8 re-dated 31 Oct in actions.yaml per Part 10) |
| (s) spill response test | **nowhere** | Added: Environmental Manager, 31 Jan 2027 (proposed). New G14 |
| (t) customer satisfaction | REG-05 IP-02 | **No task.** Added: Quality Representative, 31 Dec 2026. New G15 |
| (u) audit programme, auditor, first audit | D3, B5, G1 | **Programme has no owner task.** Added: COO, programme 31 Oct 2026; first audit 30 Nov (proposed). G1 updated |
| (v) migration of the 21 documents | §6 item 7 | — (G17 added so the portal shows it) |
| (w) the certification body's written answers | §2i Gary task "this week" | — (T-W in actions.yaml) |

**`portal/actions.yaml` resynced** from register v1.4 (18 Aug 2026) to v1.17: 81 actions (71 open) across
B1–B6, fourteen open and four closed decisions, every open finding F4–F55, the CLAUDE.md §10 gaps G1–G9 with
their Part 10 dates, the new G10–G17, and T-W. Closed items are kept and marked closed so the list shows what
moved; the portal does not print them. Owners of open items: COO 34, Managing Director 22, Contracts Manager 5,
Environmental Manager 4, H&S Officer 2, Accounts Manager 2, Quality Representative 2. **`portal/config.yaml`:
F39 CLOSED** — the trades line names mould and damp remediation (D11, remediation only), and the 30 Sep 2026
milestone now says it is *not* the date the system started working, with the go-live target (9 Oct) and the
Stage 1 target (31 Oct, D22) added as milestones. `build/build_portal.py` rebuilt: 31 pages, 81 actions, and
the generated pages carry *v1.17, 7 October 2026*, G10–G17 and the corrected milestone (checked by grep on
`site/`, which is gitignored).

**Not done, deliberately.** Nothing was committed: Claude does not run git against the clone (§7.7). The
workbook is not committed and must not be — it is regenerated. Nothing was sent to James Milligan; whether the
workbook goes to him, and marked how, is Gary's call (F45, F46). `Claude outputs/coto/` holds the render and
page PNGs; none is needed after Gary has looked at the PDF.

**Tasks by owner, from this session:**

| Owner | Task | By |
|---|---|---|
| **Gary** | ~~Commit this workstream as **two commits on one branch** (§7.8): (1) `registers/opportunities.yaml` + `build/export_coto.py` + `CLAUDE.md` §5 + `portal/actions.yaml` + `portal/config.yaml`; (2) register v1.17. Commands below. **Claude does not merge.**~~ **CLOSED: merged as PR #15 (`93dbe9f`), confirmed 7 Oct 2026 (§2m). The push failed repeatedly first — F57.** | ~~this week~~ Done |
| Gary | Read REG-08 v0.1 end to end and confirm, change or strike each proposed score, band, status and review date; set `confirmed_by_owner` as each owner confirms. The owners are Steve (6 rows), Gary (3), Craig (1). | 30 Nov 2026 |
| **Steve** | Confirm the band thresholds (pursue ≥ 15, evaluate 8–14, hold ≤ 7) on approval of REG-08, and the six rows he owns (OPP-01, 02, 04, 07, 08, 09). **Approval is a signature; nothing is signed yet.** | with IMS-04 |
| Gary | Decide whether the generated workbook goes to James Milligan and PJR, and marked how. If so, regenerate from a committed `main` first so the cover's commit is a real one. | after commit |
| Later chat (REG-06 v0.2) | Add *processes affected* to each REG-06 issue, against the IMS-00 ¶19 process list, so the Issues tab's empty column fills from the YAML (§2k). | Phase 1 |
| Later chat (REG-05 v0.3) | F55: correct the *43 requirements* count in the REG-05 notes and in this register's §2 row to 44. | next REG-05 change |
| **Steve** | Part 10 (h): hold and minute a management review — none since 10 January 2023. **Overdue against 30 Sep 2026.** | 31 Oct 2026 (*proposed*) |
| **Steve** | Part 10 (j): set measurable environmental and OH&S objectives with dates, and the plan to achieve all three sets. **Overdue against 30 Sep 2026.** | 31 Oct 2026 (*proposed*) |
| Gary (COO) | Part 10 (c): ~~draft IMS-05 Leadership with the integrated policy statement (§6 item 3)~~ **drafted 7 Oct 2026 as v0.1 (§2m)**; Steve signs after the FRM-08 consultation and IMS-04. | 31 Oct 2026 (*proposed*) |
| Gary (COO) | Part 10 (u): write the internal audit programme; the auditor is Steve's to appoint (D3). | 31 Oct 2026 |
| Health and Safety Officer | Part 10 (d): the 5.4 consultation and participation mechanism, with records of it operating with non-managerial workers — **the mechanism is drafted at IMS-05 Part 5 (§2m); the records are FRM-06 and FRM-08, and none exists.** First record: the workforce consultation on the draft policy statement. | 31 Oct 2026 |
| Contracts Manager | Part 10 (k): register of monitoring and measuring equipment with calibration status. | 30 Nov 2026 (*proposed*) |
| Contracts Manager | Part 10 (l): role-based competence requirements as a register in the repository (requirements only; individual records stay in Workspace). | 30 Nov 2026 (*proposed*) |
| Contracts Manager | Part 10 (q): approved supplier and subcontractor register of the Employer's own, from FRM-04 evaluations. **Overdue against 30 Sep 2026** (REG-05 IP-12). | 30 Nov 2026 (*proposed*) |
| Environmental Manager | Part 10 (s): environmental emergency or spill response test, recorded. | 31 Jan 2027 (*proposed*) |
| Quality Representative | Part 10 (t): customer satisfaction monitoring (9001 9.1.2). | 31 Dec 2026 |
| Gary | Re-run `python3 build/build_portal.py` after each register change; `portal/actions.yaml` now says v1.17 and goes stale from the next version. | each register change |
| Workstream 7 | When REG-01 is migrated, `export_coto.py` `tab_risk_pointer()` is replaced by a rows tab; the REG-01 ids on the Issues tab then resolve. | Phase 1 |

**Completion note.** The opportunity register exists as ten scored, owned, dated rows that trace one for one
to what REG-06 already said, with every score flagged as a proposal and no row claiming to be realised. The
export script writes a six-tab workbook that cannot drift from the registers because it is regenerated from
them, carries REG-01 as a pointer until it is migrated, and has no ISO 27001 tab. Validated, exported, counted
three ways and read as images. Nothing signed, committed, sent or merged. F53 closed by PR #14.

---

## 2m. Workstream 3 — `SESC-IMS-05` Leadership, draft v0.1, and `SESC-FRM-08`, 7 October 2026

**Taken:** workstream 3 only (§6 item 3; IMS-00 Part 10 (c) and (d); G6, G16). **Started once `main` was confirmed to
contain PR #15.** This chat ran in the claude.ai Project, not Cowork, so it could not see the MacBook clone; it read a
**fresh clone of `GaryHill0985/QMS` from GitHub** (read-only `git --no-optional-locks log`): `main` at **`93dbe9f`**
(*Merge pull request #15 from GaryHill0985/workstream-2b-reg08-coto*), parents `0c2ee40` (register v1.17) and `ee19a6b`
(REG-08, `export_coto.py`, CLAUDE.md §5, portal resync); `git ls-tree main` lists `registers/opportunities.yaml` and
`build/export_coto.py`; the clone's tree was clean. **The §2l commit task is therefore CLOSED by PR #15.** Whether the
MacBook working tree is clean apart from `Claude outputs/` is for Gary's own `git status` in Terminal (§7.7); this chat
could not check it. **The TeraBox restore was not reachable either** — see the provenance note below.

| Built | Where | Status |
|---|---|---|
| **`SESC-IMS-05` Leadership.** Reference taken from `CLAUDE.md` §5 in the same change. 53 numbered paragraphs in seven Parts plus two annexes. Part 2: how the Managing Director demonstrates leadership (5.1) and customer focus (9001 5.1.2), each present-tense statement pointing at a signed document or marked absent at Part 6. **Part 3: the integrated policy statement** (¶22–¶28), written to supersede Part 1 of POL-16 v1.2, POL-05 v1.1 and POL-08 v1.1 **on Steve's signature and not before** (¶3, ¶32, ¶52); ¶29 maps every commitment in the three signed Part 1s to where it is carried, ¶30 maps each clause 5.2 requirement to the paragraph that meets it; carries the CLI-00 climate determination (¶24) and an ethics and quality-culture statement (¶25); names no headcount, turnover or PI limit; asserts no record. Part 4 points to IMS-04 ¶11 and **does not claim 5.3**. **Part 5: the 45001 5.4 mechanism** (below). Part 6: 13 absent records, each dated, (a)–(m). Part 7: approval block, **empty**. | `system/5-leadership.md` | **Draft v0.1** |
| **Clause map claimed:** 9001 5.1.1, 5.1.2, 5.2.1, 5.2.2 · 14001 5.1, 5.2 (**unverified** edition) · 45001 5.1, 5.2, **5.4 as the documented mechanism, with the clause note that records of it operating are not yet held** (Annex A). Not 5.3 (IMS-04 ¶11 is the statement), not 6.2 (the policy is the framework for objectives, not the objectives), not 7.4. | front matter | — |
| **`SESC-FRM-08` Worker Consultation Record.** Taken because FRM-06 cannot: record system-level consultation (policy, objectives, audit programme, roles, procurement controls — no job, no site); track an item to an answer across weeks or record that feedback was given; tag which clause 5.4 matter an item serves; or record participation in a RAMS review, an incident investigation or PPE selection (IMS-05 ¶44). 20 fields, one entry per event or per answer, `answers_item` closes an earlier item by reference, append-only (D15), `representative` left blank until D26. Claims 45001 5.4 only, with a clause note that **no completed record exists**. Picked up by `export_forms.py` (its glob); one `file` field needs adding by hand, like FRM-06/07. | `forms/SESC-FRM-08-worker-consultation-record.yaml` | **Draft v0.1** |
| `CLAUDE.md` §5: IMS-05 and FRM-08 recorded as taken on 7 Oct 2026; next free `SESC-IMS-06`, `SESC-FRM-09`. `build/workspace_forms/README.md`: FRM-08 row. `portal/actions.yaml`: G6 and G16 detail updated (status stays **open** — the mechanism is drafted, not operating; the statement is unsigned). Portal rebuilt: 31 pages, 16 controlled files, 81 actions. | `CLAUDE.md`, `build/workspace_forms/`, `portal/` | Done |
| **`build/test_render_docx.py`: `TestIMS05`**, three tests — DOCX labels = source, printed PDF labels = source, cover note *CLAUSE 5*. | `build/` | **25/25 pass** in the container (LibreOffice + pdftotext present) |

**The 5.4 mechanism, as designed (IMS-05 Part 5).** Direct consultation of **all** non-managerial workers — every
directly employed operative, **each of the four apprentices individually**, and subcontractors' operatives on the job
they are on — in paid time. Five parts, each with a named record (¶38): (a) the weekly site toolbox talk with "what did
you see / what worries you / what would you change" asked of everyone by name, on **FRM-06**; (b) the H&S Officer's
weekly review carrying every unanswered item to **FRM-08** with owner and due date within five working days; (c) the
**quarterly consultation meeting** of the whole non-managerial workforce with the Managing Director present, on the
matters 45001 names (policy, objectives, monitoring, audit, roles, procurement controls, improvement), on FRM-08;
(d) the monthly report of open items to the Managing Director alongside the corrective action log; (e) event-driven
participation in RAMS reviews, incident investigations, PPE selection and competence decisions, recorded on FRM-08.
Every item is answered within ten working days or told when, fed back in person at the next talk, and closed only by an
answer (¶40). Six barriers named and addressed (¶43), the apprentices explicitly (¶43(d)). Measures at ¶42, none yet
taken. **No workers' representative has been elected or appointed and none is assumed: offering one is D26, Steve's.**
**The first intended FRM-08 record is the consultation of the workforce on the draft policy statement itself, before
Steve signs it, due 31 Oct 2026**; the first FRM-06 record is the first live toolbox talk after go-live. **Neither
exists. The mechanism is designed, not operating, and the document says so (¶35, ¶46, Part 6 (b), (d), (e), (f)).**

**Provenance of the three signed statements, recorded honestly.** CLAUDE.md §11 (as it then stood) put the signed PDFs in
the TeraBox restore, which this chat could not reach; from §2n they are at `~/Documents/SESC/ISO/Signed/`. The three were read from the Employer's **Google Drive**
"(signed)" copies uploaded 18 Aug 2026 — POL-16 v1.2 (21 pages, 731,315 bytes), POL-05 v1.1 (32 pages, 812,667 bytes),
POL-08 v1.1 (23 pages, 708,485 bytes) — **every page, text layer, on 7 Oct 2026**. The byte sizes equal those of the
signed set on the Drive dated 17 Aug 2026. **Gary to confirm by SHA-256 that they are the same files as the `Signed/` copies**
before IMS-05 ¶20 and ¶49(a) are relied on (task below; hashes at §2n). The Drive copies were read only; nothing on the Drive was
moved, renamed or written.

**Verification.**

1. `build/validate.py`: **0 errors**, 13 warnings (the expected 14001 `verified: false`, now including
   `system/5-leadership.md`), 5 notes (one new: IMS-05 cites 45001 5.4, flagged CRITICAL). BUILD PASSES. **16 controlled
   files.** A first run failed on a YAML quoting error in FRM-08's `guidance` list; fixed.
2. `python3 build/workspace_forms/export_forms.py`: eight forms, FRM-08 reported with its `file` field to add by hand.
3. Rendered with `build/render_docx.py --pdf` to `Claude outputs/ims05/SESC-IMS-05-v0.1-DRAFT.docx` and `.pdf`:
   **19 pages**. **All 81 source labels (53 paragraph numbers, 28 sub-labels) print in order**, checked from the DOCX
   and from the PDF text layer against the Markdown (81 = 81 = 81; sequential 1–53).
4. **Read as images:** the cover (p1: MANAGEMENT SYSTEM · *CLAUSE 5 // ISO 9001 · ISO 14001 · ISO 45001* · *Leadership*;
   fields *0.1 — DRAFT, NOT ISSUED* · *7 October 2026* · *G A Hill (drafted by Claude)* · *Not yet approved (Managing
   Director)*), the policy statement page (p7, ¶23(e)–(k), ¶24–¶26, header *DRAFT — NOT ISSUED*), the ¶38 mechanism
   table (p13, rows (c) and (d)), the Part 6 table and approval block (p18: **Reviewed by, all three Dates and Signature
   empty**), and Annex A and B (p19).
5. `python3 -m unittest build.test_render_docx`: **25/25 pass**, including the three new IMS-05 tests.
6. **The first render was refused** — `SignatureError: the source carries content in a signature row` — because the
   ¶29 table's header cell read *Signed statement* and `SIG_LABELS` matches any first cell beginning "signed", header
   rows included. Header renamed *Statement*; the guard's false positive is **F58**.
7. **Cosmetic, not fixed:** the six-column ¶38 table gets equal column widths, so the *What* column runs to three pages
   of narrow text. **F54 applies** (`_widths()` on six-column tables). Readable; recorded, not shortened.

**Not done, deliberately.** Nothing was committed, pushed, merged or signed. Nothing was applied to POL-16, POL-05
or POL-08 — they are superseded only by Steve's signature on IMS-05, and amended at their next revision after it
(¶32). IMS-00 Annex B and Part 10 were **not** edited: Annex B moves its 5.1/5.2/5.4 rows to the spine only when IMS-05
is issued (IMS-00 `review_trigger`), and Part 10 (c)/(d) go to v0.2 with it. **This chat's files exist in a sandbox,
not on the MacBook:** Gary applies the patch below into the clone, then commits.

**Tasks by owner, from this session:**

| Owner | Task | By |
|---|---|---|
| **Gary** | Apply `Claude outputs/workstream-3.patch` to a new branch from an up-to-date `main` (commands below), check `git status` shows exactly the seven files, then commit as **two commits on one branch** (§7.8): (1) `system/5-leadership.md` + `forms/SESC-FRM-08…yaml` + `CLAUDE.md` + `build/test_render_docx.py` + `build/workspace_forms/README.md` + `portal/actions.yaml`; (2) register v1.18. Open the PR. **Claude does not merge.** | this week |
| Gary | Confirm that the Drive "(signed)" PDFs read for IMS-05 are the signed originals, now copied to `~/Documents/SESC/ISO/Signed/` (F59): run the `shasum -a 256` check in §2n against the hashes recorded there. If any differs, re-read the `Signed/` copy against IMS-05 ¶29 before the PR merges. | before merge |
| Gary | Re-render on the MacBook (`python3 build/render_docx.py system/5-leadership.md --pdf --out "Claude outputs/ims05"`), run the tests, and read the 19-page PDF end to end before it goes to anyone. | before sending |
| Gary | Send IMS-05 v0.1 to James Milligan **as a DRAFT**, with IMS-00 and IMS-04, for his view on whether Part 5 would satisfy 45001 5.4 at Stage 1. Record his comments here; changes go in as v0.2 by PR. | after commit |
| Gary | Run the Workspace build (README §2–§7) — now eight forms. FRM-08 is a domain-sign-in form; set `CONFIG` accordingly (D19). B3 clock. | this week |
| **Steve** | **D26: decide whether to offer the workforce an elected representative of employee safety.** Direct consultation stands until he does. | 31 Oct 2026 (*proposed*) |
| **Steve** | Read the integrated policy statement (IMS-05 ¶22–¶28). **Do not sign before (i) the workforce consultation on it is recorded on FRM-08 and (ii) IMS-04 v0.3 is signed.** His signature supersedes the three signed statements. | 31 Oct 2026 (*proposed*) |
| **Health and Safety Officer** | Run the first quarterly consultation meeting — the whole non-managerial workforce, the four apprentices by name, Steve present — on the draft policy statement; record it on FRM-08 (first record of the mechanism). | 31 Oct 2026 |
| Health and Safety Officer | First live toolbox talk on FRM-06 with the "what the team raised" question asked and answered; then weekly on every active site; weekly FRM-08 review from the first talk. | from go-live; first by 31 Oct 2026 |
| Health and Safety Officer | First monthly report of open consultation items to Steve (IMS-05 ¶38(d)). | month ending 30 Nov 2026 |
| Later chat (POL-16 v1.3, POL-05 v1.2, POL-08 v1.2) | After Steve signs IMS-05: replace each Part 1 with a pointer to IMS-05 ¶22–¶28 and name mould and damp remediation (D11); amend in place by PR; Steve signs. | 30 days after signature |
| Later chat (IMS-00 v0.2) | Move Annex B rows 5.1, 5.2, 5.4 to IMS-05 and update Part 10 (c), (d) — **only when IMS-05 is issued**. | on issue of IMS-05 |
| Later chat | F58: make `SIG_LABELS` skip header rows (row 0 of a non-label table) in `render_docx.py`, with a test. | with the next renderer change |
| Later chat | F54: `_widths()` minimum width for the first text column of six-column tables (IMS-00 ¶19, IMS-05 ¶38). | with the next renderer change |

**Completion note.** The Employer's three policy statements, read end to end, now have one successor that carries
every commitment they make, adds climate and culture, and asserts nothing no record supports — and it takes effect
only when Steve signs. Clause 5.4, until today a sentence in POL-05, has a mechanism a firm this size can run weekly,
with two forms behind it and the apprentices named as the people to ask first; its first record is to be the
workforce's own say on the policy. Validated, rendered, every number checked, four pages read as images, 25 tests
green. Nothing signed, committed, sent or merged; the §2l commit task closed by PR #15; one new decision (D26) and two
new findings (F57, F58).

---

## 2n. The project's sources reduced to three, 7 October 2026 (same chat as §2m, at Gary's direction)

**Trigger.** Gary: every new chat was being sent to the TeraBox restore and reconciling four or five locations. **His
decision, 7 Oct 2026: three sources only** — `~/Documents/SESC/ISO/` on the MacBook (the clone and its reference
material), GitHub `GaryHill0985/QMS`, and the Google Drive for the Workspace record capture only. The shared ISO folder
on the Drive is not to be used unless he asks in the chat. Everything else — TeraBox, the TeraBox restore, Dropbox, the
MSI — is removed from the project's instructions.

**What was found.** `find ~/Documents/SESC/ISO -maxdepth 3` (Gary, 7 Oct 2026) returned **only `CLAUDE ISO/`**. None of
the material `CLAUDE.md` §11 depends on — standards, signed policies, BRAND-SPEC, Architecture Plan, insurance records —
was in the ISO folder. It was all in the TeraBox restore, which also holds **a stale, `.git`-less copy of this
repository** at `TeraBox Restore/SESC/SESC/ISO/CLAUDE ISO/`, the POW, ITC and Pow Property trees (§7.2-forbidden
references), and the whole JOSCAR working estate. That mix is why chats kept being sent there. Gary's listing of the four
relevant folders was read in full and the copy list was drawn from it, file by file.

**What changes.**

| Change | Where | Status |
|---|---|---|
| **`copy-iso-reference.zsh`** copies, never moves, into `~/Documents/SESC/ISO/`: `Reference/Standards/` (BS 99001 PDF and text, CIOB Code, ISO 45001:2018, ISO 14001:2015, ISO 9001:2015); `Reference/CertiKit/` (six demo files and the 27001 v13-1 folder); `Reference/Architecture/` (the Plan); `Reference/Design/` (BRAND-SPEC, INTERIOR-SPEC, master logo); `Reference/Decisions/` (the consistency findings and completion note, the C2–C8 decisions, Section workflow method, signature verification, the PI, accident book and guarantees/training findings, and `JOSCAR Master Register.md`); `Signed/` (the 21 signed PDFs, flattened); `Insurance/` (all nine). `cp -n` never overwrites; every file is checked with `cmp`, the 27001 folder with `diff -rq`; it prints copied / differ / missing counts and the signed count (expect 21). Tested against a mock tree and run twice: idempotent. **Not copied, deliberately:** `PROJECT-INSTRUCTIONS.md`, `README (1).md` and `SESC Document Design Spec.md` (old instruction files — the cause of this finding), `sesc_cover.py` (already ported), the JOSCAR-only reference notes, the Armed Forces Covenant files, the stale `CLAUDE ISO` copy, `CLAUDE CODE OUTPUT`, `_Claude Project setup`, and everything POW, ITC and Pow Property. | Gary runs it | **Not yet run** |
| **`CLAUDE.md` §2, §9.4 and §11 rewritten** to the three sources: §2 reads `~/Documents/SESC/ISO/` and forbids any other source by name; §9.4 points the traps at `Reference/Decisions/` and records the fifth; §11 states the three sources, the Project-copy rule (the MacBook copy governs), and a location table under `~/Documents/SESC/ISO/`. **The "reusable structure from prior builds" row (POW, Pow Property, ITC) is removed**: none is a source any more, and §3 already forbids their content. A separate commit from workstream 3 (§7.8). | `CLAUDE.md` | Drafted |
| **Claude Project** — section 3 of the instructions replaced (text given to Gary in this chat); `SESC-Business-System-Project-Handover-v1.0.md` removed from Project knowledge as superseded; the standards, CIOB Code, BRAND-SPEC, INTERIOR-SPEC, Architecture Plan and the 17 August decision records kept as read-only copies. `Section workflow method.md` kept only if it will not be edited. | claude.ai Project settings | **Gary** |

**The other folder under `~/Documents/SESC/`.** Gary's listing of `~/Documents/SESC` (7 Oct 2026) shows one folder beside
`ISO/`: `SESC Solutions Limited/`, the twenty numbered folders plus `To be Allocated` — the local copy of James Milligan's
Dropbox template set read at §2h. **It is not a source.** `CLAUDE.md` §2 and §11 name it, so that no chat treats a folder
one level from the clone as part of the system. The §2h tasks that read it as structure (legal register, procedure layout)
stand, but are done only when Gary asks in the chat.

**Left as written, deliberately.** The historical sections of this register (§2 to §2m) record the TeraBox paths as
they were at the time; they are history and are not rewritten (amend, never regenerate). The `standards/*.yaml`
provenance notes ("read from … held at `Desktop\SESC\ISO\`") and `build/render_docx.py`'s note that it was ported from
files in the TeraBox restore say where something came from, and stay. `portal/actions.yaml` D10 (the untracked planning
files, which exist only in the restore) stays open as it was.

**The three signed statements read for IMS-05, by SHA-256** (Drive "(signed)" copies, downloaded 7 Oct 2026). After the
copy, run `shasum -a 256 ~/Documents/SESC/ISO/Signed/SESC-POL-0[58]*.pdf ~/Documents/SESC/ISO/Signed/SESC-POL-16*.pdf`
and compare:

| Document | Bytes | SHA-256 |
|---|---|---|
| SESC-POL-05 v1.1 | 812,667 | `5fcf4ef7f18d26d0b914b6ed81f3c9e66ad379e2dda9d593fe0ccab8e025bc95` |
| SESC-POL-08 v1.1 | 708,485 | `6bd7b16142213bd29f295d1bd907435907c776662442d6daf7cca2347c7d85e0` |
| SESC-POL-16 v1.2 | 731,315 | `19d14aae3cf82dfb8442212630d97bf7190d51029d973372a3c17e1b797786de` |

**Tasks by owner, from this section:**

| Owner | Task | By |
|---|---|---|
| **Gary** | Run `copy-iso-reference.zsh` **before** applying the patches; expect `0 differ`, `0 missing`, signed count 21. Any `MISSING` or `DIFFERS` line: stop and bring it to the next chat. | before the commit |
| Gary | Run the SHA-256 check above. | before merge |
| Gary | Replace section 3 of the Claude Project instructions and remove the Handover file from Project knowledge. | now |
| Gary | Decide, separately, whether the TeraBox restore stays on the Mac. Nothing in the project depends on it once the copy is verified. **Its copy of `CLAUDE ISO` must never be opened as if it were the repository.** | your call |
| Later chat | Bring REG-02, REG-03, REG-04, REC-01…04 and TPL-01…04 into `Signed/` when a workstream needs them; they were not in `Branded/Signed/`. | when needed |

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
| **D21** | **The CMS Manual: its reference, and how it relates to SESC-IMS-04…10** | **Gary** | **NEW 6 Oct 2026.** James asks for the CMS Manual first. SESC already has IMS-04 (clause 4) and the `SESC-IMS-nn` spine for clauses 4–10. Options: (a) one **Integrated Management System Manual** as the top document, citing IMS-04…10 and the policies rather than repeating them; (b) the manual **is** the spine, IMS-04…10 as its chapters. Either way it is written in house style from SESC's facts; James's template is a heading checklist only (§7.2, F41). **Decide before drafting, and take the reference from §5 in the same turn.**<br><br>**CLOSED 6 Oct 2026 — Gary's decision: option (a), one Integrated Management System Manual on top.** It walks clauses 4–10 in the order of James's template headings, says briefly how the Employer meets each, and points to IMS-04, the policies, registers and forms rather than repeating them. Where something does not exist yet, the manual says so with a date (records held, records not yet held). **Reference proposed: `SESC-IMS-00`** (the spine's overview, ahead of the clause chapters 04–10). That extends the `SESC-IMS-nn` rule in `CLAUDE.md` §5, so confirm it at the start of the drafting chat and add the line to §5 by PR in the same change. Drafting is the next workstream, in its own chat.<br><br>**6 Oct 2026, drafting chat: reference `SESC-IMS-00` CONFIRMED by Gary's instruction and TAKEN.** `CLAUDE.md` §5 amended in the same change. **Drafted as v0.1 — see §2j.** Claims clauses 4.4 and 7.5.1 only. With Gary to commit and send to James for review; Steve's signature follows IMS-04's. |
| **D22** | **Stage 1 by end of October 2026** | **Steve** | **NEW 6 Oct 2026, agreed at the meeting (Gary).** Replaces Phase 4's Stage 1 window. Stage 2 still waits on records (§1.1). §2i.2, F50. |
| **D24** | **The COTO Log: SESC's version is REG-01 + REG-05 + REG-06, plus a new opportunity register and a generated workbook view** | **Gary** | **NEW, CLOSED 6 Oct 2026 — Gary's decision (§2k).** No COTO log is built from the template. SESC's context data stays as YAML registers in the repository (one master). Two additions: **`SESC-REG-08` Opportunity Register** (scored, with pursuit plan, owner and status, separate from risks — 9001:2026-ready), and **a generated read-only workbook** in the template's tab layout for James and the certification body, written by a build script from the registers so it can never drift from them. Workstream 2b, next chat. Risks 27001 tab not carried (D1).<br><br>**7 Oct 2026, workstream 2b: BUILT — see §2l.** `SESC-REG-08` taken and drafted as v0.1 (ten rows, all from REG-06, scores proposed); `build/export_coto.py` writes the workbook with REG-01 as a pointer. With Gary to commit; Steve confirms the bands and his six rows on approval. |
| **D25** | **The H&S Policy Manual: SESC-POL-05 is SESC's version; no new manual** | **Gary** | **NEW, CLOSED 6 Oct 2026 — Gary's decision (§2k).** James is sent the signed POL-05 v1.1 with the comparison note. Four candidate gaps (housekeeping, DSE, young persons, electricity at work) and two to-confirms go to **POL-05 v1.2 after a full read of all 32 pages** — they are candidates, not findings, until then. Any change is an amendment in place by PR, signed by Steve. |
| **D26** | **An elected representative of employee safety?** | **Steve** | **NEW 7 Oct 2026 (§2m).** No workers' representative has been elected or appointed. IMS-05 Part 5 designs clause 5.4 as **direct consultation of all non-managerial workers**, which the Health and Safety (Consultation with Employees) Regulations 1996 allow, and which is POL-05 O7 ¶15's position today. ISO 45001 5.2 and 5.4 refer to workers' representatives *where they exist*. Options: (a) stay with direct consultation; (b) invite the workforce to elect a representative of employee safety under the 1996 Regulations, who then attends the monthly review and is named on FRM-08, with direct consultation of everyone continuing alongside. **Not assumed either way; IMS-05 is reviewed on the decision (its `review_trigger`).** |
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
| F39 | **`portal/config.yaml` is stale against this register.** Its `trades` line omits mould and damp remediation (D11). Its milestone for 30 Sep 2026 says *"The date to quote when asked when the management system started working"*. That contradicts B3, and IMS-04 ¶39 was corrected for the same statement in v0.3 (F33). The portal publishes it, including to the auditor build.<br><br>**Closed 7 Oct 2026 (§2l.1):** trades line and milestone corrected; `portal/actions.yaml` resynced from v1.4 to v1.17 in the same change. | **Medium** | **Closed (§2l.1)** |
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
| **F52** | **The renderer labelled `SESC-IMS-00` as "Clause 0".** `header_right()` and `cover_note()` derived the label from the two-digit suffix with no case for the manual. Found before the first render by reading the code; fixed and tested in the same change (§2j). | Low | **Closed (§2j)** |
| **F53** | **The clone's `register-v1.14` branch carried an uncommitted, modified register when this session began**, newer than the committed `48ddbba` (FS-13, FS-14, F51 are in the working tree only). Not a drift between two copies, but §7.7 says record it: if the working tree were lost, those additions would go with it. This session built on the working-tree copy.<br><br>**Closed 7 Oct 2026:** the additions are in `a4ab77f`, merged to `main` by PR #14 (`965535b`). | Medium | **Closed (PR #14)** |
| **F54** | **Six-column tables wrap single words in narrow columns** — *Manage-ment* in IMS-00 ¶19, *CLAUS-E* in the Annex B header. Cosmetic; a `_widths()` minimum-width rule would fix it. Do not shorten the words to suit the renderer. | Low | Later chat |
| **F55** | **`SESC-REG-05` v0.2 holds 44 requirements, not 43.** This register's §2 row and the REG-05 file both say 43; the F16 restoration added the first-aid needs assessment requirement at IP-06 and the count was not updated. Found by `export_coto.py --check` on 7 Oct 2026. Correct at REG-05 v0.3. | Low | Later chat |
| **F56** | **A file written through the device bridge did not change, and reported that it had.** On 7 Oct 2026 a corrected `build/export_coto.py` was written over the first version; the bridge reported *written*, but the file on disk kept the old content (confirmed by `md5sum` and `grep`). Writing the file under a new staged name landed it. §7.7 applies in a new form: **after any write through the bridge, check the file on disk, not the tool's reply.** | Low | Recorded; rule at §7.9 |
| **F57** | **The push of branch `workstream-2b-reg08-coto` (PR #15) failed repeatedly with GitHub "Internal Server Error"**, reported by Gary on 7 Oct 2026. An empty test commit failed the same way; the push then succeeded, unchanged, on a later retry. **Transient; no cause established.** Rule: on a GitHub 500, retry before diagnosing the clone, the key or the ruleset. | Low | Recorded |
| **F58** | **`render_docx.py`'s signature guard fires on a table HEADER whose first cell begins "signed".** `SIG_LABELS = ("signature", "signed")` is matched against row 0 of a non-label table too, so IMS-05's ¶29 header *Signed statement* was refused as a filled signature row on a draft. Worked round by renaming the header; the guard should skip header rows. | Low | Later chat, with a test |
| **F59** | **The reference material the project's rules depend on was not in `~/Documents/SESC/ISO/`.** The folder held only the clone; the standards, signed policies, BRAND-SPEC, the Architecture Plan and the insurance records were all in the TeraBox restore, beside a stale `.git`-less copy of the repository and the POW/ITC trees. `CLAUDE.md` §11 pointed every chat into that mix, which is why each new chat was sent back to TeraBox. **Fixed in §2n:** copy-and-verify into `~/Documents/SESC/ISO/`, and §2, §9.4 and §11 rewritten to three sources. Closes when the copy has run clean and the PR is merged. | Medium | Gary |
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
| **2a** | **DONE 6 Oct 2026 (§2j) — `SESC-IMS-00` Integrated Management System Manual, draft v0.1** (D21). With Gary to commit; to James for review; Steve signs after IMS-04. | James asked for the manual first (§2i); it is also what a Stage 1 assessor opens first. | Done |
| **2b** | **DONE 7 Oct 2026 (§2l) — `SESC-REG-08` Opportunity Register, draft v0.1, and `build/export_coto.py`**, the generated *SESC COTO Log* workbook from REG-05, REG-06, REG-08 (REG-01 as a pointer until migrated). With Gary to commit; Steve confirms bands and rows on approval. | James and PJR will expect a COTO log to look like a workbook; the registers already hold the content. Separating opportunities from risks is 9001:2026-ready. | 1 session |
| 3 | **DRAFTED 7 Oct 2026 (§2m) — `SESC-IMS-05` Leadership, draft v0.1**, with the integrated policy statement (supersedes the three signed statements **on Steve's signature only**) and the 45001 5.4 mechanism, with new `SESC-FRM-08`. With Gary to commit; the workforce consultation on the statement (FRM-08) and D26 before Steve signs, after IMS-04. | 5.4 is the clause 45001 auditors test hardest; it now has a mechanism and no records. | Done, awaiting records and Steve |
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
9. **After writing a file through the device bridge, check the file on disk** — `md5sum` or `grep`
   for the change — not the tool's reply. On 7 October 2026 the bridge reported a write that did not
   land (F56).

---

## 8. Revision history

| Version | Date | Author | Change |
|---|---|---|---|
| 1.18 | 7 October 2026 | Claude, for G A Hill | **Also §2n (same chat, at Gary's direction): the project's sources reduced to three — `~/Documents/SESC/ISO/`, GitHub `QMS`, and the Drive for record capture only. The reference material was found NOT to be in `~/Documents/SESC/ISO/` (only the clone was); a copy-and-verify script brings it across from the TeraBox restore (`Reference/`, `Signed/`, `Insurance/`), and `CLAUDE.md` §2, §9.4 and §11 are rewritten to the new layout as a separate commit. New F59. The POW/ITC 'reusable structure' row is removed from §11.** **Workstream 3: `SESC-IMS-05` Leadership, draft v0.1, and `SESC-FRM-08` Worker Consultation Record, draft v0.1.** New §2m. IMS-05 and FRM-08 taken from `CLAUDE.md` §5 (next free IMS-06, FRM-09). The integrated policy statement carries every commitment of POL-16, POL-05 and POL-08 Part 1 (all three read in full, from the Drive signed copies — TeraBox not reachable), CLI-00 and an ethics/culture statement, and supersedes nothing until Steve signs. The 5.4 mechanism: direct consultation of all non-managerial workers including the four apprentices, five parts, FRM-06 + FRM-08, no record yet; the elected-representative question is **new D26** (Steve). Claims 5.1, 5.2, 5.4; not 5.3, not 6.2. Validated (0 errors, 16 files), rendered to 19 pages, all 81 labels checked, four pages read as images, 25/25 tests. **PR #15 (`93dbe9f`) confirmed merged; the §2l commit task closed. New F57** (transient GitHub 500 on push) **and F58** (signature guard matches a table header). G6, G16, §6 row 3 and the Part 10 (c)/(d) task rows updated; IMS-00 untouched. **Nothing signed, committed, sent or merged.** |
| 1.17 | 7 October 2026 | Claude, for G A Hill | **Workstream 2b (D24): `SESC-REG-08` Opportunity Register, draft v0.1, and `build/export_coto.py`.** New §2l. REG-08 reference taken from `CLAUDE.md` §5 (next free register now REG-09). Ten rows seeded one for one from REG-06's opportunity fields, scored 1–5 × 1–5, every score and plan marked proposed; claims 6.1.1 only. `export_coto.py` writes the six-tab *SESC COTO Log* workbook (REG-01 as pointer, no 27001 tab) to the gitignored `out/`; validated (0 errors), exported, counted three ways (44 / 30 / 10) and read as images. **F53 closed by PR #14 (`965535b`).** New F55 (REG-05 holds 44 requirements, not 43) and F56 (a bridge write that did not land); new rule §7.9. D24 and §6 row 2b updated. **Task 5 (§2l.1): IMS-00 Part 10 (a)–(w) reconciled — ten items had no owner task in whole or in part and are added (c, d, h, j, k, l, q, s, t, u); `portal/actions.yaml` resynced from v1.4 to v1.17 (81 actions, new G10–G17); `portal/config.yaml` corrected and F39 closed; portal rebuilt.** **Nothing signed, committed, sent or merged.** |
| 1.16 | 6 October 2026 | Claude, for G A Hill | **Review of James Milligan's H&S Policy Manual and COTO Log templates** (§2k, same chat as §2j, analysis only). Both found to duplicate documents SESC already holds. **New D24** (COTO: registers stay the master; add REG-08 Opportunity Register and a generated workbook view — workstream 2b) and **D25** (POL-05 is SESC's H&S manual; four candidate gaps to v1.2 after a full read). Comparison note for James written to `Claude outputs/`. §6 row 2b added. **Nothing built, uploaded, signed, committed or merged.** |
| 1.15 | 6 October 2026 | Claude, for G A Hill | **Workstream: `SESC-IMS-00` IMS Manual, draft v0.1** (D21 confirmed and taken). New §2j. `system/0-manual.md`: 68 paragraphs, clauses 4–10 in the template's heading order, pointers only, Part 10 inventory of 23 absent records (a)–(w), Annex B document map. Claims 4.4 and 7.5.1 only. Renderer `IMS-00` labels fixed with two new tests (F52 closed); 22/22 pass. `CLAUDE.md` §5 names IMS-00. Validated (0 errors), rendered to 20 pages, all 68 numbers checked, six pages read as images, approval block empty. New F53 (uncommitted register in the working tree at start) and F54 (six-column table wraps). §6 row 2a added. **Nothing signed, committed, uploaded or merged.** |
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
