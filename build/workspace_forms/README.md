# Record capture on Google Workspace — setup runbook

**Workstream 1a · decision D15 · drafted 24 September 2026 by Claude for G A Hill · not yet run.**

This folder builds the Google Forms that start the operating-history clock (blocker **B3**).
It is build tooling, not a controlled document. The controlled documents are the schemas in
`forms/SESC-FRM-01…07` and the site sheet `documents/SESC-WI-01-how-to-log-a-record.md`.

| File | What it is |
|---|---|
| `export_forms.py` | Reads `forms/SESC-FRM-*.yaml` and writes `out/workspace-forms/SESC-Record-Forms.gs` (gitignored). |
| `Code.gs` | The Apps Script that builds the Forms, sheets, triggers and index. Pasted in after the generated definitions. |
| This file | The steps, in order, and who does each. |

**Nothing here is a decision of Steve's**, as long as it uses the Workspace SESC already pays
for. If any step needs a paid add-on, a new licence or a change to SESC's Google contract, stop:
that is spending, and it is Steve's decision.

---

## 1. What gets built

| Form | Who fills it in | Access (default) | Clauses the schema declares |
|---|---|---|---|
| FRM-01 Near miss and hazard | Anyone on site | **open**, anonymous | 45001 10.2 |
| FRM-02 Accident and incident | Anyone on site | **open** | 45001 10.2 |
| FRM-03 Training and competence | Contracts Manager | domain sign-in | 9001 / 14001 / 45001 7.2 |
| FRM-04 Supplier evaluation | Contracts Manager | domain sign-in | 9001 8.4.1, 8.4.2 · 14001 8.1 · 45001 8.1.4.2 |
| FRM-05 Nonconformity and corrective action | Quality Representative | domain sign-in | 9001 10.2.1, 10.2.2 · 14001 10.2 · 45001 10.2 |
| FRM-06 Toolbox talk | Supervisor delivering it | domain sign-in | 9001 7.3 · 14001 7.3 · 45001 5.4, 7.3, 7.4.2 |
| FRM-07 Site inspection | Health and Safety Officer, supervisors | domain sign-in | 9001 / 14001 / 45001 9.1.1 |

14001 clause numbers come from the `verified: false` map. **Do not quote them to anyone.**

Each form gets a response spreadsheet with three extra sheets:

- `_field_map`: every question tied to its schema **key**. When the records move to the SESC
  Platform, this is the mapping. Nothing has to be re-keyed.
- `_record_refs`: a reference for every entry (`FRM-07-0012`), with the time, whether it
  corrects an earlier entry, and whether it was a setup **test** or a **live** record.
- `_about`: which schema version built the form, where the schema lives, and the append-only rule.

It also builds a spreadsheet called **"SESC Record Forms - index"** listing every form link. That
link list goes onto the site sheet, SESC-WI-01.

---

## 2. Before anything else: Gary, in the Google Admin console

1. **2-step verification (B6).** Turn it on and enforce it for every account that will have
   access to the Shared Drive. Record the date in the register at B6. **Do not run step 5
   until this is done**, because the sheets will hold personal data (POL-14).
2. **Create the Shared Drive** `SESC Records`. Inside it, create one folder, `Record forms`.
3. **Add named members only.** No groups, no "anyone in the domain".
   - **Manager:** the SESC account that will run the script, plus one other person so the
     drive is never orphaned.
   - **Viewer or Commenter:** anyone who needs to read the records, such as Steve and James
     Milligan if he needs them. Nobody needs Editor. The forms write the records.
4. **Shared Drive settings:** switch off sharing with people outside the organisation.
   Switch off download, copy and print for commenters and viewers.
5. Open the `Record forms` folder. Copy the part of the address after `/folders/`. That is
   the folder ID.

## 3. Generate the script: Gary, macOS Terminal

Run these from the clone. The path contains a space, so it is quoted.

```zsh
cd "$HOME/Documents/SESC/ISO/CLAUDE ISO"
python3 build/workspace_forms/export_forms.py
open "out/workspace-forms"
```

Seven forms should be listed. The export refuses to write if a schema has a duplicate key,
an unknown field type, or no `correction_of` field.

## 4. Decide two things before you paste

Open `SESC-Record-Forms.gs` in TextEdit and look at `CONFIG` near the top of `Code.gs`.

1. **Access.** FRM-01 and FRM-02 are open to anyone with the link, because operatives &
   subcontractors report from a phone and may not have an SESC account. The rest need an SESC
   sign-in. **If supervisors do not have SESC accounts, FRM-06 and FRM-07 need to be open
   too.** Change `ACCESS` to suit, and record what you chose in the register.
2. **Who is emailed.** Add addresses under `NOTIFY`. At minimum, FRM-02 should email the
   Health and Safety Officer, because RIDDOR has deadlines. The email gives the record
   reference and the RIDDOR answer, never the description.

## 5. Photographs: the schema has them, the forms will not (decision D18)

Five schemas have a `file` field: photos, the evidence certificate and the signed attendance
sheet. **The script does not create these questions.** The `_field_map` records each one as
`NOT CREATED`, so the gap is on the record and cannot be missed. There are two reasons:

- Google's Apps Script `Form` class lists no method for adding a file upload question
  (checked 24 Sep 2026, developers.google.com/apps-script/reference/forms/form).
- A Google Docs Editors community guide says a file upload question forces respondents to
  sign in, and that **uploading files to a form held on a Shared Drive is not possible**. That
  is a community guide, not Google's own documentation. Test it before relying on it either
  way.

Until Gary decides otherwise, **photos are filed by hand.** Put them in a `Record photos`
folder in the Shared Drive and name each one with its record reference, for example
`FRM-07-0012-1.jpg`. Whoever receives the record does this. SESC-WI-01 tells site to send
photos to that person.

## 6. Build, then test: Gary

1. Sign in to the SESC Workspace account that is a **Manager** of the Shared Drive. Go to
   `script.google.com` and create a new project called `SESC Record Forms`.
2. Delete the sample code. Paste the whole of `SESC-Record-Forms.gs`. Set
   `CONFIG.FOLDER_ID` to the ID from §2.5. Save.
3. Select `buildAll`, then **Run**. Accept the permission prompts. They cover Forms, Sheets,
   Drive, triggers and sending email as that account.
4. **Read the execution log.** Every line starting `CHECK BY HAND` is a setting Google did
   not accept from the script. Set each one by hand in that form's Settings.
5. **Check every form in the Forms editor.** This is not optional, because a script that
   exits cleanly is not verification.
   - Each form says **Published** and is **accepting responses**. Google says forms created
     by API after 30 June 2026 start unpublished. If a form is not published, press
     **Publish**.
   - The responder setting matches §4: "Anyone with the link" for open forms, and your
     domain for domain forms.
   - **Allow response editing** is **off**.
   - The questions match the schema, in schema order.
6. **Make one test entry on every form**, with `TEST` as the site. Open FRM-01 and FRM-02 on a
   phone, in a private window, **signed out**. They must not ask for a sign-in. Check each
   test appears in its responses sheet, and in `_record_refs` marked `test`.
7. Try to type into a responses sheet as a second, non-owner account. **It must refuse.**
   If it does not, the append-only rule is not operating. Stop and fix the protection first.

## 7. Go live: Gary

1. In the script, select `markGoLive` and run it once. Entries made before this moment stay
   in the sheets, marked `test`. They are never deleted, but they do not count as records.
2. Open "SESC Record Forms - index". Send Claude the form links in the next chat, so the QR
   codes can go onto SESC-WI-01 and it can be rendered.
3. When the first **live** record arrives, run `clockStart`. **Put that date into the
   register at B3.** That is the day the operating-history clock starts. Remember that
   B3's gate is records created weekly **by someone other than Gary**.

## 8. Every month: whoever keeps the records index

Run `exportRecordsIndex`. It prints the metadata only: reference, date, form and clauses. It
leaves out answers, names and email addresses. Paste the output under `records:` in
`portal/records-index.yaml` and commit it by pull request. That is how the portal's twelve-month
staleness rule (`CLAUDE.md` §12.6) sees the records. **Nothing else from the sheets ever goes
into git** (`CLAUDE.md` §8).

## 9. Changing a form later

Change the YAML and bump its version by pull request, then re-export. **The script will not
rebuild a form it has already built**, because a rebuilt form orphans its responses. To add a
question to a live form, add it by hand in the Forms editor, **exactly** as the schema words
it. Then add a row to that form's `_field_map` with the new item ID. That is the one time the
field map is edited, and the sheet's version history records it.

## 10. Known limits, stated so nobody finds them later

- **The script account can still edit the sheets.** Protection stops everyone else, not the
  owner, and a Manager of the Shared Drive can remove protection. Append-only therefore rests
  on sheet protection, the version history and the rule. It is not tamper-proof. The SESC
  Platform is where tamper-evidence belongs.
- **Open forms prove nothing about who submitted them.** That is deliberate for near misses.
  FRM-02 has no "reported by" field at all (finding F26).
- **Testing so far:** the generator ran against a mock of Google's services on 24 Sep 2026.
  It built seven forms and seven triggers. A second run skipped all seven. It assigned
  references and marked test and live entries correctly, and the export left out test
  entries. **It has not yet run against real Google Workspace.** Section 6 is that test.
