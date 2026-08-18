# SESC-IMS-Master-Register

**The state of the CLAUDE ISO project. v1.3 · 18 August 2026.**

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
| **Repository** | **`github.com/GaryHill0985/QMS`**, pushed 18 August 2026, commit `d3782f7`. The working clone is `Desktop\SESC\ISO\CLAUDE ISO\`. **D4 CLOSED.** |
| **Master document count** | 21 signed (POL-01…19, CRP-01, REG-01) + REG-02, REG-03, REG-04 + REC-01…04 + TPL-01…04. |
| **This repository holds** | 3 controlled source files, 134 clauses across 3 standards, CI passing. |

### 1.1 The phase plan, and the principle that governs it

**Phase gates are about records accumulating, not build speed.** A phase is not passed by
finishing the work in it; it is passed when the evidence the next phase needs actually exists.

| Phase | Window | Gate to pass |
|---|---|---|
| 0 | to 27 Aug 2026 | JOSCAR submitted. **Effectively clear** — all 30 sections at 100%, held only on insurance attachments. |
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

## 3. Blockers — the four, restated with what has actually moved

| # | Blocker | Position at 18 August 2026 |
|---|---|---|
| B1 | Appoint the independent professional adviser | **CLOSED ON NAMING.** Simon Davies FCCA of Rapture Accounts Limited, confirmed 17 August. **NOT CLOSED ON DOCUMENTS: twenty documents still carry a blank adviser row and their branded PDFs must be rebuilt.** A name typed into a `.docx` does not reach a PDF already rendered.<br><br>**Nine documents route an actual control through that person and are the priority order for the rebuild: POL-02, POL-03, POL-11, POL-13, POL-16, POL-17, POL-18, POL-19 and REG-01.** POL-13 §21(j) and POL-17 §66 concede the gap in terms. CRP-01 has no such row. **POL-05 carries three separate approval rows and only the third is blank — Simon Davies goes in the third row and nowhere near the first**, which is Craig Bartle as regulation 7 competent person. |
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
| D2 | Certification body | Steve | **Open.** Three written quotes. Ask in writing: *"Have you completed your UKAS accreditation extension for ISO 14001:2026, and if not, which tranche and what decision date?"* Also ask for the body's own effective-personnel calculation, for SSIP deemed-to-satisfy inside the scope, and **for how much live operating history it requires before Stage 2** (see §1.1).<br><br>**The cost basis, recorded so it is not re-derived — and its caveat, recorded so it is not repeated as fact.** Three standards integrated: ~13 audit days before reduction, **£7k–£13k** of CB fees in year one. All four: ~18 days, **£12k–£20k**. SESC's largest single contract is about £50,000. **⚠ Those figures assume an effective personnel count of 16–25 (IAF MD 5 base 3.0 / 4.5 / 5.5 = 13.0 days). SESC's payroll mean is about thirteen, which falls in the 11–15 band, where the base figures are lower and were NOT read from the source. And the pricing is triangulated from UK vendor sources, not quoted.** Three written quotes settle it. |
| D3 | Internal auditor — train or buy | Steve | **Open.** Train two, buy in the first cycle for independence. |
| D4 | Git host and approver | Gary | **FULLY CLOSED 18 Aug 2026.** `github.com/GaryHill0985/QMS`. Ruleset **"Protect main - controlled documents"** (id 20986828), **Active**, targeting `main`, bypass list empty, **four rules: restrict deletions · require a pull request before merging · block force pushes · require signed commits.** Commit signing configured on MSI with an ed25519 SSH key added to GitHub as a **Signing Key** (`SHA256:5IUWBrgogowui5I6MXWcc9uYYQPIvcUKVTAb9Waw18Y`). Steve approves, Gary authors and reviews — see D12. |
| D5 | Independent professional adviser | Steve | **Closed on naming** — see B1. |
| D6 | Buy the standards | Steve | **OPEN.** ISO 14001:2026 not held in any form. ISO/IEC 27001:2022 not held in any form. The 9001:2015 PDF held is licensed to Unitspark Ltd, single user. Buy own copies — **and ISO/IEC 27002:2022 with 27001, because without 27002 the Annex A control set cannot be applied.** |
| D7 | BS 99001:2022 | Gary | **Deferred.** UKAS accreditation is still a pilot with four CBs and no completion date, and BS 99001 references ISO 9001:2015 which is superseded next month. **Revisit when a Building-Safety-Act bid asks for it. A copy of BS 99001:2022 is already held at `Desktop\SESC\ISO\`.** |
| **D8** | **The design carve-out for the standard quotation** | **Steve** | **NEW, AND THE ISO 9001 SCOPE TURNS ON IT.** The capability statements and the quotation contradict each other. Proposed wording at `system/4-context.md` ¶58. Nothing is applied to any customer-facing document until it is approved or replaced. |
| **D9** | **The `SESC-IMS-nn` series for the Annex SL spine** | **Gary** | **NEW.** Confirm or overturn — see §2 decision 1. |
| **D10** | **Should the four planning files be tracked in the repo?** | **Gary** | **NEW.** `SESC-IMS-Project-Instructions-v1.0.md`, the Readiness & Gap Analysis, the Gap Register xlsx and the review copies sit untracked in the clone, so **GitHub is not backing them up and the only copy is the laptop.** Options: move them into a `planning/` folder and track them, or leave them and accept the backup risk. Moving files inside `Desktop\SESC` is reserved to Gary. |
| **D12** | **Should Steve be a collaborator on the repository?** | **Gary** | **NEW, and it is the sole-director problem again.** `CLAUDE.md` says *"Steve approves, Gary authors and reviews. Two named humans."* **Required approvals on the ruleset is set to 0, because GitHub will not let a person approve their own pull request and 1 would deadlock a solo repository.** So the PR gate and the diff exist, but the second human does not. **Adding Steve as a collaborator and raising required approvals to 1 is what makes the rule operable** — exactly as appointing Simon Davies made the Board-independence clause operable. Until then the two-human rule is written and not operated, which is the failure pattern POL-08 is marked down for. |
| **D11** | **Are fire doors and mould & damp remediation named trades for the certificate scope?** | **Steve** | **NEW, and it changes the scope statement.** The project instructions describe the business as "M&E, roofing, **mould and damp remediation, fire doors** and renewables". The signed policies say "roofing, building fabric, mechanical, electrical and renewable energy works" and name neither. **A Building-Safety-Act-adjacent trade omitted from a scope statement is a finding.** If they are carried out, they are named at IMS-04 ¶14. |

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
| F12 | **The QinetiQ question was never asked and has no owner.** *"Is ISO 27001 a requirement or a scoring advantage at SESC's tier?"* Five minutes to their supply chain team. **It is the one answer that could reverse D1.** Until answered, the plan stands. | Medium | Gary |
| F13 | **Neither figure for pre-Stage-2 operating history is sourced** — see §1.1. | Medium | Gary, via D2 |
| F14 | **All commits before 18 August 2026 are unsigned**, and the signing key carries no passphrase. Both are deliberate and both are recorded at §2b rather than left for an auditor to find. | Low, if stated | Recorded |
| F15 | **The "two named humans" approval rule is not yet operable** — required approvals is 0 and Steve is not a collaborator. The control exists on paper only. | **Medium** | Gary, via D12 |
| F16 | **⚠ TWO SESSIONS WORKED ON THIS REPOSITORY AT ONCE ON 18 AUGUST, AND ONE OVERWROTE THE OTHER.** A Claude Code session built a portal generator (`build/build_portal.py`, `portal/*.yaml`, README changes) between 11:59 and 12:12. **In the process `registers/interested-parties.yaml` was reverted from v0.2 back to the v0.1 committed content, silently losing three restorations** — the first-aid needs assessment obligation, the "an unaccredited certificate submitted to JOSCAR is worse than no certificate" line, and Sovereign Housing named against IP-02. Found only because a file expected to be modified did not appear in `git status`. **This is the fourth time on this project that two copies of one thing have drifted.** | **High** | v0.2 restored. **Rule below.** |
| F17 | **A stale `.git/index.lock` blocked `git add` and `git commit`**, so a branch was pushed with no commits on it. Cause: a `git status` run through the device bridge, which cannot remove its own lock file. **Do not run git commands against the working clone through the device bridge.** | Medium | Closed — lock removed, rule recorded at §7.7 |

---

## 6. What happens next — one workstream per chat, in this order

| Order | Workstream | Why this order | Est. |
|---|---|---|---|
| ~~1~~ | ~~Push to GitHub, protect `main`, require PR review, require signed commits~~ — **ALL DONE 18 Aug 2026.** See §2b. Remaining question is D12, whether Steve becomes a collaborator. | Everything now arrives as a pull request. | Done |
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
| 1.0 | 18 August 2026 | Claude, for G A Hill | Created. Closes finding F1. Records the QMS build session 1: repository, clause map, `SESC-IMS-04`, `SESC-REG-05`, `SESC-REG-06`, validator and CI. |
| 1.3 | 18 August 2026 | Claude, for G A Hill | F16 — concurrent-session overwrite found and `registers/interested-parties.yaml` v0.2 restored. F17 — stale index.lock from the device bridge. Two new rules at §7.7 and §7.8. Portal generator built by a parallel Claude Code session noted and left intact. |
| 1.2 | 18 August 2026 | Claude, for G A Hill | GitHub controls completed — ruleset "Protect main - controlled documents" Active with four rules, and commit signing configured. New §2b. D4 fully closed. New decision D12 (Steve as collaborator, so the two-human rule is operable) and findings F14, F15. **Direct pushes to `main` are no longer possible.** |
| 1.1 | 18 August 2026 | Claude, for G A Hill | Session 2. D4 closed — repo live at `github.com/GaryHill0985/QMS`. Full migration audit of the project instructions against the repo: 31 dropped items and 8 weakened ones closed by adding `CLAUDE.md` §11 and §12. `.gitignore` defect fixed (F10). Phase plan restored at §1.1 with the unsourced-operating-history caveat. Nine adviser-dependent documents added to B1. Cost basis and its caveat added to D2. New decisions D10, D11; new findings F10–F13. |
