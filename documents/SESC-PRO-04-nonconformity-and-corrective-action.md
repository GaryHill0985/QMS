---
id: SESC-PRO-04
title: Nonconformity and Corrective Action
version: "0.1"
status: draft
owner: Contracts Manager
approver: Managing Director
issued: 2026-10-26
revised: 2026-10-26
prepared_by: G A Hill (drafted by Claude)
next_review: 2027-10-26
classification: internal
clauses:
  iso9001:  ["10.2.1", "10.2.2"]
  iso14001: ["10.2"]
  iso45001: ["10.2"]
registers_cited: [SESC-REG-01, SESC-REG-03, SESC-REG-09, SESC-REG-10]
records_generated: [nonconformity_record, corrective_action_record, effectiveness_verification]
review_trigger:
  - record capture going live in Workspace, and the first SESC-FRM-05 record
  - the record capture section of the SESC Platform replacing the Workspace stopgap (D20)
  - the first internal audit report (SESC-PRO-02) and the first management review (SESC-PRO-03)
  - a major nonconformity, an enforcement action or a RIDDOR-reportable injury
  - ISO 14001:2026 being bought and read
supersedes: null
---

# SESC-PRO-04 · Nonconformity and Corrective Action

**Clause 10.2 of ISO 9001:2015, ISO 14001:2026 and ISO 45001:2018 — what the Employer does when
something does not meet a requirement: react, record, find the cause, act so it does not recur,
check that it worked, and keep the evidence of all five.**

> **Status: DRAFT, version 0.1, 26 October 2026. Not approved and not issued.**
> This procedure is issued for review by the Chief Operating Officer and approval by the Managing
> Director. Until the Approval block at Part 9 is completed it evidences nothing, and the
> arrangements at SESC-POL-16 Q14 and Q20, SESC-POL-05 A8 and A24 and SESC-POL-08 ¶39 and ¶59
> remain the operative statements. **No nonconformity and corrective action log of the Employer's
> own has been opened** (CLAUDE.md §10; SESC-IMS-00 Part 10 (i)); the three signed documents each
> said one would open on 31 August 2026, and it did not.
>
> **The Employer holds no ISO certification of any kind and does not claim to.**

---

## Part 1 — Purpose, scope and words used

1. This procedure states how a nonconformity of any kind — in the work, in the system, in health
   and safety, in environmental control, in compliance — is raised, controlled, investigated,
   corrected, prevented from recurring and closed, and how the record of that is kept. It is the
   procedure SESC-IMS-00 Part 10 (o) says does not exist. It consolidates, without changing, the
   control and disposition of non-conforming work at SESC-POL-16 Q14, the improvement log at
   SESC-POL-16 Q20, the corrective action log at SESC-POL-05 A8 ¶50 and SESC-POL-08 E10 ¶59, the
   investigation requirements at SESC-POL-05 A24 ¶136 and SESC-POL-08 ¶39, and the single form
   SESC-FRM-05 that records all of them.

2. **One log.** A defect in a roof, a missing waste transfer note, an unbriefed RAMS, an audit
   finding, a complaint, a breach of a compliance obligation and a near miss that reveals a failed
   control are the same object — a requirement not met — with a different domain tag. The Employer
   keeps one nonconformity and corrective action log for all three standards, on SESC-FRM-05, for
   the reason SESC-FRM-05's own design note gives: separate logs are how a small business ends up
   reviewing none of them.

3. **Scope.** Every requirement the Employer has accepted: the three standards, its own documents,
   the law and the scheme rules in SESC-REG-09, the customer's specification and site rules, and
   the manufacturer's instructions. Every site, every job, Unit 19, and the system itself. All Staff
   of the Employer, including all employees & subcontractors.

4. **The sole-director clause.** Where the Employer has only one director, any function reserved to
   the Board which requires independence from a person involved in the matter will be performed by
   the independent professional adviser named in the Approval block.

5. **Words used.** "A nonconformity" is the non-fulfilment of a requirement. "Correction" is what is
   done to fix the nonconformity itself. "Cause" is why it happened, found by investigation, not
   assumed. "Corrective action" is what is done to the cause so that it does not recur, here or
   elsewhere. "Verification of effectiveness" is the later check, by someone other than the person
   who acted, that the corrective action worked. "The log" is the set of SESC-FRM-05 records.
   "Disposition" is the decision on what happens to non-conforming work or material, taken under
   SESC-POL-16 Q14 ¶47 and nowhere else.

---

## Part 2 — Roles

6. | Role | In this procedure |
   |---|---|
   | Everyone | Raises a nonconformity when they see one — on SESC-FRM-05, or on SESC-FRM-01 or SESC-FRM-02 where it is a near miss, hazard or incident, from which the Health and Safety Officer raises the SESC-FRM-05. Does not conceal, work around or build over one (SESC-POL-16 ¶45, ¶76). |
   | Site Supervisors | Take the immediate action: stop, make safe, isolate, mark and separate (¶10). Report the same day. |
   | Contracts Manager | As Quality Representative, Health and Safety Officer and Environmental Manager: owns the log and this procedure; decides the disposition of non-conforming work (SESC-POL-16 ¶47, ¶48); leads or allocates every investigation; raises the SESC-FRM-05 for every incident, audit finding and compliance breach; reports open and overdue items to the Managing Director monthly. |
   | Chief Operating Officer | Verifies effectiveness where the Contracts Manager acted; raises nonconformities from the system's own checks (validate.py, the gap report, the records inventories); presents the analysis to the management review. |
   | Managing Director | Notified the same day of every major nonconformity, every reportable incident and every compliance breach; decides every corrective action that costs money, changes a contractual position or involves a statement to a customer, insurer, regulator or the certification body; receives the monthly report. |
   | Non-managerial workers | Take part in the investigation of any nonconformity on their job and in the choice of corrective action that changes how they work (ISO 45001 clause 10.2; SESC-IMS-05 ¶38(e)). |
   | Retained external adviser | Advises on investigation and cause for health and safety and environmental nonconformities where asked; does not decide. |

---

## Part 3 — Where nonconformities come from

7. A nonconformity is raised whenever any of these occurs, and the source is tagged on SESC-FRM-05:

   | Source | Tag | Raised by |
   |---|---|---|
   | Non-conforming work or material found in process, at inspection, at handover or in the guarantee period (SESC-POL-16 Q7, Q11, Q13, Q14) | quality | Anyone; disposition by Quality Representative |
   | Customer complaint (SESC-POL-16 Q15) | quality / complaint | Quality Representative, same day |
   | Accident, incident, dangerous occurrence, ill health, or a near miss that shows a control failed (SESC-POL-05 A24; SESC-FRM-01, 02) | OH&S | Health and Safety Officer, from the FRM-01/02 |
   | Environmental incident, spill, release, or a duty-of-care failure (SESC-POL-08 E7 ¶39) | environment | Environmental Manager |
   | Internal audit finding graded major or minor (SESC-PRO-02 ¶20) | audit | Auditor |
   | Certification body, SSIP, CHAS, NICEIC, Gas Safe, MCS or other external assessment finding | external | Chief Operating Officer |
   | Compliance evaluation result "not compliant" (SESC-REG-09 evaluation method) | compliance | Environmental Manager / Health and Safety Officer |
   | Enforcement contact, notice or prosecution by HSE, the Environment Agency, a local authority or a scheme | enforcement | Managing Director notified at once |
   | A control in the aspects register (SESC-REG-10) or a risk treatment in SESC-REG-01 found not operating | system | Owner of the register |
   | The system's own checks: a record declared not yet held whose date has passed; a review date missed; validate.py failing on main; a document found to be another organisation's | system | Chief Operating Officer |
   | An item raised by a worker through the consultation mechanism that reveals a requirement unmet (SESC-IMS-05 ¶41) | OH&S / system | Health and Safety Officer |
   | A supplier or subcontractor failure (SESC-POL-16 ¶25; SESC-POL-08 ¶51(e)) | supplier | Contracts Manager |
   | A lost record (SESC-PRO-01 ¶35) | system | Record owner |

8. **Grading.** Major: systemic, or a legal or scheme breach, or a record told to anyone as held
   that does not exist, or actual or potential serious harm. Minor: a single lapse against a
   requirement otherwise operated. The grade sets the clock at ¶13 and who is told at ¶6.

---

## Part 4 — The five steps

### 4.1 React: control and correct

9. The person who finds it stops it getting worse. Work that is unsafe is stopped under the
   stop-work authority (SESC-IMS-04 ¶13). Non-conforming material is marked, physically separated
   and recorded so that it cannot be installed by mistake; non-conforming work is identified and,
   where it presents a safety risk, isolated or made safe at once (SESC-POL-16 ¶46). A spill is
   contained under SESC-POL-08 ¶38(b). An injured person is treated under SESC-POL-05 A25. The
   scene of a serious injury or dangerous occurrence is preserved (SESC-POL-05 ¶137).

10. **Disposition of non-conforming work or material** is decided by the Quality Representative,
    recorded, and is one of the five at SESC-POL-16 ¶47 — rework, repair with the customer's
    written agreement, accept by written concession, reject and replace, scrap — and never anything
    else; a concession is never given on site (¶48), and never where safety or a statutory
    requirement is involved. Suspected counterfeit material is handled under SESC-POL-17 before any
    disposition. **This procedure does not change Q14; it points at it.**

11. The correction — what was done to fix this instance — is recorded on SESC-FRM-05 with the date
    and by whom. Correction is not corrective action, and closing a record at this step is not
    permitted for anything graded major or for any recurrence.

### 4.2 Record

12. Every nonconformity is recorded on SESC-FRM-05 the day it is found, with the fields the form
    requires: date raised; raised by; the job, person, organisation or asset it attaches to; the
    source and domain tag at ¶7; the requirement not met, cited to the document, clause, law or
    specification; what was found, where and by whom; the grade; the immediate correction and
    disposition; and whether the customer, a regulator, the insurer or the certification body must
    be told, and the Managing Director's decision on that. A record that names an individual's
    conduct or health is held in the records store under SESC-POL-14 with the repository holding
    metadata only (SESC-FRM-05 `completed_record`; SESC-PRO-01 ¶32).

### 4.3 Investigate: find the cause

13. **Who and when.** The Contracts Manager leads or allocates the investigation. A major
    nonconformity is investigated within five working days of being raised; a minor within fifteen.
    An accident, dangerous occurrence or significant near miss is investigated under SESC-POL-05
    ¶136 proportionately to its actual and potential severity; an environmental incident under
    SESC-POL-08 ¶39. A worker who does the job takes part in the investigation of anything on their
    job (SESC-IMS-05 ¶38(e)), and the record names the role and number of workers who took part.

14. **How.** The investigation establishes the sequence of events; the immediate cause; and the
    underlying cause — asking in turn whether the requirement was clear, whether the risk
    assessment or method statement or specification addressed it, whether the person was competent
    and briefed, whether the equipment and materials were right and in date, whether the
    supervision and the programme allowed the work to be done properly, and whether the system
    itself (a missing procedure, a document that says one thing while the work does another, a
    record that nobody makes) is the cause. "Operator error" is never recorded as a cause without
    the question why having been asked and answered. Where the same or a similar nonconformity has
    occurred before, the earlier record is cited and the previous corrective action is reviewed as
    having failed.

15. **Does it exist elsewhere?** The investigation asks whether the same nonconformity exists, or
    could occur, on other jobs, other sites, with other people, or in other documents, and records
    the answer. A requirement unmet on one job is checked on every live job of the same type before
    the record moves on.

### 4.4 Act: corrective action

16. Corrective action is addressed to the cause at ¶14, is proportionate to the effect and potential
    effect of the nonconformity, and has an owner (a role) and a date. Where it changes a controlled
    document, a RAMS, a register, a competence requirement, a supplier's status or a control in
    SESC-REG-10, the change is made through SESC-PRO-01 or the register concerned and the
    SESC-FRM-05 cites the change. Where it changes how workers work, the workers concerned take part
    in choosing it and are briefed on it at the next toolbox talk (SESC-FRM-06). Where it needs
    money, the Managing Director decides; an action with no time or money allocated is either
    resourced or closed with the reason recorded (SESC-POL-16 ¶63(d)).

17. **Risks and opportunities.** The investigation's findings are checked against SESC-REG-01 and
    SESC-REG-08, and against the hazards and aspects in the RAMS and SESC-REG-10: a nonconformity
    that reveals a risk not registered, or a control not working, updates the register, and the
    SESC-FRM-05 cites the row (ISO 9001 10.2.1 e); ISO 45001 10.2 e)).

### 4.5 Verify and close

18. **Closure is by verification, never by the calendar.** When the owner reports the corrective
    action done, a person other than the owner — normally the Chief Operating Officer, or the
    auditor who raised it, or the Contracts Manager where the Chief Operating Officer acted —
    examines the evidence that the action was implemented and, after an interval long enough to
    tell, that it worked: the nonconformity has not recurred; the changed document is in use; the
    record it required is being made; the control is observed operating on site. The verifier
    records what was examined, when and the conclusion, and signs the closure. A corrective action
    that did not work reopens the record with a new cause analysis.

19. **Time to close.** Major: corrective action implemented within thirty days of the record and
    verified within ninety; minor: implemented within sixty days and verified within one hundred and
    twenty. An item that will take longer is re-dated once, by the Managing Director, with the
    reason minuted. An overdue item is reported as overdue at ¶20 until closed.

---

## Part 5 — The log, the monthly report and the review

20. The Contracts Manager maintains the log — every SESC-FRM-05 record, its grade, source, owner,
    dates and status — and reports to the Managing Director monthly: items raised in the month,
    open items by grade and age, overdue items, items awaiting his decision, and items awaiting
    verification. The monthly report is the one at SESC-POL-16 ¶50 and ¶63(c), SESC-POL-05 ¶50 and
    SESC-POL-08 ¶59, which this procedure consolidates, and from the first month it runs it sits
    alongside the consultation report at SESC-IMS-05 ¶38(d).

21. **To the management review** (SESC-PRO-03 inputs 4 to 6): the number and grade of
    nonconformities by source and domain; the causes found, grouped; the time to close against ¶19;
    the proportion of closures verified by an independent person; recurrences; and the corrective
    actions that changed a document, a control or a competence requirement — which, with the
    improvements at SESC-REG-08, is the Employer's evidence of continual improvement under clause
    10.3.

22. **Telling people.** Lessons from an investigation are shared with the workforce by toolbox talk
    (SESC-POL-05 ¶136; SESC-POL-08 ¶39) and recorded on SESC-FRM-06. The customer is told where the
    contract or the nature of the nonconformity requires it, and the decision to tell is the
    Managing Director's, recorded on the SESC-FRM-05. A regulator is told where the law requires it
    (RIDDOR under SESC-POL-05 ¶134; the Environment Agency incident hotline under SESC-POL-08
    ¶38(e)) and the report reference is recorded.

---

## Part 6 — Measuring the process

23. From the first record, and reported at the management review: nonconformities raised per month
    by source; the proportion investigated within the ¶13 period; the proportion closed within the
    ¶19 period; the proportion of closures verified by someone other than the owner; recurrences;
    and the proportion of records with a cause other than "operator error". **No measure has yet
    been taken, because no record exists.** A rising count of nonconformities raised in the first
    year is treated as a positive indicator of a reporting culture, as the near-miss count is under
    SESC-POL-05 ¶45.

---

## Part 7 — The procedure in one table

24. | Stage | Who | Control | Record |
    |---|---|---|---|
    | 1 Found and reacted to | Anyone; Site Supervisor | Stop, make safe, mark and separate (¶9); disposition only by Quality Representative under SESC-POL-16 ¶47 (¶10) | SESC-FRM-05 opened; site diary |
    | 2 Recorded, same day | Finder; Contracts Manager | SESC-FRM-05 fields at ¶12; grade at ¶8; Managing Director told of any major | SESC-FRM-05 |
    | 3 Correction done | Owner | ¶11; not closure | SESC-FRM-05 correction entry |
    | 4 Investigated | Contracts Manager or allocated lead; workers on the job | ¶13 to ¶15; cause, not symptom; elsewhere checked | SESC-FRM-05 investigation entry; SESC-FRM-08 for participation |
    | 5 Corrective action decided | Contracts Manager; Managing Director for spend | ¶16 and ¶17; owner and date; registers updated | SESC-FRM-05 action entry; register rows; pull request where a document changes |
    | 6 Implemented | Owner | ¶19 periods; workforce briefed | SESC-FRM-05; SESC-FRM-06 |
    | 7 Verified and closed | Verifier other than owner | ¶18; evidence examined and named | SESC-FRM-05 verification entry |
    | 8 Reported monthly | Contracts Manager to Managing Director | ¶20 | Monthly report |
    | 9 Analysed at management review | Chief Operating Officer | ¶21 | Management review pack and minutes |

---

## Part 8 — Records held, records not yet held

25. This section is included so that this procedure can be read alongside the records that support
    it, **without overstating what exists or concealing what does not**. It is reviewed at every
    review of this procedure, and **an item is removed from it only when the record it describes
    exists**.

26. **Records that exist and support this procedure:**

    (a) SESC-FRM-05 Nonconformity and Corrective Action, draft v0.2 of 24 September 2026, the form
        schema this procedure operates, validated in the repository and not yet in use; SESC-FRM-01,
        SESC-FRM-02, SESC-FRM-06 and SESC-FRM-08 as drafts;

    (b) SESC-POL-16 Q14 (¶45 to ¶50) and Q20 (¶63), SESC-POL-05 A8 ¶50 and A24 (¶132 to ¶138), and
        SESC-POL-08 ¶39 and ¶59, the signed arrangements this procedure consolidates — each of which
        states that no log of the Employer's own existed at its issue and that one would open on
        31 August 2026;

    (c) SESC-REG-03 Accident, Incident and RIDDOR Register v1.0, the register of incidents; and

    (d) `portal/actions.yaml`, the project's own action list of blockers, decisions and findings,
        which is the project's management record and **is not the Employer's nonconformity log and
        is not offered as one**.

27. **Records and documents this procedure describes which do not yet exist.** Each carries the date
    by which it is created. **No earlier record of any of them exists and none is offered as
    evidence.** Dates marked *proposed* are proposed in this draft for the owner to confirm.

    | # | What does not exist | Position and date |
    |---|---|---|
    | (a) | **The Managing Director's signature on this procedure** | Not given. Owner: Managing Director. Due 30 November 2026 (*proposed*). |
    | (b) | **A nonconformity and corrective action log of the Employer's own — the first SESC-FRM-05 record** | None. Committed to open 31 August 2026 by SESC-POL-16 ¶63(b), SESC-POL-05 ¶50 and ¶172(j) — **overdue**. Opens with record capture go-live. Owner: Quality Representative; the go-live is the Chief Operating Officer's (B3). Due 30 November 2026 (*proposed*; the 9 October 2026 target has passed). |
    | (c) | **A completed investigation, a cause analysis, a corrective action or a verification of effectiveness, for any nonconformity** | None. First with the first record at (b). |
    | (d) | **The monthly report to the Managing Director at ¶20** | None. Committed for the month ending 30 September 2026 by SESC-POL-16 ¶63(c) and SESC-POL-05 ¶50 — **overdue**. First for the month in which (b) occurs. Owner: Contracts Manager. |
    | (e) | **A record of worker participation in an investigation (SESC-FRM-08)** | None; the mechanism has not run (SESC-IMS-05 Part 6(f)). |
    | (f) | **The measures at ¶23** | None. First at the management review after one full quarter of records. |
    | (g) | **Records belonging to others.** A non-conformance and corrective action log created during an earlier external consultancy engagement is held on shared drives (SESC-POL-16 ¶75). It is that consultant's record, carries another organisation's identity, and **is not offered, uploaded or relied on** as evidence of the Employer's arrangements. | Recorded here so that it is never mistaken for (b). |
    | (h) | **ISO 14001:2026, bought and read** | Not held. ISO 14001 clause references here are carried from the withdrawn 2015 edition and unverified (D27). |

28. **Certification claims.** The Employer holds no ISO 9001, ISO 14001, ISO 45001 or ISO/IEC 27001
    certification, no BS 99001 certification, no Cyber Essentials certification and no NFRC
    membership. None is to be claimed anywhere, in any document, in any tender, or on the website.

---

## Part 9 — Approval

29. This procedure is issued with the authority of the Board of Directors of SESC Solutions Ltd.

| | | | |
|---|---|---|---|
| **Prepared by** | Gary Adam Hill, Chief Operating Officer | **Date** | 26 October 2026 |
| **Reviewed by** | | **Date** | |
| **Approved by** | Steven A Coffen, Managing Director | **Date** | |
| **Signature** | | | |
| **Independent professional adviser appointed for the purposes of the sole-director clause** | Simon Davies FCCA | **Firm** | Rapture Accounts Limited |

---

## Annex A — Clause map

30. This procedure is declared in its front matter to satisfy the clauses below. **No clause is
    cited that this procedure does not genuinely address.** ISO 9001 clause 8.7, the control of
    nonconforming outputs, is not claimed here: the control and disposition of non-conforming work
    are at SESC-POL-16 Q14, which this procedure points to at ¶10 and does not restate. Clause 10.3
    is not claimed: the evidence of continual improvement is assembled at SESC-PRO-03 from this
    procedure's outputs and SESC-REG-08. Clause 9.2 is not claimed: audit findings arrive from
    SESC-PRO-02.

| Standard | Clauses | What in this procedure satisfies it |
|---|---|---|
| ISO 9001:2015 | 10.2.1 | Part 4 — react and control (¶9 to ¶11); evaluate the need for action by reviewing the nonconformity, determining its cause and whether similar nonconformities exist or could occur (¶13 to ¶15); implement action (¶16); review effectiveness (¶18); update risks and opportunities (¶17); change the system where necessary (¶16); proportionate to the effects (¶16) |
| ISO 9001:2015 | 10.2.2 | Part 4.2 and Part 5 — **retained documented information** on the nature of nonconformities and actions taken (¶12), and on the results of corrective action (¶18); **none yet exists — Part 8(b), (c)** |
| ISO 14001:2026 | 10.2 | As above, with environmental nonconformities and incidents at ¶7 and the regulator notification at ¶22. **Clause numbering carried from the withdrawn 2015 edition and marked unverified — see Part 8(h) and D27.** |
| ISO 45001:2018 | 10.2 | As above, with the participation of workers in the investigation and in determining corrective action (¶6, ¶13, ¶16), the assessment of OH&S risks before action that changes a control (¶16, ¶17), the review of the hazard identification and risk assessment (¶14, ¶17), and the communication of the record to workers (¶22) |

---

## Annex B — Revision history

| Version | Date | Author | Change |
|---|---|---|---|
| 0.1 | 26 October 2026 | G A Hill (drafted by Claude) | First draft, as workstream 6 of the Master Register (§6 item 6) and SESC-IMS-00 Part 10 (o) and (i). Consolidates SESC-POL-16 Q14 and Q20, SESC-POL-05 A8 and A24 and SESC-POL-08 ¶39 and ¶59 into one five-step procedure on one log (SESC-FRM-05), without changing the disposition rules at Q14; records the 31 August 2026 log-opening commitment as overdue rather than re-dating it. Written after reading every page of SESC-POL-05 v1.1, SESC-POL-08 v1.1 and SESC-POL-16 v1.2. Structure follows the stage / responsibility / control / record layout of a consultant's template procedure used as a layout only (Master Register §2h item 3); no content was taken from it or from any other organisation's document. Claims 10.2.1 and 10.2.2 (9001), 10.2 (14001), 10.2 (45001) only. **The Approval block at Part 9 is unsigned; no log has been opened.** |
