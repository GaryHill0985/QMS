"""portal_theme.py — the house look, in one place.

Carried from the JOSCAR Evidence Pack so that the two read as one system, with a
brand-red identity rule added at the masthead. BRAND-SPEC.md remains authoritative
for the DOCUMENT cover system; this is screen furniture and does not touch it.
"""

CSS = """
:root{--ink:#111418;--mut:#5b6672;--line:#dde3ea;--bg:#fbfcfd;--acc:#0b4f8a;
--ok:#137a4a;--warn:#8a5a00;--bad:#a01b2b;--okbg:#eaf6f0;--warnbg:#fdf4e3;--badbg:#fdecee;
--brand:#ED1D24;--brandink:#231F20;--panel:#fff;}
*{box-sizing:border-box}
body{margin:0;padding:0 0 72px;background:var(--bg);color:var(--ink);
font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
.wrap{max-width:1180px;margin:0 auto;padding:0 28px}
.brandrule{height:4px;background:var(--brand)}
header.masthead{border-bottom:3px solid var(--acc);padding:24px 0 14px;margin-bottom:0;background:#fff}
h1{font-size:25px;margin:0 0 4px;letter-spacing:-.01em}
h2{font-size:18px;margin:30px 0 10px;padding-bottom:5px;border-bottom:1px solid var(--line)}
h3{font-size:15px;margin:20px 0 7px}
.sub{color:var(--mut);font-size:13.5px}
main{padding-top:22px}

nav.tabs{background:#fff;border-bottom:1px solid var(--line);position:sticky;top:0;z-index:20}
nav.tabs .wrap{display:flex;gap:2px;flex-wrap:wrap;align-items:center}
nav.tabs a{display:block;padding:10px 13px;font-size:13.5px;font-weight:600;color:var(--mut);
text-decoration:none;border-bottom:3px solid transparent}
nav.tabs a:hover{color:var(--acc);background:#f4f7fa}
nav.tabs a.on{color:var(--acc);border-bottom-color:var(--acc)}
nav.tabs .aud{margin-left:auto;font-size:12px;color:var(--mut);padding:10px 0}
nav.tabs .aud b{color:var(--ink)}

.tag{display:inline-block;padding:1px 8px;border-radius:10px;font-size:11.5px;
font-weight:600;letter-spacing:.02em;border:1px solid transparent;vertical-align:1px;white-space:nowrap}
.t-ok{background:var(--okbg);color:var(--ok);border-color:#bde3ce}
.t-warn{background:var(--warnbg);color:var(--warn);border-color:#f0d9a6}
.t-bad{background:var(--badbg);color:var(--bad);border-color:#f3c3c9}
.t-mut{background:#eef1f4;color:var(--mut);border-color:#dde3ea}
.t-acc{background:#eaf1f8;color:var(--acc);border-color:#c3d7ea}

table{border-collapse:collapse;width:100%;margin:10px 0 4px;font-size:13.5px;background:#fff}
th,td{border:1px solid var(--line);padding:7px 9px;text-align:left;vertical-align:top}
th{background:#eef3f8;font-weight:600;font-size:12.5px;letter-spacing:.02em;position:sticky;top:44px}
tr:nth-child(even) td{background:#fafbfc}
td.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
code{font:12.5px/1.4 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
background:#eef1f4;padding:1px 5px;border-radius:3px}
a{color:var(--acc)}

.card{background:#fff;border:1px solid var(--line);border-left-width:4px;border-radius:5px;
padding:12px 15px;margin:11px 0}
.card.bad{border-left-color:var(--bad)}
.card.warn{border-left-color:var(--warn)}
.card.ok{border-left-color:var(--ok)}
.card.info{border-left-color:var(--acc)}
.card h3{margin:0 0 5px;font-size:14.5px}
.card p{margin:5px 0}
ul{margin:7px 0 7px 20px;padding:0}li{margin:3px 0}

footer{margin-top:38px;padding-top:14px;border-top:1px solid var(--line);
color:var(--mut);font-size:12.5px}

.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:11px;margin:12px 0}
.tile{background:#fff;border:1px solid var(--line);border-radius:5px;padding:11px 13px}
.tile .n{font:600 12px ui-monospace,Menlo,Consolas,monospace;color:var(--mut)}
.tile .t{font-weight:600;margin:2px 0 4px}
.tile .s{font-size:12.5px;color:var(--mut)}

.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:11px;margin:14px 0}
.stat{background:#fff;border:1px solid var(--line);border-radius:5px;padding:13px 15px}
.stat .v{font-size:27px;font-weight:600;letter-spacing:-.02em;line-height:1.1;
font-variant-numeric:tabular-nums}
.stat .k{font-size:12.5px;color:var(--mut);margin-top:3px}
.stat.bad .v{color:var(--bad)}.stat.ok .v{color:var(--ok)}.stat.warn .v{color:var(--warn)}

.bar{height:10px;background:#eef1f4;border-radius:5px;overflow:hidden;display:flex;margin:6px 0 2px}
.bar i{display:block;height:100%}
.bar .b-ok{background:var(--ok)}.bar .b-doc{background:var(--acc)}.bar .b-warn{background:#d9a441}.bar .b-bad{background:#e5e9ee}
.legend{font-size:12px;color:var(--mut)}
.legend span{margin-right:12px;white-space:nowrap}
.legend b{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:4px}

.ctl{display:flex;gap:9px;flex-wrap:wrap;align-items:center;margin:14px 0 6px;
background:#fff;border:1px solid var(--line);border-radius:5px;padding:10px 12px}
.ctl input[type=search],.ctl select{font:14px inherit;padding:6px 9px;border:1px solid var(--line);
border-radius:4px;background:#fff;color:var(--ink)}
.ctl input[type=search]{min-width:260px;flex:1}
.ctl label{font-size:12.5px;color:var(--mut);font-weight:600}
.ctl .count{margin-left:auto;font-size:12.5px;color:var(--mut);font-variant-numeric:tabular-nums}
tr.hidden,.hidden{display:none !important}

details.cl{background:#fff;border:1px solid var(--line);border-radius:5px;margin:7px 0}
details.cl summary{padding:9px 12px;cursor:pointer;font-size:13.5px;display:flex;
gap:9px;align-items:baseline;flex-wrap:wrap}
details.cl summary::-webkit-details-marker{display:none}
details.cl summary:before{content:"\\25B8";color:var(--mut);font-size:11px;margin-right:2px}
details.cl[open] summary:before{content:"\\25BE"}
details.cl summary .cid{font:600 12.5px ui-monospace,Menlo,Consolas,monospace;color:var(--acc);
min-width:62px}
details.cl .body{padding:2px 14px 13px 34px;font-size:13.5px;border-top:1px solid var(--line)}
details.cl .body p{margin:8px 0}

form.rec{background:#fff;border:1px solid var(--line);border-radius:5px;padding:16px 18px;margin:12px 0}
form.rec .f{margin:0 0 14px}
form.rec label.l{display:block;font-weight:600;font-size:13.5px;margin-bottom:3px}
form.rec .help{font-size:12.5px;color:var(--mut);margin:0 0 5px}
form.rec input[type=text],form.rec input[type=date],form.rec input[type=time],
form.rec select,form.rec textarea{width:100%;font:14px inherit;padding:7px 9px;
border:1px solid var(--line);border-radius:4px;background:#fff;color:var(--ink)}
form.rec textarea{min-height:78px;resize:vertical}
form.rec .req{color:var(--bad);font-weight:700}
.btn{display:inline-block;font:600 14px inherit;padding:9px 16px;border-radius:4px;
border:1px solid var(--acc);background:var(--acc);color:#fff;cursor:pointer}
.btn.alt{background:#fff;color:var(--acc)}
.btn:disabled{opacity:.5;cursor:not-allowed}
.out{background:#f6f8fa;border:1px solid var(--line);border-radius:4px;padding:10px 12px;
font:12.5px/1.5 ui-monospace,Menlo,Consolas,monospace;white-space:pre-wrap;margin-top:12px}

.overdue{color:var(--bad);font-weight:600}
.never{color:var(--bad)}
.soon{color:var(--warn);font-weight:600}

@media print{
  body{background:#fff}
  nav.tabs,.ctl,.btn{display:none}
  .card,.tile,table,details.cl{break-inside:avoid}
  details.cl{border:none}
  details.cl .body{display:block !important}
  th{position:static}
}
@media (max-width:700px){
  .wrap{padding:0 14px}
  nav.tabs .aud{display:none}
  table{font-size:12.5px}
}
"""
