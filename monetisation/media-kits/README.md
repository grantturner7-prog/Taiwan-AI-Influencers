# Media kits (Phase 8): what they are and how to keep them current

DRAFT v0.1, written 2026-10-12 for the operator (English). Every zh-TW string in the kits is an AI draft for the wife; the operator reads the English column. **Nothing here has been sent, published or approved, and nothing may be sent by Claude.** Outreach is sent by the humans only.

## 1. What is in this folder

| File | What it is |
|---|---|
| [studio.md](studio.md) | Umbrella kit: who the studio is, the character directory, what it can offer (not yet offered), the disclosure standard, brand safety, process, studio-level figures (all empty), terms in outline, contact and invoicing placeholders |
| [fangcun.md](fangcun.md) | Kit for 方寸 (home organisation, Instagram and YouTube Shorts) |
| [buzhou.md](buzhou.md) | Kit for 步驟 (AI tools, YouTube Shorts and Threads) |
| [sehuan.md](sehuan.md) | Kit for 色環 (colour and outfit logic, Instagram and Threads) |
| [check_kits.py](check_kits.py) | Checks the four kits (structure, placeholders, empty data tables, no invented facts, zh-TW word lists) and, with `--filled`, whether a filled working copy is ready to send |
| [kit_figures.py](kit_figures.py) | Read-only helper: prints the tracker figures a kit needs for one period (section 5.3) |
| [test_check_kits.py](test_check_kits.py) | Unit tests for the two scripts (16 cases: each kind of invented fact, each zh-TW problem, the placeholder and data-table rules, send-ready mode, the DEMO guard and the read-only guarantee). Run: `python3 -B -m unittest discover -s monetisation/media-kits -p "test_check_kits.py" -v` |
| `.gitignore` | Keeps filled working copies and exports out of git (section 5.7) |

Every kit has the same shape: a short status block and a legend; **Part A** (operator only: the gates, the two ways to send, words not to use, statements that expire); sections **1 to 12** in two columns, zh-TW on the left and English on the right (the studio kit has sections 1 to 10); and **appendix C** (operator only: sources, unverified statements, rulings for the wife, open items). Each pilot kit covers, in order: who the character is, the audience **hypothesis**, content pillars, formats, how disclosure works (four places), what the character does and does not do, the brand-safety statement and decline list, process, deliverable examples, audience and performance figures (empty), quotes and terms in outline, contact and invoicing.

## 2. Where things stand on 2026-10-12

* There is no account, follower, image, client, registration, mailbox, handle or rate. So the kits are **a standard and a capability statement with empty data tables**, not a record of work. They contain no follower count, reach, engagement, result, client, case study, testimonial or award, and the checker fails if one appears.
* Every price is absent on purpose. The studio's own proposed prices live in the rate card (`monetisation/rate-card.md`, another Phase 8 stream) and are not in a kit; section 11 of each kit says "quoted per scope" and has a placeholder for the rate card's version.
* **Sell the creative, not the audience.** This matches the rate card's tier T0 (no audience yet): until real insights exist, the kit is sent in *mode 1* with section 10 replaced by a plain "no data yet" paragraph. Mode 2 (with figures) needs about six weeks of real platform insights, which means not before roughly the week-6 review.
* Nothing in a kit tells a brand the character is a person, has used anything, or recommends anything (Ground rules 1 and 4). Everything the character does is "presents, explains, compares and demonstrates, with dated sources".
* All Taiwan-law points are **unverified, lawyer question**. The kits describe what the studio does; they never say that it is compliant.

## 3. Where the content comes from

| Kit section | Source |
|---|---|
| 1 Who | `personas/<slug>/bible.md` 2, 4; `photoreal-addendum.md` 1 to 4; the launch persona files for bios |
| 2 Audience hypothesis | `strategy/portfolio.md` 2B (all assumptions; no Taiwan data splits platform use by interest) |
| 3 Pillars | bible 6 (example topics are the bible's draft ideas, unproduced) |
| 4 Formats | bible 6 and 8; portfolio 2C (routes); `monetisation/rate-card.md` offer families (stills only for clients) |
| 5 Disclosure | portfolio 1.4; bible 8; photoreal addenda 7 and 8; decision D6 |
| 6 Does and does not | bible 3.2, 3.4, 7 |
| 7 Brand safety | BRIEF ground rules 4 to 7; bible 9.2, 9.3 |
| 8 Process | portfolio 5.5; bible 1.4, 9.4; `launch/README.md` D8 (the public-promise limits) |
| 9 Deliverables | bible 6 and 9; `content/sehuan/b2b-pitch.md` (options); specifications only, no past work |
| 10 Figures | empty; filled only from platform insights (section 5 below) |
| 11 Terms | bible 9.4 and the rate card's standing terms (referenced, not copied) |
| 12 Contact | placeholders only; no name, address, number or ID is invented |

## 4. Before any kit is sent

1. **Close the gates** listed in Part A of the kit (name cleared, registration, lawyer answers, image-tool terms read, images that passed the checks, the wife's read). On 2026-10-12 none is closed, so no kit can be sent.
2. **Make a working copy.** Never send or edit the repo file for a send. `mkdir -p monetisation/media-kits/filled` and `cp monetisation/media-kits/fangcun.md monetisation/media-kits/filled/fangcun_YYYY-MM.md`.
3. In the copy: choose mode 1 or 2 (Part A, A2); fill or delete every placeholder; resolve every `[C2]` and `[D8]` marker (keep a D8 sentence only if the wife and the lawyer agreed); edit every expiring statement (Part A, A4); delete Part A, every OPERATOR ONLY box and appendix C.
4. `python3 -B monetisation/media-kits/check_kits.py --filled monetisation/media-kits/filled/fangcun_YYYY-MM.md` must print `0 error(s)`. It checks that no placeholder, marker or operator box is left. It **cannot** tell whether a number is true.
5. **The wife reads every zh-TW cell against the English cell and the screenshot** for each figure (digits are where transcription errors hide) and confirms no sentence claims more than the data shows.
6. Export the copy (PDF or a document) and send it by hand with a person's own message. A kit is never sent by a script, never posted, and never attached to a message Claude wrote on the sender's behalf. Record the send in the kit's refresh log (section 12) and in the lead log (`analytics/templates/lead_signals.csv`, kind `outreach_sent`).
7. If a brand names a deliverable the kit says is not offered or on hold (virtual try-on for 色環, video for clients, anything needing first-hand experience), say so and decline or rewrite the brief. Do not improvise an offer.

## 5. Monthly refresh from analytics

### 5.1 When, and who

* **When:** in the first-Friday monthly session (`ops/weekly-routine.md` section 9), **only for kits that are in use** (a brand conversation is open, or a send is planned). If no kit is in use, skip the refresh and record "skipped" in the log. Always refresh before a send, whatever the calendar says.
* **Time (assumption; measure the first one):** operator about 30 minutes per kit in use (about 10 minutes of screenshots per account, 3 to run `kit_figures.py`, 7 to type and cross-check); wife about 10 minutes; `studio.md` adds about 10 minutes and 5 minutes. This is **not yet in the weekly routine's monthly bundle** (about 90 operator and 60 wife minutes). Proposed as task M9 for `ops/weekly-routine.md` section 9 (see section 7 below). If a month is tight, skip the kit refresh before skipping M1, M2 or M3, which that routine says never to skip.
* **Who types:** the operator. The wife checks the zh-TW. Claude may draft the filled wording from numbers you paste, but never invents or rounds a number.

### 5.2 What must already exist

The weekly analytics slot (`analytics/README.md` section 4) has been run for the period, so the tracker holds post metrics and daily account numbers. If it has not, there is nothing to put in a kit: run the weekly import first. The kit's figures are a read-out of the tracker plus screenshots, not a second data entry.

### 5.3 Steps

1. **Pick the period.** One fixed window each month, the platform's "last 28 days" or "last 30 days" if it offers one, otherwise a calendar month. Write the exact start and end dates in 10.1. Keep the same window kind every month.
2. **Capture screenshots, per account, from the platform's own insights** with the date range visible: overview; reach or views; interactions (saves, shares, comments; likes kept separate); audience age and gender; audience top locations; the content list. Save them **outside the repo** as `YYYY-MM-DD_<slug>_<PLATFORM>_<PANEL>.png` in the private evidence folder (same pattern as `launch/evidence-log.csv`). Crop comment names and other personal data before a screenshot goes in any file that leaves the studio. The panel names differ by platform and have not been seen by this project (HUMAN_TODO 10); trust the live screen.
3. **Run the read-out** (read-only, no network):

   ```
   python3 -B monetisation/media-kits/kit_figures.py --start YYYY-MM-DD --end YYYY-MM-DD
   python3 -B monetisation/media-kits/kit_figures.py --persona fangcun --start YYYY-MM-DD --end YYYY-MM-DD
   ```

   It prints, per persona and platform, the posts published, the medians of saves, shares and comments, the median ER with its denominator, the last recorded followers, the AI-label record, standing events and the sponsored-post list, using the tracker's own definitions (`analytics/metrics.py`). It refuses a DEMO database unless `--demo` is given and then prints a banner: **a DEMO number never goes in a kit**. If the real database does not exist yet it says so and stops.
4. **Fill the working copy** from the field map below. Put the screenshot file name and date in every Source cell. A cell the platform did not show says "not reported by platform", never 0.
5. **Cross-check** two or three printed numbers against the screenshots (followers, one post's saves). If they disagree, fix the import, not the kit.
6. **Wife's second check** (section 4, step 5), then `check_kits.py --filled`, then add a line to the refresh log at the end of section 12 of the working copy: date, who, what changed, evidence file names, next due date.
7. **Expiry:** a figure older than 45 days (assumption) is refreshed or deleted before a send.

### 5.4 Field map: kit field, source, notes

| Kit field | Source | Notes |
|---|---|---|
| Reporting period | You choose | Same window kind every month |
| Followers or subscribers (period end) | Screenshot of the profile or insights overview; cross-check `kit_figures.py` ("last recorded day") | The tracker holds end-of-day values from `account_daily` |
| Reach or views in the period | **Screenshot only** (the platform's own period total) | Never sum daily reach: the same person would be counted many times |
| Posts published in the period | `kit_figures.py` | Counts published posts; taken-down posts are excluded |
| Median saves, shares, comments | `kit_figures.py` | Blank where the platform does not report; "not reported by platform" |
| Median ER (studio definition) | `kit_figures.py` | (saves + shares + comments) / reach, likes excluded, organic posts only. States reach or views. Fewer than 8 scored posts: say so or leave the row empty. Not comparable to ER figures that include likes |
| Link-page clicks | none yet | No counter is chosen (`strategy/portfolio.md` 6.1); leave "not reported" |
| Account standing | `kit_figures.py` and `analytics/templates/standing.csv` | Strikes, restrictions, label disputes |
| AI-label record | `kit_figures.py` | From `posts.ai_label_on`; "not recorded" is not "off" |
| Age bands, gender, top cities, share in Taiwan | **Screenshots only** | The tracker keeps two optional shares (`target_age_share`, `taiwan_share`); everything else is read from the panel. Small accounts may show no panel (unverified) |
| Representative posts | The content list screenshot plus `posts.url` | Rule in the kit: top three on one named metric, plus the weakest |
| Collaboration record | `kit_figures.py` sponsored list; `analytics/templates/revenue.csv` and `lead_signals.csv` | A brand is named only with its written permission. Money amounts never go in a kit |
| Studio: live characters, first post date, totals | `kit_figures.py` studio block | "First post" prints "assumed" until a real post exists |
| Studio: public corrections | Your own correction list | The tracker has no field for corrections. Keep a dated list (post id, date, what changed) in the evidence folder and count it |

### 5.5 Rules for every refresh

* A number goes in only if a dated screenshot or the tracker (itself fed from platform exports) shows it. Estimates, projections, "about" and rounding up are not allowed.
* Show weak numbers. Do not drop a metric because it is low; delete a row only when its source does not exist.
* Never print the internal verdicts (scale, keep, fix, retire) or the thresholds. They are the studio's own assumptions (`strategy/portfolio.md` section 6), not industry benchmarks.
* Never add figures across platforms or characters. Followers overlap.
* Sponsored, gifted and affiliate posts are excluded from the organic medians and listed separately.
* A brand name, quote, logo or screenshot of a collaboration appears only with the brand's written permission.
* If a platform change (labels, insights) alters what a field means, change the row, note it in the log, and tell the wife.
* If the studio stops using per-post human review, or any statement marked as expiring in Part A stops being true, edit the kit **before** the next send. The D8 statements are public promises.

### 5.6 What the refresh does not do

It does not change the audience hypothesis. That is rewritten only after the week-6 review, by hand, from the platform's age, gender and location panels (section 2 of each kit says so). It does not update the contract terms, prices or the decline lists; those change through the rate card, the lawyer and the bibles.

### 5.7 Where filled copies live

Filled working copies contain real numbers, and later perhaps brand names. They go in `monetisation/media-kits/filled/` (ignored by git through `.gitignore`) or outside the repo, and exports in `exports/` (also ignored). The tracked files in this folder keep placeholders only. `analytics/data/real/.gitignore` already keeps the real database out of git; `analytics/dashboard.html` is **not** ignored, so do not commit it once it holds real numbers (`analytics/README.md` section 5).

## 6. Kit formats and the rate-card offers (for quoting)

`monetisation/rate-card.md` is written by another stream and its prices are the studio's own proposed asks. This table only shows which rate-card offer each kit format would be quoted from. Check it against the rate card when that file changes.

| Kit format | Rate-card offer | Note |
|---|---|---|
| 方寸 P1 sponsored explainer; 步驟 S1; 色環 C3 | SP sponsored post by tier | A tier-0 account is sold for its creative only. Tiers 1 to 3 need the real insights these kits feed |
| 方寸 P2 and P3 | B2 room-render diagram set | Diagrams drawn by the studio; the character in a separate panel |
| 步驟 S3 | B3 explainer stills set | Stills only for clients |
| 色環 C1 and C2 | B1 (face-free options, priced with the B2 table until measured) | Virtual try-on stills (C4) are on hold |
| 步驟 S2 | none (a supplied plan or credit is a disclosure case, not a price) | |

## 7. Open items and things this stream did not do

1. **Add a monthly kit-refresh task (proposed M9)** to `ops/weekly-routine.md` section 9: operator about 30 minutes per kit in use, wife about 10, skip if no kit is in use. That file is shared and was not edited here.
2. **Add the kit gates to the launch or Phase 8 checklists** if you want them tracked in `HUMAN_TODO.md`; this stream did not edit it. The kit gates are the same as the existing items (HUMAN_TODO 4, 7, 8, 9, 18, 20, 27, 33, 34, 35, 36, 37).
3. **One studio rule for the order of the AI line and the commercial tag** is still missing (`launch/README.md` section 7 item 6). The kits state no order publicly.
4. **First caption line for posts that show 方寸**: the 方寸 addendum kept 「圖為示意」, while the 色環 and 步驟 addenda changed theirs to 「圖像為 AI 生成，並非真人」. The kits repeat each persona's current line; the wife should pick one rule.
5. **The studio paragraph in `strategy/portfolio.md` 1.3 says 「他們」** for the characters; the link page and these kits say 「角色的工作」 to avoid a gendered pronoun. Shared file, not edited.
6. **Outreach lists, outreach emails, the one-page B2B offer, the contract checklist and the revenue model** are other Phase 8 streams. Link them from sections 3 and 11 of the kits when their file names are final.
7. **A corrections list** (for the studio-level "public corrections" figure) has no home in the tracker. Decide where it lives.
8. The 24-hour take-down is an internal rule (`strategy/portfolio.md` 6.2). The kits do not state any take-down time, and `check_kits.py` fails a kit that does. Keep it that way until the lawyer has answered (`launch/README.md` D8; HUMAN_TODO 37).

## 8. Changing a kit, or adding a character

* Edit the tracked files directly for a template change (a new section, a corrected line). Keep both columns in step: a zh-TW row without its English twin fails `check_kits.py`. Re-run `python3 -B monetisation/media-kits/check_kits.py` after every edit.
* A new character (wave 2 onward) gets a kit only after it has an approved bible and a live account. Copy the closest kit, change sections 1 to 9 from its bible (pillars, formats, disclosure lines, decline list), keep sections 10 to 12 as they are, add the character to the table in `studio.md` section 2 **only when it is live**, and add it to `KITS` in `check_kits.py` and `PILOTS` in `kit_figures.py`.
* A change to the decline list or the disclosure lines starts in the bible (the bible wins) and is then copied here.

## 9. What was checked, and what was not

Checked (`test_check_kits.py` runs these cases against deliberately broken copies): `check_kits.py` passes on the four kits (structure, bilingual rows, placeholders in both languages, the data tables contain only empty placeholders, no price, follower count, e-mail, phone number, business ID or take-down time, no Simplified character, no mainland word from the project scanner, no gendered pronoun for a character in brand-facing text, backticked repo paths resolve); `kit_figures.py` runs against the DEMO database and stops cleanly when the real one does not exist.

Not checked: every zh-TW string (no native reader has seen any); every platform feature name and limit (recalled, unverified); every Taiwan-law point (unverified, lawyer question); whether any statement about the studio's process will still be true when a kit is sent (that is what the expiring-statements table in Part A is for). Web access was unavailable, so no platform help page, law or regulator page was opened.
