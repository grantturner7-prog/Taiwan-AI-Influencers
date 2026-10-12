# 色環 (sehuan) 30-day content calendar

**Status: DRAFT v0.2 (v0.1 written 2026-10-12, Phase 5, content; v0.2 updated the same day for three decisions).** Pilot persona, slot 3, niche FAS1 fashion (outfit logic, colour, climate styling). Platforms: Instagram (primary) and Threads. The 30 days run from **W0 = Mon 2026-11-16 (an assumption) to Tue 2026-12-15**. Weeks 1 and 2 are fully written; weeks 3 and 4 and days 29 and 30 are outlined.

**What changed in v0.2 (`DECISIONS.md`, 2026-10-12, "recommended answers adopted"; each decision is Claude's choice on the user's behalf and reversible).**

1. **OPS-D1: hold at 12 approvals a week across the three pilots through week 8.** 色環 keeps 4 approvals a week (2 Instagram + 2 Threads) in every week, not 6 in weeks 3 and 4. Two whole masters leave the 30 days: **M5 (P09 and P10) and M10 (P19 and P20)**, chosen as the lowest-value pair (section 6.1). The 30 days now hold **18 posts (9 Instagram, 9 Threads) from 9 masters**, not 22 and 11. The IDs P01 to P22 are kept so folder names, hook rows and the sibling schedule do not move.
2. **D6: a still photoreal face may appear in a Reel or Short with conditions** (gate 15 is closed; section 0 and 7.3). No 色環 draft was on hold for this reason and none is scheduled, so no post changes status.
3. **D3: Claude draws the diagram and lesson-graphic layer as SVG and renders it to PNG** (section 7.2). The operator's build time falls away; the operator's and the wife's review of every asset stays (section 8).

Nothing is approved by any of this.

**What this file is not.** No image, video or voice exists. Every media item is PENDING and carries its generation prompt (AI-generated character images) or a build spec (lesson graphics drawn by Claude as SVG, decision D3). Every zh-TW string is an AI draft for the wife to review, with an English gloss beside it because the operator does not read Chinese. Nothing is approved. No account, handle or studio name has been cleared. **No brand-paid, gifted, affiliate or client content appears anywhere in the 30 days** (the business is not registered, HUMAN_TODO 4 and 7; the lawyer has not answered; the image tools' commercial terms are unread, HUMAN_TODO 33), and no real brand, product or logo is named or shown (bible choice C5). This file contains no engagement data and no invented source; anything marked DEMO is format only.

**Reading order.** Section 0 (conventions), 1 (what moves the dates), 2 (cadence), 3 (the 30 days at a glance), 4 (holiday and taboo check), 5 (weeks 1 and 2 in full), 6 (weeks 3 and 4 outlined; 6.1 the posts deferred by OPS-D1), 7 (shared blocks: assets, Lesson Kit, labels, checklist), 8 (effort and capacity), 9 (open items for the human), 10 (checks run).

**Sources of authority.** `BRIEF.md` section 3 (ground rules) and 5 (language); `DECISIONS.md` (latest entries win, especially 2026-10-11 and 2026-10-12: photoreal AI characters that stay openly AI, and the 2026-10-12 "recommended answers adopted" entry with D6, D3 and OPS-D1); `ops/weekly-routine.md` (OPS-D1); `strategy/portfolio.md` (cadence 5.2, capacity 5, thresholds 6); `personas/sehuan/bible.md` (voice, pillars, disclosure, checklists); `personas/sehuan/photoreal-addendum.md` (the character's look; it supersedes the bible's visual sections); `pipeline/image-pack/sehuan-photoreal.md` (character lock and golden-set prompts); `research/culture.md` (calendar and taboos). Where this file departs from the bible's indicative plan (bible 6.5) the departure is listed in section 3.

---

## 0. Conventions

| Item | Meaning |
|---|---|
| Evidence labels | *assumption* = my planning figure, to calibrate. *unverified* = recalled or reported, not checked against a primary source. *computed* = calculated in this session (dates, weekdays, colour distances and contrast ratios were recomputed by script on 2026-10-12). |
| `UNVERIFIED-OPERATOR-TO-FILL` | A placeholder in a `sources[]` field of `post.json`. It marks a fact whose source the operator must open and record. **A post carrying this placeholder is BLOCKED**: it cannot be approved until the exact page and date replace it. No URL in these files has been invented. |
| `{待填}` | A fill-in field inside on-screen text. It must be replaced before the image is exported; braces must never appear in a published image. |
| NO FACTUAL CLAIM / ARITHMETIC ONLY | Prefixes of a `sources[]` entry that makes no external factual claim (a teaching device, a question, or an invented example sum). The pipeline checker allows an empty URL for these only. |
| Calendar IDs | P01 to P22 are posts in date order. M1 to M11 are masters (one idea feeding one Instagram post and one Threads post). Queue folders are `pipeline/review-queue/sehuan/<date>_<NN>/`. **P09, P10, P19 and P20 (masters M5 and M10) are deferred by OPS-D1**: they keep their IDs but are not in the 30 days, have no queue folder and are listed in section 6.1. |
| Series codes | A = 轉一格 (colour formulas, pillar P1). B1 = 三層順序 and B2 = 三關檢查 (the 三步整理 format: climate P2 and occasion P3). C = 一詞看懂 (read the information, pillar P4). See `series.md`. |
| Hook IDs | H01 to H44 in `hook-library.md`. |
| Flags | **AI-label flag = TRUE on every post** (studio rule, pipeline README). **Sponsorship flag = FALSE, type none, on every post.** |
| Times | Taiwan time (UTC+8). Days and times are a test, not a finding. |
| Colour words | Hex values are guidance for whoever builds the graphics (bible 4.4). Colours in image prompts are written as words, never hex. |
| Terms | 搭配示意 (styling illustration) is the standing label; the captions never say what the character wore or wears. |

The character appears as **still images** from the golden set. **Decision D6 (2026-10-12)** also lets a still, or a slow pan or zoom of a still, appear inside a Reel or Short, **only with all four conditions**: (1) the platform AI label is on; (2) a persistent on-screen badge 「AI 生成｜虛擬角色」 is on every frame; (3) no animation of the face (no blinking, lip-sync or morphing); (4) no synthetic voice (captions or human-recorded sound only). Face animation, synthetic voice and lip-sync stay barred (addendum risk J, QA checklist section 6) until a separate video addendum and review exist; Claude does not make video. **No Reel is drafted or scheduled in the 30 days.** No 色環 draft was ever on hold only for D6 (none had been written), and under OPS-D1 a Reel would count as one of the 4 approvals a week, taking an Instagram slot rather than adding a third, so a Reel enters the calendar only when a human decides to draft one. The platform-audio rule is also unchecked (bible G13). `series.md` holds the Reel templates, now carrying the D6 conditions, so one can be switched on after a human drafts it into the review queue.

---

## 1. What moves the dates (gates)

Nothing in this calendar can be published until the launch gates in `personas/sehuan/bible.md` 1.2 and the photoreal addendum are met. The ones that matter most for these posts:

| # | Gate | Owner | State (2026-10-12) |
|---|---|---|---|
| 1 | The user confirms that "real people" means photoreal AI characters that stay openly AI | User | Recorded in `DECISIONS.md` 2026-10-12 (the reading is Claude's, confirmed by the user's words "actual photo real characters") |
| 2 | The wife rules on the photoreal design questions that gate judging R01 (addendum 12.1 items 2, 3, 4, 5, 7) | Wife | Open (`HUMAN_TODO.md` 35) |
| 3 | Golden set exists and has passed the tests: R01 master, R02, R06 headshot, R12 chip-ring object still, R08b knees-up, R13 glance, E05 headshot (pack sections 4 to 6, addendum 9 and 11) | Operator, wife | **Open: no photoreal image exists** |
| 4 | Commercial-use terms of the exact Gemini or ChatGPT plan read and recorded (`HUMAN_TODO.md` 33). Until then every image is internal design material and nothing is published | User | Open |
| 5 | Instagram "AI-generated profile" label checked on a Taiwan test account (`HUMAN_TODO.md` 10 and 38) | Operator | Open |
| 6 | Name reading test, TIPO and 經濟部 searches, handle checks (`HUMAN_TODO.md` 18, 20, 21) | Wife, operator | Open |
| 7 | Wife's reviewer trial and vocabulary sign-off (`HUMAN_TODO.md` 8) | Wife | Open |
| 8 | Lawyer's launch-gate answers (`research/legal.md` 12: questions 1, 2, 3, 4, 6, 20, 22; photoreal questions in `HUMAN_TODO.md` 37) | User | Open |
| 9 | Business registration started | Wife (to be confirmed) | Open |
| 10 | **Lesson Kit v0** (section 7.2) drawn by Claude as SVG and rendered to PNG (**decision D3, 2026-10-12: authorised**); the operator and the wife review the kit once; a Taiwan-glyph font whose commercial licence has been read and whose file the operator supplies (bible G9, G14) | Claude draws; operator and wife review; operator supplies the font | Open: the kit is **not yet drawn**, the font licence is unread, and the render sandbox has no Noto Sans TC (checked 2026-10-12) |
| 11 | Colour-theory reference chosen and logged (bible G7) | Operator | Open. Optional for P01 and P05 (both are labelled rules of thumb with no source claim); **required before P17** (adjacent and opposite colours) |
| 12 | Weather source chosen: the agency's climate-statistics page for Taipei and Kaohsiung (bible G8) | Operator | Open. **Blocks P03** and every later P2 post that shows a number |
| 13 | One neutral public source for the size-label terms 平量 and 圍度 (bible 6.4 and open item 26) | Operator | Open. **Blocks P07 and P08** |
| 14 | Polling-day date confirmed with the Central Election Commission (recalled as Sat 2026-11-28, *unverified*; `HUMAN_TODO.md` 17) | Operator | Open |
| 15 | A still photoreal face inside a Reel or Short before the video and voice addendum exists | User | **Closed by D6 (2026-10-12) with four conditions** (section 0): AI label on, persistent badge 「AI 生成｜虛擬角色」, no animation of the face, no synthetic voice. No Reel is drafted or scheduled in the 30 days |
| 16 | Fashion-contact sanity-check route (bible G10) | User | Open. Not needed for P01 to P14; **needed from P15** (occasion posts) |
| 17 | The user approves the Threads text-only first-line adaptation (bible 8.2 and open item 14) | User | Open. Needed for P04 and P12 (P20 is deferred by OPS-D1) |

**Shift rule.** If a gate slips, move W0 by **whole weeks** so the weekday pattern holds, and shift every date together. Three things do not shift with W0: (a) the no-post day on polling day (recomputed against the confirmed date); (b) the 雙12 rule (no price, discount or sale wording on any post), which is tied to Sat 2026-12-12 and applies to whatever is scheduled near it (P19 and P20 are deferred by OPS-D1; if they are restored they land on 12-11 and 12-12); (c) the quiet days and the 228 rule later in the year. Re-run the section 4 check after any shift. If the confirmed polling day falls outside the window, the colour-neutral rule for weeks 1 and 2 may be relaxed by the user; it is kept here because the date is unconfirmed.

**Approval lead time (assumption).** The weekly rhythm in `portfolio.md` 5.5 is: Monday batch ready, Tuesday operator pre-check, Wednesday wife review, Thursday final approval and scheduling. Allow one full week between the batch being ready and the first post, and **two weeks for the first batch** because the golden set must exist and Lesson Kit v0 must be drawn and reviewed first (section 8).

---

## 2. Cadence, days and times

From `portfolio.md` 5.2 and bible 6, **as changed by decision OPS-D1** (`DECISIONS.md` 2026-10-12; `ops/weekly-routine.md`): the pilots are held at **12 approvals a week combined through the first 8 weeks**, which is 2 posts per platform per pilot. 色環 therefore posts **2 Instagram + 2 Threads a week (4 approvals, 2 masters) in every week**; the portfolio's 3 + 3 from week 3 is not used. The step up to 3 + 3 is made only after logged minutes show room, and `ops/weekly-routine.md` 2.4 plans none before the week-8 review (Thu 2027-01-14); the deferred masters in section 6.1 are then restored first. One master feeds one Instagram post and one Threads post: production counts once and approvals twice (`portfolio.md` 5.1).

| Week | Dates | Instagram (20:30) | Threads (18:00) | Approvals | Masters |
|---|---|---|---|---|---|
| W1 | 2026-11-16 to 22 | Wed 11-18, Fri 11-20 | Thu 11-19, Sat 11-21 | 4 | 2 (M1, M2) |
| W2 | 2026-11-23 to 29 | Mon 11-23, Wed 11-25 | Tue 11-24, Thu 11-26 | 4 | 2 (M3, M4) |
| W3 | 2026-11-30 to 12-06 | Wed 12-02, Fri 12-04 | Thu 12-03, Sat 12-05 | 4 | 2 (M6, M7) |
| W4 | 2026-12-07 to 13 | Mon 12-07, Wed 12-09 | Tue 12-08, Thu 12-10 | 4 | 2 (M8, M9) |
| Days 29 and 30 | 2026-12-14, 12-15 | Mon 12-14 | Tue 12-15 | 2 | 1 (M11) |
| **Total** | 30 days | 9 | 9 | **18** | **9** |

**Deferred by OPS-D1 (section 6.1):** Mon 11-30 and Tue 12-01 (P09, P10; master M5) and Fri 12-11 and Sat 12-12 (P19, P20; master M10). Before OPS-D1 the table held 6 approvals in each of W3 and W4 and 22 in all (computed: 4 + 4 + 6 + 6 + 2 = 22; now 4 + 4 + 4 + 4 + 2 = 18). The primary platform (Instagram) keeps 2 posts a week in each of W1 to W4, which is the floor.

Design choices (*assumption*; all to be tested, not defended):

- **The first post is Wed 2026-11-18, not Mon 11-16.** W0 is the week the pilots start. 方寸's calendar launches on Instagram on Mon 2026-11-16 and proposes 色環 launches on Wed 2026-11-18; 步驟's calendar launches on Thu 2026-11-19. The studio rule is no coordinated launch on the same day and no two personas posting in the same clock hour (`portfolio.md` 3.3 item 6).
- **Slots known on 2026-10-12 (read from the sibling calendars, section 2 of each; the three were written in parallel):** 方寸 Instagram Mon and Thu 12:30 (plus Sat 10:30 from W3), YouTube Shorts Tue and Fri 19:30 (plus Sun 19:30 from W3); 步驟 Threads 08:15 and YouTube Shorts 21:00 on Thu and Sun in weeks 1 and 2, and on Tue, Thu and Sun from week 3. 色環 posts Instagram at **20:30** (Mon, Wed, Fri) and Threads at **18:00** (Tue, Thu, Sat). Those were the slots before OPS-D1; the sibling calendars were then updated for OPS-D1 as well, and the check was re-run on the updated working-tree files (section 10, check 11): 方寸 now posts Instagram Mon and Thu 12:30 and YouTube Shorts Tue and Fri 19:30 with no weekend slot, and 步驟 keeps Threads 08:15 and Shorts 21:00 on its own days. **No two personas share a clock hour on the same date** across the 色環 slots that remain; the closest pairs are 60 minutes apart, 方寸's Friday Short at 19:30 and my Instagram post at 20:30 on 11-20 and 12-04 (12-11 left with P19). 步驟's Thursday launch day shares a date with my Threads post of 11-19 (18:00 against its 08:15 and 21:00); that is not a 色環 launch. **The operator must still reconcile the three calendars** (open item 3): the other two calendars schedule posts inside this calendar's quiet block (方寸's Friday Short on 2026-11-27 and 步驟's Sunday posts on 2026-11-29); those are decisions for their files.
- **Threads follows Instagram by one day** (Wed to Thu, Fri to Sat, Mon to Tue, Wed to Thu), so the Instagram carousel is the master and the Threads post is the short native version. The pair is also the test for hypothesis H2 (Instagram against Threads for the same idea, common metric (shares + comments) per 1,000 views, `portfolio.md` 4.2 and 6.1).
- **Quiet block Fri 11-27, Sat 11-28, Sun 11-29.** The recalled polling day is Sat 2026-11-28 (*unverified*); the day before is Black Friday and the recalled campaign eve; the day after is likely to carry heated comment threads. Nothing is scheduled on those three days. W2 therefore ends on Thu 11-26. **Effect of OPS-D1:** Mon 11-30 and Tue 12-01 are also empty (P09 and P10 are deferred), so the account is silent for five days (Fri 11-27 to Tue 12-01) and W3 starts on Wed 12-02, as W1 started on Wed 11-18. That gives the comment threads two more days to settle, at the cost of a longer gap; whether a five-day gap hurts reach is untested (*assumption*). If the operator prefers continuity, P11 and P12 can move to Mon 11-30 and Tue 12-01 (the weekday rules in section 2 still hold), but the queue folders, hooks and the launch schedule then move with them.
- **Posting is by the platform's own scheduler or by hand**, after the operator's final approval (`portfolio.md` 5.5). No third-party automation (Ground rule 9).
- **Pause switch** (`portfolio.md` 5.5): a disaster, a typhoon day or a public tragedy unschedules everything.
- Rest days are not empty: they carry the comment batches (`reply-guidelines.md`), the Friday trend check (`trend-check.md`) and the weekly report.

---

## 3. The 30 days at a glance

Computed for W0 = Mon 2026-11-16 (weekdays checked by script). Section 5 has P01 to P08 in full; section 6 has the rest; section 6.1 has the four posts deferred by OPS-D1 (P09, P10, P19, P20), which are not in the table below.

| Day | Date | Weekday | Week | Posts (ID, platform, format) | Notes |
|---|---|---|---|---|---|
| 1 | 2026-11-16 | Mon | W1 | none | W0 (assumption). 方寸 launches on Instagram today; 色環 stays quiet |
| 2 | 2026-11-17 | Tue | W1 | none | Final checks of the first batch |
| 3 | 2026-11-18 | Wed | W1 | P01 IG carousel | **Launch**: identity slide inside a colour-formula post. Pin it if the app allows |
| 4 | 2026-11-19 | Thu | W1 | P02 Threads image | |
| 5 | 2026-11-20 | Fri | W1 | P03 IG carousel | **Blocked until the weather data is filled (gate 12)** |
| 6 | 2026-11-21 | Sat | W1 | P04 Threads text | Needs gate 17 |
| 7 | 2026-11-22 | Sun | W1 | none | Weekly report; the Friday trend check feeds the next batch |
| 8 | 2026-11-23 | Mon | W2 | P05 IG carousel | Colour-neutral week (election run-up) |
| 9 | 2026-11-24 | Tue | W2 | P06 Threads image | |
| 10 | 2026-11-25 | Wed | W2 | P07 IG carousel | **Blocked until the size-term source is recorded (gate 13)** |
| 11 | 2026-11-26 | Thu | W2 | P08 Threads image | Blocked with P07 |
| 12 | 2026-11-27 | Fri | W2 | none | Black Friday; recalled campaign eve. Quiet |
| 13 | 2026-11-28 | Sat | W2 | **none, hard stop** | Recalled polling day (*unverified*). No post, no scheduled post; hide political comments |
| 14 | 2026-11-29 | Sun | W2 | none | Day after; watch comments |
| 15 | 2026-11-30 | Mon | W3 | none | First day after the quiet block. P09 is deferred by OPS-D1. Comment batch |
| 16 | 2026-12-01 | Tue | W3 | none | P10 is deferred by OPS-D1 |
| 17 | 2026-12-02 | Wed | W3 | P11 IG carousel | |
| 18 | 2026-12-03 | Thu | W3 | P12 Threads text | Needs gate 17 |
| 19 | 2026-12-04 | Fri | W3 | P13 IG carousel | 色差 explainer lands before 雙12 |
| 20 | 2026-12-05 | Sat | W3 | P14 Threads image | |
| 21 | 2026-12-06 | Sun | W3 | none | Weekly report |
| 22 | 2026-12-07 | Mon | W4 | P15 IG carousel | First occasion post: needs gate 16 |
| 23 | 2026-12-08 | Tue | W4 | P16 Threads image | |
| 24 | 2026-12-09 | Wed | W4 | P17 IG carousel | Needs gate 11 |
| 25 | 2026-12-10 | Thu | W4 | P18 Threads image | |
| 26 | 2026-12-11 | Fri | W4 | none | P19 is deferred by OPS-D1 |
| 27 | 2026-12-12 | Sat | W4 | none | 雙12 (*computed*). P20 is deferred by OPS-D1; no post, so no price, discount or sale content |
| 28 | 2026-12-13 | Sun | W4 | none | Weekly report |
| 29 | 2026-12-14 | Mon | W5 | P21 IG carousel | Needs gate 16 |
| 30 | 2026-12-15 | Tue | W5 | P22 Threads image | End of the 30 days. 6-week review is Mon 2026-12-28 |

**Totals after OPS-D1:** 18 posts scheduled (9 Instagram, 9 Threads; 8 written in full, 10 outlined) and 4 deferred (P09, P10, P19, P20); 9 masters (M5 and M10 are deferred with them). Posts per week: 4, 4, 4, 4 and 2 on days 29 and 30 (*computed*: 18). Pillar mix of the 9 masters: P1 3 (M1, M3, M9), P2 2 (M2, M6), P3 2 (M8, M11), P4 2 (M4, M7). The bible's target for weeks 3 to 8 is P1 39%, P2 22%, P3 22%, P4 17% (*assumption*); this 30-day slice is 33%, 22%, 22%, 22%, close enough to calibrate against, and weeks 3 and 4 hold exactly one master of each pillar (M6 P2, M7 P4, M8 P3, M9 P1). Before OPS-D1 the slice was 22 posts, 11 masters and 36%, 27%, 18%, 18%.

**Deviations from the bible's indicative plan (bible 6.5), with reasons.**

| Bible 6.5 said | This calendar does | Why |
|---|---|---|
| W1: P2-1 then P1-1 | M1 = P1-1 (三色口訣), M2 = P2-1 | The launch post carries the identity slide, so it should be the post that is safest in the election window and least dependent on an unfilled source. P1-1 needs no external source; P2-1 needs the weather page |
| W2: P1-3 (adjacent and opposite) and P4-1 | M3 = **P1-4** (neutrals), M4 = P4-1; P1-3 moves to **P17 (12-09)** | Opposite colours on the wheel invite the very pairs (blue against orange or green, red against green) that read as camps in the election run-up (bible C3). Neutrals are the most colour-neutral lesson in the set |
| W4: P3-5, P1-4, P2-3 | M8 = P3-5, M9 = P1-3, M10 = **P2-5** (**deferred by OPS-D1**) | P2-3 is plum-rain colours; plum rain is about May to June (bible 6.5), so it is out of season in December. P2-5 (rainy-day trouser length and shoe colour) fits the damp north in winter. M10 is then cut from the 30 days under OPS-D1 (section 6.1) |
| W5 begins with P3-1 (尾牙) on 12-14 to 12-20 | M11 = P3-1 (尾牙) on 12-14 and 12-15 | 尾牙 is Sat 2027-01-23 (*computed*, `culture.md` 4.2): about five weeks ahead, the bible's "a month ahead" |
| Three posts a week per platform from W3 (`portfolio.md` 5.2) | **Two a week per platform in every week** | OPS-D1 (adopted 2026-10-12): 12 approvals a week across the three pilots through week 8. M5 (P09, P10) and M10 (P19, P20) are deferred; section 6.1 gives the reasons and the restore order |
| (not stated) | W1 starts on Wed, and Fri 11-27 to Sun 11-29 are quiet | Section 2 |

---

## 4. Holiday, taboo and sensitivity check for 2026-11-16 to 2026-12-15

Dates are *computed* unless marked; the polling day is recalled (*unverified*). Sources: `research/culture.md` 4 and 5; bible 3.3 D, 6.5, 7.2.

| Date or window | What it is | What this calendar does |
|---|---|---|
| Sat 2026-11-28 | Recalled local-election polling day (*unverified*) | Hard stop: nothing scheduled, no post, comments with political content hidden and never answered. The Fri before and Sun after are also quiet |
| 2026-11-16 to 11-29 | Election run-up | Colour-neutral content (bible C3): no blue, green, teal or yellow headline or cover, no camp pair (藍綠, 藍白, 綠白) anywhere in a headline, caption lead or cover; the wheel appears only as a muted circular diagram; the persimmon is never a headline colour. The only slides that show the wheel's blue and green segments are P01 slide 5 and P05 slide 3 (muted, circular, numbered, in a neutral diagram), plus the earrings on the character, which carry the same twelve muted segments |
| Fri 2026-11-27 | Black Friday (*computed*) | No post; no price, discount or sale content any day |
| Sat 2026-12-12 | 雙12 (*computed*) | Nothing is scheduled on Fri 12-11 or Sat 12-12 (P19 and P20 are deferred by OPS-D1). If they are restored, P20 is a text question with no price or sale wording and P19 says nothing about buying. No other post may carry price, discount or sale wording either |
| 週年慶 (autumn 2026) | Dates not found (`culture.md` 4.4) | "How to read a label" content only; no discount figures; no 週年慶 price content |
| Tue 2026-12-22 (冬至), Fri 12-25 (聖誕), Thu 12-31 (跨年), Fri 2027-01-01 (元旦) | Outside the 30 days | P15 (12-07) is a planning post for the Christmas and countdown parties; no festive jokes on 冬至; red and green appear only in a neutral layout with no slogan |
| Sat 2027-01-23 | 尾牙 (*computed*; companies hold them in January and February, *unverified*) | P21 (12-14) is about five weeks ahead |
| Mourning colours | All-white and all-black outfits | Never in celebration content (P15, P21); every example outfit has a second colour |
| Gift taboos | Umbrella, shoes, clock, fan, scissors, handkerchief; sets of four | P19 (deferred; if restored) shows trouser length and shoe colour as styling, never as a gift; no set of four in any list (lists are three items; the wheel has twelve) |
| Politics, religion, ritual dress, Indigenous patterns, rainbow | `culture.md` 5 | None used; no rainbow emoji or six-stripe bar; the wheel is a muted circle (bible C4) |
| Pride window (probable Sat 2026-10-31, *unverified*) | Before W0 | Nothing in the 30 days |
| Typhoon or other disaster | Pause switch | Unschedule everything; no promotional tone |
| Ghost month | 2027-08-02 to 08-31 | Far outside the window |
| Weekly moderation | Comments on any post may drift to politics around 11-28 | Hide, never reply, never like (`reply-guidelines.md`) |

---

## 5. Weeks 1 and 2: fully written (P01 to P08)

### P01 · Wed 2026-11-18 20:30 · Instagram carousel · 轉一格 #01 (M1)

| Field | Value |
|---|---|
| Queue folder | `pipeline/review-queue/sehuan/2026-11-18_01/` (`sehuan-2026-11-18-01`) |
| Pillar · series · master | P1 配色公式 · 轉一格 #01 · M1 |
| Hook (zh-TW, 17 characters) | 三色口訣：主色、輔色、點綴色怎麼分 |
| On-screen label | AI 生成｜虛擬角色（有色環的頁面）／AI 生成（純圖解的頁面） |
| Flags | AI label **TRUE** · sponsorship flag **false** · type none |
| Caption length | 159 characters (limit about 2200, recalled, *unverified*) |
| Status | Ready for review once the media exist (media PENDING; no source blocks it) |

**Caption (zh-TW, DRAFT)**

```
【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布，圖像為 AI 生成，並非真人。
配色比例的一個口訣（經驗法則）：主色六成、輔色三成、點綴色一成。
這篇用三組搭配示意圖拆給你看，先收藏起來，之後搭配時可以對照～
圖為搭配示意，不是實際商品；這是經驗法則，不是標準。
螢幕有色差，實際顏色以品牌提供的資訊為準。
```

**Gloss (English, for the operator)**

```
[AI virtual character] This post is published by the AI-generated virtual character "Sehuan"; the images are AI-generated and are not a real person.
A rule of thumb for colour proportion: main colour 60%, secondary colour 30%, accent colour 10%.
This post breaks it down in three styling illustrations. Save it and compare when you put outfits together~
The images are styling illustrations, not real products; this is a rule of thumb, not a standard.
Screens shift colour; for the real colour, go by the information the brand provides.
```

**Hashtags:** #配色 #穿搭公式 #色彩 #搭配示意 #AI虛擬角色

**Slides (all drawn by Claude as SVG from Lesson Kit v0 and rendered to PNG, with approved golden-set images placed as supplied files; every zh-TW line is a DRAFT; the operator and the wife review every slide)**

| # | Name | On-screen text (zh-TW, DRAFT) | Gloss | Visual build spec | Badge | Assets |
|---|---|---|---|---|---|---|
| 1 | cover | 三色口訣／主色、輔色、點綴色怎麼分／轉一格 #01 | Three-colour rule of thumb / How to tell main, secondary and accent colours apart / Turn-one-step #01 (series chip) | Pale-blush ground (#F2DAD2); title in charcoal (#3A3735) on the upper two-thirds; a persimmon (#CD8B6A) underline under 「三色口訣」 (the only persimmon on the slide, at most one tenth of it); cut-out of A1 lower-left. Badge top-right, inset at least 11% of the height from the top and bottom edges and at least 8% of the width from the sides (so a centred square crop of a 4:5 picture cannot remove it; see pipeline/qa-checklist.md D3). | 「AI 生成｜虛擬角色」 | A1 |
| 2 | who I am | 我是色環，AI 虛擬角色。／我沒有衣櫃，連這圈色票也是 AI 生成的。／角色造型是設計，不是穿搭示範。 | I'm Sehuan, an AI virtual character. / I have no wardrobe; even this ring of colour chips is AI-generated. / The character's outfit is a design, not an outfit demonstration. | A2 on the right two-fifths (cut-out or framed panel, no shadow trick); a small arrow added in post pointing to the chip ring; text left, three lines, large. J2 line is the photoreal replacement of addendum 12.2; the wife rules on it. | 「AI 生成｜虛擬角色」 | A2 |
| 3 | the rule | 配色比例的一個口訣（經驗法則）／主色 六成｜輔色 三成｜點綴色 一成／這是經驗法則，不是標準。 | A rule of thumb for colour proportion / Main 60% \| secondary 30% \| accent 10% / This is a rule of thumb, not a standard. | One horizontal bar split 6:3:1 drawn to scale (warm stone #B8AEA2 / cream #F4E8DF / persimmon #CD8B6A), labels under each segment; A3 as a framed panel on the right edge, glancing toward the bar. No second bar, no stripes of six or more colours. | 「AI 生成｜虛擬角色」 | A3 |
| 4 | three combinations | 三組搭配示意／① 暖灰＋奶油白＋柿子橘／② 炭灰＋暖灰＋灰玫瑰色／③ 奶油白＋炭灰＋灰紫色／主色佔最大面積，點綴色最小 | Three styling illustrations / (1) warm stone + cream + persimmon / (2) charcoal + warm stone + dusty rose / (3) cream + charcoal + soft violet / The main colour takes the largest area, the accent the smallest | Three faceless dress forms (人台) side by side, each dressed in generic garment flats drawn as SVG (jacket, top, scarf or tote; no logo, tag, pattern or invented detail), each with the 6:3:1 bar under it. Persimmon, dusty rose (#C27F80) and soft violet (#9F8AAB) each cover at most one tenth of their form. Label 「搭配示意」 on the slide. No character on this slide. | 「AI 生成｜搭配示意」 | none |
| 5 | turn one step | 轉一格／公式不變，色環轉一格，換個色相再看一次。／點綴色：柿子橘 → 紅橘色 | Turn one step / Same formula; turn the wheel one step; look again in a new hue. / Accent colour: persimmon -> red-orange | The 12-segment muted wheel (drawn as SVG; positions numbered 1 to 12, no colour-pair labels) with positions 3 and 2 highlighted and a curved arrow between them; beside it the slide-4 combination 1 re-coloured with position 2 (#C58479) as the accent. Same bar, same proportions. | 「AI 生成｜搭配示意」 | none |
| 6 | your turn | 換你填／主色 ＿＿（六成）／輔色 ＿＿（三成）／點綴色 ＿＿（一成）／先收藏起來，之後搭配時可以對照～ | Your turn / Main __ (60%) / Secondary __ (30%) / Accent __ (10%) / Save it and compare when you put outfits together~ | Clean worksheet: the empty 6:3:1 bar with three blank lines; no character panel on this slide. | 「AI 生成」 | none |
| 7 | footers | 本篇由明說角色工作室創作與營運。／圖像為 AI 生成，並非真人。／這是配色的經驗法則，不是標準，沒有外部出處。／螢幕有色差，實際顏色以品牌提供的資訊為準。 | This post is created and run by Plainspoken Studio. / The images are AI-generated and are not a real person. / This is a colour rule of thumb, not a standard, and has no external source. / Screens shift colour; for the real colour, go by the information the brand provides. | Small centred type on the ground colour; the 「AI 生成」 badge in the same corner as every other slide; no persimmon needed. | 「AI 生成」 | none |

**AI-generated assets (all PENDING; prompts are in the `shot_prompt` of each media item)**

- **A1** `R01_master_v1`: AI-generated photoreal image of the openly-AI character 色環; label added in post, never generated. Master portrait R01: waist-up, front, outfit A, calm closed-mouth expression, both hands below the frame. Alt text: 「AI 生成的虛擬角色色環，非真人。」 (AI-generated virtual character Sehuan, not a real person.)
- **A2** `R08b_knees-up_v1`: AI-generated photoreal image of the openly-AI character 色環; label added in post, never generated. Knees-up, hands inside the trouser pockets, outfit A, chip ring of exactly six blank cards clipped at the left hip (R08b). Alt text: 「AI 生成的虛擬角色色環，非真人。」 (AI-generated virtual character Sehuan, not a real person.)
- **A3** `R13_glance_v1`: AI-generated photoreal image of the openly-AI character 色環; label added in post, never generated. Waist-up glance toward the lesson (R13), outfit A; the arrows are drawn in the SVG layer. Alt text: 「AI 生成的虛擬角色色環，非真人。」 (AI-generated virtual character Sehuan, not a real person.)

**Sources**

- NO FACTUAL CLAIM: the 60/30/10 split is presented as a rule of thumb (口訣, 經驗法則) that the studio teaches, not as a cited standard and not as something 'commonly cited'. The three proportions are drawn to scale in the SVG source file (6:3:1 = 60%, 30%, 10%). If the operator logs a colour-theory reference (gate G7) that contains the rule, add it here and on slide 7; if not, leave this entry as it is.

**The wife rules on**

- The J2 line 「我沒有衣櫃，連這圈色票也是 AI 生成的。」 and the J1-style line (addendum 12.2).
- Colour names: 柿子橘 / 柿橘 / 柿色, 灰玫瑰色, 灰紫色, 紅橘色, 暖灰 (all draft; the pair 灰玫瑰色 and 灰紫色 is new in this file).
- 六成／三成／一成 against 60%／30%／10%.
- The ～ at the end of caption line 3, and 拆給你看.
- Colour footer: 官方 was replaced by 品牌提供 (the pipeline checker treats 官方 as a source-dependent claim); she may restore 官方.
- Election-window colour read: no camp pair, no dominant saturated blue, green, teal or yellow; persimmon not read as a party colour.

**The operator checks**

- Bar drawn to scale (6:3:1) and persimmon at most one tenth of slides 1 and 4.
- A2 shows exactly six blank cards, no text on them, no hands, correct hip.
- Alt text set on every image; platform AI label ON; Instagram 'AI-generated profile' label test done first (HUMAN_TODO 38).
- Pin this post if the app allows (it carries the identity slide); the pinned-post text of bible 8.1 plus the addendum 8.2 line can be pasted as the highlight.

### P02 · Thu 2026-11-19 18:00 · Threads image · 轉一格 #01 (Threads version) (M1)

| Field | Value |
|---|---|
| Queue folder | `pipeline/review-queue/sehuan/2026-11-19_01/` (`sehuan-2026-11-19-01`) |
| Pillar · series · master | P1 配色公式 · 轉一格 #01 (Threads version) · M1 |
| Hook (zh-TW, 15 characters) | 點綴色最多一成，你會放在哪裡？ |
| On-screen label | AI 生成｜虛擬角色 |
| Flags | AI label **TRUE** · sponsorship flag **false** · type none |
| Caption length | 99 characters (limit about 500, recalled, *unverified*) |
| Status | Ready for review once the media exist (media PENDING; no source blocks it) |

**Caption (zh-TW, DRAFT)**

```
【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布，圖像為 AI 生成，並非真人。
三色口訣（經驗法則）：主色六成、輔色三成、點綴色一成。
你會把一成的點綴色放在哪裡？外套、包包，還是鞋子？
```

**Gloss (English, for the operator)**

```
[AI virtual character] This post is published by the AI-generated virtual character "Sehuan"; the image is AI-generated and is not a real person.
Three-colour rule of thumb: main colour 60%, secondary 30%, accent 10%.
Where would you put the 10% accent? On the jacket, the bag, or the shoes?
```

**Hashtags:** #配色

**Card (all drawn by Claude as SVG from Lesson Kit v0 and rendered to PNG, with an approved golden-set image placed as a supplied file; every zh-TW line is a DRAFT; the operator and the wife review every slide)**

| # | Name | On-screen text (zh-TW, DRAFT) | Gloss | Visual build spec | Badge | Assets |
|---|---|---|---|---|---|---|
| 1 | formula card | 三色口訣（經驗法則）／主色 六成｜輔色 三成｜點綴色 一成／點綴色，你會放在哪裡？ | Three-colour rule of thumb / Main 60% \| secondary 30% \| accent 10% / Where would you put the accent? | One card, ground #F2DAD2, charcoal type. The 6:3:1 bar drawn to scale across the middle (same fills as P01 slide 3). A5 as a small framed square panel in the top-left corner (about one fifth of the card width). A persimmon underline under the question only. Badge top-right, inset at least 11% of the height from the top and bottom edges and at least 8% of the width from the sides (so a centred square crop of a 4:5 picture cannot remove it; see pipeline/qa-checklist.md D3). | 「AI 生成｜虛擬角色」 | A5 |

**AI-generated assets (all PENDING; prompts are in the `shot_prompt` of each media item)**

- **A5** `EXP_E05_*_v1`: AI-generated photoreal image of the openly-AI character 色環; label added in post, never generated. Mild-smile headshot (E05), 1:1, shown as a small framed panel. Alt text: 「AI 生成的虛擬角色色環，非真人。」 (AI-generated virtual character Sehuan, not a real person.)

**Sources**

- NO FACTUAL CLAIM: same rule of thumb as sehuan-2026-11-18-01 (a labelled teaching device, not a cited standard); the closing line is a question to the audience.

**The wife rules on**

- Is 你會放在哪裡 a natural question for a comment thread, and does 一成 read clearly as 'one tenth'?
- The first line uses the photoreal line v2 because a headshot appears on the card.

**The operator checks**

- Card matches P01 slide 3 (same proportions and fills).
- A5 passes the face checks (hands absent, six-or-fewer defects, same person as R01).
- Platform AI label ON; Threads label carry-over from Instagram unverified (HUMAN_TODO 38).

### P03 · Fri 2026-11-20 20:30 · Instagram carousel · 三步整理・三層順序 #01 (M2)

| Field | Value |
|---|---|
| Queue folder | `pipeline/review-queue/sehuan/2026-11-20_01/` (`sehuan-2026-11-20-01`) |
| Pillar · series · master | P2 氣候穿搭 · 三步整理・三層順序 #01 · M2 |
| Hook (zh-TW, 20 characters) | 東北季風天，濕冷怎麼疊？先記住三層順序。 |
| On-screen label | AI 生成｜虛擬角色（有色環的頁面）／AI 生成（純圖解的頁面） |
| Flags | AI label **TRUE** · sponsorship flag **false** · type none |
| Caption length | 169 characters (limit about 2200, recalled, *unverified*) |
| Status | **BLOCKED** until the `UNVERIFIED-OPERATOR-TO-FILL` sources are recorded (media also PENDING) |

**Caption (zh-TW, DRAFT)**

```
【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布，圖像為 AI 生成，並非真人。
東北季風天，濕冷怎麼疊？先記住三層順序：內層、中層、外層。
這是工作室整理的疊穿框架，不是標準；顏色比例用面積來看會比較清楚。
氣象資料在第 4 張，標示城市與資料日期；僅供搭配示意，非天氣預報，最新預報請看氣象署。
圖為搭配示意，不是實際商品。
```

**Gloss (English, for the operator)**

```
[AI virtual character] This post is published by the AI-generated virtual character "Sehuan"; the images are AI-generated and are not a real person.
On northeast-monsoon days, how do you layer for damp cold? Remember the three-layer order first: inner, middle, outer.
This is the studio's own layering framework, not a standard; colour proportions are easier to see by area.
The weather data is on slide 4, with the city and the data date; for styling illustration only, not a forecast; for the latest forecast see the weather agency.
The images are styling illustrations, not real products.
```

**Hashtags:** #疊穿 #濕冷穿搭 #配色 #AI虛擬角色

**Slides (all drawn by Claude as SVG from Lesson Kit v0 and rendered to PNG, with approved golden-set images placed as supplied files; every zh-TW line is a DRAFT; the operator and the wife review every slide)**

| # | Name | On-screen text (zh-TW, DRAFT) | Gloss | Visual build spec | Badge | Assets |
|---|---|---|---|---|---|---|
| 1 | cover | 東北季風天／濕冷怎麼疊？／先記住三層順序／三步整理・三層順序 #01 | On northeast-monsoon days / How do you layer for damp cold? / Remember the three-layer order first / Series chip: three-step round-up, three layers #01 | Pale-blush ground; title large in charcoal; persimmon underline under 「三層順序」; cut-out of A3 lower-left (glancing toward the title). No weather icons, no rain drawing, no umbrella. Badge top-right. | 「AI 生成｜虛擬角色」 | A3 |
| 2 | the three layers | 內層｜中層｜外層／順序固定，顏色再各自換／這是工作室整理的框架，不是標準 | Inner \| middle \| outer / The order is fixed; the colours change each time / This is the studio's framework, not a standard | Three generic garment flats in a row (inner cream tee, middle charcoal knit, outer warm-stone coat), numbered 1, 2, 3 with arrows pointing outward; no logo, tag or invented detail. Label 「搭配示意」. No character on this slide. | 「AI 生成｜搭配示意」 | none |
| 3 | by area | 以露出的面積來看／外層最多，先決定主色／內層最少，適合放點綴色（經驗法則） | Look at it by visible area / The outer layer shows the most and sets the main colour / The inner layer shows the least and suits the accent (rule of thumb) | Three horizontal bars of 60, 30 and 10 units labelled 外層, 中層, 內層 using the same fills as the P01 bar; a small dress form beside them. Persimmon only on the 內層 bar. | 「AI 生成｜搭配示意」 | none |
| 4 | weather data (BLOCKED until filled) | 氣象資料（搭配示意用）／台北 11 月平均氣溫 {待填}°C｜12 月 {待填}°C／高雄 11 月 {待填}°C｜12 月 {待填}°C／統計：{統計種類與期間}／氣象資料來源：{氣象署頁面名稱}｜{城市}｜{YYYY/MM/DD}。僅供搭配示意，非天氣預報，最新預報請見氣象署。 | Weather data (for styling illustration) / Taipei mean temperature in November {fill} C \| December {fill} C / Kaohsiung November {fill} C \| December {fill} C / Statistic: {statistic type and period} / Source line (agency page, city, date); for styling illustration only, not a forecast; see the agency for the latest forecast. | A plain two-by-two table, charcoal type, no chart, no icons. Every number typed from the saved agency page; the capture date shown on the slide. The braces {待填} must never reach the exported image. The wife judges the regional wording (Taipei damp cold versus Kaohsiung). | 「AI 生成」 | none |
| 5 | two illustrations | 兩組示意／例一：同色系，只改明暗／例二：點綴色放在內層 | Two illustrations / Example 1: one colour family, only the lightness changes / Example 2: the accent goes in the inner layer | Two small dress forms with three flats each. Example 1: light, mid and dark warm stone. Example 2: the inner layer is persimmon showing only at the neckline (at most one tenth), the middle charcoal, the outer warm stone. Label 「搭配示意」. | 「AI 生成｜搭配示意」 | none |
| 6 | your turn | 換你填／外層 ＿＿｜中層 ＿＿｜內層 ＿＿／看看三層的面積比例 | Your turn / Outer __ \| middle __ \| inner __ / Look at the area proportion of the three layers | Clean worksheet with three blank lines and the empty 60/30/10 bars; no character panel. | 「AI 生成」 | none |
| 7 | footers | 本篇由明說角色工作室創作與營運。／圖像為 AI 生成，並非真人。／三層順序是工作室整理的框架，不是標準。／氣象資料來源：{氣象署頁面名稱}｜{城市}｜{YYYY/MM/DD}。僅供搭配示意，非天氣預報，最新預報請見氣象署。／螢幕有色差，實際顏色以品牌提供的資訊為準。 | Created and run by Plainspoken Studio. / The images are AI-generated and are not a real person. / The three-layer order is the studio's framework, not a standard. / Climate source line. / Screens shift colour; for the real colour, go by the information the brand provides. | Small centred type; the climate source line repeats slide 4 exactly (same page title, city, date). | 「AI 生成」 | none |

**AI-generated assets (all PENDING; prompts are in the `shot_prompt` of each media item)**

- **A3** `R13_glance_v1`: AI-generated photoreal image of the openly-AI character 色環; label added in post, never generated. Waist-up glance toward the lesson (R13), outfit A; the arrows are drawn in the SVG layer. Alt text: 「AI 生成的虛擬角色色環，非真人。」 (AI-generated virtual character Sehuan, not a real person.)

**Sources**

- BLOCKING: Monthly mean temperature (climate normals) for Taipei and Kaohsiung, November and December, from the national weather agency (its current name is recalled as 中央氣象署, unverified). The operator opens the agency's climate-statistics page, records page title, URL, statistic type, period and capture date, and types the four numbers into slide 4. No number may be typed from memory.
- BLOCKING: The statement implied by the hook that northeast-monsoon days bring damp, cold weather to northern Taiwan: recalled, unverified. The operator confirms it from the same agency's climate or glossary page; if it cannot be confirmed, cut the season wording and keep only the layer logic.
- NO FACTUAL CLAIM: the three-layer order (inner, middle, outer) and the 60/30/10 area split per layer are the studio's own teaching framework, labelled as such.

**The wife rules on**

- Regional wording: 濕冷 for Taipei and the north; is 東北季風天 natural for readers under 35?
- 疊穿 versus 洋蔥式穿搭; 三層順序 and 內層／中層／外層; 以露出的面積來看.
- Whether the caption's second sentence (the framework is not a standard) is too heavy.
- She does not verify the weather numbers (she cannot judge them); the operator does.

**The operator checks**

- BLOCKED until slide 4 and the source slip are filled from the weather agency's page (URL, statistic type, period, capture date, four numbers).
- Confirm or cut the season claim implied by the hook.
- No health, cold-prevention, warmth or fabric-performance wording anywhere (none is used in this draft).
- Persimmon at most one tenth of any slide; alt text set; platform AI label ON.

### P04 · Sat 2026-11-21 18:00 · Threads text · 三步整理・三層順序 (Threads question) (M2)

| Field | Value |
|---|---|
| Queue folder | `pipeline/review-queue/sehuan/2026-11-21_01/` (`sehuan-2026-11-21-01`) |
| Pillar · series · master | P2 氣候穿搭 · 三步整理・三層順序 (Threads question) · M2 |
| Hook (zh-TW, 18 characters) | 出門前，你會先看氣溫，還是降雨機率？ |
| On-screen label | AI 生成｜虛擬角色（純文字貼文，沒有畫面） |
| Flags | AI label **TRUE** · sponsorship flag **false** · type none |
| Caption length | 73 characters (limit about 500, recalled, *unverified*) |
| Status | Ready for review once the media exist (media PENDING; no source blocks it) |

**Caption (zh-TW, DRAFT)**

```
【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布。
問個問題：出門前，你會先看氣溫，還是先看降雨機率？
沒有標準答案，說說你的習慣就好。
```

**Gloss (English, for the operator)**

```
[AI virtual character] This post is published by the AI-generated virtual character "Sehuan".
A question: before going out, do you check the temperature first, or the chance of rain first?
There is no standard answer; just tell us your habit.
```

**Hashtags:** #疊穿

**No image.** Text only; the platform AI label is still switched on by hand.

**Sources**

- NO FACTUAL CLAIM: a question to the audience; it states nothing about weather or clothing.

**The wife rules on**

- The text-only first line drops 「圖像為 AI 生成，並非真人」 because there is no image (bible 8.2 and open item 14; the user must also approve this adaptation).
- Is 先看氣溫／先看降雨機率 the way people say it?

**The operator checks**

- The user approves the text-only first-line adaptation (bible open item 14) before this is scheduled.
- Platform AI label ON even for text (studio rule: every post).
- The caption promises no follow-up post (the earlier draft did, and no such post is scheduled; removed in the independent review). Do not promise one in a reply either.

### P05 · Mon 2026-11-23 20:30 · Instagram carousel · 轉一格 #02 (M3)

| Field | Value |
|---|---|
| Queue folder | `pipeline/review-queue/sehuan/2026-11-23_01/` (`sehuan-2026-11-23-01`) |
| Pillar · series · master | P1 配色公式 · 轉一格 #02 · M3 |
| Hook (zh-TW, 17 characters) | 中性色也有冷暖：灰、米、駝放上色環 |
| On-screen label | AI 生成｜虛擬角色（有色環的頁面）／AI 生成（純圖解的頁面） |
| Flags | AI label **TRUE** · sponsorship flag **false** · type none |
| Caption length | 155 characters (limit about 2200, recalled, *unverified*) |
| Status | Ready for review once the media exist (media PENDING; no source blocks it) |

**Caption (zh-TW, DRAFT)**

```
【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布，圖像為 AI 生成，並非真人。
灰、米、駝色看起來都很「中性」，放上色環就會發現：有的偏暖，有的偏冷。
這篇用三組搭配示意圖比較冷暖並置的差別，只談顏色之間的對比，不談誰適合。
先收藏起來，搭配時可以對照～
螢幕有色差，實際顏色以品牌提供的資訊為準。
```

**Gloss (English, for the operator)**

```
[AI virtual character] This post is published by the AI-generated virtual character "Sehuan"; the images are AI-generated and are not a real person.
Grey, beige and camel all look "neutral", but placed on the colour wheel you see that some lean warm and some lean cool.
This post compares warm and cool neutrals side by side in three styling illustrations. It only discusses contrast between colours, not who something suits.
Save it and compare when you put outfits together~
Screens shift colour; for the real colour, go by the information the brand provides.
```

**Hashtags:** #配色 #色彩 #中性色 #穿搭公式 #AI虛擬角色

**Slides (all drawn by Claude as SVG from Lesson Kit v0 and rendered to PNG, with approved golden-set images placed as supplied files; every zh-TW line is a DRAFT; the operator and the wife review every slide)**

| # | Name | On-screen text (zh-TW, DRAFT) | Gloss | Visual build spec | Badge | Assets |
|---|---|---|---|---|---|---|
| 1 | cover | 中性色也有冷暖／灰、米、駝，放上色環看看／轉一格 #02 | Neutrals have a warm and a cool side too / Grey, beige and camel, placed on the wheel / Turn-one-step #02 | Pale-blush ground; large title; persimmon underline under 「冷暖」; A4 (three-quarter left) cut-out lower-right so the earring shows; badge top-right. | 「AI 生成｜虛擬角色」 | A4 |
| 2 | what a neutral is | 什麼是中性色？／灰、米、駝、炭灰這類彩度低的顏色／彩度低，就是顏色不鮮豔 | What is a neutral? / Colours such as grey, beige, camel and charcoal that have low chroma / Low chroma means the colour is not vivid | A strip of seven muted swatches from the persimmon down to grey, with the four neutrals bracketed. 彩度 (wife rules 彩度 against 飽和度) defined in one plain line. No character. | 「AI 生成」 | none |
| 3 | on the wheel | 放上色環，看它偏哪一邊／偏黃橘那一側＝偏暖／偏藍紫那一側＝偏冷 | Place it on the wheel and see which side it leans toward / The yellow-orange side = leans warm / The blue-violet side = leans cool | A half-wheel (the warm half in full, the cool half in full, muted, circular, numbered positions) with four chips placed by lean: 暖灰, 冷灰, 駝色, 米色. The wheel is a neutral diagram: no headline or label pairs blue with green or blue with white. | 「AI 生成」 | none |
| 4 | same lean | 同一邊的中性色：對比小／暖灰＋駝色＋奶油白 | Neutrals from the same side: low contrast / warm stone + camel + cream | One dress form in generic flats (stone jacket, camel trousers, cream top) with a small persimmon scarf (at most one tenth). Label 「搭配示意」. | 「AI 生成｜搭配示意」 | none |
| 5 | mixed lean | 冷暖並置：對比比較明顯／冷灰＋駝色＋奶油白／轉一格：把暖灰換成冷灰 | Warm and cool side by side: the contrast is more visible / cool grey + camel + cream / Turn one step: swap the warm stone for a cool grey | The same dress form and the same accent; only the jacket changes from warm stone to cool grey (#9A9EA3, a low-chroma slate grey, not a saturated blue). The two forms side by side. Label 「搭配示意」. No verdict words. | 「AI 生成｜搭配示意」 | none |
| 6 | your turn | 換你填／手邊的中性色，你覺得偏暖還是偏冷？／放在一起比一比 | Your turn / Do the neutrals you have lean warm or cool? / Put them side by side and compare | Worksheet: three blank swatch squares with 偏暖／偏冷 tick boxes. No request for photos; no character. | 「AI 生成」 | none |
| 7 | footers | 本篇由明說角色工作室創作與營運。／圖像為 AI 生成，並非真人。／冷暖是配色的說法，這篇只比較顏色，不談誰適合。／螢幕有色差，實際顏色以品牌提供的資訊為準。 | Created and run by Plainspoken Studio. / The images are AI-generated and are not a real person. / Warm and cool is a colour-design convention; this post only compares colours and says nothing about who they suit. / Screens shift colour; for the real colour, go by the information the brand provides. | Small centred type; no new content. | 「AI 生成」 | none |

**AI-generated assets (all PENDING; prompts are in the `shot_prompt` of each media item)**

- **A4** `R02_three-quarter-left_v1`: AI-generated photoreal image of the openly-AI character 色環; label added in post, never generated. Three-quarter view toward the viewer's left (R02), waist-up, outfit A; shows the tucked ear and the colour-wheel earring. Alt text: 「AI 生成的虛擬角色色環，非真人。」 (AI-generated virtual character Sehuan, not a real person.)

**Sources**

- NO FACTUAL CLAIM: warm and cool lean of a neutral is described as a design convention, by comparing the neutral swatches with the wheel in the SVG source file; it is about garments and swatches only, never about skin. Hue positions are read from the hex values by the operator in the editor. If the operator logs a colour-theory reference (gate G7) that defines warm and cool colours, add it here and on slide 7.

**The wife rules on**

- 彩度 against 飽和度; 中性色; 偏暖／偏冷; 冷灰; 暖灰; 駝色.
- Whether 不談誰適合 reads as a clear refusal to match colours to skin (C2) without sounding stiff.
- Whether 「看起來都很『中性』」 sounds natural.
- Colour read: the cool grey must not read as a party colour and the half-wheel must not read as a rainbow.

**The operator checks**

- Hue positions of the four chips read from the SVG source file; the cool grey is a low-chroma slate grey, not a saturated blue.
- No skin, face or body reference anywhere; no colour held against the character (C2).
- A4 shows the tucked ear and the earring with the correct wedge count (inspect at 200%).
- Alt text; platform AI label ON.

### P06 · Tue 2026-11-24 18:00 · Threads image · 轉一格 #02 (Threads version) (M3)

| Field | Value |
|---|---|
| Queue folder | `pipeline/review-queue/sehuan/2026-11-24_01/` (`sehuan-2026-11-24-01`) |
| Pillar · series · master | P1 配色公式 · 轉一格 #02 (Threads version) · M3 |
| Hook (zh-TW, 15 characters) | 三個灰色放在一起，哪一個偏冷？ |
| On-screen label | AI 生成｜搭配示意 |
| Flags | AI label **TRUE** · sponsorship flag **false** · type none |
| Caption length | 82 characters (limit about 500, recalled, *unverified*) |
| Status | Ready for review once the media exist (media PENDING; no source blocks it) |

**Caption (zh-TW, DRAFT)**

```
【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布，圖為搭配示意。
三個灰色放在一起，你覺得哪一個偏冷？
螢幕有色差，同一個顏色在不同螢幕上看起來會不一樣。
```

**Gloss (English, for the operator)**

```
[AI virtual character] This post is published by the AI-generated virtual character "Sehuan"; the picture is a styling illustration.
Three greys side by side: which one do you think leans cool?
Screens shift colour; the same colour can look different on different screens.
```

**Hashtags:** none

**Card (all drawn by Claude as SVG from Lesson Kit v0 and rendered to PNG, with an approved golden-set image placed as a supplied file; every zh-TW line is a DRAFT; the operator and the wife review every slide)**

| # | Name | On-screen text (zh-TW, DRAFT) | Gloss | Visual build spec | Badge | Assets |
|---|---|---|---|---|---|---|
| 1 | three greys | 三個灰色，哪一個偏冷？／A　B　C | Three greys: which one leans cool? / A  B  C | Three equal swatches side by side labelled A, B, C (a warm grey about #B8AEA2, a near-neutral grey, a cool slate grey about #9A9EA3), on the ground colour; no character, no garment. Persimmon underline under the question only. Badge top-right. The order of A, B, C is chosen so the cool one is not always C (here: B). | 「AI 生成｜搭配示意」 | none |

**Sources**

- NO FACTUAL CLAIM: a question to the audience; the three greys are swatches drawn as SVG (one warm, one near-neutral, one cool) whose lean the operator can read from the hex values.

**The wife rules on**

- Is 你覺得哪一個偏冷 natural, and is 灰色 the right word for the swatches?

**The operator checks**

- Record the hex values of A, B, C in the SVG source file so the answer is checkable if a viewer asks.
- No reply in the thread gives a verdict on anyone's screen; the reply template is R9 in reply-guidelines.md.
- Platform AI label ON.

### P07 · Wed 2026-11-25 20:30 · Instagram carousel · 一詞看懂 #01 (M4)

| Field | Value |
|---|---|
| Queue folder | `pipeline/review-queue/sehuan/2026-11-25_01/` (`sehuan-2026-11-25-01`) |
| Pillar · series · master | P4 看懂標示與趨勢 · 一詞看懂 #01 · M4 |
| Hook (zh-TW, 18 characters) | 尺寸表看不懂？先搞懂「平量」兩個字。 |
| On-screen label | AI 生成｜虛擬角色（有色環的頁面）／AI 生成（純圖解的頁面） |
| Flags | AI label **TRUE** · sponsorship flag **false** · type none |
| Caption length | 181 characters (limit about 2200, recalled, *unverified*) |
| Status | **BLOCKED** until the `UNVERIFIED-OPERATOR-TO-FILL` sources are recorded (media also PENDING) |

**Caption (zh-TW, DRAFT)**

```
【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布，圖像為 AI 生成，並非真人。
尺寸表看不懂？先搞懂「平量」和「圍度」兩個詞。
平量是把衣服攤平量出來的寬度，圍度是繞一圈的長度；胸、腰、下擺這類位置，圍度大約是平量的兩倍。
這篇附上空白量法表，數字請填你自己衣服的尺寸，也請看品牌尺寸表旁邊的量法說明。
角色未穿著，合不合身請以品牌提供的尺寸表為準。
```

**Gloss (English, for the operator)**

```
[AI virtual character] This post is published by the AI-generated virtual character "Sehuan"; the images are AI-generated and are not a real person.
Can't read the size chart? Start with two words: 平量 (flat measurement) and 圍度 (circumference).
Flat measurement is the width you get when the garment is laid flat; circumference is the length all the way round. For positions such as chest, waist and hem, the circumference is roughly twice the flat measurement.
This post includes a blank measuring sheet. Fill in the sizes of your own garment, and also read the measuring note next to the brand's size chart.
The character has not worn anything; for whether something fits, go by the size chart the brand provides.
```

**Hashtags:** #尺寸表 #看懂標示 #穿搭 #AI虛擬角色

**Slides (all drawn by Claude as SVG from Lesson Kit v0 and rendered to PNG, with approved golden-set images placed as supplied files; every zh-TW line is a DRAFT; the operator and the wife review every slide)**

| # | Name | On-screen text (zh-TW, DRAFT) | Gloss | Visual build spec | Badge | Assets |
|---|---|---|---|---|---|---|
| 1 | cover | 尺寸表看不懂？／先搞懂「平量」兩個字／一詞看懂 #01 | Can't read the size chart? / Start with the two words 「平量」 / One-word explainer #01 | Pale-blush ground; large title; persimmon underline under 「平量」; A1 cut-out lower-left; badge top-right. | 「AI 生成｜虛擬角色」 | A1 |
| 2 | two words | 平量＝把衣服攤平，量出來的寬度／圍度＝繞一圈的長度 | Flat measurement = the width when the garment is laid flat / Circumference = the length all the way round | A generic shirt flat (no logo, tag or pattern) with a straight dimension line across the chest labelled 胸寬 (平量), and the same chest drawn as a loop with a curved arrow labelled 胸圍 (圍度). Terms 胸寬／胸圍／肩寬／衣長／袖長 are the wife's to confirm. | 「AI 生成｜搭配示意」 | none |
| 3 | the relation | 胸、腰、下擺這類位置：圍度 ≒ 平量 × 2／範例：平量 50 → 圍度約 100／範例數字，非真實商品 | At positions such as chest, waist and hem: circumference ≈ flat measurement x 2 / Example: flat 50 -> circumference about 100 / Example numbers, not a real product | Two bars, one half the length of the other, labelled 50 and 100 (units 公分). The tag 「範例數字，非真實商品」 on the slide. No character. | 「AI 生成」 | none |
| 4 | blank measuring sheet | 空白量法表／胸寬 ＿ 公分｜肩寬 ＿ 公分／衣長 ＿ 公分｜袖長 ＿ 公分／填你自己衣服的尺寸，和品牌尺寸表旁邊的量法說明比一比 | Blank measuring sheet / Chest width __ cm \| shoulder width __ cm / Length __ cm \| sleeve length __ cm / Fill in your own garment's sizes and compare with the measuring note next to the brand's size chart | The flat from slide 2 with four blank dimension lines; no example numbers; no character panel. | 「AI 生成」 | none |
| 5 | what to check on a chart | 看尺寸表，先確認三件事／① 標題寫平量還是圍度／② 單位是公分還是吋／③ 量法說明（每個品牌可能不同） | On a size chart, check three things first / (1) does the heading say flat measurement or circumference / (2) is the unit centimetres or inches / (3) the measuring note (each brand may differ) | Three numbered rows with plain icons (a ruler, a unit mark, a note); no chart of a real brand; no brand name. | 「AI 生成」 | none |
| 6 | your steps | 你的流程／① 把衣服攤平／② 量同一個位置／③ 和尺寸表上的數字比一比（只比數字） | Your steps / (1) lay the garment flat / (2) measure the same position / (3) compare with the numbers on the chart (numbers only) | Three-step strip; no body, no measuring of a person, no tape measure on a body (the tape measure motif belongs to another character); a plain ruler only. | 「AI 生成」 | none |
| 7 | footers | 角色未穿著，合不合身請以品牌提供的尺寸表為準。／範例數字，非真實商品。／資料來源：{頁面名稱}｜{YYYY/MM/DD}（定義）／本篇由明說角色工作室創作與營運。圖像為 AI 生成，並非真人。 | The character has not worn anything; for whether something fits, go by the size chart the brand provides. / Example numbers, not a real product. / Source: {page name} \| {date} (definitions) / Created and run by Plainspoken Studio. The images are AI-generated and not a real person. | Small centred type; the source line is filled from the operator's slip and must not contain braces when exported. | 「AI 生成」 | none |

**AI-generated assets (all PENDING; prompts are in the `shot_prompt` of each media item)**

- **A1** `R01_master_v1`: AI-generated photoreal image of the openly-AI character 色環; label added in post, never generated. Master portrait R01: waist-up, front, outfit A, calm closed-mouth expression, both hands below the frame. Alt text: 「AI 生成的虛擬角色色環，非真人。」 (AI-generated virtual character Sehuan, not a real person.)

**Sources**

- ARITHMETIC ONLY: 50 x 2 = 100. An invented example (flat measurement 50 cm giving a circumference of about 100 cm for an un-stretched loop at a chest, waist or hem position), tagged 範例數字，非真實商品 on screen. Ignores stretch, ease and seams. Recomputed by Claude 2026-10-12; the operator recomputes.
- BLOCKING: The definitions of 平量 and 圍度 and how garment size charts are commonly labelled in Taiwan: recalled, unverified. The operator opens one neutral public source (a national standard or consumer-labelling guidance page; which one applies in Taiwan is unverified) and records its title, URL and the date read; the slide-7 source line is then filled.

**The wife rules on**

- 平量／圍度／胸寬／胸圍／衣長／袖長／肩寬: are these the words readers use, and would readers under 30 know 平量 (bible 10.2 question 4)?
- 合不合身 appears only in the fixed footer line and the caption's last line, as a declined topic.
- Whether the caption's third sentence (about twice) reads clearly.

**The operator checks**

- Fill the definition source (slide 7, sources[]): one neutral public page, title, URL, date. Until then the post is BLOCKED.
- Recompute 50 x 2 = 100; example numbers tagged 範例數字，非真實商品 on slides 3 and 7.
- No brand name, logo or real size table anywhere; the flat is generic.
- A1 is the master R01 (no new generation); alt text; platform AI label ON.

### P08 · Thu 2026-11-26 18:00 · Threads image · 一詞看懂 #01 (Threads version) (M4)

| Field | Value |
|---|---|
| Queue folder | `pipeline/review-queue/sehuan/2026-11-26_01/` (`sehuan-2026-11-26-01`) |
| Pillar · series · master | P4 看懂標示與趨勢 · 一詞看懂 #01 (Threads version) · M4 |
| Hook (zh-TW, 10 characters) | 平量和圍度，差在哪？ |
| On-screen label | AI 生成｜示意圖 |
| Flags | AI label **TRUE** · sponsorship flag **false** · type none |
| Caption length | 100 characters (limit about 500, recalled, *unverified*) |
| Status | **BLOCKED** until the `UNVERIFIED-OPERATOR-TO-FILL` sources are recorded (media also PENDING) |

**Caption (zh-TW, DRAFT)**

```
【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布，圖為示意。
尺寸表上寫「平量」，數字是攤平量出來的寬度，不是繞一圈的長度。
同一個位置，圍度大約是平量的兩倍；量法請看品牌尺寸表旁邊的說明。
```

**Gloss (English, for the operator)**

```
[AI virtual character] This post is published by the AI-generated virtual character "Sehuan"; the picture is an illustration.
When a size chart says 「平量」, the number is the width measured with the garment laid flat, not the length all the way round.
At the same position the circumference is roughly twice the flat measurement; for the measuring method, read the note next to the brand's size chart.
```

**Hashtags:** #尺寸表

**Card (all drawn by Claude as SVG from Lesson Kit v0 and rendered to PNG, with an approved golden-set image placed as a supplied file; every zh-TW line is a DRAFT; the operator and the wife review every slide)**

| # | Name | On-screen text (zh-TW, DRAFT) | Gloss | Visual build spec | Badge | Assets |
|---|---|---|---|---|---|---|
| 1 | label card | 一詞看懂：平量／平量＝攤平量的寬度／圍度＝繞一圈的長度／圍度 ≒ 平量 × 2（範例：50 → 100，範例數字，非真實商品） | One-word explainer: 平量 / Flat measurement = the width laid flat / Circumference = the length all the way round / circumference ≈ flat x 2 (example: 50 -> 100, example numbers, not a real product) | One card on the ground colour: the shirt flat of P07 slide 2 small on the left with the two dimension marks; the three text lines right; persimmon underline under 「平量」. No character panel (so the first line uses 圖為示意). Badge top-right. | 「AI 生成」 | none |

**Sources**

- ARITHMETIC ONLY: 50 x 2 = 100, an invented example tagged 範例數字，非真實商品 on the card (same as sehuan-2026-11-25-01).
- BLOCKING: Definitions of 平量 and 圍度: same neutral public source as sehuan-2026-11-25-01; the operator records it once and reuses the slip.

**The wife rules on**

- Same terms as sehuan-2026-11-25-01; the Threads text is shorter.

**The operator checks**

- Same definition source as the Instagram post; BLOCKED until it is recorded.
- Card numbers equal the Instagram slide 3 numbers.
- Platform AI label ON.


---

## 6. Weeks 3 and 4, and days 29 and 30: outlined (P11 to P18, P21, P22)

This table holds the ten outlined posts that stay in the 30 days. P09, P10, P19 and P20 were outlined here before OPS-D1 and now sit in section 6.1. Each outlined post will be written to the same depth as section 5 after the week-2 review of the first batch's minutes and the wife's first rulings. Source needs are stated now so the operator can open the pages early. Hooks refer to `hook-library.md`.

| ID | Date, time | Platform, format | Master and series | Hook (zh-TW) | Outline | Source needs | Cautions |
|---|---|---|---|---|---|---|---|
| P11 | Wed 2026-12-02 20:30 | IG carousel | M6 · B1 三層順序 #02 · P2 | H15 冷氣房外套怎麼選色：辦公室、捷運、電影院 | Pick the colour of a layer by its relation to the base outfit (same lean, or contrast) rather than by the room; three 示意 plates (office, MRT exit, cinema) drawn as SVG that never contain her | None for the logic. Plates: Taiwan details per bible 4.8; if any number appears, a weather-agency slip | **No MRT map, station name or line colour.** No warmth, cold or health wording (not 保暖, not 怕冷). Wife checks plate details |
| P12 | Thu 2026-12-03 18:00 | Threads text | M6 · B1 (question) | H42 冷氣房裡的外層，你會選同色系還是撞色？ | One question, text only | None | Needs gate 17 |
| P13 | Fri 2026-12-04 20:30 | IG carousel | M7 · C 一詞看懂 #02 · P4 | H30 色差是什麼：螢幕上的顏色為什麼不同？ | Screens differ; photos depend on light; the colour name and the brand's information prevail; compare on two screens; blank checklist | A named public source on display and lighting differences, or the post stays at "screens differ, go by the brand's information" | No brand, no photo of a real product; no price or discount; lands before 雙12 |
| P14 | Sat 2026-12-05 18:00 | Threads image | M7 · C (Threads) | H36 色名一樣，螢幕上的顏色一樣嗎？ | Label card: the colour name outranks the screen colour | As P13 | No claim about any device |
| P15 | Mon 2026-12-07 20:30 | IG carousel | M8 · B2 三關檢查 #01 · P3 | H22 聖誕與跨年派對：亮色點綴的比例 | Three checks: what the invitation says (the host's request prevails), the accent as at most one tenth, the shoe colour joins the outfit; red and green only in a neutral layout; no all-white or all-black example | General etiquette line (一般禮儀整理，請以主辦方的要求為準); a fashion contact sanity-checks (gate 16) | No slogan overlay on red and green; no 開運 or lucky-colour wording; dates 聖誕 Fri 12-25 and 跨年 Thu 12-31 are *computed* |
| P16 | Tue 2026-12-08 18:00 | Threads image | M8 · B2 (Threads) | H26 派對的亮色點綴，你會放在配件還是外套？ | Card of the three checks plus a question | As P15 | Question only |
| P17 | Wed 2026-12-09 20:30 | IG carousel | M9 · A 轉一格 #03 (chips follow publication order; it was #04 while M5 was in the plan) · P1 | H07 色環上相鄰與相對：三種關係一次看 | Three relationships on the 12-position wheel (adjacent, one step apart, opposite) shown on garment flats; positions numbered, no colour-pair headline; turn one step | **The colour-theory reference (gate 11)** for the terms 類似色 and 互補色 | First post to show opposite colours: the wife judges the colour read of every pair; no 藍綠, 藍白 or 紅配綠 wording; no verdict on taste |
| P18 | Thu 2026-12-10 18:00 | Threads image | M9 · A (Threads) | H12 兩個顏色，在色環上隔幾格？ | Quiz card with two chips and a numbered wheel | As P17 | Question only |
| P21 | Mon 2026-12-14 20:30 | IG carousel | M11 · B2 三關檢查 #02 · P3 | H21 尾牙穿搭，先過三關：場合、顏色、鞋子。 | Occasion (the host's dress note prevails), colour (why all-white and all-black are commonly avoided at celebrations, the wife's wording), shoes; three example outfits each with a second colour | General etiquette line; wife's taboo ruling; fashion-contact sanity check (gate 16). 尾牙 date Sat 2027-01-23 is *computed* | No set of four; no gift framing; no claim that "everyone" does or avoids something; the wife confirms north–south differences (bible 10.2 question 14) |
| P22 | Tue 2026-12-15 18:00 | Threads image | M11 · B2 (Threads) | H44 尾牙穿搭的三個檢查點 | Card of the three checks | As P21 | Day 30 |

### 6.1 Deferred by OPS-D1 (P09, P10, P19, P20; masters M5 and M10)

**The decision.** OPS-D1, adopted for the user on 2026-10-12 (`DECISIONS.md`; `ops/weekly-routine.md` section 2.4), holds the three pilots at 12 approvals a week combined through the first 8 weeks, which is 4 a week for 色環 (2 Instagram + 2 Threads). Weeks 3 and 4 therefore lose one master each: 4 of the 22 slots (2 Instagram, 2 Threads). The choice of which masters is Claude's, is reversible, and is for the operator and the wife to overrule. A deferred post is not deleted: its outline stays here, it has no queue folder, its hook row in `hook-library.md` is marked, and nothing about it is scheduled or approved.

**How the two were chosen** (*assumption*; no engagement data exists, so this is judgement, not a finding):

1. **A master is cut whole**, Instagram and Threads together. That keeps the Instagram-against-Threads pair test (H2) intact for every master that stays and saves the whole master's drawing, review and approval, not half of it.
2. **The primary platform keeps 2 posts a week** in every week (Instagram: W3 Wed and Fri; W4 Mon and Wed), the floor in the decision.
3. **Weeks 3 and 4 keep one master of each pillar** (M6 P2, M7 P4, M8 P3, M9 P1), so the week-6 comparison of series still has data on all four pillars (`series.md` section 6).
4. **M5 (P1, 同色系：只改明暗) goes first** because it is the third colour-formula lesson after M1 and M3 and the least distinct: "the formula stays, one thing changes" is the Series A format itself, M1's slide 5 already shows it with the accent hue, and M5 would show it again with lightness. It is also the cheapest, needs no outside source and is safe in any week, which is why it is the first to restore.
5. **M10 (P2, 雨天褲長與鞋色) goes second** because it carries the most cautions for the least lesson: its Friday and Saturday sit on 雙12 (no buying wording, shoes never framed as a gift), it needs two Taiwan street plates (騎樓, bus shelter) that the wife must check, and a weather slip if any number appears. Its pillar P2 is already covered by M2 and M6.

The alternative that was weighed: cut M7 (色差) instead of M5. It keeps a source-free post and a Monday restart on 11-30, but it removes the only P4 master in weeks 3 and 4 and the only post that lands before 雙12. The pillar shares come out the same distance from the bible target either way (11 percentage points in total, computed from the rounded shares), so the tie was broken on lesson value. Overrule it if the wife or operator reads the value differently.

| ID | Was | Platform, format | Master and series | Hook | Why it goes | Restore |
|---|---|---|---|---|---|---|
| P09 | deferred (was Mon 2026-11-30 20:30) | IG carousel | M5 · A 轉一格 #03 · P1 | H06 同色系怎麼配：只改明暗的三種示意 | Third colour-formula lesson in a row and the least distinct; cheap and source-free, so the first to restore | First, when a third weekly slot is allowed |
| P10 | deferred (was Tue 2026-12-01 18:00) | Threads image | M5 · A (Threads) | H41 三種明度，你會把哪一格放在外層？ | Pair of M5; Threads version of the same ladder | With P09 |
| P19 | deferred (was Fri 2026-12-11 20:30) | IG carousel | M10 · B1 三層順序 #03 · P2 | H16 雨天褲長與鞋色：一張圖看配色比例 | Most cautions per lesson (the day before 雙12, shoes near gift taboos, two street plates for the wife to check); P2 is covered by M2 and M6 | Second, when a further slot is allowed |
| P20 | deferred (was Sat 2026-12-12 18:00) | Threads text | M10 · B1 (question) | H43 雨天褲腳，你會選到腳踝還是更長？ | Pair of M10; it would sit on 雙12 itself and needs gate 17 | With P19 |

**Effects.** (1) The 30 days hold 18 posts, not 22 (sections 2 and 3). (2) The account is silent Fri 11-27 to Tue 12-01 (section 2). (3) Nothing is scheduled on 雙12 or the day before. (4) Gate 17 (the text-only first line) is needed for P04 and P12 only. (5) The Series A table in `series.md` loses the "same family by lightness" episode, and M9 becomes 轉一格 #03.

**Restore order**, if logged minutes show room (the ramp rule of `ops/weekly-routine.md` 2.4, which plans no step up before the week-8 review on Thu 2027-01-14): **M5 first, M10 second.** A restored post keeps its ID and weekday and moves by whole weeks if its November or December date has passed, takes a queue folder named for its new date, is drafted to the depth of section 5 and goes through the same review; nothing here pre-approves it. If it is restored, `verify.py` must be edited so the 30-day table may hold it again.

---

## 7. Shared blocks

### 7.1 Golden-set assets used in the 30 days

All AI-generated images of 色環 come from the golden set (addendum 11): **no new face is generated for a post**. A crop or colour correction is a logged human edit; skin smoothing, brightening and hand repair are banned; an object-only repair of the earring or a chip card is allowed (addendum 11 item 6). Hands stay out of frame or in pockets (addendum 5.1). The R01 prompt is carried in full in the `shot_prompt` of `sehuan-2026-11-18-01` (asset A1) and referenced elsewhere.

| Code | Golden-set file | Framing | Used in | Prompt location |
|---|---|---|---|---|
| A1 | `R01_master_v1` | Waist-up, front, outfit A, calm closed-mouth face, hands below the frame | P01 (cover), P07 (cover), later covers | Full text in P01 media[0]; pack 2.1 (Gemini) and 2.2 (ChatGPT) |
| A2 | `R08b_knees-up_v1` | Knees-up, hands in pockets, chip ring at the left hip (needs `R12_chip-ring_v1` as an object reference) | P01 (identity slide) | P01 media[1]; pack 4.3 and 4.1 |
| A3 | `R13_glance_v1` | Waist-up glance toward the lesson | P01 (formula slide), P03 (cover) | P01 media[2]; pack 4.4 |
| A4 | `R02_three-quarter-left_v1` | Three-quarter toward the viewer's left; shows the tucked ear and the earring | P05 (cover) | P05 media[0]; pack 3.4 |
| A5 | `EXP_E05_*_v1` | Mild-smile headshot, 1:1 | P02 (small panel) | P02 media[0]; pack 4.2 |
| (R06) | `R06_headshot_v1` | Headshot, the face lock for the E-series | Reference for A5 | Pack 3.4 |
| (R12) | `R12_chip-ring_v1` | Object still, no person | Reference for A2 | Pack 4.1 |

Needed later in weeks 3 and 4 (not yet written into drafts): E02 (explaining), E04 (comparing), E07 (careful) and E09 (pleased, light) headshots for Threads cards, and R03 (three-quarter right) as a cover variant. **Not used in the 30 days:** outfits B and C and the season variants V1 to V3 (R09, R10). Reason: a season outfit on a climate post risks reading as "she dressed for the weather" (bible 4.3 and addendum 4.2 forbid that reading); the lessons use flats on a dress form, drawn as SVG, instead. The golden set is generated one pilot per fortnight starting with 方寸 (`HUMAN_TODO.md` 34); 色環's set follows 方寸's and 步驟's, so **the earliest realistic first post depends on that order** (section 8).

### 7.2 Lesson Kit v0 (the diagram layer, drawn by Claude as SVG)

**Route (decision D3, 2026-10-12).** Everything that carries a word, a number, a diagram, a garment drawing or a badge is **drawn by Claude as SVG** (vector code, directed by the operator and the wife, no image model) and **rendered to PNG with headless Chromium** (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, present in the sandbox on 2026-10-12). This is the route used for the superseded 步驟 art (`DECISIONS.md` 2026-10-11). It removes the build step from the operator; it removes **no** review step. **The operator and the wife still review and approve every asset; drawing a slide does not approve it.** Claude cannot edit video, so a Reel's cut, timing and sound are a human job. **No image generator is asked for text, numerals, flats, wheels or badges** (bible C9; addendum 7). Because Claude is an AI, these graphics are AI-made: the badge on every lesson slide stays (「AI 生成」, or 「AI 生成｜搭配示意」 and 「AI 生成｜示意圖」 where bible 8.3 requires them), and provenance logs them as Claude-drawn SVG, not as image-model output.

**Status: not yet drawn.** The kit below is a specification. No SVG or PNG exists for any post yet (every media item is PENDING). The first drawing job is the kit itself (about ten flats, the dress form, the 12-position wheel, the proportion bar, the chip ring, the badge pill, the worksheet and footer blocks, the carousel and card templates), followed by the slides of P01 and P02 for review.

| Part | Spec (*assumption* unless marked) |
|---|---|
| Canvas | Instagram carousel 4:5 (1080 x 1350 px is the size I recall; *unverified*, check in the app). Threads image 4:5 as well. All slides in a post share one size |
| Colour tokens | Ground pale blush `#F2DAD2`; cream `#F4E8DF` (garments and light panels); warm stone `#B8AEA2`; charcoal `#3A3735` (type and lines); persimmon `#CD8B6A` (one accent, at most about one tenth of any slide); dusty rose `#C27F80` and soft violet `#9F8AAB` as extra accent fills at the same cap; the 12 wheel hues of bible 4.4. Use the cream, not the mist `#E4D6CB`, for a light panel (the mist is only 4.6 from the ground, bible integration log item 4) |
| Contrast | Charcoal on the ground 8.85:1 and on cream 9.82:1 (*computed*); cream text on a charcoal badge 9.82:1 (*computed*). **Persimmon on the ground is 2.10:1 (*computed*): fills and underlines only, never text** |
| Type | A Taiwan-glyph (TC) font such as Noto Sans TC, language tag `zh-TW`; the commercial licence is read before use (bible G14, licence terms *unverified*). **The render sandbox has no Noto Sans TC** (checked 2026-10-12 with `fc-list`: only WenQuanYi Zen Hei and Unifont JP are installed, and neither is a Taiwan-glyph reference). Final slide text is therefore not rendered until the operator supplies the licensed font file; any render before then is a layout preview, and the wife checks glyph shapes by eye. Title 72 to 96 px, body at least 44 px, footers at least 32 px (*assumption*; test on a phone). Up to 3 lines per slide and about 14 characters per line (bible 3.1) |
| Badge | Solid charcoal pill with cream text; text height at least 3.5% of the image height (47 px on 1350, *computed*); inset at least 8% of the width from the sides (86 px) and 11% of the height from top and bottom (149 px) (*computed*; centred 1:1 crop of 4:5 removes 10% top and bottom); **same corner (top-right) on every slide**. Wording: 「AI 生成｜虛擬角色」 on slides that show her; 「AI 生成」 on lesson slides without her; 「AI 生成｜搭配示意」 and 「AI 生成｜示意圖」 where bible 8.3 requires them. Typeset, never generated; the "first second only" option is not used (addendum 8.2) |
| Garment flats library v1 (bible G9) | About ten generic flats drawn from scratch as SVG paths (not traced from a brand photo): open blazer, crew-neck knit, tee, collared shirt, sleeveless vest, midi skirt, wide trousers, straight trousers, long open knit coat, scarf, tote. No logo, tag, label, pattern, stripe, check or recognisable branded silhouette; plain buttons; fills recoloured by hex. QA: no invented garment detail (the FAS1 tripwire) |
| Dress form (人台) | Faceless, headless, a plain neutral form; never the character; she is never placed on it or in a taught outfit (bible C1) |
| Wheel diagram | 12 equal wedges, muted hues, **circular**, positions numbered 1 to 12 (position 8 named 青 only if the wife agrees; never the pair 藍綠), saturation never above the persimmon's; no six-stripe horizontal colour bar anywhere (bible C4) |
| Proportion bar | A horizontal bar drawn to scale (6:3:1 for the formula posts); three segments only |
| Chip ring | Exactly six blank cards on a charcoal ring; no text, number or code |
| Character images | Claude places an approved golden-set file in the SVG **as supplied**: a framed panel (rounded rectangle, no shadow trick) by default, or a transparent cut-out only if a human has made one. A cut-out is a human edit; addendum 11 item 6 does not list it (crop, colour correction, stray mark, badge and text, object-only repair), so the wife and operator decide whether to add it. Claude does not cut out hair edges. Where a slide spec in section 5 says "cut-out", read "supplied cut-out or framed panel". Hair edge checked at 200%; a halo or a hard edge fails; placed lower-left on covers and in a panel on lesson slides; never composited into a photoreal scene |
| Alt text | A per-slide zh-TW line that starts 「AI 生成的…」 and says 「非真人」 whenever she is in the picture (for example 「AI 生成的虛擬角色色環，非真人；…」); each media description in `post.json` ends with its alt text; the wife reads them |
| Review and provenance | The operator reviews every rendered PNG (numbers copied from the source slip, bar drawn to scale, persimmon at most one tenth, badge corner and inset, 1:1 crop test, safe zones) and the wife reads every character and the colour reads, before either sets a review field. Claude keeps the SVG source beside the render and logs each render in `assets/provenance.csv` the way the code-drawn 步驟 art was (tool 「Claude (code-drawn SVG, no image model)」, model = the script or file and version). Copyright status of code-authored art in Taiwan is *unverified* (a lawyer question, as the existing row for the 步驟 art says) |
| Layout checks | Two screens; a nine-tile grid test (the grid must not read as one saturated colour); party-colour, rainbow and mourning reads by the wife; nothing sits where the platform's own controls cover it (safe zones *unverified*) |
| Election window layouts (weeks 1 and 2) | No blue, green, teal or yellow headline or cover; no camp pair; no slogan layout; no flags, red stars or party symbols |

### 7.3 Disclosure and label strings (all DRAFT for the wife)

| Use | zh-TW (DRAFT) | Gloss |
|---|---|---|
| Bio, Instagram (bible 8.1) | AI 虛擬角色｜色環｜配色、穿搭公式與台灣氣候疊穿說明｜圖為搭配示意，角色未穿著商品｜明說角色工作室 創作與營運 | AI virtual character / Sehuan / colour, outfit formulas and Taiwan-climate layering explained / images are styling illustrations; the character has not worn any product / created and run by Plainspoken Studio |
| Bio, Threads | AI 虛擬角色｜色環｜配色與穿搭邏輯說明｜圖為搭配示意｜明說角色工作室 創作與營運 | Shorter version |
| Display name | 色環｜AI 虛擬角色 | |
| First line, any post that shows her (addendum 8.2) | 【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布，圖像為 AI 生成，並非真人。 | |
| First line, lesson card without her | 【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布，圖為搭配示意。 | |
| First line, label card without her | 【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布，圖為示意。 | |
| First line, text only (needs user approval) | 【AI 虛擬角色】本篇由 AI 生成的虛擬角色「色環」發布。 | |
| Badge | 「AI 生成｜虛擬角色」, 「AI 生成」, 「AI 生成｜搭配示意」, 「AI 生成｜示意圖」 | See the wording note under the table |
| Badge, Reel with a still of her (D6; none is planned) | 「AI 生成｜虛擬角色」 on every frame for the whole clip | Persistent, typeset, never generated; inset at least as in `pipeline/qa-checklist.md` D3 (11% top and bottom, 8% sides); 9:16 safe zones are *unverified* (QA T7) |
| First line, Reel with a still of her (D6; none is planned) | The same line as "any post that shows her" | 色環 has no YouTube presence in the pilot (`series.md` section 1), so there is no Short and no 「本影片…」 variant |
| Colour footer | 螢幕有色差，實際顏色以品牌提供的資訊為準。 | Bible 8.8 says 官方; the pipeline checker treats 官方 as a source-dependent claim, so the wording is 品牌提供. The wife rules |
| Size and fit footer | 角色未穿著，合不合身請以品牌提供的尺寸表為準。 | Bible 8.8, same change |
| Etiquette line (P3) | 一般禮儀整理，請以主辦方的要求為準。 | |
| Climate data line (P2) | 氣象資料來源：{氣象署頁面名稱}｜{城市}｜{YYYY/MM/DD}。僅供搭配示意，非天氣預報，最新預報請見氣象署。 | |
| Example numbers | 範例數字，非真實商品。 | |
| Correction | 【更正】{YYYY/MM/DD}：{內容}已更新為「…」。原說明有誤。 | |
| Automated reply (none in the first 30 days) | 這是自動回覆訊息。我是 AI 虛擬角色，由明說角色工作室創作與營運。 | |
| Paid, gifted, affiliate, client lines | Not used in the 30 days. Kept in bible 8.5 to 8.7 | |

**Badge wording note.** Addendum 8.2 and `pipeline/qa-checklist.md` D3 agree on 「AI 生成｜虛擬角色」 for anything that shows her, and that is also the wording decision D6 fixes for a Reel or Short, so D6 changes no string. They differ on diagrams: the QA checklist names 「AI 生成｜示意圖」, while addendum 8.2 and this calendar use 「AI 生成」 on lesson slides without her and keep 「搭配示意」 and 「示意圖」 as in bible 8.3. That difference is older than D6 and is left as it was; the wife rules. In a Reel the one persistent badge 「AI 生成｜虛擬角色」 stays on every frame, including frames with only a diagram, so the badge never changes mid-clip.

Platform label: **ON for every post**, including text posts and flat-only cards (studio rule). Instagram and Threads also get the account-level "AI-generated profile" label if it exists for a Taiwan account (gate 5). Never strip metadata or a tool's visible mark; save downloads untouched (addendum 8.2).

### 7.4 Source-slip convention

- Every `sources[]` entry is `{claim, url, date}`. A claim that depends on an outside page carries that page's real URL and the date it was read. Until the operator has opened the page the entry says `UNVERIFIED-OPERATOR-TO-FILL` and the post is blocked.
- An entry that makes no outside claim starts with `NO FACTUAL CLAIM` or `ARITHMETIC ONLY` and may have an empty URL and date.
- One slip per master, in the form of bible 10.3 (the FAS1 fact-check slip). Re-check due: data at 90 days, climate numbers at the season change (*assumption*).
- Numbers on an image are copied from the saved page, never typed from memory. Example numbers carry 範例數字，非真實商品.
- Every colour proportion is labelled 口訣（經驗法則）. The word 「常見」 is used only if the G7 reference confirms it.

### 7.5 Publishing checklist (the operator, per post)

1. `queue.py validate` shows no ERROR or FLAG, and every WARN has been read.
2. `sources[]` has no placeholder; the slip is complete; the image numbers equal the page.
3. All media generated or rendered, logged in `assets/provenance.csv` the same day (a Claude-drawn SVG is logged as such, section 7.2), and `media[].path` updated to the final file.
4. Inspection at 100% and 200% (hands, earrings, wedges, ears, text); the badge is present, in the same corner, and not croppable; alt text set.
5. Two-screen colour check and the three colour reads (party, rainbow, mourning) by the wife.
6. The wife has set `wife_language`; the operator has set `operator_facts`; only then does a human set `approved` (Claude never does).
7. Not 228, polling day, an active disaster, 清明 or another subdued day; the sponsor ledger shows no sponsor (none in the 30 days).
8. Schedule with the platform's own tool; switch on the platform AI label by hand; screenshot the four disclosure places (bio, first line, badge, platform label).
9. After posting: reply only through approved templates; hide political and sexualised comments; count 「是真人嗎」 comments for the week (five or more triggers the stronger label within 48 hours, `portfolio.md` 6.2).
10. Log operator and wife minutes (section 8), **including the operator's review minutes per rendered asset**, which are the new unknown after decision D3.
11. A Reel or Short with a still of her (decision D6; none is planned): check all four conditions on the exported file and on the scheduled preview: platform AI label on; badge 「AI 生成｜虛擬角色」 on every frame for the whole clip; no blinking, lip-sync or morphing of the face (a slow pan or zoom of the still is the only motion); no synthetic voice (captions or human-recorded sound only; platform-library music only after bible G13 is checked). Claude does not edit video, so a human cuts it. Then the usual review.

### 7.6 Review-queue map

| Post | Folder under `pipeline/review-queue/sehuan/` | Status on 2026-10-12 |
|---|---|---|
| P01 · sehuan-2026-11-18-01 | `2026-11-18_01/` (`post.json`, `media/.gitkeep`) | Media PENDING; review pending / pending / not approved |
| P02 · sehuan-2026-11-19-01 | `2026-11-19_01/` (`post.json`, `media/.gitkeep`) | Media PENDING; review pending / pending / not approved |
| P03 · sehuan-2026-11-20-01 | `2026-11-20_01/` (`post.json`, `media/.gitkeep`) | Blocked on a source; also media PENDING; review pending / pending / not approved |
| P04 · sehuan-2026-11-21-01 | `2026-11-21_01/` (`post.json`, `media/.gitkeep`) | Media PENDING; review pending / pending / not approved |
| P05 · sehuan-2026-11-23-01 | `2026-11-23_01/` (`post.json`, `media/.gitkeep`) | Media PENDING; review pending / pending / not approved |
| P06 · sehuan-2026-11-24-01 | `2026-11-24_01/` (`post.json`, `media/.gitkeep`) | Media PENDING; review pending / pending / not approved |
| P07 · sehuan-2026-11-25-01 | `2026-11-25_01/` (`post.json`, `media/.gitkeep`) | Blocked on a source; also media PENDING; review pending / pending / not approved |
| P08 · sehuan-2026-11-26-01 | `2026-11-26_01/` (`post.json`, `media/.gitkeep`) | Blocked on a source; also media PENDING; review pending / pending / not approved |

All eight validate with no ERROR and no FLAG; the warnings are the placeholders that block approval. Nothing in them is approved. Posts P11 to P18, P21 and P22 have no folder yet, and P09, P10, P19 and P20 are deferred by OPS-D1 (section 6.1) and will have none unless they are restored. **Keeping this file and the drafts in step:** the captions, hooks and slide text in section 5 and in the `post.json` files were generated from one data file and are identical today. After a human edit, `post.json` is the master (the review queue reads it) and this section must be edited to match; since the 2026-10-12 review `python3 content/sehuan/verify.py` prints a WARN when a post.json hook, caption or gloss no longer appears verbatim in this file.

---

## 8. Effort and capacity (the main risk in this calendar)

`portfolio.md` 5.1 to 5.3 budgets 5 minutes of operator time per approval and 10 minutes of the wife's time per master. It has **no line for the lesson graphics**. In v0.1 of this file that gap was filled by operator build time (a human drawing flats, a dress form and a wheel in a design tool). **Decision D3 (2026-10-12) moves the drawing to Claude** (SVG rendered to PNG, section 7.2), so the operator's build minutes fall to zero; **the operator's review minutes per asset do not**, and become the new unknown. **Decision OPS-D1** holds 色環 at 4 approvals a week. The figures below are *assumptions*, none measured; the sums are *computed*.

### 8.1 Assumptions

| Item | v0.1 (human-built, 3 + 3 from week 3) | Now (D3 and OPS-D1) | Basis |
|---|---|---|---|
| Lesson Kit v0, one time, operator | 5 h build (range 3 to 8) | **0 min build; 60 min review** (range 30 to 90) | Claude draws the kit; the operator checks it once against section 7.2. The review time is an assumption |
| Lesson Kit v0, one time, wife | none counted | **30 min** (range 15 to 45) | The wheel's colour reads, the badge, the template text. Assumption |
| Golden set for 色環, one time | 7 to 9 h hands-on over three sittings | **unchanged** | Photoreal images are made by hand in Gemini or ChatGPT (Claude cannot make them); pack 0 and addendum 12.3 item 7 |
| One 7-slide carousel, operator | 60 min build (40 to 90) | **0 build; 20 min review** (low case 10) | Open 7 PNGs at phone size and on a desktop screen, check numbers against the slip, the bar to scale, the badge corner and inset, the 1:1 crop test, request redraws. 20 is the top of the v0.1 "15 to 20" range for import, check and export; the low case is about 1.5 min a slide |
| One Threads card, operator | 15 min build | **0 build; 5 min review** (low case 3) | One image, same checks. A text-only Threads post has no asset to review |
| Operator approval | 5 min per post | 5 min per post | `portfolio.md` 5.1. It already contains some media checking, so booking the asset review on top of it is **conservative** |
| Redraw rounds | inside the 36-minute rework reserve | inside the 36-minute rework reserve | A change request costs Claude a redraw and the operator one re-check, not a build |
| Wife review | 10 min per master + 3 min for the second platform + about 1 min per slide | unchanged | `portfolio.md` 5.1; per-slide figure from v0.1. She still reads every character; the sandbox renders with a non-Taiwan-glyph font until the operator supplies one (section 7.2), so she also checks glyph shapes |

### 8.2 Weekly load for 色環 alone (operator, minutes)

Worst case per week: 2 carousels and 2 cards (a week with a text-only Threads post is 5 minutes lighter).

| Case | Asset time | Approvals | Total | Share of 360 |
|---|---|---|---|---|
| v0.1, weeks 1 and 2 (4 approvals): 2 x 60 + 2 x 15 build | 150 | 4 x 5 = 20 | **170** | 47% |
| v0.1, weeks 3 and 4 at 3 + 3 (6 approvals): 3 x 60 + 3 x 15 build | 225 | 6 x 5 = 30 | **255** | 71% |
| D3 only, weeks 3 and 4 at 3 + 3: 3 x 20 + 3 x 5 review | 75 | 30 | **105** | 29% |
| **Now, every week (D3 and OPS-D1), planning case**: 2 x 20 + 2 x 5 review | **50** | 20 | **70** | **19%** |
| Now, low case: 2 x 10 + 2 x 3 review | 26 | 20 | **46** | 13% |

What each decision saves in weeks 3 and 4: D3 saves 255 - 105 = 150 minutes and OPS-D1 saves 105 - 70 = 35 (one carousel review 20, one card review 5 and two approvals 10), 185 in all. In weeks 1 and 2 only D3 applies: 170 - 70 = 100 minutes. Over the 30 days (4 full weeks plus the 2 posts of days 29 and 30) the planning case is 4 x 70 + (20 + 5 + 2 x 5) = **315 minutes (5.25 h)**, against 2 x 170 + 2 x 255 + (60 + 15 + 2 x 5) = 935 minutes (15.6 h) in v0.1, which is the build time the operator no longer carries; the one-time kit falls from 5 h of building to 1 h of review.

**All-in operator minutes per approval** (`portfolio.md` 6.1 effort row: 8 or less Scale-eligible, 12 or less Keep, over 12 to 15 Fix, over 15 after one redesign Retire-review, which is the effort breach of 6.3): planning case 70 / 4 = **17.5**, low case 46 / 4 = **11.5**. The planning case is above the breach line and the low case is just inside Keep, so **which figure is true decides whether 色環 alone fits**; the wife's minutes are not in this number, and rework is outside it. This is the reason to log review minutes from the first post.

### 8.3 Against the shared plan

`portfolio.md` 5.3 plans 250 operator minutes for weeks 1 and 2 (12 approvals) with 110 minutes of reserve and slack, of which 36 is the rework reserve; its weeks 3 to 8 column (18 approvals, 300 planned, 60 slack) is **not used** under OPS-D1, which keeps the three pilots on the 250 / 110 column. 色環's asset review (50 minutes, planning case) is not in the 250, because the portfolio has no graphics line, and takes **45% of the 110** (50 / 110), leaving 60, or 24 after the rework reserve. If the other two pilots needed asset review of the same size (not known; their calendars hold their own figures), three pilots would need 3 x 50 = 150 minutes, more than the 110 minutes of slack; at the low case, 3 x 26 = 78 fits in 110 but not in the 74 left after the reserve. **Review time, not build time, is therefore the operator's binding graphics constraint**, and the portfolio's cut list (`portfolio.md` 5.6) stays the fallback. For the wife, OPS-D1 returns the three pilots to the 363-minute column (147 minutes of headroom to her 510 gate) instead of the 402-minute column (108 minutes). Her own load for 色環 in weeks 3 and 4 is 2 x 10 + 2 x 3 = 26 minutes of draft review plus 2 x 7 = 14 minutes reading slides, **40 a week**, against 3 x 10 + 3 x 3 = 39 plus 3 x 7 = 21, **60 a week**, at 3 + 3.

### 8.4 What would make it fit (the operator decides)

1. **Claude draws Lesson Kit v0 as SVG and renders the slides: adopted (D3).** It needs the operator's font file and licence read (gate 10) and one kit review.
2. **Hold at 4 approvals a week: adopted (OPS-D1).** M5 and M10 are deferred (section 6.1) and come back first if minutes show room.
3. **Shorten the carousels to 5 slides** (cover with identity folded in, rule, examples, your turn, footers): not adopted. It now saves review and the wife's reading time rather than build time; if review scales with slides, 20 x 5 / 7 = about 14 minutes, a saving of about 6 minutes (29% fewer slides) per carousel.
4. **Reuse one dress-form layout** for every post and change only the flats' fill colours: built into the SVG kit by design (`series.md` section 2), which also makes each review quicker.
5. **Cut the Threads cards to text questions** in a given week: still available; saves 5 minutes of review per card (the portfolio floor is 2 posts a week per live persona, `portfolio.md` 5.4).
6. **Start later.** If the golden set, the kit and the sources are not ready, move W0 by whole weeks (section 1). A late start is cheaper than a rushed first post.

**Measure before trusting any of this:** log the operator's **review minutes per rendered asset**, the approval minutes and the wife's minutes for the first nine masters of the 30 days (ten if M5 is restored) (`HUMAN_TODO.md`, bible open item 25). If the all-in operator minutes per approval exceed 12 (`portfolio.md` 6.1 Keep level), apply the cuts in `portfolio.md` 5.6.

---

## 9. Open items for the human

1. **Gates 3, 10, 12, 13, 14.** The golden set, Lesson Kit v0 (now Claude's to draw, the operator's and wife's to review), the weather source, the size-term source and the polling-day date decide when P01 to P08 can be approved. P03, P07 and P08 are blocked by design until their sources are recorded.
2. **Supply a Taiwan-glyph font file whose licence has been read** so that Claude can render final slide text (section 7.2, gate 10), and **book the operator's review time** for the kit and every rendered asset (section 8). Authorising Claude to draw the kit is settled by D3; the review minutes (planning case 20 per carousel, 5 per card) are the largest remaining unknown in the operator's hours.
3. **Reconcile the three pilot calendars.** The three were written in parallel. This calendar's slots were checked against the other two as they stood on 2026-10-12 after each had been updated for OPS-D1 (no shared clock hour; section 2 and check 11 in section 10). Confirm the first-post days (方寸 Mon 11-16, 色環 Wed 11-18, 步驟 Thu 11-19) and decide whether 方寸's Friday Short on 11-27 and 步驟's Sunday posts on 11-29 should move out of the election-eve and day-after quiet days that this calendar keeps.
4. **Approve the text-only first line** for Threads text posts (P04 and P12; P20 is deferred) or ask for a different wording (bible open item 14).
5. **Confirm the quiet block Fri 11-27 to Sun 11-29** and the hard stop on Sat 11-28 once the Central Election Commission date is read.
6. **Wife's rulings** (each post's notes list the specifics): colour names (柿子橘, 灰玫瑰色, 灰紫色, 紅橘色, 冷灰, 暖灰, 駝色, 中性色, 彩度 against 飽和度); 平量, 圍度, 胸寬, 胸圍; the J2 line; 六成 against 60%; the closing ～ in captions; 品牌提供 against 官方; 疊穿 against 洋蔥式穿搭; 濕冷 and 東北季風天; the bible's pillar title P3-4 (面試穿搭的顏色選擇) hides the banned substring 試穿, so the hook library uses 面試場合的顏色選擇; whether the half-wheel in P05 reads as a rainbow; whether the cool-grey swatch reads as a party colour.
7. **Choose the colour-theory reference** before P17 (gate 11), and the **weather page** before P03 (gate 12).
8. **Name the fashion contact(s)** who will sanity-check occasion and trend posts from P15 (gate 16). A sanity check is not an approval.
9. **Hold all B2B and client work out of the persona account in the 30 days.** Any free sample for a contact is shared privately (`b2b-pitch.md`); publishing it would make it a 【合作內容】 post and open the lawyer's unanswered advertisement question.
10. **Gate 15 is closed by D6**; no action. If a Reel is wanted, a human drafts it into the review queue with the four D6 conditions in its production notes, and it takes one of the 4 weekly approvals (OPS-D1); `series.md` has the Reel templates ready. Face animation, synthetic voice and lip-sync still need a separate video addendum.
11. **Overrule or confirm the OPS-D1 cut** (section 6.1): M5 and M10 are Claude's choice of the two lowest-value masters; the wife and operator may swap them, for example for M7. Also decide whether the five-day silence Fri 11-27 to Tue 12-01 is acceptable (section 2).
12. **Decide how character images enter the slides**: framed panel by default, or add a transparent cut-out to the allowed human edits of addendum 11 item 6 (section 7.2).
13. Add the items above that are not yet in `HUMAN_TODO.md` (this stream did not edit the shared tracking files).

---

## 10. Checks run on this file (2026-10-12)

All commands were run from the repository root on 2026-10-12 after the last edit. Nothing was committed. Checks 1 to 13 were first run at v0.1; **they were all run again after the v0.2 update** (decisions D6, OPS-D1 and D3), and the counts below are the v0.2 results unless a row says otherwise.

| # | Check | Result |
|---|---|---|
| 1 | `python3 pipeline/scripts/queue.py validate pipeline/review-queue/sehuan` | 8 drafts, **0 ERROR, 0 FLAG**. 4 WARN, all `PLACEHOLDER` on the three blocked drafts (P03 two entries, P07 one, P08 one); INFO `MEDIA_PENDING` on every draft with media. A clean run is not approval |
| 2 | `python3 content/sehuan/verify.py` (this folder's script; reuses the pipeline word scanner) | **0 errors**, 5 warnings (the three BLOCKED drafts, the RP05 quoted-denial note and a note about OpenCC; the author's summary said 4). It checks: required fields and types, id and folder agree, `ai_label_flag` true, sponsorship none, review fields pending, no draft on 2026-11-27 to 11-29, Instagram days Mon, Wed, Fri and Threads days Tue, Thu, Sat, hook at most 20 characters, caption starts with the disclosure line and names 「色環」, caption length, hashtag counts and banned hashtags, media items all PENDING with a prompt, no hex or Chinese in an AI prompt, the word scanner on hooks, captions, labels, hashtags and every slide's on-screen text, the 30 weekday rows of section 3, the weekday of every heading and outline row, P01 to P22 present, all hook IDs in the calendar exist, 44 hooks scanned, 12 replies scanned, Simplified-only characters in every file, and the arithmetic in this file. **Added at v0.2:** the section 3 table must schedule exactly 18 posts, never a deferred one, at most 2 Instagram and 2 Threads a week and at least 2 Instagram in each of weeks 1 to 4; section 6 must hold the ten scheduled outlines and section 6.1 exactly P09, P10, P19 and P20; every outline's weekday must fit its platform; gate 15 must read Closed by D6; a Reel or Short draft (none exists) must carry the four D6 conditions in `review.notes` and be Instagram only; every lesson graphic must say DRAWN BY CLAUDE AS SVG and no stale human-built wording may remain in the `post.json` files or in sections 5 and 6; the headline section 8 numbers must appear in the text. Negative tests on temporary copies (a deferred post put back in the table, a third Instagram post in a week, gate 15 reopened, a changed capacity number, old wording in section 6, a Reel without D6 notes, an old route in a prompt) each produced the expected ERROR |
| 3 | `gen_image.check_prompt` on all 38 `shot_prompt` values (7 AI-image prompts, 31 notes for Claude-drawn SVG graphics) | 0 blocked terms, 0 warnings. The blocklist is a keyword check, not look-alike clearance |
| 4 | Word scanner on the 44 hooks | All `clean`. Three problems were caught and fixed during drafting: 面試穿搭 hides the banned substring 試穿 (hook H25 and the bible's pillar title P3-4); three hooks ran over 20 characters; one hook used 先看 as an instruction |
| 5 | Word scanner on the 12 sample replies | 11 `clean`; RP05 shows one INFO (the refused topic 顯瘦 is quoted inside a denial) |
| 6 | Word scanner on slide text | One catch fixed: 統計項目 used the mainland word 項目 (now 統計種類). The scanner does not read `media[].description`, so `verify.py` extracts the slide text and scans it |
| 7 | Source-dependent wording | The scanner treats 官方 as a claim that needs a real source. The colour and size footers therefore say 品牌提供 (the wife may restore 官方); no caption uses 資料日期 or 出處 unless its post carries a real or placeholder source |
| 8 | OpenCC `s2t` over every new text file and all eight `post.json` | The only changes proposed are 台 to 臺 in five files (re-run at v0.2 over the six text files and the eight `post.json`: the same five), a variant that is acceptable in Taiwan and that the project already writes as 台灣. No Simplified character found |
| 9 | Weekdays and dates recomputed by script | W0 Mon 2026-11-16; Day 30 Tue 2026-12-15; Sat 2026-11-28; Sat 2026-12-12; Sat 2027-01-23; Mon 2026-12-28; every row of section 3 and every post heading |
| 10 | Arithmetic and colour numbers recomputed | 60 + 30 + 10 = 100; 50 x 2 = 100; badge 3.5% of 1350 = 47 px, 8% of 1080 = 86 px, 8% of 1350 = 108 px; build 2 x 60 + 2 x 15 = 150 min, 150 + 20 = 170, 170 / 360 = 47%; pillar mix 4, 3, 2, 2 of 11 = 36%, 27%, 18%, 18% (v0.1) and 3, 2, 2, 2 of 9 = 33%, 22%, 22%, 22% (v0.2); posts 4 + 4 + 4 + 4 + 2 = 18 against 4 + 4 + 6 + 6 + 2 = 22; section 8: 2 x 20 + 2 x 5 = 50, 50 + 20 = 70 = 19% of 360, low case 26 + 20 = 46 = 13%, v0.1 weeks 3 and 4 3 x 60 + 3 x 15 + 6 x 5 = 255 = 71%, D3 only 75 + 30 = 105, savings 150 + 35 = 185, 30-day totals 315 against 935 minutes, 70 / 4 = 17.5 and 46 / 4 = 11.5 minutes per approval, 50 / 110 = 45%, 3 x 50 = 150 and 3 x 26 = 78 against 110 and 74, wife 40 against 60 a week; contrast charcoal on ground 8.85:1, on cream 9.82:1, persimmon on ground 2.10:1; CIE76 distance from the persimmon to wheel position 2 is 12.1 (visibly different) |
| 11 | Cross-calendar slot check, **re-run at v0.2** on the working-tree files after 方寸 and 步驟 were also updated for OPS-D1 (their section 3 day tables; 18 slots each, 54 in all; a one-off script kept in the session scratchpad, not in the repository) | **No two personas share a clock hour on any date.** Closest pairs: 60 minutes (方寸 Short Fri 19:30 against 色環 Instagram Fri 20:30 on 11-20 and 12-04; 12-11 left with P19). Pairs 90 minutes apart: 方寸 Short Tue 19:30 against 色環 Threads 18:00 on 11-24, 12-08 and 12-15. Both other calendars still hold posts inside this calendar's quiet block (方寸 Short Fri 2026-11-27; 步驟 Sun 2026-11-29, two posts): flagged in section 9, not changed. The siblings' files may still change, so the operator re-runs this when the three calendars are reconciled |
| 12 | Golden-set prompts | The R01, R08b, R13, R02 and E05 prompt bodies were copied by script from `pipeline/image-pack/sehuan-photoreal.md` with start-of-text assertions, not retyped |
| 13 | Existing pipeline test suite | 119 tests, OK at authoring time (the shared scripts were not edited); 130 tests, OK at the independent review (the suite had grown); 130 tests, OK again at v0.2 (`python3 -m unittest discover -s pipeline/scripts`; the shared scripts were not edited) |

**Not checked, and why.** The naturalness, tone and Taiwan vocabulary of any zh-TW line (the wife's job). Every fact against a source (the operator's job; the sources are placeholders where they depend on a page). That any image can be generated to the described standard (no image exists and none was generated). Platform limits for captions, hashtags, slides and image size (recalled, *unverified*). That any lesson graphic exists or renders correctly: none has been drawn, and the sandbox has no Taiwan-glyph font (section 7.2). That the operator's review minutes are as assumed (section 8): they are the largest unmeasured number. That the OPS-D1 choice of M5 and M10 is the best pair: it is judgement without engagement data (section 6.1). The election date, the weather-agency name and the size-term definitions (all recalled or unverified).

---

## 11. Review log (independent skeptical review, 2026-10-12)

*This log reviewed v0.1. Its counts (22 posts, 11 masters, 8 drafts) and its capacity figures are v0.1 figures; section 12 records what v0.2 changed and section 8 holds the current arithmetic.*

Reviewer read every file of the stream (this calendar, hook library, series, trend check, reply guidelines, B2B page, `verify.py`, the eight `post.json`) against `BRIEF.md` section 3 and 5, `DECISIONS.md`, `portfolio.md`, the 色環 bible and photoreal addendum, and the two sibling calendars. Nothing was approved, published or committed.

**Re-run by the reviewer.** `queue.py validate` on the eight drafts: 0 ERROR, 0 FLAG, 4 WARN (placeholders on P03, P07, P08, as intended). `content/sehuan/verify.py`: 0 errors, 5 warnings. Pipeline test suite: 130 tests, OK. A separate script checked all eight `post.json` against the shared format (field names and order, enums, id and folder agree, `ai_label_flag` true, sponsorship none, review pending and `approved` false, media entries with `path`/`description`/`shot_prompt`, `media/.gitkeep` present) and that every hook, caption, gloss and hashtag also appears verbatim in section 5: all pass. OpenCC `s2t` over all stream files: only 台 to 臺 variants, no Simplified characters. A grep for mainland and banned wearing, body and hype words found hits only in the "do not use" tables. Hook lengths (44 hooks, longest 20), caption lengths (159, 99, 169, 73, 155, 82, 181, 100), pillar counts and weekday/date rows were recomputed and match. The seven AI-image prompt bodies were compared with `pipeline/image-pack/sehuan-photoreal.md`: identical. The slot claim against the 方寸 and 步驟 calendars holds (no shared clock hour).

**Fixed in place.**

1. `sehuan-2026-11-21_01` (P04, Threads text): the caption's last line promised that the two cases "will each be laid out in one image later". No such post exists in the 30 days, and the operator checklist itself said not to promise a follow-up. Replaced by 「沒有標準答案，說說你的習慣就好。」 in `post.json`, in section 5 (caption and gloss), the character count (78 to 73) and the operator check. A note was appended to the draft's `review.notes`.
2. `reply-guidelines.md` RP09: the reply said sources are always shown (「也會標示來源」), which is untrue for the rule-of-thumb posts that carry no source. Narrowed to 「有引用資料時會標示來源」.
3. `verify.py` hardened: a malformed `post.json`, a non-object `review`, non-list `media` or `hashtags`, or a missing input file now produces ERROR lines instead of a traceback; the arithmetic and date checks no longer use `assert` (they vanished under `python -O`); files are closed; every check step is wrapped. The review-state check no longer forces `pending` forever (it would have failed the first time a human legitimately set a field): it now validates the allowed values, errors on `approved: true` without both reviewers approved, and warns when a human has set a field. A media `path` may now be a real relative path once an image exists (absolute paths and `..` are errors; a missing file is a warning). New WARN when `post.json` and this calendar drift apart.
4. Section 10 numbers corrected: the verify run has 5 warnings (the author's summary said 4; the RP05 quoted-denial note was omitted), and the test suite is 130, not 119.

**Left as the author had it, and why.** The replacement of the bible's 官方 by 品牌提供 in the colour and size footers (the wife may restore it; RP02 and the B2B Part C still say 官方, which is consistent with the bible); the J2 line 「我沒有衣櫃，連這圈色票也是 AI 生成的。」 (a negated limit, not a testimony; the wife rules); the calendar deviations from the bible's indicative plan (listed in section 3 with reasons; accepted).

**Concerns the reviewer could not close by editing.**

- 「虛擬試穿示意」 (B2B Part B and C, bible 8.3) contains 試穿, a word the studio's own scanner and hook rules treat as a wearing claim, while the same label says 「角色未實際穿著」. The wife and the lawyer should decide whether the label contradicts itself. Nothing in the 30 days uses it.
- 圖像為 AI 生成 is the addendum's wording; OpenCC's Taiwan phrase list prefers 影像 and 宣告 over 圖像 and 聲明 in some contexts. Both are used in Taiwan; the wife rules.
- The P03 weather panel compares Taipei with Kaohsiung during the election run-up. It is a data table with no verdict, but the wife should confirm the pairing does not read as a political contrast.
- The wife-minutes comparison in section 8 adds 40 minutes on top of the portfolio's 363 (an overcount, since 色環's drafts are already in the 363): the conclusion (inside the 510 gate) stands, but "far inside" is generous (about 107 minutes of headroom). The operator-minutes comparison adds 20 minutes of approvals that the portfolio's 250 already contains; build time alone (150) still exceeds the 110 minutes of slack.
- All platform limits, image sizes, the election date, the agency names, the 尾牙 date and the size-term definitions remain recalled or unverified, as the author labelled them.

---

## 12. Update log: decisions D6, OPS-D1 and D3 (v0.2, 2026-10-12)

Source: `DECISIONS.md`, the 2026-10-12 entry "User asked for the recommended answers; Claude's recommended choices adopted on the user's behalf (reversible)". Each decision below was applied, not re-decided. Nothing was approved, scheduled, published or committed.

| Decision | What was applied here | What was left alone, and why |
|---|---|---|
| **D6** a still, or a slow pan or zoom of a still, in a Reel or Short with four conditions | Gate 15 closed (section 1). The four conditions are written into sections 0, 7.3, 7.5 and 9, into the Reel templates of `series.md` and the hook rules, and `verify.py` now requires them in `review.notes` of any Reel or Short draft. The badge wording 「AI 生成｜虛擬角色」 matches addendum 8.2 and `pipeline/qa-checklist.md` D3, so no string changed; the one older difference (diagram badge 「AI 生成」 or 「搭配示意」 against the checklist's 「AI 生成｜示意圖」) is noted in section 7.3 | **No 色環 post was on hold only for D6, so no post changed status.** The eight drafts are Instagram carousels and Threads images or text; no Reel or Short was ever drafted, and none was invented. The three blocked drafts (P03, P07, P08: unfilled sources) and P04 (gate 17, the user's text-only first line) stay held for their own reasons. The addendum's "not covered" line and QA checklist section 6 still say video is barred until a separate addendum exists, which is right for face animation, voice and lip-sync and is not edited here (other folders) |
| **OPS-D1** 12 approvals a week across the three pilots through week 8 | W3 and W4 cut from 6 to 4 approvals; M5 (P09, P10) and M10 (P19, P20) deferred (section 6.1, with the reasons, the alternative weighed and the restore order); cadence statements in sections 2 and 3, the totals (18 posts, 9 masters), the deviations table, the 雙12 and gate 17 notes, the weeks 3 and 4 capacity arithmetic (section 8), `series.md` episode tables and rotation, `hook-library.md` rows H06, H16, H41, H43 | The IDs P01 to P22, the dates and the queue folders of the remaining posts did not move. The primary platform (Instagram) keeps 2 posts a week in each of W1 to W4. The other files that hold 色環 slots (`launch/schedule.md`, `launch/schedule_check.py`, `ops/`, `analytics/`, `strategy/portfolio.md`) are outside this stream and still show the 22-slot plan: see the hand-over note in the stream summary |
| **D3** Claude draws the diagram, lesson-graphic and edit-asset layer as SVG, rendered to PNG; the operator and the wife still approve every asset | Section 7.2 rewritten (route, status, font, character images, review and provenance); the 31 non-AI `shot_prompt` values and the build-spec wording in all eight `post.json` files and in sections 5 and 6 changed from human-built to DRAWN BY CLAUDE AS SVG; a D3 note appended to the seven `review.notes` that have media; section 8 rewritten with the review-time assumption (20 minutes per carousel, 5 per card, low case 10 and 3), the weekly loads before and after, the all-in minutes per approval and the comparison with the shared slack | **No SVG or PNG was drawn in this update**; the kit is a specification and the first drawing job is stated in section 7.2. No Taiwan-glyph font is installed in the sandbox (`fc-list`, 2026-10-12), so final text cannot yet be rendered. Claude cannot edit video. `hex` guidance, slide copy, captions and hooks were not changed |
