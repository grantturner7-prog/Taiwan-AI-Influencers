# STATUS: what exists and what is blocked (2026-10-12)

Plain-English snapshot after the Phases 4 to 9 build. Nothing is published, approved, registered or committed. No image, video or voice exists. All zh-TW text is an AI draft for the wife. Platform, price and Taiwan-law facts are recalled or unverified unless a file says otherwise.

## 1. What exists now

| Area | What exists | Checked by | Blocked on |
|------|-------------|-----------|-----------|
| Image pipeline (`pipeline/`) | tools shortlist and cost model, QA checklist, image prompt packs for 3 pilots, provenance log, `gen_image.py` (inert without a key, untested against live APIs), review-queue scripts | 130 unit tests pass; `queue.py validate` over 21 drafts: 0 errors, 0 flags | API key and allowed domains (or the app route), licence terms read, model ids |
| Review queue (`pipeline/review-queue/`) | 21 drafts: 方寸 5, 步驟 8 (4 Threads, 4 Shorts), 色環 8. All `ai_label_flag` true, review pending/pending/false, media PENDING, empty `media/` | Checked again by the integrator | Wife and operator review; images; placeholders (below) |
| 方寸 content (`content/fangcun/`) | 30-day calendar (22 posts), hook library, series, trend check, reply guide, `verify.py` | `verify.py`: 0 errors, 1 warning | Source for 坪 (blocks P05, P06, P09); still-face-in-video decision (P02, P03, P04, P06, P08); diagram build time |
| 步驟 content (`content/buzhou/`) | 30-day calendar (22 posts), hooks, series, replies, `verify.py` | 0 errors, 7 warnings (unfilled vendor fields, by design) | Vendor pages read and filled in; recordings and stills; editing time; the Shorts are on HOLD |
| 色環 content (`content/sehuan/`) | 30-day calendar, hooks, replies, B2B pitch (docs only), `verify.py` | 0 errors, 5 warnings | Sources for P03, P07, P08; golden-set stills; Lesson Kit build time; wife design rulings |
| Launch (`launch/`) | studio setup, account checklists per persona, 4 static link pages, scheduler slot check, templates, empty logs | `check_launch_docs.py`, `schedule_check.py`, `check_pages.py` pass in draft mode (`--final` fails on purpose: 15 placeholders) | Accounts, handles, avatars, host and domain, studio mailbox, gates A1 to A7 |
| Analytics (`analytics/`) | importer, metrics, decision tree, weekly report, dashboard (DEMO data only; real dashboard says NO DATA YET) | 139 tests pass | Real data; thresholds confirmed; link-click counter; time and verdict logging |
| Ops (`ops/`) | weekly routine, 33-risk register, crisis playbook with 11 draft statements | Dates and minute totals recomputed | Lawyer not retained; studio mailbox and vault; wife rulings on statements; OPS-D1 capacity decision |

## 2. Blocked, by who unblocks it

* **Image generation:** no tool in this session. The app route works now; the API route needs a key (HUMAN_TODO 39). No photoreal face has been generated, so no age-guess, look-alike or near-pair test has run.
* **Accounts and handles:** none created. Needs the reading test, TIPO and 經濟部 searches, handle checks (HUMAN_TODO 18 to 21) and a human to pass phone or ID checks (L5).
* **Registration and lawyer:** business registration not started; lawyer not booked; the launch-gate answers (HUMAN_TODO 9, 37) are open.
* **Reviewer rulings:** the wife has not read any zh-TW string. Rulings are listed in each calendar and in HUMAN_TODO 45.
* **Facts:** every source URL/date is a placeholder (UNVERIFIED-OPERATOR-TO-FILL). Polling date 2026-11-28 and all platform limits are unverified.
* **Capacity:** diagram/lesson/editing build time is not in the portfolio model (HUMAN_TODO 43). W0 2026-11-16 is unlikely (launch/README.md section 4).

## 3. Next 10 steps, in order

1. Decide the three open choices that change the files: still faces inside Reels/Shorts (launch D6), who builds diagrams and lesson graphics (HUMAN_TODO 43), and hold at 12 approvals a week (HUMAN_TODO 46). Everything else in the calendars depends on these.
2. Wife: reading test of 明說角色工作室 and the three persona names; operator: TIPO and 經濟部 searches and logged-out handle checks (HUMAN_TODO 18 to 21).
3. Book the lawyer (and 記帳士); ask the launch-gate questions, an after-hours contact and the urgent-letter fee (HUMAN_TODO 9, 37, 47).
4. Record the commercial-use terms of the image tool and plan you will use (HUMAN_TODO 33). Until then every image is internal design material.
5. Generate the golden sets (方寸 R01, R06, R13 and headshots; 步驟 and 色環 sets) in the app, or add the API key (HUMAN_TODO 39 to 42); log each in `assets/provenance.csv`; run the age-guess, look-alike and near-pair tests.
6. Fill the source placeholders from the real pages: 坪 definition, weather-agency page, 平量/圍度 definition, vendor pages (HUMAN_TODO 44).
7. Wife: review all zh-TW drafts and word lists (HUMAN_TODO 3 area, 41, 45); operator: fact-check each draft; run `queue.py validate` after every edit.
8. Studio mailbox, password manager and two-factor method; then create accounts one persona per sitting, run the Instagram AI-label test and scheduling dry runs (L2, L5, L6, 38).
9. Build the link pages' real values and deploy; start business registration; settle the ops pre-launch controls (HUMAN_TODO 48).
10. Set W0 at a gate review (L12), re-date the review-queue folders if it moves, and start the 30-day run with real minute logging; run `analytics/tracker.py import-queue` after each review session.

## 4. Commands (all offline)

* `python3 pipeline/scripts/queue.py validate` and `list`
* `python3 -m unittest discover -s pipeline/scripts`
* `python3 -m unittest discover -s analytics/tests`
* `python3 content/{fangcun,buzhou,sehuan}/verify.py`
* `python3 launch/check_launch_docs.py`, `python3 launch/schedule_check.py`, `python3 launch/link-pages/check_pages.py`
