#!/usr/bin/env python3
"""
build_portal.py — generates the SESC IMS portal into site/.

    python3 build/build_portal.py                # all four audience builds
    python3 build/build_portal.py --audience auditor
    python3 build/build_portal.py --asof 2026-12-01   # what it looked like then

NOTHING IN site/ IS WRITTEN BY HAND. Every page is generated from:

    standards/*.yaml      the clause map
    system/*.md           the Annex SL spine, read for its front matter
    registers/*.yaml      the registers
    forms/*.yaml          the record capture schemas
    portal/config.yaml    organisation facts and the audience model
    registers/documents.yaml  SESC-REG-07, the legacy document estate (PDFs outside the repo)
    portal/obligations.yaml   SESC-REG-02 as data
    portal/actions.yaml   blockers, decisions, findings and gaps

Edit the source. Re-run. Never patch site/ — the next run overwrites it, and a
hand-patched copy is the one an auditor reads.

WHY THIS IS A GENERATOR AND NOT AN APPLICATION
    A generated site cannot be edited by the person reading it, which is the
    point. Clause coverage is computed from what documents actually declare, so
    it cannot be talked up. The gap list is derived, so an item leaves it when
    the evidence exists, not when somebody decides it does not matter.

    Audiences are DISTRIBUTION, not authentication. Each audience gets its own
    build with content it must not see left out. Handing the auditor build to an
    auditor is a real control. It is not a login and this portal never pretends
    it is.
"""

import argparse, datetime, glob, html, json, os, re, sys
from collections import defaultdict

try:
    import yaml
except ImportError:
    sys.exit("build_portal.py needs PyYAML:  pip install pyyaml")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from portal_theme import CSS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = lambda s: html.escape(str(s if s is not None else ""), quote=True)


NEVER_TAG = ' <span class="tag t-bad">never done</span>'
DUAL_TAG = '<span class="tag t-bad">dual</span>'


def tag_mut(x):
    return '<span class="tag t-mut">' + E(x) + '</span> '


def flat(s):
    """YAML folded blocks arrive with newlines. Collapse them for HTML."""
    return " ".join(str(s or "").split())


def load(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def front_matter(path):
    """Front matter of a controlled source file. .md is fenced, .yaml is the file."""
    text = open(path, encoding="utf-8").read()
    if path.endswith((".yaml", ".yml")):
        return yaml.safe_load(text)
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    return yaml.safe_load(text[3:end]) if end != -1 else None


def d(v):
    if isinstance(v, datetime.date):
        return v
    if isinstance(v, str):
        for f in ("%Y-%m-%d", "%Y-%m"):
            try:
                return datetime.datetime.strptime(v, f).date()
            except ValueError:
                pass
    return None


def uk(v):
    dt = d(v)
    if dt:
        return dt.strftime("%-d %B %Y") if len(str(v)) > 7 else dt.strftime("%B %Y")
    return str(v) if v else "—"


# ══════════════════════════════════════════════════════════════════ load

class System:
    def __init__(self, asof):
        self.asof = asof
        self.cfg = load("portal/config.yaml")
        self.docs_legacy = load("registers/documents.yaml")   # SESC-REG-07
        self.obl = load("portal/obligations.yaml")
        self.act = load("portal/actions.yaml")
        self.recidx = load("portal/records-index.yaml")

        # clause maps
        self.std = {}
        for s in self.cfg["standards"]:
            raw = load(s["file"])
            self.std[s["key"]] = {
                "label": s["label"], "edition": str(raw.get("edition")),
                "verified": bool(raw.get("verified")), "note": flat(raw.get("verified_note")),
                "clauses": [{
                    "id": str(c["id"]), "title": c.get("title", ""),
                    "di": c.get("documented_information", False),
                    "note": flat(c.get("note")),
                    "dual": bool(c.get("dual_maintain_and_retain")),
                    "critical": bool(c.get("critical")),
                } for c in raw["clauses"]],
            }

        # controlled source files in the repository — these are the only things
        # that can evidence a clause, because they are the only things that
        # declare one.
        self.controlled = []
        for folder in ("system", "documents", "registers", "forms"):
            for pat in ("*.md", "*.yaml"):
                for p in sorted(glob.glob(os.path.join(ROOT, folder, "**", pat), recursive=True)):
                    fm = front_matter(p)
                    if not fm or "id" not in fm:
                        continue
                    fm["_path"] = os.path.relpath(p, ROOT).replace("\\", "/")
                    fm["_folder"] = folder
                    self.controlled.append(fm)

        self.by_id = {c["id"]: c for c in self.controlled}
        self._map_clauses()
        self._map_records()

    def _map_clauses(self):
        """clause -> the controlled files that declare it. Declared, not guessed."""
        self.cite = defaultdict(list)          # (std, clause) -> [fm]
        for fm in self.controlled:
            for skey, ids in (fm.get("clauses") or {}).items():
                for cid in ids or []:
                    self.cite[(skey, str(cid))].append(fm)

    def _map_records(self):
        """clause -> records within the staleness window. CLAUDE.md 12.6."""
        months = self.recidx.get("window_months", 12)
        cutoff = self.asof - datetime.timedelta(days=int(months * 30.44))
        self.recs = defaultdict(list)
        for r in self.recidx.get("records", []):
            rd = d(r.get("date"))
            if not rd or rd < cutoff:
                continue
            for skey, ids in (r.get("clauses") or {}).items():
                for cid in ids or []:
                    self.recs[(skey, str(cid))].append(r)

    def clause_state(self, skey, cid):
        """CLAUDE.md 12.6 — a document with no record in twelve months is not coverage.

        evidenced  approved document AND a record inside the window
        documented approved document, no record inside the window
        drafted    only draft documents
        absent     nothing declares it
        """
        cites = self.cite.get((skey, cid), [])
        recent = self.recs.get((skey, cid), [])
        if any(c.get("status") == "approved" for c in cites):
            state = "evidenced" if recent else "documented"
        elif cites:
            state = "drafted"
        else:
            state = "absent"
        return state, cites

    # ---------------------------------------------------------- obligations
    def obligations(self):
        out = []
        for o in self.obl["obligations"]:
            due, last = d(o.get("next_due")), d(o.get("last_done"))
            days = (due - self.asof).days if due else None
            out.append({**o, "_due": due, "_last": last, "_days": days,
                        "_never": last is None,
                        "_overdue": bool(due and due < self.asof),
                        "_soon": bool(days is not None and 0 <= days <= 30)})
        out.sort(key=lambda x: (x["_due"] or datetime.date(2099, 1, 1)))
        return out

    # ------------------------------------------------------------- actions
    def actions(self, audience):
        internal_ok = next(a["sees_internal"] for a in self.cfg["audiences"] if a["key"] == audience)
        rank = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        out = [a for a in self.act["actions"]
               if (internal_ok or not a.get("internal"))
               and a.get("status") != "closed"]
        out.sort(key=lambda a: (rank.get(a.get("severity"), 9),
                                d(a.get("due")) or datetime.date(2099, 1, 1)))
        return out


# ══════════════════════════════════════════════════════════════════ chrome

PAGES = [
    ("index",     "Overview",   ["controller", "approver", "contributor", "auditor"]),
    ("clauses",   "Clause map", ["controller", "approver", "auditor"]),
    ("documents", "Documents",  ["controller", "approver", "contributor", "auditor"]),
    ("registers", "Registers",  ["controller", "approver", "auditor"]),
    ("calendar",  "Calendar",   ["controller", "approver", "contributor", "auditor"]),
    ("actions",   "Actions",    ["controller", "approver", "auditor"]),
    ("records",   "Raise a record", ["controller", "contributor"]),
    ("audit",     "Audit mode", ["controller", "approver", "auditor"]),
    ("about",     "About",      ["controller", "approver", "contributor", "auditor"]),
]
TITLE_FOR = {"auditor": {"actions": "Known gaps"}}


def page(sysm, audience, slug, heading, strap, body):
    aud = next(a for a in sysm.cfg["audiences"] if a["key"] == audience)
    org = sysm.cfg["organisation"]
    if slug == "__chooser__":
        nav = "".join(f'<a href="{a["key"]}/index.html">{E(a["name"])}</a>'
                      for a in sysm.cfg["audiences"])
        audline = "pick a build"
    else:
        nav = "".join(
            f'<a href="{s}.html" class="{"on" if s == slug else ""}">'
            f'{E(TITLE_FOR.get(audience, {}).get(s, t))}</a>'
            for s, t, auds in PAGES if audience in auds)
        audline = f'build for <b>{E(aud["name"])}</b> &middot; {E(aud["holder"])}'
    return f"""<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(heading)} · SESC IMS portal</title>
<style>{CSS}</style></head><body>
<div class="brandrule"></div>
<header class="masthead"><div class="wrap">
<h1>{E(heading)}</h1>
<div class="sub">{E(strap)}</div>
<div class="sub">{E(org['legal_name'])} &middot; company {E(org['company_number'])}
&middot; Integrated Management System &mdash; ISO 9001, ISO 14001, ISO 45001
&middot; generated {sysm.asof.strftime('%-d %B %Y')}</div>
</div></header>
<nav class="tabs"><div class="wrap">{nav}
<div class="aud">{audline}</div>
</div></nav>
<main><div class="wrap">
{body}
<footer>
<p><strong>Generated by <code>build/build_portal.py</code> from the <code>sesc-ims</code>
repository. Not maintained by hand.</strong> Edit the source and re-run. Anything typed
into this folder is lost on the next build, and a hand-patched copy is the one an
auditor reads.</p>
<p>{'' if slug == "__chooser__" else f"This is the <strong>{E(aud['name'])}</strong> build. {E(flat(aud['summary']))}"}
Audiences are separated by distribution, not by login &mdash; a generated site cannot
authenticate anybody, and this one does not pretend to.</p>
<p>SESC holds <strong>no ISO certification of any kind</strong> and does not claim to.
No certification body has ever assessed the Employer. Companies are certified;
certification bodies are accredited.</p>
</footer>
</div></main></body></html>"""


def bar(parts):
    """parts = [(count, css-class), ...]"""
    total = sum(c for c, _ in parts) or 1
    segs = "".join(f'<i class="{cls}" style="width:{100*c/total:.2f}%"></i>' for c, cls in parts if c)
    return f'<div class="bar">{segs}</div>'


def filter_bar(select_specs, count_label, extra=""):
    sels = "".join(
        f'<label for="{sid}">{E(lbl)}</label><select id="{sid}" data-col="{col}">'
        + "".join(f'<option value="{E(v)}">{E(t)}</option>' for v, t in opts) + "</select>"
        for sid, lbl, col, opts in select_specs)
    return (f'<div class="ctl"><input type="search" id="q" placeholder="Search&hellip;" '
            f'aria-label="Search">{sels}{extra}'
            f'<span class="count" id="count">{E(count_label)}</span></div>')


FILTER_JS = """
<script>
(function(){
 var q=document.getElementById('q'),cnt=document.getElementById('count'),
     tbl=document.querySelector('table[data-filter]'),
     rows=tbl?[].slice.call(tbl.tBodies[0].rows):[].slice.call(document.querySelectorAll('[data-row]')),
     sels=[].slice.call(document.querySelectorAll('.ctl select')),
     noun=cnt?cnt.getAttribute('data-noun')||'rows':'rows';
 function run(){
  var t=(q&&q.value||'').toLowerCase(),n=0;
  rows.forEach(function(r){
   var ok=!t||r.textContent.toLowerCase().indexOf(t)>-1;
   sels.forEach(function(s){
    if(ok&&s.value){var k=s.getAttribute('data-col');
     ok=((r.getAttribute('data-'+k)||'')+'').split('|').indexOf(s.value)>-1;}
   });
   r.classList.toggle('hidden',!ok); if(ok)n++;
  });
  if(cnt)cnt.textContent=n+' of '+rows.length+' '+noun;
 }
 if(q)q.addEventListener('input',run); sels.forEach(function(s){s.addEventListener('change',run)});
 run();
})();
</script>"""


# ══════════════════════════════════════════════════════════════════ pages

def p_index(s, aud):
    obs = s.obligations()
    never = [o for o in obs if o["_never"]]
    overdue = [o for o in obs if o["_overdue"]]
    soon = [o for o in obs if o["_soon"] and not o["_overdue"]]
    acts = s.actions(aud)
    crit = [a for a in acts if a.get("severity") == "critical"]

    # clause arithmetic
    tot = appr = docd = draft = 0
    per = []
    for k, st in s.std.items():
        a = dc = dd = 0
        for c in st["clauses"]:
            state, _ = s.clause_state(k, c["id"])
            a += state == "evidenced"
            dc += state == "documented"
            dd += state == "drafted"
        n = len(st["clauses"])
        tot += n; appr += a; docd += dc; draft += dd
        per.append((k, st, n, a, dc, dd))

    mine = ""
    if aud in ("approver", "contributor"):
        role = {"approver": "Managing Director",
                "contributor": ("Contracts Manager", "Accounts Manager")}[aud]
        roles = (role,) if isinstance(role, str) else role
        m = [o for o in obs if o["owner"] in roles]
        mo = [o for o in m if o["_overdue"] or o["_never"]]
        mine = (f'<div class="card {"bad" if mo else "ok"}"><h3>Owned by you</h3>'
                f'<p><strong>{len(m)}</strong> recurring obligations are owned by '
                f'{E(" or ".join(roles))}, of which <strong>{len(mo)}</strong> are overdue or '
                f'have never been carried out. The calendar lists them.</p></div>')

    milestones = "".join(
        f'<tr><td class="num">{E(uk(m["date"]))}</td><td class="num">'
        f'{(d(m["date"]) - s.asof).days} days</td><td><strong>{E(m["label"])}</strong><br>'
        f'<span class="sub">{E(flat(m.get("note")))}</span></td></tr>'
        for m in sorted(s.cfg["milestones"], key=lambda x: d(x["date"])))

    body = f"""
<div class="card bad"><h3>Where this system actually is</h3>
<p><strong>{appr} of {tot} clauses across the three standards are evidenced.</strong>
{docd} are covered by an approved document with no record behind it in the last twelve months,
{draft} more are addressed only by a draft, and the remaining {tot - appr - docd - draft} are
not addressed by anything in this repository.</p>
<p>That number is low because it is computed, not asserted, and because it applies the gap
report definition at <code>CLAUDE.md</code> &sect;12.6: <em>a clause covered by a document
nobody has used in a year is not covered</em>. A clause counts only when a controlled file in
this repository declares it in front matter <strong>and</strong> a record inside the window
sits behind it. The twenty-one signed policy documents declare nothing, because they have not
been migrated in and carry no front matter &mdash; see the document register.
<strong>Nothing here is padded to look better than it is.</strong> A green gap report over an
empty system is worse than a red one.</p></div>

<div class="stats">
<div class="stat {'bad' if appr == 0 else 'ok'}"><div class="v">{appr}/{tot}</div>
  <div class="k">clauses evidenced &mdash; document and a record</div></div>
<div class="stat {'bad' if never else 'ok'}"><div class="v">{len(never)}</div>
  <div class="k">recurring obligations never carried out</div></div>
<div class="stat {'bad' if overdue else 'ok'}"><div class="v">{len(overdue)}</div>
  <div class="k">obligations overdue today</div></div>
<div class="stat warn"><div class="v">{len(soon)}</div>
  <div class="k">due in the next 30 days</div></div>
<div class="stat {'bad' if crit else 'ok'}"><div class="v">{len(crit)}</div>
  <div class="k">critical open items</div></div>
</div>
{mine}

<h2>Clause coverage, by standard</h2>
<div class="legend" style="margin-bottom:8px">
<span><b style="background:#137a4a"></b>evidenced</span>
<span><b style="background:#0b4f8a"></b>document, no recent record</span>
<span><b style="background:#d9a441"></b>draft only</span>
<span><b style="background:#e5e9ee"></b>nothing</span></div>
<div class="grid">"""
    for k, st, n, a, dc, dd in per:
        warn = ("" if st["verified"] else
                '<div class="s" style="color:#a01b2b;margin-top:6px"><strong>Clause map '
                'UNVERIFIED.</strong> The edition has not been read. Do not quote these '
                'clause numbers to a customer or an auditor.</div>')
        body += (f'<div class="tile"><div class="n">{E(st["label"])}:{E(st["edition"])}</div>'
                 f'<div class="t">{a} of {n} evidenced</div>'
                 f'{bar([(a, "b-ok"), (dc, "b-doc"), (dd, "b-warn"), (n - a - dc - dd, "b-bad")])}'
                 f'<div class="s">{dc} document only &middot; {dd} draft &middot; '
                 f'{n - a - dc - dd} unaddressed</div>{warn}</div>')
    body += "</div>"

    if overdue or soon:
        body += "<h2>Due now, or within thirty days</h2><table><tr><th>Due</th><th>Obligation</th>"\
                "<th>Owner</th><th>Record it produces</th></tr>"
        for o in (overdue + soon)[:14]:
            cls = "overdue" if o["_overdue"] else "soon"
            lab = "OVERDUE " if o["_overdue"] else ""
            body += (f'<tr><td class="num {cls}">{lab}{E(uk(o["_due"]))}</td>'
                     f'<td>{E(flat(o["obligation"]))}{NEVER_TAG if o["_never"] else ""}</td>'
                     f'<td>{E(o["owner"])}</td><td>{E(flat(o["record"]))}</td></tr>')
        body += "</table>"

    if crit:
        body += "<h2>Critical, open</h2>"
        for a in crit:
            body += (f'<div class="card bad"><h3><code>{E(a["ref"])}</code> {E(a["title"])}</h3>'
                     f'<p>{E(flat(a["detail"]))}</p><p class="sub">Owner {E(a["owner"])}'
                     f'{" &middot; due " + E(uk(a["due"])) if a.get("due") else ""}</p></div>')

    body += f"<h2>Dates that are fixed</h2><table><tr><th>Date</th><th>In</th><th>What</th></tr>{milestones}</table>"

    body += """
<h2>What this portal is not</h2>
<div class="card warn">
<p><strong>It is not an editor and it is not a login.</strong> It is generated from the
repository every time the build is run. Nobody can change a status by typing into it, which
is the property that makes the numbers above worth reading.</p>
<p><strong>It holds no personal data.</strong> Health surveillance, occupational health,
individual training records, accident detail naming individuals, DBS outcomes, right-to-work
scans, disciplinary and Speak Up reports never enter the repository and so never reach these
pages. Git history is immutable and replicated, which is exactly wrong for a UK GDPR erasure
request and for Article 9 data.</p>
<p><strong>It does not evidence certification.</strong> It evidences the state of a system
being built towards it.</p></div>"""
    return body


def p_clauses(s, aud):
    specs = [("fstd", "Standard", "std",
              [("", "All three")] + [(k, s.std[k]["label"]) for k in s.std]),
             ("fstate", "State", "state",
              [("", "Any"), ("evidenced", "Evidenced"),
               ("documented", "Document, no recent record"),
               ("drafted", "Draft only"), ("absent", "Nothing")]),
             ("fdi", "Documented information", "di",
              [("", "Any"), ("maintain", "Maintain — a document"),
               ("retain", "Retain — a record"), ("both", "Both"), ("none", "Neither")])]
    out = ['<div class="card info"><h3>The clause map is the point</h3>'
           '<p>Every clause of all three standards, and what in this repository declares it. '
           'A clause turns green only when an <strong>approved</strong> controlled file names it '
           'in its front matter. Nothing is inferred from a document title.</p>'
           '<p><strong>Read <code>documented information: retain</code> as "a record, not a '
           'policy".</strong> Those are the clauses a certification body cannot be talked out '
           'of, and they are where SESC is thinnest. The five ISO 45001 dual '
           '<em>maintain AND retain</em> clauses need both, and are the most commonly missed '
           'requirements in the whole set.</p>'
           '<p><strong>The staleness rule is applied.</strong> <code>CLAUDE.md</code> '
           '&sect;12.6: a clause with an artefact but no record in the last twelve months is '
           'not covered. A clause is <em>evidenced</em> only where an approved document names '
           'it <em>and</em> a record inside the window sits behind it; otherwise it reads '
           '<em>document, no recent record</em>. Records are indexed at '
           '<code>portal/records-index.yaml</code>, metadata only &mdash; four records exist '
           'in the whole company and none is yet mapped to a clause.</p></div>',
           filter_bar(specs, "", ""), '<div id="clauselist">']

    banners = "".join(
        f'<div class="card bad"><h3>{E(st["label"])}:{E(st["edition"])} — clause map '
        f'UNVERIFIED</h3><p>{E(st["note"])}</p></div>'
        for st in s.std.values() if not st["verified"])
    out.insert(1, banners)

    n = 0
    for k, st in s.std.items():
        for c in st["clauses"]:
            n += 1
            state, cites = s.clause_state(k, c["id"])
            di = c["di"] if c["di"] in ("maintain", "retain", "both") else "none"
            tag = {"evidenced": '<span class="tag t-ok">evidenced</span>',
                   "documented": '<span class="tag t-acc">document, no recent record</span>',
                   "drafted": '<span class="tag t-warn">draft only</span>',
                   "absent": '<span class="tag t-bad">nothing</span>'}[state]
            ditag = {"maintain": '<span class="tag t-acc">document</span>',
                     "retain": '<span class="tag t-acc">RECORD required</span>',
                     "both": '<span class="tag t-acc">document + RECORD</span>',
                     "none": ""}[di]
            extra = ""
            if c["dual"]:
                extra += ' <span class="tag t-bad">dual maintain AND retain</span>'
            if c["critical"]:
                extra += ' <span class="tag t-bad">critical</span>'
            if cites:
                ev = "<table><tr><th>Declared by</th><th>Ref</th><th>Status</th><th>Version</th></tr>"
                for fm in cites:
                    stt = fm.get("status", "—")
                    cls = "t-ok" if stt == "approved" else "t-warn"
                    ev += (f'<tr><td>{E(fm["title"])}<br><span class="sub">'
                           f'<code>{E(fm["_path"])}</code></span></td><td><code>{E(fm["id"])}</code></td>'
                           f'<td><span class="tag {cls}">{E(stt)}</span></td>'
                           f'<td>{E(fm.get("version", "—"))}</td></tr>')
                ev += "</table>"
            else:
                ev = ('<p><strong>Nothing in this repository declares this clause.</strong> '
                      'It may well be addressed by one of the twenty-one signed policy documents, '
                      'but those carry no front matter, so no claim is made here. A clause map '
                      'built from titles is worthless to an auditor and dangerous to the '
                      'business.</p>')
            recwarn = ""
            if di in ("retain", "both") or c["dual"]:
                recwarn = ('<p class="card bad" style="margin:8px 0"><strong>A retained record '
                           'is required, and the records layer is empty.</strong> Four records '
                           'exist in the whole company, all dated 17 August 2026. This is the '
                           'gap that time and operation close, not writing.</p>')
            out.append(
                f'<details class="cl" data-row data-std="{k}" data-state="{state}" data-di="{di}">'
                f'<summary><span class="tag t-mut">{E(st["label"].replace("ISO ", ""))}</span>'
                f'<span class="cid">{E(c["id"])}</span>'
                f'<span style="flex:1">{E(c["title"])}</span>{tag} {ditag}{extra}</summary>'
                f'<div class="body">'
                f'<p class="sub">{E(st["label"])}:{E(st["edition"])} clause {E(c["id"])}</p>'
                + (f'<p>{E(c["note"])}</p>' if c["note"] else "")
                + ev + recwarn + '</div></details>')
    out.append("</div>")
    out.append(FILTER_JS.replace("'rows'", "'clauses'"))
    body = "\n".join(out)
    return body.replace('id="count">', 'id="count" data-noun="clauses">')


def p_documents(s, aud):
    rows = []
    legacy = [x for x in s.docs_legacy["documents"] if aud in x.get("audiences", [])]
    for x in legacy:
        st = x.get("state", "—")
        cls = {"signed": "t-ok", "issued": "t-ok", "record": "t-acc",
               "missing": "t-bad"}.get(st, "t-mut")
        defect = (f'<div style="margin-top:5px"><span class="tag t-bad">defect</span> '
                  f'<span class="sub">{E(flat(x["defect"]))}</span></div>') if x.get("defect") else ""
        note = (f'<div class="sub" style="margin-top:4px">{E(flat(x["note"]))}</div>'
                if x.get("note") else "")
        rows.append(
            f'<tr data-row data-state="{E(st)}" data-loc="legacy" data-map="pending">'
            f'<td><code>{E(x["ref"])}</code></td>'
            f'<td><strong>{E(x["title"])}</strong>{note}{defect}</td>'
            f'<td class="num">{E(x.get("version", "—"))}</td>'
            f'<td><span class="tag {cls}">{E(st)}</span></td>'
            f'<td class="num">{E(uk(x.get("issued")))}</td>'
            f'<td class="num">{E(uk(x.get("next_review")))}</td>'
            f'<td>{E(x.get("owner") or "—")}</td>'
            f'<td><span class="tag t-bad">pending</span></td>'
            f'<td class="num">{E(x.get("pages", "—"))}</td></tr>')

    for fm in sorted(s.controlled, key=lambda f: f["id"]):
        st = fm.get("status", "—")
        cls = {"approved": "t-ok", "draft": "t-warn", "in-review": "t-warn",
               "superseded": "t-mut"}.get(st, "t-mut")
        nc = sum(len(v or []) for v in (fm.get("clauses") or {}).values())
        rows.append(
            f'<tr data-row data-state="{E(st)}" data-loc="repo" data-map="mapped">'
            f'<td><code>{E(fm["id"])}</code></td>'
            f'<td><strong>{E(fm["title"])}</strong><div class="sub">'
            f'<code>{E(fm["_path"])}</code> &middot; in the repository, under version control</div></td>'
            f'<td class="num">{E(fm.get("version", "—"))}</td>'
            f'<td><span class="tag {cls}">{E(st)}</span></td>'
            f'<td class="num">{E(uk(fm.get("issued")))}</td>'
            f'<td class="num">{E(uk(fm.get("next_review")))}</td>'
            f'<td>{E(fm.get("owner", "—"))}</td>'
            f'<td><span class="tag t-ok">{nc} clauses</span></td>'
            f'<td class="num">—</td></tr>')

    specs = [("floc", "Where", "loc", [("", "Everywhere"), ("repo", "In the repository"),
                                       ("legacy", "Legacy PDF")]),
             ("fmap", "Clause map", "map", [("", "Any"), ("mapped", "Mapped"),
                                            ("pending", "Pending migration")]),
             ("fst", "State", "state", [("", "Any"), ("signed", "Signed"), ("issued", "Issued"),
                                        ("record", "Record"), ("draft", "Draft"),
                                        ("missing", "Missing")])]
    return f"""
<div class="card info"><h3>Two estates, one register</h3>
<p><strong>In the repository</strong> — {len(s.controlled)} files under version control, each
carrying front matter, each declaring the clauses it satisfies, each validated by
<code>build/validate.py</code> on every push. Every change is a commit with an author, a date
and a reason, and any past version can be recovered and re-rendered.</p>
<p><strong>Legacy PDFs</strong> — {len(legacy)} documents outside the repository. They are real,
most are signed, and they are what SESC currently runs on. They have no front matter, so they
declare no clauses and contribute nothing to coverage. Migrating them is workstream 7, starting
with SESC-POL-16 as the reference implementation.</p>
<p class="sub"><strong>Document owner is blank for every legacy document.</strong> The value
exists in each PDF control table; the Evidence Pack extraction did not capture it. Until a
document has a named owning role, nobody is accountable for reviewing it — finding F11.</p></div>
{filter_bar(specs, "", "")}
<table data-filter><thead><tr><th>Ref</th><th>Title</th><th>v</th><th>State</th>
<th>Issued</th><th>Next review</th><th>Owner</th><th>Clause map</th><th>pp</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table>
{FILTER_JS.replace("'rows'", "'documents'")}"""


def p_registers(s, aud):
    ip = load("registers/interested-parties.yaml")
    iss = load("registers/issues.yaml")

    stat_cls = {"held": "t-ok", "partial": "t-warn", "absent": "t-bad",
                "unverified": "t-warn", "unverified_absence": "t-warn", "unknown": "t-mut"}
    rows = []
    counts = defaultdict(int)
    for p in ip["parties"]:
        for r in p["requirements"]:
            st = r.get("status", "unknown")
            counts[st] += 1
            rows.append(
                f'<tr data-row data-status="{E(st)}" data-cat="{E(p["category"])}">'
                f'<td><code>{E(p["ref"])}</code><br>{E(p["party"])}</td>'
                f'<td>{E(flat(r["requirement"]))}<div class="sub">{E(flat(r.get("basis")))}</div></td>'
                f'<td><span class="tag t-mut">{E(r.get("obligation", "—"))}</span></td>'
                f'<td><span class="tag {stat_cls.get(st, "t-mut")}">{E(st)}</span></td>'
                f'<td>{E(flat(r.get("evidence")) or "—")}</td>'
                f'<td>{E(flat(r.get("gap")) or "—")}</td></tr>')

    irows = []
    for i in iss["issues"]:
        doms = i.get("domains", [])
        opp = "".join(f"<li>{E(flat(o))}</li>" for o in (i.get("opportunities") or []))
        irows.append(
            f'<tr data-row data-type="{E(i["type"])}" data-dom="{E("|".join(doms))}">'
            f'<td><code>{E(i["ref"])}</code></td>'
            f'<td>{E(i.get("category", "—"))}</td>'
            f'<td>{E(flat(i["issue"]))}'
            + (f'<div style="margin-top:6px"><strong>Opportunity</strong><ul>{opp}</ul></div>' if opp else "")
            + '</td><td>' + "".join(tag_mut(x) for x in doms) + '</td>'
              f'<td>{E(", ".join(str(x) for x in (i.get("risks") or [])) or "—")}</td>'
              f'<td>{E(i.get("owner", "—"))}</td></tr>')

    nreq = sum(len(p["requirements"]) for p in ip["parties"])
    return f"""
<h2>SESC-REG-05 &mdash; Interested Parties</h2>
<div class="card info"><p>{len(ip["parties"])} parties, {nreq} requirements. A party is listed
only where its requirement, unmet, would affect the Employer's ability to provide conforming
work, prevent harm to workers, or meet its compliance obligations. <strong>Parties that merely
exist are not listed.</strong> Every row names where the evidence sits, or says plainly that it
does not exist.</p>
<p class="sub">Version {E(ip["version"])}, {E(ip["status"])}. Owner {E(ip["owner"])},
approver {E(ip["approver"])}. Satisfies clause 4.2 of all three standards, and 6.1.3 of
14001 and 45001.</p></div>
<div class="stats">
<div class="stat ok"><div class="v">{counts['held']}</div><div class="k">requirements evidenced</div></div>
<div class="stat warn"><div class="v">{counts['partial']}</div><div class="k">partial</div></div>
<div class="stat bad"><div class="v">{counts['absent']}</div><div class="k">no evidence at all</div></div>
<div class="stat warn"><div class="v">{counts['unverified'] + counts['unverified_absence'] + counts['unknown']}</div>
<div class="k">unverified either way</div></div></div>
{filter_bar([("fs", "Status", "status", [("", "Any"), ("held", "Held"), ("partial", "Partial"),
                                         ("absent", "Absent"), ("unverified", "Unverified")]),
             ("fc", "Party", "cat", [("", "All"), ("internal", "Internal"), ("external", "External")])],
            "", "")}
<table data-filter><thead><tr><th>Party</th><th>Requirement</th><th>Type</th><th>Status</th>
<th>Evidence</th><th>Gap</th></tr></thead><tbody>{"".join(rows)}</tbody></table>

<h2>SESC-REG-06 &mdash; Issues</h2>
<div class="card info"><p>{len(iss["issues"])} issues. <strong>Risks and opportunities are held
in separate fields and are never merged</strong> &mdash; ISO 9001:2026 separates them, and
building it that way now costs nothing. One unified register, four lenses: small businesses
that keep separate quality, environmental, safety and information risk registers end up
reviewing none of them.</p>
<p><strong>Climate change is determined RELEVANT</strong>, expressly and substantively, with
nine issues behind the determination. For a building services contractor a "not relevant"
conclusion is not defensible.</p></div>
<div class="ctl"><input type="search" id="q2" class="hidden"></div>
<table><thead><tr><th>Ref</th><th>Category</th><th>Issue</th><th>Domains</th>
<th>Risks in REG-01</th><th>Owner</th></tr></thead><tbody>{"".join(irows)}</tbody></table>
{FILTER_JS.replace("'rows'", "'requirements'")}"""


def p_calendar(s, aud):
    obs = s.obligations()
    if aud == "contributor":
        obs = [o for o in obs if o["owner"] in ("Contracts Manager", "Accounts Manager")]
    rows = []
    for o in obs:
        if o["_overdue"]:
            due, cls = f"OVERDUE {uk(o['_due'])}", "overdue"
        elif o["_soon"]:
            due, cls = uk(o["_due"]), "soon"
        else:
            due, cls = uk(o["_due"]), ""
        last = (f'<span class="never">never</span>' if o["_never"] else E(uk(o["_last"])))
        rows.append(
            f'<tr data-row data-freq="{E(o["frequency"])}" data-owner="{E(o["owner"])}" '
            f'data-done="{"never" if o["_never"] else "done"}">'
            f'<td><code>{E(o["ref"])}</code></td>'
            f'<td>{E(flat(o["obligation"]))}<div class="sub">{E(flat(o["source"]))}</div></td>'
            f'<td><span class="tag t-mut">{E(o["frequency"])}</span></td>'
            f'<td>{E(o["owner"])}</td><td>{E(flat(o["record"]))}</td>'
            f'<td class="num">{last}</td><td class="num {cls}">{E(due)}</td></tr>')

    owners = sorted({o["owner"] for o in obs})
    ev = "".join(
        f'<tr><td><code>{E(e["ref"])}</code></td><td>{E(flat(e["trigger"]))}</td>'
        f'<td>{E(flat(e["action"]))}</td><td>{E(flat(e["source"]))}</td><td>{E(e["owner"])}</td></tr>'
        for e in s.obl["event_driven"])
    miss = "".join(
        f'<div class="card bad"><h3>{E(flat(m["obligation"]))}</h3>'
        f'<p class="sub">{E(m["standard_clause"])}</p><p>{E(flat(m["status"]))}</p></div>'
        for m in s.obl["not_yet_in_the_calendar"])

    never_n = sum(1 for o in obs if o["_never"])
    q = s.obl["first_operated_quarter_ends"]
    return f"""
<div class="card info"><h3>SESC-REG-02 Assurance Calendar</h3>
<p>Every recurring review, test, check and record the policy set commits the business to, with
its frequency, its owner, the record it produces and when it is next due. <strong>This is the
document that turns "at least annually" from an answer on a questionnaire into something that
actually happens.</strong></p>
<p>{E(flat(s.obl["operated_by"]))}</p></div>
<div class="card {'bad' if never_n else 'ok'}"><h3>Honest starting position</h3>
<p><strong>{never_n} of {len(obs)} scheduled obligations shown have never been carried out.</strong>
Almost every obligation here is being done for the first time. Three have a completed record —
the information asset assessment, the information security risk assessment and the business
continuity exercise, all dated 17 August 2026.</p>
<p><strong>The first quarter in which this calendar is fully operated ends
{E(uk(q))}.</strong> That is the date to quote when asked when the management system started
working, and it is deliberately a real date rather than a claim that it always has been.</p></div>
{filter_bar([("ff", "Frequency", "freq",
              [("", "All")] + [(x, x) for x in ("monthly", "quarterly", "six-monthly", "annual")]),
             ("fo", "Owner", "owner", [("", "Anyone")] + [(x, x) for x in owners]),
             ("fd", "History", "done", [("", "Any"), ("never", "Never done"), ("done", "Has a record")])],
            "", "")}
<table data-filter><thead><tr><th>Ref</th><th>Obligation</th><th>Frequency</th><th>Owner</th>
<th>Record produced</th><th>Last done</th><th>Next due</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table>

<h2>Event-driven &mdash; no date, but they must not be forgotten</h2>
<table><thead><tr><th>Ref</th><th>Trigger</th><th>What must happen</th><th>Source</th>
<th>Owner</th></tr></thead><tbody>{ev}</tbody></table>

<h2>Not in the calendar, and needed for certification</h2>
<p class="sub">SESC-REG-02 &sect;9 names three things added when certification is sought.
None of the three exists.</p>
{miss}
{FILTER_JS.replace("'rows'", "'obligations'")}"""


def p_actions(s, aud):
    acts = s.actions(aud)
    kindlab = {"blocker": "Blocker", "decision": "Decision", "finding": "Finding", "gap": "Gap"}
    sev = {"critical": "t-bad", "high": "t-bad", "medium": "t-warn", "low": "t-mut"}
    rows = []
    for a in acts:
        due = d(a.get("due"))
        cls = "overdue" if due and due < s.asof else ("soon" if due and (due - s.asof).days <= 30 else "")
        rows.append(
            f'<tr data-row data-kind="{E(a["kind"])}" data-sev="{E(a.get("severity", ""))}" '
            f'data-owner="{E(a["owner"])}">'
            f'<td><code>{E(a["ref"])}</code></td>'
            f'<td><span class="tag t-mut">{E(kindlab.get(a["kind"], a["kind"]))}</span></td>'
            f'<td><strong>{E(a["title"])}</strong><div class="sub" style="margin-top:4px">'
            f'{E(flat(a["detail"]))}</div></td>'
            f'<td><span class="tag {sev.get(a.get("severity"), "t-mut")}">'
            f'{E(a.get("severity", "—"))}</span></td>'
            f'<td>{E(a["owner"])}</td>'
            f'<td class="num {cls}">{E(uk(a.get("due")) if a.get("due") else "no date")}</td>'
            f'<td><span class="tag t-warn">{E(a.get("status", "open"))}</span></td></tr>')
    owners = sorted({a["owner"] for a in acts})
    intro = ('<div class="card bad"><h3>Known gaps, stated by SESC</h3>'
             '<p>This list is published to an assessor deliberately. Every item on it is '
             'something SESC has found in its own system and written down with an owner and a '
             'date. An assessor finds these anyway; a supplier that has already found them, '
             'dated them and owned them is in a different position from one that has not.</p>'
             '<p>Commercial decisions and the project\'s own management are not shown &mdash; '
             'they bear on nobody\'s conformity.</p></div>') if aud == "auditor" else (
        '<div class="card info"><h3>One list, four sources</h3>'
        '<p>Blockers, open decisions, findings and the things that are simply not yet true all '
        'resolve to the same object: somebody has to do something by a date. Held in one list so '
        'nobody has to read three tables to find out what is owed. Sorted hardest first.</p>'
        f'<p class="sub">Derived from {E(s.act["source_register"])}. If that register moves, '
        'this page is stale until the build is re-run.</p></div>')
    return f"""{intro}
{filter_bar([("fk", "Type", "kind", [("", "All")] + [(k, v) for k, v in kindlab.items()]),
             ("fv", "Severity", "sev", [("", "Any"), ("critical", "Critical"), ("high", "High"),
                                        ("medium", "Medium"), ("low", "Low")]),
             ("fo", "Owner", "owner", [("", "Anyone")] + [(x, x) for x in owners])], "", "")}
<table data-filter><thead><tr><th>Ref</th><th>Type</th><th>Item</th><th>Severity</th>
<th>Owner</th><th>Due</th><th>Status</th></tr></thead><tbody>{"".join(rows)}</tbody></table>
{FILTER_JS.replace("'rows'", "'items'")}"""


def p_records(s, aud):
    forms = [f for f in s.controlled if f["_folder"] == "forms"]
    forms.sort(key=lambda f: f["id"])
    cards = "".join(
        f'<div class="tile"><div class="n">{E(f["id"])}</div>'
        f'<div class="t"><a href="#{E(f["id"])}">{E(f["title"])}</a></div>'
        f'<div class="s">{E(flat(f.get("purpose"))[:130])}&hellip;</div></div>' for f in forms)

    out = [f"""
<div class="card warn"><h3>Read this before using a form</h3>
<p><strong>Nothing on this page is submitted anywhere.</strong> A generated site has no server.
Filling a form here builds a record in your browser and gives you a file to download and a page
to print. The Chief Operating Officer files it. That is the honest limit of stage one, and it is
the limit that record capture will force us past first.</p>
<p><strong>Completed records containing personal data must never be committed to the
repository.</strong> Accident detail naming individuals is Article 9 special category data. Git
history is immutable and replicated, which cannot satisfy a UK GDPR erasure request. Each form
below states where its completed record goes and how long it is kept.</p>
<p class="sub">All five forms are <strong>drafts</strong>. They take the next five free FRM
references and nothing is issued until the Managing Director approves them &mdash; decision D11.
The schema is fixed now on purpose: when these move to a server, the fields do not change and
no record has to be migrated.</p></div>
<div class="grid">{cards}</div>"""]

    for f in forms:
        cr = f.get("completed_record", {}) or {}
        cl = " &middot; ".join(f'{s.std[k]["label"]} {", ".join(str(x) for x in v)}'
                               for k, v in (f.get("clauses") or {}).items())
        fields_json = json.dumps(f.get("fields", []))
        fid = f["id"].replace("-", "_")
        rows = []
        for fl in f.get("fields", []):
            req = ' <span class="req">*</span>' if fl.get("required") else ""
            helptxt = f'<p class="help">{E(flat(fl.get("help")))}</p>' if fl.get("help") else ""
            t = fl["type"]
            name = f'{fid}__{fl["key"]}'
            if t == "textarea":
                ctl = f'<textarea id="{name}" name="{E(fl["key"])}"></textarea>'
            elif t in ("select", "multiselect"):
                opts = "".join(f'<option value="{E(o)}">{E(o)}</option>' for o in fl.get("options", []))
                multi = " multiple size=4" if t == "multiselect" else ""
                blank = "" if t == "multiselect" else '<option value=""></option>'
                ctl = f'<select id="{name}" name="{E(fl["key"])}"{multi}>{blank}{opts}</select>'
            elif t == "file":
                ctl = ('<p class="sub">Attach the photograph to the record when it is filed. '
                       'This page cannot upload anything.</p>')
            else:
                ctl = f'<input type="{E(t if t in ("date", "time") else "text")}" id="{name}" name="{E(fl["key"])}">'
            rows.append(f'<div class="f"><label class="l" for="{name}">{E(fl["label"])}{req}</label>'
                        f'{helptxt}{ctl}</div>')

        riddor = (f'<div class="card bad"><h3>RIDDOR</h3><p>{E(flat(f["riddor_note"]))}</p></div>'
                  if f.get("riddor_note") else "")
        guide = ("".join(f"<li>{E(flat(g))}</li>" for g in f.get("guidance", [])))
        guide = f'<div class="card ok"><h3>Before you start</h3><ul>{guide}</ul></div>' if guide else ""
        design = (f'<div class="card info"><h3>Why it is built this way</h3>'
                  f'<p>{E(flat(f["design_note"]))}</p></div>') if f.get("design_note") else ""

        out.append(f"""
<h2 id="{E(f["id"])}">{E(f["id"])} &mdash; {E(f["title"])}</h2>
<div class="card info"><p>{E(flat(f.get("purpose")))}</p>
<p class="sub"><strong>Satisfies</strong> {cl} &middot; version {E(f.get("version"))},
{E(f.get("status"))} &middot; owner {E(f.get("owner"))} &middot; approver {E(f.get("approver"))}</p></div>
<div class="card {'bad' if cr.get('contains_personal_data') else 'ok'}">
<h3>Where the completed record goes</h3>
<p><strong>{'Contains personal data' if cr.get('contains_personal_data') else 'No personal data'}
{' — Article 9 special category' if cr.get('special_category') else ''}.</strong>
{E(flat(cr.get('store')))}</p>
<p><strong>Retention:</strong> {E(flat(cr.get('retention')) or '—')}<br>
<strong>Feeds:</strong> {E(flat(cr.get('feeds_register')) or '—')}</p></div>
{guide}{riddor}{design}
<form class="rec" id="form_{fid}" onsubmit="return false">
{"".join(rows)}
<button class="btn" type="button" onclick="buildRecord('{fid}')">Build the record</button>
<button class="btn alt" type="button" onclick="window.print()">Print</button>
<div class="out hidden" id="out_{fid}"></div>
<a class="btn alt hidden" id="dl_{fid}" download="">Download as JSON</a>
</form>
<script>window.SCHEMA=window.SCHEMA||{{}};window.SCHEMA['{fid}']={{"id":{json.dumps(f["id"])},
"title":{json.dumps(f["title"])},"version":{json.dumps(str(f.get("version")))},
"fields":{fields_json}}};</script>""")

    out.append("""
<script>
function buildRecord(fid){
 var sch=window.SCHEMA[fid],form=document.getElementById('form_'+fid),
     out=document.getElementById('out_'+fid),dl=document.getElementById('dl_'+fid),
     rec={form:sch.id,form_title:sch.title,form_version:sch.version,
          built:new Date().toISOString(),values:{}},missing=[];
 sch.fields.forEach(function(f){
  if(f.type==='file')return;
  var el=document.getElementById(fid+'__'+f.key);if(!el)return;
  var v;
  if(f.type==='multiselect'){v=[].slice.call(el.selectedOptions).map(function(o){return o.value});
   if(f.required&&!v.length)missing.push(f.label);}
  else{v=el.value;if(f.required&&!v)missing.push(f.label);}
  rec.values[f.key]=v;
 });
 out.classList.remove('hidden');
 if(missing.length){out.textContent='Not finished. These are required:\\n\\n  '+
   missing.join('\\n  ');dl.classList.add('hidden');return;}
 var txt=JSON.stringify(rec,null,2);
 out.textContent='Record built. Download it and send it to the Chief Operating Officer, '+
  'or print this page.\\n\\n'+txt;
 dl.href='data:application/json;charset=utf-8,'+encodeURIComponent(txt);
 dl.download=sch.id+'-'+(rec.values.date||new Date().toISOString().slice(0,10))+'.json';
 dl.classList.remove('hidden');
}
</script>""")
    return "\n".join(out)


def p_audit(s, aud):
    # what an assessor asks, and where the answer is
    qa = [
        ("Show me your scope statement, and how you determined it.",
         "SESC-IMS-04 Context of the Organisation, Parts 1 to 7, with SESC-REG-05 and "
         "SESC-REG-06 behind it.",
         "DRAFT v0.1. Not approved and not issued. Until the approval block is completed it "
         "evidences nothing."),
        ("Did you determine whether climate change is a relevant issue?",
         "Yes, expressly. SESC-REG-06 CLI-00 to CLI-08 — nine issues, not a sentence.",
         "Strong. This is ahead of most suppliers of this size."),
        ("Show me your internal audit programme and the last audit report.",
         "Nothing.",
         "NO INTERNAL AUDIT HAS EVER BEEN CARRIED OUT, under any system, for any period. "
         "Clause 9.2 of all three standards. Gap G1."),
        ("Show me the minutes of your last management review.",
         "Nothing since 10 January 2023.",
         "Clause 9.3 of all three standards. Gap G2."),
        ("Show me your nonconformity log and three closed corrective actions.",
         "SESC-FRM-05 exists as a draft form. The log does not exist.",
         "Clause 10.2. An NCR is not closed until effectiveness is verified — the field "
         "assessors find empty. Gap G3."),
        ("Show me your environmental aspects and impacts register.",
         "Does not exist. The one held belongs to a landscaping firm.",
         "THE DEFINING ISO 14001 DOCUMENT AND THE HIGHEST-PRIORITY GAP IN THE SYSTEM. Gap G4."),
        ("How do workers who are not managers get consulted, and where are the records?",
         "Nothing beyond a paragraph in SESC-POL-05.",
         "ISO 45001 clause 5.4 requires a mechanism AND records of it operating. This is the "
         "clause 45001 assessors test hardest and the one small firms fail. Gap G6."),
        ("How long has the system been operating?",
         "The first fully operated quarter ends 30 September 2026.",
         "A real date, given rather than dressed up. A body typically wants around three months "
         "of operation, one internal audit round and one management review before Stage 2."),
        ("Who controls your documents, and can you show me what a policy said in March?",
         "Every controlled file is in a git repository. Every change is a commit with an author, "
         "a date and a reason, and any past version can be recovered and re-rendered.",
         "Strong — provided the twenty-one legacy PDFs are migrated in. Until then most of the "
         "estate has no version history at all."),
        ("Which edition of ISO 14001 are you building to?",
         "14001:2026. :2015 was withdrawn on 15 April 2026.",
         "THE EDITION IS NOT HELD AND HAS NEVER BEEN READ. The clause map carries :2015 numbering "
         "and is marked verified:false throughout. Blocker B4."),
        ("Show me a competence record for the person who did this work.",
         "SESC-FRM-03 exists as a draft form. Records are thin: 22 qualifications are recorded as "
         "expired against 20 current.",
         "Clause 7.2 of all three standards, and it is a records question, not a policy one."),
        ("How do you evaluate and re-evaluate your subcontractors?",
         "SESC-POL-12 Supplier Code of Conduct sets the standards. SESC-FRM-04 is the draft "
         "evaluation form. The approved supplier register does not exist.",
         "9001 8.4.1 wants criteria for selection AND re-evaluation; 45001 8.1.4.2 wants health "
         "and safety criteria in the procurement decision, not checked afterwards."),
    ]
    qhtml = "".join(
        f'<details class="cl" data-row><summary><span class="cid">Q{i+1:02d}</span>'
        f'<span style="flex:1">{E(q)}</span></summary><div class="body">'
        f'<p><strong>The answer today:</strong> {E(a)}</p>'
        f'<p class="card {"bad" if n.isupper() or "Gap" in n or "Blocker" in n else "info"}" '
        f'style="margin:8px 0">{E(n)}</p></div></details>'
        for i, (q, a, n) in enumerate(qa))

    # retain-clauses table: the record-hungry ones
    rr = []
    for k, st in s.std.items():
        for c in st["clauses"]:
            if c["di"] in ("retain", "both") or c["dual"]:
                state, cites = s.clause_state(k, c["id"])
                rr.append((st["label"], st["edition"], c, state, cites))
    rrows = "".join(
        f'<tr><td>{E(lab)}:{E(ed)}</td><td><code>{E(c["id"])}</code></td><td>{E(c["title"])}</td>'
        f'<td>{DUAL_TAG if c["dual"] else ""}'
        f'<span class="tag t-acc">{E(c["di"] if c["di"] else "retain")}</span></td>'
        f'<td><span class="tag {"t-ok" if state == "approved" else "t-warn" if state == "drafted" else "t-bad"}">'
        f'{E(state)}</span></td>'
        f'<td><span class="tag t-bad">no record held</span></td></tr>'
        for lab, ed, c, state, cites in rr)

    return f"""
<div class="card info"><h3>Audit mode</h3>
<p>What an assessor asks, in the order they ask it, and what SESC can put in front of them
today. Answers are written the way they should be given: the evidence first, then what is
wrong with it, before the assessor finds out for themselves.</p>
<p><strong>The rule this page is built on:</strong> a supplier who has found a gap, dated it and
named an owner is in a completely different position from one who has not found it. Every
"nothing" below has an owner and a date on the actions page.</p></div>
<h2>Twelve questions, and the honest answer to each</h2>
{qhtml}

<h2>The record-hungry clauses</h2>
<div class="card bad"><p><strong>{len(rr)} clauses across the three standards require a
<em>retained record</em>, not a document.</strong> These are the ones a certification body
cannot be talked out of, and SESC holds four records in total, all dated 17 August 2026.
The five ISO 45001 <em>dual maintain AND retain</em> clauses need both a document and a record,
and are the most commonly missed requirements in the whole set.</p>
<p>This table is the argument for why the next twelve months is about operating the system,
not writing more of it.</p></div>
<table><thead><tr><th>Standard</th><th>Clause</th><th>Title</th><th>Requires</th>
<th>Document</th><th>Record</th></tr></thead><tbody>{rrows}</tbody></table>"""


def p_about(s, aud):
    files = "".join(
        f'<tr><td><code>{E(p)}</code></td><td>{E(desc)}</td></tr>' for p, desc in [
            ("standards/*.yaml", "The clause map for all three standards, as data. 134 clauses."),
            ("system/*.md", "The Annex SL spine — clause 4 to clause 10, written once for all three."),
            ("registers/*.yaml", "Registers. YAML, never Word tables."),
            ("forms/*.yaml", "Record capture schemas."),
            ("portal/config.yaml", "Organisation facts and the audience model."),
            ("registers/documents.yaml", "SESC-REG-07 Document Register — every managed "
                                        "document, including the legacy PDFs outside the "
                                        "repository. Claims clause 7.5.3."),
            ("portal/obligations.yaml", "SESC-REG-02 Assurance Calendar, as data."),
            ("portal/actions.yaml", "Blockers, decisions, findings and gaps."),
            ("portal/records-index.yaml", "An index of records — reference, date and clauses. "
                                          "Metadata only, no content and no personal data. It "
                                          "is what makes the twelve-month staleness rule at "
                                          "CLAUDE.md 12.6 computable."),
            ("build/validate.py", "The CI gate. Front matter, clause references, dates, house "
                                  "style, and the personal-data guard."),
            ("build/build_portal.py", "This portal."),
        ])
    auds = "".join(
        f'<tr><td><strong>{E(a["name"])}</strong></td><td>{E(a["holder"])}</td>'
        f'<td>{E(flat(a["summary"]))}</td>'
        f'<td>{"internal items shown" if a["sees_internal"] else "internal items hidden"}</td></tr>'
        for a in s.cfg["audiences"])
    return f"""
<div class="card info"><h3>How this is built</h3>
<p>Every page in this portal is generated by <code>build/build_portal.py</code> from files in
the <code>sesc-ims</code> repository. <strong>Nothing here is written by hand and nothing here
can be edited by the person reading it.</strong> That is not a limitation that was accepted —
it is the reason the numbers are worth reading. A coverage figure that somebody can type over is
a self-assessment, and self-assessments drift green.</p>
<p>To change what this says, change the source and re-run the build. To see what the system
looked like on a past date, check that date out of git and re-run the build. Document control
and the audit trail are not features that had to be written; they are what a repository already
is.</p></div>

<h2>Where everything comes from</h2>
<table><thead><tr><th>File</th><th>What it holds</th></tr></thead><tbody>{files}</tbody></table>

<h2>The four builds</h2>
<div class="card warn"><p><strong>These are distribution audiences, not logins.</strong> A
generated site cannot authenticate anybody. What it can do is be generated four times, leaving
out of each build the content that audience must not see, so that the auditor folder is a folder
you can hand to an auditor. That is a real control. It is not access control, and this portal
never claims to be.</p>
<p>Nothing that bears on conformity is hidden from the auditor build. What is withheld is
commercial decision-making and the project's own management — and all personal data, from every
build, because it never enters the repository in the first place.</p></div>
<table><thead><tr><th>Build</th><th>Held by</th><th>Sees</th><th>Internal items</th></tr></thead>
<tbody>{auds}</tbody></table>

<h2>What it would take to make this an application</h2>
<div class="card info">
<p><strong>Stage 1, this.</strong> Generated, read-only, offline, no server, no cost, nothing to
breach. Read, search, retrieve, prepare for an audit.</p>
<p><strong>Stage 2, write-back.</strong> A small local writer in front of the same repository so
that an edit becomes a commit. Same data model, same pages. What forces this is
<em>record capture</em> — an operative logging a near miss at seven in the evening is the one
thing a folder genuinely cannot do, and near-miss records are exactly what ISO 45001 will want
twelve months of.</p>
<p><strong>Stage 3, hosted.</strong> The same templates behind a server with real logins and
real roles. Before that is worth paying for, three things need answering that only operating
the system can answer: which screens people actually use, where the personal-data boundary sits
in practice, and whether the record volume justifies a database. Building it first means
guessing at all three.</p>
<p class="sub">The cost of stage 3 is not the build. It is a DPIA against SESC-POL-14, a
controller-processor decision, an entry on the information asset register, backup and restore
evidence for SESC-POL-15, and access review evidence for SESC-POL-13. Four registers fed, and
not one certificate earned. That is the argument for doing it when the system is running, not
before.</p></div>

<h2>Rules this build obeys</h2>
<ul>
<li><strong>Never assert something no record supports.</strong> Clause coverage counts only what
a controlled file declares in its front matter. No clause is inferred from a document title.</li>
<li><strong>Personal data does not go in git</strong> — and so does not reach these pages.</li>
<li><strong>Companies are certified; certification bodies are accredited.</strong></li>
<li><strong>SESC holds no ISO certification of any kind</strong> and no page here says otherwise.</li>
<li><strong>A script exiting cleanly is not verification.</strong> This portal reports the state
of the system; it does not vouch for it.</li>
</ul>"""


BUILDERS = {"index": p_index, "clauses": p_clauses, "documents": p_documents,
            "registers": p_registers, "calendar": p_calendar, "actions": p_actions,
            "records": p_records, "audit": p_audit, "about": p_about}

STRAP = {
    "index": "the state of the management system, computed rather than asserted",
    "clauses": "every clause of all three standards, and what declares it",
    "documents": "every managed document, where it lives and whether it is mapped",
    "registers": "SESC-REG-05 interested parties and SESC-REG-06 issues",
    "calendar": "SESC-REG-02 — what is due, who owns it, and what record it produces",
    "actions": "blockers, decisions, findings and gaps, hardest first",
    "records": "raise a record — the forms, and where the completed record goes",
    "audit": "what an assessor asks, and the honest answer to each",
    "about": "how this is built, and what it deliberately cannot do",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--audience", choices=[a["key"] for a in load("portal/config.yaml")["audiences"]])
    ap.add_argument("--asof", help="ISO date; defaults to today")
    ap.add_argument("--out", default="site")
    args = ap.parse_args()

    asof = d(args.asof) if args.asof else datetime.date.today()
    s = System(asof)
    auds = [args.audience] if args.audience else [a["key"] for a in s.cfg["audiences"]]

    total = 0
    for aud in auds:
        outdir = os.path.join(ROOT, args.out if len(auds) == 1 and args.audience else
                              os.path.join(args.out, aud))
        os.makedirs(outdir, exist_ok=True)
        for slug, title, allowed in PAGES:
            if aud not in allowed:
                continue
            heading = TITLE_FOR.get(aud, {}).get(slug, title)
            body = BUILDERS[slug](s, aud)
            with open(os.path.join(outdir, f"{slug}.html"), "w", encoding="utf-8") as fh:
                fh.write(page(s, aud, slug, heading, STRAP[slug], body))
            total += 1
        print(f"  {aud:12s} -> {os.path.relpath(outdir, ROOT)}/  "
              f"{sum(1 for _, _, a in PAGES if aud in a)} pages")

    # a chooser at site/index.html, so the folder opens to something
    if not args.audience:
        tiles = "".join(
            f'<div class="tile"><div class="n">{E(a["key"].upper())}</div>'
            f'<div class="t"><a href="{a["key"]}/index.html">{E(a["name"])} build</a></div>'
            f'<div class="s">{E(a["holder"])}</div>'
            f'<div class="s" style="margin-top:6px">{E(flat(a["summary"]))}</div>'
            f'<div class="s" style="margin-top:6px">'
            f'<span class="tag {"t-warn" if a["sees_internal"] else "t-ok"}">'
            f'{"internal items shown" if a["sees_internal"] else "safe to hand over"}</span></div></div>'
            for a in s.cfg["audiences"])
        chooser = f"""<div class="card info"><h3>Four builds of one system</h3>
<p>The same repository, generated four times. Each build leaves out what that audience must not
see, so the <strong>Auditor</strong> folder is a folder you can hand to an auditor without
reading it through first.</p>
<p><strong>These are distribution audiences, not logins.</strong> A generated site cannot
authenticate anybody and this one does not pretend to. What it can do is be handed over safely.</p></div>
<div class="grid">{tiles}</div>
<div class="card warn"><h3>If you only open one thing</h3>
<p>Open <a href="controller/index.html">Controller &rarr; Overview</a>. It is the honest state
of the management system on one screen, computed from the repository rather than asserted by
anybody.</p></div>"""
        with open(os.path.join(ROOT, args.out, "index.html"), "w", encoding="utf-8") as fh:
            fh.write(page(s, "controller", "__chooser__", "SESC IMS portal",
                          "one repository, four builds", chooser))
        total += 1

    print(f"\nbuild_portal.py — {total} pages, {len(s.controlled)} controlled files, "
          f"{sum(len(v['clauses']) for v in s.std.values())} clauses, "
          f"{len(s.obl['obligations'])} scheduled obligations, "
          f"{len(s.act['actions'])} actions.  as at {asof}")
    print("Nothing in site/ is maintained by hand. Edit the source and re-run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
