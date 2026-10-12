#!/usr/bin/env python3
"""check_pages.py - static checks for the link-in-bio pages. Standard library only; makes NO network call.

    python3 launch/link-pages/check_pages.py            # draft mode: placeholders and the draft banner are expected
    python3 launch/link-pages/check_pages.py --final    # publication mode: placeholders, banner and TODO markers are errors
    python3 launch/link-pages/check_pages.py --list-todo

What it checks (each page: studio, fangcun, buzhou, sehuan):
  structure   lang="zh-Hant-TW", charset, viewport (zoom not blocked), one h1, a title, landmarks
  no trackers no script, iframe, embed, object, form or input; no inline event handlers or style attributes;
              no analytics strings; no stylesheet or image from another host; a CSP meta that blocks scripts
  links       external links only to an allow-list of hosts, with rel="noopener noreferrer"; no href="#";
              every #fragment exists; persona pages link only to the studio page (Ground rule 8)
  disclosure  the literal line 'AI 虛擬角色 / 由 明說角色工作室 創作與營運' is in the visible text
  language    the project's own scanners (pipeline/scripts/ground_rules.py) over the visible text: Simplified
              characters, mainland vocabulary, lived-experience words, health/finance/politics words.
              Denial sentences ("沒有穿過") are reported as INFO for a human to read, never fixed.
  contrast    WCAG 2.x contrast for every text colour pair in every theme of shared/linkpage.css (4.5:1)

It is a keyword and rule net, not a language review. The wife reads every character.
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.append(str(ROOT / "pipeline" / "scripts"))  # append, never insert: queue.py there shadows the stdlib module
try:
    import ground_rules  # type: ignore
except Exception:  # pragma: no cover
    ground_rules = None

PAGES = {"studio": "studio", "fangcun": "fangcun", "buzhou": "buzhou", "sehuan": "sehuan"}
PERSONAS = ["fangcun", "buzhou", "sehuan"]
PERSONA_NAMES = {"fangcun": "方寸", "buzhou": "步驟", "sehuan": "色環"}
DISCLOSURE = "AI 虛擬角色 / 由 明說角色工作室 創作與營運"
STUDIO_NAME = "明說角色工作室"
# Hosts a link may point to once the real accounts exist. Anything else is an error until a human adds it here.
ALLOWED_HOSTS = {
    "instagram.com", "www.instagram.com",
    "threads.net", "www.threads.net", "threads.com", "www.threads.com",
    "youtube.com", "www.youtube.com", "youtu.be",
}
# Sentences that STATE what the studio does not do. They contain words the blunt scanners flag (投資, 政治, 賺錢,
# 互相追蹤). They are copied from the bibles or portfolio.md and reviewed as disclaimers; the scanner skips exactly these
# sentences and says so. Any other hit still fails. The wife confirms each one reads as a disclaimer.
REVIEWED_DISCLAIMERS = [
    "不提供健康、醫療、投資或理財建議，也不談政治議題。",
    "不提供投資、醫療、法律或賺錢相關的建議。",
    "各角色的帳號不會互相追蹤、留言或推薦對方。",
]
TRACKER_STRINGS = [
    "google-analytics", "googletagmanager", "gtag(", "fbq(", "facebook.net", "connect.facebook", "matomo", "hotjar",
    "clarity.ms", "plausible", "umami", "mixpanel", "segment.com", "amplitude", "doubleclick", "adsbygoogle",
    "line-scdn", "tiktok", "pixel", "fonts.googleapis", "fonts.gstatic", "cdn.", "unpkg", "jsdelivr", "cloudflareinsights",
]
FORBIDDEN_TAGS = {"script", "iframe", "embed", "object", "form", "input", "button", "frame", "frameset", "audio", "video", "canvas", "svg"}
TOKENS = ["bg", "card", "text", "muted", "line", "btn-bg", "btn-text", "chip-bg", "chip-text", "accent", "focus",
          "todo-bg", "todo-text", "todo-line", "banner-bg", "banner-text"]
TEXT_PAIRS = [("text", "bg"), ("text", "card"), ("muted", "bg"), ("muted", "card"), ("btn-text", "btn-bg"),
              ("chip-text", "chip-bg"), ("todo-text", "todo-bg"), ("banner-text", "banner-bg")]
NONTEXT_PAIRS = [("focus", "bg"), ("focus", "card"), ("focus", "todo-bg")]  # focus ring must reach 3:1


# ----------------------------------------------------------------------------- html parsing
class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[tuple[str, dict]] = []
        self.text: list[str] = []
        self.title = ""
        self._in_title = False
        self._skip = 0
        self.lang_en_depth = 0

    def handle_starttag(self, tag, attrs):
        a = {k: (v if v is not None else "") for k, v in attrs}
        self.tags.append((tag, a))
        if tag == "title":
            self._in_title = True
        if tag in ("style", "script"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in ("style", "script") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        elif not self._skip:
            self.text.append(data)

    def visible_text(self) -> str:
        return re.sub(r"\s+", " ", "".join(self.text)).strip()


def hex_to_rgb(h: str):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def luminance(rgb):
    def ch(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(h1: str, h2: str) -> float:
    l1, l2 = luminance(hex_to_rgb(h1)), luminance(hex_to_rgb(h2))
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def parse_css_themes(css: str) -> dict[str, dict[str, str]]:
    """Return {theme-name: tokens}. 'studio' is the base; the other themes inherit missing tokens from it."""
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    blocks = re.findall(r"([^{}]+)\{([^{}]*)\}", css)
    themes: dict[str, dict[str, str]] = {}
    for sel, body in blocks:
        names = re.findall(r"\.theme-([a-z]+)", sel)
        if not names:
            continue
        tokens = dict(re.findall(r"--([a-z-]+)\s*:\s*(#[0-9A-Fa-f]{6})\s*;", body))
        for n in names:
            themes.setdefault(n, {}).update(tokens)
    base = themes.get("studio", {})
    for n, t in themes.items():
        for k, v in base.items():
            t.setdefault(k, v)
    return themes


# ----------------------------------------------------------------------------- checks
class Result:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warns: list[str] = []
        self.info: list[str] = []

    def err(self, m): self.errors.append(m)
    def warn(self, m): self.warns.append(m)
    def note(self, m): self.info.append(m)


def check_css(css_path: Path) -> tuple[Result, dict[str, dict[str, str]]]:
    r = Result()
    css = css_path.read_text(encoding="utf-8")
    bare = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    if re.search(r"@import|url\(\s*['\"]?https?:", bare, re.I):
        r.err("shared css: @import or an external url() is not allowed")
    if re.search(r"@font-face", bare, re.I):
        r.err("shared css: @font-face (web fonts) is not allowed; use the system font stack")
    themes = parse_css_themes(css)
    for n in ["studio", *PERSONAS]:
        if n not in themes:
            r.err(f"shared css: theme .theme-{n} is missing")
            continue
        for tk in TOKENS:
            if tk not in themes[n]:
                r.err(f"shared css: theme {n} lacks token --{tk}")
        for fg, bg in TEXT_PAIRS:
            if fg in themes[n] and bg in themes[n]:
                c = contrast(themes[n][fg], themes[n][bg])
                (r.err if c < 4.5 else r.note)(f"contrast {n}: --{fg} {themes[n][fg]} on --{bg} {themes[n][bg]} = {c:.2f}:1" + ("  (below 4.5:1)" if c < 4.5 else ""))
        for fg, bg in NONTEXT_PAIRS:
            if fg in themes[n] and bg in themes[n]:
                c = contrast(themes[n][fg], themes[n][bg])
                (r.err if c < 3.0 else r.note)(f"contrast {n}: --{fg} on --{bg} = {c:.2f}:1 (focus ring, needs 3:1)")
    return r, themes


def check_page(slug: str, final: bool, themes) -> Result:
    r = Result()
    path = HERE / slug / "index.html"
    if not path.exists():
        r.err(f"{path} does not exist")
        return r
    raw = path.read_text(encoding="utf-8")
    no_comments = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    p = Page()
    p.feed(no_comments)
    tags = p.tags
    names = [t for t, _ in tags]

    # --- structure
    html_attrs = next((a for t, a in tags if t == "html"), {})
    if html_attrs.get("lang") != "zh-Hant-TW":
        r.err(f'<html lang> must be "zh-Hant-TW", found {html_attrs.get("lang")!r}')
    if not raw.lstrip().lower().startswith("<!doctype html>"):
        r.err("missing <!doctype html>")
    if not any(t == "meta" and a.get("charset", "").lower() == "utf-8" for t, a in tags):
        r.err('missing <meta charset="utf-8">')
    vp = next((a.get("content", "") for t, a in tags if t == "meta" and a.get("name") == "viewport"), None)
    if vp is None:
        r.err("missing viewport meta")
    elif re.search(r"user-scalable\s*=\s*(no|0)|maximum-scale\s*=\s*1(\.0)?\b", vp):
        r.err("viewport blocks zoom (accessibility)")
    if not p.title.strip():
        r.err("empty <title>")
    elif "AI 虛擬角色" not in p.title:
        r.warn("<title> does not contain 'AI 虛擬角色'")
    if names.count("h1") != 1:
        r.err(f"expected exactly one <h1>, found {names.count('h1')}")
    for lm in ("header", "main", "footer"):
        if lm not in names:
            r.err(f"missing <{lm}> landmark")

    # --- CSP and trackers
    csp = next((a.get("content", "") for t, a in tags if t == "meta" and a.get("http-equiv", "").lower() == "content-security-policy"), "")
    if "default-src 'none'" not in csp:
        r.err("CSP meta must start from default-src 'none'")
    if re.search(r"script-src|unsafe-eval|unsafe-inline|https?:|\*", csp):
        r.err("CSP meta must not allow scripts, inline code, wildcards or other hosts")
    for t in sorted(set(names) & FORBIDDEN_TAGS):
        r.err(f"forbidden tag <{t}>")
    low = no_comments.lower()
    for s in TRACKER_STRINGS:
        if s in low:
            r.err(f"possible tracker or third-party string in the page: {s!r}")
    for t, a in tags:
        for k in a:
            if k.startswith("on"):
                r.err(f"inline event handler attribute {k!r} on <{t}>")
            if k == "style":
                r.err(f"inline style attribute on <{t}> (blocked by the CSP; use a class in shared/linkpage.css)")
        for k in ("href", "src", "action", "poster", "srcset"):
            v = a.get(k, "")
            if v.lower().startswith("javascript:"):
                r.err(f"javascript: URL in <{t} {k}>")
    for t, a in tags:
        if t == "link":
            rel = a.get("rel", "").lower()
            href = a.get("href", "")
            if rel == "stylesheet":
                if re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I) or href.startswith("//"):
                    r.err(f"stylesheet from another host: {href}")
                elif not (HERE / slug / href).resolve().exists():
                    r.err(f"stylesheet not found: {href}")
            elif rel == "icon":
                if not href.startswith("data:"):
                    r.err("icon must be a data: URL (no extra request)")
            else:
                r.err(f"unexpected <link rel={rel!r}>")
        if t == "img":
            src = a.get("src", "")
            if "alt" not in a:
                r.err("<img> without alt")
            if re.match(r"^[a-z][a-z0-9+.-]*:", src, re.I) and not src.startswith("data:"):
                r.err(f"image from another host: {src}")
    r.note(f"robots meta: {next((a.get('content') for t, a in tags if t == 'meta' and a.get('name') == 'robots'), 'none')}")

    # --- links
    ids = {a["id"] for _, a in tags if "id" in a}
    for t, a in tags:
        if t != "a":
            continue
        href = a.get("href", "")
        rel = a.get("rel", "")
        if href in ("", "#"):
            r.err('empty or "#" href (use a real target or the todo placeholder)')
        elif href.startswith("#"):
            if href[1:] not in ids:
                r.err(f"anchor {href} has no matching id")
        elif re.match(r"^https?://", href, re.I):
            host = re.sub(r"^https?://([^/:?#]+).*$", r"\1", href, flags=re.I).lower()
            if host not in ALLOWED_HOSTS:
                r.err(f"external link to a host that is not on the allow-list: {host}")
            if not ("noopener" in rel and "noreferrer" in rel):
                r.err(f'external link without rel="noopener noreferrer": {href}')
            if "HANDLE" in href:
                r.err(f"template handle left in link: {href}")
        elif href.startswith("mailto:"):
            r.warn(f"mailto link present: {href} (confirm it is the studio mailbox, not a personal one)")
        elif re.match(r"^[a-z][a-z0-9+.-]*:", href, re.I):
            r.err(f"unsupported link scheme: {href}")
        else:
            target = (HERE / slug / href)
            if target.is_dir():
                target = target / "index.html"
            if not target.resolve().exists():
                r.err(f"relative link target not found: {href}")
            m = re.match(r"^\.\./([a-z]+)/", href)
            if m and slug in PERSONAS and m.group(1) != "studio":
                r.err(f"persona page links to another persona page ({href}); only the studio page is allowed (Ground rule 8)")

    # --- disclosure and wording
    vis = p.visible_text()
    if DISCLOSURE not in vis:
        r.err(f"literal disclosure line not found in visible text: {DISCLOSURE!r}")
    if STUDIO_NAME not in vis:
        r.err("studio name not found in visible text")
    if slug in PERSONAS:
        own = PERSONA_NAMES[slug]
        if own not in vis:
            r.err(f"persona name {own} not in visible text")
        for other, nm in PERSONA_NAMES.items():
            if other != slug and nm in vis:
                r.warn(f"persona page mentions another persona's name {nm} (Ground rule 8: no cross-reference); check the context")
    if re.search(r"(?<!其)[他她]|(?<![他她])它們?", vis):
        r.warn("pronoun 他/她/它 found; copy should use the name or 「這個角色」 (bibles: no gendered pronouns)")
    if re.search(r"[真正]人實拍|非\s?AI|不是\s?AI", vis):
        r.err("wording that denies the AI disclosure")
    scan_vis = vis
    for d in REVIEWED_DISCLAIMERS:
        if d in scan_vis:
            scan_vis = scan_vis.replace(d, "")
            r.note(f"reviewed disclaimer excluded from the keyword scan (a human reads it): {d}")
    scan_fields = [("title", p.title), ("visible", scan_vis)]
    for t, a in tags:
        for k in ("alt", "aria-label", "content"):
            if a.get(k) and (k != "content" or t == "meta" and a.get("name") == "description"):
                scan_fields.append((f"{t}[{k}]", a[k]))
    if ground_rules is not None:
        for fld, text in scan_fields:
            for f in ground_rules.scan_text(text, f"{slug}:{fld}"):
                line = f.render()
                if f.level in ("ERROR", "FLAG"):
                    r.err("language scan: " + line)
                elif f.level == "WARN":
                    r.warn("language scan: " + line)
                else:
                    r.note("language scan: " + line)
    else:
        r.warn("ground_rules.py could not be imported; language scan skipped")

    # --- draft state
    todos = [a for t, a in tags if "todo" in a.get("class", "").split()]
    banner = any("draft-banner" in a.get("class", "").split() for _, a in tags)
    noindex = any(t == "meta" and a.get("name") == "robots" and "noindex" in a.get("content", "") for t, a in tags)
    body_class = next((a.get("class", "") for t, a in tags if t == "body"), "")
    theme = body_class.replace("theme-", "").strip()
    if theme not in themes:
        r.err(f"body class {body_class!r} has no theme in shared/linkpage.css")
    r.note(f"{len(todos)} placeholder(s) with class todo; draft banner {'present' if banner else 'absent'}")
    if final:
        if todos:
            r.err(f"{len(todos)} placeholder(s) still present")
        if banner:
            r.err("draft banner still present")
        if "【待填" in vis or "PENDING" in vis:
            r.err("visible 【待填 or PENDING text remains")
        if noindex:
            r.warn("robots noindex is still set (fine if you do not want the page indexed)")
        if "HANDLE" in raw:
            r.err("template text HANDLE remains")
    return r


def list_todo():
    for slug in PAGES:
        p = Page()
        raw = re.sub(r"<!--.*?-->", "", (HERE / slug / "index.html").read_text(encoding="utf-8"), flags=re.S)
        # crude: print the text of each todo span
        for m in re.finditer(r'<span class="todo">(.*?)</span>', raw, flags=re.S):
            print(f"{slug}: {m.group(1).strip()}")


def main(argv):
    if "--list-todo" in argv:
        list_todo()
        return 0
    final = "--final" in argv
    verbose = "-v" in argv or "--verbose" in argv
    failed = 0
    css_res, themes = check_css(HERE / "shared" / "linkpage.css")
    print("== shared/linkpage.css")
    for m in css_res.errors:
        print("  ERROR", m)
    if verbose:
        for m in css_res.info:
            print("  info ", m)
    else:
        worst = min((float(re.search(r"= ([0-9.]+):1", m).group(1)), m) for m in css_res.info if "= " in m and "focus" not in m)
        print(f"  info  lowest text contrast: {worst[1]}")
    failed += bool(css_res.errors)
    for slug in PAGES:
        res = check_page(slug, final, themes)
        status = "FAIL" if res.errors else "ok"
        print(f"== {slug}/index.html: {status} ({len(res.errors)} error, {len(res.warns)} warn)")
        for m in res.errors:
            print("  ERROR", m)
        for m in res.warns:
            print("  warn ", m)
        for m in res.info:
            if verbose or not m.startswith("language scan") or True:
                print("  info ", m)
        failed += bool(res.errors)
    print("\nRESULT:", "FAIL" if failed else "PASS", "(final mode)" if final else "(draft mode)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
