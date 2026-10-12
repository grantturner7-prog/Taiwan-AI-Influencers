# launch/: Phase 6, account setup, link-in-bio pages and the posting schedule (DRAFT v0.1, 2026-10-12)

Start here. For the operator (English); every zh-TW string is an AI draft for the wife. **Nothing in this folder has been published, scheduled, created or approved.** No account exists, no handle has been checked, no avatar has been generated (Claude has no image tool in this session), no hosting or domain exists, and the studio name 明說角色工作室 is provisional and unsearched. Platform menus, limits and rules are recalled and **unverified**; the live screen overrules this folder.

The three pilots (user decision, `DECISIONS.md` 2026-10-11 and 2026-10-12: photoreal AI characters that stay openly AI): 方寸 (fangcun, home organisation: Instagram then YouTube Shorts), 步驟 (buzhou, AI tools: YouTube Shorts then Threads) and 色環 (sehuan, outfit logic and colour: Instagram then Threads). First post date W0 = Mon 2026-11-16 is an assumption.

## 1. What is here

| Path | What it is |
|---|---|
| `README.md` | This file: gates, step order, capacity check, decisions, your jobs, open items |
| `00-studio-setup.md` | Studio-level set-up done once: who does what, the credentials policy (nothing secret in the repo), mailbox, password manager, two-factor, recovery, Meta and Google structure, link-page host, what not to create, what to do if access is lost |
| `platform-checklists.md` | Instagram, Threads and YouTube step lists with tick boxes; one table for AI-label settings and one for paid-partnership tools; templates for a Facebook Page and a LINE Official Account (neither is planned) |
| `personas/fangcun.md`, `buzhou.md`, `sehuan.md` | Per pilot: accounts, handle candidates (all UNCHECKED), zh-TW name field and bios with computed lengths, avatar rules with the carried generation prompt (media PENDING), settings, gates, who does what, sign-off |
| `link-pages/` | Four static HTML pages (the three pilots and the studio), one shared CSS file, a checker, a screenshot script and phone-width screenshots. Its own `README.md` has the English gloss of every page string |
| `schedule.md` | The approval gate, the weekly rhythm in 6 + 10 hours, how each platform is scheduled with official tools, the manual fallback, the pause switch, the merged 30-day slots |
| `schedule_check.py` | Merges the three calendars' slots, shifts them with W0 and checks clock-hour clashes, no-post dates, weekly hours and the approval gate. Read-only |
| `check_launch_docs.py` | Checks this folder: bio lengths, handle lists against the bibles, zh-TW scan, relative links, no secrets |
| `templates/avatar-guide.svg` | Layout guide for the avatars: circular crop, safe disc, where the AI chip goes (inside the circle) |
| `evidence-log.csv`, `schedule-log.csv` | Empty logs with headers; filled by hand. They hold file names, never the screenshots or any secret |

## 2. Rules that apply to everything here

Openly virtual in four places (bio, first caption line, on-screen badge, platform label); original face; adults only; no lived experience; paid relationships disclosed; no health, finance, gambling or politics; no fake popularity; the studio named in every bio and the personas never vouching for each other; official tools only, no automation; every automated reply says it is automated; every post approved by a human first for at least 30 days (`BRIEF.md` section 3). Credentials, recovery codes, two-factor secrets, API keys and phone numbers are never written into the repo (`00-studio-setup.md` section 2). Claude does not commit.

## 3. The order of work, and who does it

A human creates every account and passes every phone or ID check. Claude drafts, builds and checks; it does not log in to anything or press publish.

| # | Step | Who | Needs | Where |
|---|---|---|---|---|
| 1 | Decide D1 to D9 (section 5) | You | Nothing | This file |
| 2 | Reading test of the studio name and the three names | Wife | | `HUMAN_TODO.md` 18 |
| 3 | TIPO and 經濟部 searches (studio name and pilots, Chinese and romanised) | You, wife | Step 2 | `HUMAN_TODO.md` 20 |
| 4 | Handle checks, logged out, nothing created | You | Step 3 | `personas/<slug>.md` section 2; `HUMAN_TODO.md` 21 |
| 5 | Studio mailbox, password manager, two-factor method, ownership memo | You, wife | | `00-studio-setup.md` sections 3 to 5 |
| 6 | Business registration started; lawyer consult booked | Wife (registrant, to be confirmed) | | `HUMAN_TODO.md` 4, 7, 9 |
| 7 | Read and record the commercial-use terms of the image tool and plan | You | | `HUMAN_TODO.md` 33. Until then **no public account** |
| 8 | Make the avatars: run the image packs, pass the age-guess, look-alike and near-pair tests, add the AI chip | You, wife | Steps 4 and 7 | `pipeline/image-pack/README-photoreal.md`; `personas/<slug>.md` section 5; `templates/avatar-guide.svg` |
| 9 | Wife reads and approves every string and the link-page text | Wife | Step 2 | `personas/<slug>.md` section 3; `link-pages/README.md` section 4 |
| 10 | Link-page host and domain (D4); fill the placeholders; `check_pages.py --final`; deploy | You | Steps 5 and 9 | `link-pages/README.md` section 6 |
| 11 | Create the accounts, **one persona per sitting**, in launch order 方寸, 色環, 步驟 | You (a human must pass verification) | Steps 4, 5, 7, 8, 9 | `platform-checklists.md` A, B, C; `personas/<slug>.md` section 8 |
| 12 | Instagram "AI-generated profile" label check on a Taiwan account (D1) | You | An Instagram account | `HUMAN_TODO.md` 10 and 38 |
| 13 | Scheduling and label dry runs, one per platform per account | You | Step 11 | `schedule.md` section 4 |
| 14 | Reviewer trial; STOP 3 samples; lawyer's launch-gate answers | Wife, you | | `HUMAN_TODO.md` 8, 9, 37; `BRIEF.md` section 6 |
| 15 | Batch 1 through the weekly rhythm: Claude drafts, you pre-check, wife reviews, you approve and schedule | All | Steps 11 to 14 | `schedule.md` sections 2 and 3 |
| 16 | First post, live check, evidence | You | Every gate closed | `schedule.md` section 9 |

An account is created only when its gates A1 to A7 are closed (`personas/<slug>.md` section 7): no account may be created earlier, because parked or placeholder accounts are barred (`personas/README.md` section 2; `strategy/portfolio.md` 6.2).

**Status board (2026-10-12).** Every cell is open.

| Account | Gates A1 to A7 | Created | AI-generated profile label | Link set | 2FA + recovery | Dry run | Evidence logged |
|---|---|---|---|---|---|---|---|
| 方寸 Instagram | open | no | not checked | no | no | no | no |
| 方寸 YouTube | open | no | n/a | no | no | no | no |
| 步驟 YouTube | open | no | n/a | no | no | no | no |
| 步驟 Threads | open | no | not checked | no | no | no | no |
| 步驟 Instagram (prerequisite, only if Threads needs it) | open | no | not checked | no | no | no | no |
| 色環 Instagram | open | no | not checked | no | no | no | no |
| 色環 Threads | open | no | not checked | no | no | no | no |
| Link pages (4) | wife's review open | not deployed | n/a | n/a | n/a | n/a | n/a |

## 4. Capacity check: is W0 = 2026-11-16 realistic?

*All minutes below are assumptions, labelled as such; sums were computed in this session.*

| Item | Operator minutes | Wife minutes |
|---|---|---|
| Studio mailbox, vault, two-factor design | 60 | |
| Link pages: first deployment 90, filling placeholders for the four pages 45 | 135 | |
| 方寸: Instagram 70, YouTube 50, two dry runs 40, evidence 10 | 170 | |
| 色環: Instagram 70, Threads 25, two dry runs 40, evidence 10 | 145 | |
| 步驟: Instagram prerequisite 70, Threads 25, YouTube 50, two dry runs 40, evidence 10 | 195 (125 if Threads needs no Instagram) | |
| Reading every string and page; reading the live profiles aloud (20 minutes each for three personas, 20 for the studio page, 20 per live profile) | | 140 |
| **Launch setup total** | **705 (about 11.8 h); 635 without the 步驟 Instagram account** | **140 (about 2.3 h)** |

Operator hours between today and W0: 5 weeks x 6 h = **30 h** (computed). Known operator jobs that come first: this setup (about 11.8 h), the image packs for the avatars and golden sets (**about 24 to 28 h** for all three pilots, `HUMAN_TODO.md` 34; the packs' estimates mix operator, wife and panel time, so this is an upper bound for the operator), and the first batch's approvals and 步驟 recordings (12 approvals x 5 min plus 40 min, about 1.7 h, `portfolio.md` 5.3). That is roughly **38 to 42 h against 30 h**, before the handle checks, the licence-terms reading, the label check, the lawyer and registration admin, the diagram-kit build and the recording hygiene kit that the calendars flag as unbudgeted. **W0 = 2026-11-16 is unlikely.** At 6 h a week the operator needs about 6 to 7 weeks for what is listed (38 to 42 h divided by 6), which from 2026-10-12 is **2026-11-23 to 2026-11-30 at the very earliest, and later if anything slips** (computed, rough). The first gate review should set W0, and every date then moves by whole weeks (`schedule.md` section 10). This is decision D7.

## 5. Decisions for you (all reversible; each has a default that is used until you say otherwise)

| # | Decision | Default and why |
|---|---|---|
| D1 | Where the Instagram "AI-generated profile" label check is done. `HUMAN_TODO.md` 10 and 38 plan one separate test Instagram professional account | **Do it inside the real 方寸 account on its creation day, before any post.** Then no test account exists, which fits "no parked accounts" and "never open a second account to dodge a label". Alternative: the one planned test account, never a second |
| D2 | Do the persona link pages link to the studio page? | **Yes.** It makes the studio line in the bio checkable (Ground rule 8) and is the only cross-persona surface (`DECISIONS.md` STOP 2 item 7). The studio page lists the three live characters neutrally and each persona page links nowhere else. To remove it, delete one list item per page |
| D3 | Instagram professional account type (Creator or Business) and how two people log in | **Shared login from the vault** for the pilot; Creator or Business chosen on the screen after checking that scheduling, the AI label and the paid-partnership tool are offered. A Meta business portfolio is the alternative (requirements unverified): `00-studio-setup.md` section 8 |
| D4 | Link-page host and domain | **A free static host address now** costs nothing but the URL changes later (up to seven bios to edit); a domain first avoids that but must wait for the TIPO searches. Budget line NT$300 a month (`portfolio.md` 7) |
| D5 | Posts inside 色環's quiet block around the recalled polling day (方寸 Fri 11-27 19:30; 步驟 Sun 11-29 08:15 and 21:00) | **Keep as written**; hide political comments. Stricter option: unschedule the three (`schedule.md` section 7) |
| D6 | May the photoreal character appear as still images inside Reels and Shorts before a video addendum exists? | **No answer given yet.** Until it is yes, 3 of 方寸's 5 drafts and every 步驟 Short stay on HOLD; if no, drop the character panels and use the 「AI 生成｜示意圖」 badge |
| D7 | W0 | **Keep 2026-11-16 only as a label.** Set the real date at the first gate review; sections 3 and 4 (`schedule.md` section 8 gives the back-schedule for 2026-11-16) |
| D8 | Two public promises on the studio page | The wording 「目前每則貼文都由真人審閱後才發布」 and 「製作角色時，不使用任何真人照片作為參考，也不以特定真人為藍本」 are true of the current process. Keep, soften or strike with the wife and the lawyer. The 24-hour take-down is an internal rule and is deliberately not stated as a number publicly |
| D9 | Create the 步驟 Instagram prerequisite account | **Only if the Threads sign-up needs an Instagram login** (unverified). If Threads offers another route, tell Claude first |

## 6. Your jobs (numbered L1 to L12 so they can be merged into `HUMAN_TODO.md` without clashing with its numbers)

1. **L1** Decide D1 to D9 (section 5).
2. **L2** Studio mailbox, password manager, two-factor method and a one-page ownership memo for accounts, domain, mailbox and characters, with the 記帳士 or lawyer (`00-studio-setup.md` sections 3 to 5).
3. **L3** Wife: read and rule on every zh-TW string in `personas/<slug>.md` section 3 and `link-pages/README.md` section 4, including the three "非真人" bio lines and the studio-page promises.
4. **L4** Make the three avatars (image packs, tests, the AI chip by `templates/avatar-guide.svg`), after the licence terms are recorded (`HUMAN_TODO.md` 33, 34, 36).
5. **L5** Create the accounts, one persona per sitting, passing every verification yourself; set two-factor, recovery, bios, avatars and the label settings; screenshot and log (`platform-checklists.md`).
6. **L6** Run the label check (D1) and the scheduling dry runs; record in `evidence-log.csv` what each platform really offers; tell Claude the real menu names so the checklists can be corrected.
7. **L7** Choose host and domain (D4), fill the link-page placeholders, run `check_pages.py --final`, deploy, test on a phone.
8. **L8** Confirm the polling date with the Central Election Commission; decide D5 and D6.
9. **L9** Settle the order of the AI line and the commercial tag before the first sponsored post (section 7, item 6).
10. **L10** Learn the weekly rhythm by doing batch 1; log real minutes for setup and for the first four weeks (`schedule.md` section 3).
11. **L11** Add a row to `schedule-log.csv` for every scheduled or manual post and run the live check (`schedule.md` section 9).
12. **L12** Set W0 at the first gate review (D7) and, if it moves, ask Claude to re-date the review-queue drafts.

## 7. Open items and inconsistencies found in other files (not edited here)

1. `HUMAN_TODO.md` 10 and 38 plan a test Instagram account; `personas/README.md` bars parked accounts. D1 proposes the real account instead.
2. `personas/fangcun/bible.md` 8.1 says "all room images are AI-generated illustrations". Under the photoreal addendum the room diagrams are human-built. The bio, YouTube description and link page here use the corrected sentence; the bible itself is unchanged.
3. The three pilot bios gain a 「非真人」 line (photoreal risk "mistaken for a real person"). It is new text, not in any bible.
4. Whether Threads needs an Instagram login, and whether the Instagram "AI-generated profile" label carries to Threads, are unresolved (`research/platforms.md` 4.2). 步驟 and 色環 both depend on the answer.
5. Alt-text drafts differ: 方寸's addendum says 「…方寸，示意圖，非真人。」, 色環's says 「…色環，非真人。」, 步驟 has none, and `pipeline/qa-checklist.md` D8 uses the 示意圖 form for all. The persona files use each addendum's form and copy 色環's for 步驟.
6. **The order of the AI line and the commercial tag differs.** 方寸 bible 8.5: AI line, then the tag. 色環 bible 8.5: the 【業配】 line first, then the AI line. 步驟 bible 8.5: the tag first line of the description, above or directly after the AI line. `qa-checklist.md` D6: the tag directly under the AI line. `queue.py` only requires the tag in the first lines. No sponsored post is possible in the first 30 days, but one studio rule should be chosen before the first one.
7. `strategy/portfolio.md` 6.1 wants link clicks counted at account level within about NT$300, while the Phase 6 brief says the link pages carry no analytics. The pages carry none; the metric stays unscored until Phase 7 chooses a method (`link-pages/README.md` section 7).
8. The review-queue folders are named by date. If W0 moves they must be re-dated (`schedule.md` section 7, row 7).
9. The three calendars treat 雙12 differently (方寸 and 色環 post, 步驟 does not) and the polling-day quiet block differently (D5). Both are inside the rules.
10. `HUMAN_TODO.md` 25 asks for platform limits (bio, name, Shorts length, safe zones, caption fold) to be read in the apps. The values in `platform-checklists.md` section 0 are recalled and need that session.

## 8. What was checked, and what was not

Checked in this session (2026-10-12), with the commands that reproduce it:

* `python3 launch/link-pages/check_pages.py`: PASS for all four pages (structure, no script or tracker, links, the literal disclosure line, language scan, contrast); `--final` fails on purpose (15 placeholders, banner, PENDING avatars). A negative test on a mutated copy failed on every injected fault.
* Headless Chromium (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless`) rendered the four pages at 320, 390 and 1280 px and the screenshots were viewed; five layout problems were fixed. Screenshots: `link-pages/screenshots/`.
* `python3 launch/schedule_check.py`: PASS, 0 errors and 3 warnings (decision D5). Weekly loads reproduce `portfolio.md` 5.3 (250 and 300 operator minutes, 363 and 402 wife minutes).
* `python3 launch/check_launch_docs.py`: see its output; it checks bio lengths, handles against the bibles, the zh-TW scan, links and the absence of secrets.
* `python3 -m unittest discover -s pipeline/scripts`: 119 tests OK (unchanged by this stream).

Not checked, and not checkable here: any platform screen, menu name, limit or rule; whether any handle or the studio name is free or clear; a real phone, Safari or the Instagram in-app browser; a screen reader; Taiwan-law statements (all unverified, not legal advice); any image (none exists); the commercial-use terms of any tool.

## 9. Review log (independent skeptical review, 2026-10-12)

Reviewer read every file in `launch/` and re-ran all checkers. Result: no ground-rule violation found; no Simplified character or mainland term found (a separate character scan plus the project scanner, which was also tested on injected bad strings and flags them); no invented fact, price, contact or URL (the three Instagram help URLs trace to `research/platforms.md`); all platform specifics remain labelled recalled or unverified.

Fixed in place:
1. `schedule.md` section 2 said 17 slots have a draft; the review queue has 21 (方寸 5, 步驟 8, 色環 8). Corrected.
2. `personas/buzhou.md` section 4 said no 步驟 Short is in the review queue and A14 said "0 of 4 drafts"; four Short drafts exist (all HOLD, media PENDING). Corrected to 8 drafts (4 Threads, 4 Shorts).
3. `schedule_check.py` printed a traceback on a malformed `--w0` or `--no-post` date; it now prints one line and exits 2.
4. `check_launch_docs.py` printed 30 characters of anything that looked like a secret; it now prints 4 and says the rest is withheld.

Checked and passing: `check_launch_docs.py`, `schedule_check.py` (0 error, 3 warn = D5; shifting W0 by one week reproduces a clean run apart from the fixed polling-day date, as documented), `check_pages.py` (negative test: an injected external link fails), 130 pipeline tests, all 21 `post.json` files validated against the shared format (fields, ids, folder dates, `ai_label_flag` true, `approved` false, review fields pending, `media/.gitkeep` present). Scheduler slots were compared with the three calendars' tables and match; weekdays of the key dates were recomputed.

Still open (not fixable by editing): (a) public promises on the studio page (D8) include a third one, 「先暫停相關內容再進行查證」 in the corrections card, which the wife and lawyer should rule on together with the two already listed; (b) the page claim 「每張圖片與每支影片都標有『AI 生成』」 is true only if the badge is applied to 步驟's screen recordings, as the queue labels say; (c) the wife-minutes line in section 4 ("20 per live profile") is ambiguous and the 140 total should be recounted by hand; (d) filled-form Threads links use `threads.net`; confirm at deployment which host Threads now uses (`threads.com` is also allowed by the checker); (e) the checker's keyword scan skips three disclaimer sentences by design, so the wife must read them.
