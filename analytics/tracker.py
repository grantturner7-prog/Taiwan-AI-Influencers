#!/usr/bin/env python3
"""tracker.py - the studio analytics database (Phase 7).

SQLite through the Python standard library. No network access, no scraping, no platform login.
Numbers get in by (a) CSV files you export or type from each platform's own insights page and
(b) `import-queue`, which only READS pipeline/review-queue/*/*/post.json.

Usage (from the project folder):
  python3 analytics/tracker.py init                      # create the REAL database (empty) and seed personas
  python3 analytics/tracker.py columns [KIND] [--md]     # the CSV columns each import expects
  python3 analytics/tracker.py templates                 # (re)write header-only CSV templates
  python3 analytics/tracker.py import KIND FILE.csv [--rename "Their Header=our_column"] [--skip-bad-rows]
  python3 analytics/tracker.py import-queue              # register queue drafts as posts + review events
  python3 analytics/tracker.py status                    # table counts, date ranges, DEMO flag
  python3 analytics/tracker.py schema                    # print the SQL schema

KINDs: accounts posts post_metrics account_daily costs revenue lead_signals effort reviews standing experiments

Blank cell = "the platform did not report this" and is stored as NULL. Zero must be typed as 0.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import re
import sqlite3
import sys
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
REAL_DB = HERE / "data" / "real" / "tracker.db"
DEMO_DB = HERE / "data" / "demo" / "tracker.db"
TEMPLATES_DIR = HERE / "templates"
QUEUE_DIR = PROJECT / "pipeline" / "review-queue"
SCHEMA_VERSION = "1"
DEMO_PREFIX = "DEMO-"

# ---------------------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------------------
SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS meta (
  key   TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

-- The ten persona slugs (portfolio.md 2A, personas/README.md). Only pilots get accounts at first.
CREATE TABLE IF NOT EXISTS personas (
  slug               TEXT PRIMARY KEY,
  name_zh            TEXT NOT NULL,
  niche              TEXT,
  wave               INTEGER,
  status             TEXT NOT NULL CHECK (status IN ('pilot','provisional','lawyer-gated')),
  assumed_first_post TEXT CHECK (date(assumed_first_post) IS assumed_first_post),
  notes              TEXT
);

CREATE TABLE IF NOT EXISTS platforms (
  code  TEXT PRIMARY KEY,
  name  TEXT NOT NULL,
  kind  TEXT NOT NULL CHECK (kind IN ('social','link_page')),
  notes TEXT
);

-- One row per persona x platform (an "account"). 'linkpage' = the persona's link-in-bio page counter.
CREATE TABLE IF NOT EXISTS accounts (
  persona   TEXT NOT NULL REFERENCES personas(slug),
  platform  TEXT NOT NULL REFERENCES platforms(code),
  handle    TEXT,
  role      TEXT NOT NULL DEFAULT 'primary' CHECK (role IN ('primary','secondary','link_page')),
  opened_on TEXT CHECK (date(opened_on) IS opened_on),
  PRIMARY KEY (persona, platform)
);

-- post_id equals the review-queue id (for example fangcun-2026-11-16-01) so the two line up.
CREATE TABLE IF NOT EXISTS posts (
  post_id          TEXT PRIMARY KEY,
  persona          TEXT NOT NULL,
  platform         TEXT NOT NULL,
  master_id        TEXT,
  format           TEXT CHECK (format IS NULL OR format IN ('carousel','reel','short','text','image')),
  pillar           TEXT,
  hook_type        TEXT,
  scheduled_date   TEXT CHECK (date(scheduled_date) IS scheduled_date),
  published_date   TEXT CHECK (date(published_date) IS published_date),
  status           TEXT NOT NULL DEFAULT 'draft'
                   CHECK (status IN ('draft','approved','scheduled','published','taken_down')),
  sponsorship_type TEXT NOT NULL DEFAULT 'none' CHECK (sponsorship_type IN ('none','paid','gifted','affiliate')),
  ai_label_on      INTEGER CHECK (ai_label_on IS NULL OR ai_label_on IN (0,1)),
  url              TEXT,
  notes            TEXT,
  FOREIGN KEY (persona, platform) REFERENCES accounts(persona, platform)
);

-- Per-post numbers by snapshot date. NULL = not reported by the platform (never write 0 for unknown).
-- reach may hold unique accounts or unique viewers; views holds views/impressions. ER uses reach,
-- else views, and the dashboard says which.
CREATE TABLE IF NOT EXISTS post_metrics (
  post_id       TEXT NOT NULL REFERENCES posts(post_id),
  snapshot_date TEXT NOT NULL CHECK (date(snapshot_date) IS snapshot_date),
  reach         INTEGER CHECK (reach IS NULL OR reach >= 0),
  views         INTEGER CHECK (views IS NULL OR views >= 0),
  likes         INTEGER CHECK (likes IS NULL OR likes >= 0),
  saves         INTEGER CHECK (saves IS NULL OR saves >= 0),
  shares        INTEGER CHECK (shares IS NULL OR shares >= 0),
  comments      INTEGER CHECK (comments IS NULL OR comments >= 0),
  link_clicks   INTEGER CHECK (link_clicks IS NULL OR link_clicks >= 0),
  PRIMARY KEY (post_id, snapshot_date)
);

-- Daily account-level numbers. For platform 'linkpage' only link_clicks is used.
CREATE TABLE IF NOT EXISTS account_daily (
  day                  TEXT NOT NULL CHECK (date(day) IS day),
  persona              TEXT NOT NULL,
  platform             TEXT NOT NULL,
  followers            INTEGER CHECK (followers IS NULL OR followers >= 0),
  reach                INTEGER CHECK (reach IS NULL OR reach >= 0),
  views                INTEGER CHECK (views IS NULL OR views >= 0),
  likes                INTEGER CHECK (likes IS NULL OR likes >= 0),
  saves                INTEGER CHECK (saves IS NULL OR saves >= 0),
  shares               INTEGER CHECK (shares IS NULL OR shares >= 0),
  comments             INTEGER CHECK (comments IS NULL OR comments >= 0),
  link_clicks          INTEGER CHECK (link_clicks IS NULL OR link_clicks >= 0),
  real_person_comments INTEGER CHECK (real_person_comments IS NULL OR real_person_comments >= 0),
  target_age_share     REAL CHECK (target_age_share IS NULL OR (target_age_share >= 0 AND target_age_share <= 1)),
  taiwan_share         REAL CHECK (taiwan_share IS NULL OR (taiwan_share >= 0 AND taiwan_share <= 1)),
  PRIMARY KEY (day, persona, platform),
  FOREIGN KEY (persona, platform) REFERENCES accounts(persona, platform)
);

-- Money. Costs are studio-level tool spend by default (persona NULL); persona is for tagging only.
CREATE TABLE IF NOT EXISTS costs (
  ref         TEXT PRIMARY KEY,
  cost_date   TEXT NOT NULL CHECK (date(cost_date) IS cost_date),
  persona     TEXT REFERENCES personas(slug),
  cost_kind   TEXT NOT NULL DEFAULT 'tool' CHECK (cost_kind IN ('tool','one_time')),
  category    TEXT NOT NULL,
  description TEXT NOT NULL,
  amount_twd  REAL NOT NULL CHECK (amount_twd >= 0),
  notes       TEXT
);

CREATE TABLE IF NOT EXISTS revenue (
  ref          TEXT PRIMARY KEY,
  revenue_date TEXT NOT NULL CHECK (date(revenue_date) IS revenue_date),
  persona      TEXT REFERENCES personas(slug),
  source_type  TEXT NOT NULL CHECK (source_type IN
               ('b2b_creative','affiliate','sponsored','sticker','product','platform_payout','licensing','other')),
  amount_twd   REAL NOT NULL CHECK (amount_twd >= 0),
  status       TEXT NOT NULL DEFAULT 'received' CHECK (status IN ('invoiced','received')),
  counterparty TEXT,
  notes        TEXT
);

-- Lead signals (portfolio.md 6.1 Revenue row): enquiry, accepted free sample, written quote, agency budget reply.
CREATE TABLE IF NOT EXISTS lead_signals (
  ref         TEXT PRIMARY KEY,
  signal_date TEXT NOT NULL CHECK (date(signal_date) IS signal_date),
  persona     TEXT NOT NULL REFERENCES personas(slug),
  kind        TEXT NOT NULL CHECK (kind IN
              ('outreach_sent','written_enquiry','accepted_free_sample','written_quote','agency_budget_reply')),
  notes       TEXT
);

-- Time log (operator and wife). Per-unit effort rows carry post_id and/or master_id.
CREATE TABLE IF NOT EXISTS effort_log (
  ref       TEXT PRIMARY KEY,
  log_date  TEXT NOT NULL CHECK (date(log_date) IS log_date),
  persona   TEXT REFERENCES personas(slug),
  post_id   TEXT,
  master_id TEXT,
  role      TEXT NOT NULL CHECK (role IN ('operator','wife')),
  task      TEXT NOT NULL CHECK (task IN
            ('approval','n7_recording','master_review','moderation','admin','analytics','other')),
  minutes   REAL NOT NULL CHECK (minutes >= 0),
  notes     TEXT
);

-- Review-rejection stats: one row per draft the wife reviewed, FIRST-PASS verdict.
-- 'changes' and 'rejected' both count as a rejection (portfolio.md 6.1: any returned-with-changes counts).
CREATE TABLE IF NOT EXISTS review_events (
  ref               TEXT PRIMARY KEY,
  post_id           TEXT NOT NULL,
  persona           TEXT NOT NULL REFERENCES personas(slug),
  platform          TEXT,
  reviewed_on       TEXT NOT NULL CHECK (date(reviewed_on) IS reviewed_on),
  reviewer          TEXT NOT NULL DEFAULT 'wife',
  first_pass_verdict TEXT NOT NULL CHECK (first_pass_verdict IN ('approved','changes','rejected')),
  reason_category   TEXT CHECK (reason_category IS NULL OR reason_category IN ('language','culture','safety','fact','other')),
  near_miss         INTEGER NOT NULL DEFAULT 0 CHECK (near_miss IN (0,1)),
  source            TEXT NOT NULL DEFAULT 'csv' CHECK (source IN ('csv','queue_snapshot')),
  notes             TEXT
);

-- Account-standing events (portfolio.md 6.2). cleared_on NULL = still open.
CREATE TABLE IF NOT EXISTS standing_events (
  ref          TEXT PRIMARY KEY,
  event_date   TEXT NOT NULL CHECK (date(event_date) IS event_date),
  persona      TEXT NOT NULL REFERENCES personas(slug),
  platform     TEXT,
  gate         TEXT NOT NULL CHECK (gate IN ('strike_restriction','rule6_contact','likeness_complaint',
                'disclosure_failure','real_person_comments','near_miss_rate','garbled_or_wrong')),
  description  TEXT NOT NULL,
  action_taken TEXT,
  cleared_on   TEXT CHECK (date(cleared_on) IS cleared_on)
);

CREATE TABLE IF NOT EXISTS experiments (
  exp_id          TEXT PRIMARY KEY,
  persona         TEXT NOT NULL REFERENCES personas(slug),
  platform        TEXT,
  hypothesis_ref  TEXT,
  kind            TEXT NOT NULL CHECK (kind IN ('hook','format','platform','cadence','redesign','other')),
  is_fix          INTEGER NOT NULL DEFAULT 0 CHECK (is_fix IN (0,1)),
  name            TEXT NOT NULL,
  hypothesis      TEXT,
  variable_changed TEXT,
  control         TEXT,
  treatment       TEXT,
  start_date      TEXT NOT NULL CHECK (date(start_date) IS start_date),
  end_date        TEXT CHECK (date(end_date) IS end_date),
  planned_posts   INTEGER,
  status          TEXT NOT NULL CHECK (status IN ('planned','running','done','abandoned')),
  primary_metric  TEXT,
  baseline_value  REAL,
  result_value    REAL,
  sample_n        INTEGER,
  decision        TEXT,
  notes           TEXT
);

CREATE INDEX IF NOT EXISTS ix_posts_acct   ON posts(persona, platform, published_date);
CREATE INDEX IF NOT EXISTS ix_daily_acct   ON account_daily(persona, platform, day);
CREATE INDEX IF NOT EXISTS ix_effort_p     ON effort_log(persona, log_date);
CREATE INDEX IF NOT EXISTS ix_review_p     ON review_events(persona, reviewed_on);

-- Latest metrics snapshot per post (what ER is computed from).
CREATE VIEW IF NOT EXISTS v_post_latest AS
SELECT p.post_id, p.persona, p.platform, p.master_id, p.format, p.pillar, p.hook_type,
       p.scheduled_date, p.published_date, p.status, p.sponsorship_type, p.url,
       m.snapshot_date, m.reach, m.views, m.likes, m.saves, m.shares, m.comments, m.link_clicks
FROM posts p
JOIN post_metrics m ON m.post_id = p.post_id
WHERE m.snapshot_date = (SELECT MAX(snapshot_date) FROM post_metrics WHERE post_id = p.post_id);
"""

# ---------------------------------------------------------------------------------------
# Seed data (portfolio.md 2A and personas/README.md). Dates are the doc's ASSUMED first posts.
# ---------------------------------------------------------------------------------------
PERSONA_SEED = [
    # slug, name_zh, niche, wave, status, assumed_first_post
    ("fangcun", "方寸", "N9 home organisation, small space and renting", 1, "pilot", "2026-11-16"),
    ("buzhou", "步驟", "N7 AI tools and productivity AI", 1, "pilot", "2026-11-16"),
    ("sehuan", "色環", "FAS1 fashion: outfit logic, colour, climate styling", 1, "pilot", "2026-11-16"),
    ("jiehua", "接話", "N10 language learning, English first", 2, "provisional", "2027-01-18"),
    ("zhuancheng", "轉乘", "N3 travel in Taiwan: transport and itineraries", 2, "provisional", "2027-01-18"),
    ("suisui", "歲歲", "N19 customs and festivals, non-political", 3, "provisional", "2027-03-08"),
    ("licheng", "里程", "N15 cars and scooters: licences, rules, specs", 3, "provisional", "2027-03-08"),
    ("guige", "規格", "N6 tech and gadgets: spec-sheet literacy", 4, "provisional", "2027-04-26"),
    ("dengyixia", "等一下", "FIN2 scam awareness (wealth, narrowed)", 4, "lawyer-gated", "2027-09-06"),
    ("guiwei", "歸位", "FIT1 gym etiquette and venue notices", 4, "lawyer-gated", "2027-10-18"),
]
PLATFORM_SEED = [
    ("instagram", "Instagram", "social", "Reach and saves reported by Instagram insights (Taiwan availability unverified)."),
    ("threads", "Threads", "social", "Views reported; saves not expected (unverified)."),
    ("youtube_shorts", "YouTube Shorts", "social", "Views reported; saves not expected (unverified)."),
    ("facebook", "Facebook Page", "social", "Pages only for personas (unverified)."),
    ("linkpage", "Link-in-bio page", "link_page", "Click counter not yet chosen (portfolio.md 6.1); rows appear only once a counter exists."),
]
# Pilot accounts: (persona, platform, role). Handles are NOT chosen yet and are left blank.
ACCOUNT_SEED = [
    ("fangcun", "instagram", "primary"), ("fangcun", "youtube_shorts", "secondary"), ("fangcun", "linkpage", "link_page"),
    ("buzhou", "youtube_shorts", "primary"), ("buzhou", "threads", "secondary"), ("buzhou", "linkpage", "link_page"),
    ("sehuan", "instagram", "primary"), ("sehuan", "threads", "secondary"), ("sehuan", "linkpage", "link_page"),
]


def connect(path: Path | str, create: bool = False, read_only: bool = False) -> sqlite3.Connection:
    """Open a database. create=True makes the folder and the schema."""
    path = Path(path)
    if read_only:
        conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    else:
        if create:
            path.parent.mkdir(parents=True, exist_ok=True)
        elif not path.exists():
            raise FileNotFoundError(f"database not found: {path} (run: python3 analytics/tracker.py init)")
        conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    if create and not read_only:
        conn.executescript(SCHEMA)
    return conn


def memory_db() -> sqlite3.Connection:
    """An empty, seeded in-memory database (used by the dashboard when no real database exists yet)."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    seed(conn)
    set_meta(conn, "is_demo", "0")
    return conn


def seed(conn: sqlite3.Connection) -> None:
    conn.executemany("INSERT OR IGNORE INTO personas(slug,name_zh,niche,wave,status,assumed_first_post) VALUES (?,?,?,?,?,?)", PERSONA_SEED)
    conn.executemany("INSERT OR IGNORE INTO platforms(code,name,kind,notes) VALUES (?,?,?,?)", PLATFORM_SEED)
    conn.executemany("INSERT OR IGNORE INTO accounts(persona,platform,role) VALUES (?,?,?)", ACCOUNT_SEED)
    conn.execute("INSERT OR IGNORE INTO meta(key,value) VALUES ('schema_version', ?)", (SCHEMA_VERSION,))
    conn.commit()


def set_meta(conn: sqlite3.Connection, key: str, value: str) -> None:
    conn.execute("INSERT INTO meta(key,value) VALUES (?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value", (key, value))
    conn.commit()


def get_meta(conn: sqlite3.Connection, key: str, default: str | None = None) -> str | None:
    row = conn.execute("SELECT value FROM meta WHERE key=?", (key,)).fetchone()
    return row["value"] if row else default


def is_demo(conn: sqlite3.Connection) -> bool:
    return get_meta(conn, "is_demo", "0") == "1"


def init_db(path: Path | str, demo: bool = False) -> sqlite3.Connection:
    conn = connect(path, create=True)
    seed(conn)
    if get_meta(conn, "is_demo") is None:
        set_meta(conn, "is_demo", "1" if demo else "0")
    return conn


# ---------------------------------------------------------------------------------------
# CSV import: declarative specs
# ---------------------------------------------------------------------------------------
@dataclass
class Col:
    name: str
    kind: str = "str"          # str date int float bool enum share persona platform
    required: bool = False
    choices: tuple = ()
    default: object = None
    doc: str = ""


@dataclass
class Spec:
    kind: str
    table: str
    key: tuple
    cols: list = field(default_factory=list)
    doc: str = ""
    auto_ref: bool = False     # a blank `ref` is replaced by a hash of the row (makes re-imports idempotent)


ENUM_FORMAT = ("carousel", "reel", "short", "text", "image")
ENUM_PLATFORM_NOTE = "instagram, threads, youtube_shorts, facebook, linkpage"

SPECS: dict[str, Spec] = {}


def _add(spec: Spec) -> None:
    SPECS[spec.kind] = spec


_add(Spec("accounts", "accounts", ("persona", "platform"), [
    Col("persona", "persona", True, doc="persona slug, for example fangcun"),
    Col("platform", "platform", True, doc=ENUM_PLATFORM_NOTE),
    Col("handle", doc="public handle once chosen (blank until then)"),
    Col("role", "enum", False, ("primary", "secondary", "link_page"), "secondary"),
    Col("opened_on", "date", doc="YYYY-MM-DD"),
], "One row per persona x platform. Pilots are seeded by `init`; add wave-2+ accounts here."))

_add(Spec("posts", "posts", ("post_id",), [
    Col("post_id", "str", True, doc="use the review-queue id, for example fangcun-2026-11-16-01"),
    Col("persona", "persona", True),
    Col("platform", "platform", True),
    Col("master_id", doc="the idea shared by its platform versions (wife review minutes are per master)"),
    Col("format", "enum", False, ENUM_FORMAT),
    Col("pillar"),
    Col("hook_type", doc="free label for the opening line type, for example question, number, claim, how-to"),
    Col("scheduled_date", "date"),
    Col("published_date", "date", doc="the day it went live; needed for status published"),
    Col("status", "enum", False, ("draft", "approved", "scheduled", "published", "taken_down"),
        doc="blank = published when published_date is set, else draft"),
    Col("sponsorship_type", "enum", False, ("none", "paid", "gifted", "affiliate"), "none",
        "anything other than none is excluded from organic medians"),
    Col("ai_label_on", "bool", doc="1 if the platform AI label was switched on"),
    Col("url"),
    Col("notes"),
], "One row per post. Re-importing a post_id replaces the row."))

_add(Spec("post_metrics", "post_metrics", ("post_id", "snapshot_date"), [
    Col("post_id", "str", True),
    Col("snapshot_date", "date", True, doc="the day you read the numbers; the latest snapshot per post is used"),
    Col("reach", "int", doc="accounts reached (Instagram) or unique viewers if the platform offers them; blank if not reported"),
    Col("views", "int", doc="views or impressions; used as the ER denominator only when reach is blank"),
    Col("likes", "int", doc="reported separately, never in ER"),
    Col("saves", "int", doc="blank where the platform does not report saves (Threads, Shorts): blank is NOT zero"),
    Col("shares", "int"),
    Col("comments", "int"),
    Col("link_clicks", "int", doc="only if the platform reports clicks per post"),
], "One row per post per snapshot date. The post must already exist in posts."))

_add(Spec("account_daily", "account_daily", ("day", "persona", "platform"), [
    Col("day", "date", True),
    Col("persona", "persona", True),
    Col("platform", "platform", True, doc="use linkpage for the link-in-bio click counter (only link_clicks is read)"),
    Col("followers", "int", doc="follower count at the end of that day"),
    Col("reach", "int"),
    Col("views", "int"),
    Col("likes", "int"),
    Col("saves", "int"),
    Col("shares", "int"),
    Col("comments", "int"),
    Col("link_clicks", "int"),
    Col("real_person_comments", "int", doc="your hand count of comments asking whether it is a real person"),
    Col("target_age_share", "share", doc="share of followers in the target age band, 0.45 or 45%, only if insights show it"),
    Col("taiwan_share", "share", doc="share of followers in Taiwan, only if insights show it"),
], "One row per account per day."))

_add(Spec("costs", "costs", ("ref",), [
    Col("ref", doc="optional stable id; blank = generated from the row"),
    Col("cost_date", "date", True),
    Col("persona", "persona", doc="leave blank: tool spend is studio-level and never allocated to one persona (portfolio.md 6.1)"),
    Col("cost_kind", "enum", False, ("tool", "one_time"), "tool",
        "tool = counts against the monthly cap; one_time = registration, 記帳士, lawyer, TIPO (outside the cap)"),
    Col("category", "str", True, doc="for example image_api, design_tool, domain, line_oa, legal"),
    Col("description", "str", True),
    Col("amount_twd", "float", True, doc="NT$, tax included if you can tell; say in notes"),
    Col("notes"),
], "One row per payment.", auto_ref=True))

_add(Spec("revenue", "revenue", ("ref",), [
    Col("ref"),
    Col("revenue_date", "date", True),
    Col("persona", "persona", doc="tagging only; B2B income is studio-level"),
    Col("source_type", "enum", True,
        ("b2b_creative", "affiliate", "sponsored", "sticker", "product", "platform_payout", "licensing", "other")),
    Col("amount_twd", "float", True),
    Col("status", "enum", False, ("invoiced", "received"), "received", "only received counts as revenue"),
    Col("counterparty"),
    Col("notes"),
], "One row per receipt or invoice.", auto_ref=True))

_add(Spec("lead_signals", "lead_signals", ("ref",), [
    Col("ref"),
    Col("signal_date", "date", True),
    Col("persona", "persona", True),
    Col("kind", "enum", True,
        ("outreach_sent", "written_enquiry", "accepted_free_sample", "written_quote", "agency_budget_reply"),
        doc="outreach_sent is counted but is not a signal"),
    Col("notes"),
], "Enquiries, accepted free samples, written quotes, agency budget replies; also outreach sent.", auto_ref=True))

_add(Spec("effort", "effort_log", ("ref",), [
    Col("ref"),
    Col("log_date", "date", True),
    Col("persona", "persona", doc="blank for studio-level time"),
    Col("post_id", doc="for per-approval rows"),
    Col("master_id", doc="for per-master rows (wife review, N7 recording)"),
    Col("role", "enum", True, ("operator", "wife")),
    Col("task", "enum", True, ("approval", "n7_recording", "master_review", "moderation", "admin", "analytics", "other"),
        doc="approval = pre-check + approval + rework for one post; master_review = wife; n7_recording = recording + claims check"),
    Col("minutes", "float", True),
    Col("notes"),
], "The time log (portfolio.md 5.5 step 5).", auto_ref=True))

_add(Spec("reviews", "review_events", ("ref",), [
    Col("ref"),
    Col("post_id", "str", True),
    Col("persona", "persona", True),
    Col("platform", "platform"),
    Col("reviewed_on", "date", True),
    Col("reviewer", "str", False, default="wife"),
    Col("first_pass_verdict", "enum", True, ("approved", "changes", "rejected"),
        doc="the verdict on her FIRST read of the draft; changes and rejected both count as a rejection"),
    Col("reason_category", "enum", False, ("language", "culture", "safety", "fact", "other")),
    Col("near_miss", "bool", False, default=0, doc="1 if the draft was caught with testimony, health, finance or income wording"),
    Col("notes"),
], "One row per draft reviewed (first pass).", auto_ref=True))

_add(Spec("standing", "standing_events", ("ref",), [
    Col("ref"),
    Col("event_date", "date", True),
    Col("persona", "persona", True),
    Col("platform", "platform", doc="blank = the whole persona"),
    Col("gate", "enum", True, tuple(
        ("strike_restriction", "rule6_contact", "likeness_complaint", "disclosure_failure",
         "real_person_comments", "near_miss_rate", "garbled_or_wrong"))),
    Col("description", "str", True),
    Col("action_taken"),
    Col("cleared_on", "date", doc="blank while the event is open"),
], "Account-standing events (portfolio.md 6.2).", auto_ref=True))

_add(Spec("experiments", "experiments", ("exp_id",), [
    Col("exp_id", "str", True, doc="for example E001"),
    Col("persona", "persona", True),
    Col("platform", "platform"),
    Col("hypothesis_ref", doc="H1..H9 from portfolio.md 4.2 if it tests one"),
    Col("kind", "enum", True, ("hook", "format", "platform", "cadence", "redesign", "other"),
        doc="hook, format, platform = a Fix experiment; redesign = the 'one redesign' before an effort retire-review"),
    Col("is_fix", "bool", False, default=0,
        doc="1 = this is the 4-week Fix experiment the decision tree asked for; its dates become the re-test window"),
    Col("name", "str", True),
    Col("hypothesis"),
    Col("variable_changed"),
    Col("control"),
    Col("treatment"),
    Col("start_date", "date", True),
    Col("end_date", "date"),
    Col("planned_posts", "int"),
    Col("status", "enum", True, ("planned", "running", "done", "abandoned")),
    Col("primary_metric"),
    Col("baseline_value", "float"),
    Col("result_value", "float"),
    Col("sample_n", "int"),
    Col("decision"),
    Col("notes"),
], "The experiments log (the markdown template is experiments.md)."))

IMPORT_ORDER = ["accounts", "posts", "post_metrics", "account_daily", "costs", "revenue",
                "lead_signals", "effort", "reviews", "standing", "experiments"]


class ImportErrorList(Exception):
    def __init__(self, errors):
        super().__init__("; ".join(errors[:3]))
        self.errors = errors


def _clean_header(h: str) -> str:
    return (h or "").strip().lstrip("﻿").lower().replace(" ", "_")


_INT_RE = re.compile(r"^-?\d{1,3}(,\d{3})+$|^-?\d+$")


def parse_cell(col: Col, raw: str, conn: sqlite3.Connection | None = None):
    """Return the Python value for one cell, or None for blank. Raises ValueError with a plain message."""
    s = (raw or "").strip()
    if s == "":
        return None
    k = col.kind
    if k in ("str",):
        return s
    if k == "date":
        s2 = s.replace("/", "-")
        try:
            return dt.date.fromisoformat(s2).isoformat()
        except ValueError:
            raise ValueError(f"{col.name}: '{s}' is not a date in YYYY-MM-DD form")
    if k == "int":
        if not _INT_RE.match(s):
            raise ValueError(f"{col.name}: '{s}' is not a whole number")
        v = int(s.replace(",", ""))
        if v < 0:
            raise ValueError(f"{col.name}: negative value {v}")
        return v
    if k == "float":
        s2 = s.replace(",", "").replace("NT$", "").replace("$", "").strip()
        try:
            v = float(s2)
        except ValueError:
            raise ValueError(f"{col.name}: '{s}' is not a number")
        if v < 0:
            raise ValueError(f"{col.name}: negative value {v}")
        return v
    if k == "bool":
        if s.lower() in ("1", "true", "yes", "y"):
            return 1
        if s.lower() in ("0", "false", "no", "n"):
            return 0
        raise ValueError(f"{col.name}: '{s}' must be 1 or 0")
    if k == "share":
        try:
            if s.endswith("%"):
                v = float(s[:-1]) / 100.0
            else:
                v = float(s)
        except ValueError:
            raise ValueError(f"{col.name}: '{s}' is not a share")
        if not 0 <= v <= 1:
            raise ValueError(f"{col.name}: '{s}' must be between 0 and 1 (write 0.45 or 45%)")
        return v
    if k == "enum":
        s2 = s.lower()
        if s2 not in col.choices:
            raise ValueError(f"{col.name}: '{s}' is not one of {', '.join(col.choices)}")
        return s2
    if k in ("persona", "platform"):
        return s.lower()
    raise ValueError(f"unknown column kind {k}")


@dataclass
class ImportResult:
    kind: str
    inserted: int = 0
    updated: int = 0
    warnings: list = field(default_factory=list)
    errors: list = field(default_factory=list)

    def summary(self) -> str:
        head = f"{self.kind}: {self.inserted} added, {self.updated} replaced"
        if self.errors:
            head += f", {len(self.errors)} problem row(s)"
        return head


def _row_ref(kind: str, values: dict) -> str:
    payload = json.dumps({k: values.get(k) for k in sorted(values) if k != "ref"}, ensure_ascii=False, sort_keys=True)
    return "auto-" + hashlib.sha1((kind + payload).encode("utf-8")).hexdigest()[:16]


def read_csv_rows(path: Path | str, rename: dict | None = None):
    """Read a CSV (UTF-8, with or without BOM). Returns (headers, rows) where rows are dicts keyed by our names."""
    rename = {_clean_header(k): _clean_header(v) for k, v in (rename or {}).items()}
    with open(path, "r", encoding="utf-8-sig", newline="") as fh:
        text = fh.read()
    reader = csv.reader(io.StringIO(text))
    try:
        raw_headers = next(reader)
    except StopIteration:
        raise ImportErrorList(["the file is empty"])
    headers = []
    for h in raw_headers:
        c = _clean_header(h)
        headers.append(rename.get(c, c))
    rows = []
    for i, rec in enumerate(reader, start=2):
        if not any((c or "").strip() for c in rec):
            continue
        row = dict(zip(headers, rec))
        extra = [c for c in rec[len(headers):] if (c or "").strip()]
        if extra:
            # more cells than headers: usually an unquoted thousands comma (1,200) or a stray comma in a note
            row["__extra__"] = extra
        rows.append((i, row))
    return headers, rows


def import_csv(conn: sqlite3.Connection, kind: str, path: Path | str, rename: dict | None = None,
               skip_bad_rows: bool = False) -> ImportResult:
    if kind not in SPECS:
        raise ImportErrorList([f"unknown kind '{kind}'. Choose from: {', '.join(IMPORT_ORDER)}"])
    spec = SPECS[kind]
    res = ImportResult(kind)
    if Path(path).name.upper().startswith("DEMO") and not is_demo(conn):
        raise ImportErrorList([f"'{Path(path).name}' is a DEMO file and cannot be imported into a real database"])
    headers, rows = read_csv_rows(path, rename)
    known = {c.name for c in spec.cols}
    missing = [c.name for c in spec.cols if c.required and c.name not in headers]
    if missing:
        raise ImportErrorList([f"missing required column(s): {', '.join(missing)}. Expected columns: {', '.join(c.name for c in spec.cols)}"])
    ignored = [h for h in headers if h and h not in known]
    if ignored:
        res.warnings.append(f"ignored unknown column(s): {', '.join(ignored)} (use --rename 'Their Header=our_column' to map them)")

    demo_db = is_demo(conn)
    personas = {r[0] for r in conn.execute("SELECT slug FROM personas")}
    accounts = {(r[0], r[1]) for r in conn.execute("SELECT persona, platform FROM accounts")}
    platforms = {r[0] for r in conn.execute("SELECT code FROM platforms")}
    parsed = []
    for line, raw in rows:
        vals, errs = {}, []
        if raw.get("__extra__"):
            errs.append(f"the row has {len(raw['__extra__'])} more cell(s) than the header ({', '.join(raw['__extra__'][:3])}): "
                        "a number such as 1,200 or a note with a comma must be inside double quotes")
        for col in spec.cols:
            try:
                v = parse_cell(col, raw.get(col.name, ""))
            except ValueError as e:
                errs.append(str(e))
                continue
            if v is None and col.default is not None:
                v = col.default
            if v is None and col.required:
                errs.append(f"{col.name}: required but blank")
            vals[col.name] = v
        if not errs:
            errs.extend(_row_checks(kind, vals, conn, personas, accounts, platforms))
        if not errs:
            key_text = " ".join(str(vals.get(k)) for k in spec.key)
            ident = [vals.get(k) for k in spec.key] + [vals.get("ref"), vals.get("exp_id"), vals.get("post_id")]
            if any(isinstance(x, str) and x.startswith(DEMO_PREFIX) for x in ident) and not demo_db:
                errs.append(f"'{key_text}' is DEMO data and cannot be imported into a real database")
        if errs:
            res.errors.append(f"line {line}: " + "; ".join(errs))
        else:
            if spec.auto_ref and not vals.get("ref"):
                vals["ref"] = _row_ref(kind, vals)
            parsed.append(vals)
    if res.errors and not skip_bad_rows:
        res.warnings.append("nothing was imported (fix the rows above, or pass --skip-bad-rows to import the good ones)")
        return res
    cols = [c.name for c in spec.cols]
    sets = ", ".join(f"{c}=excluded.{c}" for c in cols if c not in spec.key)
    sql = (f"INSERT INTO {spec.table} ({', '.join(cols)}) VALUES ({', '.join('?' for _ in cols)}) "
           f"ON CONFLICT({', '.join(spec.key)}) DO UPDATE SET {sets}" if sets else
           f"INSERT OR IGNORE INTO {spec.table} ({', '.join(cols)}) VALUES ({', '.join('?' for _ in cols)})")
    exists_sql = f"SELECT 1 FROM {spec.table} WHERE " + " AND ".join(f"{k}=?" for k in spec.key)
    try:
        conn.execute("BEGIN")
        for vals in parsed:
            if conn.execute(exists_sql, [vals[k] for k in spec.key]).fetchone():
                res.updated += 1
            else:
                res.inserted += 1
            conn.execute(sql, [vals.get(c) for c in cols])
        conn.commit()
    except sqlite3.Error as e:
        conn.rollback()
        res.errors.append(f"database refused the import ({e}); nothing was imported")
        res.inserted = res.updated = 0
    return res


def _row_checks(kind, v, conn, personas, accounts, platforms) -> list:
    errs = []
    if kind in ("accounts", "posts", "account_daily", "reviews", "lead_signals", "effort", "standing",
                "experiments", "costs", "revenue"):
        p = v.get("persona")
        if p and p not in personas:
            errs.append(f"persona '{p}' is not in the personas table")
    if kind in ("accounts",):
        if v["platform"] not in platforms:
            errs.append(f"platform '{v['platform']}' is not one of {ENUM_PLATFORM_NOTE}")
    if kind in ("posts", "account_daily"):
        if (v["persona"], v["platform"]) not in accounts:
            errs.append(f"no account row for {v['persona']} on {v['platform']} (add it with the accounts import first)")
    if kind in ("reviews", "standing", "experiments") and v.get("platform") and v["platform"] not in platforms:
        errs.append(f"platform '{v['platform']}' is not one of {ENUM_PLATFORM_NOTE}")
    if kind == "posts":
        if v.get("status") is None:
            v["status"] = "published" if v.get("published_date") else "draft"
        if v["status"] in ("published", "taken_down") and not v.get("published_date"):
            errs.append("status published needs published_date")
        if v.get("published_date") and v["status"] in ("draft", "approved", "scheduled"):
            errs.append(f"published_date is set but status is {v['status']}")
    if kind == "post_metrics":
        if not conn.execute("SELECT 1 FROM posts WHERE post_id=?", (v["post_id"],)).fetchone():
            errs.append(f"post '{v['post_id']}' is not in posts (import posts first)")
    if kind == "standing" and v.get("cleared_on") and v["cleared_on"] < v["event_date"]:
        errs.append("cleared_on is before event_date")
    if kind == "experiments" and v.get("end_date") and v["end_date"] < v["start_date"]:
        errs.append("end_date is before start_date")
    if kind == "effort" and v.get("task") in ("approval",) and not v.get("post_id") and not v.get("master_id"):
        pass  # allowed: unit-less rows still count toward weekly totals, but not toward per-approval averages
    return errs


# ---------------------------------------------------------------------------------------
# Review-queue sync (read-only on the queue)
# ---------------------------------------------------------------------------------------
@dataclass
class QueueSync:
    drafts_seen: int = 0
    posts_added: int = 0
    posts_updated: int = 0
    reviews_added: int = 0
    skipped: list = field(default_factory=list)


def import_queue(conn: sqlite3.Connection, queue_dir: Path | str = QUEUE_DIR, today: dt.date | None = None) -> QueueSync:
    """Register every review-queue draft as a post (status draft unless the tracker already knows better) and
    record the wife's CURRENT review state as a review event. Never writes to the queue.

    Caveat (also in README): the queue file holds only the current state. If she flipped 'changes' to
    'approved' before this ran, the first-pass verdict is lost. Run it after each of her review sessions, or
    log first-pass verdicts with the `reviews` CSV instead.
    """
    today = today or dt.date.today()
    out = QueueSync()
    queue_dir = Path(queue_dir)
    if not queue_dir.exists():
        out.skipped.append(f"{queue_dir} does not exist")
        return out
    accounts = {(r[0], r[1]) for r in conn.execute("SELECT persona, platform FROM accounts")}
    for path in sorted(queue_dir.glob("*/*/post.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as e:
            out.skipped.append(f"{path.relative_to(queue_dir)}: cannot read ({e})")
            continue
        out.drafts_seen += 1
        pid, persona, platform = data.get("id"), data.get("persona"), data.get("platform")
        if not pid or (persona, platform) not in accounts:
            out.skipped.append(f"{path.relative_to(queue_dir)}: no account row for {persona} on {platform}")
            continue
        if str(pid).startswith(DEMO_PREFIX) and not is_demo(conn):
            out.skipped.append(f"{pid}: DEMO id in a real database")
            continue
        existed = conn.execute("SELECT 1 FROM posts WHERE post_id=?", (pid,)).fetchone()
        fmt = data.get("format") if data.get("format") in ENUM_FORMAT else None
        sp = data.get("sponsorship_type") if data.get("sponsorship_type") in ("none", "paid", "gifted", "affiliate") else "none"
        label = 1 if data.get("ai_label_flag") is True else (0 if data.get("ai_label_flag") is False else None)
        try:
            conn.execute(
                """INSERT INTO posts(post_id,persona,platform,format,pillar,scheduled_date,status,sponsorship_type,ai_label_on)
                   VALUES (?,?,?,?,?,?,'draft',?,?)
                   ON CONFLICT(post_id) DO UPDATE SET format=excluded.format, pillar=excluded.pillar,
                     scheduled_date=excluded.scheduled_date, sponsorship_type=excluded.sponsorship_type""",
                (pid, persona, platform, fmt, data.get("pillar"), data.get("scheduled_date"), sp, label))
        except sqlite3.IntegrityError as e:
            out.skipped.append(f"{path.relative_to(queue_dir)}: database refused it ({e})")
            continue
        if existed:
            out.posts_updated += 1
        else:
            out.posts_added += 1
        rv = data.get("review") or {}
        verdict = {"approved": "approved", "changes": "changes"}.get(rv.get("wife_language"))
        if verdict:
            ref = f"queue-{pid}"
            if not conn.execute("SELECT 1 FROM review_events WHERE ref=?", (ref,)).fetchone():
                conn.execute(
                    """INSERT INTO review_events(ref,post_id,persona,platform,reviewed_on,first_pass_verdict,source,notes)
                       VALUES (?,?,?,?,?,?,'queue_snapshot',?)""",
                    (ref, pid, persona, platform, today.isoformat(), verdict,
                     "Recorded from the queue's current state, not necessarily her first pass. Add reason_category by hand."))
                out.reviews_added += 1
    conn.commit()
    return out


# ---------------------------------------------------------------------------------------
# Documentation helpers
# ---------------------------------------------------------------------------------------
def columns_markdown(kinds=None) -> str:
    lines = []
    for kind in (kinds or IMPORT_ORDER):
        spec = SPECS[kind]
        lines.append(f"### `{kind}`  (table `{spec.table}`)\n")
        lines.append(spec.doc + "\n")
        lines.append("| Column | Type | Required | Allowed values / notes |")
        lines.append("|---|---|---|---|")
        for c in spec.cols:
            t = {"str": "text", "date": "date YYYY-MM-DD", "int": "whole number", "float": "number", "bool": "1 or 0",
                 "enum": "one of", "share": "0 to 1 or %", "persona": "persona slug", "platform": "platform code"}[c.kind]
            allowed = ", ".join(c.choices) if c.choices else ""
            note = c.doc
            if c.default is not None:
                note = (note + " " if note else "") + f"Default: {c.default}."
            cell = (allowed + ("; " if allowed and note else "") + note).strip()
            lines.append(f"| `{c.name}` | {t} | {'yes' if c.required else 'no'} | {cell} |")
        lines.append("")
    return "\n".join(lines)


def write_templates(out_dir: Path | str = TEMPLATES_DIR) -> list:
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for kind in IMPORT_ORDER:
        p = out_dir / f"{kind}.csv"
        with open(p, "w", encoding="utf-8", newline="") as fh:
            csv.writer(fh).writerow([c.name for c in SPECS[kind].cols])
        written.append(p)
    return written


def status_text(conn: sqlite3.Connection) -> str:
    lines = [f"database: {'DEMO' if is_demo(conn) else 'REAL (not demo)'}"]
    for t in ["personas", "accounts", "posts", "post_metrics", "account_daily", "costs", "revenue", "lead_signals",
              "effort_log", "review_events", "standing_events", "experiments"]:
        n = conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        lines.append(f"  {t:<16}{n:>7}")
    r = conn.execute("SELECT MIN(published_date), MAX(published_date) FROM posts WHERE status='published'").fetchone()
    lines.append(f"  published posts: {r[0] or '-'} to {r[1] or '-'}")
    r = conn.execute("SELECT MIN(day), MAX(day) FROM account_daily").fetchone()
    lines.append(f"  account_daily:   {r[0] or '-'} to {r[1] or '-'}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------------------
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Studio analytics tracker (SQLite, standard library, no network).")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("init", "import", "import-queue", "status"):
        p = sub.add_parser(name)
        p.add_argument("--db", default=str(REAL_DB), help=f"database file (default {REAL_DB.relative_to(PROJECT)})")
        if name == "import":
            p.add_argument("kind", choices=IMPORT_ORDER)
            p.add_argument("file")
            p.add_argument("--rename", action="append", default=[], metavar="'THEIR HEADER=our_column'")
            p.add_argument("--skip-bad-rows", action="store_true")
        if name == "import-queue":
            p.add_argument("--queue-dir", default=str(QUEUE_DIR))
    sub.add_parser("schema")
    pc = sub.add_parser("columns")
    pc.add_argument("kind", nargs="?", choices=IMPORT_ORDER)
    pc.add_argument("--md", action="store_true")
    pt = sub.add_parser("templates")
    pt.add_argument("--out", default=str(TEMPLATES_DIR))
    a = ap.parse_args(argv)

    if a.cmd == "schema":
        print(SCHEMA)
        return 0
    if a.cmd == "columns":
        print(columns_markdown([a.kind] if a.kind else None))
        return 0
    if a.cmd == "templates":
        for p in write_templates(a.out):
            print("wrote", p)
        return 0
    if a.cmd == "init":
        path = Path(a.db)
        existed = path.exists()
        conn = init_db(path)
        print(("opened existing" if existed else "created") + f" {path} (personas and pilot accounts seeded; no metrics)")
        print("next: export or type numbers into the CSV templates in analytics/templates/, then `import`.")
        return 0
    try:
        conn = connect(a.db)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        return 2
    if a.cmd == "status":
        print(status_text(conn))
        return 0
    if a.cmd == "import-queue":
        r = import_queue(conn, a.queue_dir)
        print(f"drafts seen {r.drafts_seen}; posts added {r.posts_added}, updated {r.posts_updated}; review events added {r.reviews_added}")
        for s in r.skipped:
            print("  skipped:", s)
        return 0
    if a.cmd == "import":
        rename = {}
        for item in a.rename:
            if "=" not in item:
                print(f"--rename needs 'Their Header=our_column', got '{item}'", file=sys.stderr)
                return 2
            k, v = item.split("=", 1)
            rename[k] = v
        try:
            res = import_csv(conn, a.kind, a.file, rename, a.skip_bad_rows)
        except (ImportErrorList, OSError, UnicodeDecodeError) as e:
            errs = e.errors if isinstance(e, ImportErrorList) else [str(e)]
            for m in errs:
                print("error:", m, file=sys.stderr)
            return 1
        print(res.summary())
        for w in res.warnings:
            print("  note:", w)
        for m in res.errors:
            print("  ERROR", m)
        return 1 if res.errors and not a.skip_bad_rows else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
