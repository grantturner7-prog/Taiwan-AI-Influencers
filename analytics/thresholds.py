"""thresholds.py - every number the analytics code applies, in one place.

Source: strategy/portfolio.md section 6.1 (threshold table), 6.2 (account-standing gates),
6.3 (decision tree), 6.4 (capacity check), 7 (cost envelope), 4.2 (hypotheses).

Labels used below:
  DOC         the number is written in portfolio.md.
  ASSUMPTION  the number is NOT in portfolio.md; the analytics code needed a rule and chose one.
              Each is listed in README.md section 8 so the operator can overrule it.

Portfolio.md itself says every threshold is an assumption "proposed for the user to confirm" and
must be recalibrated against the persona's own week-2 baseline before it is first applied. Change a
number HERE (one place) and the tracker, dashboard, weekly report and tests all follow.

Fractions, not percents: 0.006 means 0.6%.
"""
from __future__ import annotations

# ---- Windows (DOC 6.1, 6.3) -----------------------------------------------------------
# Week n of a persona = days [7*(n-1), 7*n) after its first published post.
WARMUP_WEEKS = 2                 # DOC: weeks 1 and 2 are warm-up
WINDOW_FIRST_WEEK = 3            # DOC: weeks 3 to 6
WINDOW_LAST_WEEK = 6             # DOC
EXTENDED_LAST_WEEK = 8           # DOC: "extend to week 8"
REJECTION_FIRST_WEEK = 4         # DOC: rejection rate scored on weeks 4 to 6
REJECTION_LAST_WEEK = 6          # DOC
MIN_ORGANIC_POSTS = 8            # DOC: 8 organic posts per platform
FOLLOWER_WEEKS = 6               # DOC: "3 of 6 weeks", "4 of 6 weeks"
FIX_EXPERIMENT_WEEKS = 4         # DOC: Fix = "one 4-week experiment"

# ---- Engagement rate, per account (DOC 6.1 table, ER row) -----------------------------
ER_SCALE = 0.020                 # DOC: 2.0% or more = scale-eligible
ER_KEEP = 0.006                  # DOC: 0.6% to under 2.0% = keep
ER_FIX = 0.003                   # DOC: 0.3% to under 0.6% = fix; under 0.3% = retire-review

# ER definition switch. DOC 6.1 allows link clicks in the numerator only when the platform
# reports them PER POST, and says they normally are not; the stream brief says report link
# clicks separately. False = follow the brief (ER = (saves+shares+comments)/reach).
ER_INCLUDES_POST_LINK_CLICKS = False

# ---- Saves + shares (DOC 6.1) ----------------------------------------------------------
SAVES_SHARES_SCALE_SHARE = 1 / 3  # DOC: one third or more of counted interactions

# ---- Reach trend (DOC 6.1 gives the words; the numeric band is ASSUMPTION) --------------
REACH_FLAT_BAND = 0.05           # ASSUMPTION: a week-on-week move within +/-5% counts as flat

# ---- Link clicks (DOC 6.1) --------------------------------------------------------------
LINK_WEEKS_SCALE = 3             # DOC: tracked clicks in 3 of 6 weeks (or one enquiry)
LEAD_OUTREACH_NO_SIGNAL = 10     # DOC: zero enquiries after 10 tailored outreach messages

# ---- Followers (DOC 6.1; record, do not decide on alone) ---------------------------------
FOLLOWER_GROWTH_WEEKS_SCALE = 4  # DOC: net weekly growth positive in 4 of 6 weeks
FOLLOWER_GROWTH_WEEKS_KEEP = 3   # DOC: 3 of 6
FOLLOWER_DROP = 0.10             # DOC: unexplained week-on-week drop over 10%
FOLLOWER_DROP_MIN_BASE = 100     # ASSUMPTION: ignore drops on bases under 100 followers (noise)
TARGET_AGE_SHARE_SCALE = 0.60    # DOC: 60% or more in the target age band
TAIWAN_SHARE_SCALE = 0.80        # DOC: 80% or more in Taiwan
TARGET_AGE_SHARE_RETIRE = 0.40   # DOC: under 40% target age band

# ---- Effort and rejection: (scale_max, keep_max, fix_max); above fix_max = retire-review ---
# DOC 6.1 rows. Level names: 'scale' <= scale_max, 'keep' <= keep_max, 'fix' <= fix_max, else 'retire'.
EFFORT_LEVELS = {
    "operator_min_per_approval": (8.0, 12.0, 15.0),   # DOC
    "n7_min_per_master": (20.0, 30.0, 40.0),          # DOC
    "wife_min_per_master": (10.0, 15.0, 20.0),        # DOC
    "rejection_rate": (0.10, 0.20, 0.30),             # DOC
}
EFFORT_LABELS = {
    "operator_min_per_approval": "Operator minutes per approval (all-in)",
    "n7_min_per_master": "N7 recording plus claims check, minutes per master",
    "wife_min_per_master": "Wife minutes per master",
    "rejection_rate": "Review-rejection rate (first pass, weeks 4 to 6)",
}
MIN_EFFORT_UNITS = 5             # ASSUMPTION: fewer logged units than this = shown, not scored
MIN_REVIEWS_FOR_RATE = 5         # ASSUMPTION: fewer reviewed drafts than this = shown, not scored

# ---- Capacity check (DOC 6.4, 5.1) --------------------------------------------------------
OPERATOR_PLANNED_LOAD_GATE = 324  # DOC: minutes per week, averaged over the last four weeks
WIFE_PLANNED_LOAD_GATE = 510      # DOC: minutes per week, averaged over the last four weeks
MAX_APPROVALS_PER_WEEK = 22       # DOC: planning ceiling
CAPACITY_AVG_WEEKS = 4            # DOC

# ---- Cost envelope (DOC 7, DECISIONS Q1) --------------------------------------------------
MONTHLY_TOOL_CAP_BASE = 5000      # DOC: NT$5,000 base case
MONTHLY_TOOL_CAP_HEADROOM = 10000  # DOC: NT$10,000 only if a tool clearly earns it

# ---- Standing-gate rules (DOC 6.2) ---------------------------------------------------------
# gate code -> (label, hours allowed to fix/respond or None, what 6.2 says to do)
GATES = {
    "strike_restriction": ("Platform strike, restriction, label dispute or AI-label violation", 24 * 14,
                           "Pause that persona on that platform immediately; not cleared in 14 days = stop it there"),
    "rule6_contact": ("Ground-rule-6 contact in a published post", 24,
                      "Take down within 24 hours, pause the persona 7 days; a second event within 8 weeks retires it"),
    "likeness_complaint": ("Likeness complaint or credible look-alike claim", 24,
                           "Take down within 24 hours; pause until a documented look-alike check"),
    "disclosure_failure": ("Disclosure or sponsorship/gifted-goods disclosure missing", 24,
                           "Fix within 24 hours; a repeat in the same quarter pauses the persona"),
    "real_person_comments": ("5 or more comments in one week asking whether it is a real person", 48,
                             "Strengthen the first-line and on-screen label within 48 hours"),
    "near_miss_rate": ("3 or more of any 20 drafts caught with testimony, health, finance or income wording", None,
                       "Redesign the content pillars before continuing"),
    "garbled_or_wrong": ("Garbled or Simplified Chinese, or a wrong fact, reached publication", 24,
                         "Correct within 24 hours; two in 6 weeks = pause until the QA step is fixed"),
}
RULE6_REPEAT_DAYS = 56            # DOC: 8 weeks
STRIKE_STOP_DAYS = 14             # DOC
REAL_PERSON_WEEKLY_ALERT = 5      # DOC (also H1 in 4.2)
NEAR_MISS_WINDOW_DRAFTS = 20      # DOC
NEAR_MISS_ALERT = 3               # DOC
GARBLED_REPEAT_DAYS = 42          # DOC: two in 6 weeks

# ---- Analysis rules used by the weekly report (ASSUMPTION unless noted) --------------------
GROUP_RATIO = 1.5                 # DOC 4.2 H2 uses 1.5x for "clearly stronger"; reused for every comparison
MIN_GROUP_POSTS = 4               # ASSUMPTION: a format/pillar/hook group needs 4 posts to be named (3 gave false alarms in the demo)
MIN_ARM_POSTS = 4                 # ASSUMPTION: each arm of a new experiment needs 4 posts

# Status vocabulary (code -> display label). Order = display order for rankings, best first.
STATUS_LABELS = {
    "SCALE_ELIGIBLE": "Scale-eligible",
    "KEEP": "Keep",
    "FIX": "Fix",
    "EXTEND": "Extend to week 8",
    "HOLD": "Hold, no scoring",
    "IN_PROGRESS": "In progress",
    "NOT_STARTED": "Not started",
    "RETIRE_REVIEW": "Retire-review",
    "PAUSE": "Pause",
    "RETIRE": "Retire (repeat event)",
}
# Used to pick a persona's headline from its accounts: higher = better. PAUSE and RETIRE are
# never chosen as a headline while another account is active (they are listed separately).
STATUS_RANK = {
    "SCALE_ELIGIBLE": 8, "KEEP": 7, "FIX": 6, "EXTEND": 5, "HOLD": 4, "IN_PROGRESS": 3,
    "NOT_STARTED": 2, "RETIRE_REVIEW": 1, "PAUSE": 0, "RETIRE": -1,
}

THRESHOLD_TABLE_ROWS = [
    # (metric, scale, keep, fix, retire-review, kind) for the dashboard definitions panel
    ("Engagement rate (median, weeks 3 to 6)", "2.0% or more", "0.6% to under 2.0%", "0.3% to under 0.6%",
     "under 0.3%, or still under 0.6% after a Fix re-test"),
    ("Reach trend (weekly)", "rising over the last 3 weeks", "flat or rising", "falling for 2 weeks",
     "falling 3 weeks in a row and ER under 0.6% (table flag; the tree decides the status)"),
    ("Saves + shares share of interactions", "one third or more", "reported, no threshold", "n/a", "n/a"),
    ("Link clicks (persona, weekly)", "clicks in 3 of 6 weeks, or one enquiry", "tracking live", "n/a",
     "zero enquiries after 10 outreach messages and ER under 0.6%"),
    ("Operator minutes per approval", "8 or less", "12 or less", "over 12 to 15", "over 15 after one redesign"),
    ("N7 recording + claims check per master", "20 or less", "30 or less", "over 30", "over 40 after one redesign"),
    ("Wife minutes per master", "10 or less", "15 or less", "over 15 to 20", "over 20 after one redesign"),
    ("Review-rejection rate (weeks 4 to 6)", "10% or less", "20% or less", "over 20% to 30%",
     "over 30% after one redesign"),
    ("Followers (recorded, never decided on alone)", "growth in 4 of 6 weeks; 60% or more in the target age band; 80% or more in Taiwan",
     "growth in 3 of 6 weeks", "unexplained week-on-week drop over 10%", "target age band under 40% (allow one re-target first)"),
    ("Cost (studio-level tool spend)", "within NT$5,000 a month", "within NT$5,000 (NT$10,000 only if a tool clearly earns it)",
     "a persona-specific paid tool in the first 90 days (not allowed)", "studio spend above NT$10,000 in any month"),
    ("Revenue (studio-level, persona-tagged)", "at least one lead signal", "none required (year-1 platform payouts planned at NT$0)", "n/a",
     "never retires a persona alone"),
]


def effort_level(metric: str, value):
    """Return 'scale' | 'keep' | 'fix' | 'retire' | 'unknown' for an effort or rejection value."""
    if value is None:
        return "unknown"
    s, k, f = EFFORT_LEVELS[metric]
    if value <= s:
        return "scale"
    if value <= k:
        return "keep"
    if value <= f:
        return "fix"
    return "retire"
