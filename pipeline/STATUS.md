# STATUS: what exists and what is blocked (2026-10-12, updated after the recommended answers were adopted)

Plain-English snapshot after the Phases 4 to 9 build and the adoption of the recommended answers. Nothing is published, approved or registered. No image, video or voice exists. All zh-TW text is an AI draft for the wife. Platform, price and Taiwan-law facts are recalled or unverified unless a file says otherwise.

**Adopted on your behalf on 2026-10-12 (Claude's choices within your delegation, each reversible; `DECISIONS.md`, last entry):** launch decisions D1 to D9 at their defaults (`launch/README.md` section 5); **D6** yes, a still (or a slow pan or zoom of a still) of the photoreal character may appear inside a Reel or Short with the platform AI label on, a persistent 「AI 生成｜虛擬角色」 badge, no animation of the face and no synthetic voice (face animation, voice and lip-sync stay barred); **the graphics decision**, Claude draws the diagram, lesson-graphic and overlay layers as SVG rendered to PNG, you and your wife still approve every asset, Claude cannot edit video; **OPS-D1**, 12 approvals a week combined through the first 8 weeks (12 slots in weeks 3 and 4 deferred). To reverse any of them, tell Claude.

## 1. What exists now

| Area | What exists | Checked by | Blocked on |
|------|-------------|-----------|-----------|
| Image pipeline (`pipeline/`) | tools shortlist and cost model, QA checklist, image prompt packs for 3 pilots, provenance log, `gen_image.py` (inert without a key, untested against live APIs), review-queue scripts | 130 unit tests pass; `queue.py validate` over 21 drafts: 0 errors, 0 flags | API key and allowed domains (or the app route), licence terms read, model ids |
| Graphics layer (Claude-drawn SVG) | Only the 步驟 v0.1 front view and picture-in-picture art (`pipeline/art/buzhou_front.py`). The Diagram Kit v0, lesson kit and overlay layers are specified in the calendars but **not drawn yet** | n/a | Claude to draw them; then you and your wife approve each asset (`pipeline/qa-checklist.md` T9); a Taiwan-glyph font on the render machine (Noto Sans TC not found there on 2026-10-12); operator review and video assembly minutes (not in any capacity total) |
| Review queue (`pipeline/review-queue/`) | 21 drafts: 方寸 5, 步驟 8 (4 Threads, 4 Shorts), 色環 8. All `ai_label_flag` true, review pending/pending/false, media PENDING, empty `media/`. 方寸 P02, P03 and P04 (a still inside a Short or Reel) are now **ready for review** under D6, not approved | Checked again by the integrator | Wife and operator review; images; placeholders (below). Still held for other reasons: 方寸 P05 (坪 source), the four 步驟 Shorts (vendor terms and unfilled fields), 色環 P03, P07, P08 (source placeholders) |
| 方寸 content (`content/fangcun/`) | 30-day calendar (18 posts after OPS-D1; P13, P14, P19, P20 deferred), hook library, series, trend check, reply guide, `verify.py` | `verify.py`: 0 errors, 1 warning | Source for 坪 (blocks P05, P06, P09); the diagram layer to be drawn by Claude and approved; operator review and video assembly time |
| 步驟 content (`content/buzhou/`) | 30-day calendar (18 posts after OPS-D1; masters M7 and M8 cut), hooks, series, replies, `verify.py` | 0 errors, 7 warnings (unfilled vendor fields, by design) | Vendor pages read and filled in; recordings and stills; the four Shorts stay on HOLD for vendor terms and unfilled fields (D6 no longer holds them); the operator assembles the video |
| 色環 content (`content/sehuan/`) | 30-day calendar (18 posts after OPS-D1; masters M5 and M10 deferred), hooks, replies, B2B pitch (docs only), `verify.py` | `verify.py`: 0 errors, 5 warnings | Sources for P03, P07, P08; golden-set stills; the Lesson Kit to be drawn by Claude and approved; wife design rulings |
| Launch (`launch/`) | studio setup, account checklists per persona, 4 static link pages, scheduler slot check (54 slots after OPS-D1, `--with-deferred` shows the 66), templates, empty logs; D1 to D9 adopted | `check_launch_docs.py`, `schedule_check.py`, `check_pages.py` pass in draft mode (`--final` fails on purpose: 15 placeholders) | Accounts, handles, avatars, host and domain, studio mailbox, gates A1 to A7; the wife and the lawyer on the two (three) public promises (D8) |
| Analytics (`analytics/`) | importer, metrics, decision tree, weekly report, dashboard (DEMO data only; real dashboard says NO DATA YET) | 139 tests pass | Real data; thresholds confirmed; link-click counter; time and verdict logging |
| Ops (`ops/`) | weekly routine (12-approval week), 33-risk register (PHO-9 re-scored as a proposal), crisis playbook with 11 draft statements | Dates and minute totals recomputed | Lawyer not retained; studio mailbox and vault; wife rulings on statements; OPS-D2 and OPS-D4 to D7 still to confirm (OPS-D1 adopted) |

## 2. Blocked, by who unblocks it

* **Image generation:** no tool in this session. The app route works now; the API route needs a key (HUMAN_TODO 39). No photoreal face has been generated, so no age-guess, look-alike or near-pair test has run.
* **Accounts and handles:** none created. Needs the reading test, TIPO and 經濟部 searches, handle checks (HUMAN_TODO 18 to 21) and a human to pass phone or ID checks (L5).
* **Registration and lawyer:** business registration not started; lawyer not booked; the launch-gate answers (HUMAN_TODO 9, 37) are open.
* **Reviewer rulings:** the wife has not read any zh-TW string. Rulings are listed in each calendar and in HUMAN_TODO 45.
* **Facts:** every source URL/date is a placeholder (UNVERIFIED-OPERATOR-TO-FILL). Polling date 2026-11-28 and all platform limits are unverified.
* **Capacity:** the hold at 12 approvals a week (OPS-D1) and Claude drawing the graphics remove the operator's build time, but the operator's review of every Claude-drawn asset and the assembly of every Reel and Short are in no capacity total, and the three pilot calendars put them at 164 to 321 minutes a week against 45 minutes of slack (`ops/weekly-routine.md` 2.2 to 2.4). So the plan is not shown to fit even at 12. W0 2026-11-16 is still unlikely (`launch/README.md` section 4).
* **Video:** under D6 only a still (or a slow pan or zoom of a still) with the label, the persistent badge, no face animation and no synthetic voice. Claude cannot edit video: the operator assembles every Reel and Short. Face animation, voice and lip-sync stay barred until a separate video addendum and review exist; D6 has not been put to the lawyer (HUMAN_TODO 37).

## 3. Next 10 steps, in order

1. Read the answers adopted on your behalf (D1 to D9, D6, the graphics decision, OPS-D1) and tell Claude which, if any, to reverse (HUMAN_TODO 53). Each reversal changes files, so do this before the week-1 batch is drafted.
2. Wife: reading test of 明說角色工作室 and the three persona names; operator: TIPO and 經濟部 searches and logged-out handle checks (HUMAN_TODO 18 to 21).
3. Book the lawyer (and 記帳士); ask the launch-gate questions, including the D6 question (a still with a slow pan or zoom inside a Reel or Short, with the label and badge), an after-hours contact and the urgent-letter fee (HUMAN_TODO 9, 37, 47).
4. Record the commercial-use terms of the image tool and plan you will use (HUMAN_TODO 33). Until then every image is internal design material.
5. Generate the golden sets (方寸 R01, R06, R13 and headshots; 步驟 and 色環 sets) in the app, or add the API key (HUMAN_TODO 39 to 42); log each in `assets/provenance.csv`; run the age-guess, look-alike and near-pair tests. Claude cannot generate photoreal images.
6. Ask Claude to draw Diagram Kit v0, the Lesson Kit and the overlay layers as SVG and render them to PNG (the graphics decision); install a Taiwan-glyph font on the render machine first; then you and your wife approve each asset (`pipeline/qa-checklist.md` T9). Claude cannot edit video: you assemble the Reels and Shorts.
7. Fill the source placeholders from the real pages: 坪 definition, weather-agency page, 平量/圍度 definition, vendor pages (HUMAN_TODO 44).
8. Wife: review all zh-TW drafts and word lists (HUMAN_TODO 3 area, 41, 45), including the badge wording in video; operator: fact-check each draft and run `pipeline/qa-checklist.md` 6.1 on every Reel and Short; run `queue.py validate` after every edit.
9. Studio mailbox, password manager and two-factor method; then create accounts one persona per sitting, do the Instagram AI-label check inside the real 方寸 account on its creation day (D1) and the scheduling dry runs (L2, L5, L6, 38); build the link pages' real values and deploy; start business registration; settle the ops pre-launch controls (HUMAN_TODO 48).
10. Set W0 at a gate review (L12), re-date the review-queue folders if it moves, and start the 30-day run at 12 approvals a week with real minute logging, including graphics review and video assembly; run `analytics/tracker.py import-queue` after each review session. Decide any step up from 12 only at the week-8 review.

## 4. Commands (all offline)

* `python3 pipeline/scripts/queue.py validate` and `list`
* `python3 -m unittest discover -s pipeline/scripts`
* `python3 -m unittest discover -s analytics/tests`
* `python3 content/{fangcun,buzhou,sehuan}/verify.py`
* `python3 launch/check_launch_docs.py`, `python3 launch/schedule_check.py` (add `--with-deferred` for the superseded 66-slot plan), `python3 launch/link-pages/check_pages.py`
