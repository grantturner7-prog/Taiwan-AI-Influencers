# Weekly operating routine (Phase 9), DRAFT v0.1

Written 2026-10-12. For the operator (English); the wife's tasks are listed in the same tables. This is the week as the two of you run it inside **6 hours (operator) plus 10 hours (wife)**. It extends the posting rhythm in [launch/schedule.md](../launch/schedule.md) section 3 and the approval flow in [portfolio.md 5.5](../strategy/portfolio.md); it does not replace them. Companion files: [risk-register.md](risk-register.md) (what to watch) and [crisis-playbook.md](crisis-playbook.md) (what to do when something happens).

**Nothing here has been run.** No account exists, no post is approved, and every minute below is an *assumption* (from [portfolio.md 5.1 and 5.3](../strategy/portfolio.md) or this author's estimate) that the first four weeks of logging will replace. W0 = Monday 2026-11-16 is an assumption that moves with the launch gates ([launch README](../launch/README.md) decision D7); every date below moves with it by whole weeks. Dates and weekdays were computed with a script on 2026-10-12. Evidence labels: *assumption*, *unverified*, *computed*.

## 1. The short version

1. **One-week lead.** Posts for week N+1 are approved and scheduled on Thursday of week N. The first two batches are done before W0 ([schedule.md](../launch/schedule.md) section 8).
2. **Two keys, and every post, for at least 30 days.** The wife approves the Chinese, the operator approves facts, labels and flags, a human sets `approved: true`. Claude never does. Whether to relax this after day 30 is the user's decision and is not assumed.
3. **Removing needs one key; adding needs two.** Either of you may pause a persona or take a post down at once (playbook section 3).
4. **A daily five-minute notice check** (the wife, with the operator covering) is what makes the 24-hour take-down clocks possible. It is not in the capacity model.
5. **The week has fixed points:** Monday batch, Tuesday pre-check, Wednesday wife review, Thursday final approval and scheduling, Friday trend note and the 30-minute standup, Sunday analytics. Section 3 has the day table.
6. **The hours do not fit at 18 approvals a week once this routine's own overhead is counted** (section 2, *computed*). The proposal is to run at 12 approvals a week until logged minutes show room (decision OPS-D1).
7. **Never cut:** the AI labels, source slips, the wife's review, sponsorship disclosure, the 24-hour clocks, moderation of political drift, the daily notice check and the live check (section 12).

## 2. Hours: what the plan has, and what it leaves out

### 2.1 What [portfolio.md 5.3](../strategy/portfolio.md) models

| Operator line | Weeks 1 and 2 (12 approvals) | Weeks 3 to 8 (18 approvals) |
|---|---|---|
| Admin, brand and agency contact | 60 | 60 |
| Analytics and weekly report | 30 | 30 |
| Comment and DM review | 60 | 60 |
| Approvals, 5 minutes each | 60 | 90 |
| 步驟 extras, 20 minutes per master | 40 | 60 |
| **Planned load** | **250** | **300** |

The wife's planned load is 363 and 402 minutes (draft review 10 minutes per master, second-platform variants, moderation 90, image QA 45, B2B review 60, registrant duties 60, weekly sync 30). The gates are 324 (operator) and 510 (wife), averaged over four weeks ([portfolio.md 6.4](../strategy/portfolio.md)).

### 2.2 What the routine adds, and is not in 5.3

| Line | Who | Minutes a week | Where the figure comes from |
|---|---|---|---|
| Weekly standup (section 7) | Both | 30 each | 5.1 gives the wife a 30-minute weekly sync but gives the operator no matching line. **Reading A** charges his 30 to his admin line; **Reading B** charges it on top |
| Trend session (section 5) | Operator 10; wife 20 | 10 and 20 | The three persona trend-check files each say 30 minutes, but their step tables add up to about **69 operator and 21 wife minutes** a week if all three run as written (*computed* from the step times). Run once as a studio session it is 30 in total. The wife's 20 come out of her 90-minute moderation line, as those files say; the operator's 10 are new |
| Account-status look (section 8) | Operator | 10 | About 7 accounts at 1 to 2 minutes each (*assumption*) |
| Live check, 2 minutes per post | Operator | 24 at 12 posts; 36 at 18 | [schedule.md](../launch/schedule.md) section 3, which takes it from the reserve |
| Daily notice check, 5 minutes a day (section 8) | Wife | 35 | *Assumption* |
| Monthly bundle, averaged (section 9) | Operator about 21; wife about 14 | 21 and 14 | 90 and 60 minutes a month divided by 4.33 (*assumption*) |

### 2.3 The accounting (*computed*)

Operator, minutes a week against 360 available. The rework reserve [portfolio.md 5.1](../strategy/portfolio.md) assumed is 36.

| | Weeks 1 and 2, or held at 12 approvals | Weeks 3 to 8 at 18 approvals |
|---|---|---|
| Planned (5.3) | 250 | 300 |
| Trend session, operator share | 10 | 10 |
| Account-status look | 10 | 10 |
| Live checks | 24 | 36 |
| **Total, Reading A** (standup inside the admin line, leaving 30 minutes for B2B and registration admin) | **294** | **356** |
| Monthly bundle, averaged | 21 | 21 |
| **Total with monthly, Reading A** | **315** | **377** |
| Slack against 360 | **45** | **-17** |
| Total with monthly, Reading B (standup on top) | 345 | 407 |
| Slack against 360 | 15 | -47 |

Wife, minutes a week against 600 available (gate 510):

| | Weeks 1 and 2, or held at 12 | Weeks 3 to 8 at 18 |
|---|---|---|
| Planned (5.3) | 363 | 402 |
| Daily notice check | 35 | 35 |
| Monthly bundle, averaged | 14 | 14 |
| **Total** | **412** | **451** |
| Slack to the 510 gate | 98 | 59 |

### 2.4 What this means, and a proposal

* **The wife's load fits either way.** The operator's does not at 18 approvals: it is over by 17 minutes (Reading A) or 47 (Reading B) *before any rework or incident*, and the plan's 36-minute rework reserve fits only in Reading A at 12 approvals (45 minutes of slack). Set-up, the two review weeks and any incident come on top.
* **Proposal (decision OPS-D1, default yes): hold at 12 approvals a week (2 posts per platform per persona) after week 2, and use Reading A.** Reading A means B2B and registration admin gets 30 minutes a week from the start, which is cut #2 in [portfolio.md 5.6](../strategy/portfolio.md) applied early; revenue is priority 3 and the week-8 revenue checkpoint (at least 5 warm fashion contacts approached, 1 sample delivered, 3 quotes) is therefore at risk. Say so at the week-2 standup rather than discovering it at week 8.
* **Ramp rule (derived).** The step from 12 to 18 adds 6 approvals (30 minutes), one 步驟 master (20) and 12 live-check minutes: **62 minutes**. To land at or under the 324-minute gate, the real all-in operator total at 12 approvals must be **262 minutes or less** (324 minus 62), averaged over the last two logged weeks. At the assumed numbers it is 315, so the ramp happens only if real minutes come in well under the assumptions (for example 3 minutes an approval instead of 5). Decide it at the Friday 2026-11-20 standup, because the week-3 batch is drafted on Monday 2026-11-23 and approved on Thursday 2026-11-26. **Caveat (reviewer):** on that Friday only the pre-launch logs and four days of week 1 exist, so "the last two logged weeks" cannot be met and the ramp rule cannot honestly pass; the default at that standup is therefore hold at 12. The first date with two logged weeks is the Fri 2026-11-27 standup (week 1 complete, week 2 partial), which decides the week-4 batch drafted on Mon 2026-11-30 and approved on Thu 2026-12-03. If the ramp happens at all, it therefore starts at week 4, and weeks 3 to 6 then hold more than the 8 organic posts per platform the thresholds need.
* **Consequences to settle if OPS-D1 is accepted:** the calendars and [schedule.md](../launch/schedule.md) section 7 show three posts per platform from week 3; about 12 of the 66 slots in weeks 3 and 4 (two per persona per week) would be dropped (*computed* roughly), and `launch/schedule_check.py` and the calendars need their slots edited. At 2 posts a week, weeks 3 to 6 give exactly 8 organic posts per platform, the minimum sample for the thresholds ([portfolio.md 6.1](../strategy/portfolio.md)), so one skipped post extends the window to week 8.
* **Log real minutes from the first approval.** `analytics/templates/effort.csv` has the columns; the 2-minute habit per post is the cheapest data in the project.

## 3. The week, day by day

Steady state at 18 approvals; the 12-approval version is in the last row. Minutes are per person. The operator's live checks (2 minutes per post, 36 a week at 18) are spread across the days and are not in the day totals.

| Day | Operator | Wife | Claude (drafts only; never logs in or approves) |
|---|---|---|---|
| **Mon** | **30.** Comment and DM review 15 (hide, tally 「是真人嗎」, send approved replies). Admin 15 (registration, lawyer, B2B, contract follow-ups; read the standing-events log) | **35.** Moderation and tone of weekend comments 30. Notice check 5 | Drafts next week's batch from the calendar and Friday's trend note; scaffolds each with `queue.py new-draft`, fills it, runs `queue.py validate`; lists everything blocked (HOLD, PENDING media, `UNVERIFIED-OPERATOR-TO-FILL`) |
| **Tue** | **105.** Pre-check 45: open every source on the slips and record the date, recompute every number, media QA at 200% against R01, labels and flags. 步驟 recordings and claims check 60 | **35.** Registrant duties 30 (registration, 記帳士, lawyer). Notice check 5 | Fixes validation findings; prepares reply suggestions for the categories in the reply guidelines |
| **Wed** | **30.** Comments 15. Admin 15. Any rework after the wife's `changes` verdicts (regenerate, fix text with Claude) comes from the rework reserve, not from these minutes | **167.** **Review window**: draft review 90, second-platform variants 27, Chinese on every image 45, one verdict per draft with reason codes in `review.notes`. Notice check 5 | Applies text changes; re-runs `validate` |
| **Thu** | **45.** Final approval and scheduling: confirm `operator_facts`, a human sets `approved: true`, `queue.py approve <folder>` shows what is open, schedule with the official tool, label on by hand, log in `launch/schedule-log.csv` | **35.** Moderation 10. **Trend session 20** (section 5). Notice check 5 | Prepares the trend note draft from her notes |
| **Fri** | **55.** Comments 15. **Standup 30** (section 7). Trend note and decision 10 | **95.** B2B correspondence review 60. **Standup 30**. Notice check 5 | Drafts the weekly experiment from Sunday's report for the standup |
| **Sat** | **0** (live checks for weekend posts only) | **65.** Moderation 30. Registrant duties 30. Notice check 5 | |
| **Sun** | **55.** Comments 15. **Analytics and weekly report 30** (section 6). Account-status look 10 | **5.** Notice check only | Runs the weekly report on the imported data |
| **Total at 18** | **320 + 36 live = 356** | **437** | |
| **Total at 12** | **270 + 24 live = 294** (Tue 70, Thu 30) | **398** (Wed 128) | |

Checks on the arithmetic: the planned lines (admin 60 = Mon 15 + Wed 15 + Fri 30 [the standup]; comments 60 = Mon, Wed, Fri, Sun 15 each; approvals 90; 步驟 60; analytics 30) sum to 300, plus the trend share 10 and status look 10 makes 320, plus 36 live checks makes 356. The wife's moderation line is 90 = Mon 30 + Thu 10 + Sat 30 + trend session 20 on Thursday.

**Weeks 1 and 2.** Twelve approvals (6 masters). The first batch needs two weeks of lead because the golden set and the diagram kit must exist first. Set-up (accounts, dry runs, link pages, avatars) is not in these tables; [launch README](../launch/README.md) section 4 estimates it at about 11.8 operator hours.

## 4. The approvals flow

Source of truth: the folder in `pipeline/review-queue/<persona>/<date>_<NN>/` ([pipeline README](../pipeline/README.md) section 2). A platform scheduler holds a copy, never the record.

| # | Step | Who | What happens | Field or command |
|---|---|---|---|---|
| 1 | Draft | Claude | Script, caption, hashtags, flags, shot prompts, source slip; zero ERROR and FLAG | `queue.py new-draft`, `validate`; review fields `pending`, `pending`, `false` |
| 2 | Media | Operator | Generate in the app; log the same day; add badges and all Chinese in a design tool; set the media paths | `provenance.py add`; `qa-checklist.md` |
| 3 | Pre-check | Operator | Open each source, recompute, QA the media, record 步驟 | notes in the folder |
| 4 | Language review | Wife | Traditional Chinese, Taiwan vocabulary, tone, culture, taboos, every character on every image | `review.wife_language` approved or changes, reason codes V T S E R P D X C H |
| 5 | Facts | Operator | After the wife's fixes | `review.operator_facts` |
| 6 | Final approval | A human (by default the operator, who holds the approval duty under BRIEF Ground rule 9) | Only when both are approved, no media is PENDING and no HOLD or BLOCKED remains | `review.approved` true; `queue.py approve` reports and changes nothing |
| 7 | Schedule | Operator | Official tool; AI label on by hand; paid-partnership tool if sponsored; no location tag | `launch/schedule-log.csv` |
| 8 | Live check | Operator | The four disclosure places seen on the live post; screenshot kept outside the repo | schedule-log row |
| 9 | Learn | Operator | Numbers into the tracker; the wife's first-pass verdicts into the review log | section 6 |

Rules that keep it honest:

* **Any edit after approval resets approval.** Both review fields go back to `pending`, the scheduled copy is deleted from the platform, and the post goes through the week again ([schedule.md](../launch/schedule.md) section 2).
* **Nothing is scheduled to fill a gap.** An empty slot is fine; the floor is two posts a week per live persona.
* **A correction or statement in an incident** is a new draft with an expedited ten-minute review by both. Removing something needs no review (playbook section 3).
* **Replies to comments** are drafted by Claude from the reply guidelines, wording reviewed by whoever sends them, and sent by a person from the official app. The operator recomputes any reply that contains a number. No automated reply, no DM automation, no bulk replies. Two reply windows a week.
* **The 30-day minimum** counts from each persona's first post (Wed 2026-12-16 for 方寸 if W0 holds). It does not relax anything by itself; see section 10.

## 5. The weekly trend session (30 minutes, once for the studio)

This runs the three persona trend-check routines ([方寸](../content/fangcun/trend-check.md), [步驟](../content/buzhou/trend-check.md), [色環](../content/sehuan/trend-check.md)) as **one** session, split by language: the wife reads the Chinese pages; the operator reads the English tool pages. Their hard limits all apply: public pages read by hand; no scraping, no automation, no login-wall browsing as research; the persona accounts are not used to browse; no personal data in the note; nothing unverified without the label; nothing is ever used to seed engagement. A trend never overrides a pillar, and the default outcome is **no change** to next week's masters.

| Min | Who | Day | Step | Output |
|---|---|---|---|---|
| 3 | Wife | Thu | **Calendar and pause check:** the official holiday calendar page, the weather agency's (中央氣象署) public warnings, and the no-post lists of the three calendars | Pause switch on or off; days to avoid |
| 6 | Wife | Thu | **Search interest:** the public Google Trends page, Taiwan, past 7 and 30 days, the fixed term groups of the three routines (about 2 minutes each). Direction only | Up to 3 candidate terms per persona, no numbers |
| 7 | Wife | Thu | **Phrasing scan, one persona a week in rotation** (方寸, 步驟, 色環): public Dcard and Threads pages that open logged out; 2 or 3 phrases; flag dated, mainland-leaning or "brand trying too hard" wording in our drafts | Phrases; 0 to 3 flags |
| 4 | Wife | Thu | **Tone check** of next week's hooks for all three, against each hook library | Verdicts on hooks only |
| 7 | Operator | Fri | **步驟 release and ledger watch:** the public release notes and help articles of the tools in the next two weeks' drafts (English), against the re-check ledger | Ledger updates; stale flags; re-record candidates |
| 3 | Operator | Fri | **Studio trend note and decision:** NO CHANGE (default), swap one hook, or add one dated post | The note |

That is 20 wife minutes and 10 operator minutes. **Dropped from the weekly session** because it is covered elsewhere or moved to monthly: the own-insights glance (Sunday analytics), the viewer-question tally (the Monday and Wednesday comment review), the separate weather window (merged into the first step), the season and shopping hook (it is in each calendar's holiday check and the monthly look-ahead), and the platform policy watch (monthly, section 9).

**Where the note lives.** The persona routines file `content/<slug>/trend-notes/YYYY-Www.md`. To save three file operations a week this routine files **one** studio note with a block per persona at `ops/trend-notes/YYYY-Www.md` (the folder does not exist yet). Copy the persona templates' lines into each block; leave a line out when nothing changed. Switch back to the per-persona files if you prefer; nothing else depends on the location.

## 6. The weekly analytics review (30 minutes, Sunday, operator)

The steps and CSV rules are in [analytics README](../analytics/README.md) sections 4 and 5; this is only how it sits in the week.

1. Read the numbers from each platform's own insights for every post now 7 days old, plus each account's day-end followers and reach. Blank means the platform did not show it; type 0 only for a real zero.
2. Type them into the CSV templates; log the week's minutes (`effort.csv`) and first-pass review verdicts (`reviews.csv`); add new posts (`posts.csv` or `tracker.py import-queue`).
3. `python3 analytics/tracker.py import KIND FILE.csv` for each file; then `python3 analytics/dashboard.py` and `python3 analytics/weekly_report.py`.
4. Bring the report's single suggested experiment to the Friday standup. Accept or decline it there; never run two at once on a persona, and never on an account with an open standing event.
5. Add the week's count of 「是真人嗎」 comments, hidden-comment categories and any near-misses to the log (reply-guidelines section 10).

Reading rules (from the analytics README and [portfolio.md 6](../strategy/portfolio.md)): no decision from one week; the tree runs per account, not per persona; a restriction week is marked, not scored; **read every Instagram result with the label caveat** (risk PHO-2); thresholds are assumptions to be recalibrated against each persona's week-2 baseline before they are applied (section 10). The Sunday report is discussed at the Friday standup five days later; that is acceptable because anything urgent arrives through the daily notice check and the standing-events log, not through the weekly numbers.

## 7. The 30-minute standup (Friday, both of you)

By video call or in person, on time, notes kept in a running file `ops/standup-log.md` (create it at the first one; no viewer or claimant names). The first standup of each calendar month runs 50 minutes: the extra 20 are the register review (section 9).

| Min | Item | Questions |
|---|---|---|
| 0 to 3 | **Safety first** | Any open standing event or incident? Any 24-hour or 14-day clock running, and when does it end? Is the pause switch on? Any notice this week that the other has not seen? |
| 3 to 8 | **Last week in numbers** | One line per persona from Sunday's report; the 「是真人嗎」 tally (3 or 5 triggers); rejection rate; hidden-comment categories; minutes logged against the plan |
| 8 to 13 | **Pipeline** | What is blocked (HOLD, PENDING, unverified sources, `changes` verdicts)? What is in Thursday's batch? Anything that will not be ready? Who has the daily notice check next week? |
| 13 to 18 | **Calendar and trend note** | No-post days, dated hooks, the decision in the trend note, any swap |
| 18 to 22 | **Compliance watch** | Near-misses this week (experience, health, finance, politics, label); wording the wife wants on the word list; any policy change noticed; lawyer, registration or 記帳士 follow-ups |
| 22 to 26 | **Capacity and energy** | Each person's energy 1 to 5 for the next week (5 fine, 1 cannot keep up). Minutes against the gates. Is any cut from section 12 due? Absences coming up (section 11)? |
| 26 to 30 | **Decisions and actions** | At most three decisions, each with an owner and a date. Update `HUMAN_TODO.md` or `DECISIONS.md`. Log the standup's minutes |

Rules: safety before anything else; parking lot for anything that is not a decision; no discussion of a viewer by name; if you disagree on wording say nothing publicly until the next day; the more cautious action wins on safety (playbook section 3).

## 8. The daily notice check and the weekly status look

**Why.** The 24-hour clocks start when either of you first sees a problem. Without a daily look, "within 24 hours" is not a promise anyone can keep. It is five minutes a day (*assumption*), not in the capacity model, and it goes to the wife because platform notices for Taiwan accounts will mostly be in Traditional Chinese, which the operator reads poorly. The operator covers days she is away; agree who has it at each standup.

**The daily check (5 minutes, any time before evening).**

1. Open the **studio mailbox**: platform notices, comment and message notification digests, brand, agency, lawyer or agency (government) email.
2. Open the weather agency's public warnings page and one public news front page for a disaster, an earthquake or an announcement of national mourning (Scenario 7).
3. Is anything scheduled for today that should not go out?
4. Write one line in the running log: date, who, "nothing" or what you saw. If something is wrong: tell the other person now; pausing is allowed; open the playbook.

It does not log in to the persona accounts, reply to comments or approve anything.

**The weekly status look (10 minutes, Sunday, operator).** For each account (about 7), open its account-status or channel-health page in the app, note the AI-label state and any limit or warning, and screenshot it into the private evidence folder. The names of these pages are *unverified*; find them in the dry runs and write them here. This catches what is not emailed.

## 9. Monthly and quarterly tasks

The first-Friday session is the monthly one: Fri 2026-11-06 (a pre-launch readiness check), Fri 2026-12-04, then Fri 2027-01-08 because 2027-01-01 is New Year's Day. Later dates are set at the previous session. Minutes are *assumptions*; averaged over a month they are the 21 and 14 minutes in section 2.

| # | Task | Who | Minutes | Notes |
|---|---|---|---|---|
| M1 | **Platform and regulatory policy watch.** Reopen the policy pages listed in [platforms.md](../research/platforms.md) section 4 (Meta AI labels, the AI-generated profile label, branded content; YouTube altered or synthetic content and inauthentic content; Threads) and note any change with the date or "no change"; the Fair Trade Commission's and other agencies' announcements on AI advertising | Operator (English pages); Wife (Chinese announcements) | 15 and 10 | All URLs *unverified*. A change goes to the other person the same day (risks ACC-2, LEG-1) |
| M2 | **Cost check.** Update `COSTS.md` and `costs.csv`; compare provider console spend with the NT$5,000 base cap and confirm the hard limits are still set | Operator | 10 | Stop adding spend above the cap (BIZ-2) |
| M3 | **Provenance, drift and look-alike sample.** `provenance.py check`; the latest three finals of each persona beside R01 (the 4-week drift check); the monthly look-alike and age-read sample ([方寸 addendum](../personas/fangcun/photoreal-addendum.md) 9.1 and 9.3) | Operator 20; Wife 10 | 30 | Two of three failing a locked feature: regenerate from the golden set (PHO-8) |
| M4 | **Account security spot check** of the mailbox, vault and two-factor; full re-check each quarter | Operator | 10 | [00-studio-setup.md](../launch/00-studio-setup.md) section 5 |
| M5 | **Risk register review** inside the extended standup: re-score the top ten, add what incidents and near-misses showed, summarise incidents by category | Both | 20 | [risk-register.md](risk-register.md) section 5 |
| M6 | **Reviewer calibration.** The other person second-reads three approved posts; the wife's reason-code mix; rejection rate not drifting to zero (PPL-3) | Both | 10 each | |
| M7 | **Evidence housekeeping.** Evidence folder index and backup to a second place; `git status` check that nothing personal is in the repo | Operator | 5 | |
| M8 | **Six-week calendar look-ahead.** Official holiday calendar, no-post dates, dated hooks ([culture.md](../research/culture.md) 4), any date needing `schedule_check.py --no-post` | Wife | 10 | |

Operator total about 90 minutes a month and wife about 60. If a month is tight, skip M6 to M8 first and never skip M1, M2 or M3.

**Quarterly:** a full re-score of the register; the regulatory check ([legal.md](../research/legal.md) 10 item 10); the two-factor and recovery re-check ([00-studio-setup.md](../launch/00-studio-setup.md) section 5); the annual look-alike procedure; a reverse search of each published avatar for misuse (PHO-3); a review with the lawyer of anything the soft triggers collected (playbook section 5).

## 10. Milestones and the two reviews

W0 = Mon 2026-11-16; the three pilots start on different days ([schedule.md](../launch/schedule.md) section 7), so each has its own dates. Day 0 is the first post. Everything shifts by whole weeks if W0 does.

| Milestone | 方寸 (Mon 2026-11-16) | 色環 (Wed 2026-11-18) | 步驟 (Thu 2026-11-19) | Use this date |
|---|---|---|---|---|
| **Ramp decision** for the week-3 batch (section 2.4) | | | | Fri 2026-11-20 standup |
| **Baseline calibration** (week-2 posts need 7 days to mature, so this happens in week 3) | | | | Fri 2026-12-04 |
| **Day 30** (minimum per-post approval period met; nothing relaxes by itself) | Wed 2026-12-16 | Fri 2026-12-18 | Sat 2026-12-19 | |
| **Week-6 review** (day 42) | Mon 2026-12-28 | Wed 2026-12-30 | Thu 2026-12-31 | Thu 2026-12-31, or the first weekend after (Sat 2027-01-02) |
| **Fix experiments end** (4 weeks after the week-6 review) | Mon 2027-01-25 | Wed 2027-01-27 | Thu 2027-01-28 | |
| **Week-8 review** (day 56) | Mon 2027-01-11 | Wed 2027-01-13 | Thu 2027-01-14 | Thu 2027-01-14 |
| **Wave 2 earliest** ([portfolio.md 2.5](../strategy/portfolio.md)) | | | | Mon 2027-01-18 |

Notes: [portfolio.md](../strategy/portfolio.md) labels the reviews 2026-12-28 and 2027-01-11 using W0 alone; the pilots' own day-42 and day-56 dates run up to three days later, and the analytics window is defined from each persona's first published post, so hold the session after the last pilot's window closes. **Wave 2 on 2027-01-18 leaves almost no lead time:** under the one-week lead its first posts would need approval by Thursday 2027-01-14, the day of the week-8 review (*computed*). Treat 2027-01-18 as the earliest possible date, not the plan.

### 10.1 Baseline calibration (Fri 2026-12-04, after the 50-minute first-Friday session, about 30 minutes more; that Friday runs about 80 minutes, a one-off not in section 2)

[portfolio.md 6](../strategy/portfolio.md) says every threshold is recalibrated against each persona's own week-2 baseline before it is first applied. Read the medians of the week-1 and week-2 posts per account, compare them with the thresholds in `analytics/thresholds.py`, and decide with Claude which, if any, to change. Record each change with its reason in [DECISIONS.md](../DECISIONS.md). Do not move a threshold to rescue a result; move it only because the benchmark it came from was not Taiwan data.

### 10.2 Week-6 review (about 75 minutes, both; the extra 45 minutes are the one planned overtime of the test, paid for by dropping that week's admin)

**Pre-read** (operator, prepared the day before the session from the latest data): dashboard, weekly report, all CSVs complete, effort and review logs, standing log, comment log, costs, lead signals, the evidence log, the register.

1. **Gate check:** any open standing event (portfolio.md 6.3 step 1). An open event means PAUSE, not score.
2. **Sample size:** 8 organic posts per platform in weeks 3 to 6; otherwise extend to week 8.
3. **Each account through the tree** ([portfolio.md 6.3](../strategy/portfolio.md), run per account by the tracker): scale-eligible, keep, fix, retire-review or pause. Confirm or overrule the tracker's reading choices ([analytics README](../analytics/README.md) section 8), and write down any you overrule and why. **Ask first whether an Instagram label or limit applied (PHO-2).**
4. **Effort and capacity:** operator minutes per approval, 步驟 recording minutes, wife minutes per master, rejection rate, and the capacity check (324 and 510 averaged over four weeks) with this routine's lines included. Revise the plan from real minutes.
5. **The hypotheses H1 to H9** ([portfolio.md 4.2](../strategy/portfolio.md)): proved, killed or open. For H1 and H9 read the 「是真人嗎」 and "looks fake" tallies and the engagement of labelled posts; this is the evidence for the photoreal decision and the fallback triggers (decision OPS-D5).
6. **Audience overlap** for the same-platform pair (方寸 and 色環 on Instagram): the age and gender panels; if the top two cells match, read public commenters by hand (public pages only).
7. **Voice distinctness:** the wife reads three unlabelled lines from each live persona and says whether she can tell them apart ([personas/README.md](../personas/README.md) section 6).
8. **Incidents and near-misses:** each root cause, each control changed, any second event inside 8 weeks.
9. **Money:** spend against the cap; revenue received; lead signals; progress on the studio revenue checkpoint.
10. **Register:** re-score the top ten.
11. **Decide and record:** per account the status, and for any Fix, one variable for four weeks with the decision rule written before the data (the weekly report proposes it). Write it in [DECISIONS.md](../DECISIONS.md) and the experiments log.

### 10.3 Week-8 review (about 60 minutes, both)

1. **Fix experiments in flight** (they end at week 10): which accounts are at Keep now.
2. **The wave gate** ([portfolio.md 6.4](../strategy/portfolio.md)): at least 2 of the 3 pilots at Keep or better; no safety incident open; registration complete and the reviewer trial passed; the capacity check; the wave-specific gates in 2.5. Otherwise extend the pilots 4 weeks or swap; do not add. Wave 2 has only two personas, so one miss blocks wave 3; the fallback is undecided ([personas/README.md](../personas/README.md) section 7 item 1).
3. **The studio revenue checkpoint (by week 8):** at least 5 warm fashion contacts approached, at least 1 free scoped sample delivered, at least 3 written rate quotes, affiliate and LINE Creators Market terms screenshotted. Within six months: at least one written quote or accepted sample, otherwise treat B2B as unproven and hold spend at NT$5,000 a month or below.
4. **Per-post approval.** The user decides whether to relax it; it is not assumed. If raised, the evidence to look at is: no open standing event; at most one published error in the last six weeks; fewer than 3 of 20 drafts caught; every live check clean for four weeks. The wife's review and the AI labels stay on the never-cut list whatever is decided.
5. **The photoreal decision checkpoint:** read PHO-1, PHO-2 and PHO-4 against the fallback triggers (HUMAN_TODO 32). The two looks are never mixed on one account.
6. **Hours:** the logged minutes against section 2; set the cadence for the next eight weeks.
7. **Register and decisions:** re-score; record in DECISIONS.md.

## 11. Absence and holiday rules

1. **Nothing is scheduled to publish in a window when neither of you can open the studio mailbox and the accounts within 24 hours.** The take-down clocks cannot be met otherwise.
2. **Planned absence of either person for three days or more:** say so at the standup before it; the other takes the daily check and the weekly status look. Hand over any pending item in the standup notes.
3. **If the wife is away:** no new `wife_language` approvals, so no new posts beyond what is already two-key approved; the operator keeps the existing schedule within its approved horizon, hides but does not answer comments, and takes the daily check. If a Chinese notice arrives he may paste its text (not a screenshot of a settings page), with personal details such as emails, phone numbers and viewer names removed first (PDPA and cross-border transfer, *unverified*, risk LEG-5), into Claude for a gloss, and treats the gloss as a machine reading, not as the notice itself.
4. **If the operator is away:** no final approvals and no new scheduling; the wife may publish an already-approved post by hand ([schedule.md](../launch/schedule.md) section 5), may pause or take down, and holds the daily check.
5. **Both away, or either seriously unwell:** the pause switch is on (unschedule everything).
6. **Holidays:** plan the quiet days in the calendars (農曆新年 is 2027-02-06, with 除夕 on 2027-02-05; 228 is 2027-02-28; the official 2027 holiday calendar is *unverified* and must be read, HUMAN_TODO 29). Before any holiday week of three or more days, either schedule only two-key-approved posts with a named person holding the check, or pause.
7. **Spare evergreen posts** (decision OPS-D6, optional): a few approved posts whose facts do not date (arithmetic, method posts). Re-check any dated source before use.

## 12. What to cut first if hours slip

[portfolio.md 5.6](../strategy/portfolio.md) is the base order (revenue is priority 3, so it is cut before posting; safety is never cut). This extends it with the routine's own lines (marked *added*).

| Order | Cut | Saves (*assumption*) |
|---|---|---|
| 0 | **Stop adding:** no new wave, platform, series, experiment or tool | |
| 1 | Pause any pending wave launch (5.6 #1) | |
| 2 | Weekly report to a monthly deep-dive; keep only the data entry (5.6 #2) | about 15 operator |
| 3 | B2B outreach and admin from 60 to 30 (5.6 #2). Under Reading A this is already the base | 30 operator |
| 4 | *Added:* the 步驟 release watch and the phrasing scan every second week; keep the weekly calendar and pause check | 7 operator, 7 wife |
| 5 | *Added:* the standup to 20 minutes (safety, numbers, decisions only); defer M6 to M8 | 10 each |
| 6 | Each pilot's third weekly post on its weaker platform (5.6 #3). **This is the base if OPS-D1 is accepted** | about 62 operator |
| 7 | Drop the weaker platform of the weakest pilot (5.6 #4) | |
| 8 | Move the weakest persona to 2 posts a week on one platform (5.6 #5) | |
| 9 | Pause, never delete, the lowest-ranked persona (5.6 #6) | |

**Never cut:** the AI labels and the live check of the four places; source slips; the wife's review; sponsorship disclosure; the 24-hour clocks and the daily notice check that serves them; moderation of political drift; evidence capture.

**What starts a cut** (so it is not a feeling): the operator's all-in logged total over 360 in any week or over 324 two weeks running; the wife's over 510 two weeks running; any 24-hour clock missed; an energy score of 1 or 2 from either person two weeks running, or both at 3 or below; a published error whose root cause is "we were rushed". Apply the next row **that week**.

## 13. The time and energy log

* **Per approval and per master:** minutes, into `analytics/templates/effort.csv` (task `approval`, `n7_recording`, `master_review`, `moderation`, `admin`, `analytics`, `other`). Add `ops` as an `other` row with a note for the standup, trend session, status look, live checks and daily check, so the real cost of this routine shows up (these tasks have no category of their own).
* **Per incident:** minutes for each of you in the incident note (playbook section 10.1); incidents are not in the plan.
* **Energy:** one line per standup, two numbers.
* **Reviews:** the week-6 and week-8 reviews read this log first.

## 14. Open items and what was not checked

1. **Decide OPS-D1** (hold at 12 approvals) before the week-3 batch is drafted; it changes the calendars and the schedule table.
2. **Name who has the daily notice check** and the cover, at the first standup.
3. **Find the real names of the account-status pages and the unschedule lists** in the dry runs and write them in sections 8 and the playbook.
4. **Every minute is an assumption.** The routine is untested; the first four weeks of logs replace the numbers in section 2.
5. **Unverified platform behaviour:** native scheduling, label settings in the schedule path, edit limits, comment controls, the Google Trends, Dcard and Threads pages, the official holiday calendar. All depend on the dry runs and the first trend sessions.
6. **The new overhead is not in [portfolio.md 5.3](../strategy/portfolio.md) or [launch/schedule.md](../launch/schedule.md).** If OPS-D1 is accepted, those two files and `schedule_check.py` should be updated by their owners.
7. **The week-6 and week-8 sessions are overtime of about 45 and 30 minutes each** (*assumption*) that the capacity model does not contain, and so is the one-off baseline calibration of about 30 extra minutes on Fri 2026-12-04 (section 10.1).
