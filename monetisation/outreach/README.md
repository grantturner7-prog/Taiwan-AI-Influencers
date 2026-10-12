# Outreach (Phase 8): target lists, email drafts and playbook, DRAFT v0.1

Written 2026-10-12 for the operator (English) and the wife (who reads every zh-TW string and is the likely sender). Studio name 明說角色工作室 / Plainspoken Studio is provisional and uncleared.

**Where things stand on 2026-10-12: no account exists, no follower exists, the business is not registered, no image exists, no client or enquiry exists, and nothing in this folder has been sent.** The lists are **not verified**: no primary page was opened, every row is labelled `recalled` or `search summary` and says "verify existence and current contact route". Outreach is sent by the humans only; Claude only drafts. Every zh-TW string is an AI draft for the wife. All Taiwan-law points are **unverified, lawyer question**.

## 1. What is in this folder

| File | What it is |
| :-- | :-- |
| [target-list-fashion.md](target-list-fashion.md) · [.csv](target-list-fashion.csv) | Fashion, apparel and colour (showroom 色環). Includes the **warm-contact route**: the operator's roughly five fashion contacts come first; none is named because the project does not record them |
| [target-list-ai-tools.md](target-list-ai-tools.md) · [.csv](target-list-ai-tools.csv) | AI tools, productivity software and SME services (showroom 步驟): SaaS vendors with a Taiwan presence, Taiwan creative and performance agencies, tech media |
| [target-list-home.md](target-list-home.md) · [.csv](target-list-home.csv) | Home organisation, storage, furniture, home improvement and rental platforms (showroom 方寸), with HOLD and SKIP rows |
| [email-drafts.md](email-drafts.md) | zh-TW drafts with English gloss: **T1** first contact (brand), **T2** first contact (agency, platform, vendor), **T3** follow-up, **T4** reply to interest, plus **T5** opt-out confirmation and **T6** decline a brief |
| [outreach-playbook.md](outreach-playbook.md) | Gates, who sends, order and weekly time, cadence, do-not-contact rules, the tracking sheet, what to do on a reply, the consent and anti-spam note with the lawyer questions O1 to O7, data handling |
| [tracking-template.csv](tracking-template.csv) | The tracking sheet header (36 columns); copy to a git-ignored `filled/` folder to use |
| [do-not-contact-template.csv](do-not-contact-template.csv) | The do-not-contact sheet, seeded from the lists' HOLD and SKIP rows (generated) |
| [render_lists.py](render_lists.py) | Builds the three list pages, the do-not-contact seed and the counts below from the CSVs. **The CSVs are the source of truth**; never edit a generated page by hand |
| [check_outreach.py](check_outreach.py) · [test_check_outreach.py](test_check_outreach.py) | The checker and its tests (lists, drafts, playbook, links; `--filled` for a sendable copy; `--tracking` for a filled tracking sheet) |
| `.gitignore` | Keeps filled working copies out of git |

## 2. Counts and the honest shortfalls

<!-- BEGIN GENERATED:counts -->
<!-- END GENERATED:counts -->

**What the counts mean.**

* A row exists only if I am confident the entity exists and trades in Taiwan; the `existence_confidence` column says how confident (high, medium-high, medium). **No row is a verified fact.** Evidence is recall, plus search-result summaries on 2026-10-12 (marked `search summary`). A "medium" row rests on a thin summary and must be checked first.
* **Fashion and AI tools each reach 50 rows, but the reply-likely part is small.** Most rows are large or multinational (department stores, marketplaces, magazines, big agency networks, telecoms), marked P3, and unlikely to answer a two-person studio. The entities most likely to reply (small independent labels, boutique agencies and SaaS start-ups) are what I can name least confidently. The fashion page and the AI-tools page say where to find more (the operator's warm contacts, Pinkoi and Instagram, the operator's own knowledge) and how to add rows.
* **Home falls short**: see the count above. I could not name enough mid-size Taiwan furniture, custom-cabinet, renovation and home-e-commerce firms I am confident exist, and I did not pad with guesses. Three rental platforms are HOLD and six property brokerages are SKIP, listed so that nobody contacts them by mistake.
* A few entities appear in two or three lists (for example iKala, AnyMind, momo, Dcard). They count once as entities; the playbook allows **one open thread per entity and per corporate group**.
* **Dropped on purpose** (considered, not listed): entities I could not confirm (for example 凱堡 KAPOO, 歐德, 大眾搬家, Money Forward Taiwan); payment, security and finance-adjacent firms (ECPay, Trend Micro, anti-scam apps: finance adjacency or security-claim risk); ZARA, H&M and a media-buying agency (very low reply likelihood, little value); government and non-profit bodies (out of scope for now); any person (no individual creator or employee is listed).
* **Not listed, because they are not outreach targets:** affiliate programmes (Shopee, momo, PChome, Accesstrade, ValueCommerce, Rakuten, CJ). Those are applications, not pitches (`HUMAN_TODO.md` 12; rate card section 3.5).

## 3. Which file to open for which job

| If you are about to… | Open | Then |
| :-- | :-- | :-- |
| Decide whether outreach can start at all | [outreach-playbook.md](outreach-playbook.md) section 1 (gates) | Until G1 to G5 close, only private, verbal conversations with warm contacts |
| Talk to a warm fashion contact | the fashion page, "Warm-contact route", and `content/sehuan/b2b-pitch.md` A3 and A5 | Fill the W1 to W5 table with real names |
| Pick who to write to | the list page for the niche; P1 first | Do the five-minute verification; fill `verified_on` in the CSV |
| Write a first message | [email-drafts.md](email-drafts.md) T1 or T2; section 1 pre-send check | The wife reads; replace every `TO FILL`; `check_outreach.py --filled FILE` |
| Answer a reply | playbook section 7 | T4, T5 or T6; fuller decline wording is in [decline-list.md](../decline-list.md) |
| Log what happened | [tracking-template.csv](tracking-template.csv) and `analytics/templates/lead_signals.csv` | `check_outreach.py --tracking FILE` prints the funnel |
| Ask the lawyer about cold email | playbook section 8, questions O1 to O7 | Add them to the lawyer list (open item 1 below) |

## 4. Commands

```
python3 -B monetisation/outreach/render_lists.py             # rebuild the generated pages and this file's counts from the CSVs
python3 -B monetisation/outreach/render_lists.py --check     # fail if a generated file is out of date
python3 -B monetisation/outreach/check_outreach.py           # check lists, drafts, playbook, links (exit 1 on any ERROR)
python3 -B monetisation/outreach/check_outreach.py --scan    # also print every zh-TW wording flag (informational)
python3 -B monetisation/outreach/check_outreach.py --filled FILE      # a built message is ready to send: no placeholder left
python3 -B monetisation/outreach/check_outreach.py --tracking FILE    # a filled tracking sheet: values, cadence, do-not-contact, funnel
python3 -B monetisation/outreach/test_check_outreach.py      # tests
```

All standard library; no network; nothing is read outside the repository except the file you pass.

## 5. Open items (shared files are not edited by this stream)

1. **Lawyer list.** Add the outreach questions O1 to O7 (playbook section 8) to `research/legal.md` section 12 and `HUMAN_TODO.md`; O1 to O5 gate the first cold message ([Gate: outreach]).
2. **`HUMAN_TODO.md`.** Add: (a) the operator writes his five warm fashion contacts into the fashion page's W1 to W5 table; (b) both of you verify each P1 row before use and add small labels, studios and SaaS start-ups you know; (c) decide who is named in the signature and which address and response time the studio shows; (d) create the studio mailbox and the git-ignored `filled/` folder; (e) decide per recipient whether to offer the free private sample.
3. **`analytics/`.** Confirm whether `lead_signals.kind = written_quote` covers a quote the studio gives and a price the studio receives, or only one of them (playbook section 6).
4. **`monetisation/README.md`.** Its row for `outreach/` can now link the playbook and tracking sheet by name (the files exist).
5. **`SOURCES.md`.** The 2026-10-12 search summaries behind some rows (KEYWAY and SHUTER sold via momo and Yahoo; Searchome under 麥浩斯/城邦; 好房網 under 永慶; NITORI MALL plan; 特力屋 listing report; awoo, Yoctol, Rosetta.ai, Ragic, TenMax, AD2, Wavenet, Hakuhodo/Growww) are not recorded there yet. They are search-result summaries, not opened pages.
6. **Wife.** Read every zh-TW line of the drafts and rule on the points in email-drafts section 9.
