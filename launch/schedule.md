# Posting schedule and scheduler setup, for the three pilots (DRAFT v0.1, 2026-10-12)

For the operator. **Nothing is scheduled, nothing is approved, no account exists.** This file says how posts get from the review queue to the platforms using only official tools, in what weekly rhythm, and what stops a post from going out. Tool names, menus and limits are recalled and **UNVERIFIED** (the research session could not open a primary page: `research/platforms.md` section 0); the one-time dry run in section 4 settles them on the real screens. Every zh-TW string is an AI draft for the wife. W0 = Mon 2026-11-16 is an assumption that moves with the gates (`strategy/portfolio.md` 2.5).

Sources: `strategy/portfolio.md` 5.1 to 5.6 (hours, weekly rhythm, what to cut), 3.3 (studio rules), 6.2 (standing incidents); the three `content/<slug>/calendar-30d.md` files (slots), `pipeline/README.md` and `pipeline/scripts/queue.py` (review fields); `research/platforms.md` 4 (platform rules). The slot table in section 7 is produced and checked by `launch/schedule_check.py`.

## 1. Short version

1. **Approval gate:** nothing is scheduled, queued or saved with a time until the draft's two review fields are both `approved` and a human has set `approved: true` (section 2).
2. **Tools:** Instagram's own scheduler (or Meta Business Suite), Threads' own scheduler if it exists, YouTube Studio's schedule option. All official, all free. No third-party scheduler, no automation, no scraping (Ground rule 9). Whether each one can carry the AI label is checked once, in a dry run (section 4). If a scheduler cannot set the label, that post is published **by hand** (section 5).
3. **Rhythm:** a one-week lead. Monday the batch is ready, Tuesday the operator pre-checks, Wednesday the wife reviews, Thursday the operator gives final approval and schedules the *following* week (section 3). That uses 300 of the operator's 360 minutes and 402 of the wife's 600 in steady state (*computed* from `portfolio.md` 5.3).
4. **Pause switch:** either of you can unschedule everything in about ten minutes (section 6). Both must agree to resume.

## 2. The approval gate

A post may be scheduled, queued, saved as a timed draft, or published **only if every row below is true**. The gate applies to every post for at least the first 30 days; relaxing it after day 30 is the user's decision and is not assumed (`portfolio.md` 5.4).

| # | Condition | Who sets or checks it | Where |
|---|---|---|---|
| 1 | `review.wife_language` is `approved` | The wife, by editing the file | `pipeline/review-queue/<persona>/<date>_<NN>/post.json` |
| 2 | `review.operator_facts` is `approved` | The operator | same file |
| 3 | `review.approved` is `true`, set **after** 1 and 2 | A human. Claude never sets any review field | same file |
| 4 | No media is `PENDING`: every `media[].path` is a real file with a row in `assets/provenance.csv`, the badge 「AI 生成｜…」 is on every image and frame, and the QA checklist was run | Operator, wife | `pipeline/qa-checklist.md` |
| 5 | No `HOLD` or `BLOCKED` in `review.notes`, no `{待填}` on any image, no `UNVERIFIED-OPERATOR-TO-FILL` in `sources` | Operator | the same file |
| 6 | `python3 pipeline/scripts/queue.py validate <folder>` shows 0 ERROR and 0 FLAG | Operator (Claude pre-screens) | terminal |
| 7 | Every gate in `personas/<slug>.md` section 7 that applies to the post is closed (A1 to A13, and A14 to A16 where they exist) | Operator | those files |
| 8 | The date is not a no-post date and no other persona posts within 60 minutes (section 6, 7) | `schedule_check.py` | terminal |

`python3 launch/schedule_check.py --list` prints `SCHEDULABLE` for a post only when rows 1 to 3 hold and no media is `PENDING` and no HOLD or BLOCKED note remains (the parts of rows 4 and 5 it can see); rows 6 to 8 are still yours to check. It **reads** the files and never changes them. `python3 pipeline/scripts/queue.py approve <folder>` prints what is still open and also changes nothing.

**State today (2026-10-12), from `schedule_check.py`:** 66 slots in the 30 days; 21 have a draft (方寸 5, 步驟 8, 色環 8) in the review queue; **0 are SCHEDULABLE**. Every draft has both review fields `pending`; most media is `PENDING`; several carry a HOLD or BLOCKED note (still faces inside video; the official 坪 definition; the weather page; the size-term source).

**Rules that keep the gate honest**

* **A platform scheduler holds a copy, never the record.** The folder in the review queue stays the source of truth.
* **Any edit after approval resets approval.** If the caption, hashtags, media, label, sources or date change, the editor sets both review fields back to `pending`, the scheduled copy is deleted from the platform, and the post goes through the weekly rhythm again. A stale scheduled copy is a way to publish an unreviewed post.
* **Nothing is scheduled to fill a gap.** An empty slot is fine (the floor is two posts a week per live persona, `portfolio.md` 5.4). Do not publish an unapproved post to keep a slot.
* **Log every scheduling action** in `launch/schedule-log.csv` (empty today): the post id, platform, time, who, method, whether the AI label was set, and the later live check.
* Sponsored, gifted or affiliate posts are not possible in the first 30 days (business not registered, lawyer unanswered). When they are, they are published from the app so the paid-partnership label is set (`platform-checklists.md` S2).

## 3. Weekly rhythm that fits 6 + 10 hours

One idea (a "master") feeds one post on each of a persona's two platforms: production counts once and approvals count twice (`portfolio.md` 5.1). Approvals per week: 12 in weeks 1 and 2 (2 posts per platform per persona), 18 from week 3 (3 per platform), against a planning ceiling of 22. **A one-week lead:** posts for week N+1 are approved and scheduled on Thursday of week N. The first batch needs two weeks (the golden set and the diagram kit must exist first, `calendar-30d.md` of each pilot).

| Day | Operator (minutes, steady state) | Wife (minutes, steady state) | What happens |
|---|---|---|---|
| Mon | 35 (comments 15, admin and brand contact 20) | 30 (comment moderation and tone) | Claude has the next week's batch ready: script, caption, hashtags, shot prompts, flags, source slips. Comments reviewed |
| Tue | 105 (pre-check 45; 步驟 recordings and claims check 60) | 30 (registrant duties: registration, 記帳士, lawyer) | Operator pre-check: facts against the source slips, media QA (hands, faces, text), labels |
| Wed | 35 (comments 15, admin 20) | 162 (draft review 90, second-platform variants 27, zh-TW QA of images 45) | **Wife's review window:** Traditional Chinese, Taiwan vocabulary, tone, taboos, every character on every image. Verdict per draft in `review.notes` with reason codes |
| Thu | 45 (final approval and scheduling of next week's batch) | 30 (comment moderation) | Operator sets `operator_facts`, then `approved`, then schedules or queues by hand (sections 4 and 5). Logs it |
| Fri | 35 (comments 15, admin 20) | 90 (B2B correspondence review 60, weekly sync and time log 30) | Claude's Friday trend check is ready (`content/<slug>/trend-check.md`) |
| Sat | 0 | 60 (comment moderation 30, registrant duties 30) | Posts go out; live checks come from the reserve |
| Sun | 45 (weekly report 30, comments 15) | 0 | Weekly report: what worked, what did not, one experiment |
| **Total** | **300 of 360** | **402 of 600** | Operator reserve 60 minutes (rework 36 plus 24 slack); the live checks below come out of it |

Weeks 1 and 2 (12 approvals, 6 masters): operator 250 (Tue 70, Thu 30), wife 363 (Wed 123). Both totals are *computed* by `schedule_check.py` from the `portfolio.md` assumption chain and agree with `portfolio.md` 5.3. The gates are 324 (operator) and 510 (wife) averaged over four weeks.

* **Minutes are assumptions** (5 minutes per approval, 10 per master for the wife, 20 for each 步驟 master). Log real minutes from week 1 and re-plan at week 3 (`portfolio.md` 5.4).
* **Setup is extra:** account creation, link-page deployment, the dry runs and the label check are not in these 300 minutes; `README.md` section 4 estimates them.
* **The live check after each publication** (about 2 minutes per post, assumption; 18 posts is about 36 minutes a week; section 9) comes out of the 60-minute reserve, which leaves only about 24 minutes for rework against the 36 the plan assumed. That is tight. If the reserve is used up, say so and re-plan; do not skip the check.
* **What to cut first if hours slip** is `portfolio.md` 5.6: pause new waves, cut B2B admin to 30 minutes, drop the third weekly post on the weaker platform. Never cut the AI labels, the source slips, the wife's review, the sponsorship disclosure, the 24-hour take-down rule or the moderation of political drift.

## 4. How each platform is scheduled, and the one-time dry run

| Platform | Official tool (all UNVERIFIED) | Can it set the AI label? | If not |
|---|---|---|---|
| Instagram (feed, carousel, Reel) | The Instagram app's own "schedule this post" for professional accounts (recalled; horizon recalled as about 75 days, plan 14 days ahead at most). Alternative: Meta Business Suite's planner (an official Meta tool; whether it needs a Facebook Page for an Instagram-only account is unverified) | Unknown. The dry run decides | Publish by hand from the app (section 5) |
| Threads | **Native scheduling: label UNVERIFIED.** The research found Threads and Business Suite scheduling reported inconsistently (S58, low confidence); one recollection is a scheduling option in Threads on the web. Check in the app | Unknown | Publish by hand. Threads is text-first and short, so by hand is cheap |
| YouTube Shorts | YouTube Studio: upload, then visibility, then "Schedule" with a date and time (long established, still unverified here). The altered or synthetic content answer and the paid-promotion box are in the same upload form and must be set **before** scheduling | Yes in principle: the question is part of the upload form | n/a |
| Any third-party scheduler | **Not used in the pilot.** One would qualify only if it posts through the official API (Instagram content publishing is rate-limited; Threads API too; YouTube uploads from an unaudited API project may be locked private: S36, S38, S45), sets the AI label, and (for a sponsored post) the paid-partnership label, which Meta says is applied in the app (S32). No tool is recommended or priced; any paid tool is a decision and a `COSTS.md` line | Not checked | n/a |
| Automation | **Never:** no browser or phone automation, macro or screen-driving tool, no unofficial endpoint, no scraping behind a login, no auto-reply (Ground rule 9) | n/a | n/a |

**The dry run, once per platform per account, in the real account, without scheduling or publishing anything.** It is part of the account set-up (`platform-checklists.md` A.4, B.2, C.4) and is also logged here.

1. Open the platform's scheduling flow with a plain test image or clip **you** made (a solid-colour square; no persona image, no real post) and the caption 「測試」. Set a time. **Stop before confirming.**
2. In the flow, find the AI label control and the paid-partnership control. Screenshot each, with the date. Note whether they appear in the *schedule* path or only in the *post now* path.
3. Back out and delete any draft the app saved. Nothing is scheduled; the approval gate is untouched.
4. Write the result in `evidence-log.csv` and set the method for that platform: **native scheduler** (label settable in the schedule path) or **manual** (it is not, or you cannot tell).
5. After the **first real approved post** is scheduled, reopen it from the scheduled list and confirm the caption, media, label and time survived. After it publishes, run the live check (section 9). If the label did not carry, the method for that platform becomes manual from then on, and the post is fixed within 24 hours (`portfolio.md` 6.2: disclosure failure).

Taiwan time (UTC+8) is the only time zone used. Check the platform's time-zone setting once, because a scheduler set to another zone publishes at the wrong hour.

## 5. Manual fallback (and the default for any post a scheduler cannot label)

A publish card per post, done by the operator at the slot (or the wife, if she is the one at hand; she may publish only an approved post and logs it the same way):

1. Open the approved folder. Confirm `review.approved` is `true` and the file is unchanged since approval (no edit after approval; section 2).
2. Open the platform's app on the phone that holds the account. Create the post: attach the final media files in the order of the `media` list; paste `caption_zh` exactly; paste the hashtags; add the alt text (`personas/<slug>.md` section 3.3).
3. Set the **platform AI label** and, for a sponsored post, the **paid-partnership tool**; set no location tag; do not add any tag or mention of another persona.
4. Publish (or, for YouTube, schedule through the form).
5. Run the live check (section 9) and log it in `schedule-log.csv`.

**If you miss the slot:** publishing within the same day is acceptable. If you cannot publish that day, skip it and tell Claude; do not move it onto a no-post date or into another persona's clock hour, and never publish several missed posts in one burst (a burst of posts is also a pattern the platforms' spam rules may read as inauthentic; unverified). A skipped post goes back through the weekly rhythm if it is still relevant. The busiest day in the pilots is Thursday with four slots (08:15, 12:30, 18:00 and 21:00); native scheduling takes that to zero touches, manual takes it to four.

## 6. Pause switch, no-post dates and how to unschedule

**Either of you may pause; both must agree to resume.**

| Trigger | Action |
|---|---|
| A typhoon day or a disaster in the news; a public tragedy | Unschedule everything that publishes today and tomorrow (`portfolio.md` 5.5). On such a day check the lists at 07:30, before the first slot (步驟's Threads posts are at 08:15) |
| A platform strike, restriction, label dispute or AI-label violation | Pause that persona on that platform at once; no replacement account ever; a restriction not cleared in 14 days stops that persona on that platform (`portfolio.md` 6.2) |
| A Ground rule 6 contact, a likeness complaint, a disclosure failure (any standing incident, `portfolio.md` 6.2) | Take the post down within 24 hours; pause the persona as the table there says |
| A post found to breach any rule after it was scheduled | Delete the scheduled copy; reset the draft's review fields to `pending` |
| Polling day (recalled **Sat 2026-11-28, unverified**) and 228 (2027-02-28) | **No post and nothing scheduled** (`portfolio.md` 2.5, `calendar-30d.md` of each pilot). Confirm the election date with the Central Election Commission before scheduling anything in weeks 1 and 2 |

**Where to look to unschedule (UNVERIFIED; find the real lists during the dry run and screenshot them):** Instagram's scheduled-content list (in the app or in Meta Business Suite if you used it); Threads' scheduled posts (if the app has them); YouTube Studio, Content, the Scheduled filter, then set each video to private or delete the schedule. Delete or move the item; do not leave a paused schedule "to publish later". Count the items before and after. Time it once during the dry run: about ten minutes is the planning figure (assumption). Then write in the log what was paused, why and by whom.

**To resume:** re-check each paused post against the gate in section 2 (a pause is a reason to look again, not a reason to skip a check), then reschedule by whole days only where the calendar rules allow, and re-run `schedule_check.py` with the new dates.

## 7. The 30 days, merged (W0 = Mon 2026-11-16)

Produced by `python3 launch/schedule_check.py --grid` from the slots in the three calendars. Times are Taiwan time. IG = Instagram, YT Short = YouTube Shorts. P01 and so on are each calendar's own post ids (方寸 and 色環 both have a P01, in separate columns); T and S are 步驟's Threads post and Short. **These are slots, not approvals.**

**Week 1: Mon 2026-11-16 to Sun 2026-11-22**

| Day | Date | 方寸 | 步驟 | 色環 | Note |
|---|---|---|---|---|---|
| Mon | 2026-11-16 | 12:30 IG P01 |  |  |  |
| Tue | 2026-11-17 | 19:30 YT Short P02 |  |  |  |
| Wed | 2026-11-18 |  |  | 20:30 IG P01 |  |
| Thu | 2026-11-19 | 12:30 IG P03 | 08:15 Threads T1<br>21:00 YT Short S1 | 18:00 Threads P02 |  |
| Fri | 2026-11-20 | 19:30 YT Short P04 |  | 20:30 IG P03 |  |
| Sat | 2026-11-21 |  |  | 18:00 Threads P04 |  |
| Sun | 2026-11-22 |  | 08:15 Threads T2<br>21:00 YT Short S2 |  |  |

**Week 2: Mon 2026-11-23 to Sun 2026-11-29**

| Day | Date | 方寸 | 步驟 | 色環 | Note |
|---|---|---|---|---|---|
| Mon | 2026-11-23 | 12:30 IG P05 |  | 20:30 IG P05 |  |
| Tue | 2026-11-24 | 19:30 YT Short P06 |  | 18:00 Threads P06 |  |
| Wed | 2026-11-25 |  |  | 20:30 IG P07 | 統一發票 draw (方寸 posts no content) |
| Thu | 2026-11-26 | 12:30 IG P07 | 08:15 Threads T3<br>21:00 YT Short S3 | 18:00 Threads P08 |  |
| Fri | 2026-11-27 | 19:30 YT Short P08 |  |  | Black Friday: no sale wording |
| Sat | 2026-11-28 |  |  |  | NO POST: recalled polling day, unverified |
| Sun | 2026-11-29 |  | 08:15 Threads T4<br>21:00 YT Short S4 |  |  |

**Week 3: Mon 2026-11-30 to Sun 2026-12-06**

| Day | Date | 方寸 | 步驟 | 色環 | Note |
|---|---|---|---|---|---|
| Mon | 2026-11-30 | 12:30 IG P09 |  | 20:30 IG P09 |  |
| Tue | 2026-12-01 | 19:30 YT Short P10 | 08:15 Threads T5<br>21:00 YT Short S5 | 18:00 Threads P10 |  |
| Wed | 2026-12-02 |  |  | 20:30 IG P11 |  |
| Thu | 2026-12-03 | 12:30 IG P11 | 08:15 Threads T6<br>21:00 YT Short S6 | 18:00 Threads P12 |  |
| Fri | 2026-12-04 | 19:30 YT Short P12 |  | 20:30 IG P13 |  |
| Sat | 2026-12-05 | 10:30 IG P13 |  | 18:00 Threads P14 |  |
| Sun | 2026-12-06 | 19:30 YT Short P14 | 08:15 Threads T7<br>21:00 YT Short S7 |  |  |

**Week 4: Mon 2026-12-07 to Sun 2026-12-13**

| Day | Date | 方寸 | 步驟 | 色環 | Note |
|---|---|---|---|---|---|
| Mon | 2026-12-07 | 12:30 IG P15 |  | 20:30 IG P15 |  |
| Tue | 2026-12-08 | 19:30 YT Short P16 | 08:15 Threads T8<br>21:00 YT Short S8 | 18:00 Threads P16 |  |
| Wed | 2026-12-09 |  |  | 20:30 IG P17 |  |
| Thu | 2026-12-10 | 12:30 IG P17 | 08:15 Threads T9<br>21:00 YT Short S9 | 18:00 Threads P18 |  |
| Fri | 2026-12-11 | 19:30 YT Short P18 |  | 20:30 IG P19 |  |
| Sat | 2026-12-12 | 10:30 IG P19 |  | 18:00 Threads P20 | 雙12: no price, discount or sale wording |
| Sun | 2026-12-13 | 19:30 YT Short P20 | 08:15 Threads T10<br>21:00 YT Short S10 |  |  |

**Week 5: Mon 2026-12-14 to Sun 2026-12-20**

| Day | Date | 方寸 | 步驟 | 色環 | Note |
|---|---|---|---|---|---|
| Mon | 2026-12-14 | 12:30 IG P21 |  | 20:30 IG P21 |  |
| Tue | 2026-12-15 | 19:30 YT Short P22 | 08:15 Threads T11<br>21:00 YT Short S11 | 18:00 Threads P22 |  |

**Totals:** 66 slots (22 per persona): 12 approvals in each of weeks 1 and 2, 18 in each of weeks 3 and 4, 6 in the part of week 5. The closest two personas are 60 minutes apart (Fri 2026-11-20, 方寸 Short 19:30 and 色環 Instagram 20:30); no two personas share a clock hour on any date (`schedule_check.py` checks every date).

**What was reconciled, and what is left for you** (the three calendars were written in parallel):

| # | Point | Result |
|---|---|---|
| 1 | Launch days | 方寸 Mon 11-16, 色環 Wed 11-18, 步驟 Thu 11-19: three different days, no coordinated launch (`portfolio.md` 3.3 item 6) |
| 2 | Clock hours | At least 60 minutes between any two personas' posts, checked by script. 步驟 owns 08:15 and 21:00; 方寸 12:30, 19:30 and (Saturdays) 10:30; 色環 18:00 and 20:30 |
| 3 | Same-day pairs on YouTube | On Tue 12-01, 12-08 and 12-15 and Sun 12-06 and 12-13 a 方寸 Short (19:30) and a 步驟 Short (21:00) go out 90 minutes apart on two different channels. Allowed by the studio rule; it is also the evening peak for both |
| 4 | Thursday | Four posts across three personas: 步驟 Threads 08:15, 方寸 Instagram 12:30, 色環 Threads 18:00, 步驟 Short 21:00 |
| 5 | **Decision D5: the quiet block** | 色環's calendar keeps Fri 11-27 to Sun 11-29 quiet around the recalled polling day. 方寸 has a Short on Fri 11-27 19:30 (P08), and 步驟 has posts on Sun 11-29 (T4 08:15, S4 21:00). `portfolio.md` bars only the polling day itself. **Recommendation:** keep them as written (each calendar already applies its own precautions: no sale wording on Black Friday, a neutral topic the day after) and hide political comments; or choose the stricter reading and unschedule those three, which saves moderation time that weekend. Your call (`README.md` section 5) |
| 6 | 雙12 (Sat 2026-12-12, computed) | 方寸 and 色環 post as normal with no price, discount or sale wording; 步驟 posts nothing that day. Different judgements, both inside the rules |
| 7 | Review-queue dates | The queue folders are named by date. If W0 moves, ask Claude to re-date the drafts: `python3 launch/schedule_check.py --w0 <new Monday>` shows the new dates, and the folders and `scheduled_date` fields must follow |

## 8. Countdown to W0 (all dates move with W0; the order does not)

| When (W0 = 2026-11-16) | What must be true | Who |
|---|---|---|
| Today, Mon 2026-10-12 | Nothing exists. Names, handles, the avatar, the mailbox, the licence terms and the label check are all open (`README.md` section 3) | |
| By Mon 2026-10-26 | Wife's reading test; TIPO and 經濟部 searches; handle checks (A1 to A3) | Wife, operator |
| By Mon 2026-11-02 | Avatars approved with the age-guess, look-alike and near-pair tests; licence terms recorded; mailbox, vault and two-factor decided; every string approved by the wife (A4 to A7) | Operator, wife |
| Mon 2026-11-02 to Wed 2026-11-04 | Accounts created, dry runs done, label check done (`personas/<slug>.md` section 8) | Operator |
| Mon 2026-11-02 | Batch 1 (the posts of week 1) is ready; this is a week early because of the first-batch rule | Claude, then the human steps of section 3 |
| Thu 2026-11-05 | Batch 1 approved and scheduled (target). Latest: Thu 2026-11-12 | Operator |
| Thu 2026-11-12 | Batch 2 (the posts of week 2) approved and scheduled | Operator |
| Mon 2026-11-16 | W0: the first 方寸 Instagram post, if every gate is closed | |

**This is a back-schedule, not a forecast.** Five weeks is not much time: the operator has 6 hours a week and the image packs alone are estimated at about 24 to 28 hours for all three pilots (`HUMAN_TODO.md` 34). See the capacity check in `README.md` section 4. If a gate is open on the Thursday before a post's week, **that post does not go out**, and if the whole first batch is not ready, W0 moves by whole weeks (section 10).

## 9. After publishing: the live check (about 2 minutes per post)

For every post, on the live post, not the draft:

1. The platform's own AI label is visible (or the platform label is on, in the YouTube case).
2. The first caption line is the AI line 「【AI 虛擬角色】…」 and nothing hides it behind "more"; for a sponsored post the commercial tag is in the first lines too.
3. The on-image badge 「AI 生成｜…」 is visible and not cut by the grid or square crop.
4. No location tag, no mention or tag of another persona, no link other than the persona's link page.
5. The first comments: any 「是真人嗎」 question counts toward the weekly tally (5 or more in a week means a stronger label within 48 hours, `portfolio.md` 6.2).
6. Screenshot the post with the date (kept outside the repo) and add the row to `schedule-log.csv`.

A label or badge missing on a published post is a disclosure failure: fix within 24 hours and log it; a repeat in the same quarter pauses the persona (`portfolio.md` 6.2).

## 10. If W0 slips

W0 moves by **whole weeks**, so the weekday pattern holds (`calendar-30d.md`). Three things do not move with it: the no-post days (polling day, 228), the 雙12 hook, and the quiet-block dates; `schedule_check.py` re-checks them for the new dates:

```
python3 launch/schedule_check.py --w0 2026-11-23     # shift one week
python3 launch/schedule_check.py --w0 2026-11-30 --grid
```

A shifted plan will run into new dates: 冬至 (Tue 2026-12-22), 聖誕 and 行憲紀念日 (Fri 2026-12-25), 跨年 (Thu 2026-12-31), 元旦 (Fri 2027-01-01) and the 農曆新年 run-up (2027-02-06, computed). Read `research/culture.md` 4 and the official calendar before scheduling across them (`HUMAN_TODO.md` 17 and 29). The script does not know the official holiday calendar; add any date with `--no-post`.

## 11. What is unverified or open in this file

* **Every scheduler claim** (Instagram app and Business Suite scheduling, its horizon, Threads native scheduling, YouTube's schedule option) and **whether the AI label and the paid-partnership tool can be set in a scheduled path**: settled only by the dry run.
* The polling date 2026-11-28 (recalled), the official 2027 holiday calendar, and which of the dated notes in the grid are holidays.
* Whether Threads accepts scheduled posts, and in which app.
* The exact limit on Shorts length and the safe zones (`HUMAN_TODO.md` 25).
* All minute values (assumptions from `portfolio.md` 5.1 and 5.3).
* Decision D5 (the quiet block) and decision D6 (still faces inside video: 3 of 方寸's 5 drafts and every 步驟 Short are on HOLD for it).
* Whether per-post approval is relaxed after day 30: not assumed.

