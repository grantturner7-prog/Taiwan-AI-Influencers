#!/usr/bin/env python3
"""dashboard.py - writes a single static, offline HTML dashboard from the tracker database.

  python3 analytics/dashboard.py                 # real database  -> analytics/dashboard.html
  python3 analytics/dashboard.py --demo          # DEMO database  -> analytics/dashboard_demo.html (DEMO DATA banner)
  python3 analytics/dashboard.py --as-of 2027-01-04 --out /tmp/x.html

No network, no external scripts, fonts or images. A few lines of inline script give tooltips and a theme
toggle; every value is also in a table view, so the page works with scripts off.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import sys
from pathlib import Path

import metrics
import thresholds as T
import tracker

HERE = Path(__file__).resolve().parent
esc = html.escape

# Persona -> categorical slot (fixed by the entity, never by rank). portfolio.md 2A slot order.
PERSONA_SLOT = {"fangcun": 1, "buzhou": 2, "sehuan": 3, "jiehua": 4, "zhuancheng": 5, "suisui": 6, "licheng": 7, "guige": 8}
PLATFORM_LABEL = {"instagram": "Instagram", "threads": "Threads", "youtube_shorts": "YouTube Shorts", "facebook": "Facebook Page"}
STATUS_CLASS = {"SCALE_ELIGIBLE": "good", "KEEP": "good", "FIX": "warn", "RETIRE_REVIEW": "crit", "PAUSE": "serious",
                "RETIRE": "crit", "EXTEND": "neutral", "HOLD": "neutral", "IN_PROGRESS": "neutral", "NOT_STARTED": "neutral"}
ICONS = {
    "SCALE_ELIGIBLE": '<path d="M7 1.5 L13 12.5 H1 Z"/>',
    "KEEP": '<circle cx="7" cy="7" r="5.5"/>',
    "FIX": '<path d="M7 0.8 L13.2 7 L7 13.2 L0.8 7 Z"/>',
    "RETIRE_REVIEW": '<rect x="1.5" y="1.5" width="11" height="11"/>',
    "PAUSE": '<rect x="2.5" y="1.5" width="3.2" height="11"/><rect x="8.3" y="1.5" width="3.2" height="11"/>',
    "RETIRE": '<path d="M2 2 L12 12 M12 2 L2 12" fill="none" stroke="currentColor" stroke-width="2.6"/>',
    "EXTEND": '<circle cx="2.8" cy="7" r="1.8"/><circle cx="7" cy="7" r="1.8"/><circle cx="11.2" cy="7" r="1.8"/>',
    "HOLD": '<rect x="1.5" y="5.8" width="11" height="2.6"/>',
    "IN_PROGRESS": '<path d="M7 1.5 A5.5 5.5 0 0 1 7 12.5 Z"/><circle cx="7" cy="7" r="4.6" fill="none" stroke="currentColor" stroke-width="1.6"/>',
    "NOT_STARTED": '<circle cx="7" cy="7" r="4.6" fill="none" stroke="currentColor" stroke-width="2"/>',
}
LEVEL_STATUS = {"scale": ("SCALE_ELIGIBLE", "within Scale"), "keep": ("KEEP", "within Keep"), "fix": ("FIX", "Fix zone"),
                "retire": ("RETIRE_REVIEW", "over the retire line"), "unknown": ("NOT_STARTED", "not scored")}

CSS = r"""
:root{color-scheme:light;
 --page:#f9f9f7;--surface:#fcfcfb;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--grid:#e1e0d9;--axis:#c3c2b7;--ring:rgba(11,11,11,.10);
 --s1:#2a78d6;--s2:#eb6834;--s3:#1baf7a;--s4:#eda100;--s5:#e87ba4;--s6:#008300;--s7:#6250d6;--s8:#e34948;--sx:#898781;
 --good:#0ca30c;--warning:#fab219;--serious:#ec835a;--critical:#d03b3b;
 --bannerbg:#fff1c2;--bannerbd:#a06b00;--soft:#f1f0ec;--track:#e9e8e2}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;
 --page:#0d0d0d;--surface:#1a1a19;--ink:#f0efec;--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#383835;--ring:rgba(255,255,255,.10);
 --s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;--s5:#d55181;--s6:#008300;--s7:#9085e9;--s8:#e66767;
 --bannerbg:#3b2f05;--bannerbd:#e0a52a;--soft:#232321;--track:#2c2c2a}}
:root[data-theme="dark"]{color-scheme:dark;
 --page:#0d0d0d;--surface:#1a1a19;--ink:#f0efec;--ink2:#c3c2b7;--grid:#2c2c2a;--axis:#383835;--ring:rgba(255,255,255,.10);
 --s1:#3987e5;--s2:#d95926;--s3:#199e70;--s4:#c98500;--s5:#d55181;--s6:#008300;--s7:#9085e9;--s8:#e66767;
 --bannerbg:#3b2f05;--bannerbd:#e0a52a;--soft:#232321;--track:#2c2c2a}
*{box-sizing:border-box}
html{background:var(--page)}
body{margin:0;background:var(--page);color:var(--ink);font:15px/1.5 system-ui,-apple-system,"Segoe UI","Noto Sans TC","PingFang TC","Microsoft JhengHei","WenQuanYi Zen Hei",sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:0 16px 48px}
a{color:var(--ink)}
.skip{position:absolute;left:-999px;top:8px;background:var(--surface);color:var(--ink);padding:8px 12px;border:2px solid var(--ink);z-index:10}
.skip:focus{left:8px}
:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
header.top{padding:20px 0 8px;display:flex;flex-wrap:wrap;gap:8px 24px;align-items:flex-end;justify-content:space-between}
h1{font-size:1.5rem;line-height:1.2;margin:0 0 4px;font-weight:650}
h2{font-size:1.2rem;margin:0 0 4px;font-weight:650}
h3{font-size:1.05rem;margin:0;font-weight:650}
.sub{color:var(--ink2);margin:0;font-size:.9rem}
button.theme{font:inherit;font-size:.85rem;color:var(--ink);background:var(--surface);border:1px solid var(--axis);border-radius:6px;padding:6px 10px;cursor:pointer;min-height:32px}
.banner{position:sticky;top:0;z-index:5;background:var(--bannerbg);color:var(--ink);border:2px solid var(--bannerbd);border-radius:8px;padding:10px 14px;margin:8px 0 12px;display:flex;gap:12px;align-items:baseline;flex-wrap:wrap}
.banner strong{font-size:1.15rem;letter-spacing:.04em}
.banner.empty{position:static;background:var(--soft);border-color:var(--axis)}
nav.sections{display:flex;flex-wrap:wrap;gap:4px 14px;margin:6px 0 18px;font-size:.88rem}
section.block{background:var(--surface);border:1px solid var(--ring);border-radius:10px;padding:18px 18px 16px;margin:0 0 18px}
section.block>header{margin-bottom:12px}
section.block>header p{margin:2px 0 0;color:var(--ink2);font-size:.9rem;max-width:80ch}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px;margin:0 0 18px}
.tile{background:var(--surface);border:1px solid var(--ring);border-radius:10px;padding:12px 14px}
.tile .l{color:var(--ink2);font-size:.85rem}
.tile .v{font-size:1.7rem;font-weight:650;line-height:1.2;margin-top:2px}
.tile .d{color:var(--ink2);font-size:.82rem;margin-top:2px}
.meter{height:8px;border-radius:4px;background:var(--track);margin:8px 0 2px;position:relative;overflow:hidden}
.meter>i{display:block;height:100%;background:var(--sx);border-radius:4px 0 0 4px}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(330px,1fr));gap:14px}
.pcard{border:1px solid var(--ring);border-top:4px solid var(--c,var(--sx));border-radius:10px;padding:14px;background:var(--surface)}
.pcard header{display:flex;flex-wrap:wrap;gap:6px 12px;justify-content:space-between;align-items:flex-start}
.pcard .meta{color:var(--ink2);font-size:.82rem;margin:2px 0 0}
.pcard p.clock{color:var(--ink2);font-size:.84rem;margin:8px 0}
table{border-collapse:collapse;width:100%;font-size:.88rem}
caption{text-align:left;color:var(--ink2);font-size:.82rem;padding:0 0 6px}
th,td{padding:6px 8px;border-bottom:1px solid var(--grid);vertical-align:top;text-align:left}
th{font-weight:600;color:var(--ink2);font-size:.8rem}
tbody th{font-size:.9rem;color:var(--ink);font-weight:600}
.acct{border-top:1px solid var(--grid);padding:8px 0}
.ahead{display:flex;flex-wrap:wrap;gap:4px 10px;align-items:center}
.ameta{font-size:.85rem;margin-top:2px;font-variant-numeric:tabular-nums}
.acct p{margin:2px 0 0}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}
.tscroll{overflow-x:auto}
.chip{display:inline-flex;align-items:center;gap:6px;font-size:.82rem;font-weight:600;color:var(--ink);border:1px solid var(--axis);border-left:4px solid var(--st,var(--sx));border-radius:6px;padding:2px 8px 2px 6px;white-space:nowrap;background:var(--surface)}
.chip svg{width:13px;height:13px;fill:var(--st,var(--sx));color:var(--st,var(--sx));flex:none}
.chip.good{--st:var(--good)}.chip.warn{--st:var(--warning)}.chip.serious{--st:var(--serious)}.chip.crit{--st:var(--critical)}.chip.neutral{--st:var(--ink2)}
.chip.big{font-size:.95rem;padding:4px 10px 4px 8px}
.sw{display:inline-block;width:10px;height:10px;border-radius:3px;background:var(--c,var(--sx));margin-right:6px;vertical-align:baseline;flex:none}
small,.small{font-size:.8rem;color:var(--ink2)}
details{margin:8px 0 0}
summary{cursor:pointer;color:var(--ink2);font-size:.85rem;padding:4px 0}
details ol,details ul{margin:6px 0 0;padding-left:20px;font-size:.85rem;color:var(--ink2)}
details li{margin:2px 0}
.note{font-size:.84rem;color:var(--ink2);margin:6px 0 0}
.flag{font-size:.84rem;margin:6px 0 0;padding:6px 10px;border-left:4px solid var(--warning);background:var(--soft);border-radius:0 6px 6px 0}
.flag.crit{border-left-color:var(--critical)}
/* horizontal bar rows */
.rows{display:flex;flex-direction:column;gap:2px}
.row{display:grid;grid-template-columns:minmax(150px,230px) 1fr minmax(110px,150px);gap:4px 14px;align-items:center;padding:8px 0;border-bottom:1px solid var(--grid)}
.row.head{border-bottom:0;padding:0 0 2px}
.row .lab strong{font-weight:600}
.row .lab small{display:block}
.plot{position:relative;min-height:26px;border-left:1px solid var(--axis)}
.plot .ref,.mplot .ref{position:absolute;top:0;bottom:0;width:0;border-left:1px solid var(--axis)}
.plot .bar{position:absolute;left:0;top:2px;height:10px;background:var(--c,var(--sx));border-radius:0 4px 4px 0;min-width:2px}
.plot .bar.out{background:transparent;border:2px solid var(--c,var(--sx));border-left:0;height:10px}
.plot .dots{position:absolute;left:0;right:0;top:18px}
.dot{position:absolute;width:8px;height:8px;margin-left:-4px;border-radius:50%;background:var(--c,var(--sx));box-shadow:0 0 0 2px var(--surface)}
.dot.hollow{background:var(--surface);box-shadow:none;border:2px solid var(--c,var(--sx))}
.dot::after,.bar::after{content:"";position:absolute;inset:-8px}
.axis{position:relative;height:18px;font-size:.75rem;color:var(--ink2)}
.axis span{position:absolute;transform:translateX(-50%);white-space:nowrap}
.axis span:first-child{transform:none}
.val{font-variant-numeric:tabular-nums}
.val strong{font-size:1.05rem}
.legendline{display:flex;flex-wrap:wrap;gap:4px 16px;font-size:.82rem;color:var(--ink2);margin:8px 0 0}
.key{display:inline-flex;align-items:center;gap:6px}
.key i{width:14px;height:8px;border-radius:2px;display:inline-block}
/* mini charts */
.minis{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}
.mini{border:1px solid var(--ring);border-radius:10px;padding:10px 12px}
.mini h3{font-size:.95rem}
.mini .pair{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px}
.mini figure{margin:0}
.mini figcaption{font-size:.78rem;color:var(--ink2)}
.mini .big{font-size:1.25rem;font-weight:650;line-height:1.2}
.spark{position:relative;height:56px;margin-top:4px;border-bottom:1px solid var(--axis)}
.spark svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.spark .ln{fill:none;stroke:var(--c,var(--sx));stroke-width:2;stroke-linejoin:round;stroke-linecap:round;vector-effect:non-scaling-stroke}
.spark .ar{fill:var(--c,var(--sx));opacity:.10;stroke:none}
.spark .end{position:absolute;width:8px;height:8px;margin:-4px 0 0 -4px;border-radius:50%;background:var(--c,var(--sx));box-shadow:0 0 0 2px var(--surface)}
.spark .hit{position:absolute;top:0;bottom:0;display:block}
.spark .hit:hover,.spark .hit:focus-visible{background:var(--ring)}
.xl{display:flex;justify-content:space-between;font-size:.72rem;color:var(--ink2)}
/* money */
.cost{background:var(--sx)}.rev{background:var(--s7)}
.mbar{position:absolute;left:0;height:10px;border-radius:0 4px 4px 0;min-width:2px}
.mrow{display:grid;grid-template-columns:78px 1fr;gap:8px 12px;align-items:center;padding:8px 0;border-bottom:1px solid var(--grid)}
.mplot{position:relative;height:34px;border-left:1px solid var(--axis)}
.mplot .l{position:absolute;font-size:.75rem;color:var(--ink2);white-space:nowrap;font-variant-numeric:tabular-nums}
.pre{white-space:pre-wrap}
#tip{position:fixed;z-index:20;pointer-events:none;background:var(--ink);color:var(--surface);font-size:.8rem;line-height:1.35;padding:6px 9px;border-radius:6px;max-width:300px;white-space:pre-line}
footer{color:var(--ink2);font-size:.82rem;margin-top:24px}
@media (max-width:640px){
 .row{grid-template-columns:1fr;gap:2px}
 .row.head{display:none}
 .mini .pair{grid-template-columns:1fr}
 section.block{padding:14px 12px}
 .banner{position:static}
}
@media (forced-colors:active){
 .bar,.dot,.mbar,.meter>i,.sw{forced-color-adjust:none}
 .chip{border:1px solid CanvasText}
}
@media print{.banner{position:static}button.theme,nav.sections,#tip{display:none}section.block{break-inside:avoid}}
"""

JS = r"""
(function(){
 var root=document.documentElement,btn=document.getElementById('theme'),modes=['auto','light','dark'],i=0;
 function apply(m){if(m==='auto'){root.removeAttribute('data-theme');}else{root.setAttribute('data-theme',m);}
  if(btn){btn.textContent='Theme: '+m;} }
 try{var s=localStorage.getItem('analytics-theme');if(s&&modes.indexOf(s)>-1){i=modes.indexOf(s);}}catch(e){}
 if(location.hash==='#dark'){i=2}else if(location.hash==='#light'){i=1}
 apply(modes[i]);
 if(btn){btn.addEventListener('click',function(){i=(i+1)%3;apply(modes[i]);try{localStorage.setItem('analytics-theme',modes[i]);}catch(e){}});}
 var tip=document.getElementById('tip');
 function place(x,y){var w=tip.offsetWidth,h=tip.offsetHeight,nx=x+14,ny=y+14;
  if(nx+w>window.innerWidth-8){nx=Math.max(8,x-w-14);} if(ny+h>window.innerHeight-8){ny=Math.max(8,y-h-14);}
  tip.style.left=nx+'px';tip.style.top=ny+'px';}
 function show(el,x,y){tip.textContent=el.getAttribute('data-tip');tip.hidden=false;place(x,y);}
 document.addEventListener('pointerover',function(e){var t=e.target.closest&&e.target.closest('[data-tip]');if(t){show(t,e.clientX,e.clientY);}});
 document.addEventListener('pointermove',function(e){if(!tip.hidden){place(e.clientX,e.clientY);}});
 document.addEventListener('pointerout',function(e){var t=e.target.closest&&e.target.closest('[data-tip]');if(t){tip.hidden=true;}});
 document.addEventListener('focusin',function(e){var t=e.target.closest&&e.target.closest('[data-tip]');if(t){var r=t.getBoundingClientRect();show(t,r.left+r.width/2,r.top);}});
 document.addEventListener('focusout',function(){tip.hidden=true;});
 document.addEventListener('keydown',function(e){if(e.key==='Escape'){tip.hidden=true;}});
})();
"""


# ---------------------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------------------
def pct(x, d=2):
    return "n/a" if x is None else f"{x * 100:.{d}f}%"


def nt(x):
    return f"NT${x:,.0f}"


def num(x, d=0):
    return "-" if x is None else f"{x:,.{d}f}"


def tipattr(text):
    return 'data-tip="' + esc(text, quote=True).replace("\n", "&#10;") + '"'


def zh(text):
    return f'<span lang="zh-Hant-TW">{esc(text)}</span>'


def pclass(slug):
    return "p-" + re.sub(r"[^a-z0-9_-]", "", str(slug).lower())


def persona_css(slugs):
    out = []
    for s in slugs:
        slot = PERSONA_SLOT.get(s)
        cls = pclass(s)
        out.append(f".{cls}{{--c:var(--s{slot})}}" if slot else f".{cls}{{--c:var(--sx)}}")
    return "\n".join(out)


def chip(status, label=None, big=False):
    cls = STATUS_CLASS[status]
    text = label or T.STATUS_LABELS[status]
    return (f'<span class="chip {cls}{" big" if big else ""}"><svg viewBox="0 0 14 14" aria-hidden="true" focusable="false">{ICONS[status]}</svg>'
            f'{esc(text)}</span>')


def level_chip(level):
    st, text = LEVEL_STATUS[level]
    return chip(st, text)


def plat(p):
    return PLATFORM_LABEL.get(p, p)


def axis(ticks, vmax, fmt):
    spans = "".join(f'<span style="left:{min(100, t / vmax * 100):.2f}%">{esc(fmt(t))}</span>' for t in ticks)
    return f'<div class="axis" aria-hidden="true">{spans}</div>'


def refs(values, vmax):
    return "".join(f'<span class="ref" style="left:{v / vmax * 100:.2f}%"></span>' for v in values)


def dots_html(values, vmax, hollow, cls_tip):
    """Beeswarm-ish strip: values (with tip text) placed on up to 4 rows so equal values do not hide each other."""
    placed, last = [], [-99.0] * 4
    for v, tip in sorted(values, key=lambda x: x[0]):
        x = min(100.0, v / vmax * 100)
        r = next((i for i in range(4) if x - last[i] >= 2.0), 3)
        last[r] = x
        placed.append((x, r, tip))
    h = (max((r for _, r, _ in placed), default=0) + 1) * 11
    inner = "".join(f'<span class="dot{" hollow" if hollow else ""}" style="left:{x:.2f}%;top:{r * 11}px" aria-hidden="true" {tipattr(t)}></span>'
                    for x, r, t in placed)
    return f'<div class="dots" style="height:{h}px">{inner}</div>', h + 20


# ---------------------------------------------------------------------------------------
# sections
# ---------------------------------------------------------------------------------------
def section_kpis(snap):
    fin = snap["finance"]
    cur = fin["current"]
    spend = cur["tool"]
    frac = min(1.0, spend / fin["cap_base"]) if fin["cap_base"] else 0
    as_s = snap["as_of"].isoformat()
    open_gates = sum(1 for e in snap["standing"] if e["event_date"] <= as_s and (e["cleared_on"] is None or e["cleared_on"] > as_s))
    organic = snap["n_posts"]
    return f"""
<div class="kpis" role="list">
 <div class="tile" role="listitem"><div class="l">Personas with accounts</div><div class="v">{len(snap['personas'])}</div>
  <div class="d">{sum(len(p['accounts']) for p in snap['personas'])} accounts (persona x platform)</div></div>
 <div class="tile" role="listitem"><div class="l">Published posts</div><div class="v">{organic}</div>
  <div class="d">all personas, sponsored included</div></div>
 <div class="tile" role="listitem"><div class="l">Tool spend, {esc(fin['current_month'])}</div><div class="v">{nt(spend)}</div>
  <div class="meter" role="img" aria-label="{nt(spend)} of the {nt(fin['cap_base'])} base cap"><i style="width:{frac * 100:.1f}%"></i></div>
  <div class="d">of {nt(fin['cap_base'])} base cap ({nt(fin['cap_headroom'])} only if a tool clearly earns it)</div></div>
 <div class="tile" role="listitem"><div class="l">Open account-standing gates</div><div class="v">{open_gates}</div>
  <div class="d">portfolio.md 6.2; any open gate pauses that account</div></div>
</div>"""


def account_block(a):
    d = a["decision"]
    s = a["summary"]
    reason = d["reasons"][0] if d["reasons"] else ""
    er = s["er"]
    scored = d["status"] in ("SCALE_ELIGIBLE", "KEEP", "FIX", "RETIRE_REVIEW")
    if er is None:
        meta = f'{s["n_scored"]} posts counted · no ER yet'
    elif scored:
        meta = f'{s["n_scored"]} posts counted · median ER {pct(er)}'
    else:
        meta = f'{s["n_scored"]} posts so far · ER {pct(er)} (not scored)'
    prov = " <small>provisional reading</small>" if d["provisional"] else ""
    return (f'<div class="acct"><div class="ahead"><strong>{esc(plat(a["platform"]))}</strong><small>{esc(a["role"] or "")}</small>{chip(d["status"])}{prov}</div>'
            f'<div class="ameta">{esc(meta)}</div><p class="small">{esc(reason)}</p></div>')


def decision_path(a):
    d = a["decision"]
    items = "".join(f'<li><strong>{esc(s["question"])}</strong> {esc(s["answer"])}' + (f'. {esc(s["detail"])}' if s["detail"] else "") + "</li>" for s in d["steps"])
    extra = ""
    if d["scale_checks"]:
        li = "".join(f'<li>{"yes" if v else ("no" if v is False else "cannot tell")}: {esc(k)}</li>' for k, v in d["scale_checks"].items())
        extra += f"<li>Scale conditions:<ul>{li}</ul></li>"
    cav = "".join(f"<li>{esc(c)}</li>" for c in d["caveats"])
    if a.get("sample_note"):
        cav += f"<li>{esc(a['sample_note'])}</li>"
    out = f'<details><summary>{esc(plat(a["platform"]))}: decision path (6.3)</summary><ol>{items}{extra}</ol>'
    if cav:
        out += f'<p class="note">Caveats</p><ul>{cav}</ul>'
    out += "</details>"
    return out


def section_status(snap):
    cards = []
    for p in snap["personas"]:
        first = p["first_post"]
        if p["first_post_kind"] == "actual":
            clock = (f"Week {p['week_now']} since the first post on {first}. Week-6 review date {p['review_date']}; "
                     f"scoring window weeks {T.WINDOW_FIRST_WEEK} to {T.WINDOW_LAST_WEEK}.")
        elif first:
            clock = f"No post published yet. Planned first post {first} (an assumption; moves with the launch gates)."
        else:
            clock = "No first-post date yet."
        head = p["headline"]
        best = f'Best active account: {esc(plat(p["headline_account"]))}.' if p["headline_account"] and head != "NOT_STARTED" else ""
        paused = f' Paused or retired: {esc(", ".join(plat(x) for x in p["paused"]))}.' if p["paused"] else ""
        rows = "".join(account_block(a) for a in p["accounts"])
        paths = "".join(decision_path(a) for a in p["accounts"])
        watch = "".join(f'<p class="flag">{esc(w)}</p>' for a in p["accounts"] for w in a["decision"]["watch"])
        alerts = "".join(f'<p class="flag crit">{esc(w)}</p>' for w in p["alerts"])
        cards.append(f"""
<article class="pcard {pclass(p['slug'])}" aria-labelledby="pc-{p['slug']}">
 <header><div><h3 id="pc-{p['slug']}">{zh(p['name_zh'])} <small>{esc(p['slug'])}</small></h3>
  <p class="meta">Wave {p['wave']} · {esc(p['status'])}</p></div>
  <div>{chip(head, big=True)}</div></header>
 <p class="clock">{esc(clock)} {best}{paused}</p>
 <div class="accts" role="group" aria-label="Decision per account (the tree runs once per persona and platform)">{rows}</div>
 {watch}{alerts}{paths}
</article>""")
    return f"""
<section class="block" id="status" aria-labelledby="h-status">
 <header><h2 id="h-status">Scale, keep or retire: status per persona</h2>
 <p>Portfolio.md 6.3 decision tree, applied to weeks 3 to 6 of each persona, with the minimum sample of {T.MIN_ORGANIC_POSTS} organic posts per platform.
 Statuses are indications for the operator to confirm. Nothing here retires a persona or changes a post by itself.</p></header>
 <div class="grid3">{''.join(cards)}</div>
</section>"""


def er_rows(snap):
    """Collect (persona, account) pairs for the ER and saves charts."""
    return [(p, a) for p in snap["personas"] for a in p["accounts"]]


def section_er(snap):
    pairs = er_rows(snap)
    allv = [p["er"] for _, a in pairs for p in a["posts"] if p["er"] is not None]
    mx = max(allv + [x for _, a in pairs for x in [a["summary"]["er"]] if x is not None] + [0.025])
    vmax = 0.025 if mx <= 0.026 else (0.03 if mx <= 0.031 else (0.04 if mx <= 0.041 else (0.05 if mx <= 0.051 else int(mx * 105) / 100 + 0.01)))
    ticks = [0, T.ER_FIX, T.ER_KEEP, T.ER_SCALE] + ([vmax] if vmax > 0.026 else [])
    rows, table = [], []
    for p, a in pairs:
        s, d = a["summary"], a["decision"]
        scored = d["status"] in ("SCALE_ELIGIBLE", "KEEP", "FIX", "RETIRE_REVIEW")
        values = []
        for po in a["posts"]:
            if po["er"] is not None:
                rec = po["er_rec"]
                values.append((po["er"], f"{po['post_id']}\n{po['published_date']} · {po['format'] or 'format n/a'}\nER {pct(po['er'])} = {rec['numerator']} / {rec['denominator']} {rec['denom_kind']}\n({'+'.join(rec['terms'])})"))
        dots, h = dots_html(values, vmax, hollow=not scored, cls_tip=None) if values else ('<div class="dots"></div>', 22)
        bar = ""
        if scored and s["er"] is not None:
            tip = f"{p['name_zh']} {plat(a['platform'])}\nmedian ER {pct(s['er'])} over {s['n_scored']} organic posts\nrange {pct(s['er_min'])} to {pct(s['er_max'])}"
            bar = (f'<span class="bar" style="width:{min(100, s["er"] / vmax * 100):.2f}%" tabindex="0" role="img" '
                   f'aria-label="{esc(tip, quote=True)}" {tipattr(tip)}></span>')
        den = "/".join(s["denominators"]) or "n/a"
        step = ""
        if s["median_reach_or_views"]:
            step = f"median {s['median_interactions']:.0f} interactions on {s['median_reach_or_views']:,.0f} {den}; one interaction moves ER by {pct(1 / s['median_reach_or_views'])}"
        if scored:
            valtxt = f'<strong>{pct(s["er"])}</strong><br><small>range {pct(s["er_min"])} to {pct(s["er_max"])}<br>{esc(step)}</small>'
        elif s["n_scored"]:
            valtxt = f'<strong>not scored</strong><br><small>{s["n_scored"]} posts so far; hollow dots</small>'
        else:
            valtxt = "<strong>no data</strong>"
        rows.append(f"""
<div class="row {pclass(p['slug'])}">
 <div class="lab"><span class="sw"></span><strong>{zh(p['name_zh'])}</strong> {esc(plat(a['platform']))}
  <small>{chip(d['status'])} {('n=' + str(s['n_scored']) + ' · ER on ' + esc(den)) if s['n_scored'] else 'no posts counted yet'}</small></div>
 <div class="plot" style="min-height:{h}px">{refs([T.ER_FIX, T.ER_KEEP, T.ER_SCALE], vmax)}{bar}{dots}</div>
 <div class="val">{valtxt}</div>
</div>""")
        table.append(f"<tr><td>{zh(p['name_zh'])}</td><td>{esc(plat(a['platform']))}</td><td>{esc(T.STATUS_LABELS[d['status']])}</td>"
                     f"<td class=\"num\">{s['n_scored']}</td><td class=\"num\">{pct(s['er'])}</td><td class=\"num\">{pct(s['er_min'])}</td>"
                     f"<td class=\"num\">{pct(s['er_max'])}</td><td>{esc(den)}</td><td>{esc('+'.join(s['terms']) or 'n/a')}</td><td class=\"num\">{num(s['median_interactions'], 1)}</td><td class=\"num\">{num(s['median_reach_or_views'])}</td><td>{esc(a.get('window_label', ''))}</td></tr>")
    head = (f'<div class="row head" aria-hidden="true"><div></div>{axis(ticks, vmax, lambda t: pct(t, 1))}<div></div></div>')
    return f"""
<section class="block" id="er" aria-labelledby="h-er">
 <header><h2 id="h-er">Engagement rate per account</h2>
 <p>ER = (saves + shares + comments) / reach for each post, using only the terms the platform reports; likes are excluded and link clicks are reported separately.
 Bar = median of organic posts in the scoring window; each dot is one post. Lines mark 0.3% (Fix), 0.6% (Keep) and 2.0% (Scale-eligible).
 Threads and YouTube Shorts report views, not reach, and no saves, so their ER uses views and is not comparable with Instagram. Platforms are never ranked against each other here.</p></header>
 <div class="rows" role="group" aria-label="Median engagement rate per account">{head}{''.join(rows)}</div>
 <div class="legendline"><span class="key"><i style="background:var(--ink2)"></i>bar = median</span><span class="key"><i style="border-radius:50%;width:8px;height:8px;background:var(--ink2)"></i>dot = one post (hollow = not scored yet)</span>
 <span>Zones: under 0.3% retire-review · 0.3% to 0.6% fix · 0.6% to 2.0% keep · 2.0% and over scale-eligible</span></div>
 <details><summary>Table view</summary><div class="tscroll"><table><caption>Engagement rate per account</caption>
 <thead><tr><th scope="col">Persona</th><th scope="col">Platform</th><th scope="col">Status</th><th class="num" scope="col">Posts</th><th class="num" scope="col">Median ER</th><th class="num" scope="col">Min</th><th class="num" scope="col">Max</th><th scope="col">Denominator</th><th scope="col">Terms used</th><th class="num" scope="col">Median interactions</th><th class="num" scope="col">Median reach or views</th><th scope="col">Window</th></tr></thead>
 <tbody>{''.join(table)}</tbody></table></div></details>
</section>"""


def section_saves(snap):
    pairs = er_rows(snap)
    rows, table = [], []
    for p, a in pairs:
        s = a["summary"]
        d = a["decision"]
        share = s["sv_share"]
        noref = False
        if share is None:
            valtxt = ("<strong>n/a</strong><br><small>platform reports no saves</small>" if s["n_scored"] else "<strong>no data</strong><br><small>no posts counted yet</small>")
            plot = ""
            noref = True
        else:
            tip = f"{p['name_zh']} {plat(a['platform'])}\nsaves + shares are {pct(share, 0)} of counted interactions\nmedian saves + shares per post {num(s['sv_median'], 1)}"
            plot = (f'<span class="bar" style="width:{share * 100:.2f}%" tabindex="0" role="img" aria-label="{esc(tip, quote=True)}" {tipattr(tip)}></span>')
            valtxt = f'<strong>{pct(share, 0)}</strong><br><small>median {num(s["sv_median"], 1)} saves+shares per post</small>'
        rows.append(f"""
<div class="row {pclass(p['slug'])}">
 <div class="lab"><span class="sw"></span><strong>{zh(p['name_zh'])}</strong> {esc(plat(a['platform']))}<small>n={s['n_scored']}</small></div>
 <div class="plot" style="min-height:22px">{'' if noref else refs([T.SAVES_SHARES_SCALE_SHARE], 1.0)}{plot}</div>
 <div class="val">{valtxt}</div></div>""")
        table.append(f"<tr><td>{zh(p['name_zh'])}</td><td>{esc(plat(a['platform']))}</td><td class=\"num\">{pct(share, 0)}</td><td class=\"num\">{num(s['sv_median'], 1)}</td><td class=\"num\">{s['n_scored']}</td></tr>")
    head = f'<div class="row head" aria-hidden="true"><div></div>{axis([0, 1 / 3, 1.0], 1.0, lambda t: pct(t, 0))}<div></div></div>'
    return f"""
<section class="block" id="saves" aria-labelledby="h-saves">
 <header><h2 id="h-saves">Saves plus shares, share of interactions</h2>
 <p>Saves and shares as a share of all counted interactions (saves + shares + comments) in the scoring window. The line marks one third, the Scale-eligible level.
 Scored only where the platform reports saves; where it does not, Scale cannot be confirmed on this row.</p></header>
 <div class="rows">{head}{''.join(rows)}</div>
 <details><summary>Table view</summary><div class="tscroll"><table><caption>Saves plus shares</caption>
 <thead><tr><th scope="col">Persona</th><th scope="col">Platform</th><th class="num" scope="col">Share of interactions</th><th class="num" scope="col">Median saves+shares per post</th><th class="num" scope="col">Posts</th></tr></thead>
 <tbody>{''.join(table)}</tbody></table></div></details>
</section>"""


def mini_line(vals, ymax, tipfn):
    n = len(vals)
    if n == 0 or all(v is None for v in vals):
        return '<div class="spark"></div>'
    xs = [(i / (n - 1) * 100 if n > 1 else 50) for i in range(n)]
    ys = [None if v is None else 38 - (v / ymax) * 34 for v in vals]
    segs, cur = [], []
    for x, y in zip(xs, ys):
        if y is None:
            if cur:
                segs.append(cur)
            cur = []
        else:
            cur.append((x, y))
    if cur:
        segs.append(cur)
    line = " ".join("M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in s) for s in segs)
    area = " ".join("M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in s) + f" L{s[-1][0]:.2f} 40 L{s[0][0]:.2f} 40 Z" for s in segs if len(s) > 1)
    last = next(((x, y) for x, y in reversed(list(zip(xs, ys))) if y is not None), None)
    hits = "".join(f'<span class="hit" style="left:{max(0, x - 50 / max(n, 2)):.2f}%;width:{100 / max(n, 2):.2f}%" aria-hidden="true" {tipattr(tipfn(i))}></span>'
                   for i, x in enumerate(xs))
    endpt = f'<span class="end" style="left:{last[0]:.2f}%;top:{last[1] / 40 * 100:.2f}%"></span>' if last else ""
    return (f'<div class="spark"><svg viewBox="0 0 100 40" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
            f'<path class="ar" d="{area}"/><path class="ln" d="{line}"/></svg>{endpt}{hits}</div>')


def section_trends(snap):
    cards, table = [], []
    for p in snap["personas"]:
        for a in p["accounts"]:
            fs, rs = a["followers_series"], a["reach_series"]
            if not fs and not rs:
                cards.append(f'<div class="mini {pclass(p["slug"])}"><h3><span class="sw"></span>{zh(p["name_zh"])} {esc(plat(a["platform"]))}</h3><p class="note">No data yet.</p></div>')
                continue
            weeks = sorted(set(fs) | set(rs))
            weeks_done = [w for w in weeks if w <= (a["week_now"] or 0) - 1] or weeks
            if not weeks_done:
                cards.append(f'<div class="mini {pclass(p["slug"])}"><h3><span class="sw"></span>{zh(p["name_zh"])} {esc(plat(a["platform"]))}</h3><p class="note">No data yet.</p></div>')
                continue
            fvals = [fs.get(w) for w in weeks_done]
            rvals = [rs.get(w) for w in weeks_done]
            unit = "views" if a["reach_source"] and "views" in a["reach_source"] else ("reach" if a["reach_source"] == "account daily" else "reach (from posts)")
            fy = max([v for v in fvals if v is not None] + [1]) * 1.05
            ry = max([v for v in rvals if v is not None] + [1]) * 1.05
            flast = next((v for v in reversed(fvals) if v is not None), None)
            rlast = next((v for v in reversed(rvals) if v is not None), None)
            trend = {"rising": "rising", "flat": "flat", "falling2": "falling 2 weeks", "falling3": "falling 3 weeks", "unknown": "not enough weeks"}[a["reach_trend"]]
            fst = a["follower_stats"] or {}
            cards.append(f"""
<div class="mini {pclass(p['slug'])}">
 <h3><span class="sw"></span>{zh(p['name_zh'])} {esc(plat(a['platform']))}</h3>
 <div class="pair">
  <figure><figcaption>Followers, weekly close</figcaption><div class="big">{num(flast)}</div>
   {mini_line(fvals, fy, lambda i: f'{p["name_zh"]} {plat(a["platform"])} week {weeks_done[i]}\nfollowers {num(fvals[i])}')}
   <div class="xl"><span>W{weeks_done[0]}</span><span>W{weeks_done[-1]}</span></div></figure>
  <figure><figcaption>Weekly {esc(unit)}</figcaption><div class="big">{num(rlast)}</div>
   {mini_line(rvals, ry, lambda i: f'{p["name_zh"]} {plat(a["platform"])} week {weeks_done[i]}\nweekly {unit} {num(rvals[i])}')}
   <div class="xl"><span>W{weeks_done[0]}</span><span>W{weeks_done[-1]}</span></div></figure>
 </div>
 <p class="note">Reach trend: <strong>{esc(trend)}</strong>. Follower growth positive in {fst.get('growth_weeks', 0)} of {fst.get('weeks_counted', 0)} weeks (Scale needs {T.FOLLOWER_GROWTH_WEEKS_SCALE} of 6, Keep {T.FOLLOWER_GROWTH_WEEKS_KEEP}); followers are recorded, not decided on alone.</p>
</div>""")
            table.append(f"<tr><th scope=\"row\">{zh(p['name_zh'])} {esc(plat(a['platform']))} followers</th>" + "".join(f"<td class=\"num\">{num(fs.get(w))}</td>" for w in weeks_done) + "</tr>")
            table.append(f"<tr><th scope=\"row\">{zh(p['name_zh'])} {esc(plat(a['platform']))} weekly {esc(unit)}</th>" + "".join(f"<td class=\"num\">{num(rs.get(w))}</td>" for w in weeks_done) + "</tr>")
    maxw = max([len(r.split("<td")) - 1 for r in table] + [0])
    return f"""
<section class="block" id="trends" aria-labelledby="h-trends">
 <header><h2 id="h-trends">Followers and reach, by account</h2>
 <p>Weekly closing follower count and weekly reach (views where the platform reports only views). Each chart starts at zero. Weeks are counted from each persona's first post.
 Followers and reach are different units, so they are separate charts. The reach label says whether the figure is reach or views.</p></header>
 <div class="minis">{''.join(cards)}</div>
 <details><summary>Table view</summary><div class="tscroll"><table><caption>Weekly values by week since first post (W1 = first week)</caption>
 <thead><tr><th scope="col">Series</th>{''.join(f'<th class="num" scope="col">W{i + 1}</th>' for i in range(maxw))}</tr></thead>
 <tbody>{''.join(table)}</tbody></table></div></details>
</section>"""


def section_links(snap):
    rows = []
    wmax = 0
    for p in snap["personas"]:
        lk = p["links"]
        if not lk or not lk["weekly"]:
            rows.append((p, None))
            continue
        wmax = max(wmax, len(lk["weekly"]))
        rows.append((p, lk))
    head = "".join(f'<th class="num" scope="col">W{i + 1}</th>' for i in range(wmax))
    body = []
    for p, lk in rows:
        if lk is None:
            body.append(f"<tr><th scope=\"row\">{zh(p['name_zh'])}</th><td colspan=\"{wmax + 3}\" class=\"small\">no link-click data yet (the click counter is not chosen yet; portfolio.md 6.1)</td></tr>")
            continue
        cells = ""
        for w in lk["weekly"]:
            tip = "week %d: %d clicks; %s per 1,000 reach" % (w["week"], w["clicks"], num(w["per_1000_reach"], 1))
            cells += '<td class="num" %s>%d<br><small>%s</small></td>' % (tipattr(tip), w["clicks"], num(w["per_1000_reach"], 1))
        cells += '<td class="num"></td>' * (wmax - len(lk["weekly"]))
        ok = lk["weeks_with_clicks"] >= T.LINK_WEEKS_SCALE
        body.append(f"<tr><th scope=\"row\">{zh(p['name_zh'])}</th>{cells}<td class=\"num\">{lk['weeks_with_clicks']} of {min(T.FOLLOWER_WEEKS, lk['weeks_counted'])}</td>"
                    f"<td>{esc(lk['source'] or 'none')}{' · ' + 'meets the 3-of-6 Scale test' if ok else ''}</td></tr>")
    return f"""
<section class="block" id="links" aria-labelledby="h-links">
 <header><h2 id="h-links">Link clicks, weekly, reported separately</h2>
 <p>Clicks on the persona's link-in-bio page (or platform link taps if no page counter exists), per week since the first post. The small figure under each count is clicks per 1,000 reach summed over the persona's accounts that week.
 Link clicks are never inside ER. The Scale test is clicks in 3 of the first 6 weeks, or one written enquiry.</p></header>
 <div class="tscroll"><table><caption>Link clicks per week (count, then per 1,000 reach)</caption>
 <thead><tr><th scope="col">Persona</th>{head}<th class="num" scope="col">Weeks with clicks</th><th scope="col">Source</th></tr></thead>
 <tbody>{''.join(body)}</tbody></table></div>
</section>"""


def section_review(snap):
    rej_rows, eff_rows = [], []
    for p in snap["personas"]:
        rj = p["rejection"]
        if not rj or not rj["n"]:
            rej_rows.append(f'<div class="row {pclass(p["slug"])}"><div class="lab"><span class="sw"></span><strong>{zh(p["name_zh"])}</strong></div><div class="plot" style="min-height:22px">{refs([0.1, 0.2, 0.3], 0.5)}</div><div class="val"><strong>no reviews</strong></div></div>')
        else:
            v = rj["value"]
            tip = f"{p['name_zh']}\n{rj['rejected']} of {rj['n']} drafts returned or rejected on the first pass ({pct(v, 0)})"
            cls = "bar" if rj["scored"] else "bar out"
            reasons = ", ".join(f"{k} {c}" for k, c in sorted(rj["reasons"].items())) or "none"
            rej_rows.append(f"""<div class="row {pclass(p['slug'])}"><div class="lab"><span class="sw"></span><strong>{zh(p['name_zh'])}</strong>
 <small>{rj['rejected']} of {rj['n']} drafts · {level_chip(T.effort_level('rejection_rate', v) if rj['scored'] else 'unknown')}</small></div>
 <div class="plot" style="min-height:22px">{refs([0.1, 0.2, 0.3], 0.5)}<span class="{cls}" style="width:{min(100, v / 0.5 * 100):.2f}%" tabindex="0" role="img" aria-label="{esc(tip, quote=True)}" {tipattr(tip)}></span></div>
 <div class="val"><strong>{pct(v, 0)}</strong><br><small>reasons: {esc(reasons)}</small></div></div>""")
        cells = []
        for m in ("operator_min_per_approval", "n7_min_per_master", "wife_min_per_master"):
            e = p["effort"].get(m)
            if e is None:
                cells.append('<td class="small">n/a</td>')
                continue
            lv = T.effort_level(m, e["value"]) if e["scored"] else "unknown"
            cells.append(f'<td>{num(e["value"], 1) if e["value"] is not None else "-"} min <small>(n={e["n"]})</small><br>{level_chip(lv)}</td>')
        eff_rows.append(f"<tr><th scope=\"row\">{zh(p['name_zh'])}</th>{''.join(cells)}</tr>")
    rtable = ""
    for p in snap["personas"]:
        rj = p["rejection"]
        if rj and rj["n"]:
            rtable += (f"<tr><th scope=\"row\">{zh(p['name_zh'])}</th><td class=\"num\">{rj['n']}</td><td class=\"num\">{rj['rejected']}</td><td class=\"num\">{pct(rj['value'], 1)}</td>"
                       f"<td>{esc(', '.join(f'{k} {c}' for k, c in sorted(rj['reasons'].items())) or 'none')}</td><td class=\"num\">{rj['near_misses']}</td>"
                       f"<td>{'scored' if rj['scored'] else 'not scored (under ' + str(T.MIN_REVIEWS_FOR_RATE) + ' drafts)'}</td></tr>")
        else:
            rtable += f"<tr><th scope=\"row\">{zh(p['name_zh'])}</th><td colspan=\"6\" class=\"small\">no reviews logged in the window</td></tr>"
    rtable = ('<details><summary>Table view</summary><div class="tscroll"><table><caption>First-pass review outcomes, weeks 4 to 6</caption>'
              '<thead><tr><th scope="col">Persona</th><th class="num" scope="col">Drafts reviewed</th><th class="num" scope="col">Returned or rejected</th><th class="num" scope="col">Rate</th>'
              '<th scope="col">Reasons</th><th class="num" scope="col">Near misses</th><th scope="col">Scored</th></tr></thead><tbody>' + rtable + '</tbody></table></div></details>')
    rhead = f'<div class="row head" aria-hidden="true"><div></div>{axis([0, 0.1, 0.2, 0.3, 0.5], 0.5, lambda t: pct(t, 0))}<div></div></div>'
    cap = snap["capacity"]
    if cap.get("available"):
        def meter(v, g):
            return f'<div class="meter" role="img" aria-label="{v:.0f} of {g}"><i style="width:{min(100, v / g * 100):.1f}%"></i></div>'
        capbox = f"""
<div class="kpis" style="margin-top:14px">
 <div class="tile"><div class="l">Operator minutes per week (logged, last {len(cap['weeks'])} weeks)</div><div class="v">{cap['operator_avg']:.0f}</div>{meter(cap['operator_avg'], cap['gate_operator'])}<div class="d">gate {cap['gate_operator']} · {chip('KEEP', 'under the gate') if cap['operator_avg'] <= cap['gate_operator'] else chip('RETIRE_REVIEW', 'over the gate')}</div></div>
 <div class="tile"><div class="l">Wife minutes per week (logged)</div><div class="v">{cap['wife_avg']:.0f}</div>{meter(cap['wife_avg'], cap['gate_wife'])}<div class="d">gate {cap['gate_wife']} · {chip('KEEP', 'under the gate') if cap['wife_avg'] <= cap['gate_wife'] else chip('RETIRE_REVIEW', 'over the gate')}</div></div>
 <div class="tile"><div class="l">Approvals (published posts) per week</div><div class="v">{cap['approvals_avg']:.1f}</div>{meter(cap['approvals_avg'], cap['gate_approvals'])}<div class="d">ceiling {cap['gate_approvals']} · {chip('KEEP', 'under the ceiling') if cap['approvals_avg'] <= cap['gate_approvals'] else chip('RETIRE_REVIEW', 'over the ceiling')}</div></div>
</div>
<p class="note">Capacity check (6.4): scaling is allowed only if all three are under their gates, averaged over the last four weeks. Only logged minutes are counted, so an incomplete time log understates the load.</p>"""
    else:
        capbox = '<p class="note">Capacity check (6.4): no time log yet, so the gates (operator 324 min, wife 510 min, 22 approvals per week) cannot be checked.</p>'
    return f"""
<section class="block" id="review" aria-labelledby="h-review">
 <header><h2 id="h-review">Review rejection and effort</h2>
 <p>Review-rejection rate = drafts the wife returns or rejects on the first pass, as a share of drafts she reviews, over weeks 4 to 6 (a returned-with-changes draft counts). Lines mark 10% (Scale), 20% (Keep) and 30% (retire-review after one redesign).
 Rates from fewer than {T.MIN_REVIEWS_FOR_RATE} reviewed drafts are shown as outlines and not scored.</p></header>
 <div class="rows">{rhead}{''.join(rej_rows)}</div>
 {rtable}
 <div class="tscroll" style="margin-top:14px"><table><caption>Effort per unit, scoring window (all-in minutes; scored when at least {T.MIN_EFFORT_UNITS} units are logged)</caption>
 <thead><tr><th scope="col">Persona</th><th scope="col">{esc(T.EFFORT_LABELS['operator_min_per_approval'])}</th><th scope="col">{esc(T.EFFORT_LABELS['n7_min_per_master'])}</th><th scope="col">{esc(T.EFFORT_LABELS['wife_min_per_master'])}</th></tr></thead>
 <tbody>{''.join(eff_rows)}</tbody></table></div>
 {capbox}
</section>"""


def section_money(snap):
    fin = snap["finance"]
    months = fin["months"]
    vmax = max([fin["cap_headroom"]] + [m["tool"] + m["one_time"] for m in months] + [m["received"] for m in months]) * 1.08
    rows = []
    for m in months:
        c, r = m["tool"], m["received"]
        rows.append(f"""
<div class="mrow"><div><strong>{esc(m['month'])}</strong></div>
 <div class="mplot" role="group" aria-label="{esc(m['month'])} tool spend {nt(c)}, revenue received {nt(r)}">
  {refs([fin['cap_base'], fin['cap_headroom']], vmax)}
  <span class="mbar cost" style="top:2px;width:{c / vmax * 100:.2f}%" tabindex="0" role="img" aria-label="tool spend {nt(c)}" {tipattr(f"{m['month']} tool spend {nt(c)}" + (f" (plus {nt(m['one_time'])} one-time, outside the cap)" if m['one_time'] else ""))}></span>
  <span class="l" style="top:-1px;left:calc({c / vmax * 100:.2f}% + 6px)">{nt(c)}{(" (+" + nt(m["one_time"]) + " one-time, outside the cap)") if m["one_time"] else ""}</span>
  <span class="mbar rev" style="top:20px;width:{r / vmax * 100:.2f}%" tabindex="0" role="img" aria-label="revenue {nt(r)}" {tipattr(f"{m['month']} revenue received {nt(r)}")}></span>
  <span class="l" style="top:17px;left:calc({r / vmax * 100:.2f}% + 6px)">{nt(r)}</span>
 </div></div>""")
    axis_html = (f'<div class="mrow" style="border:0;padding:0"><div></div><div class="axis" aria-hidden="true"><span style="left:0">NT$0</span>'
                 f'<span style="left:{fin["cap_base"] / vmax * 100:.2f}%">{nt(fin["cap_base"])} base cap</span>'
                 f'<span style="left:{fin["cap_headroom"] / vmax * 100:.2f}%">{nt(fin["cap_headroom"])} headroom</span></div></div>')
    trows = "".join(f"<tr><th scope=\"row\">{esc(m['month'])}</th><td class=\"num\">{nt(m['tool'])}</td><td class=\"num\">{nt(m['one_time'])}</td><td class=\"num\">{nt(m['received'])}</td><td class=\"num\">{nt(m['invoiced'])}</td><td class=\"num\">{nt(m['net'])}</td></tr>" for m in months)
    prow = ""
    for who, by in sorted(fin["revenue_by_persona"].items()):
        label = zh(next((p["name_zh"] for p in snap["personas"] if p["slug"] == who), who)) if who != "(studio)" else "studio (untagged)"
        prow += f"<tr><th scope=\"row\">{label}</th><td>{esc(', '.join(f'{k} {nt(v)}' for k, v in sorted(by.items())))}</td><td class=\"num\">{nt(sum(by.values()))}</td></tr>"
    if not prow:
        prow = '<tr><td colspan="3" class="small">No revenue received yet. Platform payouts are planned at NT$0 in year 1.</td></tr>'
    over = ""
    months_over = [m["month"] for m in months if m["tool"] > fin["cap_headroom"]]
    if months_over:
        over += f'<p class="flag crit">Tool spend was above the NT${fin["cap_headroom"]:,} ceiling in {esc(", ".join(months_over))}: portfolio.md 6.1 lists this as a retire-review trigger for the studio budget.</p>'
    if fin["current"]["tool"] > fin["cap_base"] and fin["current"]["tool"] <= fin["cap_headroom"]:
        over += f'<p class="flag">Tool spend this month is above the NT${fin["cap_base"]:,} base cap. The headroom is for a tool that clearly earns it.</p>'
    if fin["persona_tagged_cost"]:
        over += ('<p class="flag">Some tool spend is tagged to one persona. Portfolio.md 6.1 treats tool spend as studio-level and bars a persona-specific paid tool in the first 90 days.</p>')
    return f"""
<section class="block" id="money" aria-labelledby="h-money">
 <header><h2 id="h-money">Cost and revenue</h2>
 <p>Tool spend is studio-level and never allocated to one persona. One-time costs (registration, 記帳士, lawyer, TIPO filing) are outside the monthly cap. Only revenue marked received counts. Persona tags on revenue are for tracking; do not judge persona-level profit before month 6.</p></header>
 <div class="kpis">
  <div class="tile"><div class="l">Cumulative cost (tool + one-time)</div><div class="v">{nt(fin['cum_cost'])}</div></div>
  <div class="tile"><div class="l">Cumulative revenue received</div><div class="v">{nt(fin['cum_revenue'])}</div></div>
  <div class="tile"><div class="l">Net to date</div><div class="v">{'-' if fin['cum_net'] < 0 else ''}{nt(abs(fin['cum_net']))}</div><div class="d">{'revenue below cost' if fin['cum_net'] < 0 else 'revenue at or above cost'}</div></div>
 </div>
 {over}
 <div role="group" aria-label="Monthly tool spend and revenue received">{axis_html if rows else ''}{''.join(rows) or '<p class="note">No costs or revenue recorded yet.</p>'}</div>
 <div class="legendline"><span class="key"><i class="cost"></i>tool spend (one-time costs excluded)</span><span class="key"><i class="rev"></i>revenue received</span><span>Vertical lines: the base cap and the headroom ceiling.</span></div>
 <details><summary>Table view</summary><div class="tscroll"><table><caption>By month</caption>
 <thead><tr><th scope="col">Month</th><th class="num" scope="col">Tool spend</th><th class="num" scope="col">One-time costs</th><th class="num" scope="col">Revenue received</th><th class="num" scope="col">Invoiced, not received</th><th class="num" scope="col">Net</th></tr></thead>
 <tbody>{trows}</tbody></table></div>
 <div class="tscroll"><table><caption>Revenue received by persona tag</caption><thead><tr><th scope="col">Persona</th><th scope="col">By source</th><th class="num" scope="col">Total</th></tr></thead><tbody>{prow}</tbody></table></div></details>
</section>"""


def section_standing(snap):
    ev = snap["standing"]
    as_of = snap["as_of"].isoformat()
    names = {p["slug"]: p["name_zh"] for p in snap["personas"]}
    evrows = ""
    for e in ev:
        label, hours, action = T.GATES[e["gate"]]
        open_ = e["cleared_on"] is None or e["cleared_on"] > as_of
        evrows += (f"<tr><td>{esc(e['event_date'])}</td><td>{zh(names.get(e['persona'], e['persona']))}</td><td>{esc(plat(e['platform']) if e['platform'] else 'whole persona')}</td>"
                   f"<td>{esc(label)}</td><td>{esc(e['description'])}</td><td>{chip('PAUSE', 'Open') if open_ else chip('KEEP', 'Cleared ' + e['cleared_on'])}</td><td class=\"small\">{esc(action)}</td></tr>")
    if not evrows:
        evrows = '<tr><td colspan="7" class="small">No standing events logged.</td></tr>'
    ex = ""
    for e in snap["experiments"]:
        ex += (f"<tr><td>{esc(e['exp_id'])}</td><td>{zh(names.get(e['persona'], e['persona']))} {esc(plat(e['platform']) if e['platform'] else '')}</td><td>{esc(e['kind'])}{' (Fix)' if e['is_fix'] else ''}</td>"
               f"<td>{esc(e['name'])}</td><td>{esc(e['status'])}</td><td>{esc(e['start_date'])} to {esc(e['end_date'] or 'open')}</td><td class=\"small\">{esc(e['primary_metric'] or '')}</td>"
               f"<td class=\"num\">{pct(e['baseline_value']) if e['baseline_value'] is not None and e['baseline_value'] < 1 else num(e['baseline_value'], 1)}</td>"
               f"<td class=\"num\">{pct(e['result_value']) if e['result_value'] is not None and e['result_value'] < 1 else num(e['result_value'], 1)}</td><td>{esc(e['decision'] or '')}</td></tr>")
    if not ex:
        ex = '<tr><td colspan="10" class="small">No experiments logged yet. Template: analytics/experiments.md.</td></tr>'
    return f"""
<section class="block" id="standing" aria-labelledby="h-standing">
 <header><h2 id="h-standing">Account-standing events and experiments</h2>
 <p>Portfolio.md 6.2 gates override every number on this page: an open event pauses that account. Experiments follow the rule of one change at a time, four weeks per Fix.</p></header>
 <div class="tscroll"><table><caption>Standing events (6.2)</caption>
 <thead><tr><th scope="col">Date</th><th scope="col">Persona</th><th scope="col">Where</th><th scope="col">Gate</th><th scope="col">What happened</th><th scope="col">State</th><th scope="col">Rule</th></tr></thead><tbody>{evrows}</tbody></table></div>
 <div class="tscroll" style="margin-top:12px"><table><caption>Experiments</caption>
 <thead><tr><th scope="col">ID</th><th scope="col">Account</th><th scope="col">Kind</th><th scope="col">Name</th><th scope="col">Status</th><th scope="col">Dates</th><th scope="col">Metric</th><th class="num" scope="col">Baseline</th><th class="num" scope="col">Result</th><th scope="col">Decision</th></tr></thead><tbody>{ex}</tbody></table></div>
</section>"""


def section_rules():
    trs = "".join(f"<tr><th scope=\"row\">{esc(a)}</th><td>{esc(b)}</td><td>{esc(c)}</td><td>{esc(d)}</td><td>{esc(e)}</td></tr>" for a, b, c, d, e in T.THRESHOLD_TABLE_ROWS)
    return f"""
<section class="block" id="rules" aria-labelledby="h-rules">
 <header><h2 id="h-rules">Thresholds, definitions and caveats</h2></header>
 <details open><summary>Threshold table (portfolio.md 6.1) - all numbers are assumptions to confirm</summary><div class="tscroll"><table><caption>Thresholds applied</caption>
 <thead><tr><th scope="col">Metric</th><th scope="col">Scale-eligible</th><th scope="col">Keep</th><th scope="col">Fix (one 4-week experiment)</th><th scope="col">Retire-review</th></tr></thead><tbody>{trs}</tbody></table></div>
 <p class="note">No Taiwan engagement benchmark exists (the 0.2% to 1.9% virtual-influencer figures are vendor and tracker numbers, not Taiwan data, with unknown definitions). Recalibrate every threshold against the persona's own week-2 baseline before first applying it.</p></details>
 <details><summary>Decision tree (6.3), as coded</summary><ol>
  <li>Any account-standing gate open? Yes: pause. A restriction open over 14 days, or a second Ground-rule-6 event within 8 weeks, shows Retire.</li>
  <li>Enough data ({T.MIN_ORGANIC_POSTS} organic posts per platform in weeks 3 to 6)? No: extend to week 8 and re-run; still no: hold, no scoring.</li>
  <li>Effort breach after one redesign (operator over 15 min per approval, N7 over 40, wife over 20 per master, rejection over 30%)? Yes: retire-review. Over the line with no redesign logged: Fix, and do the redesign first.</li>
  <li>Median ER under 0.3%? Yes: retire-review.</li>
  <li>ER 0.3% to under 0.6%, or Keep conditions partly unmet? Yes: Fix, one variable for 4 weeks, then re-test; still under after the re-test: retire-review.</li>
  <li>ER 0.6% to under 2.0%, reach not falling, effort within Keep, rejection 20% or less? Yes: Keep.</li>
  <li>ER 2.0% or more and saves + shares one third of interactions, reach rising, effort and rejection within Scale, no standing event in the window, and a lead signal or link clicks in 3 of 6 weeks? Yes: Scale-eligible, then the capacity check (6.4).</li></ol></details>
 <details><summary>Definitions</summary><ul>
  <li><strong>Week n</strong> = days 7(n-1) to 7n-1 after the persona's first published post. Weeks 1 and 2 are warm-up.</li>
  <li><strong>Organic</strong> = not sponsored, gifted or affiliate. Sponsored posts are excluded from every median.</li>
  <li><strong>ER</strong> = (saves + shares + comments) / reach, per post, only the terms the platform reported. Where reach is blank the denominator is views, and that is labelled. Account figure = median of posts. Likes and link clicks are excluded.</li>
  <li><strong>Blank is not zero.</strong> A platform that does not report saves leaves them blank; they are never treated as 0.</li>
  <li><strong>Review-rejection rate</strong> counts any first-pass return or rejection.</li></ul></details>
 <details><summary>Sample-size caveats</summary><ul>
  <li>Each account figure is the median of at least {T.MIN_ORGANIC_POSTS} and usually 8 to 15 posts. At these sizes one or two unusual posts, one viral share or one missing metrics snapshot can move a median across a threshold. The dots show the spread; look at them.</li>
  <li>Small accounts have few interactions per post, so ER moves in steps (each row shows how much one interaction is worth). A difference of one or two interactions is not a finding.</li>
  <li>Posts whose latest snapshot is under 7 days old can still gain reach and interactions; the weekly report counts them.</li>
  <li>Nothing here is a statistical test. The report calls a difference real only if it is at least 1.5x and both sides have at least {T.MIN_GROUP_POSTS} posts, and even then as a hypothesis to test.</li>
  <li>Platform metric availability (reach, saves, link clicks) in Taiwan is unverified (HUMAN_TODO 10). Platforms are never compared with each other on ER.</li></ul></details>
</section>"""


# ---------------------------------------------------------------------------------------
# page
# ---------------------------------------------------------------------------------------
def render(snap, source_label, generated=None):
    generated = generated or dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    demo = snap["is_demo"]
    empty = (not demo) and snap["n_posts"] == 0 and snap["n_metric_rows"] == 0
    slugs = [p["slug"] for p in snap["personas"]]
    if demo:
        banner = ('<div class="banner" role="status"><strong>DEMO DATA</strong><span>Every number on this page was invented by analytics/demo_data.py to test the tools. '
                  'It is not evidence about any persona, platform or audience. Do not quote it.</span></div>')
    elif empty:
        banner = ('<div class="banner empty" role="status"><strong>NO DATA YET</strong><span>The real tracker holds no posts or metrics. Import CSVs (see analytics/README.md); '
                  'to preview this page with invented numbers run <code>python3 analytics/dashboard.py --demo</code>.</span></div>')
    else:
        banner = ""
    title = "Analytics dashboard (DEMO DATA)" if demo else "Analytics dashboard"
    nav = ('<nav class="sections" aria-label="Sections"><a href="#status">Status</a><a href="#er">Engagement rate</a><a href="#saves">Saves + shares</a>'
           '<a href="#trends">Followers and reach</a><a href="#links">Link clicks</a><a href="#review">Review and effort</a><a href="#money">Cost and revenue</a>'
           '<a href="#standing">Events and experiments</a><a href="#rules">Thresholds</a></nav>')
    body = "".join([section_kpis(snap), section_status(snap), section_er(snap), section_saves(snap), section_trends(snap), section_links(snap),
                    section_review(snap), section_money(snap), section_standing(snap), section_rules()])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<title>{esc(title)}</title>
<style>{CSS}
{persona_css(slugs)}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="wrap">
<header class="top">
 <div><h1>Studio analytics{' - DEMO DATA' if demo else ''}</h1>
 <p class="sub">As of {esc(snap['as_of'].isoformat())} · source: {esc(source_label)} · generated {esc(generated)} · offline page, no scripts needed to read it</p></div>
 <button class="theme" id="theme" type="button" aria-label="Change colour theme">Theme: auto</button>
</header>
{banner}
{nav}
<main id="main">{body}</main>
<footer><p>Definitions follow strategy/portfolio.md sections 6.1 to 6.4. Every threshold is an assumption awaiting the operator's confirmation. Taiwan platform metric availability is unverified.
Nothing on this page was scraped: all figures come from CSV files the operator exported or typed from each platform's own insights.</p></footer>
</div>
<div id="tip" role="tooltip" hidden></div>
<script>{JS}</script>
</body>
</html>
"""


def build(db_path, as_of=None, demo_fallback=False):
    path = Path(db_path)
    if path.exists():
        conn = tracker.connect(path, read_only=True)
        label = str(path.relative_to(HERE.parent)) if str(path).startswith(str(HERE.parent)) else str(path)
    else:
        conn = tracker.memory_db()
        shown = str(path.relative_to(HERE.parent)) if str(path).startswith(str(HERE.parent)) else str(path)
        label = f"{shown} (not created yet: showing an empty tracker)"
    try:
        snap = metrics.portfolio_snapshot(conn, as_of)
    finally:
        conn.close()
    return snap, label


def main(argv=None):
    ap = argparse.ArgumentParser(description="Write the static analytics dashboard.")
    ap.add_argument("--demo", action="store_true", help="use the DEMO database and write dashboard_demo.html")
    ap.add_argument("--db", help="database file (default: the real database, or the demo one with --demo)")
    ap.add_argument("--as-of", help="YYYY-MM-DD (default today; the DEMO database has its own date)")
    ap.add_argument("--out", help="output file")
    a = ap.parse_args(argv)
    db = Path(a.db) if a.db else (tracker.DEMO_DB if a.demo else tracker.REAL_DB)
    if a.demo and not db.exists():
        print(f"{db} does not exist: run python3 analytics/demo_data.py first", file=sys.stderr)
        return 2
    out = Path(a.out) if a.out else (HERE / ("dashboard_demo.html" if a.demo else "dashboard.html"))
    as_of = dt.date.fromisoformat(a.as_of) if a.as_of else None
    snap, label = build(db, as_of)
    out.write_text(render(snap, label), encoding="utf-8")
    print(f"wrote {out} ({'DEMO DATA' if snap['is_demo'] else 'real database'}, as of {snap['as_of']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
