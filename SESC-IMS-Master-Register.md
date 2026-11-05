# SESC-IMS-Master-Register

**The state of the CLAUDE ISO project. v1.37 · 5 November 2026.**

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
| **Repository** | **`github.com/GaryHill0985/QMS`**, pushed 18 August 2026, commit `d3782f7`. The working clone was `Desktop\SESC\ISO\CLAUDE ISO\` on the MSI; **from 24 September 2026 it is `~/Documents/SESC/ISO/CLAUDE ISO/` on the MacBook** — see §2d. **From 4 November 2026 Gary works from the Windows PC clone at `C:\Users\Admin\Desktop\QMS`, with its own signing key from 5 November 2026 (§2t, D4); **from 5 November 2026 the PC clone is the master and the MacBook clone is retired (F84 closed, §2w).** PR #20, the fire door record pack, merged as `fc225da` on 5 November 2026 (§2t.5).** **PR #24, the F84 change (register v1.30 and `CLAUDE.md` §2, §9 and §11), merged as `b3f4894` on 5 November 2026 (§2w.7).** **PR #26, register v1.31 to v1.35 — §2x, the HANDOFF-FD-002 brief, the Platform clones and F86 to F88 — merged as `21d3ef3` on 5 November 2026 (§2x.7).** **PR #27, register v1.36 (§2x.7), merged as `4e9bb15` on 5 November 2026 (§2y); the clone's `main` is at `4e9bb15`.** **D4 CLOSED.** |
| **Master document count** | 22 signed (POL-01…20, CRP-01, REG-01 — **POL-20 Anti-Bribery and Corruption Policy v1.0 added 27 Oct 2026, §2s, with its dates in question at F77**) + REG-02, REG-03, REG-04 + REC-01…04 + TPL-01…04. |
| **This repository holds** | 3 controlled source files, 134 clauses across 3 standards, CI passing. **From 24 Sep 2026: a branded renderer, `build/render_docx.py`, with its tests (§2g).** **From 6 Oct 2026: `SESC-IMS-00` IMS Manual, draft v0.1 (§2j).** **From 7 Oct 2026: `SESC-REG-08` Opportunity Register, draft v0.1, and `build/export_coto.py`, the generated COTO Log workbook (§2l).** **From 7 Oct 2026, workstream 3: `SESC-IMS-05` Leadership, draft v0.1, with the integrated policy statement and the 45001 5.4 mechanism, and `SESC-FRM-08` Worker Consultation Record, draft v0.1 (§2m).** **From 7 Oct 2026 the project has three sources only: `~/Documents/SESC/ISO/`, GitHub `QMS`, and the Drive for record capture (§2n, `CLAUDE.md` §11).** **From 12 Oct 2026, workstream 5: `SESC-REG-09` Compliance Obligations Register, draft v0.1 — 79 obligations, every instrument read on its issuing body, with a documented evaluation method and no evaluation yet carried out (§2o).** **From 22 Oct 2026: REG-09 v0.2 and `SESC-REC-05`, the first record in `portal/records-index.yaml` since 17 August — the waste carrier public-register check (§2p).** **From 26 Oct 2026, workstreams 6, 4 and the clause 6 chapter in one chat (§2q): `SESC-PRO-01` Control of Documented Information, `SESC-PRO-02` Internal Audit with the first-cycle programme, `SESC-PRO-03` Management Review, `SESC-PRO-04` Nonconformity and Corrective Action, `SESC-REG-10` Environmental Aspects and Impacts Register (28 aspects, scores proposed) and `SESC-IMS-06` Planning with nineteen proposed objectives — all draft v0.1, under decision D27 that the EMS documents are drafted without waiting for ISO 14001:2026 to be bought.** **From 26 October 2026, Batch B first session (§2r): `SESC-PRO-05` Purchasing and Control of Suppliers and Subcontractors, `SESC-PRO-06` Training, Competence and Awareness, `SESC-PRO-07` Incident, Near Miss and Hazard Reporting and Investigation, `SESC-REG-11` Approved Supplier and Contractor Register (issued empty — one register in place of the four lists six signed policies describe) and `SESC-REG-12` Competence Requirements Register (44 requirements by role, no interval stated from memory) — all draft v0.1. 28 controlled files, 0 errors.** **From 4 November 2026 (§2t), the fire door record pack under decision D28, which reverses the fire door half of D11: `SESC-PRO-08` Fire Door Installation, `SESC-FRM-09` to `SESC-FRM-14`, `SESC-REG-13` Fire Door Asset and Install Register (issued empty), `SESC-WI-02`, `SESC-TPL-05`, `SESC-IMS-04` v0.4 and `SESC-REG-12` v0.2 — all draft; `build/render_form.py` and `build/export_fire_door_register.py`; the renderer, the portal builder and the tests made to run on Windows, which is the working machine from 4 November 2026 (F84). 38 controlled files, 0 errors; 25/25 renderer tests; every new document rendered to PDF and read as images.** **From 5 November 2026 (§2u): the renderer's signature guard fixed (F58 and F82 closed) and `SESC-PRO-06` rendered and read as images for the first time; 28/28 renderer tests. New F85: the fourteen numbered-paragraph tables in the seven §2q/§2r procedures print without their header row.** **From 5 November 2026 (§2v): F85 fixed in the renderer's parser — the fourteen numbered-paragraph tables in `SESC-PRO-01` to `SESC-PRO-07` render with their header rows; `SESC-PRO-06` and `SESC-PRO-01` rendered to PDF and read as images; 29/29 renderer tests. PR #22 merged.** |

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
| (g) compliance obligations register | §6 item 5, G5 | — **12 Oct 2026: register drafted as REG-09 (§2o); G5 detail updated in `portal/actions.yaml`, status open until the first evaluation record exists (30 Nov 2026, Environmental Manager)** |
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
| **Gary** | ~~Apply `Claude outputs/workstream-3.patch` to a new branch from an up-to-date `main` (commands below), check `git status` shows exactly the seven files, then commit as **two commits on one branch** (§7.8): (1) `system/5-leadership.md` + `forms/SESC-FRM-08…yaml` + `CLAUDE.md` + `build/test_render_docx.py` + `build/workspace_forms/README.md` + `portal/actions.yaml`; (2) register v1.18. Open the PR. **Claude does not merge.**~~ **CLOSED: merged as PR #16 (`cd98fdd`), confirmed 12 Oct 2026 (§2n.1). Workstream 3 is committed.** | ~~this week~~ Done |
| Gary | ~~Confirm that the Drive "(signed)" PDFs read for IMS-05 are the signed originals, now copied to `~/Documents/SESC/ISO/Signed/` (F59): run the `shasum -a 256` check in §2n against the hashes recorded there. If any differs, re-read the `Signed/` copy against IMS-05 ¶29 before the PR merges.~~ **CLOSED 7 Oct 2026: all three hashes match (§2n.1).** | ~~before merge~~ Done |
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
| ~~Later chat~~ | ~~F58: make `SIG_LABELS` skip header rows (row 0 of a non-label table) in `render_docx.py`, with a test.~~ **Done 5 Nov 2026 (§2u).** | ~~with the next renderer change~~ done |
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
| **`copy-iso-reference.zsh`** copies, never moves, into `~/Documents/SESC/ISO/`: `Reference/Standards/` (BS 99001 PDF and text, CIOB Code, ISO 45001:2018, ISO 14001:2015, ISO 9001:2015); `Reference/CertiKit/` (six demo files and the 27001 v13-1 folder); `Reference/Architecture/` (the Plan); `Reference/Design/` (BRAND-SPEC, INTERIOR-SPEC, master logo); `Reference/Decisions/` (the consistency findings and completion note, the C2–C8 decisions, Section workflow method, signature verification, the PI, accident book and guarantees/training findings, and `JOSCAR Master Register.md`); `Signed/` (the 21 signed PDFs, flattened); `Insurance/` (all nine). `cp -n` never overwrites; every file is checked with `cmp`, the 27001 folder with `diff -rq`; it prints copied / differ / missing counts and the signed count (expect 21). Tested against a mock tree and run twice: idempotent. **Not copied, deliberately:** `PROJECT-INSTRUCTIONS.md`, `README (1).md` and `SESC Document Design Spec.md` (old instruction files — the cause of this finding), `sesc_cover.py` (already ported), the JOSCAR-only reference notes, the Armed Forces Covenant files, the stale `CLAUDE ISO` copy, `CLAUDE CODE OUTPUT`, `_Claude Project setup`, and everything POW, ITC and Pow Property. | Gary runs it | **RUN 7 Oct 2026: 57 copied and identical, 0 differ, 0 missing, 21 signed (§2n.1)** |
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
| **Gary** | ~~Run `copy-iso-reference.zsh` **before** applying the patches; expect `0 differ`, `0 missing`, signed count 21. Any `MISSING` or `DIFFERS` line: stop and bring it to the next chat.~~ **CLOSED 7 Oct 2026 — ran clean (§2n.1).** | Done |
| Gary | ~~Run the SHA-256 check above.~~ **CLOSED 7 Oct 2026 — matched (§2n.1).** | Done |
| Gary | Replace section 3 of the Claude Project instructions and remove the Handover file from Project knowledge. | now |
| Gary | Decide, separately, whether the TeraBox restore stays on the Mac. Nothing in the project depends on it once the copy is verified. **Its copy of `CLAUDE ISO` must never be opened as if it were the repository.** | your call |
| Later chat | Bring REG-02, REG-03, REG-04, REC-01…04 and TPL-01…04 into `Signed/` when a workstream needs them; they were not in `Branded/Signed/`. | when needed |

---

### 2n.1 Status carried forward, 7–12 October 2026 (recorded at v1.19, before workstream 5)

**Source: Gary's instructions at the start of the workstream 5 chat, 12 October 2026, and this chat's own read-only checks.**

| Item | Position |
|---|---|
| **PR #16 (workstream 3, register v1.18)** | **Merged as `cd98fdd`** (*Merge pull request #16 from GaryHill0985/workstream-3-ims05-leadership*), parents `f2c726b` (register v1.18) and `46c1c25` (CLAUDE.md §2/§9.4/§11). Confirmed 12 Oct 2026 from a fresh read-only clone: `git ls-tree cd98fdd` lists `system/5-leadership.md` and `forms/SESC-FRM-08-worker-consultation-record.yaml`; `CLAUDE.md` §11 names the three sources. **Workstream 3 is closed as committed.** |
| **SHA-256 check (F59 provenance)** | **Run by Gary, 7 Oct 2026:** POL-05, POL-08 and POL-16 in `~/Documents/SESC/ISO/Signed/` match the hashes at §2n. The copy script reported **57 copied and identical, 0 differ, 0 missing, 21 signed.** Confirmed independently by this chat on 12 Oct 2026 (same three hashes on the staged copies). **F59 closed.** |
| **The MacBook cannot render branded PDFs (F62)** | **Gary, 7 Oct 2026: the MacBook has neither LibreOffice nor `pdftotext`.** So `build/render_docx.py --pdf` cannot run there and the two printed-number tests in `build/test_render_docx.py` skip. §2g's statement that IMS-04 was rendered on the MacBook with LibreOffice, 19/19 including the PDF test, **is not supported by what is on the machine now**; it is recorded here and §2g is not rewritten. Run the tests as `python3 build/test_render_docx.py` — the `-m unittest` form does not load on the Mac. Tasks below. |
| **D26** | Gary's recommendation: direct consultation through the toolbox talks and the quarterly meeting, with no separate representative. Steve to confirm, most simply on signing IMS-05; IMS-05 ¶37 and Part 6(e) to state the decision at v0.2. Recorded at D26. |
| **Working folder with James Milligan — Steve's choice** | **The shared ISO folder on the Google Drive replaces James's Dropbox as the working folder with James.** It is a **transfer folder, not a source** (CLAUDE.md §11 unchanged). The Dropbox copy and `~/Documents/SESC/SESC Solutions Limited/` are stale duplicates and not sources. **Only copies marked DRAFT go to the Drive folder; no personal data, no insurance documents, and never this register.** |

**Tasks by owner, from this section:**

| Owner | Task | By |
|---|---|---|
| Gary | Install LibreOffice from libreoffice.org on the MacBook, so the PDF tests run and branded renders can be read as images there | before the next render |
| Later chat | Add a `pdfplumber` fallback to `build/test_render_docx.py` for the printed-number test where `pdftotext` is absent | with the next renderer change |

---

## 2o. Workstream 5 — `SESC-REG-09` Compliance Obligations Register, draft v0.1, 12 October 2026

**Taken:** workstream 5 only (§6 item 5; IMS-00 Part 10 (g); G5). **Started once `main` was confirmed to contain PR #16** (§2n.1). This chat ran in Cowork with the MacBook linked. **The clone's `.git` and most tracked files could not be read through the device bridge's shell** — every read returned *Resource deadlock avoided* — because the files in `~/Documents/SESC/ISO/` are **iCloud cloud-only placeholders** (F64). The bridge's file tools could stage them (which downloads them), so every tracked text file was staged and hashed: **all 37 match `main` at `cd98fdd` byte for byte**, and the working tree held nothing else but the untracked `Claude outputs/`, `out/` and `_to_delete/`. The chat then worked in a fresh clone of `GaryHill0985/QMS` on branch `workstream-5-reg09-compliance-obligations`, and the changed files are written back to the MacBook clone through the bridge's file tools (checked on disk by hash afterwards, §7.9). Nothing was committed: Claude does not run git against the clone (§7.7).

**The 2020 register was looked for first, as instructed.** It is not in the repository, not in `SESC-REG-07`, not in IMS-00 Annex B as a document, and not anywhere under `~/Documents/SESC/ISO/` (all 57 reference files listed). It was not looked for on the Drive beyond folder 14. By name it is not in the TeraBox restore either (file listing only — not read, not a source). **It exists in none of the three sources, so nothing was asked for and nothing was carried from it.** What *was* found: **`SESC-POL-19` v1.1 ¶84–86 says the Employer's Compliance with Legislation Register is at POL-19 Annex A (30 rows, signed 16 Aug 2026), and that "any earlier legal register — including one dated 2020, or one containing links to network drives that no longer exist — is superseded by Annex A and must be withdrawn from use."** So the Employer already has one issued legal register — product and installation law only — and REG-09 is built to supersede *that* on Steve's approval, with every Annex A row re-evaluated and carried.

| Built | Where | Status |
|---|---|---|
| **`SESC-REG-09` Compliance Obligations Register.** Reference taken from `CLAUDE.md` §5 in the same change (next free register now REG-10). **79 obligations in four parts:** A — occupational health and safety (CO-01…41, including the product and installation law of POL-19 Annex A); B — environment (CO-42…58); C — data protection, employment, corporate and business conduct (CO-59…69); D — other requirements: MOD/QinetiQ site rules and JSP 375, DEFCON 658 and the Cyber Security Model, Sovereign Network Group's contractor documents, principal contractors and SSIP/CHAS/Constructionline, JOSCAR, MCS, NICEIC/Part P, PAS 2030/2035 and TrustMark, the insurance conditions precedent, customers' contract terms (CO-70…79). Each row: the source and its exact title as the issuing body publishes it, with the URL read and the date; who imposes it; which trades and site types it applies to (mould and damp remediation in; fire doors not a trade); what it requires of the Employer; the arrangement cited to the signed document and paragraph; the evidence, each record **held / not yet held with a date / nil return / not verified**; the REG-05 party and the REG-02 check it points to; the owner; the review frequency; and `last_evaluation: none yet` on every row. A `considered_and_not_carried` list (OFTEC, RECC, NFRC, the revoked List of Wastes Regulations, the removed hazardous-waste premises registration, the EPB Regulations, abstraction, marine) says what was looked at and left out, and why. Carries a *Records held, records not yet held* block and a revision history. | `registers/compliance-obligations.yaml` | **Draft v0.1** |
| **Clause map claimed:** 14001 6.1.3 and 45001 6.1.3 (determined and maintained — 14001 from the `verified: false` map, and the file says so); **14001 9.1.2 and 45001 9.1.2 claimed only because the register carries a documented `evaluation_method`** (frequency, who, the five-step how, the record, the outputs), with the clause note that **no evaluation of compliance has been carried out under any system** and the first is due **30 Nov 2026** (IMS-00 Part 10 (g)). **Nothing from ISO 9001.** `validate.py` flags 45001 6.1.3 as dual maintain-and-retain: the maintained half exists, the retained half (the evaluation record) does not, and the register says so. | front matter | — |
| **Every legal source read on its issuing body on 12 Oct 2026** — legislation.gov.uk for every statute and SI (titles copied as displayed, SI numbers checked), gov.uk and hse.gov.uk for RIDDOR, the law poster, the waste carrier service, F-gas certification, JSP 375, the Cyber Security Model and BPSS, ico.org.uk and S.I. 2018/480 for the fee, and the scheme bodies' own sites (MCS, NICEIC, Gas Safe via gov.uk/HSE, Refcom/Quidos, BSI/TrustMark, SSIP/CHAS/Constructionline, Hellios, SNG, QinetiQ). **Four things the reading changed:** (i) the official title is *Health and Safety Information for Employees Regulations 1989* (no parentheses); (ii) the **List of Wastes (England) Regulations 2005 are revoked** (1 July 2015) and the **hazardous-waste premises notification was removed in 2016** — POL-08 ¶16 and ¶34(d) are stale on both (F63); (iii) the own-waste upper-tier point now rests on the instrument itself, reg 24(5)(e) of S.I. 2011/988 (F8 updated); (iv) **S.I. 2026/873 abolishes waste carrier registration in England in favour of environmental permitting**, Part 2 in force at the end of twelve months from 22 July 2026 — a new obligation nobody had seen (CO-43, F63). Also read and recorded: PSTI Act 2022 s.55(5) makes an installer a *distributor* of consumer connectable products; the ICO fee tiers (S.I. 2025/63); the NMW rates from 1 April 2026; Equality Act s.40A in force 26 Oct 2024 with the ERA 2025 "all" uncommenced; MCS's requirement of a CTSI-approved consumer code (RECC or HIES) — see F61. | `source_url` on every row | — |
| **POL-19 Annex A re-evaluated row by row.** All 30 rows map to a CO row (the mapping is in the file's `source_counts`). POL-19's Annex A UK REACH row cites "Sections 12 and section 18 of SESC-POL-16", an ambiguous cross-reference, and POL-05 Annex A cites "Legal Register entry H024" — a pointer into the superseded 2020 register. Both are recorded for POL-19 v1.2 and POL-05 v1.2; neither issued document was touched. | CO-52 | — |
| **Structure from James Milligan's legal register, nothing else.** `Legal and Compliance Register.xlsx` in folder "14. Legal and Regulatory Requirements" of the shared ISO folder was read once, read-only, through the Drive connector: 108 rows typed across 39 topics, five columns (*Type · Compliance Obligation · Purpose / Impact · Link to Guidance · Last reviewed and compliance confirmed*). The topic typing and the idea of a per-row "last confirmed" date were taken; **no row, no wording and no link was copied**, and nothing else in that folder was opened. Nothing carries a POW, ITC, LARC, HCPL or Unitspark reference. | — | — |
| `CLAUDE.md` §5: REG-09 recorded as taken on 12 Oct 2026; next free register REG-10. `portal/actions.yaml`: G5 detail updated (status **open** — the register is drafted; the evaluation record is the open half), source line now v1.20. Portal rebuilt: 31 pages, **17 controlled files**, 134 clauses, 81 actions. | `CLAUDE.md`, `portal/` | Done |

**Verification.**

1. `build/validate.py`: **0 errors**, 14 warnings (the expected 14001 `verified: false`, now including `registers/compliance-obligations.yaml`), 6 notes (one new: REG-09 cites 45001 6.1.3, dual maintain-and-retain). BUILD PASSES. 17 controlled files. The first YAML load failed four times on unquoted scalars containing colons; each was quoted and the file re-parsed.
2. `python3 build/test_render_docx.py`: **25/25 pass** in the container (LibreOffice and `pdftotext` present). Not run on the MacBook — see §2n.1 and F62.
3. `python3 build/build_portal.py`: rebuilt; the clause map page shows 14001 6.1.3, 14001 9.1.2, 45001 6.1.3 and 45001 9.1.2 as **draft only** (REG-09 declares them; no record sits behind them), which is the honest state. The page was rendered to PNG with headless Chromium and read as an image.
4. **Row count against the sources worked from:** 79 rows. 30 from POL-19 Annex A (all mapped); 19 instruments from POL-08 ¶16's minimum list (17 carried, 2 at *considered and not carried*); every "legal" requirement in REG-05 v0.2 (IP-01, 06, 07, 08, 09, 15) has a row; 30 + 24 + 25 + 15 instruments and bodies verified across the four verification sets, every one with a URL read. 71 rows cite an arrangement to a signed paragraph; **8 have no arrangement in any signed document** — Unit 19 fire risk assessment (CO-24), Unit 19 welfare (CO-25), DSE (CO-30), packaging EPR thresholds (CO-54), ozone-depleting substances (CO-58), company accounts (CO-62), CIS and auto-enrolment (CO-63), and protected disclosures (CO-69), whose document could not be read (F60). All 79 read `last_evaluation: none yet`.
5. **Not rendered to a branded view.** Registers are YAML and `render_docx.py` renders Markdown; REG-05…08 were not rendered either. The portal page is the register's rendered view and was read as an image (3).

**The twenty-one signed documents were read in full for this workstream** (every page of every PDF in `Signed/`, text layer, 12 Oct 2026, by five parallel reads with line counts confirmed to the end of each file): POL-05 (32 pp), POL-08 (23), POL-19 (39), POL-13 (89), POL-14 (13), POL-15 (36), POL-16 (21), POL-17 (22), POL-18 (16), POL-01/02/04/06/07/09/10/11/12, CRP-01 and REG-01. **Which is how F60 was found: the file named `SESC-POL-03 Whistleblowing (Speak Up) Policy v1.1.pdf` contains the Employee Code of Business Conduct, POL-01 v1.0** — cover read as an image: *Code of Conduct · SESC-POL-01 · 1.0 · 12 August 2026*. The same bytes (SHA-256 `9e804b8b…`) sit in the TeraBox restore at `JOSCAR/Documents/2.2 Human Resources/Branded/Signed/` and in `Evidence Pack/09 Human Resources/… (signed).pdf` — so this is what was submitted to JOSCAR as the Whistleblowing Policy. No signed Whistleblowing Policy text was found anywhere this chat could look.

**Not done, deliberately.** No issued document was changed (POL-19 Annex A, POL-08 ¶16/¶34(d), POL-05 Annex A 2.6.4.15 are recorded for their next revisions). No registration number was checked against a public register, and no public register was queried: the ICO query (F7), the waste carrier tier (F8) and the scheme checkers are tasks with owners, not things a chat asserts. Nothing was sent to James Milligan; nothing went to the Drive. No evaluation of compliance was attempted: it is the owner's record, not a chat's. IMS-00 is untouched.

**Tasks by owner, from this session:**

| Owner | Task | By |
|---|---|---|
| **Gary** | Check the three written-back files landed in the clone (`md5` in Terminal, §7.9), run `git status` in Terminal and expect exactly `CLAUDE.md`, `portal/actions.yaml`, `SESC-IMS-Master-Register.md` modified and `registers/compliance-obligations.yaml` untracked; then commit as **two commits on one branch** from an up-to-date `main` (§7.8): (1) `registers/compliance-obligations.yaml` + `CLAUDE.md` + `portal/actions.yaml`; (2) register v1.19–v1.20. Open the PR. **Claude does not merge.** Commands given in the chat. | this week |
| Gary | Read REG-09 v0.1 end to end — 79 rows — and strike, correct or confirm each *proposed* date; the owners are the Contracts Manager (as EM/H&S Officer/QR), the Accounts Manager, the Managing Director and Gary | 30 Nov 2026 |
| **Gary** | **F60: find the signed Whistleblowing Policy.** Check `~/Documents/TeraBox Restore/…/2.2 Human Resources/Branded/` (unsigned PDF and DOCX exist there by name) and the Drive "(signed)" set; if no signed POL-03 exists, it is re-rendered from the DOCX and **Steve signs it again**, and the JOSCAR evidence pack is corrected. Until then CO-69 cites nothing. | 31 Oct 2026 |
| Gary | **F61:** establish from MCS's and the Employer's own documents whether a CTSI-approved consumer code membership (HIES, or a renewed RECC) is held now that RECC lapsed on 15 Nov 2024; if not, this is a scheme-rule gap to raise with Steve (it is a spend) | 31 Oct 2026 |
| Gary | Bring `SESC-REG-04` and the certificate copies it indexes (NICEIC, Gas Safe, MCS, PAS 2030, F-gas, SSIP, CHAS, Constructionline, JOSCAR) into `~/Documents/SESC/ISO/Signed/` (§2n "when needed" — needed now), so CO-23, 41, 73–77 can be marked held or not | 31 Oct 2026 |
| Gary | **F64:** decide whether `~/Documents/SESC/ISO/` stays in an iCloud-synced location. A git clone whose files are evicted to the cloud cannot be read by the bridge's shell and may be unreadable by git itself at the wrong moment; "Keep Downloaded" on the folder, or moving the clone outside iCloud, fixes it. **Gary's decision; nothing moved by this chat.** | before the next chat |
| **Environmental Manager** | **CO-43 / F8 / Part 10 (r):** confirm the tier of CBDL569181 from the certificate and a dated public-register query; then plan the S.I. 2026/873 transition (permit or exempt-activity registration before Part 2 commences, July 2027) | tier 31 Oct 2026; plan 31 Mar 2027 |
| **Contracts Manager** (as EM and H&S Officer) | **The first documented evaluation of compliance against REG-09**, by the method in the file — the retained half of 14001/45001 6.1.3 and the whole of 9.1.2. **No evaluation has ever been carried out.** Take `SESC-REC-05` for the record in that chat. | 30 Nov 2026 |
| Accounts Manager | **CO-60 / F7:** query the ICO public register and record the dated result; then the fee (tier depends on turnover — Steve's spend) | 31 Oct 2026 |
| **Steve** | Approve REG-09 as the Employer's single compliance obligations register (signature follows IMS-04's), and instruct the amendment of POL-19 Annex A, POL-08 ¶15–19/¶16/¶34(d) and POL-05 Annex A 2.6.4.15 to point at it (v1.2 of each, by PR) | after IMS-04 |
| **Steve** | **CO-24 / F49:** the Unit 19 fire risk assessment — a legal duty under the Fire Safety Order now, not an ISO item; and FS-01…14 | 30 Nov 2026 (*proposed*) |
| Later chat (POL-08 v1.2) | **F63:** correct ¶16 (List of Wastes Regulations revoked), ¶34(d) (no premises registration since 2016), add the S.I. 2026/873 position, and replace ¶15–19's own legal register with a pointer to REG-09; add the records-not-yet-held section POL-08 lacks | after approval of REG-09 |
| Later chat | Workstream 4, the aspects and impacts register, is blocked on 14001:2026 (D6/B4). REG-09 gives it the legal side; it still cannot start until the standard is bought and read. | after D6 |
| Later chat | When REG-09 is approved: IMS-00 Annex B rows 6.1.3 and 9.1.2 move to REG-09 and Part 10 (g) is re-dated to the first evaluation — **only on approval** (IMS-00 `review_trigger`) | on approval |

**Completion note.** The Employer now has one register that names every legal and other requirement its signed documents commit it to — 79 of them, each read on its issuing body's own site on the day, each pointing at the paragraph that meets it and at the record that would prove it, and each saying plainly whether that record exists. Most do not, and the dates the signed documents set for them have largely passed; the register records that rather than re-dating it. It claims the determination clauses and, on the strength of a written method, the evaluation clauses — while saying on every row that no evaluation has ever been done. The reading turned up a legal change nobody had seen (waste permitting from July 2027), two stale statements in a signed environmental manual, and a signed Whistleblowing Policy that turns out not to exist as a file. Nothing signed, committed, sent or merged; one decision carried forward (D26, Gary's recommendation recorded); five new findings (F60–F64).

## 2p. Waste carrier registration CBDU663802 received — CO-43 / F8 / Part 10 (r) closed, 22 October 2026

**Source: Gary, in the chat, 22 October 2026 — "We've just received our new waste carriers licence (SESC SOLUTIONS LTD, CBDU663802) 01/10/26–01/10/2029".** Not a build workstream; a records update. The clone was on `workstream-5-reg09-compliance-obligations` with the v1.19–v1.20 register change still uncommitted (Gary's `git status`, pasted); this chat's edits sit on top of it and go in the same commit. The iCloud placeholder problem (F64) was unchanged — every shell read of the clone returned *Resource deadlock avoided* — so the five files were staged through the bridge, edited in the container, and written back through the bridge's file tools with the modification-time guard, as §2o did. Nothing was run against `.git`.

**Checked on the issuing body, not taken on trust.** The Environment Agency public register was queried on 22 October 2026 for both numbers (`https://environment.data.gov.uk/public-register/waste-carriers-brokers/registration/<number>`), fields recorded verbatim in `SESC-REC-05`:

| Number | Register shows | Meaning |
|---|---|---|
| **CBDU663802** | "SESC SOLUTIONS LTD", company 07606236, **"Carrier Dealer - Upper Tier"**, registered 01/10/2026, expiry 01/10/2029, address "S E S C SOLUTIONS LTD., MELBURY BUSINESS PARK, WEST MELBURY, SHAFTESBURY, SP7 0AF" | **Upper tier — the tier CO-43 requires** (construction waste is excluded from the own-waste exemption, S.I. 2011/988 reg 24(5)(e)). Three-year term matches the upper-tier cycle. **F8 closed; IMS-00 Part 10 (r) met.** |
| CBDL569181 (POL-19 Annex A row 25) | "sesc solutions", **"Carrier, Broker, Dealer - Lower Tier"**, registered 05/02/2025, no expiry, address "UNIT 9, MELBURY BUSINESS PARK …" | **The number the signed documents cite was lower tier, which was never sufficient for construction waste** — F8's suspicion confirmed. Still listed; whether the EA has cancelled it is not shown. |

**Three things the register shows that need an owner (new F65, F66):** (i) the superseded lower-tier entry is still public, so a customer or auditor searching will find two registrations at different tiers — ask the EA to cancel it; (ii) the new entry carries no unit number and the old one says Unit 9, where the Employer's documents say Unit 19 — check against the lease and correct the EA entry within 28 days if wrong; (iii) the new registration is **carrier and dealer, not broker** — if the Employer ever arranges waste removal on a customer's behalf, that is not covered. The S.I. 2026/873 transition (permitting from July 2027) is unaffected and stays with the Environmental Manager at 31 Mar 2027.

| Changed | Where | Status |
|---|---|---|
| `SESC-REG-09` amended in place to **draft v0.2** (`revised: 2026-10-22`, revision history kept): CO-43 evidence — registration **held** with number, tier, type and dates; public-register check **held** (SESC-REC-05); two new not-yet-held records (certificate copy filed in `Signed/` and indexed in REG-04, COO, 31 Oct; EA confirmation that CBDL569181 is cancelled, EM, 30 Nov); broker and address points in the note. The POL-19 row-25 citation marked superseded. `records.not_yet_held` updated; the evaluation record now takes **SESC-REC-06**. `last_evaluation` stays `none yet` on every row — a register check is not an evaluation of compliance. | `registers/compliance-obligations.yaml` | Done |
| **`SESC-REC-05` taken** from `CLAUDE.md` §5 for the public-register check — the first entry in `portal/records-index.yaml` since REC-01…04 on 17 August. **Mapped to no clause, deliberately:** one registration checked on one day does not evidence 14001/45001 9.1.2; the first documented evaluation will. Metadata and the verbatim register fields only; no personal data. `CLAUDE.md` §5 next free REC reference now REC-06. | `portal/records-index.yaml`, `CLAUDE.md` | Done |
| `portal/actions.yaml`: **F8 closed** (kept, marked closed); **F65** (superseded registration still public; address; certificate to file) and **F66** (broker not covered) added, both low, Environmental Manager, 30 Nov 2026. Source line now v1.21. Portal **not rebuilt** this chat. | `portal/actions.yaml` | Done |
| **Not changed:** POL-19 v1.1 Annex A row 25 and POL-08 v1.1 ¶34(a) are issued documents; the new number and tier go in at v1.2 of each (already queued under F63 and Steve's REG-09 approval task). IMS-00 Part 10 (r) is untouched — the manual is re-dated only on approval (`review_trigger`). The Claude Project instructions §11 still say "the waste carrier tier is unconfirmed" — **Gary to edit the Project instructions**; a chat cannot. | — | — |

**Verification.** `build/validate.py` run in the container against the five written-back files plus the unchanged tracked set staged from the clone: result recorded in the revision history row. All three YAML files re-parsed after patching. Each written-back file's MD5 is listed below for Gary's check in Terminal (§7.9).

**Tasks by owner, from this chat:**

| Owner | Task | By |
|---|---|---|
| **Gary** | Check the five written-back files landed (`md5` in Terminal, §7.9); `git status` should show `CLAUDE.md`, `portal/actions.yaml`, `portal/records-index.yaml`, `registers/compliance-obligations.yaml` and `SESC-IMS-Master-Register.md` modified on `workstream-5-reg09-compliance-obligations`; commit (register v1.19–v1.21 and this change together is acceptable — it is all one branch) and open or update the PR. **Claude does not merge.** | this week |
| **Gary** | File a copy of the CBDU663802 registration certificate (the EA's PDF or letter) in `~/Documents/SESC/ISO/Signed/` with the REG-04 certificate set, and index it in `SESC-REG-04` when REG-04 is brought into the repository (§2o task) | 31 Oct 2026 |
| Gary | Edit the Claude Project instructions §11: the waste carrier tier is confirmed upper (CBDU663802, 01/10/2026–01/10/2029, SESC-REC-05) | this week |
| **Environmental Manager** | **F65:** ask the Environment Agency to cancel CBDL569181; confirm the registered address of CBDU663802 against the lease (Unit 19?) and correct the EA entry if wrong (28-day notification) | 30 Nov 2026 |
| **Environmental Manager** | **F66:** confirm whether the Employer ever arranges removal of waste on a customer's behalf; if so, vary CBDU663802 to add broker before that activity continues | 30 Nov 2026 |
| Environmental Manager | S.I. 2026/873 transition plan (unchanged from §2o) | 31 Mar 2027 |
| Later chat (POL-19 v1.2, POL-08 v1.2) | Replace CBDL569181 at POL-19 Annex A row 25 with CBDU663802, upper tier, expiry 01/10/2029; give POL-08 ¶34(a) the number, tier and the date of the last public-register check | with F63 |

**Completion note.** The one registration number the signed documents carry turned out to be a lower-tier registration, which could never have covered the construction waste the Employer's vans carry. The new upper-tier registration fixes that, and for the first time the system holds a dated, verbatim public-register check rather than an assertion. F8 is closed on the issuing body's own record. Two small follow-ups go to the Environmental Manager: get the old entry cancelled and the address right, and settle whether brokering ever happens. Nothing signed, committed, sent or merged.

---

## 2q. Workstreams 6 and 4, and the clause 6 chapter — the four core procedures, `SESC-REG-10` and `SESC-IMS-06`, draft v0.1, 26 October 2026

**Taken:** Gary's instruction in the chat, 26 October 2026 — *"Everything that you feel is relevant to SESC must be drafted"*, so that a draft of every document James Milligan's template set implies can be put in front of him — with Batch A (the Stage 1 set) started first at Gary's choice: the four core procedures, the aspects register and IMS-06. Batches B (the operational procedures) and C (the remaining spine chapters and policy gaps) are queued at §6. **Three workstreams in one chat, against §9.2 of CLAUDE.md, at Gary's explicit direction.** The clone was on `workstream-5-reg09-compliance-obligations`. **This chat assumed the v1.19–v1.21 register change was still uncommitted; Gary's `git status` at the end of the chat showed otherwise** — the branch was up to date with origin and `registers/compliance-obligations.yaml` and `portal/records-index.yaml` were clean, so §2p and v1.19–v1.21 had already been committed and pushed. The only modified files were this chat's three (`CLAUDE.md`, this register, `portal/actions.yaml`) plus the six new untracked files. Recorded as a correction (§7.7 in reverse: a file expected to be modified and which is not is evidence that it was committed). `git status` was run after the drafting, not before; that order is recorded, not excused. F64 unchanged: every shell read of the clone returned *Resource deadlock avoided*, so every file was staged through the bridge (downloading the iCloud placeholders), edited in the container, and written back with the modification-time guard. Nothing was run against `.git`.

**What was read first, in full.** Every page of SESC-POL-05 v1.1 (32 pp), SESC-POL-08 v1.1 (23 pp) and SESC-POL-16 v1.2 (21 pp), text-extracted from the signed PDFs in `Signed/`; SESC-IMS-00 v0.1, SESC-IMS-04 v0.3 ¶11–13, SESC-IMS-05 v0.1; SESC-REG-09 v0.2 (structure and evaluation method); SESC-FRM-05 v0.2; the three clause maps; `front-matter-schema.yaml`; `validate.py`; `CLAUDE.md` in full. James Milligan's local template copy at `~/Documents/SESC/SESC Solutions Limited/` was **inventoried by file name only** (173 files), at Gary's request in the chat, to answer which of its documents SESC has no equivalent for; not one file in it was opened in this chat.

### 2q.1 Decision D27 — the EMS documents are drafted now, not after the standard is bought

Gary, 26 Oct 2026, in the chat: buying ISO 14001:2026 *"really isn't a pre-requisite to pass stage 1 … It's also not a prerequisite to purchase the book before applying."* Recorded as **D27**: the aspects register and every EMS document are drafted to the 14001 clause structure held in `standards/iso14001-2026.yaml` (carried from :2015, `verified: false`), written 2026-ready, with a `review_trigger` of *ISO 14001:2026 being bought and read* in every one. **B4 changes from a blocker on drafting to a review trigger on the drafts.** What does not change: `CLAUDE.md` §6 (certify to :2026; no :2015 certificate), the rule that no 14001 clause number is quoted to a customer or an auditor until the 2026 text has been read, D6 (Steve still buys the standards), and PJR's written answer on the edition (F48) as the decision that settles what SESC certifies to. The B4 row at §3 is amended below. **The register's earlier wording "Buy it before writing any EMS document" (§3 B4; `SESC-IMS-00` ¶30 "cannot be written until ISO 14001:2026 has been bought and read"; `portal/actions.yaml` G4 "Blocked on buying 14001:2026") is superseded by D27; IMS-00 ¶30 is an issued-draft sentence and is corrected at IMS-00 v0.2, not here.**

### 2q.2 What was drafted

| Changed | Where | Status |
|---|---|---|
| **`SESC-PRO-01` Control of Documented Information, draft v0.1.** Takes the rules already operated under IMS-00 §6.5, POL-05 A30, POL-08 E17 and POL-16 Q1 into one procedure, unchanged; adds the records rules of D15 and CLAUDE.md §8, the repository rules of §7, a ten-stage table, a review checklist (Annex A) and the F64/§7.7 operating rules. Claims 7.5.2, 7.5.3 of all three; not 7.5.1 (IMS-00's). Owner: Chief Operating Officer. | `documents/SESC-PRO-01-control-of-documented-information.md` | Drafted; Steve to sign; IMS-00 §6.5 remains operative until then |
| **`SESC-PRO-02` Internal Audit, draft v0.1,** with the **first-cycle programme IA-01 to IA-06 at Annex A (PROPOSED)**, front-loaded towards the Stage 1 criteria: IA-01 Nov 2026 management processes (external internal auditor); IA-02 Dec 2026 records, reporting, consultation, competence (COO); IA-03 Feb 2027 a live site (COO); IA-04 Mar 2027 performance evaluation and improvement including the COO's own audits (external); IA-05 Jun 2027 follow-up; IA-06 Sep–Oct 2027 second-cycle planning. The **independence allocation at ¶8** answers D3's problem: James audits what Gary built; Gary audits what Craig operates; whoever reviewed a document does not audit it; nobody audits their own work. States plainly that **no audit qualification is claimed for either auditor** and that B5 is not closed. Consolidates POL-16 ¶69, POL-05 ¶48(c), POL-08 E10. Claims 9.2.1, 9.2.2 of all three. | `documents/SESC-PRO-02-internal-audit.md` | Drafted; programme awaits Steve's approval and the D3 appointment |
| **`SESC-PRO-03` Management Review, draft v0.1.** One annual review (**November**) with quarterly interim reviews (Feb, May, Aug) aligned to the REG-01 quarterly review and the quarterly consultation meeting; the **analysed pack** as the mechanism for ISO 9001 9.1.3 ("a pack that reports *no data* for an item is correct; a pack that omits the item is not"); every input and output of the three standards tabled by source record and owner; the sole-director clause operated at ¶9; agenda and minutes templates at Annexes A and B. Records the **30 September 2026 review commitment as overdue**, not re-dated. Claims 9.1.3, 9.3.1–9.3.3 (9001); 9.3 (14001, 45001). | `documents/SESC-PRO-03-management-review.md` | Drafted; first review proposed for November 2026, date for Steve to fix in REG-02 |
| **`SESC-PRO-04` Nonconformity and Corrective Action, draft v0.1.** Five steps — react, record, investigate, act, verify — on **one log for three standards (SESC-FRM-05)**; thirteen sources tabled; grading; the Q14 dispositions pointed at, not restated; "operator error" never a cause without *why*; closure by independent verification, never by the calendar; time limits (major 30/90 days, minor 60/120); the earlier consultant's NC log recorded at Part 8(g) as **not the Employer's and not offered**. Records the **31 August 2026 log-opening commitment as overdue**. Claims 10.2.1, 10.2.2 (9001); 10.2 (14001, 45001); not 8.7 (POL-16 Q14). Owner: Contracts Manager. | `documents/SESC-PRO-04-nonconformity-and-corrective-action.md` | Drafted; log opens at record capture go-live |
| **`SESC-REG-10` Environmental Aspects and Impacts Register, draft v0.1** — **the gap CLAUDE.md §10 called the highest priority in the system, now a draft.** Twenty-eight aspects in ten activity groups, every one taken from SESC-IMS-04 ¶14 and POL-08 ¶12 and ¶37 — vehicles and plant; Unit 19; roofing and fabric; mechanical, gas and F-Gas; electrical; renewables; waste and strip-out; mould and damp remediation; site set-up and water; emergencies — each with life cycle stage, condition, control-or-influence, a documented significance method (severity × likelihood ≥ 10, or a direct legal requirement, or emergency reach to water or protected species, or a stated interested-party requirement), **proposed** scores, the control cited to the signed paragraph, the REG-09 topic, the REG-05 party, the IMS-06 objective area, and evidence marked held or not yet held with a date. **Twenty-four proposed significant, four not. Every score is proposed; nothing is communicated.** No quantity is stated because the E15 data set does not exist; the first data set is a review trigger. Claims 14001 6.1.2 only. Owner: Contracts Manager (Environmental Manager). | `registers/environmental-aspects.yaml` | Drafted; Environmental Manager to confirm scores; Steve to approve |
| **`SESC-IMS-06` Planning, draft v0.1** — the clause 6 chapter. Points at REG-01, REG-06, REG-05, REG-08 (risks and opportunities), REG-10 (aspects) and REG-09 (obligations) rather than restating them; adds the OH&S-opportunities process for 45001 6.1.2.3 (REG-08 v0.2 to carry an OH&S tag); planning of action (6.1.4) integrated into the quotation, RAMS, readiness review and procurement; **nineteen PROPOSED objectives** at ¶18 across quality (OB-Q1–Q5), environment (OB-E1–E5), health and safety (OB-H1–H6) and the system (OB-S1–S3), each giving a number and a date to a framework already signed (POL-16 ¶67, POL-05 ¶46, POL-08 ¶65), each with baseline *measured or not measured*, target, actions, resources, owner, measure and evaluation point; **no percentage reduction is proposed against an unmeasured baseline** — OB-E1 to E3 are "measure first, set the target at the February 2027 interim review"; planning of changes (6.3) with D27 itself recorded as the first planned change. Records every passed commitment date as overdue. Claims 9001 6.1.1, 6.1.2, 6.2.1, 6.2.2, 6.3; 14001 6.1.1, 6.1.4, 6.2.1, 6.2.2; 45001 6.1.1, 6.1.2.3, 6.1.4, 6.2.1, 6.2.2. | `system/6-planning.md` | Drafted; **no objective is set until Steve signs** |
| `CLAUDE.md` §5 next-free line: `SESC-PRO-01` to `SESC-PRO-04`, `SESC-REG-10` and `SESC-IMS-06` taken 26 Oct 2026; next free now `SESC-PRO-05` · `SESC-REG-11` · `SESC-IMS-07`. | `CLAUDE.md` | Done |
| `portal/actions.yaml`: D27 added; B4 re-worded (review trigger, not a drafting blocker); G1, G2, G3, G4, G9, G10 updated to *drafted* with the document named (none closed — a draft procedure closes no gap; the record does); F67–F70 added; source line v1.22. Portal **not rebuilt**. | `portal/actions.yaml` | Done |

**Verification.** `build/validate.py` run in the container on 26 Oct 2026 against the staged tracked set plus the six new files: **17 controlled files, 134 clauses, 0 errors, 16 warnings (all the standing ISO 14001 unverified-edition warning, one per file citing 14001), 7 notes. BUILD PASSES.** All three new YAML files parse; the house-style check raised nothing. **Not done: no branded render.** The MacBook has no LibreOffice (F62) and the container's renderer was not run on these six files in this chat; the first render is the next chat's first task and F27/F34/F58 apply. Every written-back file's size and MD5 is listed in the completion note for Gary's check in Terminal (§7.9).

### 2q.3 Findings raised

| # | Finding | Severity | Owner |
|---|---|---|---|
| **F67** | **Every commitment date in the three signed documents for the records these procedures operate has passed** — corrective action log and monthly report (31 Aug / 30 Sep 2026), management review (30 Sep), internal audit (31 Oct, will not be met), induction and toolbox records, PAT, face-fit, health surveillance provider, noise assessment, approved contractor register, calibration verification, Driver Register, COSHH registers, first aid needs assessment (all 31 Aug–31 Oct 2026). The procedures record each as **overdue** and propose new dates marked *proposed*; none is re-dated silently. **Steve's decision at the first management review is to confirm, re-date once with the reason minuted, or close each** (SESC-PRO-03 ¶14(f); OB-S3). The pattern is itself the first finding the first audit will make. | **High** | Steve, at the November 2026 review |
| **F68** | **Three signed documents each describe their own annual audit, their own management review and their own corrective action log** (POL-16 Q14/Q20/Q23; POL-05 A8; POL-08 E10/E11/E17). PRO-02, PRO-03 and PRO-04 consolidate them into one of each, **on approval**. Until the three policies are amended at their next revision to point at the procedures, the system carries two descriptions of the same arrangement — the condition this project has been bitten by four times. Queue POL-05 v1.2, POL-08 v1.2 and POL-16 v1.3 pointers with F63. | Medium | Later chat, with F63 |
| **F69** | **The quality objectives have no numbers anywhere in the three sources.** POL-16 ¶67 lists eight measures and ¶74(e) says objectives are set for the year from 1 September 2026; IMS-00 ¶33 and IMS-05 ¶8 repeat that "quality objectives are set". **No document states a target or a baseline for any of the eight, and no measure has been taken.** IMS-06 ¶16 records this and ¶18 proposes numbers. The statement "quality objectives exist" in IMS-00 and IMS-05 is true only in the sense that the measures are named, and should be softened at their next versions. | Medium | Later chat (IMS-00 v0.2, IMS-05 v0.2); Steve to set at the review |
| **F70** | **Mould and damp remediation has no recorded product list, waste streams or quantities anywhere in the system.** SESC-REG-10 EA-22 is drafted from the nature of the work as IMS-04 describes it and is flagged as the first row the Environmental Manager should confirm or rewrite. The trade is in the certification scope (D11) and the project COSHH register that would hold its products was committed for 31 August 2026 and does not exist. | Medium | Environmental Manager |

**Tasks by owner, from this chat:**

| Owner | Task | By |
|---|---|---|
| **Gary** | Open or confirm the PR for `workstream-5-reg09-compliance-obligations` (already pushed). Then branch from its tip — `git checkout -b workstream-6-core-procedures-reg10-ims06` carries today's working-tree changes across — and commit this chat's six new files, register v1.22, `CLAUDE.md` and `portal/actions.yaml`, **one commit per workstream if practicable (PRO-01…04 · REG-10 · IMS-06 · register/CLAUDE/actions), or one commit naming all three**. Do **not** add `Claude outputs/` (scratch, lock files). Check each file's MD5 against the completion note (§7.9). **Claude does not merge.** | this week |
| Gary | Render all six to branded PDF (install LibreOffice per §2n.1, or render in the container) and read the cover and a body page of each as images before any goes to James or Steve. **Until rendered and read, none is verified** (CLAUDE.md §9.4). | next chat, first task |
| Gary | Send James the six drafts **marked DRAFT and unsigned**, with IMS-00, IMS-04, IMS-05, REG-08, REG-09 if not already sent, via the Drive transfer folder (no personal data, no insurance documents, never this register) | after render |
| Gary | Batch B and Batch C drafting per §6 items 6b and 6c (one chat each, or as Gary directs) | following chats |
| Gary | Edit the Claude Project instructions §11: the waste carrier tier line (still says unconfirmed — carried from §2p); add D27 | this week |
| **Steve** | **Fix the date of the first management review in November 2026** and the four FS/insurance/calibration spend decisions the IMS-06 objectives flag (OB-Q4, OB-H2, OB-H6, OB-S1); decide D3 with PRO-02 ¶8 in front of him; approve or amend the PRO-02 Annex A programme | before the review |
| **Steve** | Sign IMS-04 (on F29–F31), then IMS-05, IMS-00, IMS-06, PRO-01 to PRO-04, REG-08, REG-09, REG-10 — in that order, each after Gary's review and the 5.4 consultation where it applies | 30 Nov 2026 (*proposed*) |
| **Craig** (Environmental Manager) | Confirm or revise every proposed score in SESC-REG-10, starting with EA-22; list the mould and damp products actually used (F70) | 30 Nov 2026 |
| Craig (Health and Safety Officer) | Put the audit programme (PRO-02 Annex A), the policy statement and the OH&S objectives (IMS-06 OB-H1–H6) to the first quarterly consultation meeting; record on SESC-FRM-08 | 30 Nov 2026 |
| James | Review the six drafts and IMS-00; comment, do not edit (they are controlled in the repository, not in the Drive folder) | per Steve's engagement |
| Later chat | IMS-00 v0.2: ¶30 (aspects register "cannot be written until…" — superseded by D27), ¶46 (PRO-01 now drafted), Part 10 (f), (i), (j), (o), (u) positions; IMS-05 v0.2 Part 6(h); POL-05/08/16 pointers (F68); F69 softening | with the next spine change |

**Completion note.** Six documents in one chat, at Gary's direction, against the one-workstream rule. The four procedures the certification body asks for first now exist as drafts that consolidate what three signed documents each said separately, and they say — with dates — what has not happened: no audit, no review since January 2023, no log, no live record. The aspects register exists for the first time as the Employer's own, with every score marked proposed and nothing communicated. IMS-06 gives the eight quality measures, three standing OH&S objectives and five environmental areas the numbers they never had, as proposals for Steve. The honesty convention held throughout: every passed date is recorded as overdue, no percentage is set against an unmeasured baseline, and nothing from James's templates or any other organisation entered the repository. Nothing was signed, committed, sent, rendered or merged.

---

## 2r. Batch B, first session — `SESC-PRO-05`, `SESC-PRO-06`, `SESC-PRO-07`, `SESC-REG-11` and `SESC-REG-12`, draft v0.1, 26 October 2026

**Taken:** §6 item 6b, Batch B, at Gary's choice of slice on 26 October 2026 — the three procedures that produce records first: supply chain (8.4; G13), competence (7.2, 7.3; G12) and incident reporting (POL-05 A24 with FRM-01/02). **Branch: stacked on the `workstream-6-core-procedures-reg10-ims06` tip at Gary's decision**, because the drafts cite PRO-01 to 04, REG-10 and IMS-06, which are pushed and not merged; the PR follows workstream 6's. The chat opened on Gary's `git status` in Terminal, run before any work: on `workstream-6-core-procedures-reg10-ims06`, up to date with origin, nothing modified, `Claude outputs/` untracked — which confirmed that the §2q task to commit the six workstream-6 files, register v1.22, `CLAUDE.md` and `portal/actions.yaml` was done and pushed (all six tracked; every hash matched the staged copies). **The §2q render-and-verify pass is not done and stays queued** (Gary: "I will go back to the workstream 6 render & verify pass later"). F64 unchanged: twelve tracked files and seven signed PDFs were iCloud placeholders; every file was staged through the bridge into the container, the chat worked on the copies, and the five new files plus the three changed ones are written back with the modification-time guard. `git log` through the bridge bus-errors on the placeholders; nothing was run against `.git` beyond a read of `HEAD` and `ls-files`. The `Signed/` folder was connected for this chat and the signed PDFs read from it, not from the TeraBox restore.

**Sources read, every page:** SESC-POL-05 v1.1 (32 pp), SESC-POL-06 v1.1 (6), SESC-POL-08 v1.1 (23), SESC-POL-10 v1.1 (10), SESC-POL-12 v1.1 (7), SESC-POL-14 v1.3 (13), SESC-POL-16 v1.2 (21), SESC-POL-17 v1.1 (22), SESC-POL-18 v1.1 (16), SESC-POL-19 v1.1 (39) — 189 pages, text-extracted with every page checked for content (the one empty page in each is the cover, read as an image for POL-05); the four form schemas FRM-01 to 04; IMS-00, 04, 05, 06; PRO-01 to 04; REG-05, 07, 09, 10; the three clause maps. **Not read:** SESC-REG-03 (not in `Signed/`); the Training Matrix (records store); the Approved Supplier Questionnaire (not held).

### 2r.1 What was drafted

| What | Where | Status |
|---|---|---|
| **`SESC-PRO-05` Purchasing and Control of Suppliers and Subcontractors, draft v0.1.** Consolidates POL-16 Q6/Q7, POL-05 A28, POL-08 E8, POL-17 §§1–3, 9, 10, POL-10 ¶¶15–20, POL-18 §1, POL-19 §19 and POL-12 into one procedure, unchanged, operating one register. The acceptance criteria are a table of citations to the signed paragraph and the FRM-04 field, not restated. Three criticality grades (critical / significant / routine) set evaluation depth, controls and re-evaluation interval (two years, from POL-08 ¶51(f) and POL-12 ¶17). Sanctions screening by the Accounts Manager before the Contracts Manager evaluates (POL-18 ¶9, ¶13). Eight outsourced processes tabled with where each is controlled (45001 8.1.4.3) — two providers not appointed, the adviser's engagement letter not held. The information given to suppliers (8.4.3) tabled, with the fact that the Supplier Code clause is not in the PO terms (REG-05 IP-12) stated, not hidden. Claims 9001 8.4.1–8.4.3; 45001 8.1.4.1–8.1.4.3; the externally-provided part of 14001 8.1. Owner: Contracts Manager. | `documents/SESC-PRO-05-purchasing-and-control-of-suppliers-and-subcontractors.md` | Drafted; no supplier evaluated; Steve to sign |
| **`SESC-REG-11` Approved Supplier and Contractor Register, draft v0.1 — issued EMPTY.** One register in place of the four lists six signed policies describe (F71), each name an alias. Categories carried unchanged from FRM-04; source categories from POL-17 Annex B; sixteen evidence types with where each is verified; a row schema; `suppliers: []` by design — no row without a dated FRM-04. Sole traders by `ST-nn` reference only (CLAUDE.md §8). Claims 9001 8.4.1 and 45001 8.1.4.2 *once a row exists*, and says the gap report is right to show 8.4 red until then. | `registers/approved-suppliers.yaml` | Drafted; empty; first row needs the first FRM-04 |
| **`SESC-PRO-06` Training, Competence and Awareness, draft v0.1.** Consolidates POL-05 A4, POL-16 Q5, POL-08 ¶¶70/88/90, POL-17 §§11–12, POL-18 §3, POL-19 §3, POL-14 ¶¶37–38, POL-10 ¶14(a)/¶26(a), POL-06 ¶32. Separates the three things the signed estate runs together: the *requirements* (REG-12, in git), the *evidence* (FRM-03 and the Training Matrix, in the records store), and the *currency check before allocation* (POL-16 ¶22; POL-05 ¶30). Induction content gathered from nine policies into one list (¶13). Effectiveness evaluated by FRM-03's own vocabulary — "attendance only" is not competence. Claims 7.2 and 7.3 of all three; not 5.4 (IMS-05), not 7.4 (Batch B, later). Owner: Contracts Manager. | `documents/SESC-PRO-06-training-competence-and-awareness.md` | Drafted; no induction or talk record exists; Steve to sign |
| **`SESC-REG-12` Competence Requirements Register, draft v0.1.** Forty-four requirements by role (CR-01 to CR-44), every one cited to the signed paragraph, scheme or REG-09 obligation that requires it. **No qualification, interval or scheme rule stated from memory**: where a signed document states an interval (manual handling three years, POL-05 ¶62; the annual refreshers) the row carries it; otherwise "to be read from the awarding body" (F75). Names no person; states no count beyond the signed twenty-two expired / twenty current at 16 August 2026. Records as a gap that nothing states what competence mould and damp remediation needs (CR-35) and lists twelve risk-assessed activities with no stated requirement (F73). Claims 7.2 as the maintained determination only. | `registers/competence-requirements.yaml` | Drafted; intervals to be entered; mould and damp row empty |
| **`SESC-PRO-07` Incident, Near Miss and Hazard Reporting and Investigation, draft v0.1.** Consolidates POL-05 A24/A25 ¶147, POL-08 E7 ¶38(e)/¶39, POL-06 ¶15(c), POL-12 ¶5(e)/¶6(f), POL-19 ¶¶49–53, with FRM-01, FRM-02, the accident book and REG-03 as one sequence ending at the FRM-05 under PRO-04 — the two procedures share 45001/14001 10.2 as the incident half and the corrective-action half, stated in both clause maps. Same-day reporting; site authority first on a customer or Government site; RIDDOR by the Health and Safety Officer with the Managing Director notified (the signed position — the draft FRM-02 says otherwise, F72); scene preservation; post-incident testing that cannot happen until a provider is appointed; investigation by PRO-04's method with the worker taking part; the A7 indicators counted and never published without a dated hours denominator. Three rules the signed documents do not contain are marked as the procedure's own (investigator independence; the Managing Director told the same day; the Accounts Manager notifies insurers). Claims 45001 10.2 and 14001 10.2; not 9001 10.2, not 6.1.2.1, not 8.2. | `documents/SESC-PRO-07-incident-near-miss-and-hazard-reporting-and-investigation.md` | Drafted; no record of any kind exists; Steve to sign |
| `CLAUDE.md` §5 next-free line: PRO-05, 06, 07, REG-11, REG-12 taken 26 Oct 2026; next free now `SESC-PRO-08` · `SESC-REG-13`. `portal/actions.yaml`: G12 and G13 detail updated (status **open** — drafted, no record); F71–F76 added; source line v1.23. Portal rebuilt: 31 pages, **28 controlled files**, 134 clauses, 94 actions. | `CLAUDE.md`, `portal/actions.yaml` | Done |

**Verification.** `build/validate.py` in the container against the staged tracked set plus the five new files: **28 controlled files, 134 clauses, 0 errors, 24 warnings (the standing unverified-14001 warning per file citing it), 8 notes. BUILD PASSES.** Both new YAML files re-parsed after every edit; paragraph numbering in each procedure checked as a continuous sequence by script; house-style words grepped (none). **An independent verification pass** was run by a second agent against every citation in the five drafts (about 650 checked): it found 19 defects — three wrong paragraph numbers (PRO-02 ¶7 not ¶8, three places), twelve attributions the source did not support or that overstated it (among them "same day" to the Managing Director, which POL-05 ¶8(e) does not say; the accident book "maintained" by the Health and Safety Officer, which ¶12 gives to the Accounts Manager; POL-12 ¶6(f)'s *immediately* softened to *the same day*; NEBOSH stated as a requirement at POL-05 ¶117 when it is only what Annex C records the adviser holds; the Gas Safe / NICEIC / MCS verification dated to POL-16 Annex C when the verifier and date are in POL-05 Annex C), three unsourced rules (the under-18 retention from the draft FRM-02 only; an invented LPG interval; the 27001:2013 rule cited to CLAUDE.md), and one internal contradiction. **All nineteen corrected**; where a rule is the procedure's own it now says so. **Not done: no branded render** (F62 applies; the §2q render pass is also still queued). Every written-back file's size and MD5 is in the completion note for Gary's check in Terminal (§7.9).

### 2r.2 Findings raised

| # | Finding | Severity | Owner |
|---|---|---|---|
| **F71** | **Six signed documents name the supplier list four different ways, and every one of them is empty**: Approved Contractor Register (POL-05 ¶159; POL-08 ¶52; POL-10 ¶16), list of approved and preferred suppliers (POL-16 ¶23), Supplier Authorisation Record (POL-17 Annex B), approved supplier list (POL-19 §19 Stage 2). SESC-REG-11 is drafted as all four with the names as aliases; the policies point at it at their next revision. Joins F63 and F68 as the pointer queue. | Medium | Chief Operating Officer, with F68 |
| **F72** | **SESC-FRM-02's `riddor_note` says the Managing Director makes the RIDDOR report; SESC-POL-05 ¶9(g) and ¶134 say the Health and Safety Officer makes it and ¶8(e) that the Managing Director is notified.** The signed policy governs and PRO-07 ¶16 follows it. The same form proposes retention to age 21 for an injured person under 18, which no signed document states. Both at FRM-02 v0.3, the second for Steve to confirm. | Medium | Chief Operating Officer; Steve for the retention |
| **F73** | **No signed document, scheme or product list states what competence mould and damp remediation needs** (REG-12 CR-35), although the trade is in the certification scope (D11) and its products and wastes are recorded nowhere (F70). And **twelve activities in the generic risk assessment library** — mobile towers, MEWPs, scaffolding, slinging, confined spaces, lead, PAT, harness inspection, temporary works, calibration, banksman, mould and damp — have **no stated competence requirement** anywhere. Each is to be stated from the issuing body, not invented. | High | Contracts Manager |
| **F74** | **The Approved Supplier Questionnaire** that POL-08 ¶51(a), POL-10 ¶16 and POL-12 ¶17 say a supplier completes **is not held in the three sources**; the one previously used was another organisation's (REG-05 IP-12). FRM-04 asks the evaluator, not the supplier. Decide: a supplier-facing form (next free FRM-09), or FRM-04 completed with the supplier. FRM-04 also lacks a *sub-contracted designer* category — FRM-04 v0.3. | Medium | Contracts Manager |
| **F75** | **No signed document states the renewal interval for most site qualifications** — CSCS, SSSTS/SMSTS, asbestos awareness, EFAW/FAW, abrasive wheels, fire awareness, harness, and the trade schemes' individual assessments. POL-05 ¶32 says "at the interval specified by the awarding body" and names none. REG-12 marks each *to be read from the awarding body*; nothing is entered from memory (CLAUDE.md §2). The Training Matrix presumably holds expiry dates per person; the *requirement* side needs the interval read from the body once. | Medium | Health and Safety Officer |
| **F76** | **Induction-record retention differs between signed documents**: POL-05 Annex B and POL-14 Annex C give engagement plus seven years; POL-17 ¶59 gives six years after leaving, and three years for superseded Training Matrix versions. The longer applies (PRO-01 ¶36; PRO-06 ¶26). Align at POL-17's next revision. | Low | Chief Operating Officer |

**Decisions reserved to Steve, raised by these drafts and not taken (stop rule):** which purchase-order and subcontract terms go out and the insertion of the Supplier Code clause (PRO-05 Part 8(d)); appointment and spend on the occupational health provider, the drug and alcohol testing provider and the retained adviser's engagement letter (PRO-05 Part 8(j); PRO-07 Part 8(g)); the training spend behind OB-H2 (PRO-06 Part 7(c)); the under-18 retention at F72; and the signatures.

**Tasks by owner, from this chat:**

| Owner | Task | By |
|---|---|---|
| **Gary** | Check the eight written-back files landed (`md5` in Terminal, §7.9 — hashes in the completion note); run `git status` and expect `CLAUDE.md`, `portal/actions.yaml`, `SESC-IMS-Master-Register.md` modified and five untracked files under `documents/` and `registers/`; then `git checkout -b workstream-7-batch-b-1-pro05-07-reg11-12` (carries the changes across) and commit — **one commit per procedure-and-register pair if practicable (PRO-05 + REG-11 · PRO-06 + REG-12 · PRO-07 · register/CLAUDE/actions), or one commit naming all**. Push; open the PR **after** the workstream-6 PR is merged, or mark it as stacked on it. Do **not** add `Claude outputs/`. **Claude does not merge.** | this week |
| Gary | The render-and-verify pass on **both** batches — the six §2q files and these five — as one chat, when chosen (F27/F34/F58 apply; F62: no LibreOffice on the MacBook, so the container renders) | next render chat |
| Gary | Batch B second session (operational control set: emergency preparedness 8.2 → POL-15; management of change 45001 8.1.3; plant, equipment, calibration and PAT with the log, 7.1.5, G11; driving and vehicles; RAMS by reference) and third session (performance set: 9.1 with the compliance evaluation method; 9.1.2 customer satisfaction with a feedback form, G15; 7.4 communication) | later chats |
| **Steve** | Sign PRO-05, PRO-06, PRO-07 and approve REG-11 and REG-12 after Gary's review and after IMS-04, 05, 00, 06 and PRO-01 to 04 (the order at §2q); decide the terms question at PRO-05 Part 8(d); the three appointments at Part 8(j) | 30 Nov 2026 (*proposed*) |
| **Craig** (Contracts Manager) | Evaluate on SESC-FRM-04 every current subcontractor and waste contractor, starting with the fifteen whose insurance records are held, and instruct the entry of each row on SESC-REG-11 (OB-E5; PRO-05 Part 8(a)); verify every carrier and facility on the Environment Agency register (Part 8(g)); provide the quarantine location and open the quarantine register (Part 8(h)) | 30 Nov 2026 |
| Craig (Health and Safety Officer) | Enter every "to be read from the awarding body" interval in SESC-REG-12 from the body's own documentation, with the date read (F75); state the mould and damp competence requirement with its source (F73); add the four missing Training Matrix rows (PRO-06 Part 7(d)); place the accident book at Unit 19 and every site (PRO-07 Part 8(a)); report the position against the 31 October 2026 renewal date (PRO-06 Part 7(c)) | 30 Nov 2026 |
| Accounts Manager | Produce the SESC-POL-18 Annex A Screening Record as it stands, so PRO-05 Part 8(c) and REG-11 can record what exists; the Article 28 contracts at PRO-05 Part 8(k) | 30 Nov 2026 (*proposed*) |
| Later chat | SESC-FRM-02 v0.3 (F72) and SESC-FRM-04 v0.3 (F74); SESC-REG-07 v0.2 to list PRO-05 to 07, REG-11 and REG-12 with the other drafts (PRO-01 Part 7(f)); SESC-IMS-00 v0.2 rows 7.2, 8.4 and 10.2 and Part 10 (l), (q) to point at these documents; read SESC-REG-03 against PRO-07 (Part 8(i)) | with the next spine change |

**Completion note.** Three procedures and two registers in one chat, on the slice Gary chose. Each procedure consolidates what six to ten signed policies each said separately, cites rather than restates, and ends in a records inventory that says — with dates — what does not exist: no supplier evaluated, no induction or talk recorded, no accident book placed, no report of any kind. The supplier register is issued empty on purpose, and says why. The competence register states no interval it has not read. An independent check of about 650 citations found nineteen defects and all were corrected, with the three rules that are the drafts' own now labelled as such. Nothing was taken from James's templates or from any other organisation's document. Nothing was signed, committed, sent, rendered or merged.

**Written-back files, for the `md5` check in Terminal (§7.9):**

| File | Bytes | MD5 |
|---|---|---|
| `documents/SESC-PRO-05-purchasing-and-control-of-suppliers-and-subcontractors.md` | 48646 | `7cfdea45e7549967b2b048778fd0c7dd` |
| `documents/SESC-PRO-06-training-competence-and-awareness.md` | 35439 | `1353d690c365568d53fb5c4156ffcac8` |
| `documents/SESC-PRO-07-incident-near-miss-and-hazard-reporting-and-investigation.md` | 35801 | `5736063355f7bbd806647759b3a52ede` |
| `registers/approved-suppliers.yaml` | 15965 | `38f7199d8871546490384586146d550c` |
| `registers/competence-requirements.yaml` | 42621 | `45b8078c9d6af138ebd6aa62b4064465` |
| `CLAUDE.md`, `portal/actions.yaml`, `SESC-IMS-Master-Register.md` | — | given in the chat after the final write |

---

## 2s. Three files received from a separate chat — `SESC-POL-20` filed and registered, the letterhead template filed, the bank letter declined, 27 October 2026

**What arrived.** Gary attached three files produced in a separate chat on 27 October 2026 and asked for them to be registered and filed. Every page of each was read before anything was done (POL-20: 11 of 11 pages, cover and body read as images; the bank letter: 1 page; the letterhead: the document, header, footer, comments part and metadata).

### 2s.1 What was filed, and where

| Item | Where it now sits | Bytes / SHA-256 | Status |
|---|---|---|---|
| **`SESC-POL-20` Anti-Bribery and Corruption Policy v1.0**, 11 pp, branded, Steve's signature image in the Approval block dated 03/03/2026, Simon Davies FCCA (Rapture Accounts Limited) named as the independent professional adviser. Cover bands it *JOSCAR 2 // Section 2.5*. | `~/Documents/SESC/ISO/Signed/SESC-POL-20 Anti-Bribery and Corruption Policy v1.0.pdf` — the same flattened folder and the same file-name pattern as POL-01…19 (`CLAUDE.md` §11). **Not in git**, like every other signed PDF. | 608,739 · `3914dc93…1a2d9` (identical to the file Gary attached) | **Filed and registered** — `registers/documents.yaml` (SESC-REG-07) row added; `CLAUDE.md` §5 next free policy now **`SESC-POL-21`** |
| **SESC Letterhead Template** (`.docx`): placeholder letter (date, recipient, subject, body at Arial 9.5 pt/1.15, sign-off), header with the Unit 19 address, telephone and web address, footer with the registered office, company number, VAT registration and UTR, one logo image, an empty comments part, no author metadata. | `~/Documents/SESC/ISO/Reference/Design/SESC Letterhead Template.docx`, beside `BRAND-SPEC.md` and the master logo (Gary's choice, 27 Oct 2026). Not a controlled document; no reference taken. | 115,154 · `540943f9…8c590` (identical) | **Filed; not registered as a controlled document** |
| **SESC Bank Details Confirmation Letter** (PDF, 1 page, dated 27 October 2026, ref `SESC/FIN/BANK-2026`, on the letterhead above, signature block for Steven A Coffen as Managing Director — unsigned). | **Nowhere in the three sources, by Gary's decision (27 Oct 2026).** It is a finance document carrying the Employer's bank account details; it is not an IMS artefact and does not belong in the ISO folder or in git. Its existence is recorded here; its contents are not. | — | **Declined; noted only** |

**Reference taken:** `SESC-POL-20`, the next free policy reference at `CLAUDE.md` §5 as at 26 October 2026. The 18 August decision not to use POL-20 for the scope document (§2, decision 1) is unaffected — the scope document is `SESC-IMS-04` and POL-20 is now a policy, which is what the series is for.

### 2s.2 What POL-20 v1.0 says, read against the house rules

It is a Bribery Act 2010 policy in 49 numbered paragraphs plus Annex A, a Gifts, Hospitality and Donations Declaration: statement and purpose; responsibilities; the four offences and the related Acts (Fraud Act 2006, POCA 2002, ECCTA 2023, Procurement Act 2023); definitions; gifts and hospitality with a £50 record / £100 prior-approval threshold and a Gifts and Hospitality Register kept by the Managing Director; facilitation payments and kickbacks; political and charitable donations (cross-referring to POL-09); third parties (POL-12); competition law and fraud (POL-04, POL-01, POL-02); the six Ministry of Justice principles; records (seven-year retention, "in line with POL-02 and POL-03"); training; what to do; reporting (POL-03 and Protect); non-compliance; review; approval. **House style:** "the Employer" throughout the body (defined at ¶1); the sole-director clause at ¶8 in the `CLAUDE.md` §4 wording, with "below" appended; numbered paragraphs; six-field control block on the cover and a seven-cell control table on page 3; *uncontrolled when printed* footer on every page; British English. **Honesty convention:** it names a Gifts and Hospitality Register, an annual risk assessment, induction issue and recorded annual briefings — **none of which exists as a record on 27 October 2026** — and, unlike the drafts in `documents/`, it carries **no "Records held, records not yet held" section**. That is the convention for the signed estate of 12–16 August, which pre-dates the rule; it is recorded, not rewritten. No clause is claimed for POL-20 (`clause_map: pending`, like POL-01…19): a clause map is drawn from the text when the document is migrated, never from its title.

### 2s.3 Findings raised

| # | Finding | Severity | Owner |
|---|---|---|---|
| **F77** | **`SESC-POL-20` v1.0 is signed, and its dates do not agree with one another.** The cover's *Revision date* and the page-3 *Issue date* both read **03 March 2027**; *Next review* also reads **03 March 2027** (the same day — the validator's own rule is review after issue, at most twelve months); the Approval block is signed and dated **03/03/2026**; and the file was produced on 27 October 2026. The document cannot be reconciled from its own text. Which date is right is Steve's to say, and the correction is a **v1.1 reissue on his instruction** — not a chat's edit of a signed PDF (`CLAUDE.md` §2). Until then the register row carries `issued: null` and the defect. | **High** — a signed document that misstates its own issue date is the version drift `CLAUDE.md` §5 exists to prevent | Gary, to put to Steve |
| **F78** | **Export artefacts left in the signed PDF.** The contents page (p. 2) lists eighteen headings with **no page numbers** and carries the authoring instruction *"Page numbers update on refresh — select all and press F9"*; the registered-office line on p. 3 sits above the control table as an unstyled line. Cosmetic, but it is in the signed artefact. Take it at v1.1 with F77; add "refresh fields before export" to the renderer checklist if the branded policies are ever rebuilt from `.docx`. | Medium | Gary, with F77 |
| **F79** | **POL-20 routes its reporting through a document the estate does not hold as signed text.** ¶40(d) and ¶42 send reports "through the confidential routes in the Whistleblowing (Speak Up) Policy (SESC-POL-03)", and ¶37 ties retention to POL-02 and POL-03. The file named POL-03 in `Signed/` contains POL-01 (F60). POL-20's pointer is correct in intent and dangling in fact until F60 is closed. Joins F60. | Low | Chief Operating Officer, with F60 |
| **F80** | **The letterhead footer prints the Employer's UTR** alongside the company number and VAT registration. The company number and registered office are required on business letters (Companies Act 2006 s.82 and the 2015 Regulations) and the VAT number on invoices; the UTR is a tax identifier that is not required on either and is routinely asked for by fraudsters to impersonate a company to HMRC. Whether to keep it on every outgoing letter is Gary's call, then Steve's; it is a brand-asset question, not an IMS one, so recorded here once and not carried to `portal/actions.yaml`. | Low | Gary |

**Not done, deliberately.** No file was renamed, moved or deleted. No signed PDF was edited. The bank letter was not filed anywhere and its account details appear in no file in the three sources. No `git` command was run against the clone through the bridge (a read-only `git status` through the mount faulted with a bus error — F64 territory; run it in Terminal). Nothing was signed, committed, sent, rendered or merged. `SESC-IMS-00` and the `Signed/` PDFs of POL-01…19 are untouched.

**Tasks by owner, from this chat:**

| Owner | Task | By |
|---|---|---|
| **Gary** | In Terminal: `shasum -a 256 "$HOME/Documents/SESC/ISO/Signed/SESC-POL-20 Anti-Bribery and Corruption Policy v1.0.pdf"` and expect `3914dc93fa0a00cfa739e7b45988bd4af6f4a15372956756dd1c2dd1eea1a2d9`; `git status` in `CLAUDE ISO` and expect **four** modified tracked files — `CLAUDE.md`, `SESC-IMS-Master-Register.md`, `registers/documents.yaml`, `portal/actions.yaml` — and nothing untracked (the two filed files are outside the clone). Commit on a branch (`chore/pol-20-filed-27-oct`) and open the PR; **Claude does not merge.** | this week |
| **Gary** | Put F77 to Steve: which of 03/03/2026 and 03 March 2027 is the issue date, and is 2027 the review date. Record the answer here (the next free decision number when taken — ~~D28~~, which was taken on 4 November 2026 for fire doors, §2t). | before POL-20 is sent to anyone |
| **Steve** | Instruct the v1.1 reissue of POL-20 correcting the dates (F77) and the contents page (F78); re-sign. Decide F80 if Gary raises it. | *proposed* 30 Nov 2026 |
| **Gary** | Decide where the bank details letter lives (finance, not ISO) and whether a copy on the Drive is wanted; nothing here depends on it. | when convenient |
| Later chat | When POL-20 is migrated into `documents/` with POL-01…19, draw its clause map from the text (candidates to test, not to assume: 9001 5.1.1, 7.3, 8.4; 45001 5.4 on the reporting route) and add the "Records held, records not yet held" section. | migration workstream |

**Completion note.** One signed policy filed where the other twenty-one sit and registered without a clause claimed; one brand asset filed beside the brand spec; one finance letter read and deliberately kept out. The policy's dates contradict each other on its own cover, which is the one thing a certification body reads first on a controlled document, so F77 goes to Steve before the document goes anywhere else.

---

## 2t. Workstream — the Fire Door Installation Record Pack, draft v0.1, 4 November 2026

**Taken:** the whole of Gary's handoff `HANDOFF-FD-001` (dated 4 November 2026: a fire door service line — installation, remedial work and planned maintenance — and a QinetiQ instruction, reported by Gary and not held in the three sources, to install three fire doors at MOD Boscombe Down). One workstream, one branch `fire-door-record-pack`. **Gary's decisions in the chat, 4 November 2026:** the ten references proposed were accepted ("Yes, build it"); the pack is built as YAML schemas and Markdown with generated `.docx` forms and a generated `.xlsx` register, not hand-built Office files; and **this Windows PC is the working machine from today — Git, Python 3.12 and LibreOffice were installed on it at Gary's instruction and `GaryHill0985/QMS` was cloned to `C:\Users\Admin\Desktop\QMS`** (F84 on what that does to `CLAUDE.md` §11).

**The decision this workstream turns on — D28.** D11 (24 September 2026) put fire doors *out* of the scope as "not a trade SESC sells" (§2f, §2i.3). The handoff makes them a trade. D28 is raised for Steve: fire door installation, remedial repair and maintenance are inside the scope. It is drafted at `SESC-IMS-04` v0.4 ¶7, ¶14 and ¶16(c)–(d) and is formal only on his signature; nothing is installed under `SESC-PRO-08` before then. **The next free decision number was pencilled at §2s for the F77 answer; that row now says "next free when taken", because D28 is this.**

### 2t.1 What was drafted

| Reference | Title | What it is |
|---|---|---|
| `SESC-PRO-08` v0.1 | Fire Door Installation | The procedure: five hold points, nine photographs per door, the one wording for the basis of installation (¶6: *installed in accordance with BS 8214 and the doorset manufacturer's installation instructions, using components matching the doorset's test evidence, by trained operatives under SESC supervision*), the no-certification rule (¶7), the client's written acceptance of that basis before work (¶10, hold point 1), the rating taken from the client (¶11), gap tolerances read from the manufacturer onto the form and never printed (¶26), gauges under 7.1.5.1 (¶25), release (¶29), handover (¶30), the register (¶34), nonconformity (Part 5). Claims 9001 8.1, 8.5.1, 8.5.2, 8.5.5, 8.6, 8.7, 7.1.5.1 and 14001 8.1 — **the first clause 8.5 claims in the system.** Not 7.2, 8.2, 8.4, 10.2; no 45001 clause. Sixteen pages rendered. |
| `SESC-FRM-09` to `SESC-FRM-14` v0.1 | Pre-Installation Survey · Product Evidence Record · Installation Checklist and Gap Record · Installation Completion Certificate · Handover and Maintenance Schedule · Operative Authorisation Record | Schemas in `forms/`, in the FRM-01…08 shape (every field type one `export_forms.py` accepts; `correction_of` on each) plus `section`, `photo_stage` and a `print` block that the new form renderer reads. FRM-11 carries the ten gap measurements, five manufacturer-tolerance boxes with their source, and photographs S02–S09. FRM-12 prints the ¶6 statement and the ¶7 note verbatim. FRM-14 names a person and its completed record is marked personal data for the records store. |
| `SESC-REG-13` v0.1 | Fire Door Asset and Install Register | `registers/fire-door-assets.yaml`: thirty columns, each keyed to the `fire_door_assets` column it becomes in the SESC Platform (D20). **Issued empty.** Claims 8.5.2 only, and only once a row exists. The working register with rows lives in the records store, written from the columns by `build/export_fire_door_register.py`. |
| `SESC-WI-02` v0.1 | Fire Door Record Pack | The "which form when" sheet, two pages, held by document ID rather than as a README in a folder (`CLAUDE.md` §5 "file by ID, never by folder"). Handoff acceptance criterion 5. |
| `SESC-TPL-05` v0.1 | Fire Door Installation Basis Confirmation | The email asking the client to confirm competent installation without third-party certification is acceptable. **Steve sends it** (a statement to a customer, `CLAUDE.md` §12.1). Claims 8.2.1. |
| `SESC-IMS-04` v0.4 | Context of the Organisation | D28 at ¶7, ¶14, ¶16 lead, new ¶16(c)–(d); Part 8(b) updated and re-dated; new Part 8(w) (insurance response to fire door work, F83) and (x) (REG-09 rows for the trade). No renumbering: ¶58 and every other cited paragraph keeps its number. Typed footer updated to v0.4. The two test expectations that pin IMS-04's version and revision date were moved to v0.4 / 4 November 2026. |
| `SESC-REG-12` v0.2 | Competence Requirements Register | New section G, CR-45 to CR-48, and the role `operative_fire_door`. **No course, awarding body, scheme card or interval is named, because none has been read;** CR-47 is a gap on that point and CR-48 states the responsible person's competence only as a role. The scheme's requirements (the Approved-Person shape the handoff describes) are entered when the scheme document is held — `SESC-PRO-08` Part 7(j). |
| `build/render_form.py` | — | Prints any FRM schema as a branded A4 form: control line, header and footer from the front matter, sections, tick boxes for selects, photograph prompts with the file-name pattern, the gap table. `--pdf` through LibreOffice. The YAML stays the source. |
| `build/export_fire_door_register.py` | — | Writes the working REG-13 workbook: Register sheet with the header locked and the data rows unlocked, select columns validated, Columns and About sheets locked; `--check` compares the header row with the YAML. |
| `build/render_docx.py`, `build/build_portal.py`, `build/workspace_forms/README.md`, `CLAUDE.md` §5, `portal/actions.yaml` | — | Windows fixes (F81); the FRM-09…14 row in the runbook; the next-free line (now `SESC-PRO-09` · `SESC-WI-03` · `SESC-REG-14` · `SESC-FRM-15` · `SESC-TPL-06`); D28, F81–F84, source line v1.25. |

**Wording rules from the handoff, applied everywhere:** no statement or implication of BM TRADA, Q-Mark, FIRAS or any third-party certification; the ¶6 wording and no other; tolerances as fields from manufacturer data, never limits in a document; UK English.

### 2t.2 Verification

`build/validate.py`: 38 controlled files, **0 errors**, 26 warnings (all the expected 14001 `verified: false`), BUILD PASSES. `build/workspace_forms/export_forms.py`: 14 forms accepted. `build/test_render_docx.py`: **25/25 pass** after the Windows font fix and the two IMS-04 expectation updates; the two PDF-numbering tests skip because `pdftotext` is not on this machine. `build/render_docx.py --pdf`: PRO-08 (16 pp), WI-02 (6 pp), TPL-05, IMS-04 v0.4 rendered with LibreOffice. `build/render_form.py --pdf`: six forms rendered (FRM-11 is 6 pp). `build/export_fire_door_register.py --check`: 30 columns match. `build/build_portal.py`: 31 pages, 38 controlled files, 101 actions. **Read as images at 90 dpi:** PRO-08 cover, control page, pp 6, 10 and 14; FRM-11 pp 1 and 4 (the gap table), FRM-12 p 1 (the statement callout and the no-certification note), FRM-09 p 1, FRM-13 p 2, WI-02 p 3. Cover, control block, headers, footers, numbering, tables, tick boxes and the gap table all read correctly. **PRO-06 does not render (F82).**

### 2t.3 Findings raised

| # | Finding | Severity | Owner |
|---|---|---|---|
| **F81** | **The build did not run on Windows.** `render_docx.py` `_font_for()` listed Linux and macOS font paths only (the cover's own list had Windows); `soffice()` did not look in Program Files; `to_pdf()` built a malformed `file://` profile URI; `build_portal.py` used `%-d`, which is glibc/macOS only. All fixed in this PR; the renderer tests and the portal build pass on Windows. **Closed.** | Medium | Closed |
| **F82** | **`SESC-PRO-06` v0.1 will not render:** the Part 6 records table at ¶25 has a first-column cell beginning *Signed induction sheets*, which `SIG_LABELS` matches, so the renderer refuses the draft. Same root cause as F58 (the guard matches header rows and ordinary cells). Fix the guard with a test, or reword the cell at PRO-06 v0.2. Found when PRO-06 was used to prove the renderer on this machine. **CLOSED 5 Nov 2026 (§2u): the guard fixed with three tests; PRO-06 rendered and read; the cell is unchanged.** | Medium | **Closed** |
| **F83** | **The liability business description does not name fire door work.** The broker's letter of 6 August 2026 and the PI Statement of Fact name neither fire door installation nor maintenance (IMS-04 ¶16(a), ¶16(d)). Written confirmation that EL, PL and PI respond to the trade is required before the first door is installed (IMS-04 v0.4 Part 8(w); PRO-08 Part 7(f)). The F30 pattern again. A statement to an insurer, so Steve's. | **High** | Steve |
| **F84** | **Two clones now exist, and `CLAUDE.md` §11 names only one.** From 4 November 2026 Gary works from the Windows PC: Git 2.56, Python 3.12.10, LibreOffice and the build's packages installed; the repository cloned to `C:\Users\Admin\Desktop\QMS` from `main` at `36573a2` (identical to GitHub, so nothing from the MacBook was needed). §11 still says the MacBook clone at `~/Documents/SESC/ISO/CLAUDE ISO/` is the master and §11's command guidance is zsh. §7.7 (one session per clone) now has two clones to police. **Gary's decision, not a chat's:** which clone is the master, whether the MacBook clone is retired or kept as a pull-only mirror, and whether `Reference/`, `Signed/` and `Insurance/` are copied beside the Windows clone (they are not here — nothing in this workstream needed them). The `Fire Door/` folder holding the handoff sits **untracked** inside the clone; decide where it lives.<br><br>**5 Nov 2026 — the signing-key half is closed; the clone question stays open.** A key was generated on the PC and registered on GitHub (D4 for the fingerprint); the workstream commit `549931c` is signed and shows **Verified** on GitHub. Two things found on the way, recorded so the next chat does not rediscover them: **(1)** the first key pair, made with a passphrase, was rejected on every attempt to sign with it and was discarded; the key in use **has no passphrase** — the Windows `ssh-agent` service is Disabled on this PC, so a passphrase would prompt on every commit, which is the §2b trade-off again (F14). **(2)** the Windows-supplied OpenSSH client (`C:\Windows\System32\OpenSSH`, 9.5p2) cannot negotiate with GitHub (*unsupported KEX method sntrup761x25519*), so the repository's `core.sshCommand` points at Git for Windows' own client (`C:\PROGRA~1\Git\usr\bin\ssh.exe`, 10.6p1) with this key; GitHub's host key was written to `known_hosts` after its fingerprint was checked against the one GitHub publishes.<br><br>**5 Nov 2026 — CLOSED (§2w).** Gary's decisions: the PC clone is the master and the MacBook clone is retired; `Reference\`, `Signed\` and `Insurance\` go to `C:\Users\Admin\Documents\SESC\ISO\` (to be copied from the MacBook); `Fire Door\` stays untracked in the clone. `CLAUDE.md` §2, §9 and §11 amended. | Medium | **Closed** |

### 2t.4 Tasks by owner

| Owner | Task | By |
|---|---|---|
| **Gary** | ~~**Signing key and the PR.** In PowerShell on this PC, interactively, one command per block: `ssh-keygen -t ed25519 -C "garyadamhill@outlook.com" -f "$HOME\.ssh\id_ed25519_sesc_win"` (with a passphrase); add the public key to GitHub as **both** an Authentication key and a Signing key; then `git config gpg.format ssh`, `git config user.signingkey "$HOME\.ssh\id_ed25519_sesc_win.pub"`, `git config commit.gpgsign true`, `git remote set-url origin git@github.com:GaryHill0985/QMS.git`. Then commit the branch `fire-door-record-pack` as one workstream commit and open the PR. Record the new key's fingerprint at D4.~~ **Done 5 Nov 2026** — key generated (no passphrase, see F84 and F14), registered on GitHub as both key types, fingerprint at D4; `549931c` committed, signed, pushed and Verified; PR opened (§2t.5). **Claude does not merge.** | ~~this week~~ done |
| **Gary** | Put **D28** to Steve, with IMS-04 v0.4 ¶16(c)–(d) and PRO-08 ¶6–¶7 in front of him; his signature on v0.4 makes it formal. | before any survey |
| **Steve** | D28; **F83** — written confirmation from the broker/insurer that EL, PL and PI respond to fire door installation, remedial repair and maintenance; buy **BS 8214** (PRO-08 Part 7(h)); send the **TPL-05** email to QinetiQ and file the reply (hold point 1); approve PRO-08, FRM-09…14, REG-13, WI-02, TPL-05, IMS-04 v0.4, REG-12 v0.2. | before the first installation; *proposed* 30 Nov 2026 |
| **Gary** | Supply the handoff §9 items — QinetiQ job number, PO, site contact, the three door IDs and locations, the doorset supplier and rating, install dates and operatives. **They go on the forms and the working register, not into git.** | before the survey |
| **Contracts Manager** | REG-09 rows for the trade, each instrument read on its issuing body (PRO-08 Part 7(g); IMS-04 Part 8(x)); the REG-10 aspect row for fire door waste (Part 7(i)); state from the awarding body what external qualification, if any, CR-47 needs; the first FRM-14 authorisations; a numbered gap gauge checked against a steel rule (¶25). | *proposed* 30 Nov 2026; before the first survey |
| **Gary** | ~~**F84:** decide which clone is the master and amend `CLAUDE.md` §11 and §7.7 by PR; decide where `Fire Door/HANDOFF-FD-001…md` lives (suggest `Reference/Decisions/` beside the other briefs, outside the clone).~~ **Decided 5 Nov 2026 (§2w)**; the `CLAUDE.md` amendment is in the §2w PR. | ~~next chat~~ done |
| **Gary** | Decide whether FRM-09…14 are also built as Workspace forms (the exporter accepts them; the photo fields would be NOT CREATED) or stay printed/tablet until the Platform (`build/workspace_forms/README.md` §1). | before go-live |
| ~~Later chat~~ | ~~F82/F58: make the signature guard skip header rows and ordinary cells, with a test;~~ **done 5 Nov 2026 (§2u)**; then the queued §2q/§2r render pass, **which now also needs F85 fixed first**. | next renderer chat |
| Later chat | **Phase 2 of the handoff:** inspection (PPM) and remedial repair records, after the first handover (PRO-08 Part 7(n)); the Platform's `fire_door_assets` table from REG-13's keys (workstream 1c, D20). | after the first job |

**Not done, deliberately.** Nothing signed, merged or sent. ~~No commit yet, because the ruleset requires signed commits and no signing key exists on this PC (F84).~~ *(Committed and pushed 5 Nov 2026 — §2t.5.)* No REG-09 or REG-10 row written, because each instrument is to be read on its issuing body first and that is the Contracts Manager's. No gap tolerance, fixing spacing, inspection interval, course, scheme rule or qualification stated anywhere, because none has been read. The QinetiQ instruction is reported, not cited. The MacBook was not touched.

**Completion note.** The pack exists, validates, renders and has been read. A door can be recorded end to end on FRM-09, FRM-10, FRM-11 and FRM-12 with nine photographs, handed over on FRM-13 and entered on REG-13, by an operative authorised on FRM-14, with no form carrying a figure that belongs to the manufacturer and no document implying a certification the Employer does not hold. **What it waits on is Steve: D28 and his signature on IMS-04 v0.4, the insurer's answer (F83), the TPL-05 email, and BS 8214 on the shelf.**

### 2t.5 Committed, pushed and put up for review — 5 November 2026

Gary's choice in the chat: *key first, then commit.* The sequence, so that the next chat has it: `.ssh` did not exist on the PC; a first ed25519 key pair with a passphrase was generated in the terminal, and every attempt to sign with it was refused as *incorrect passphrase* — it was moved out of `.ssh` and not used; a second pair was generated **without a passphrase** (the Windows `ssh-agent` service is Disabled, so a passphrase would prompt on every commit — the §2b trade-off, recorded at F14 and F84). Gary added the public key to GitHub as both an Authentication key and a Signing key and made `garyadamhill@outlook.com` the verified primary address on the account, so the commit identity set at §2t matches. The branch's one workstream commit, **`549931c`**, carries the 21 files (3,585 insertions, 29 deletions), an SSH signature, and author and committer `Gary Adam Hill <garyadamhill@outlook.com>`; pushed to `origin/fire-door-record-pack`; **the GitHub API reports `verification.verified: true, reason: valid`.** The Windows OpenSSH client could not reach GitHub (F84 (2)), so git on this clone uses Git for Windows' bundled client. The GitHub CLI was installed at the same time, because neither `gh` nor a browser connection was available to open the pull request from this PC. **The pull request is **PR #20** (`github.com/GaryHill0985/QMS/pull/20`), `fire-door-record-pack` → `main`, reviewer Gary, approver Steve; Claude does not merge.** This register row and the matching `portal/actions.yaml` line are the second commit on the branch.

**Merged, 5 November 2026.** PR #20 was merged into `main` by Gary as **`fc225da`** (GitHub's merge commit; signed by GitHub and reported Verified) after his review and — **as reported by Gary in the chat** — Steve's approval. **No review is recorded on the pull request itself,** so Steve's approval of the PR is held only as Gary's report; if it was given in writing, file it. **Merging issued nothing:** every document in the pack stays draft v0.1 on `main`, D28 is formal only on Steve's signature on IMS-04 v0.4, and nothing is installed under PRO-08 before that signature, the insurer's answer (F83) and the client's reply to the TPL-05 email. The merged branch was deleted on GitHub and in the clone; the clone's `main` is at `fc225da`. Claude did not merge. The F82/F58 renderer fix was handed to a separate session the same day, on its own branch, and will be registered when it comes back as a PR.

---

## 2u. Renderer — the signature guard fixed, F58 and F82 closed, `SESC-PRO-06` rendered, 5 November 2026

A side session started from the §2t chat, on the branch `claude/reverent-chandrasekhar-c65259`, cut from
`fire-door-record-pack` because the Windows fixes of F81 were only there. While it ran, Gary merged PR #20 as
`fc225da` and PR #21 took this register to v1.27, so `origin/main` was merged into the branch and this
workstream is v1.28. **PR #22** (`github.com/GaryHill0985/QMS/pull/22`), `claude/reverent-chandrasekhar-c65259` → `main`.
One change to the renderer and its tests; **no document content changed; nothing signed or merged.**

### 2u.1 What changed

| File | Change |
|---|---|
| `build/render_docx.py` | **The guard was a prefix match on every first-column cell of every table.** `strip_md(r[0]).lower().startswith(SIG_LABELS)` matched a content table's header *Signed statement* (F58) and the Part 6 records cell *Signed induction sheets; certificates and cards; …* (F82) as signature rows, and refused the draft because their other cells held text. Now a new `is_signature_label()` matches only when the **whole** label, stripped of markdown, case and a trailing colon, is `Signature` or `Signed`, and `table()` applies it only in a **label/value table** (the empty-header form the approval block uses) — a header row of a content table, and any body cell that merely begins with the word, is an ordinary cell. The guard itself is unchanged: a filled signature cell in the approval block on anything other than an approved document still raises `SignatureError`, and the renderer still never fills one. `find_signature_table()` (trap 2) uses the same test and skips rows marked `w:tblHeader`, so a content table headed *Signature* can never be mistaken for the approval table. |
| `build/test_render_docx.py` | Three tests in `TestFixture`: `test_guard_refuses_filled_approval_signature_cell` (a filled approval-block cell is refused under four spellings of the label); `test_guard_accepts_header_row_containing_signature` (a content table whose header row begins *Signature* / *Signed statement* renders on a draft, and `find_signature_table()` still returns the approval table); `test_guard_accepts_body_cell_beginning_signed` (the PRO-06 ¶25 cell, verbatim, renders). Both "accepts" tests were run against the old guard first and both failed with `SignatureError`, so they test the defect and not themselves. |

### 2u.2 Verification

`build/render_docx.py --pdf` on `documents/SESC-PRO-06-training-competence-and-awareness.md`: **renders, 13 pages**, DOCX and PDF, with LibreOffice on the Windows PC. **Read as images at 90 dpi** (pymupdf): p. 1 cover (PROCEDURE band, title, the six-field control block reading `SESC-PRO-06` · `0.1 — DRAFT, NOT ISSUED` · `26 October 2026` · *Not yet approved (Managing Director)*), p. 2 contents, p. 9 (Part 6, the ¶25 records table with the *Signed induction sheets* row printed as an ordinary row), p. 12 (Part 8 approval block: *Signature* row empty, *Reviewed by* and every *Date* empty, the adviser row filled from the front matter). Header, footer and *uncontrolled when printed* present on every page read. `build/validate.py` and the full `build/test_render_docx.py` were run after the change; the results are in the revision-history row for v1.27 and the completion note. **One defect seen on p. 9 is not this change's and is recorded as F85 below.** `build/validate.py`: 38 controlled files, 0 errors, 26 warnings (the standing 14001 `verified: false`), 8 notes, BUILD PASSES. `build/test_render_docx.py` from PowerShell: **28 run, OK, 2 skipped** (the two PDF-numbering tests, `pdftotext` absent). Run from Git Bash the same two tests ERROR instead of skipping: Git for Windows ships an xpdf `pdftotext` 4.06 at `/ucrt64/bin` that `shutil.which()` finds and that has no `-bbox` option (poppler's). On this PC run the tests from PowerShell; noted here, not raised as a finding.

### 2u.3 Findings raised

| # | Finding | Severity | Owner |
|---|---|---|---|
| **F85** | **A table that starts on the numbered-paragraph line prints without its header.** All seven §2q/§2r procedures open their tables as `25. \| Record \| What it is \| Where \| Who holds it \|` — the header row on the same line as the paragraph number, the `\|---\|` line and the body rows indented beneath it. `parse_blocks()` reads that first line as the paragraph's text and the indented lines as a table, so on PRO-06 p. 9 the header prints as the literal text *\| Record \| What it is \| Where \| Who holds it \|* after "25." and the first data row (*SESC-REG-12 Competence Requirements Register …*) is styled as the black header row. **Fourteen tables in seven files:** PRO-01 (3), PRO-02 (2), PRO-03 (2), PRO-04 (2), PRO-05 (1), PRO-06 (2), PRO-07 (2); IMS-00, IMS-04, IMS-05 and IMS-06 do not use the form. Seen in passing while reading PRO-06; not fixed here because it is a parser change with its own test, not the guard. Fix in the renderer (treat a numbered line whose text begins with `\|` as the table's header row) rather than in fourteen documents, then the queued §2q/§2r render pass. **CLOSED 5 Nov 2026 (§2v):** fixed in `parse_blocks()` with a fixture test; PRO-06 and PRO-01 rendered and the affected pages read as images. | Medium | **Closed** |

### 2u.4 Tasks by owner

| Owner | Task | By |
|---|---|---|
| ~~**Gary**~~ | ~~Review and merge **PR #22** (two build files, this register, `portal/actions.yaml`).~~ **Merged by Gary as `bfcef71`, 5 Nov 2026 (GitHub shows PR #22 MERGED; no review is recorded on GitHub).** | done |
| Later chat | ~~**F85** in `render_docx.py` with a test~~ **done 5 Nov 2026 (§2v)**; then the queued §2q/§2r render pass (F27/F34 apply; F58, F82 and F85 no longer do). | next renderer chat |

---

## 2v. Renderer — F85 fixed: a table whose header row sits on the numbered-paragraph line, 5 November 2026

A side session started from the §2t chat, on the branch `claude/clever-bose-7889cc`, cut from `main` at
`bfcef71` after Gary had merged PR #22 (the branch carries no other open work). **PR #23**
(`github.com/GaryHill0985/QMS/pull/23`), `claude/clever-bose-7889cc` → `main`. One change to the renderer's
parser and one test; **no document content changed; nothing signed or merged.**

### 2v.1 What changed

| File | Change |
|---|---|
| `build/render_docx.py` | **`parse_blocks()` read a numbered line whose text is a table row as the paragraph's text.** The seven §2q/§2r procedures open fourteen tables as `25. \| Record \| What it is \| Where \| Who holds it \|`, with the `\|---\|` line and the body rows indented beneath, so the header printed as literal text after the number and the first data row was styled as the black header row (F85). Now a numbered line whose text begins with `\|` yields two blocks: a `num` block with the source's number and no text, so the number still prints as its own paragraph and is still checked against the source (F27/F34), and an indented `table` block whose first row is that line — the header — followed by the indented rows. The pipe-row parsing is shared with the ordinary table branch through a new `_table_rows()`. A numbered line that does not begin with `\|` is parsed exactly as before. |
| `build/test_render_docx.py` | One test in `TestFixture`, `test_table_header_on_numbered_line`: the fixture's first paragraph becomes `1. \| Column \| Other \|` with the rule and the body row beneath; the DOCX must print `1.`, `2.`, `(a)`, `(b)` equal to the source, carry no `\|` in any paragraph, and have table 1's first row as a `w:tblHeader` row reading *Column · Other* with *a · b* as an ordinary row beneath. **Run against the old parser first it failed** with the paragraph text `1.\t\| Column \| Other \|`, so it tests the defect and not itself. |

### 2v.2 Verification

A parse check over all seven procedures: **fourteen tables** found in the form, exactly the count at F85 — PRO-01 ¶6, ¶32, ¶38; PRO-02 ¶6, ¶28; PRO-03 ¶6, ¶21; PRO-04 ¶6, ¶24; PRO-05 ¶6; PRO-06 ¶6, ¶25; PRO-07 ¶6, ¶29 — each parsed as a bare number followed by a table whose first row is the source's header row, and no block text anywhere carrying a pipe. `build/render_docx.py --pdf` on **`SESC-PRO-06`** (13 pp) and **`SESC-PRO-01`** (13 pp) with LibreOffice on the Windows PC; the DOCX paragraph numbers of both equal the source (46 and 53 labels). **Read as images at 90 dpi** (pymupdf): PRO-06 p. 1 cover (PROCEDURE band, control block `SESC-PRO-06` · `0.1 — DRAFT, NOT ISSUED` · `26 October 2026` · *Not yet approved (Managing Director)*), p. 4 (¶6, black header row ROLE · IN THIS PROCEDURE), p. 9 (¶25, black header row RECORD · WHAT IT IS · WHERE · WHO HOLDS IT, *SESC-REG-12 Competence Requirements Register* now an ordinary first row, the *Signed induction sheets* row ordinary, "25." printed above the table at the number position); PRO-01 p. 4 (¶6), p. 8 (¶32, RECORD TYPE · WHERE · WHY), p. 9 (¶38, STAGE · WHO · CONTROL · RECORD) and p. 10, where the ¶38 table continues and the header row repeats at the top of the page, which is the `w:tblHeader` mark doing its job. No literal pipe text on any page of either PDF. Header, footer and *uncontrolled when printed* present on every page read. `build/validate.py`: 38 controlled files, 0 errors, 26 warnings (the standing 14001 `verified: false`), 8 notes, BUILD PASSES. `build/test_render_docx.py` from PowerShell: **29 run, OK, 2 skipped** (the two PDF-numbering tests; poppler `pdftotext` absent on this PC, as §2u.2 records).

**One limit of the checks, noted and not raised as a finding.** The number of such a table now prints on a line of its own with nothing beside it. The DOCX-level numbering test counts it; the PDF-level check `pdf_numbers()` in the test file counts a number only when text sits beside it at the hanging indent (that is how it tells a paragraph number from the same characters in a table cell), so it would not count these fourteen if it were ever run on the procedures. Today it runs only on `SESC-IMS-04` and `SESC-IMS-05`, which do not use the form. If the PDF test is extended to the procedures, teach `pdf_numbers()` the bare-number line first.

### 2v.3 Findings raised

None. F85 closed (§2u.3, §5).

### 2v.4 Tasks by owner

| Owner | Task | By |
|---|---|---|
| **Gary** | Review and merge **PR #23** (two build files, this register, `portal/actions.yaml`). **Claude does not merge.** | this week |
| Later chat | The queued §2q/§2r render pass: PRO-02, PRO-03, PRO-04, PRO-05, PRO-07, REG-10, REG-11, REG-12 and IMS-06 rendered to PDF and read as images (F27/F34 apply; F58, F82 and F85 no longer do). | next renderer chat |

---

## 2w. The Windows PC becomes the master; F84 closed, 5 November 2026

Gary moved to the Windows PC and asked for everything to be put in order to continue. A Cowork session
(cloud, with read access to `C:\Users\Admin\Desktop\QMS` through the desktop bridge and no shell on the PC)
checked the PC's state and took Gary's three F84 decisions in the chat. **No document content changed;
nothing signed, sent or merged; Claude ran no git against the clone.**

### 2w.1 What was found on the PC

| Check | Result |
|---|---|
| Clone | `C:\Users\Admin\Desktop\QMS`, on `main` at `bfcef71`, equal to `origin/main` as last fetched (12:03 UTC, 5 Nov 2026). PRs #20 and #22 merged. |
| Remote, identity, signing | `git@github.com:GaryHill0985/QMS.git`; `Gary Adam Hill <garyadamhill@outlook.com>`; SSH signing with `id_ed25519_sesc_win`, `commit.gpgsign = true`; `core.sshCommand` to Git for Windows' client (F84 (2)). |
| Worktrees | Two Claude desktop worktrees under `.claude\worktrees\`: `reverent-chandrasekhar-c65259` (the §2u branch, merged as PR #22) and `clever-bose-7889cc` (created 12:03 UTC, at `bfcef71`, no commits at the time; it became the F85 fix, PR #23, merged as `0c57efd` later the same day). §9: one chat at a time on the repository. |
| Line endings | Files untouched since the 4 November clone (e.g. `README.md`, `.gitignore`) carry CRLF in the working tree; files updated since carry LF. `core.autocrlf = input` normalises on commit, so nothing reaches GitHub with CRLF. Recorded, not changed. |
| Reference set | **Absent.** `C:\Users\Admin\Documents` holds no `SESC` folder. `Reference\`, `Signed\` and `Insurance\` are still only on the MacBook. |
| `_to_delete\index.lock.stale` | An empty stale lock moved aside on 4 Nov; harmless. |

### 2w.2 Gary's decisions in the chat

1. **The PC clone at `C:\Users\Admin\Desktop\QMS` is the master; the MacBook clone is retired** from this
   project (not kept as a mirror).
2. **The reference set goes to `C:\Users\Admin\Documents\SESC\ISO\`** — `Reference\`, `Signed\`, `Insurance\`,
   the same layout as the MacBook, outside the clone. Gary copies them from the MacBook.
3. **`Fire Door\HANDOFF-FD-001…md` stays where it is**, untracked inside the clone.

### 2w.3 What changed

| File | Change |
|---|---|
| `CLAUDE.md` | §2, §9 and §11: MacBook paths replaced by the PC's; the PC clone named as the master; the MacBook named as not a source; PowerShell in place of zsh; the `core.sshCommand` note; the rule that a missing reference file is said and asked about, not substituted. |
| This register | §1 Repository row; F84 closed in §2t.3 and §5; the F84 task in §2t.4 marked done; this §2w; v1.30. |
| `portal/actions.yaml` | Source line v1.30; F84 marked closed. |

### 2w.4 Verification

Each edited file was diffed against the PC copy staged at the start of the session: only the lines above
changed. `CLAUDE.md` no longer names `~/Documents/SESC/ISO/` or zsh except where it names the MacBook as
retired. After the rebase onto PR #23 the validator and the portal build were re-run on the PC: `build/validate.py` 38 controlled files, 0 errors, BUILD PASSES; `build/build_portal.py` 31 pages, 104 actions.

### 2w.5 Records held, records not yet held

| Record | Held | Expected |
|---|---|---|
| Reference set on the PC (`Reference\`, `Signed\`, `Insurance\`) | **No** | Gary to copy from the MacBook; a later chat lists the folder and checks it against §11. |
| Claude Project instructions §3 and §10 updated to the PC paths and PowerShell | **No** | Gary, in claude.ai project settings. |

### 2w.6 Tasks by owner

| Owner | Task | By |
|---|---|---|
| **Gary** | Copy `Reference\`, `Signed\` and `Insurance\` from the MacBook's `~/Documents/SESC/ISO/` to `C:\Users\Admin\Documents\SESC\ISO\`. Insurance stays out of git and out of OneDrive sync. | before the next chat that needs them |
| ~~**Gary**~~ | ~~Commit this change on a branch, push, open the PR~~ (done in the next chat: branch `f84-pc-master`, rebased on `main` at `0c57efd` after PR #23); ~~review and merge~~. **Merged by Gary as `b3f4894`, 5 Nov 2026 (§2w.7). Claude did not merge.** | done |
| **Gary** | Update the Claude Project instructions (§3 sources, §10 commands) to the PC. | today |
| ~~**Gary**~~ | ~~Close or use the idle `clever-bose-7889cc` worktree session; one chat at a time on the repository.~~ **Used: it produced PR #23 (§2v), merged.** | done |

### 2w.7 Merged — 5 November 2026

**PR #24** (`github.com/GaryHill0985/QMS/pull/24`, `f84-pc-master` → `main`: register v1.30, the `CLAUDE.md` §2,
§9 and §11 amendment and the `portal/actions.yaml` source line) was merged into `main` by Gary as **`b3f4894`**
(GitHub's merge commit) at 12:30 UTC on 5 November 2026. **No review is recorded on the pull request itself** —
as with PR #20 (§2t.5), the review is Gary's own and is held only in this register. **Merging issued nothing:**
the change is to the house rules and this register, not to any controlled document. Claude did not merge.

The next chat, asked to finish what was started on `f84-pc-master`, found **nothing uncommitted** on the
branch: it was at `5b24189`, equal to its remote, and the remote branch had already been deleted by the merge.
The only untracked item in the clone is `Fire Door\` (HANDOFF-FD-001 and the 4 November PDF and workbook
outputs), which stays untracked by decision 3 at §2w.2. The clone's `main` was fast-forwarded from `0c57efd`
to `b3f4894`; the merged local branch `f84-pc-master` was deleted (its commit is on `main`); this write-back
is on `register-v1.31-pr24-merged`. **The two Claude desktop worktrees** under
`.claude\worktrees\` (`reverent-chandrasekhar-c65259`, PR #22, and `clever-bose-7889cc`, PR #23 — both merged,
both remote branches gone) were cleared at Gary's instruction in the same chat: each was checked clean and fully
merged into `main` first; both are unregistered from git and both local branches deleted. The two empty folders were
held open by the desktop app's idle sessions for PR #22 and PR #23; at Gary's instruction those two sessions were
archived (recoverable from the app's Archived list) and the folders deleted. `.claude\worktrees\` is empty. The reference set at
`C:\Users\Admin\Documents\SESC\ISO\` was not checked in this chat; §2w.5 stands.

---

## 2x. The fire door module brief for the SESC Platform; two Platform repositories read, 5 November 2026

Gary asked whether the fire door install and sign-off forms (SESC-FRM-11 and SESC-FRM-12, with the rest of the
§2t pack) could be turned into a working app, with forms for remedial work and planned inspection (PPM) as well.
He then asked for two further GitHub repositories to be read — `GaryHill0985/SESC-Platform-Design` and
`GaryHill0985/PLATFORM` — and said a *SESC Platform Build* project exists in Claude Desktop, which this chat cannot
see. Both repositories were read on his instruction in the chat (`CLAUDE.md` §2 and §11: nothing beyond the three
sources is read unless Gary asks for it; **neither is added to §11 by this section** — F87). **No controlled
document changed; no reference taken; nothing signed, sent, issued or merged.**

### 2x.1 What the two repositories hold, as read on 5 November 2026

| Repository | Found |
|---|---|
| `PLATFORM` (the build) | Vite · React 19 · TypeScript · Tailwind 4 · Supabase. One hosted Supabase project (London, Postgres 17) and a Vercel deployment at `sesc-platform.vercel.app`. **Workstream 1 only — enquiry and accountability — and it is live: Kelly logged ENQ-0001 at 13:15 on 15 September 2026**; seven staff accounts; the hosted database holds real customer personal data. Four migrations, the first frozen; append-only activity by trigger; RLS on every table; 56 tests run as a real user. **Not built:** person, site, asset, job, record, attachment, signature, document mirror, Storage, any form engine, any field surface, offline. Last commit `d601baf`, 14 September 2026; the day-one note says Prompt 4.5 (auth SMTP) is owed and has not run. |
| `SESC-Platform-Design` (the design) | Decision register v0.2, state line **15 September 2026 · 182 decisions · 14 blockers · 117 findings**, with a warning that a project-knowledge snapshot may be older than the repository. **W2 (data model and spine) is designed with a ten-prompt handoff and has not been run**; the build order says it precedes W3 onward. The designed `record` entity is polymorphic evidence over project / phase / job / site / asset / person, cites a `form_version` and a `document_version` mirrored from git (never a source), validates a jsonb payload against the form version, and generates `outcome` and `next_inspection_due`; `record_type.clauses` is the intended feed for this repository's gap report. W3 Asset, W7 forms engine, W8 photo/evidence and handover packs, W10 engineer app are prompts, not designs; W10 names Boscombe Down and makes offline mandatory. Open there and bearing here: **P20** (PWA or AppSheet), **P21** (Supabase Storage or Drive for photographs), **P23** (subcontractor logins). **Blocker B4, High: the live hosted application's five personal-data obligations were to be written back to this register before production and were not — F86.** Its §5 records, as at 15 September, that Steve had not been told the pilot held real personal data. |

### 2x.2 What was drafted

`Fire Door\HANDOFF-FD-002_Fire_Door_Platform_Module_Brief.md`, **untracked** beside HANDOFF-FD-001 (§2w.2
decision 3). A brief for the Platform project, not a controlled document: the facts above, dated; **three options
for the spine** — run W2 whole first; pull the W2 subset the doors need forward, built to W2's design column for
column (**recommended**); a fire-door-only schema (recommended against: the second shape before the first); REG-13's
thirty columns as the `asset` with its derived columns never typed; **eight record types** keyed to FRM-09 to FRM-14
plus `fd_inspection` (PPM) and `fd_remedial`, which need **`SESC-FRM-15`, `SESC-FRM-16` and `SESC-PRO-08` v0.2 drafted
in this repository first**, because the Platform mirrors controlled documents and never sources them; PRO-08's five
hold points and the release rule as transitions the database refuses; computed pass/fail from the manufacturer's
tolerance fields with no default; a fail superseded, never edited; nothing live until the PRO-08 version cited is
signed; the FRM-14 person-data boundary question; the IMS seam as metadata only; nine decisions by owner; and the
design-chat prompt to paste. **Phase 2 of HANDOFF-FD-001 is brought forward by Gary (5 November 2026) from "after
the first job" to now; PRO-08 Part 7(n) still says "after the first handover" and is amended when v0.2 is drafted.**

### 2x.3 Findings

**F86** (High, Gary) — the Platform is live with customer personal data and this register does not know it.
**F87** (Medium, Gary) — two repositories outside §11, and two designed seams to this repository that do not exist.
**F88** (Low, Gary) — on the PC `python` and `python3` were Microsoft Store stubs and the design clone's pre-commit hook blocked
every commit (§2x.6). **Closed the same day: Gary turned the two aliases off; hook re-tested, exit 0.**
All three in §5.

### 2x.4 Records held, records not yet held

| Record | Held | Expected |
|---|---|---|
| HANDOFF-FD-002, untracked in `Fire Door\` | Yes, 5 Nov 2026 | — |
| Platform register entries for the fire door module (P, B, F numbers) | **No** | Gary, in the Platform project, numbered from the register's current state line |
| `SESC-FRM-15`, `SESC-FRM-16`, `SESC-PRO-08` v0.2 | **No** | an IMS chat, when Gary asks; before the module's record types are built |
| The B4 write-back: the Platform's five personal-data obligations in this register and the documents they touch (F86) | **No** | Gary to decide the route; an IMS chat to write it |

### 2x.5 Tasks by owner

| Owner | Task | By |
|---|---|---|
| **Gary** | Read HANDOFF-FD-002; accept, change or reject §3's recommendation; paste its §10 prompt into the *SESC Platform Build* project. Check first which copy of the Platform register is current (repository or project knowledge). | next Platform session |
| **Gary** | **F86:** decide how the live Platform and its five obligations (DPIA against POL-14, controller/processor decision, SESC-REC-01 entry, POL-15 restore evidence, POL-13 access review) are written back here, and confirm whether Steve has been told since 15 September. | before the next Platform build prompt |
| **Gary** | Ask QinetiQ whether photography is permitted on site, and record the answer on the job. | before the first survey |
| Later IMS chat | `SESC-FRM-15` Fire Door Inspection Record, `SESC-FRM-16` Fire Door Remedial Work Record, `SESC-PRO-08` v0.2 (Part 6 inspection and remedial work; Part 7(n) amended), `SESC-WI-02` v0.2, `CLAUDE.md` §5 next-free line. | when Gary asks |
| **Steve** | Unchanged from §2t: D28, F83, BS 8214, the TPL-05 email, approval of the pack. **Nothing in the module goes live before these.** Any paid Supabase or Vercel tier for photograph storage is his. | before the first installation |

### 2x.6 The two Platform clones put in place on the PC, 5 November 2026

Later the same day Gary cloned both repositories to the PC under `C:\Users\Admin\Desktop\SESC Platform\` and pasted
four commands: move `PLATFORM` inside the design clone at `04-build\PLATFORM\`, which is where the design repository's
`README.md` and `CLAUDE.md` place it and which its `.gitignore` already ignores, and set `core.hooksPath` to `.githooks`
in the design clone. He reported them done. **On inspection none had run** — `PLATFORM` was still beside
`SESC-Platform-Design`, no `04-build\` existed, and `core.hooksPath` was unset in both clones. **Both were done in
this chat** as a file move within the Platform folder, which is outside `C:\Users\Admin\Documents\SESC\ISO\` and so
outside the `CLAUDE.md` §2 no-move rule, and verified. Recorded as state, not as a decision; neither repository
becomes a §11 source by this (F87). A `project-knowledge\` folder sits beside the design clone and was not read.

| Item | State, 5 November 2026 |
|---|---|
| Design clone | `C:\Users\Admin\Desktop\SESC Platform\SESC-Platform-Design\` — `main`, 45 commits, nothing uncommitted, nothing unpushed; `core.hooksPath = .githooks` from this chat. Its `tools/status.py` reports the Platform register at **v0.2 · 182 decisions · 14 blockers · 117 findings**, 17 open decisions, 0 unmerged entries files — unchanged from §2x.1. |
| Build clone | `C:\Users\Admin\Desktop\SESC Platform\SESC-Platform-Design\04-build\PLATFORM\` — `main` at `d601baf`, nothing uncommitted, nothing unpushed. Ignored by the design clone's `.gitignore` (`04-build/`), so the design repository versions the design layer only. |
| Python on the PC | Python 3.12.10 is installed (`%LocalAppData%\Programs\Python\Python312\`) and the `py` launcher runs it. **`python` and `python3` on PATH resolve first to the Microsoft Store stubs** in `%LocalAppData%\Microsoft\WindowsApps\`, which print *Python was not found* and exit non-zero. The design clone's pre-commit hook tries `python3`, then `python`, then `py`; it finds the stub first and **blocks every commit** (tested in this chat: exit 1). `py tools/register_lint.py` passes. The same stubs are why `python3 tools/status.py`, as the design `CLAUDE.md` §0 writes it, fails on this PC. **F88.** |

| Owner | Task | By |
|---|---|---|
| **Gary** | **F88:** either turn off the two App execution aliases (Settings › Apps › Advanced app settings › App execution aliases: `python.exe` and `python3.exe` off), after which `python` resolves to 3.12 and the hook passes as written; or change the hook to try `py` first. Until one is done, commit in the design clone only after `py tools/register_lint.py` by hand, or with `--no-verify`. **DONE 5 Nov 2026:** Gary turned both aliases off in Windows settings. Re-tested in the chat: `python` resolves to `%LocalAppData%\Programs\Python\Python312\python.exe`, the hook exits 0 with the lint passing. **`python3` now resolves to nothing at all on this PC**, so the design `CLAUDE.md` §0 command `python3 tools/status.py` still fails here; `python tools/status.py` or `py tools/status.py` is the form to use. Not changed in that repository by this chat. | done |

### 2x.7 Merged — 5 November 2026

**PR #26** (`github.com/GaryHill0985/QMS/pull/26`, `fire-door-platform-brief` → `main`: the two v1.31 commits pushed
after PR #25 merged, and v1.32 to v1.35 — §2x, §2x.6, F86 to F88 and the `portal/actions.yaml` resyncs) was merged
into `main` by Gary as **`21d3ef3`** (GitHub's merge commit) at 13:27 UTC on 5 November 2026, about a minute after
the v1.35 commit that recorded the pull request as open; that commit is inside the merge. CI: `validate` and `render`
both passing on the branch's final head, `validate` passing on the merge commit. **No review is recorded on the pull
request itself** — as with PRs #20 and #24, the review is Gary's own and is held only in this register. **Merging
issued nothing:** the change is to this register and the action list, not to any controlled document. Claude did
not merge.

The next chat, asked to finish what was started on `fire-door-platform-brief`, found **nothing uncommitted** on the
branch: it was at `b30805b`, equal to the merged head, and the remote branch had already been deleted by the merge.
The only untracked item in the clone is `Fire Door\` — HANDOFF-FD-001, the 4 November PDF and workbook outputs, and
HANDOFF-FD-002, last written at 12:54 UTC, three minutes before the v1.32 commit that describes it, so the brief in
the folder is the brief §2x.2 records — and it stays untracked by decision 3 at §2w.2. The clone's `main` was
fast-forwarded from `b3f4894` to `21d3ef3`; the two merged local branches `fire-door-platform-brief` and
`register-v1.31-pr24-merged` were deleted (every commit on them is on `main`; both remote branches were already
gone); `build/validate.py` re-run on the merged `main`: 0 errors, BUILD PASSES. This write-back is on
`register-v1.36-pr26-merged`. **Everything §2x leaves open is unchanged:** the §2x.4 records not yet held, the §2x.5
tasks (HANDOFF-FD-002 to Gary; F86; the QinetiQ photography question; `SESC-FRM-15`, `SESC-FRM-16` and `SESC-PRO-08`
v0.2 when Gary asks; Steve's items carried from §2t), and F86 and F87 open in §5.

---

## 2y. Docker, Node and the Supabase CLI on the PC; Prompt 4.5 verified locally (Platform B15), 5 November 2026

**Taken:** Gary's instruction in the chat — *"Install Docker Desktop & the Supabase CLI first"* — followed by a pasted
verification brief for the Platform register's blocker B15: check that W1 Prompt 4.5 (the adoption sweep, recovered
from the MacBook restore and merged to `GaryHill0985/PLATFORM` on 5 November 2026 as `48c9653`) applies and passes
its tests on a **local** database, and whether it depended on any root-level file the restore did not carry. Platform
work, recorded here because it was done on the working machine and changed its tooling, and because the two Platform
repositories were read and one of them written — on Gary's instruction, as F87 requires. **No IMS document changed.
Nothing hosted was touched: no `supabase link`, `db push`, `functions deploy` or Vercel command, no hosted key.**
First, **PR #27** (`register-v1.36-pr26-merged` → `main`: §2x.7, register v1.36) was merged by Gary as **`4e9bb15`**
at 13:34 UTC on 5 November 2026, CI `validate` and `render` passing, no review recorded on GitHub; the clone's `main`
was fast-forwarded to it in this chat and the merged local branch deleted.

### 2y.1 What was installed on the PC — state, not a decision

| Item | State, 5 November 2026 |
|---|---|
| Docker Desktop | **4.98.0** via `winget` (engine 29.9.2, WSL 2 backend, no Windows containers). The installer enabled Virtual Machine Platform, Windows Subsystem for Linux and Hyper-V, all needing a restart; Gary restarted the PC once. WSL itself was still absent after the restart and was installed with `wsl --install --no-distribution` (WSL 3.0.3.0, kernel 6.18.54.1-1). Docker Desktop is set to start at sign-in and put a shortcut on the Desktop. |
| Node.js | **26.13.0 LTS**, npm 11.20.0, via `winget`. Not in the brief, but `npm ci` needs it; the build repository's README requires Node 20 or later. |
| Supabase CLI | **2.115.0 — not a global install.** `PLATFORM/package.json` pins `supabase` as a devDependency (`^2.115.0`, locked at 2.115.0) and its npm scripts run that copy, so `npm ci` is the install the project expects. The current release, v3.0.0 of 2 November 2026, is a major version and was deliberately not installed: verifying 4.5 with a different CLI from the one it was built with would have muddied any failure. The CLI is not on `winget`; its documented Windows route, Scoop, was blocked by the chat's permission classifier and not pursued. |
| Python | Unchanged: 3.12.10, `python` resolving to it since F88 closed (§2x.6). |

### 2y.2 The verification

Both clones pulled fast-forward with nothing uncommitted: design `070e74c`, build `48c9653` (each the merge of that
repository's PR #1, the recovery). The Platform register's state line read *"24 September 2026 · 210 decisions · 17
blockers · 131 findings"*, as the brief expected. Every Prompt 4.5 file was read in full and everything it depends on
was checked against the root files, **which have not changed since `d601baf`**. Two dependencies are unmet and are
probable lost 4.5 changes, listed and not added: the Edge Function's six SMTP and recipient secrets (`SMTP_HOST`,
`SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `SMTP_FROM`, `ADOPTION_EMAIL_TO`) are not documented in `.env.example`, which
documents every other variable; and the root `README.md` says four migrations, "true as of Prompt 4", where there are
five. **All five migrations applied with no errors** on local PostgreSQL 17.6 (pg_cron 1.6.4, pg_net 0.20.4), three
times over. `npm run test:db`, as the suite's README instructs: **58 of 58 numbered tests, 842 assertions, 842 passed,
0 failed, "as pinned" — PASS**, matching the README's 58 / 842 on PostgreSQL 17. `npm run build` passed. One
environment incident: the first `supabase start` applied every migration and then failed to bind the mail-catcher's
host port 55324, *address already in use*; nothing held the port and the second start, unchanged, succeeded. The
local `.env.local` the harness reads was written from `supabase status` (local stack values only), is gitignored and
was not committed. `supabase stop` was run. **Hosted status was not checked**: a read-only dashboard checklist is in
the run-log entry. **Prompt 4.5 is verified locally, not complete.**

The run-log entry *"Prompt 4.5 — local verification (B15, 5 November 2026, Windows PC)"* was appended to
`03-handoffs/W1-run-log.md` on branch `verify/w1-prompt-4.5-local` of `GaryHill0985/SESC-Platform-Design`, commit
`6691171` (signed with the PC key, Verified on GitHub; the design clone's `tools/register_lint.py` passing: 210 · 17 ·
131, 0 unmerged), pushed, and opened as draft **PR #2** there. **Gary reviewed and merged it as `0307eb1` at 15:20 UTC**;
no review is recorded on GitHub, as with this repository's recent pull requests. The design clone's `main` is at
`0307eb1`, clean, the branch deleted; the build clone's `main` stays at `48c9653` with nothing changed. The brief
forbade issuing a Platform register number or editing the Platform register, and none was; this write-back was done
after the brief completed, on Gary's instruction in the chat.

### 2y.3 Findings

None new for this register. F87 is unchanged: the two repositories were read and one written because Gary asked in
the chat, and neither becomes a §11 source by this. Two facts belong in the Platform register, numbered there by
Gary and not here: the two probable lost root-file changes above, and the hosted checklist. The full test output of
the run exists only in the chat's scratchpad on the PC, which is not a source; the summary lines are in the run-log
entry.

### 2y.4 Records held, records not yet held

| Record | Held | Expected |
|---|---|---|
| W1 run-log entry, Prompt 4.5 local verification | Yes — `SESC-Platform-Design` `main` at `0307eb1`, 5 Nov 2026 | — |
| Hosted status of migration `20260918120000`, the `adoption-sweep` function, the two cron jobs and the two Vault secrets | **No** | Gary, read-only in the Supabase dashboard, against the checklist in the run-log entry |
| Platform register entries for the B15 local verification and the two probable lost changes | **No** | Gary, in the Platform project, numbered from the register's current state line |
| The B4 write-back (F86) | **No** — unchanged from §2x.4 | Gary to decide the route |

### 2y.5 Tasks by owner

| Owner | Task | By |
|---|---|---|
| **Gary** | Check the hosted project against the run-log entry's checklist, read-only; record the result in the Platform register and close or keep B15. If the two Vault secrets are absent, the sweep has never run. | next Platform session |
| **Gary** | Decide whether the two probable lost 4.5 root-file changes (the six function secrets in `.env.example`; the README's migration count) are re-made. A Platform build prompt, not an IMS chat. | next Platform session |
| **Gary** | F86 and the §2x.5 tasks, unchanged. | as §2x.5 |

---

## 3. Blockers — the four, restated with what has actually moved

| # | Blocker | Position at 18 August 2026, updated 24 September 2026 |
|---|---|---|
| B1 | Appoint the independent professional adviser | **CLOSED ON NAMING.** Simon Davies FCCA of Rapture Accounts Limited, confirmed 17 August. **NOT CLOSED ON DOCUMENTS: twenty documents still carry a blank adviser row and their branded PDFs must be rebuilt.** A name typed into a `.docx` does not reach a PDF already rendered.<br><br>**Nine documents route an actual control through that person and are the priority order for the rebuild: POL-02, POL-03, POL-11, POL-13, POL-16, POL-17, POL-18, POL-19 and REG-01.** POL-13 §21(j) and POL-17 §66 concede the gap in terms. CRP-01 has no such row. **POL-05 carries three separate approval rows and only the third is blank — Simon Davies goes in the third row and nowhere near the first**, which is Craig Bartle as regulation 7 competent person. |
| B2 | Sign the twenty-one documents | **CLOSED.** All 21 signed; every signature verified individually against the rendered PDF at 130 dpi on 17 August 2026. |
| B3 | Zero operating history | **OPEN, and it is the long pole.** The first quarter in which the Assurance Calendar is fully operated is the quarter ending 30 September 2026. A certification body wants roughly three months of the system running, one full internal audit round and one management review before Stage 2.<br><br>**24 Sep 2026: still the long pole. The first record entered into the Workspace forms (D15) is the date the clock starts. Record that date here when it happens.** No date recorded yet.<br><br>**24 Sep 2026, workstream 1a:** the forms generator is built in the repository (§2e), but **not yet run in Workspace. The clock has not started.** Only a **live** record counts: `markGoLive` separates setup tests from records, and `clockStart` gives the date. |
| B4 | The ISO 14001 edition problem | **OPEN. The Employer does not hold ISO 14001:2026 and nobody on this project has read it.** Every 14001 clause reference held is carried from the withdrawn :2015 edition. **Buy it before writing any EMS document.**<br><br>**24 Sep 2026:** Gary reports standards activity, but what was bought is not yet recorded. **Update this row once D6 is recorded.**<br><br>**26 Oct 2026 — D27 (§2q.1): no longer a blocker on drafting.** The EMS documents (REG-10, IMS-06, PRO-01 to 04) are drafted to the clause structure held, written 2026-ready, each with a review trigger for the purchase. B4 is now a **review trigger on the drafts** and a **blocker on quoting any 14001 clause number to PJR or a customer**, which it remains. Still not bought; still Steve's (D6). |
| B5 | A second competent person | **OPEN.** No internal auditor is trained. Book two onto the CQI/IRCA two-day course for November 2026, ~£1,130–£1,255 inc VAT each. |
| B6 | Workspace 2-step verification | **UNVERIFIED.** Recorded as off on 17 August. Five minutes. Nobody has confirmed it since.<br><br>**24 Sep 2026: it now matters twice**, because the records stopgap (D15) puts personal data in Workspace. Verify on every account with access and record the date here.<br><br>**24 Sep 2026:** this is now step 1 of `build/workspace_forms/README.md`. The build is not to be run until it is done. |

---

## 4. Open decisions — Gary's and Steve's, not a chat's

| # | Decision | Owner | Position |
|---|---|---|---|
| D1 | Certification route and scope | Gary | **Settled.** 9001+14001+45001 integrated 2027; 27001 2028+. Roofing IS in scope, and the insurance schedule must be fixed to match. |
| D2 | Certification body | Steve | **Open.** Three written quotes. Ask in writing: *"Have you completed your UKAS accreditation extension for ISO 14001:2026, and if not, which tranche and what decision date?"* Also ask for the body's own effective-personnel calculation, for SSIP deemed-to-satisfy inside the scope, and **for how much live operating history it requires before Stage 2** (see §1.1).<br><br>**24 Sep 2026: now in motion.** First conversation: James Milligan (isocertification.uk.com), **now 6 October 2026** (moved from week commencing 28 Sep). **Read F20 first.** The requirement for **three written quotes stands.** Add F20's questions to the written questions above — who issues the certificate; whether that body is UKAS-accredited for 9001:2015, 14001:2026 and 45001:2018 with IAF 28 in scope; whether it, or anyone linked to it, has consulted on SESC's system — and D16's edition question. **Engaging a certification body is Steve's decision.**<br><br>**5 Oct 2026: the 6 October meeting is a CONSULTANT conversation, not the certification body conversation** (§2h). James Milligan is offering to build SESC's documents from his ISO Certification Ltd template kit on his Dropbox. Which body certifies is still open and still needs three written quotes. Record James's answer to Q1 here.<br><br>**6 Oct 2026 (Gary, after the meeting): PJR — Perry Johnson Registrars, auditor Stephen Lloyd — to be the certification body.** UKAS schedule 0105 issue 046 (22 Apr 2026) read the same day: 9001:2015 and 45001:2018 IAF 28 in scope (45001 limited to construction excluding demolition as primary activity); **14001 at :2015 only.** See §2i.1. **Steve's decision to confirm; no written quote recorded; the three-quote requirement has not been met.**<br><br>**The cost basis, recorded so it is not re-derived — and its caveat, recorded so it is not repeated as fact.** Three standards integrated: ~13 audit days before reduction, **£7k–£13k** of CB fees in year one. All four: ~18 days, **£12k–£20k**. SESC's largest single contract is about £50,000. **⚠ Those figures assume an effective personnel count of 16–25 (IAF MD 5 base 3.0 / 4.5 / 5.5 = 13.0 days). SESC's payroll mean is about thirteen, which falls in the 11–15 band, where the base figures are lower and were NOT read from the source. And the pricing is triangulated from UK vendor sources, not quoted.** Three written quotes settle it. |
| D3 | Internal auditor — train or buy | Steve | **Open.** Train two, buy in the first cycle for independence.<br><br>**6 Oct 2026 (Gary): James Milligan to be the internal auditor.** That buys independence from SESC staff. **It does not give independence from James's own work:** he is to review the CMS Manual and carry out the fire risk assessment, and ISO 9001 and ISO 45001 9.2.2 c) want auditors who do not audit their own work. Agree with James which areas someone else audits. **B5 (a second competent person inside SESC) is not closed by this.** Steve to confirm. |
| D4 | Git host and approver | Gary | **FULLY CLOSED 18 Aug 2026.** `github.com/GaryHill0985/QMS`. Ruleset **"Protect main - controlled documents"** (id 20986828), **Active**, targeting `main`, bypass list empty, **four rules: restrict deletions · require a pull request before merging · block force pushes · require signed commits.** Commit signing configured on MSI with an ed25519 SSH key added to GitHub as a **Signing Key** (`SHA256:5IUWBrgogowui5I6MXWcc9uYYQPIvcUKVTAb9Waw18Y`). Steve approves, Gary authors and reviews — see D12.<br><br>**24 Sep 2026 — commit signing moved to the MacBook.** New ed25519 key `~/.ssh/id_ed25519_sesc`, registered on GitHub as both an Authentication key and a Signing key. **This key HAS a passphrase**, held in the macOS keychain. That reverses the §2b trade-off, which existed only because Git Bash on Windows had no ssh-agent. **Fingerprint: `SHA256:e17PhFZEmyBE1JG4LR51Du2P9Ozr5M8LJCuNTulCBwI`** (ED25519, 256-bit, comment `garyadamhill@outlook.com`), read by Gary with `ssh-keygen -lf ~/.ssh/id_ed25519_sesc.pub` on 24 Sep 2026. **The MacBook's first commit is `4b9648d`, the D13 recovery.** Local `git log` cannot check signatures, because `gpg.ssh.allowedSignersFile` is not configured on the MacBook. **Confirmed by Gary on GitHub, 24 Sep 2026: `4b9648d` and the v1.5 commit `b167f32` both show Verified.** The unbroken signed chain therefore continues from 18 August 2026 across the change of machine. **The MSI signing key (`SHA256:5IUWBrgogowui5I6MXWcc9uYYQPIvcUKVTAb9Waw18Y`) was removed from GitHub by Gary on 24 Sep 2026.**<br><br>**5 Nov 2026 — a third key, for the Windows PC (§2t.5).** ed25519, `C:\Users\Admin\.ssh\id_ed25519_sesc_win`, registered on GitHub by Gary as both an Authentication key and a Signing key. **This key has NO passphrase** — the Windows `ssh-agent` service is Disabled on the PC, so the §2b trade-off applies again (F14). **Fingerprint: `SHA256:eqUcsUYCLHs2osZeUsNYUp/bgzdchk7aIgzhGt5cRuM`** (ED25519, 256-bit, comment `garyadamhill@outlook.com`), read with `ssh-keygen -lf` on 5 Nov 2026. **The PC's first commit is `549931c`, the fire door record pack; the GitHub API reports it Verified.** The MacBook key stays registered; whether it is retired is part of F84. Git on the PC signs through Git for Windows' bundled OpenSSH 10.6 (`core.sshCommand`), because the Windows-supplied 9.5 client cannot negotiate with GitHub. `gpg.ssh.allowedSignersFile` is not configured on the PC either, so local `git log` cannot check signatures; GitHub can. |
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
| **D26** | **An elected representative of employee safety?** | **Steve** | **NEW 7 Oct 2026 (§2m).** No workers' representative has been elected or appointed. IMS-05 Part 5 designs clause 5.4 as **direct consultation of all non-managerial workers**, which the Health and Safety (Consultation with Employees) Regulations 1996 allow, and which is POL-05 O7 ¶15's position today. ISO 45001 5.2 and 5.4 refer to workers' representatives *where they exist*. Options: (a) stay with direct consultation; (b) invite the workforce to elect a representative of employee safety under the 1996 Regulations, who then attends the monthly review and is named on FRM-08, with direct consultation of everyone continuing alongside. **Not assumed either way; IMS-05 is reviewed on the decision (its `review_trigger`).**<br><br>**12 Oct 2026 (Gary, recorded at v1.19): Gary's recommendation is option (a) — direct consultation through the toolbox talks and the quarterly consultation meeting, with no separate representative. Steve to confirm, most simply by signing IMS-05; IMS-05 ¶37 and Part 6(e) are to state the decision at v0.2. Open until Steve confirms.** |
| **D27** | **The EMS documents are drafted before ISO 14001:2026 is bought** | **Gary** | **NEW, CLOSED 26 Oct 2026 — Gary's decision (§2q.1).** Buying the standard is not a prerequisite for Stage 1, for applying to PJR, or for drafting; the aspects register is built from SESC's own activities and the standard only says what it must contain. SESC-REG-10, SESC-IMS-06 and SESC-PRO-01 to 04 are drafted to `standards/iso14001-2026.yaml` as held (`verified: false`), written 2026-ready, with *ISO 14001:2026 being bought and read* as a review trigger in each. Unchanged: CLAUDE.md §6; the no-quoting rule; D6; PJR's answer on the edition (F48) as what settles the certified edition. B4 amended. |
| **D23** | **Site inspections in iAuditor (SafetyCulture)?** | **Gary, then Steve (spend)** | **NEW 6 Oct 2026.** James recommends iAuditor for Craig's site visits. SESC already has `SESC-FRM-07` Site Inspection for Workspace, with the Platform to follow (D15, D20). Using iAuditor as well would make a **third** place records live. Options: (a) iAuditor for site inspections, its template built field for field from FRM-07 so records export and migrate without re-keying; (b) stay with Workspace FRM-07 now and the Platform later. **Before choosing, read from SafetyCulture's own documentation: cost per user, export format, data location, and whether records are append-only.** A subscription is Steve's spend. |
| **D28** | **Fire door installation, remedial repair and maintenance are inside the scope** | **Steve** | **NEW 4 Nov 2026 (§2t).** Reverses the fire door half of D11, which on 24 September 2026 put fire doors out as "not a trade SESC sells". Gary's handoff of 4 November 2026 starts a fire door service line and reports a QinetiQ instruction for three doors at MOD Boscombe Down. Drafted at `SESC-IMS-04` v0.4 ¶7, ¶14 and ¶16(c)–(d), with `SESC-PRO-08` and the record pack. **Formal only on Steve's signature of v0.4; nothing is installed under PRO-08 before then.** Carries with it F83 (insurance), the REG-09 rows for the trade, and the no-certification position: the Employer holds no third-party fire door certification and the pack says so everywhere. |

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
| F7 | ICO registration is recorded as absent **because no SESC record shows one — not because the public register was queried.** That is an unverified absence, not a verified one. Query it first.<br><br>**12 Oct 2026:** still not queried. Carried at `SESC-REG-09` CO-60 with the fee tiers read from S.I. 2018/480 reg 3 (tier 1 £52 at ≤ £632,000 turnover **or** ≤ 10 staff; tier 2 £78); the tier turns on turnover, which is stated nowhere. The public register exists at `ico.org.uk/ESDWebPages/Search`. | Medium | Gary → Accounts Manager |
| F8 | The waste carrier registration number CBDL569181 appears only at POL-19 Annex A, and **the tier has not been confirmed.** Construction and demolition waste is excluded from the own-waste exemption, so **upper tier is required even carrying only the Employer's own waste.**<br><br>**12 Oct 2026: the basis is now read off the instrument** — The Waste (England and Wales) Regulations 2011 reg 24(5)(e) excludes from the own-waste category "a carrier which only transports waste produced by the carrier itself, except where it is construction or demolition waste", with construction including "improvement, repair and alteration". The tier of CBDL569181 is still unconfirmed. **And the regime is changing:** S.I. 2026/873 moves waste transporting in England into environmental permitting at the end of twelve months from its making (22 July 2026 per its introductory text — July 2027), with existing registrations transitioning under its reg 28. `SESC-REG-09` CO-43.<br><br>**CLOSED 22 Oct 2026 (§2p):** new registration **CBDU663802, "Carrier Dealer - Upper Tier", 01/10/2026–01/10/2029**, confirmed on the Environment Agency public register and recorded as `SESC-REC-05`. CBDL569181 was lower tier. Follow-ups F65, F66. | Medium | **Closed** — Environmental Manager for F65/F66 |
| F9 | **`NICEIC Consumer Protection Survey NIC13190`** — hot water, heating, ASHP and PV, certificated since 11 December 2024 — **appears in no project document.** Decide whether it belongs in the IMS scope. | Low | Gary |
| F10 | **`.gitignore` excluded `records/attachments/`, silently swallowing its `.gitkeep`** — the directory would not have existed on a fresh clone. `documents/` and `forms/` were untracked for the same reason. Found by Claude Code at push. | Medium — a build that breaks on checkout | **Closed this session.** |
| F11 | **`SESC-IMS-Project-Instructions-v1.0.md` is now actively wrong in five places** and would mislead any chat that reads it: it says the 21 documents are unsigned, that the adviser is unappointed, that `SESC-REG-02` is the next free reference, that headcount is "around 13–20" (which its own successor rule forbids stating), and that the EL certificate is not held. | **High** | **Now safe to retire — the migration gaps are closed. Do not delete until D10 is settled.** |
| F12 | **The QinetiQ question was never asked and has no owner.** *"Is ISO 27001 a requirement or a scoring advantage at SESC's tier?"* Five minutes to their supply chain team. **It is the one answer that could reverse D1.** Until answered, the plan stands.<br><br>**24 Sep 2026:** QinetiQ approved JOSCAR without raising PI or ISO 27001. **That does not answer this finding — the question was never asked.** It lowers the priority; it does not close it. | Medium | Gary |
| F13 | **Neither figure for pre-Stage-2 operating history is sourced** — see §1.1. | Medium | Gary, via D2 |
| F14 | **All commits before 18 August 2026 are unsigned**, and the signing key carries no passphrase. Both are deliberate and both are recorded at §2b rather than left for an auditor to find.<br><br>**24 Sep 2026:** the no-passphrase point applies only to the MSI key. The MacBook key that replaced it has a passphrase (D4).<br><br>**5 Nov 2026:** the Windows PC key (D4, §2t.5) **has no passphrase**, for the same reason as the MSI key — no `ssh-agent` on the machine — and is recorded here for the same reason. Single-user machine; revisit if it is ever shared. | Low, if stated | Recorded |
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
| **F58** | **`render_docx.py`'s signature guard fires on a table HEADER whose first cell begins "signed".** `SIG_LABELS = ("signature", "signed")` is matched against row 0 of a non-label table too, so IMS-05's ¶29 header *Signed statement* was refused as a filled signature row on a draft. Worked round by renaming the header; the guard should skip header rows.<br><br>**CLOSED 5 Nov 2026 (§2u):** the guard now matches only a whole *Signature* / *Signed* label in a label/value table, with three tests; a header row is never a signature row. | Low | **Closed** |
| **F59** | **The reference material the project's rules depend on was not in `~/Documents/SESC/ISO/`.** The folder held only the clone; the standards, signed policies, BRAND-SPEC, the Architecture Plan and the insurance records were all in the TeraBox restore, beside a stale `.git`-less copy of the repository and the POW/ITC trees. `CLAUDE.md` §11 pointed every chat into that mix, which is why each new chat was sent back to TeraBox. **Fixed in §2n:** copy-and-verify into `~/Documents/SESC/ISO/`, and §2, §9.4 and §11 rewritten to three sources. Closes when the copy has run clean and the PR is merged.<br><br>**CLOSED 12 Oct 2026:** the copy ran clean on 7 Oct 2026 (57 copied, 0 differ, 0 missing, 21 signed) and PR #16 is merged (§2n.1). | Medium | **Closed** |
| **F51** | **Craig Bartle's NEBOSH qualification is not on the record.** Gary believes Craig holds a current NEBOSH qualification (6 Oct 2026). No certificate has been read on this project; the only NEBOSH qualification recorded is James Milligan's NGC. **Read Craig's certificate (award, grade, date) before any document names it.** NEBOSH certificates do not expire, so whether it is current means whether his CPD and role-relevant training are current. Craig is already named across the signed documents as Quality Representative, H&S Officer, Environmental Manager and regulation 7 competent person; **he reviews and is named, but only Steve signs** (D12, CLAUDE.md §2). His certificate is personal data: it is held in Workspace under POL-14, never in git. | Medium | Craig → Gary |
| **F60** | **The signed Whistleblowing (Speak Up) Policy does not exist as a file.** `~/Documents/SESC/ISO/Signed/SESC-POL-03 Whistleblowing (Speak Up) Policy v1.1.pdf` (1,412,946 bytes, SHA-256 `9e804b8b0ef8…`) is the **Employee Code of Business Conduct, SESC-POL-01 v1.0** — cover and control block read as an image on 12 Oct 2026. The same bytes sit in the TeraBox restore at `JOSCAR/Documents/2.2 Human Resources/Branded/Signed/` and in `Evidence Pack/09 Human Resources/… (signed).pdf`, so the file submitted to JOSCAR as the Whistleblowing Policy is the Code of Conduct. The copy script compared byte for byte, so it copied the defect faithfully. Every cross-reference to POL-03 in the other signed documents (Bribery Act s.7 procedures, Protect, the Speak Up route for subcontractors) points at a document this project cannot read. **REG-09 CO-69 cites nothing from POL-03.** | **High** | Gary → Steve (re-signature if no signed copy exists) |
| **F61** | **MCS requires membership of a CTSI-approved consumer code (its guide names RECC and HIES); RECC membership 00076352 expired 15 November 2024 and is not claimed.** Whether the Employer holds HIES or any other code is recorded nowhere in the three sources. If none is held, the MCS certification NIC600672 rests on a scheme condition the record does not show as met. Read from mcscertified.com on 12 Oct 2026; MCS 001 itself was not opened. REG-09 CO-75. | **High** | Gary → Steve (a membership is a spend) |
| **F62** | **The MacBook has neither LibreOffice nor `pdftotext` (Gary, 7 Oct 2026).** `render_docx.py --pdf` cannot run there and the two printed-number tests skip. §2g's "rendered on the MacBook with LibreOffice, 19/19 including the PDF test" is not supported by what is on the machine now; recorded, not rewritten. The bridge's Linux VM does have both, but could not read the files (F64). Run the tests as `python3 build/test_render_docx.py`. | Medium | Gary (install LibreOffice); later chat (`pdfplumber` fallback) |
| **F63** | **SESC-POL-08 v1.1 is stale against the law in three places, and the waste carrier regime is being replaced.** (i) ¶16 lists the List of Wastes (England) Regulations 2005, revoked 1 July 2015; (ii) ¶34(d) says "Where required, the premises are registered as a hazardous waste producer" — Part 5 of the Hazardous Waste Regulations was omitted on 1 April 2016, so no such registration exists to require; (iii) nothing in POL-08 anticipates **S.I. 2026/873**, under which waste transporting in England becomes a regulated facility under the Environmental Permitting Regulations at the end of twelve months from 22 July 2026, the 1989 Act ceasing to apply in England and existing registrations transitioning under reg 28. Also noted for POL-19 v1.2: Annex A's UK REACH row cites "Sections 12 and section 18 of SESC-POL-16" (ambiguous); for POL-05 v1.2: Annex A 2.6.4.15 cites "Legal Register entry H024", a pointer into the superseded 2020 register. All read on legislation.gov.uk, 12 Oct 2026. REG-09 CO-42, CO-43, CO-44, CO-52. | Medium | Later chat (POL-08 v1.2, POL-19 v1.2, POL-05 v1.2); Environmental Manager (CO-43 transition) |
| **F64** | **The files in `~/Documents/SESC/ISO/` are iCloud cloud-only placeholders.** On 12 Oct 2026 the device bridge's shell could read 3 of 38 tracked files; every other read, and every read of `.git/`, returned *Resource deadlock avoided*; the bridge's staging tool reported the files as cloud-only and downloaded them to read them. A git clone whose objects can be evicted to the cloud is a clone that git itself may fail to read at the wrong moment, and it is why this chat could not run even a read-only `git log` against the MacBook. The working tree was instead verified by hashing every staged file against `main` (all 37 text files match). **Decision for Gary:** "Keep Downloaded" on the folder, or move the clone outside iCloud. Nothing was moved. | Medium | Gary |
| **F65** | **The superseded lower-tier registration CBDL569181 is still on the public register, and the new entry's address is incomplete.** On 22 Oct 2026 the EA register listed both CBDL569181 ("sesc solutions", lower tier, 05/02/2025, "UNIT 9") and CBDU663802 (upper tier, no unit number). The Employer's documents say Unit 19. Ask the EA to cancel the old entry; check the address against the lease and correct it within 28 days if wrong. The CBDU663802 certificate copy is not yet in the three sources (COO, 31 Oct). `SESC-REG-09` CO-43; §2p. | Low | Environmental Manager |
| **F66** | **CBDU663802 is registered as carrier and dealer only — not broker.** REG-09 CO-43 says the obligation applies to "brokering or dealing where removal is arranged for a customer". If the Employer ever arranges removal of waste on a customer's behalf, the registration must be varied to add broker first. Confirm whether the activity occurs. POL-19 Annex A row 25 and POL-08 ¶34(a) take the new number and tier at v1.2. §2p. | Low | Environmental Manager |
| **F81** | **The build did not run on Windows** — four portability defects in `render_docx.py` and `build_portal.py`, all fixed 4 Nov 2026 (§2t.3). | Medium | **Closed** |
| **F82** | **`SESC-PRO-06` v0.1 will not render:** a Part 6 table cell beginning *Signed induction sheets* trips the signature guard (same cause as F58). §2t.3. **CLOSED 5 Nov 2026 (§2u):** guard fixed with tests; PRO-06 rendered to 13 pages and read as images; the cell unchanged. | Medium | **Closed** |
| **F83** | **The liability business description does not name fire door work**; written confirmation that EL, PL and PI respond is required before the first installation (IMS-04 v0.4 Part 8(w)). §2t.3. | **High** | Steve |
| **F84** | **Two clones exist from 4 Nov 2026 — the MacBook's and the Windows PC's — and `CLAUDE.md` §11 names only the first; no signing key on the PC yet.** Gary's decision. §2t.3. **CLOSED 5 Nov 2026 (§2w):** the PC clone is the master, the MacBook clone retired, the reference set goes to `C:\Users\Admin\Documents\SESC\ISO\`, `Fire Door\` stays untracked in the clone; `CLAUDE.md` §2, §9 and §11 amended. | Medium | **Closed** |
| **F85** | **Fourteen tables in the seven §2q/§2r procedures print without their header row** — the header sits on the numbered-paragraph line (`25. \| Record \| … \|`) and `parse_blocks()` reads it as paragraph text, so the first data row is styled as the header. Seen on PRO-06 p. 9. A renderer fix with a test, not a document edit. §2u.3. **CLOSED 5 Nov 2026 (§2v):** `parse_blocks()` fixed with a fixture test; PRO-06 and PRO-01 rendered and read as images; 29/29 tests. | Medium | **Closed** |
| **F86** | **The SESC Platform is live with customer personal data since 15 September 2026, and this register does not know it.** The Platform's own register (B4, High) requires the hosted application's five obligations — a DPIA against POL-14, a controller/processor decision, an entry on SESC-REC-01, restore evidence for POL-15 and access review evidence for POL-13 — to be written back here before the enquiry module went to production. It was not. Kelly logged ENQ-0001 on 15 September 2026 and the hosted database has held real customer names, addresses, phone numbers and email addresses since. Nothing in SESC-IMS-04, SESC-REC-01 or the POL-13/14/15 records says so. The Platform register §5 also records, as at 15 September, that Steve had not been told; whether that has since happened is not known to this chat. §2x.1. | **High** | **Gary**; Steve to be told |
| **F87** | **Two repositories exist that `CLAUDE.md` §11 does not name** — `GaryHill0985/SESC-Platform-Design` and `GaryHill0985/PLATFORM` — read on 5 November 2026 only because Gary asked in the chat. The Platform design intends two seams to this repository that do not exist on either side: `model/entities.yaml`, generated from migration state and consumed here for clause mapping, and `record_type.clauses` feeding the gap report. Whether either repository becomes a §11 source is Gary's decision; until then they are read only on his instruction. §2x.1. | Medium | Gary |
| **F88** | **On the PC, `python` and `python3` are Microsoft Store stubs that shadow the installed Python 3.12; only `py` runs it.** The `SESC-Platform-Design` pre-commit hook enabled on 5 November 2026 tries `python3` first and therefore blocks every commit in that clone (tested: exit 1, *Python was not found*); the lint itself passes under `py`. Any `python3 build/…` command from this repository's instructions run by hand on the PC fails the same way; CI is unaffected. The fix is Gary's: disable the two App execution aliases, or have the hook try `py` first. §2x.6. **CLOSED 5 Nov 2026:** Gary turned both aliases off; `python` now resolves to the 3.12 install and the hook exits 0. `python3` resolves to nothing on this PC, so the design repository's `python3 tools/status.py` is run as `python` or `py` there. | Low | **Closed** |

---

## 6. What happens next — one workstream per chat, in this order

**From 24 September 2026, 1a and 1b come first; the existing order then resumes at 2.**

| Order | Workstream | Why this order | Est. |
|---|---|---|---|
| ~~1~~ | ~~Push to GitHub, protect `main`, require PR review, require signed commits~~ — **ALL DONE 18 Aug 2026.** See §2b. Remaining question is D12, whether Steve becomes a collaborator. | Everything now arrives as a pull request. | Done |
| **1a** | **NEW 24 Sep 2026 — Google Workspace record capture** (D15): Forms for FRM-01…05 plus toolbox talk and site inspection, the Shared Drive, and a one-page "how to log it" for site. **Repository side DONE 24 Sep 2026 (§2e): FRM-06, FRM-07, WI-01 and the generator. Workspace side is Gary's: README §2–§7.** | **Starts the B3 clock. Nothing else moves the certification date as much.** | 1 session + Gary's build |
| **1b** | **NEW 24 Sep 2026 — `SESC-IMS-04` v0.3.** **DRAFTED 24 Sep 2026 (§2f):** mould & damp named at ¶14, D8 + D17 carve-out at ¶58, fire doors removed. **With Steve for F29 (PI cover for ventilation), then signature.** | The scope statement is the first thing a certification body reads. | Done, awaiting Steve |
| **1c** | **NEW 24 Sep 2026 (D20) — the record capture section of the SESC Platform**, brought forward from item 8: photos, tamper-evident append-only records, and an authenticated submitter, with field names aligned with `forms/SESC-FRM-01…07`. **A separate workstream. Its own chat.** **5 Nov 2026 (§2x):** the Platform's enquiry module is live since 15 Sep 2026 (F86); the record capture section is not built — it is W2 plus the first slice of W3/W7/W8/W10 on the Platform side, and HANDOFF-FD-002 scopes it for the fire door trade first. | The Workspace forms cannot take photos, are not tamper-proof, and cannot prove who submitted an open form. | Platform sessions |
| ~~2~~ | **DONE 24 Sep 2026 (§2g).** **Port `policy_editor.py` to `build/render_docx.py`** and render `SESC-IMS-04` to a branded PDF, then **read the cover and a body page as images**. | Renderer parity is the Phase 1 gate. Four known traps live in `Reference\Section workflow method.md` §5. | 1 session |
| **2a** | **DONE 6 Oct 2026 (§2j) — `SESC-IMS-00` Integrated Management System Manual, draft v0.1** (D21). With Gary to commit; to James for review; Steve signs after IMS-04. | James asked for the manual first (§2i); it is also what a Stage 1 assessor opens first. | Done |
| **2b** | **DONE 7 Oct 2026 (§2l) — `SESC-REG-08` Opportunity Register, draft v0.1, and `build/export_coto.py`**, the generated *SESC COTO Log* workbook from REG-05, REG-06, REG-08 (REG-01 as a pointer until migrated). With Gary to commit; Steve confirms bands and rows on approval. | James and PJR will expect a COTO log to look like a workbook; the registers already hold the content. Separating opportunities from risks is 9001:2026-ready. | 1 session |
| 3 | **DRAFTED 7 Oct 2026 (§2m) — `SESC-IMS-05` Leadership, draft v0.1**, with the integrated policy statement (supersedes the three signed statements **on Steve's signature only**) and the 45001 5.4 mechanism, with new `SESC-FRM-08`. With Gary to commit; the workforce consultation on the statement (FRM-08) and D26 before Steve signs, after IMS-04. | 5.4 is the clause 45001 auditors test hardest; it now has a mechanism and no records. | Done, awaiting records and Steve |
| 4 | **DRAFTED 26 Oct 2026 (§2q) — `SESC-REG-10` Environmental Aspects and Impacts Register, draft v0.1**, 28 aspects from SESC's own activities, scores proposed, under D27. With Gary to commit; Craig to confirm scores; Steve to approve. | **The defining ISO 14001 document and, until this draft, the highest-priority gap in the system.** The one held belonged to a landscaping firm. No longer blocked on buying 14001:2026 (D27); re-read on purchase. | Done, awaiting scores and Steve |
| 4a | **DRAFTED 26 Oct 2026 (§2q) — `SESC-IMS-06` Planning, draft v0.1**, the clause 6 chapter with nineteen proposed objectives. With Gary to commit; the OH&S objectives to the consultation meeting; Steve to set. | Stage 1 looks for objectives; none existed with a number. | Done, awaiting Steve |
| 5 | **DRAFTED 12 Oct 2026 (§2o) — `SESC-REG-09` Compliance Obligations Register, draft v0.1**, 79 rows, replacing the 2020 register (not found in the three sources; withdrawn by POL-19 ¶86) and, on Steve's approval, POL-19 Annex A. With Gary to commit; **the retained half of the clause — the first documented evaluation of compliance — is due 30 Nov 2026 and does not exist.** | 14001 6.1.3 and 45001 6.1.3 are both dual maintain-AND-retain. | Done, awaiting the first evaluation |
| 6 | **DRAFTED 26 Oct 2026 (§2q) — `SESC-PRO-01` Control of Documented Information, `SESC-PRO-02` Internal Audit (with the first-cycle programme), `SESC-PRO-03` Management Review, `SESC-PRO-04` Nonconformity and Corrective Action, all draft v0.1.** With Gary to commit and render; the programme to the consultation meeting; Steve to approve. | The procedures the certification body asks for first, and which no SESC document provided. **Approval of a procedure closes no gap: the first audit report, the first minutes and the first log entry do** (G1–G3 stay open). | Done, awaiting render and Steve |
| **6b** | **NEW 26 Oct 2026 — Batch B, the operational procedures** (Gary's instruction: everything relevant to SESC is drafted): communication (7.4); purchasing, approved suppliers and control of subcontractors with the Approved Supplier and Contractor List as a register (8.4; G13); training, competence and awareness with a competence matrix (7.2, 7.3; G12); incident, near miss and hazard reporting and investigation (consolidating POL-05 A24 with FRM-01/02); emergency preparedness and response (8.2, pointing at POL-15); management of change (45001 8.1.3); monitoring, measurement and performance evaluation including the compliance evaluation method (9.1); plant, equipment, calibration and PAT with the maintenance and calibration log (7.1.5; G11); driving and vehicles; customer satisfaction and complaints with a feedback form (9.1.2; G15); risk assessment and method statements, bringing the RAMS system into the IMS by reference. | What the business runs on day to day; the folders of James's set that SESC has no equivalent for. Rationalised to a 13-person contractor — Deliveries & Visitors, HO controls, Enforcement Bodies, First Aid, Resources & Recruitment and Other Requirements are **not** drafted as procedures (§2q). **First session DONE 26 Oct 2026 (§2r): PRO-05 + REG-11 (8.4; G13), PRO-06 + REG-12 (7.2, 7.3; G12), PRO-07 (incidents). Remaining: the operational control set (emergency, change, plant/calibration/PAT, driving, RAMS by reference) and the performance set (9.1, 9.1.2, 7.4).** | 1 of 3–4 sessions done |
| **6c** | **NEW 26 Oct 2026 — Batch C**: `SESC-IMS-07` Support, `SESC-IMS-08` Operation, `SESC-IMS-09` Performance Evaluation, `SESC-IMS-10` Improvement; an anti-bribery and tax-evasion policy **only if POL-01 is read and found not to cover them**; a smoke- and vapour-free paragraph for POL-05/POL-06 at their next revision; a toolbox-talk topic list for FRM-06 in SESC's own titles (no HCPL text). | Completes the spine and the policy gaps James's set exposes. | 2 sessions |
| **6d** | **NEW 4 Nov 2026 — the fire door record pack (Gary's handoff HANDOFF-FD-001). DRAFTED 4 Nov 2026 (§2t):** `SESC-PRO-08`, `SESC-FRM-09`…`14`, `SESC-REG-13`, `SESC-WI-02`, `SESC-TPL-05`, `SESC-IMS-04` v0.4 (D28), `SESC-REG-12` v0.2, two build scripts. With Gary to sign-commit and open the PR; **Steve for D28, F83, BS 8214, the TPL-05 email and approval.** Phase 2 (inspection and repair records; the Platform table) follows the first job. **5 Nov 2026: Phase 2 brought forward by Gary — HANDOFF-FD-002 drafted (§2x); FRM-15, FRM-16 and PRO-08 v0.2 queued for an IMS chat when he asks.** | A live instruction with three doors is the first operational-control record set in the system, and the first clause 8.5 claim. | Done, awaiting Steve |
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
| 1.37 | 5 November 2026 | Claude, for G A Hill | **PR #27 merged; Docker, Node and the Supabase CLI on the PC; Platform B15 verified locally.** Register v1.36 merged by Gary as `4e9bb15`; the clone's `main` fast-forwarded. New §2y: Docker Desktop 4.98.0, Node 26.13.0 and WSL installed on the PC at Gary's instruction, the Supabase CLI used as the build repository's pinned 2.115.0; W1 Prompt 4.5 applies (five migrations, PostgreSQL 17.6) and passes (58/58 tests, 842/842 assertions, build passing) on a local database; two probable lost root-file changes listed; hosted status not checked; the run-log entry merged on `SESC-Platform-Design` as `0307eb1` (its PR #2). No IMS document changed; no new finding; F87 unchanged. §1 Repository row; `portal/actions.yaml` source line. |
| 1.36 | 5 November 2026 | Claude, for G A Hill | **PR #26 merged.** Register v1.31 to v1.35 (§2x, §2x.6, F86 to F88) merged into `main` by Gary as `21d3ef3`; no review recorded on GitHub, as with PRs #20 and #24; CI passing. New §2x.7; §1 Repository row. The clone's `main` fast-forwarded to `21d3ef3`; the merged local branches `fire-door-platform-brief` and `register-v1.31-pr24-merged` deleted; `Fire Door\` stays untracked (§2w.2). `portal/actions.yaml` (v1.36). No document content changed; no reference taken; nothing signed, sent or merged by Claude. Branch `register-v1.36-pr26-merged`. |
| 1.35 | 5 November 2026 | Claude, for G A Hill | **PR #26 opened** from `fire-door-platform-brief` against `main`, at Gary's instruction, carrying the two v1.31 commits pushed after PR #25 merged (`360c0b2`, `43ccbae`) and v1.32 to v1.34 (`d4813d5`, `8ee345c`, `bdc5d4d`). CI: `validate` passing, `render` pending at the time of writing. Gary reviews and merges; nothing in it needs Steve. `portal/actions.yaml` (v1.35). Nothing else changed. |
| 1.34 | 5 November 2026 | Claude, for G A Hill | **F88 closed.** Gary turned off the `python.exe` and `python3.exe` App execution aliases; the design clone's pre-commit hook re-tested, exit 0, lint passing. `python3` resolves to nothing on the PC, noted at §2x.6. §2x.3, §5, `portal/actions.yaml` (v1.34; F88 closed). Nothing else changed. Branch `fire-door-platform-brief`, on `8ee345c`. |
| 1.33 | 5 November 2026 | Claude, for G A Hill | **The two Platform clones put in place on the PC. New §2x.6.** Gary's four commands (move `PLATFORM` into `SESC-Platform-Design\04-build\`; enable the design repository's pre-commit hook) had not run; both done in this chat and verified: both clones clean and pushed, hook path set, `tools/status.py` run (Platform register unchanged at v0.2 · 182 · 14 · 117). **New F88 (Low): the Windows Store `python`/`python3` stubs shadow Python 3.12 on the PC, so the hook blocks every commit in the design clone until Gary disables them or the hook prefers `py`.** §2x.3, §5, `portal/actions.yaml` (v1.33; F88). No controlled document changed; no reference taken; nothing signed, sent, issued or merged; nothing committed in either Platform clone. Branch `fire-door-platform-brief`. |
| 1.32 | 5 November 2026 | Claude, for G A Hill | **The fire door module brief for the SESC Platform; two Platform repositories read. New §2x.** Gary asked whether the fire door forms could become a working app with remedial and PPM forms, then asked for `GaryHill0985/SESC-Platform-Design` and `GaryHill0985/PLATFORM` to be read; both read on his instruction and found: the Platform's enquiry module live since 15 September 2026 with customer personal data, W2 designed and not built, no asset, record or photo anywhere. `Fire Door\HANDOFF-FD-002…md` drafted, untracked (§2w.2): the module as a slice of W3/W7/W8/W10 on the W2 subset, eight record types keyed to FRM-09…14 plus inspection and remedial, which need FRM-15, FRM-16 and PRO-08 v0.2 here first; the design-chat prompt to paste. **New F86 (High): the Platform's B4 write-back never happened and this register did not know the Platform is live. New F87: two repositories outside §11.** §5, §6 (1c, 6d), `portal/actions.yaml` (v1.32; F86, F87). No controlled document changed; no reference taken; nothing signed, sent, issued or merged. Branch `fire-door-platform-brief`. |
| 1.31 | 5 November 2026 | Claude, for G A Hill | **PR #24 merged.** The F84 change (§2w: register v1.30 and the `CLAUDE.md` amendment) merged into `main` by Gary as `b3f4894`; no review recorded on GitHub, as with PR #20. New §2w.7; the merge task in §2w.6 marked done; §1 Repository row. The clone's `main` fast-forwarded to `b3f4894` and the merged branch `f84-pc-master` deleted; the two merged desktop worktrees (PR #22, PR #23) checked clean and cleared at Gary's instruction, and the two idle sessions holding their empty folders archived at Gary's instruction. No document content changed; nothing signed, sent or merged by Claude. |
| 1.30 | 5 November 2026 | Claude, for G A Hill | **The Windows PC becomes the master; F84 closed. New §2w.** Gary's decisions in the chat: the PC clone `C:\Users\Admin\Desktop\QMS` is the master and the MacBook clone is retired; the reference set (`Reference\`, `Signed\`, `Insurance\`) goes to `C:\Users\Admin\Documents\SESC\ISO\`, to be copied from the MacBook (not yet present); `Fire Door\` stays untracked in the clone. `CLAUDE.md` §2, §9 and §11 amended to match (PowerShell, not zsh). `portal/actions.yaml` source line v1.29. Written while PR #23 (register v1.29, §2v) merged, so the change was rebased onto `main` at `0c57efd` in the next chat, its section renumbered §2w and this row made v1.30; `portal/actions.yaml` F84 closed. Nothing signed, sent or merged. Branch `f84-pc-master`. |
| 1.29 | 5 November 2026 | Claude, for G A Hill | **F85 closed: the renderer's parser now reads a table whose header row sits on the numbered-paragraph line. New §2v.** `build/render_docx.py` `parse_blocks()`: a numbered line whose text begins with `\|` yields a bare numbered paragraph and an indented table with that line as its header row; a new `_table_rows()` shared with the ordinary table branch. One test added to `build/test_render_docx.py` (`test_table_header_on_numbered_line`), shown to fail on the old parser. All fourteen tables in `SESC-PRO-01` to `SESC-PRO-07` parse with their header; PRO-06 and PRO-01 rendered to DOCX and PDF and the affected pages read as images; DOCX numbering equals the source on both. `validate.py` 38 files, 0 errors; tests 29 run, OK, 2 skipped. §1 status row, §2u.3 F85, §2u.4 tasks (PR #22 recorded merged as `bfcef71`), §5 F85 and `portal/actions.yaml` (F85 closed; source v1.29) updated. **No document content changed; nothing signed, sent or merged.** Branch `claude/clever-bose-7889cc` cut from `main` at `bfcef71`. PR #23. |
| 1.28 | 5 November 2026 | Claude, for G A Hill | **The renderer's signature guard fixed; F58 and F82 closed; `SESC-PRO-06` rendered for the first time. New §2u.** `build/render_docx.py`: `SIG_LABELS` is no longer a prefix match on every first-column cell; a new `is_signature_label()` matches only a whole *Signature* / *Signed* label, applied only in a label/value table, and `find_signature_table()` skips header rows. Three tests added to `build/test_render_docx.py` (filled approval cell still refused; header row beginning *Signature* accepted; the PRO-06 *Signed induction sheets* cell accepted), both acceptance tests shown to fail on the old guard. PRO-06 v0.1 rendered to DOCX and PDF (13 pp) with LibreOffice on the Windows PC; cover, contents, p. 9 and the approval page read as images; signature row empty. **New F85** (fourteen numbered-paragraph tables across PRO-01 to PRO-07 print without their header — a parser defect, not fixed here). §1 status row, §2m and §2t.4 task rows, §2t.3 F82, §5 F58/F82/F85 and `portal/actions.yaml` (F58 closed, F82 closed, F85 added; source v1.28) updated. **No document content changed; nothing signed, sent or merged.** Written on a branch cut from `fire-door-record-pack`; PR #20 was merged as `fc225da` and the register taken to v1.27 (PR #21) while this session ran, so `main` was merged in and this row is v1.28. PR #22. |
| 1.27 | 5 November 2026 | Claude, for G A Hill | **PR #20 merged.** The fire door record pack (§2t) merged into `main` by Gary as `fc225da` after his review and, as he reports, Steve's approval; no review is recorded on GitHub. Recorded at §2t.5 and the §1 Repository row at Gary's choice ("record it now") rather than carried to the next workstream. Everything merged stays draft v0.1; D28 still waits on Steve's signature. `portal/actions.yaml` source line v1.27. Nothing signed, sent or issued. |
| 1.26 | 5 November 2026 | Claude, for G A Hill | **§2t committed, pushed and put up for review. New §2t.5.** Signing key for the Windows PC generated at Gary's choice ("key first, then commit") and registered on GitHub as both key types; fingerprint at D4; **no passphrase** (first pair discarded after its passphrase was refused; no `ssh-agent` on the PC) — F14 and F84 updated. Workstream commit `549931c` signed, pushed, Verified on GitHub; pull request **PR #20** (`github.com/GaryHill0985/QMS/pull/20`) opened. Windows OpenSSH 9.5 cannot negotiate with GitHub, so `core.sshCommand` uses Git for Windows' bundled client; GitHub host key checked against the published fingerprint and trusted. GitHub CLI installed. §1 Repository row, §2t.4 first task row, the §2t "not done" paragraph, `portal/actions.yaml` (v1.26; F84) updated. **Nothing signed, sent or merged; the F84 clone decision stays open.** |
| 1.25 | 4 November 2026 | Claude, for G A Hill | **The Fire Door Installation Record Pack, from Gary's handoff HANDOFF-FD-001. New §2t.** Ten references taken from `CLAUDE.md` §5 at Gary's acceptance: `SESC-PRO-08` Fire Door Installation, `SESC-FRM-09` to `SESC-FRM-14`, `SESC-REG-13` (issued empty), `SESC-WI-02`, `SESC-TPL-05` — all draft v0.1; `SESC-IMS-04` amended in place to v0.4 and `SESC-REG-12` to v0.2. **New decision D28** (fire doors inside the scope, reversing the fire door half of D11 — Steve's, open). New findings F81 (Windows build, closed), F82 (PRO-06 will not render), F83 (insurance does not name fire door work, high, Steve), F84 (two clones; signing key). `build/render_form.py` and `build/export_fire_door_register.py` added; Windows fixes to the renderer and portal builder; two IMS-04 test expectations moved to v0.4. §1 status row, §4, §5, §6 (new 6d), `portal/actions.yaml` (v1.25; D28, F81–F84) updated; the §2s task row that had pencilled D28 for the F77 answer annotated. Validation: 38 files, 0 errors; 25/25 renderer tests; portal rebuilt; every new document rendered to PDF with LibreOffice on this PC and read as images. **Nothing signed, committed, pushed, sent or merged; no signing key exists on this PC yet.** The working machine moved from the MacBook to the Windows PC at Gary's instruction; Git, Python and LibreOffice installed; clone taken from `main` at `36573a2`. |
| 1.24 | 27 October 2026 | Claude, for G A Hill | **Three files from a separate chat filed and registered. New §2s.** `SESC-POL-20` Anti-Bribery and Corruption Policy v1.0 (signed, 11 pp, every page read) filed at `Signed/` beside POL-01…19 and added to `registers/documents.yaml` with `clause_map: pending` and `issued: null`; `CLAUDE.md` §5 next free policy now POL-21, §11 count now twenty-two. The letterhead template filed at `Reference/Design/`. The bank details letter read and **kept out of the three sources** at Gary's decision. New findings **F77** (POL-20's cover and control-table dates read 03 March 2027 for issue *and* review, against a signature dated 03/03/2026 — Steve to say which; v1.1 on instruction), **F78** (contents page without page numbers and an F9 instruction left in the PDF), **F79** (its reporting route points at POL-03, which F60 says is not held), **F80** (UTR printed on the letterhead footer). `portal/actions.yaml` F77–F79 added, source v1.24. The header of this file was at v1.22 while the history was at 1.23; corrected. Nothing renamed, moved, deleted, signed, committed, sent, rendered or merged. |
| 1.23 | 26 October 2026 | Claude, for G A Hill | **Batch B, first session (§6 item 6b), at Gary's choice of slice, on a branch stacked on workstream 6. New §2r.** Five drafts v0.1: `SESC-PRO-05` Purchasing and Control of Suppliers and Subcontractors, `SESC-REG-11` Approved Supplier and Contractor Register (issued empty; one register in place of the four lists six signed policies describe), `SESC-PRO-06` Training, Competence and Awareness, `SESC-REG-12` Competence Requirements Register (44 requirements by role; no interval stated from memory), `SESC-PRO-07` Incident, Near Miss and Hazard Reporting and Investigation (the incident half of 10.2, with PRO-04 the corrective-action half). New findings F71 (four names for one empty list), F72 (FRM-02's RIDDOR note contradicts POL-05), F73 (no competence requirement stated for mould and damp or for twelve risk-assessed activities), F74 (the supplier questionnaire is not held), F75 (no signed renewal interval for most site qualifications), F76 (induction retention differs between policies). §1 status row and §6 item 6b updated. `CLAUDE.md` §5 next free: PRO-08, REG-13. `portal/actions.yaml` resynced to v1.23 (G12, G13 updated; F71–F76; 94 actions). Validation: 28 files, 0 errors, BUILD PASSES; an independent citation check of ~650 citations found 19 defects, all corrected. Every page of ten signed policies read before drafting. **The §2q render pass remains queued, with these five added to it. No render; nothing signed, committed, sent or merged.** |
| 1.22 | 26 October 2026 | Claude, for G A Hill | **Workstreams 6 and 4 and the clause 6 chapter, in one chat at Gary's direction. New §2q.** Six drafts v0.1: `SESC-PRO-01` Control of Documented Information, `SESC-PRO-02` Internal Audit with the first-cycle programme IA-01 to IA-06 (proposed), `SESC-PRO-03` Management Review (annual in November, quarterly interim), `SESC-PRO-04` Nonconformity and Corrective Action (one log on FRM-05), `SESC-REG-10` Environmental Aspects and Impacts Register (28 aspects, 24 proposed significant, every score proposed), `SESC-IMS-06` Planning (19 proposed objectives). **New decision D27:** the EMS documents are drafted without waiting for ISO 14001:2026; B4 becomes a review trigger on the drafts and stays a blocker on quoting clause numbers. §1 status row, §3 B4, §4 D27, §6 items 4, 4a, 6 (done) and new 6b, 6c (Batches B and C) updated. New findings F67 (every signed commitment date for these records has passed — Steve to confirm or re-date at the November review), F68 (three policies each describe their own audit, review and log — pointers at next revision), F69 (quality objectives have no numbers anywhere), F70 (mould and damp products and wastes recorded nowhere). `CLAUDE.md` §5 next free: PRO-05, REG-11, IMS-07. `portal/actions.yaml` resynced to v1.22. Validation: 17 files, 0 errors, BUILD PASSES. **No render; nothing signed, committed, sent or merged. Corrected at §2q: workstream 5 was already committed and pushed; the chat's assumption otherwise was wrong.** Every page of POL-05, POL-08 and POL-16 read before drafting. |
| 1.21 | 22 October 2026 | Claude, for G A Hill | **Waste carrier registration CBDU663802 received (Gary, 22 Oct 2026). New §2p.** Both numbers queried on the Environment Agency public register and recorded verbatim: CBDU663802 is **upper tier**, carrier and dealer, 01/10/2026–01/10/2029; CBDL569181 (POL-19 Annex A row 25) is lower tier and still listed. **F8 closed; IMS-00 Part 10 (r) met.** `SESC-REG-09` amended in place to v0.2 (CO-43 evidence held, two new not-yet-held records). **`SESC-REC-05` taken** for the public-register check — mapped to no clause — and `CLAUDE.md` §5 next free REC now REC-06. New F65 (old entry to cancel; address; certificate to file) and F66 (broker not covered). `portal/actions.yaml` F8 closed, F65/F66 added, source v1.21. No issued document changed; no evaluation of compliance carried out; nothing signed, committed, sent or merged. Validator result: 0 errors, 14 warnings, 6 notes, BUILD PASSES (run in the container against `main` at `cd98fdd` with the five files overlaid; the portal also rebuilt cleanly). |
| 1.20 | 12 October 2026 | Claude, for G A Hill | **Workstream 5: `SESC-REG-09` Compliance Obligations Register, draft v0.1.** New §2o. Reference taken from `CLAUDE.md` §5 (next free register REG-10). 79 obligations in four parts — OH&S, environment, data/employment/corporate, and other requirements (MOD/QinetiQ, DEFCON 658, SNG, principal contractors and prequalification, JOSCAR, MCS, NICEIC, PAS 2030/TrustMark, insurance conditions precedent, contract terms) — every instrument read on its issuing body's site on 12 Oct 2026 with the URL recorded; POL-19 Annex A (the Employer's only issued legal register, which itself withdraws the 2020 one at ¶86) re-evaluated row by row; the 2020 register not found in the three sources and nothing carried from it; James Milligan's Drive template read for column headings and topic typing only. Claims 14001/45001 6.1.3, and 9.1.2 only on the strength of a documented evaluation method — **no evaluation has ever been carried out; first due 30 Nov 2026.** Validated (0 errors, 17 files), 25/25 renderer tests in the container, portal rebuilt and read as an image, row count reconciled to the sources. G5 updated in `portal/actions.yaml`; §6 row 5 and the Part 10 (g) row updated; IMS-00 untouched. **New F60** (the signed POL-03 file is POL-01), **F61** (MCS consumer code after RECC lapsed), **F63** (POL-08 stale on the List of Wastes, hazardous-waste premises registration, and S.I. 2026/873 waste permitting), **F64** (the clone's files are iCloud cloud-only). F8 re-based on S.I. 2011/988 reg 24(5)(e). **Nothing signed, committed, sent or merged.** |
| 1.19 | 12 October 2026 | Claude, for G A Hill | **Status carried forward from Gary, 7–12 Oct 2026, recorded before workstream 5 (new §2n.1).** PR #16 merged as `cd98fdd`; workstream 3 closed as committed. SHA-256 check run by Gary on 7 Oct 2026: POL-05, POL-08 and POL-16 in `Signed/` match §2n; the copy script reported 57 copied and identical, 0 differ, 0 missing, 21 signed — **F59 closed**, the §2m and §2n provenance tasks closed. **New F62:** the MacBook has neither LibreOffice nor `pdftotext`; §2g's MacBook-render statement is not supported by the machine now and is recorded, not rewritten; tests run as `python3 build/test_render_docx.py`. D26: Gary's recommendation is direct consultation, no separate representative; Steve to confirm on signing IMS-05, IMS-05 ¶37 and Part 6(e) to state it at v0.2. Steve's choice: the shared ISO folder on the Drive replaces James Milligan's Dropbox as the working folder with James — a transfer folder, not a source; only DRAFT-marked copies, no personal data, insurance documents or this register. |
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
