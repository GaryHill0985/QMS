#!/usr/bin/env python3
"""
validate.py — the CI gate for the SESC Integrated Management System.

Run from the repository root:   python3 build/validate.py
Exit 0 = clean. Exit 1 = at least one ERROR. Warnings never fail the build.

A validator added later validates nothing, so this exists before the documents do.

What it enforces:
  1. Front matter is present, parses, and carries every required field.
  2. The document ID matches the numbering series in CLAUDE.md 5, and no ID is used twice.
  3. Every clause cited exists in the matching standards/*.yaml file. A typo'd clause
     reference silently removes a clause from the audit pack, which is worse than omitting it.
  4. Dates are sane: next_review after issued, and no more than 12 months after it.
  5. status: approved requires an approver and an issued date not in the future.
  6. PERSONAL DATA GUARD — a tracked file flagged personal_data: true or
     classification: confidential FAILS the build. Git history is immutable and replicated,
     which is exactly wrong for a UK GDPR erasure request and for Article 9 data.
  7. House style — the words that must and must not appear in body text.
  8. Unverified standards editions are reported, loudly, every run.
"""

import sys, os, re, datetime, glob
try:
    import yaml
except ImportError:
    sys.exit("validate.py needs PyYAML:  pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED = ["id", "title", "version", "status", "owner", "approver",
            "issued", "next_review", "classification", "clauses"]
ID_RE = re.compile(r"^SESC-(POL|PRO|WI|REG|FRM|REC|TPL|CAP|CRP|IMS)-\d{2}$")
VERSION_RE = re.compile(r"^\d+\.\d+$")
STATUSES = {"draft", "in-review", "approved", "superseded"}
CLASSIFICATIONS = {"public", "internal", "confidential"}
STANDARD_KEYS = {"iso9001", "iso14001", "iso45001"}

errors, warnings, notes = [], [], []


def err(f, m):  errors.append(f"ERROR   {f}: {m}")
def warn(f, m): warnings.append(f"WARN    {f}: {m}")
def note(m):    notes.append(f"NOTE    {m}")


# ---------------------------------------------------------------- clause map
def load_standards():
    std = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "standards", "iso*.yaml"))):
        d = yaml.safe_load(open(path, encoding="utf-8"))
        key = d["standard"]
        std[key] = {
            "ids": {str(c["id"]) for c in d["clauses"]},
            "verified": d.get("verified", False),
            "edition": d.get("edition"),
            "note": d.get("verified_note", ""),
            "dual": {str(c["id"]) for c in d["clauses"] if c.get("dual_maintain_and_retain")},
            "critical": {str(c["id"]) for c in d["clauses"] if c.get("critical")},
        }
    return std


# ------------------------------------------------------------- front matter
def read_front_matter(path):
    """Markdown: --- fenced YAML. YAML register: the whole file is the front matter."""
    text = open(path, encoding="utf-8").read()
    if path.endswith((".yaml", ".yml")):
        return yaml.safe_load(text), text
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    return yaml.safe_load(text[3:end]), text[end + 4:]


def as_date(v):
    if isinstance(v, datetime.date):
        return v
    if isinstance(v, str):
        try:
            return datetime.date.fromisoformat(v)
        except ValueError:
            return None
    return None


# -------------------------------------------------------------------- checks
def check(path, std, seen_ids):
    rel = os.path.relpath(path, ROOT)
    try:
        fm, body = read_front_matter(path)
    except yaml.YAMLError as e:
        err(rel, f"front matter does not parse: {e}")
        return
    if not fm:
        err(rel, "no YAML front matter found")
        return

    # 1 / 2 — required fields, ID shape, uniqueness
    for f in REQUIRED:
        if f not in fm or fm[f] in (None, ""):
            err(rel, f"missing required front-matter field '{f}'")
    doc_id = str(fm.get("id", ""))
    if doc_id and not ID_RE.match(doc_id):
        err(rel, f"id '{doc_id}' does not match the numbering series in CLAUDE.md 5")
    if doc_id:
        if doc_id in seen_ids:
            err(rel, f"id '{doc_id}' is already used by {seen_ids[doc_id]}. NEVER REUSE A REFERENCE.")
        else:
            seen_ids[doc_id] = rel
    if "version" in fm and not VERSION_RE.match(str(fm["version"])):
        err(rel, f"version '{fm['version']}' must be n.n and quoted in YAML")
    if fm.get("status") not in STATUSES:
        err(rel, f"status '{fm.get('status')}' must be one of {sorted(STATUSES)}")
    if fm.get("classification") not in CLASSIFICATIONS:
        err(rel, f"classification '{fm.get('classification')}' must be one of {sorted(CLASSIFICATIONS)}")

    # 6 — PERSONAL DATA GUARD. This is the one that must never be softened.
    if fm.get("personal_data") is True:
        err(rel, "personal_data: true — THIS FILE MUST NOT BE IN GIT. "
                 "Git history is immutable and replicated; a UK GDPR erasure request cannot be "
                 "satisfied against it. Move to the encrypted database. See CLAUDE.md 8.")
    if fm.get("classification") == "confidential":
        err(rel, "classification: confidential — THIS FILE MUST NOT BE IN GIT. See CLAUDE.md 8.")

    # 3 — clause references
    clauses = fm.get("clauses") or {}
    if not isinstance(clauses, dict) or not clauses:
        err(rel, "clauses must be a non-empty map of standard -> list of clause ids")
    else:
        for key, ids in clauses.items():
            if key not in STANDARD_KEYS:
                err(rel, f"unknown standard key '{key}' — expected one of {sorted(STANDARD_KEYS)}")
                continue
            if key not in std:
                err(rel, f"no clause map loaded for '{key}'")
                continue
            for cid in (ids or []):
                cid = str(cid)
                if cid not in std[key]["ids"]:
                    err(rel, f"clause {key} {cid} does not exist in standards/. "
                             "A typo'd clause reference silently drops the clause from the audit pack.")
                if cid in std[key]["dual"]:
                    note(f"{rel} cites {key} {cid} — a DUAL maintain-AND-retain clause. "
                         "It needs BOTH a document and a retained record.")
                if cid in std[key]["critical"]:
                    note(f"{rel} cites {key} {cid} — flagged CRITICAL in the clause map. Read the note there.")
            if not std[key]["verified"]:
                warn(rel, f"cites {key}:{std[key]['edition']}, whose clause map is UNVERIFIED. "
                          "Do not quote these clause numbers to a customer or an auditor.")

    # 4 / 5 — dates and approval
    issued, review = as_date(fm.get("issued")), as_date(fm.get("next_review"))
    today = datetime.date.today()
    if fm.get("issued") is not None and issued is None:
        err(rel, "issued is not a valid ISO date")
    if fm.get("next_review") is not None and review is None:
        err(rel, "next_review is not a valid ISO date")
    if issued and review:
        if review <= issued:
            err(rel, "next_review must be after issued")
        elif (review - issued).days > 366:
            err(rel, f"next_review is {(review - issued).days} days after issue — max is 12 months")
    if review and review < today:
        warn(rel, f"REVIEW OVERDUE by {(today - review).days} days")
    if fm.get("status") == "approved":
        if not fm.get("approver"):
            err(rel, "status: approved with no approver")
        if issued and issued > today:
            err(rel, "status: approved with an issue date in the future")

    # 7 — house style, body text only
    if path.endswith(".md"):
        for bad, good in [(r"\bthe Company\b", '"the Employer"'),
                          (r"\bemployees and subcontractors\b", '"employees & subcontractors" with an ampersand'),
                          (r"ISO\s*9001[- ]accredited", '"certified" — companies are certified, bodies are accredited'),
                          (r"ISO\s*\d+\s+accredited", '"certified" — companies are certified, bodies are accredited')]:
            for m in re.finditer(bad, body):
                line = body[:m.start()].count("\n") + 1
                warn(rel, f"line ~{line}: house style — use {good}")
        if "## Part 8" not in body and "Records held, records not yet held" not in body \
           and fm.get("id", "").startswith(("SESC-IMS", "SESC-POL", "SESC-PRO")):
            warn(rel, "no 'Records held, records not yet held' section — the honesty convention "
                      "requires one in every management-system document. See CLAUDE.md 3.")


def main():
    std = load_standards()
    if not std:
        sys.exit("ERROR: no clause maps found in standards/. Nothing can be validated.")

    for key, s in std.items():
        if not s["verified"]:
            notes.append(f"NOTE    standards/{key}-{s['edition']}.yaml is marked verified: false.\n"
                         f"        {' '.join(s['note'].split())}")

    seen_ids = {}
    targets = []
    for d in ("system", "documents", "registers", "forms"):
        targets += sorted(glob.glob(os.path.join(ROOT, d, "**", "*.md"), recursive=True))
        targets += sorted(glob.glob(os.path.join(ROOT, d, "**", "*.yaml"), recursive=True))

    for path in targets:
        check(path, std, seen_ids)

    # records/ must never be committed
    for p in glob.glob(os.path.join(ROOT, "records", "**", "*"), recursive=True):
        if os.path.isfile(p) and not p.endswith(".gitkeep"):
            errors.append(f"ERROR   {os.path.relpath(p, ROOT)}: the records layer must not be "
                          "committed. It holds personal data. See CLAUDE.md 8.")

    print(f"validate.py — {len(targets)} controlled file(s), "
          f"{sum(len(s['ids']) for s in std.values())} clauses across {len(std)} standards\n")
    for line in notes + warnings + errors:
        print(line)
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s), {len(notes)} note(s)")
    if errors:
        print("\nBUILD FAILS. Fix every ERROR above before opening a pull request.")
        return 1
    print("\nBUILD PASSES.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
