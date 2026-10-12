# 步驟 (buzhou) weekly trend-check routine

**Status: DRAFT v0.1, written 2026-10-12 (Phase 5, content).** A 30-minute routine, run by the operator on Fridays, that does two jobs for an AI-tools channel: (1) it looks for what changed in the tools and on the platforms, so that published steps do not go stale unnoticed; (2) it looks for topics worth a master. Nothing here has been run. No trend, number or release is cited in this file; the DEMO note in section 7 is format only. Every zh-TW string is an AI draft for the wife.

## 1. What the routine is for, and what it is not for

**For:**

- Finding out that a vendor changed a setting, a limit, a price page or a help article that a published 步驟 video depends on (the **re-check ledger**, section 6).
- Choosing 0 to 3 topic candidates for the backlog, from what viewers asked, what vendors released, and what people search.
- Catching a platform policy change that affects a disclosure label or an account's standing.

**Not for:**

- Chasing speed. This channel is date-stamped and source-led; being second and right is the position. A new feature is not covered until it exists on a plan the operator can show on the recording day.
- Copying anyone's script, structure or thumbnail, or reacting to a creator by name.
- Reporting news about a vendor, an incident or a scam. Those are other people's lanes (the scam lane belongs to a different character and is lawyer-gated); 步驟 only quotes a vendor's own page, with the date.
- Scoring the channel's own performance. The weekly report (Phase 7) does that.

## 2. Hard limits (the ground rules applied to research)

1. **Public pages, read by hand.** No scraping, no scripted queries and no automation of any kind against any site or app. No logged-in community scraping (Dcard, PTT and Threads search are looked at by a person, in the ordinary app or browser, and only for topics).
2. **No fake popularity.** The check never likes, follows, comments on or shares anything to prompt a reply, and never contacts another persona's account (Ground rules 7 and 8). Reading is enough.
3. **No contact with a vendor** during the check. A vendor conversation goes through the operator and, for anything commercial, the contract process (calendar section 9, item 8).
4. **No unapproved tool.** The routine does not install, sign up for or test a new AI tool. A tool becomes a topic only after gate G7 (its terms read) and a recording-day check.
5. **No personal data in the notes**: no viewer names, no screenshots of viewers' comments beyond the comment text and the post it was on.
6. **Nothing from the barred lanes becomes a candidate**: income, side hustles, trading or betting bots, loan apps, fortune-telling, face-swap, voice cloning, detector evasion, cheating, politics, elections, health or legal advice from AI (bible 7.2; `portfolio.md` 2C).
7. **Anything unverified is labelled unverified** in the note. No number is written down that was not read on the page, and the page and date are recorded next to it.

## 3. The 30-minute budget (Friday, operator; *assumption*, to be measured)

| Minutes | Step | What to do | Output |
|---|---|---|---|
| 0 to 8 | **Release and ledger watch** | Open, by hand, the public release notes, change log or "what's new" page and the help articles of the tools currently in rotation (section 5). Compare with the re-check ledger: has a cited article moved, changed or vanished? | Ledger updates; stale flags; P1 or P2 candidates |
| 8 to 13 | **Platform policy watch** | Open the policy pages listed in `research/platforms.md` section 4 for YouTube (altered or synthetic content; the "inauthentic content" monetisation rule) and for Meta (AI info labels, branded content). Note only a change since last week | A line in the note, or "no change"; a change goes to `HUMAN_TODO.md` and to the user the same day |
| 13 to 18 | **Google Trends** | By hand on the public page: Taiwan, past 7 days, the fixed terms in section 4. Write down the names of related rising queries. Write down no figure unless it is read off the page and dated | Candidate words, no numbers |
| 18 to 23 | **Search suggestions and shelf** | Type the five seed phrases in section 4 into YouTube's search box and read the suggestions. Scroll the Shorts shelf for topics only | Candidate topics; nothing copied |
| 23 to 27 | **Viewer questions** | Read the comments and replies on the channel's own posts since last Friday. Tally themes: a request, a correction, a confusion about what the channel is, a 是真人嗎 question, a stale-step complaint | Counts by theme; corrections to make |
| 27 to 30 | **Write the note and decide** | Fill the trend note (section 7). Choose 0 to 3 backlog candidates. Update the ledger. Flag any post to re-record or correct | The note, filed with the weekly log |

If the check runs over 30 minutes two Fridays running, cut the Google Trends and search steps first; never cut the ledger watch or the policy watch (a stale step or a label change is the harm; a missed topic is not).

## 4. Fixed terms and the no-post list

**Search seeds (*assumption*; the wife edits).** Google Trends terms: 提示詞, AI 工具, 逐字稿, AI 摘要, 匯出 對話. Vendor names the operator already shows (Claude, Gemini, ChatGPT) may be used as search terms; they are not endorsed by being searched. YouTube suggestion seeds: 「AI 工具 教學」, 「提示詞 範本」, 「PDF 整理 重點」, 「訂閱 價格」, 「AI 隱私」. Change the list only in writing, with the reason.

**No-post and caution list the check must apply to the next six weeks** (dates are *computed* from `research/culture.md` section 4 unless marked *unverified*):

| Date or period | Rule |
|---|---|
| Sat 2026-11-28 | Local elections, recalled, *unverified*: no post; hide political comments; AI-and-election topics barred |
| Fri 2026-11-27 and Sat 2026-12-12 | Black Friday and 雙12: no post on either day; no deal, sale or ranking wording on the days around them |
| Fri 2026-12-25, Thu 2026-12-31 | Holidays and 跨年: year-end topics only as calendar tidy-up, never as promises of getting more done |
| Thu 2027-02-04 to Sun 2027-02-07 | 除夕 (2027-02-05) and 農曆新年 (2027-02-06): quiet days; no check-driven post |
| Sun 2027-02-28 | 228: no post |
| Any day | A disaster, typhoon or public tragedy: the pause switch unschedules everything |
| 2027-08-02 to 2027-08-31 | Ghost month: no launches; neutral posts only |
| Student season (exams, new term) | Any student-facing candidate says "follow your school's rules" and never helps hide AI use |

## 5. The release-watch list (kept by the operator; one row per tool in rotation)

The operator fills the URLs by opening each vendor's own pages. **No URL is given here, because none could be checked** (web access failed on 2026-10-12). Recalled domains, **unverified**: `help.openai.com` (ChatGPT), `support.anthropic.com` (Claude; the help centre may have moved), `support.google.com/gemini` (Gemini). The vendor's own release-notes or change-log page, if it has one, is the primary source for "what changed".

| Tool | Release notes or change log (URL) | Help articles cited by published posts (URLs) | Last opened | Changes since last time |
|---|---|---|---|---|
| `{工具A}` | `{網址}` | M1 `{網址}` | `{日期}` | |
| `{工具B}` | `{網址}` | M2 `{網址}` | `{日期}` | |
| `{工具C}` | `{網址}` | M3 `{網址}` | `{日期}` | |

## 6. The re-check ledger (staleness control; the heart of this channel)

Rule (bible 7.1 item 14; calendar section 7.2 rule 12): every post gets a re-check date, **90 days after publishing or the vendor's next release, whichever is first**. On the due date the operator re-opens every cited page and compares. Outcomes: **unchanged** (log it, set the next date); **changed in a way that breaks a step or a number** (a pinned correction within 24 hours, then re-record or unlist); **page gone** (unlist or re-source). Never edit a published video around an old recording.

Opening rows (computed from the calendar; the due dates that land on a Saturday are moved to the Friday before):

| Post | Published | Re-check due (90 days) | Do it on | Owner | Status |
|---|---|---|---|---|---|
| M1 (S1, T1) | Thu 2026-11-19 | Wed 2027-02-17 | Wed 2027-02-17 | Operator | not yet due |
| M2 (S2, T2) | Sun 2026-11-22 | Sat 2027-02-20 | Fri 2027-02-19 | Operator | not yet due |
| M3 (S3, T3) | Thu 2026-11-26 | Wed 2027-02-24 | Wed 2027-02-24 | Operator | not yet due |
| M4 (S4, T4) | Sun 2026-11-29 | Sat 2027-02-27 | Fri 2027-02-26 | Operator | not yet due |

Rows for M5, M6, M9, M10 and M11 are added when each is published (M7 and M8 are cut under OPS-D1; if either is brought back, add its row then). Any vendor release that touches a cited page makes the row due early. A comment saying the video is out of date (reply R-STALE in `reply-guidelines.md`) also makes it due early.

## 7. The trend note (template)

One page, filed with the weekly log. Fill it by hand.

```
TREND NOTE v0.1 (DRAFT)          Week of: ____/__/__ (Friday)      Operator: ____      Minutes: ____

1. LEDGER
   Posts checked: ______    Changed: ______    Stale (action): ______    Pages gone: ______

2. TOOL RELEASES (public pages only; name the page and the date seen)
   {工具} | {頁面名稱} | {YYYY/MM/DD} | what changed, in the page's words | affects post(s): ______

3. PLATFORM POLICY (change since last week? Y / N)   Page: ______  Date seen: ____/__/__
   If Y: what changed in one sentence; sent to HUMAN_TODO Y / N

4. SEARCH AND SHELF (names only, no figures unless read off the page and dated)
   Google Trends related queries: ______
   YouTube suggestions: ______
   Topics seen on the shelf (not copied): ______

5. VIEWER QUESTIONS (counts by theme, this channel's own posts only)
   Requests: __  Corrections: __  Stale-step: __  Confusion about the channel: __  是真人嗎: __

6. FILTER CHECK for each candidate (all must be Y)
   [ ] a feature or page exists today and can be shown on a studio test account
   [ ] not income, trading, loan, fortune, face-swap, voice clone, detector evasion, cheating, politics, health or legal advice
   [ ] needs no viewer personal data
   [ ] script can be original and the structure is one of the three series
   [ ] not a verdict on a named vendor

7. DECISION
   Backlog candidates (0 to 3): ______
   Re-record or correct: ______
   Flags for the wife / the user: ______
```

**DEMO (format only; no real data, no real numbers, nothing here happened):**

```
TREND NOTE v0.1 (DEMO)           Week of: 2026-00-00 (DEMO)      Operator: DEMO      Minutes: DEMO

1. LEDGER   Posts checked: DEMO    Changed: DEMO    Stale (action): DEMO    Pages gone: DEMO
2. TOOL RELEASES   DEMO-TOOL | DEMO-PAGE | DEMO-DATE | DEMO-CHANGE | affects: DEMO
3. PLATFORM POLICY   change: DEMO
4. SEARCH AND SHELF   related queries: DEMO-QUERY-1, DEMO-QUERY-2 (names only)
5. VIEWER QUESTIONS   Requests: DEMO ...
6. FILTER CHECK   DEMO-CANDIDATE: all five Y / one N (reason)
7. DECISION   Backlog: DEMO-TOPIC. Re-record: none. Flags: DEMO
```

## 8. Filters: what a trend may become

| What the check sees | May become | Never becomes |
|---|---|---|
| A vendor adds or changes a feature | A P1 三步驟 candidate, **after** the feature is stable on a plan the operator can show, and only with its help article | A "first to cover" race; a claim about what the feature will do for the viewer |
| A vendor changes a price page, a plan or a limit | A P2 對照表 candidate, and an early re-check of every older P2 post | Deal or discount framing; "worth it"; a ranking; a conversion |
| A vendor changes a data-handling, export or deletion article | A P4 or P2 candidate quoting the page, and an early re-check | Commentary on a company's trustworthiness; a legal reading |
| A viral prompt or format | A P3 template only if the template can be written from scratch and tested on the sample kit | A trend that asks viewers to upload a photo of themselves or of another person, a trend that imitates a real person, or anyone else's prompt copied |
| A news item about AI, jobs or misinformation | Nothing | "AI will replace you" lines; election or political content; scam reporting |
| A viewer question that repeats | A backlog candidate | A promise to make it, or a personal answer in a comment |
| A viewer says a step has moved | An immediate ledger check and, if true, a pinned correction | A defence of the old video |

## 9. For the wife

Please read the search seeds in section 4 and the list in section 8, and tell us: (1) whether the Chinese search words are the ones people in Taiwan type; (2) whether any word is dated or mainland-leaning; (3) which kinds of AI trends in Taiwan you think are risky for this channel (so they go on the barred list); (4) anything you would add to the caution calendar. Your time for this file is one reading, about 15 minutes (*assumption*).

## 10. Open items for the operator

| # | Item | Blocks |
|---|---|---|
| 1 | Open each tool's release-notes or change-log page and the help articles used, and fill the table in section 5 | The first Friday check |
| 2 | Confirm whether each platform policy page in `research/platforms.md` section 4 still loads and note the date | Policy watch |
| 3 | Measure the real minutes of the first four checks and adjust the budget in section 3 | Capacity |
| 4 | Decide where the weekly log and the ledger live (a shared sheet or a plain file in `analytics/`, Phase 7) | The ledger |
| 5 | Confirm the Google Trends and YouTube pages can be used by hand in Taiwan without a login, and that no step needs a tool whose terms bar manual research | The routine |
