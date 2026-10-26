---
id: SESC-PRO-01
title: Control of Documented Information
version: "0.1"
status: draft
owner: Chief Operating Officer
approver: Managing Director
issued: 2026-10-26
revised: 2026-10-26
prepared_by: G A Hill (drafted by Claude)
next_review: 2027-10-26
classification: internal
clauses:
  iso9001:  ["7.5.2", "7.5.3"]
  iso14001: ["7.5.2", "7.5.3"]
  iso45001: ["7.5.2", "7.5.3"]
registers_cited: [SESC-REG-07]
records_generated: [document_change_record, document_review_record, record_correction_entry]
review_trigger:
  - the migration of the first signed document into the repository (SESC-IMS-00 Part 10 (v))
  - the record capture section of the SESC Platform replacing the Workspace stopgap (D20)
  - a change to the repository's branch protection, signing or review rules
  - ISO 14001:2026 being bought and read
  - a change in the roles at SESC-IMS-04 ¶11
supersedes: null
---

# SESC-PRO-01 · Control of Documented Information

**Clause 7.5.2 and 7.5.3 of ISO 9001:2015, ISO 14001:2026 and ISO 45001:2018 — how a controlled
document is created, changed, approved, issued, found and withdrawn, and how a record is made,
kept, corrected and disposed of.**

> **Status: DRAFT, version 0.1, 26 October 2026. Not approved and not issued.**
> This procedure is issued for review by the Chief Operating Officer and approval by the Managing
> Director. Until the Approval block at Part 8 is completed, section 6.5 of SESC-IMS-00 remains the
> operative statement of document control (SESC-IMS-00 ¶46), and this procedure changes nothing.
>
> **The Employer holds no ISO certification of any kind and does not claim to.** Every statement
> in this procedure is written to be true on the day it is read, or is marked at Part 7 as a record
> that does not yet exist, with the date by which it will.

---

## Part 1 — Purpose, scope and words used

1. This procedure states how the Employer controls the documented information its Integrated
   Management System consists of: the documents that say what is to be done, and the records that
   show what was done. It is the procedure SESC-IMS-00 ¶46 says does not yet exist, and it carries
   the rules already operated under SESC-IMS-00 section 6.5, SESC-POL-05 A30, SESC-POL-08 E17 and
   SESC-POL-16 Q1 into one place without changing them.

2. **Scope.** Every document in the series at SESC-IMS-00 ¶39 — the manual, the clause spine, the
   policies, procedures, work instructions, capability sheets, form templates and registers — and
   every record those documents cause to exist. It applies to documents held in the repository, to
   the twenty-one signed documents held as branded PDFs pending migration, and to documents of
   external origin the system relies on. It applies to all Staff of the Employer, including all
   employees & subcontractors, who create, change, use or hold a controlled document or a record.

3. **The sole-director clause.** Where the Employer has only one director, any function reserved to
   the Board which requires independence from a person involved in the matter will be performed by
   the independent professional adviser named in the Approval block.

4. **Words used.** "The Employer" is SESC Solutions Ltd. "The repository" is the version-controlled
   master copy of the system described at SESC-IMS-00 ¶42. "A controlled document" is any document
   carrying a reference in the series at ¶2. "A record" is documented information that shows a
   result achieved or an activity performed; it is created once and never edited. "The records
   store" is the Google Workspace Shared Drive used as the stopgap under D15, and in due course the
   record capture section of the SESC Platform (D20). "The Document Register" is SESC-REG-07.
   "Front matter" is the block of control fields at the head of every repository document from
   which every printed control field is generated (SESC-IMS-00 ¶41).

5. **What this procedure does not do.** It does not restate the content of any document, decide
   which documents the system needs (SESC-IMS-00 and SESC-REG-07 do), or hold any record. It does
   not override SESC-POL-13 and SESC-POL-14 on the security and privacy of information; where a
   record contains personal data those policies govern and this procedure yields to them.

---

## Part 2 — Roles

6. | Role | In this procedure |
   |---|---|
   | Managing Director | Approves and signs every controlled document and every change to one. Nobody else can. |
   | Chief Operating Officer | Document controller. Authors and reviews controlled documents, takes references from the next-free line, maintains SESC-REG-07, operates the repository's change process, runs the review-due check under SESC-REG-02. |
   | Contracts Manager | Owner of SESC-POL-05, SESC-POL-08 and SESC-POL-16 and of the registers and forms those documents list; holds the current PDF of each until migration; owns the records those arrangements produce. |
   | Site Supervisors | Hold on site only the current version of the RAMS, permits and forms for the job; create records at the point of work on the form designed for it. |
   | Accounts Manager | Holds the personnel records and the accident book under SESC-POL-05 O5; applies the retention periods in SESC-POL-14. |
   | Every person | Uses the current version; raises a record on the form for it; never alters a record; reports a wrong, missing or out-of-date document. |

---

## Part 3 — Creating and changing a controlled document (clause 7.5.2)

### 3.1 Taking a reference

7. A new document takes the next free reference in its series from CLAUDE.md §5, **in the same
   change in which the document is first drafted**, and CLAUDE.md §5 is amended in that change to
   show the reference as taken. A reference is never reused, and an issued document is never
   renumbered (SESC-IMS-00 ¶40). The series, and what belongs in each, are at SESC-IMS-00 ¶39.

8. Within the SESC-IMS series the number is the clause the document covers (04 to 10), with 00 the
   manual (D21). A document that would cover more than one clause is split or is written as a
   procedure, so that the spine stays one chapter per clause.

### 3.2 What every controlled document carries

9. **Front matter**, conforming to `standards/front-matter-schema.yaml`: reference, title,
   version, status, owner (a role, never a person), approver, issue date, next review date,
   classification, the clauses it genuinely addresses, the registers it cites, the records it
   generates, and the events that trigger a review before the review date. The automated check at
   ¶17 fails any document whose front matter is incomplete, whose clause reference does not exist
   in `standards/`, or whose review date is more than twelve months after issue.

10. **Generated from the front matter, never typed:** the six-field control block, the cover, the
    running header and the *uncontrolled when printed* footer (SESC-IMS-00 ¶41). OFFICIAL-SENSITIVE
    bands head and foot, on every page, where the document is for a defence establishment.

11. **In the body:** numbered paragraphs; "the Employer" and "employees & subcontractors" in the
    house form; the sole-director clause in every governance document; a section headed **Records
    held, records not yet held** in every management-system document, giving a date for each absent
    record (CLAUDE.md §3); an Approval block; a clause map stating what in the document satisfies
    each clause claimed; and a revision history that is never deleted.

12. **Certification language.** Companies are certified; certification bodies are accredited. No
    document states that the Employer is certified to anything, or "ISO accredited", because
    neither is true.

### 3.3 Drafting

13. A draft is written from the Employer's own facts and records. Another organisation's document
    may supply a structure or a heading list and nothing else: no sentence, row, number or
    reference is copied, and nothing enters the system carrying a POW, ITC, LARC, HCPL or Unitspark
    reference (CLAUDE.md §3; Master Register §7.2). Where a draft asserts something in the present
    tense, the record proving it exists or the sentence moves to the records-not-yet-held section
    with a date. Headcount, turnover and the professional indemnity limit are stated nowhere until a
    dated payroll, accounts or policy schedule supports the figure.

14. A draft carries `status: draft`, a version below 1.0, and a status banner at its head saying it
    is not approved and changes nothing. A draft may be shown to the retained adviser, the
    certification body or a customer **only marked DRAFT and unsigned**, and only where the Chief
    Operating Officer decides it should be; the Master Register records what was shared and when.

### 3.4 Review and approval

15. **Two named humans.** Every controlled document, and every change to one, is authored and
    reviewed by the Chief Operating Officer and approved by the Managing Director (SESC-IMS-04 ¶53;
    SESC-IMS-00 ¶42). Where the Chief Operating Officer is the author, the review is a separate,
    recorded step by him against the checklist at Annex A before the document goes to the Managing
    Director; the Managing Director's approval is the second human. No automated tool, and no
    assistant used in drafting, approves, signs or merges a change to a controlled document.

16. **Approval is the Managing Director's signature** in the Approval block, dated, on the rendered
    document. A signature block is never completed by anyone else and never pre-filled. On
    signature the status becomes `approved`, the version becomes 1.0 or the next whole or point
    version, and the issue date is the date of signature. A change to an approved document that
    alters what is required of anyone is a new version; a correction of a typographical error that
    changes no requirement may be issued as a point version with the correction recorded in the
    revision history, but still signed.

17. **The automated check.** Every proposed change to the repository runs `build/validate.py` and
    the renderer tests before it can be merged. The check fails on malformed front matter, a clause
    reference that does not exist, a review date more than twelve months out, a breach of the house
    style words at ¶11, or a file flagged as containing personal data in a tracked path. A failed
    check is fixed, never bypassed. A passing check is not approval; it is the minimum condition for
    a human to look.

18. **The repository's own controls.** The main line is protected: every change arrives as a pull
    request from a branch, carries a cryptographically signed commit identifying its author, and
    cannot be force-pushed over or deleted (Master Register D4). The pull request is the change
    record: it shows the exact difference against the current version, who proposed it, who
    reviewed it and when it was merged. **No change is merged until the Managing Director has
    approved the content it carries**, and the pull request description records how he did so
    (signature date, or his written confirmation). D12 — whether the Managing Director becomes a
    collaborator so that his approval is recorded in the repository itself — is open and not
    assumed here.

### 3.5 Issue

19. The current version of every controlled document is the one on the repository's main line.
    For the signed documents pending migration, the current version is the signed PDF in
    `~/Documents/SESC/ISO/Signed/` named in SESC-REG-07, and the Contracts Manager holds it. There
    is one master copy of each document and it lives in one place; a copy held anywhere else — a
    consultant's folder, a shared drive, a laptop, the claude.ai Project — is a copy, is marked as
    such where it can be, and is never edited.

20. Documents are issued to those who need them as rendered PDFs, through the portal built from the
    repository, or by direct issue recorded on SESC-FRM-03 where issue at induction is the control
    (SESC-IMS-05 ¶31). Every PDF carries *uncontrolled when printed*: a printed or downloaded copy
    is checked against the Document Register before it is relied on for anything that matters.

21. **Site documents.** The RAMS, permits, the emergency plan and the forms for a job are issued to
    the Site Supervisor as a dated pack. When a RAMS is revised the superseded pages are removed
    from the site pack the same day and the revision re-briefed (SESC-POL-05 A2 ¶23). The acceptance
    register records which revision was briefed.

### 3.6 Review

22. Every controlled document carries a review date no more than twelve months after issue, and a
    list of events that force an earlier review. SESC-REG-02 schedules the annual reviews; the
    repository's review-due dashboard shows what is due and overdue. A review is recorded in the
    revision history whether or not a change results (SESC-POL-05 A30 ¶168; SESC-POL-08 E17 ¶93),
    so that the review cycle is auditable and the date of last review can be stated accurately.

23. At every review the records-held, records-not-yet-held section is re-read against the records
    that exist, and an item is removed only when the record it describes exists.

### 3.7 Withdrawal and supersession

24. A superseded version is marked `superseded` in its front matter and in SESC-REG-07, is
    withdrawn from every point of use, and is retained in the repository's history, which cannot be
    rewritten. A superseded signed PDF is retained for reference only, marked superseded, and never
    issued (SESC-POL-05 A30 ¶166). A document that is withdrawn without replacement is marked
    superseded with the reason in SESC-REG-07, and the documents that cited it are reviewed.

25. **Documents found to be another organisation's.** A document found to describe another
    organisation's activities, or to carry another organisation's reference, is withdrawn from use
    at once, recorded in SESC-REG-07 as withdrawn with the reason, and is not offered to anyone as
    evidence of the Employer's arrangements. The Employer has already withdrawn an aspects
    register, a COSHH register, an emergency plan and a health and safety policy on this ground
    (CLAUDE.md §3), and this paragraph is the standing rule that follows from it.

### 3.8 Documents of external origin

26. The standards, legislation, approved codes of practice, customer specifications, scheme rules,
    manufacturers' instructions and insurers' conditions the system relies on are identified in the
    document that relies on them, with the edition or date, and are controlled by that reference
    (SESC-IMS-00 ¶44). SESC-REG-09 holds the legal and other requirements with the date each was
    last checked on its issuing body's site. A standard is cited by its edition; a clause of
    ISO 14001:2026 is not quoted to anyone until that edition has been bought and read.

### 3.9 Migration of the signed documents

27. The twenty-one signed documents are migrated into the repository one at a time, SESC-POL-16
    first as the reference implementation (SESC-IMS-00 Part 10 (v)). Migration changes no word of
    the signed content; it gives the document front matter, a generated control block and a clause
    map, and the rendered PDF is compared page by page with the signed PDF before the migrated
    version is accepted. The first content change to a migrated document is a new version signed
    by the Managing Director.

---

## Part 4 — Records (clause 7.5.3)

### 4.1 What a record is, and the one rule

28. A record is made at the point of work, by the person who did the work, on the form designed for
    it, at the time or the same day (SESC-IMS-00 ¶45; SESC-WI-01). **A record is append-only. It is
    never edited, overwritten or deleted. A correction is a new entry that references the original
    and says what was wrong** (D15). A record that is wrong and corrected is more credible than one
    that has been tidied; a record that has been altered is worthless.

29. Falsifying an inspection, test, training, attendance or accident record, or signing a record
    for something that was not done, is gross misconduct (SESC-POL-16 ¶76; SESC-POL-05 A5 ¶35(g)).

### 4.2 Identification and attachment

30. Every record carries its form reference and version, the date, the person making it (or
    "anonymous" where the form is anonymous by design, SESC-FRM-01), and is attached to a job, a
    person, an organisation or an asset, so that it can be found by any of them and can migrate to
    the SESC Platform without re-keying (CLAUDE.md §8). A record that cannot be attached to one of
    those four is attached to the system itself, and that is rare.

31. **Record references.** A record that is itself a controlled artefact of the system — an
    evaluation of compliance, an internal audit report, management review minutes, a public-register
    check — takes the next free SESC-REC-nn reference from CLAUDE.md §5 and is indexed in
    `portal/records-index.yaml` with its date and the clauses it evidences. Routine records on the
    forms (a toolbox talk, a near miss, an inspection) are identified by form, date and the job or
    person, and are counted for the twelve-month staleness test (¶37) by form type.

### 4.3 Where records live

32. | Record type | Where | Why |
    |---|---|---|
    | Records containing personal data: accident detail naming people, individual training and competence records, induction records, health surveillance, face-fit, DBS and right-to-work, driver checks, disciplinary, Speak Up | The records store, under SESC-POL-14 and SESC-POL-13. **Never in the repository.** | Git history is immutable and replicated, which cannot satisfy a UK GDPR erasure request or protect Article 9 data (CLAUDE.md §8). |
    | Records about things and processes: site inspections, supplier evaluations, nonconformities about a process, toolbox talk content, spill-kit checks, equipment inspections | The records store, as the stopgap; migrating to the SESC Platform. Metadata only in `portal/records-index.yaml`. | One place for site to send everything; the repository holds the index so the staleness test can run. |
    | Records that are controlled artefacts of the system: evaluations of compliance, audit reports, management review minutes, register checks | The repository, as SESC-REC-nn, once any personal data has been removed; otherwise the records store with the metadata in the repository. | They are read by auditors and cited by documents; they must be in the master. |
    | Job records: RAMS packs, acceptance registers, inspection and test plans, test and commissioning certificates, handover packs, site diaries, COSHH registers, waste transfer and consignment notes | The job file, under SESC-POL-16 Q17 and Annex B and SESC-POL-05 Annex B | They belong to the job and are retained with it. |

33. The records store is a restricted Shared Drive with named access only; two-step verification is
    on for every account with access before any record is created (D15, B6); sheet protection and
    version history give the append-only control, and that control is **not tamper-proof** — the
    owning account and Shared Drive Managers can still edit (D20). That limitation is why the SESC
    Platform's record capture section is built as soon as possible and is stated here rather than
    hidden.

### 4.4 Access, retrieval and protection

34. Records are available to the person who needs them to do their job, to the Managing Director,
    to the internal auditor and, on request, to the certification body and to a customer where the
    contract provides for it — except that records containing personal data are disclosed only in
    accordance with SESC-POL-14, and clinical records held by the occupational health provider are
    not disclosed to management without the individual's consent (SESC-POL-05 A22 ¶127).

35. Records are protected from loss by the Workspace service's own backup and version history for
    the stopgap, by the repository's replication for repository records, and by the arrangements in
    SESC-POL-15 for the job files. A record that is lost is recorded as lost, with the date and
    circumstances, on SESC-FRM-05; it is never recreated from memory and presented as original.

### 4.5 Retention and disposal

36. Retention periods are those in the policy that governs each record type: SESC-POL-16 Annex B
    for quality records, SESC-POL-05 Annex B for health and safety records, SESC-POL-08 Annex B for
    environmental records, SESC-POL-14 for personal data, and seven years for design records
    (SESC-POL-16 Annex B). Where two periods apply the longer applies. Statutory minimums —
    two years for waste transfer notes, three for consignment notes and RIDDOR reports, forty for
    health records under COSHH, noise and vibration — are never shortened. At the end of its
    retention period a record is disposed of securely under SESC-POL-13, and the disposal is itself
    recorded. **Nothing in the repository is ever disposed of**; a repository record past its
    retention period is a reason to keep personal data out of the repository, not a reason to
    rewrite history.

### 4.6 The staleness test

37. A clause is covered only when the document that addresses it has a record behind it inside the
    last twelve months (CLAUDE.md §12.6). `portal/records-index.yaml` and the records store's form
    counts are what let that test run. A form type with no record in twelve months turns its clause
    red in the gap report, and that is the correct result.

---

## Part 5 — The procedure in one table

38. | Stage | Who | Control | Record |
    |---|---|---|---|
    | 1 Need identified | Anyone; decided by Chief Operating Officer | Does an existing document already do this? SESC-REG-07 checked | Master Register entry |
    | 2 Reference taken | Chief Operating Officer | Next free from CLAUDE.md §5; §5 amended in the same change | CLAUDE.md §5 diff |
    | 3 Drafted | Chief Operating Officer | Part 3.3; checklist at Annex A; validate.py passes | Branch and pull request |
    | 4 Reviewed | Chief Operating Officer (separate recorded step) | Annex A checklist completed | Review note in the pull request |
    | 5 Consulted, where required | Health and Safety Officer with non-managerial workers | ISO 45001 5.4 matters — the policy, objectives, audit programme, roles, controls (SESC-IMS-05 Part 5) | SESC-FRM-08 |
    | 6 Rendered and verified | Chief Operating Officer | Branded PDF; cover and a body page read as images; printed paragraph numbers checked by the renderer tests | Render log in the Master Register |
    | 7 Approved | Managing Director | Signature, dated, in the Approval block | The signed PDF; pull request merged with approval recorded |
    | 8 Issued | Chief Operating Officer; Contracts Manager | SESC-REG-07 updated; portal rebuilt; superseded version withdrawn | SESC-REG-07 row; revision history |
    | 9 Communicated | Health and Safety Officer; Site Supervisors | Induction issue on SESC-FRM-03; toolbox talk on SESC-FRM-06 where the document affects site | SESC-FRM-03; SESC-FRM-06 |
    | 10 Reviewed on schedule or trigger | Owner; Chief Operating Officer | SESC-REG-02; review-due dashboard; review recorded whether or not changed | Revision history row |

---

## Part 6 — Operating the repository safely

39. **One person at a time** works on the repository, and `git status` is run and read before any
    work starts; a file expected to be modified and which is not is evidence that something
    overwrote it (Master Register §7.7). No git command is run against the working clone through an
    assistant's device bridge, because it leaves a lock file behind that blocks the next commit
    (§7.7). One workstream per commit; a commit message describes what the commit carries and
    nothing else (§7.8). After any file is written to the clone by a tool, the file on disk is
    checked — by hash or by searching for the change — not the tool's reply (§7.9).

40. **A script exiting cleanly is not verification.** A document is rendered to PDF and the cover
    and a body page are read as images before it goes for approval (CLAUDE.md §9). The five known
    rendering traps are listed in `Reference/Decisions/Section workflow method.md` §5 and Master
    Register §2g.1.

---

## Part 7 — Records held, records not yet held

41. This section is included so that this procedure can be read alongside the records that support
    it, **without overstating what exists or concealing what does not**. It is reviewed at every
    review of this procedure, and **an item is removed from it only when the record it describes
    exists**.

42. **Records that exist and support this procedure:**

    (a) the repository `github.com/GaryHill0985/QMS`, with the ruleset *Protect main — controlled
        documents* (restrict deletions; require a pull request; block force pushes; require signed
        commits) active since 18 August 2026, and an unbroken chain of signed commits since then
        across the change of machine on 24 September 2026 (Master Register D4);

    (b) `build/validate.py` and `.github/workflows/ci.yml`, the automated check at ¶17, passing at
        the date of this draft; `build/render_docx.py` and `build/test_render_docx.py`, the renderer
        and its tests;

    (c) SESC-REG-07 Document Register, draft v0.1, listing the signed estate; SESC-IMS-00 ¶39 to
        ¶46, the operative statement of document control this procedure replaces on approval;

    (d) the twenty-one signed documents in `Signed/`, each signature verified individually on
        17 August 2026, with their SHA-256 hashes confirmed on 7 October 2026 (Master Register §2n);

    (e) `portal/records-index.yaml`, holding SESC-REC-01 to SESC-REC-05; and

    (f) SESC-WI-01 How to Log a Record on Site, draft v0.1, and the eight form schemas SESC-FRM-01
        to SESC-FRM-08, drafts, validated in the repository and not yet in use.

43. **Records and documents this procedure describes which do not yet exist.** Each carries the date
    by which it is created. **No earlier record of any of them exists and none is offered as
    evidence.** Dates marked *proposed* are proposed in this draft for the owner to confirm.

    | # | What does not exist | Position and date |
    |---|---|---|
    | (a) | **The Managing Director's signature on this procedure** | Not given. SESC-IMS-00 section 6.5 remains operative. Owner: Managing Director. Due 30 November 2026 (*proposed*, SESC-IMS-00 Part 10 (o)). |
    | (b) | **A completed Annex A review checklist for any document** | None. The review step at ¶15 has been performed informally for every draft to date and recorded in the Master Register, but not against a checklist. First on the next document to go for approval. Owner: Chief Operating Officer. Due with the next approval. |
    | (c) | **The records store live, with two-step verification verified on every account** | Not live; B6 unverified since 17 August 2026. No live record exists. Owner: Chief Operating Officer. Target was 9 October 2026 — **overdue**. |
    | (d) | **A record correction entry made under ¶28** | None, because no live record exists. First when the first correction is needed. |
    | (e) | **The first migrated signed document (SESC-POL-16) with page-by-page comparison recorded** | Not started. Owner: Chief Operating Officer. Due 30 November 2026 (*proposed*, SESC-IMS-00 Part 10 (v)). |
    | (f) | **SESC-REG-07 extended to list the repository drafts (SESC-IMS-00, 04, 05, 06; SESC-REG-08, 09, 10; SESC-FRM-01 to 08; SESC-WI-01; SESC-PRO-01 to 04)** | REG-07 v0.1 lists the signed estate only. Owner: Chief Operating Officer. Due with REG-07 v0.2, 30 November 2026 (*proposed*). |
    | (g) | **A disposal record for any record past retention** | None; nothing has reached the end of its retention period under these arrangements. |
    | (h) | **The Managing Director's approval recorded inside a pull request (D12)** | Not possible until D12 is decided; approvals to date are evidenced by signatures on PDFs outside the repository. Owner: Managing Director to decide. Due 30 November 2026 (*proposed*). |
    | (i) | **ISO 14001:2026, bought and read** | Not held. The ISO 14001 clause references in this procedure are carried from the withdrawn 2015 edition and are unverified (D27). Owner: Managing Director to buy; Chief Operating Officer to read. |

44. **Certification claims.** The Employer holds no ISO 9001, ISO 14001, ISO 45001 or ISO/IEC 27001
    certification, no BS 99001 certification, no Cyber Essentials certification and no NFRC
    membership. None is to be claimed anywhere, in any document, in any tender, or on the website.

---

## Part 8 — Approval

45. This procedure is issued with the authority of the Board of Directors of SESC Solutions Ltd.

| | | | |
|---|---|---|---|
| **Prepared by** | Gary Adam Hill, Chief Operating Officer | **Date** | 26 October 2026 |
| **Reviewed by** | | **Date** | |
| **Approved by** | Steven A Coffen, Managing Director | **Date** | |
| **Signature** | | | |
| **Independent professional adviser appointed for the purposes of the sole-director clause** | Simon Davies FCCA | **Firm** | Rapture Accounts Limited |

---

## Annex A — Review checklist for a controlled document

46. Completed by the reviewer before a document goes to the Managing Director. Every line is
    answered yes, or the document goes back.

    | # | Check |
    |---|---|
    | 1 | Reference taken from CLAUDE.md §5 and §5 amended in the same change; no reference reused |
    | 2 | Front matter complete; owner is a role; review date within twelve months; `validate.py` passes with no errors |
    | 3 | Every clause claimed is genuinely addressed in the body and named in the clause map; no clause padded |
    | 4 | No sentence asserts in the present tense something no record supports; every absent record is in the records-not-yet-held section with an owner and a date |
    | 5 | No headcount, turnover or professional indemnity limit stated without a dated source |
    | 6 | "the Employer"; "employees & subcontractors"; sole-director clause present where the document is a governance document; British English; numbered paragraphs |
    | 7 | No certification, membership, accreditation or capability claimed that is not held and read off the issuing body's document; "certified" and "accredited" used correctly |
    | 8 | No content from another organisation's document; no POW, ITC, LARC, HCPL or Unitspark reference |
    | 9 | Cross-references to other SESC documents checked against their current version and paragraph numbers |
    | 10 | Rendered to PDF; cover and a body page read as images; printed paragraph numbers match the source |
    | 11 | Revision history row written for this version; Approval block present and empty |
    | 12 | Where the document bears on health and safety at work: the ISO 45001 5.4 consultation has happened or is scheduled before signature, with the SESC-FRM-08 reference |

---

## Annex B — Clause map

47. This procedure is declared in its front matter to satisfy the clauses below. **No clause is
    cited that this procedure does not genuinely address.** Clause 7.5.1 — what documented
    information the system consists of — is claimed by SESC-IMS-00 and is not claimed here.

| Standard | Clauses | What in this procedure satisfies it |
|---|---|---|
| ISO 9001:2015 | 7.5.2 | Part 3 — identification and description (¶9 to ¶12), format and media (¶10, ¶19, ¶20), review and approval for suitability and adequacy (¶15 to ¶18) |
| ISO 9001:2015 | 7.5.3 | Part 3, sections 3.5 to 3.8, and Part 4 — availability and suitability for use, protection, distribution, access, retrieval, storage, change control, retention and disposition, and control of documents of external origin |
| ISO 14001:2026 | 7.5.2, 7.5.3 | As above. **Clause numbering carried from the withdrawn 2015 edition and marked unverified — see Part 7(i) and D27.** |
| ISO 45001:2018 | 7.5.2, 7.5.3 | As above, with the site document control at ¶21 and the worker consultation step at Part 5 stage 5 |

---

## Annex C — Revision history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 26 October 2026 | G A Hill (drafted by Claude) | First draft, as workstream 6 of the Master Register (§6 item 6) and SESC-IMS-00 Part 10 (o). Carries the rules already operated under SESC-IMS-00 section 6.5, SESC-POL-05 A30, SESC-POL-08 E17 and SESC-POL-16 Q1 into one procedure, unchanged, with the records rules of D15 and CLAUDE.md §8 and the repository rules of Master Register §7. Structure follows the stage / responsibility / control / record layout of a consultant's template procedure used as a layout only (Master Register §2h item 3); no content was taken from it or from any other organisation's document. Claims 7.5.2 and 7.5.3 of all three standards; not 7.5.1. **The Approval block at Part 8 is unsigned; SESC-IMS-00 section 6.5 remains operative.** |
