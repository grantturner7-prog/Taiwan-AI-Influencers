"""Builders for synthetic tracker databases used by the tests. Nothing here is real data."""
import datetime as dt

import _path  # noqa: F401
import tracker

FIRST = dt.date(2026, 11, 16)        # a Monday: week n starts at FIRST + 7*(n-1)
REVIEW_DAY = FIRST + dt.timedelta(days=42)


def day(offset):
    return FIRST + dt.timedelta(days=offset)


_OPEN = []


def make_db():
    """Empty in-memory tracker (seeded personas and pilot accounts), flagged not-demo."""
    c = tracker.memory_db()
    _OPEN.append(c)
    return c


def close_all():
    while _OPEN:
        _OPEN.pop().close()


def add_post(conn, pid, persona, platform, offset, *, fmt="carousel", pillar="A", hook="number", sponsorship="none",
             reach=1000, views=None, saves=None, shares=5, comments=5, likes=50, snapshot_offset=None, master=None,
             status="published"):
    d = day(offset)
    conn.execute("""INSERT INTO posts(post_id,persona,platform,master_id,format,pillar,hook_type,scheduled_date,published_date,status,sponsorship_type)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
                 (pid, persona, platform, master, fmt, pillar, hook, d.isoformat(), d.isoformat() if status == "published" else None, status, sponsorship))
    if reach is not None or views is not None:
        sd = day(offset + (snapshot_offset if snapshot_offset is not None else 7))
        conn.execute("""INSERT INTO post_metrics(post_id,snapshot_date,reach,views,likes,saves,shares,comments) VALUES (?,?,?,?,?,?,?,?)""",
                     (pid, sd.isoformat(), reach, views, likes, saves, shares, comments))
    conn.commit()


def add_account_days(conn, persona, platform, weekly_reach, weekly_followers=None, start=0):
    """weekly_reach: list of weekly totals (spread evenly over 7 days); weekly_followers: closing counts."""
    for w, total in enumerate(weekly_reach):
        for j in range(7):
            f = None
            if weekly_followers is not None and j == 6:
                f = weekly_followers[w]
            conn.execute("INSERT INTO account_daily(day,persona,platform,followers,reach) VALUES (?,?,?,?,?)",
                         (day(start + 7 * w + j).isoformat(), persona, platform, f, total // 7))
    conn.commit()


def add_review(conn, ref, pid, persona, offset, verdict, category=None, near_miss=0):
    conn.execute("""INSERT INTO review_events(ref,post_id,persona,reviewed_on,first_pass_verdict,reason_category,near_miss)
                    VALUES (?,?,?,?,?,?,?)""", (ref, pid, persona, day(offset).isoformat(), verdict, category, near_miss))
    conn.commit()


def add_effort(conn, ref, persona, offset, role, task, minutes, post_id=None, master_id=None):
    conn.execute("""INSERT INTO effort_log(ref,log_date,persona,post_id,master_id,role,task,minutes) VALUES (?,?,?,?,?,?,?,?)""",
                 (ref, day(offset).isoformat(), persona, post_id, master_id, role, task, minutes))
    conn.commit()


def fill_window(conn, persona="fangcun", platform="instagram", n=12, er=0.01, reach=1000, start=14, step=2, saves_on=True, prefix="P",
                flat_reach=True):
    """n organic posts from day `start`, `step` days apart, each with ER ~= er (exact: interactions = er*reach)."""
    inter = round(er * reach) if reach else 0
    # the persona's first published post is day 0 (week 1, warm-up, never in a window), so week numbers are relative to FIRST
    if not conn.execute("SELECT 1 FROM posts WHERE persona=? AND published_date=?", (persona, FIRST.isoformat())).fetchone():
        add_post(conn, f"ANCHOR-{persona}-{platform}", persona, platform, 0, reach=1000, saves=1, shares=1, comments=1)
    if flat_reach and not conn.execute("SELECT 1 FROM account_daily WHERE persona=? AND platform=?", (persona, platform)).fetchone():
        add_account_days(conn, persona, platform, [7000] * 9)          # flat weekly reach, so the reach trend never interferes
    for i in range(n):
        s = inter // 3 if saves_on else None
        sh = inter // 3
        cm = inter - (s or 0) - sh
        add_post(conn, f"{prefix}{persona}-{platform}-{i:02d}", persona, platform, start + i * step, reach=reach,
                 saves=s, shares=sh, comments=cm)
