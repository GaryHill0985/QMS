/**
 * SESC record capture on Google Workspace: the Forms generator.
 * Workstream 1a, decision D15. SESC-IMS-Master-Register.md, section 4.
 *
 * FORM_DEFS above this line is GENERATED from forms/SESC-FRM-*.yaml by
 * build/workspace_forms/export_forms.py. Change the YAML, never the generated file.
 *
 * What it does, once, when buildAll() is run by the SESC Workspace account:
 *   - one Google Form per FRM schema, with the fields in schema order;
 *   - one response spreadsheet per form, in the restricted Shared Drive folder;
 *   - a _field_map sheet tying every form question back to its schema KEY, which is
 *     the name the record carries when it moves to the SESC Platform;
 *   - a _record_refs sheet, and a submit trigger that gives every record a reference
 *     (FRM-01-0001 ...) so that a correction can point at the entry it corrects;
 *   - every sheet protected, so that responses are append-only (D15);
 *   - an index spreadsheet listing every form link, for the site sheet SESC-WI-01.
 *
 * It never rebuilds a form it has already built. Rebuilding would orphan the responses,
 * and a record that has lost its form is a record nobody can explain to an auditor.
 */

const CONFIG = {
  // The folder in the restricted Shared Drive. Open the folder in Drive; the ID is the
  // part of the address after /folders/.
  FOLDER_ID: 'PASTE-THE-SHARED-DRIVE-FOLDER-ID-HERE',

  // Who can fill in each form.
  //   'open'   anyone with the link, no sign-in, no email collected.
  //   'domain' must be signed in to the SESC Workspace; the verified email is recorded.
  // FRM-01 is open because its own guidance says a report with no name is valid.
  // FRM-02 is open because operatives & subcontractors report from a phone and may not
  // hold an SESC account. Everything else is filled by someone who holds one.
  // Gary to confirm; see README section 4.
  ACCESS: {
    'SESC-FRM-01': 'open',
    'SESC-FRM-02': 'open',
    default: 'domain',
  },

  // Who is emailed when a record arrives. The email carries the record reference, a link
  // and at most the fields named in NOTIFY_FIELDS. It never carries the free text, which
  // may be personal data (POL-14). Add addresses before running buildAll().
  NOTIFY: {
    // 'SESC-FRM-01': ['someone@your-sesc-domain'],
    // 'SESC-FRM-02': ['someone@your-sesc-domain'],
  },
  NOTIFY_FIELDS: {
    'SESC-FRM-01': ['potential_severity'],
    'SESC-FRM-02': ['riddor_likely'],   // RIDDOR has deadlines; the MD makes the report
    'SESC-FRM-05': ['action_due'],
    'SESC-FRM-07': ['stop_work', 'ncr_raised'],
  },

  INDEX_TITLE: 'SESC Record Forms - index',
};

const PLACEHOLDER = 'PASTE-THE-SHARED-DRIVE-FOLDER-ID-HERE';
const APPEND_ONLY = 'Append-only (D15). Never edit or delete a response. A correction is a ' +
  'new form entry that gives the original record reference.';

// ------------------------------------------------------------------ entry points

/** Run this once. Safe to run again: forms already built are skipped. */
function buildAll() {
  assertConfigured_();
  const props = PropertiesService.getScriptProperties();
  const folder = DriveApp.getFolderById(CONFIG.FOLDER_ID);
  FORM_DEFS.forEach(function (def) {
    const existing = props.getProperty('form:' + def.id);
    if (existing) {
      Logger.log(def.id + ': already built (form ' + existing + '). Skipped. Never rebuilt.');
      return;
    }
    buildForm_(def, folder, props);
  });
  writeIndex_(folder, props);
  Logger.log('Done. Open "' + CONFIG.INDEX_TITLE + '" in the Shared Drive for the links.');
}

/** Logs every form link. The same list is in the index spreadsheet. */
function listLinks() {
  const props = PropertiesService.getScriptProperties();
  FORM_DEFS.forEach(function (def) {
    const id = props.getProperty('form:' + def.id);
    if (!id) { Logger.log(def.id + ': not built'); return; }
    Logger.log(def.id + '  ' + FormApp.openById(id).getPublishedUrl());
  });
}

/**
 * Run once, after the test entries in README section 6 and before the forms go to site.
 * Entries submitted before this moment are marked 'test' in _record_refs, are left out of
 * exportRecordsIndex(), and do not start the clock. They are not deleted: append-only.
 */
function markGoLive() {
  const props = PropertiesService.getScriptProperties();
  if (props.getProperty('golive')) {
    Logger.log('Go-live already marked: ' + props.getProperty('golive') + '. Not changed.');
    return;
  }
  const now = new Date().toISOString();
  props.setProperty('golive', now);
  Logger.log('Go-live marked: ' + now);
}

/**
 * The B3 clock. Logs the date of the first LIVE record entered on any form. Put that date
 * in SESC-IMS-Master-Register.md at B3.
 */
function clockStart() {
  const props = PropertiesService.getScriptProperties();
  if (!props.getProperty('golive')) { Logger.log('Go-live not marked yet. Run markGoLive().'); return null; }
  const first = props.getProperty('clock:first');
  Logger.log(first ? 'First live record entered: ' + first : 'No live record entered yet.');
  return first;
}

/**
 * Prints record METADATA ONLY, as YAML for portal/records-index.yaml: the reference, the
 * date, the form and the clauses it evidences. No answers, no names, no emails.
 */
function exportRecordsIndex() {
  const props = PropertiesService.getScriptProperties();
  const out = [];
  FORM_DEFS.forEach(function (def) {
    const sheetId = props.getProperty('sheet:' + def.id);
    if (!sheetId) return;
    const rows = SpreadsheetApp.openById(sheetId).getSheetByName('_record_refs')
      .getDataRange().getValues().slice(1);
    rows.forEach(function (r) {
      if (r[5] !== 'live') return;   // setup tests are not records
      out.push('  - ref: ' + r[0]);
      out.push('    title: ' + def.title);
      out.push('    date: ' + isoDate_(r[1]));
      out.push('    form: ' + def.id);
      if (r[3]) out.push('    corrects: ' + r[3]);
      out.push('    clauses: ' + clausesYaml_(def.clauses));
    });
  });
  const text = out.join('\n');
  Logger.log(text || 'No records yet.');
  return text;
}

/** Installed as a form-submit trigger on every form by buildAll(). */
function onRecordSubmit(e) {
  const props = PropertiesService.getScriptProperties();
  const id = props.getProperty('def:' + e.source.getId());
  if (!id) return;
  const def = FORM_DEFS.filter(function (d) { return d.id === id; })[0];
  const lock = LockService.getScriptLock();
  lock.waitLock(30000);
  try {
    const seq = Number(props.getProperty('seq:' + id) || '0') + 1;
    props.setProperty('seq:' + id, String(seq));
    const ref = id.replace('SESC-', '') + '-' + ('000' + seq).slice(-4);

    const ss = SpreadsheetApp.openById(props.getProperty('sheet:' + id));
    const keyByItem = {};
    ss.getSheetByName('_field_map').getDataRange().getValues().slice(1)
      .forEach(function (row) { if (row[4]) keyByItem[String(row[4])] = row[0]; });
    const answers = {};
    e.response.getItemResponses().forEach(function (ir) {
      answers[keyByItem[String(ir.getItem().getId())]] = ir.getResponse();
    });

    const when = e.response.getTimestamp();
    const golive = props.getProperty('golive');
    const phase = golive && when.toISOString() >= golive ? 'live' : 'test';
    ss.getSheetByName('_record_refs').appendRow([
      ref, when, e.response.getId(), answers.correction_of || '',
      e.response.getRespondentEmail() || '', phase,
    ]);
    if (phase === 'live' && !props.getProperty('clock:first')) {
      props.setProperty('clock:first', when.toISOString());
    }
    notify_(def, ref, answers, ss);
  } finally {
    lock.releaseLock();
  }
}

// ------------------------------------------------------------------ building

function buildForm_(def, folder, props) {
  const access = CONFIG.ACCESS[def.id] || CONFIG.ACCESS['default'];
  const form = FormApp.create(def.id + ' ' + def.title);
  form.setDescription(description_(def, access))
    .setAllowResponseEdits(false)
    .setConfirmationMessage('Received. Thank you. This record cannot be edited now. ' +
      'If something in it is wrong, submit the form again and say what it corrects.');
  // Settings whose availability could not be confirmed from Google's documentation on
  // 24 Sep 2026 are applied one at a time. A failure is logged as CHECK BY HAND, not
  // swallowed, and README section 6 has the check.
  setting_(def, form, 'setCollectEmail', access === 'domain');
  setting_(def, form, 'setRequireLogin', access === 'domain');
  setting_(def, form, 'setLimitOneResponsePerUser', false);
  setting_(def, form, 'setShowLinkToRespondAgain', true);
  setting_(def, form, 'setPublishingSummary', false);
  // Google: forms created by API after 30 June 2026 are created unpublished. Publish if the
  // Apps Script method exists; otherwise README section 6 says to press Publish by hand.
  setting_(def, form, 'setPublished', true);
  setting_(def, form, 'setAcceptingResponses', true);

  const map = def.fields.map(function (f) {
    const item = addItem_(form, f);
    return [f.key, f.label, f.type, f.required ? 'yes' : 'no',
      item ? String(item.getId()) : '',
      item ? 'created' : 'NOT CREATED: a file upload question cannot be made by script. See README section 5.'];
  });

  const created = SpreadsheetApp.create(def.id + ' ' + def.title + ' - responses');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, created.getId());
  SpreadsheetApp.flush();
  const ss = SpreadsheetApp.openById(created.getId());

  const fm = ss.insertSheet('_field_map');
  fm.getRange(1, 1, 1, 6).setValues([['key', 'label', 'type', 'required', 'form_item_id', 'status']]);
  fm.getRange(2, 1, map.length, 6).setValues(map);

  ss.insertSheet('_record_refs')
    .appendRow(['record_ref', 'submitted', 'response_id', 'correction_of', 'respondent_email', 'phase']);

  const about = ss.insertSheet('_about');
  about.getRange(1, 1, 8, 2).setValues([
    ['form', def.id + ' ' + def.title],
    ['schema version', def.version + ' (' + def.status + ')'],
    ['schema source', 'github.com/GaryHill0985/QMS  ' + def.source],
    ['owner', def.owner],
    ['access', access],
    ['built', new Date().toISOString()],
    ['rule', APPEND_ONLY],
    ['personal data', 'May hold personal data (POL-14). Never copied into git. See CLAUDE.md section 8.'],
  ]);

  const blank = ss.getSheetByName('Sheet1');
  if (blank && ss.getSheets().length > 1) ss.deleteSheet(blank);
  ss.getSheets().forEach(protect_);

  DriveApp.getFileById(form.getId()).moveTo(folder);
  DriveApp.getFileById(ss.getId()).moveTo(folder);
  ScriptApp.newTrigger('onRecordSubmit').forForm(form).onFormSubmit().create();

  const p = {};
  p['form:' + def.id] = form.getId();
  p['sheet:' + def.id] = ss.getId();
  p['def:' + form.getId()] = def.id;
  p['seq:' + def.id] = '0';
  props.setProperties(p);
  Logger.log(def.id + ': built. ' + form.getPublishedUrl());
}

function setting_(def, form, method, value) {
  if (typeof form[method] !== 'function') {
    Logger.log('CHECK BY HAND  ' + def.id + ': ' + method + ' is not available. Set it in the Forms settings.');
    return;
  }
  try {
    form[method](value);
  } catch (err) {
    Logger.log('CHECK BY HAND  ' + def.id + ': ' + method + '(' + value + ') failed: ' + err.message);
  }
}

function addItem_(form, f) {
  let item;
  switch (f.type) {
    case 'date': item = form.addDateItem(); break;
    case 'time': item = form.addTimeItem(); break;
    case 'text': item = form.addTextItem(); break;
    case 'textarea': item = form.addParagraphTextItem(); break;
    case 'number':
      item = form.addTextItem().setValidation(FormApp.createTextValidation()
        .setHelpText('A whole number.').requireWholeNumber().build());
      break;
    case 'select':
      // Radio buttons read better on a phone; long lists become a dropdown.
      item = (f.options.length <= 6 ? form.addMultipleChoiceItem() : form.addListItem())
        .setChoiceValues(f.options);
      break;
    case 'multiselect': item = form.addCheckboxItem().setChoiceValues(f.options); break;
    case 'file': return null;
    default: throw new Error('Unknown field type ' + f.type + ' for ' + f.key);
  }
  item.setTitle(f.label).setRequired(f.required);
  if (f.help) item.setHelpText(f.help);
  return item;
}

function description_(def, access) {
  const lines = [def.purpose, ''];
  def.guidance.forEach(function (g) { lines.push('- ' + g); });
  if (def.guidance.length) lines.push('');
  lines.push(access === 'open'
    ? 'No sign-in is needed.'
    : 'You must be signed in to your SESC account. Your email address is recorded with the entry.');
  lines.push('This creates a controlled record and cannot be edited after you submit.');
  lines.push(def.id + ' version ' + def.version + ' (' + def.status + ').');
  return lines.join('\n');
}

function protect_(sheet) {
  const p = sheet.protect().setDescription(APPEND_ONLY);
  const me = Session.getEffectiveUser();
  p.addEditor(me);
  p.removeEditors(p.getEditors().filter(function (u) { return u.getEmail() !== me.getEmail(); }));
  if (p.canDomainEdit()) p.setDomainEdit(false);
}

function writeIndex_(folder, props) {
  let ss;
  const existing = props.getProperty('index');
  if (existing) {
    ss = SpreadsheetApp.openById(existing);
  } else {
    ss = SpreadsheetApp.create(CONFIG.INDEX_TITLE);
    DriveApp.getFileById(ss.getId()).moveTo(folder);
    props.setProperty('index', ss.getId());
  }
  const sh = ss.getSheets()[0];
  const rows = [['form', 'title', 'schema version', 'access', 'form link (for site)', 'responses sheet']];
  FORM_DEFS.forEach(function (def) {
    const f = props.getProperty('form:' + def.id);
    const s = props.getProperty('sheet:' + def.id);
    rows.push([def.id, def.title, def.version, CONFIG.ACCESS[def.id] || CONFIG.ACCESS['default'],
      f ? FormApp.openById(f).getPublishedUrl() : 'not built',
      s ? SpreadsheetApp.openById(s).getUrl() : '']);
  });
  sh.clear();
  sh.getRange(1, 1, rows.length, rows[0].length).setValues(rows);
}

function notify_(def, ref, answers, ss) {
  const to = CONFIG.NOTIFY[def.id];
  if (!to || !to.length) return;
  const extra = (CONFIG.NOTIFY_FIELDS[def.id] || []).map(function (k) {
    const f = def.fields.filter(function (x) { return x.key === k; })[0];
    return (f ? f.label : k) + ': ' + (answers[k] === undefined ? '(blank)' : answers[k]);
  });
  MailApp.sendEmail({
    to: to.join(','),
    subject: ref + ' - new ' + def.title,
    body: ['A new ' + def.title + ' has been recorded as ' + ref + '.', '']
      .concat(extra, ['', 'Responses: ' + ss.getUrl(), '',
        'The content is not in this email because it may contain personal data.']).join('\n'),
  });
}

// ------------------------------------------------------------------ helpers

function assertConfigured_() {
  if (!CONFIG.FOLDER_ID || CONFIG.FOLDER_ID === PLACEHOLDER) {
    throw new Error('Set CONFIG.FOLDER_ID to the Shared Drive folder before running buildAll().');
  }
}

function isoDate_(v) {
  const d = v instanceof Date ? v : new Date(v);
  return Utilities.formatDate(d, 'Europe/London', 'yyyy-MM-dd');
}

function clausesYaml_(c) {
  return '{' + Object.keys(c).map(function (k) {
    return k + ': [' + c[k].map(function (x) { return '"' + x + '"'; }).join(', ') + ']';
  }).join(', ') + '}';
}
