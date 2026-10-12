"""dashboard.py: offline, labelled, escaped, accessible, well formed."""
import re
import tempfile
import unittest
import contextlib
import io
from html.parser import HTMLParser
from pathlib import Path

import _path  # noqa: F401
import dashboard
import demo_data
import metrics
import tracker
from testutil import REVIEW_DAY, close_all, day, fill_window, make_db

VOID = {"meta", "br", "hr", "img", "input", "link", "area", "base", "col", "embed", "source", "track", "wbr", "path", "circle", "rect"}
TMP = None
DEMO_HTML = None


def setUpModule():
    global TMP, DEMO_HTML
    TMP = tempfile.TemporaryDirectory()
    db, _ = demo_data.build_demo(Path(TMP.name))
    snap, label = dashboard.build(db)
    DEMO_HTML = dashboard.render(snap, label, generated="2000-01-01 00:00")


def tearDownModule():
    close_all()
    TMP.cleanup()


class Structure(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.errors, self.ids, self.tables, self.captions, self.headings = [], [], [], 0, 0, []
        self.attrs = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.attrs.append((tag, d))
        if "id" in d:
            self.ids.append(d["id"])
        if tag == "table":
            self.tables += 1
        if tag == "caption":
            self.captions += 1
        if tag in ("h1", "h2", "h3"):
            self.headings.append(tag)
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.attrs.append((tag, dict(attrs)))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"unexpected </{tag}> with stack {self.stack[-3:]}")
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
        else:
            self.stack.pop()


def parse(html):
    p = Structure()
    p.feed(html)
    p.close()
    return p


class Page(unittest.TestCase):
    def test_demo_banner_and_title(self):
        self.assertIn("<title>Analytics dashboard (DEMO DATA)</title>", DEMO_HTML)
        self.assertRegex(DEMO_HTML, r'<div class="banner" role="status"><strong>DEMO DATA</strong>')
        self.assertIn("invented by analytics/demo_data.py", DEMO_HTML)

    def test_offline_no_external_resources(self):
        self.assertNotRegex(DEMO_HTML, r"https?://")
        self.assertNotRegex(DEMO_HTML, r"(?i)<script[^>]*\ssrc=")
        self.assertNotRegex(DEMO_HTML, r"(?i)<link[\s>]")
        self.assertNotRegex(DEMO_HTML, r"(?i)@import|url\(|<img|<iframe|<object|<embed")
        self.assertNotIn("fonts.googleapis", DEMO_HTML)
        for tag, attrs in parse(DEMO_HTML).attrs:
            for k, v in attrs.items():
                if k in ("src", "href") and v:
                    self.assertTrue(v.startswith("#"), (tag, k, v))

    def test_well_formed_with_unique_ids_and_heading_order(self):
        p = parse(DEMO_HTML)
        self.assertEqual(p.errors, [])
        self.assertEqual(p.stack, [])
        self.assertEqual(len(p.ids), len(set(p.ids)))
        self.assertEqual(p.headings[0], "h1")
        self.assertEqual(p.headings.count("h1"), 1)
        self.assertNotIn("h4", p.headings)

    def test_accessibility_basics(self):
        self.assertIn('<html lang="en">', DEMO_HTML)
        self.assertIn('name="viewport"', DEMO_HTML)
        self.assertIn('class="skip" href="#main"', DEMO_HTML)
        self.assertIn('<main id="main">', DEMO_HTML)
        p = parse(DEMO_HTML)
        self.assertGreaterEqual(p.captions, p.tables - 1)                      # every data table is captioned
        self.assertGreaterEqual(DEMO_HTML.count("<summary>Table view</summary>"), 5)   # a table twin for each chart section
        self.assertIn('lang="zh-Hant-TW"', DEMO_HTML)
        for tag, a in p.attrs:
            if tag == "svg":
                self.assertEqual(a.get("aria-hidden"), "true")
            if tag == "section":
                self.assertIn("aria-labelledby", a)
        # status is never colour alone: every chip carries an svg icon and a word
        self.assertEqual(len(re.findall(r'<span class="chip [^"]*"><svg', DEMO_HTML)), len(re.findall(r'<span class="chip ', DEMO_HTML)))

    def test_light_dark_and_forced_colors_support(self):
        self.assertIn("@media (prefers-color-scheme:dark){:root:not([data-theme=\"light\"])", DEMO_HTML)
        self.assertIn(':root[data-theme="dark"]', DEMO_HTML)
        self.assertIn("@media (forced-colors:active)", DEMO_HTML)
        self.assertRegex(DEMO_HTML, r"body\{[^}]*background:var\(--page\)")
        for token in ("--s1:#2a78d6", "--s1:#3987e5", "--good:#0ca30c"):
            self.assertIn(token, DEMO_HTML)

    def test_persona_colour_follows_the_persona(self):
        self.assertIn(".p-fangcun{--c:var(--s1)}", DEMO_HTML)
        self.assertIn(".p-buzhou{--c:var(--s2)}", DEMO_HTML)
        self.assertIn(".p-sehuan{--c:var(--s3)}", DEMO_HTML)

    def test_required_content_is_present(self):
        for text in ("Scale, keep or retire", "Engagement rate per account", "Saves plus shares", "Followers and reach, by account",
                     "Link clicks, weekly, reported separately", "Review rejection and effort", "Cost and revenue", "Thresholds, definitions and caveats",
                     "2.0% or more", "0.6% to under 2.0%", "8 organic posts", "Sample-size caveats", "Scale-eligible"):
            self.assertIn(text, DEMO_HTML)
        for status in ("Keep", "Fix", "Pause", "Extend to week 8"):
            self.assertIn(status, DEMO_HTML)
        for slug_zh in ("方寸", "步驟", "色環"):
            self.assertIn(slug_zh, DEMO_HTML)

    def test_bar_widths_stay_inside_the_plot(self):
        for w in re.findall(r'class="(?:bar|mbar)[^"]*" style="(?:top:[^;]+;)?width:([0-9.]+)%', DEMO_HTML):
            self.assertLessEqual(float(w), 100.0)

    def test_output_is_reproducible_for_the_same_data(self):
        db = Path(TMP.name) / "tracker.db"
        snap, label = dashboard.build(db)
        again = dashboard.render(snap, label, generated="2000-01-01 00:00")
        self.assertEqual(again, DEMO_HTML)


class Escaping(unittest.TestCase):
    def test_untrusted_text_is_escaped(self):
        c = make_db()
        fill_window(c, n=10, er=0.01)
        evil = '<script>alert(1)</script>'
        c.execute("INSERT INTO experiments(exp_id,persona,platform,kind,name,start_date,status,decision) VALUES (?,?,?,?,?,?,?,?)",
                  ('E"1', "fangcun", "instagram", "hook", evil, day(30).isoformat(), "running", '"><img src=x onerror=alert(2)>'))
        c.execute("INSERT INTO standing_events(ref,event_date,persona,gate,description) VALUES (?,?,?,?,?)",
                  ("r1", day(30).isoformat(), "fangcun", "rule6_contact", '<b onmouseover="x()">hi</b>'))
        c.execute("UPDATE posts SET format=NULL, post_id=post_id")                    # no-op; keep the schema honest
        c.execute("INSERT INTO posts(post_id,persona,platform,format,pillar,published_date,status) VALUES (?,?,?,?,?,?,?)",
                  ('p"><i>', "fangcun", "instagram", "reel", "x", day(20).isoformat(), "published"))
        c.execute("INSERT INTO post_metrics(post_id,snapshot_date,reach,shares,comments) VALUES (?,?,?,?,?)", ('p"><i>', day(27).isoformat(), 500, 2, 1))
        c.commit()
        snap = metrics.portfolio_snapshot(c, REVIEW_DAY)
        html = dashboard.render(snap, "test")
        self.assertNotIn("<script>alert(1)", html)
        self.assertNotIn("<img src=x", html)
        self.assertNotIn('<b onmouseover', html)
        self.assertNotIn('<i>', html.replace("<i style", "").replace("<i class", ""))
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", html)
        self.assertEqual(parse(html).errors, [])
        # the page's own script tag is the only script
        self.assertEqual(len(re.findall(r"<script", html)), 1)


class States(unittest.TestCase):
    def test_empty_real_database_says_no_data_and_not_demo(self):
        snap, label = dashboard.build(Path(TMP.name) / "does-not-exist.db", REVIEW_DAY)
        html = dashboard.render(snap, label)
        self.assertIn("NO DATA YET", html)
        self.assertIn("not created yet", html)
        self.assertNotIn("<title>Analytics dashboard (DEMO DATA)</title>", html)
        self.assertNotRegex(html, r'<strong>DEMO DATA</strong>')
        self.assertEqual(parse(html).errors, [])
        self.assertIn("No revenue received yet", html)
        self.assertIn("No standing events logged", html)

    def test_real_data_has_no_banner(self):
        c = make_db()
        fill_window(c, n=10, er=0.01)
        html = dashboard.render(metrics.portfolio_snapshot(c, REVIEW_DAY), "real")
        self.assertNotIn('class="banner', html)
        self.assertNotIn("DEMO", html.split("<main")[0].replace("demo_data.py", ""))   # header and banner area only
        self.assertEqual(parse(html).errors, [])

    def test_unscored_accounts_show_hollow_dots_and_no_bar(self):
        c = make_db()
        fill_window(c, n=6, er=0.01)                                                     # extend state
        html = dashboard.render(metrics.portfolio_snapshot(c, REVIEW_DAY), "x")
        self.assertIn("dot hollow", html)
        self.assertIn("not scored", html)


class Cli(unittest.TestCase):
    def test_main_writes_only_where_told(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "x.html"
            with contextlib.redirect_stdout(io.StringIO()):
                rc = dashboard.main(["--demo", "--db", str(Path(TMP.name) / "tracker.db"), "--out", str(out)])
            self.assertEqual(rc, 0)
            self.assertIn("DEMO DATA", out.read_text(encoding="utf-8"))
            out2 = Path(d) / "y.html"
            with contextlib.redirect_stdout(io.StringIO()):
                rc = dashboard.main(["--db", str(Path(d) / "none.db"), "--out", str(out2), "--as-of", "2026-11-20"])
            self.assertEqual(rc, 0)
            self.assertIn("NO DATA YET", out2.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
