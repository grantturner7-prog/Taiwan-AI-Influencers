# Monetisation folder (Phase 8): index and gates

Written 2026-10-12 for the operator (English, with the zh-TW term beside each Taiwan-specific concept), for the wife who reads every zh-TW string, and for the lawyer and 記帳士 who will be asked the questions. Studio name 明說角色工作室 / Plainspoken Studio is provisional and uncleared. Pilots: 方寸 (home organisation, Instagram and YouTube Shorts), 步驟 (AI tools, YouTube Shorts and Threads), 色環 (outfit logic and colour, Instagram and Threads).

**Where things stand on 2026-10-12: no account exists, no follower exists, the business is not registered, no image exists, no client or enquiry exists, and nothing in this folder has been sent, posted, offered or signed.** Everything here is a draft, every zh-TW string is an AI draft for the wife, and every Taiwan-law point is **unverified, lawyer question**.

---

## 0. Read this first

1. **What this folder is.** The Phase 8 monetisation kit of `BRIEF.md` section 6: media kits, a rate card, a revenue model, outreach lists and emails, a one-page B2B offer, a sponsorship contract checklist and a decline list. It is a kit to be used later, not a record of work.
2. **No number here is market data.** Phase 1 found no Taiwan price, 業配 rate, CPM, commission, payout threshold, spokes-character fee or price for AI creative (`research/monetisation.md` sections 0 and 3). Every price in this folder is the studio's own **proposed** figure, labelled **assumption**, derived from stated hours, an assumed hourly value, an image-tool cost and a margin, and it must be recalibrated against three or more real quotes before it is used (`rate-card.md` sections 1 and 5). The revenue model is arithmetic on stated assumptions and promises nothing.
3. **Sell the creative, not the audience.** A character with no audience has no reach to sell. The studio's B2B services are the route the research ranks first for year 1, and it is **unproven** (`research/SUMMARY.md` section ii).
4. **The humans send; Claude only drafts.** Outreach, quotes, contracts, replies and declines are sent or signed by the user or the wife, by hand, from a studio mailbox that does not exist yet.
5. **The characters are openly AI.** Nothing in this folder presents a character as a person or as having used, worn, tested or visited anything. Every sponsored, affiliate or gifted deliverable is disclosed: the paid-content line (【業配】 or 【合作內容】, 【廠商提供】, 【含分潤連結】), the platform's paid-partnership tool, and the AI label.
6. **Nothing is invented.** No client, case study, testimonial, award, follower count, reach or engagement figure, contact name, e-mail address, phone number or registration number appears in any file. Missing data is a marked placeholder. A brand or agency is named only if it is real and well known, with 'verify existence and current contact route before outreach'.

## 1. What is in the folder

| File or folder | What it is | Stream and status | Read by |
|---|---|---|---|
| [README.md](README.md) | This index and the gates | Offer and contract stream; written 2026-10-12 | Everyone |
| [studio-offer.md](studio-offer.md) | The one-page B2B offer, zh-TW and English (Part B), with an operator-only Part A (gates, how to make a sendable copy, words not to use) and appendix C (unverified statements, rulings for the wife) | Offer and contract stream; draft v0.1; **ten gates open** | Operator, wife, lawyer |
| [sponsorship-contract-checklist.md](sponsorship-contract-checklist.md) | The contract checklist for sponsorship and B2B deals: about 90 clause rows with the studio's position, the source, a 'lawyer to confirm' column, a red-flag screen for a brand's own draft, a pre-signature gate, draft zh-TW clause lines and the lawyer's question list (existing Q numbers plus eight proposed) | Offer and contract stream; draft v0.1 | Operator, wife, lawyer, 記帳士 |
| [decline-list.md](decline-list.md) | Categories and briefs to refuse, each mapped to a Ground rule or bible section, a five-question screen, 15 polite zh-TW decline templates with English gloss, conditions for class B, and a blank decline log | Offer and contract stream; draft v0.1 | Operator, wife |
| [rate-card.md](rate-card.md) | The studio's proposed prices (offers B1 to B3, SP, own products, stickers), the pricing method, the standing terms, the quote-recalibration plan (3+ real quotes) and zh-TW quote lines. **Tables are generated from `assumptions.csv`** | Revenue stream; draft v0.1 | Operator, wife. Internal; no price leaves the house before the gates |
| [revenue-model.md](revenue-model.md) | Low, middle and high 12-month scenarios, month-by-month cash, break-even and sensitivity, with every assumption sourced or marked. **Generated tables** | Revenue stream; draft v0.1 | Operator |
| [assumptions.csv](assumptions.csv) · [model.py](model.py) · [test_model.py](test_model.py) · [monthly-cash.csv](monthly-cash.csv) | The inputs, the engine, 103 unit tests and the month-by-month output for a spreadsheet | Revenue stream | Operator |
| [media-kits/](media-kits/) | A kit per pilot (`fangcun.md`, `buzhou.md`, `sehuan.md`) and an umbrella kit (`studio.md`) in zh-TW and English with empty data tables; `README.md` (refresh from analytics, how to send); `check_kits.py`, `kit_figures.py`, `test_check_kits.py`; `.gitignore` (keeps filled copies out of git) | Media-kit stream; draft v0.1 | Operator, wife |
| [outreach/](outreach/) | Target lists for fashion, AI tools and home brands and agencies (each as `.md` and `.csv`), zh-TW email drafts with English gloss, and their render and check scripts. Its own playbook and tracking sheet are listed in the outreach stream's files (see section 8 item 4) | Outreach stream; status is that stream's to report | Operator, wife |

Companion material outside this folder: `research/monetisation.md`, `research/legal.md` and `research/SUMMARY.md` (the evidence and the lawyer's question list), `strategy/portfolio.md` (2C routes, 6.4 revenue checkpoint, 7 costs), `personas/<slug>/bible.md` and `personas/<slug>/photoreal-addendum.md` (decline lists and contract points, section 9), `content/sehuan/b2b-pitch.md` (the fashion pitch and the face-free options), `launch/README.md` (decision D8, the public promises), `analytics/` (the tracker the kits read from), `ops/` (risks, crisis playbook, weekly routine).

## 2. Which file to open for which job

| If you are about to… | Open | Then |
|---|---|---|
| Decide whether to answer a sponsor or a brief | `decline-list.md` sections 1 to 3 | If declined, a template in section 4; log it (section 6) |
| Tell a brand what the studio sells | `studio-offer.md` Part B (a filled copy, never the repo file) | Part A, A3 to make the copy |
| Show a brand a character | The character's kit in `media-kits/` and `media-kits/README.md` section 4 | `check_kits.py --filled` |
| Write the first message to a brand or agency | `outreach/email-drafts.md` and the target list for the niche | The outreach playbook gates |
| Quote a price | `rate-card.md` sections 1, 3 and 6, after section 5 (3+ real quotes) | A separate written quote; no price goes on the offer page or in a kit |
| Draft or review a contract | `sponsorship-contract-checklist.md` sections 3 to 5 | The lawyer (Q24); sign nothing before section 5 of that file is ticked |
| Judge whether the studio can afford a decision | `revenue-model.md` sections 1, 8 and 9 | `model.py` |
| Know what is still blocked | Section 3 and section 8 of this file | `HUMAN_TODO.md` |

## 3. The gates: nothing is sent until all three are true

**Nothing in this folder is sent, posted, offered, quoted or signed until all three of these are true.** This is the folder-wide rule; the files add their own supporting gates.

| Gate | Meaning | State 2026-10-12 | Where |
|---|---|---|---|
| **G1. Registration** | The business is registered; the registrant (the wife is the likely one) and the invoice route are settled with a 記帳士; the answer to 'which income can be received before registration' is in hand. Only the registered business invoices or signs | OPEN. Not started | `HUMAN_TODO.md` 4, 7; `research/legal.md` Q14, Q15, Q17 |
| **G2. The lawyer's launch-gate answers** | A Taiwan lawyer has answered the launch-gate questions: whether a disclosed character is an endorser (Q1), what wording lets it present without testifying (Q2), the Fair Trade Act text and fines (Q3), accepted disclosure wording and placement including gifted goods and affiliate links (Q4), the AI Basic Act (Q6), entity type (Q14), likeness diligence (Q20) and the PDPA (Q22), plus the photoreal-labelling and likeness questions in `HUMAN_TODO.md` 37. Q10 and Q12 apply only to the lawyer-gated characters (歸位, 等一下). **Before any price, contract or boosted post, the paid-gate set as well:** Q5, Q8, Q9, Q19, Q21, Q24 | OPEN. No lawyer retained; nothing asked | `HUMAN_TODO.md` 9, 27, 37, 47; `research/legal.md` section 12 |
| **G3. Real accounts with real metrics** | The characters' accounts are live and platform insights exist (about six weeks of posts, `strategy/portfolio.md` 6.1). Any figure in any document comes from a dated screenshot or the tracker, never from an estimate, and a number from the DEMO database never leaves the repo | OPEN. No account exists | `launch/README.md`; `analytics/README.md`; `media-kits/README.md` section 5 |

**Supporting gates**, needed before the documents they touch (each is in the file's own Part A):

| Gate | Needed before | Where |
|---|---|---|
| The studio name is cleared (the wife's reading test, TIPO and 經濟部 searches) | Any document that carries the name | `HUMAN_TODO.md` 18, 20 |
| The image tools' commercial-use terms are read and recorded. **Until then no client work, no free sample and no sponsored post** | The offer, a sample, a quote | `HUMAN_TODO.md` 33 |
| Character images exist and passed the adult-reading, age-guess and look-alike checks | Anything that shows a character | `HUMAN_TODO.md` 34, 36 |
| The wife has read every zh-TW string; the D8 public statements are ruled on by the wife and the lawyer | Everything in zh-TW | `HUMAN_TODO.md` 8, 35; `launch/README.md` D8 |
| At least three real quotes per offer family have been collected and the rates recalibrated | Any number to a brand | `rate-card.md` section 5; `HUMAN_TODO.md` 11 |
| The lawyer has answered the try-on questions | The virtual try-on row (**ON HOLD**) | `HUMAN_TODO.md` 27, 37 |

**Which document needs what**

| Document | G1 | G2 launch | G2 paid | G3 | Name | Tool terms | Images | Wife | 3+ quotes |
|---|---|---|---|---|---|---|---|---|---|
| `studio-offer.md` Part B | Yes | Yes | Yes | Yes | Yes | Yes | Only if a character is shown | Yes | Before any quote |
| A media kit (`media-kits/`) | Yes | Yes | Q8 and the D8 rulings | Yes (mode 2 needs about six weeks of insights) | Yes | Yes | Yes | Yes | No |
| Outreach emails (`outreach/`) | Yes | Yes | See the outreach playbook | Yes | Yes | If a sample is offered | No | Yes | No |
| A quote (`rate-card.md` section 6) | Yes | Yes | Yes | Yes | Yes | Yes | If a face is shown | Yes | Yes |
| A contract (`sponsorship-contract-checklist.md`) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| A decline reply (`decline-list.md`) | Not needed to say no | Not needed | Not needed | n/a | n/a | n/a | n/a | Yes | n/a |

**Two points to read before relying on this table.**

* **The kits are looser than this rule.** `media-kits/README.md` section 2 lets a kit go out in 'mode 1' (no data, a plain 'new, nothing to show yet' paragraph) once accounts are live, without metrics. The rule above is stricter: it asks for real metrics. Until the user decides otherwise, **this README's stricter rule applies**. If the user wants mode 1, that is a decision to record in `DECISIONS.md`; no file here changes it.
* **A decline reply** says no and offers nothing, so it needs only the wife's read, a studio mailbox and a person to send it. It is not an exception to the rule above for any other message. An inbound enquiry cannot arrive before an account or a mailbox exists.

## 4. Rules that hold in every file here

* **Disclosure.** Four places: bio, first caption line, on-screen badge, platform AI label, on every post. Sponsored, affiliate and gifted content adds the paid-content line and the platform tool. A brand may not ask for any label to be removed, shrunk or moved.
* **No testimonial, no invented experience.** The character presents, explains, compares and demonstrates, with dated sources.
* **Out of scope at any price.** Health, medical, weight-loss and cosmetic-efficacy claims; supplements; investment and financial products including any referral link; gambling; politics, elections and cross-strait content; loan apps; face-swap, voice-cloning or any deepfake-capable tool; anything illegal. See `decline-list.md`.
* **No promised outcome.** No reach, engagement, followers, clicks or sales are promised or implied.
* **Prices** are the studio's own proposals, labelled assumption, with the stated logic, or sourced with their confidence label. No price is on the offer page or in a kit.
* **Registration.** Only the registered business invoices or signs; tax treatment and invoice type are `[TO FILL WHEN REAL]` and a 記帳士 question.
* **Taiwan law.** Every point is 'unverified, lawyer question'. The files say what the studio does, never that it is compliant.
* **zh-TW.** Traditional Chinese with Taiwan vocabulary (影片, 資訊, 品質, 專案, 軟體, 網路, 合約), every string a draft for the wife.

## 5. Shared terms (so the files say the same thing)

| Term | zh-TW (DRAFT) | Meaning and where it is fixed |
|---|---|---|
| AI line | 「【AI 虛擬角色】本篇由 AI 生成的虛擬角色「{角色名}」發布，…」 | First caption line; per character in each kit, section 5. The three characters still differ on the picture sentence (`media-kits/README.md` section 7 item 4) |
| Paid post | 【業配】 | Sponsored post; the character has not used the product |
| Collaboration content | 【合作內容】 | Client creative or a demo posted on a character's account |
| Supplied by the brand | 【廠商提供】 | Gifted goods or a vendor-supplied plan |
| Affiliate link | 【含分潤連結】 | The studio may earn a commission |
| Correction | 【更正】{YYYY/MM/DD} | A dated public correction |
| Badges | 「AI 生成｜虛擬角色」, 「AI 生成｜示意圖」, 搭配示意, 示意圖, 虛擬試穿示意 (ON HOLD) | On-image labels typeset by a person |
| Screen-recording label | 「錄製條件」 or 「測試條件」 | **Open** (`HUMAN_TODO.md` 25: the 測 family is on the banned list); the offer uses 「錄製條件」 and marks it for the wife |
| Order of the AI line and the paid tag | | **Open studio rule** (`HUMAN_TODO.md` L9); contracts refer to a labelling-instructions annex so the rule can change |

## 6. Offer IDs across the files

| ID | Offer | `rate-card.md` | `studio-offer.md` | Contract rows | Status |
|---|---|---|---|---|---|
| B1 | Fashion lookbook: face-free options (colour-story board; flat-lay or dress-form layout) | 3.1 | 2.1 | B1 to B8, F1 to F16 | Not yet offered; priced with the B2 table until measured |
| B1 | Fashion lookbook: labelled virtual try-on stills | 3.1 | 2.2, section 8 | D8, F12 | **ON HOLD** (lawyer, `HUMAN_TODO.md` 27, 37) |
| B2 | Room-render diagram set (home and storage; vector diagrams, not photoreal rooms) | 3.2 | 2.3 | As B1 | Not yet offered |
| B3 | Software explainer card set (stills only) | 3.3 | 2.4 | As B1 | Not yet offered |
| SP | Sponsored post (業配) by tier, production price only | 3.4 | 2.5 | C2, C3, E6, H5 | Not before accounts are live with real figures |
| AF | Affiliate | 3.5 | n/a | C7 | Programme terms unchecked (`HUMAN_TODO.md` 12) |
| P1 to P3 | Own digital products | 3.6 | n/a | n/a | Not before the 記帳士 answers |
| n/a | LINE stickers | 3.7 | n/a | n/a | Later, uncertain |
| L | Character licensing, spokes-character | 3.8 | n/a | Discuss only | No price; nothing to sign |

## 7. Conventions, filled copies and checks

* **Two placeholder styles exist.** The kits, the offer and the contract checklist use 【待填：…】 with its English twin `[TO FILL WHEN REAL: …]`; the outreach drafts use `[… : TO FILL]` slots. Each stream's checker knows its own style. Do not mix them in one file.
* **Filled copies never go in the repo with real data.** Make them in `monetisation/media-kits/filled/` (git-ignored by `media-kits/.gitignore`) or outside the repo. A filled copy may carry a brand name, a contact, a quote reference or a number. A folder-level `.gitignore` would be safer; it was not added because only the named files were in scope.
* **Generated files.** The tables in `rate-card.md` and `revenue-model.md` are generated from `assumptions.csv`; change the assumption, never the table.
* **Commands** (read-only, no network; `-B` keeps bytecode out of the folder):

```
cd monetisation
python3 -B model.py docs --check                         # are the generated tables current?
python3 -B -m unittest test_model                        # 103 model tests
cd ..
python3 -B monetisation/media-kits/check_kits.py         # structure and word checks on the four kits
python3 -B monetisation/media-kits/check_kits.py --filled monetisation/media-kits/filled/<file>.md
                                                         # send-ready check of a filled copy of a kit or of studio-offer.md
```

## 8. Open items for the whole folder

1. **All three gates are open.** Registration, the lawyer and live accounts with real metrics (section 3).
2. **Gate wording differs between the kits and this README** (kits mode 1 against the stricter rule here). The user decides; nothing is changed until then.
3. **The correction and take-down time is inconsistent.** `rate-card.md` sections 2 and 6 state '24 hours' in a client-facing line; the kits, the studio page and `check_kits.py` deliberately state no number until the lawyer answers. The offer and the contract checklist follow the kits (proposed lawyer question NEW-3). The rate card is another stream's file and was not edited.
4. **The outreach stream's index.** This README lists the files found in `outreach/` on 2026-10-12. Its playbook, tracking sheet and checker are that stream's to complete; update this table and the 'Which document needs what' row when their names are final.
5. **Shared files that need edits, and were not edited here** (only `monetisation/` was in scope): `research/legal.md` section 12 (add NEW-1 to NEW-8 from `sponsorship-contract-checklist.md` section 7.2, and the try-on and comparative-advertising questions of `HUMAN_TODO.md` 27); `HUMAN_TODO.md` (a line for the paid-gate lawyer set and for the decline-log home); `ops/weekly-routine.md` section 9 (the monthly kit-refresh task M9 proposed in `media-kits/README.md` section 7, and a monthly read of the decline log); `analytics/templates/lead_signals.csv` (no 'declined' kind); `media-kits/studio.md` and the three character kits (link to the offer and the contract checklist from sections 3 and 9; the kits are another stream's files).
6. **The sponsor ledger** (same brand not on two characters in one ISO week) has no home in the tracker (`strategy/portfolio.md` 3.3).
7. **Capacity.** B2B jobs compete with the characters for the same hours; revenue work is cut first. The plan is not shown to fit (`HUMAN_TODO.md` 43, 46; `revenue-model.md` section 14).
8. **Evidence.** No primary law or platform page was opened in Phase 1 or since; every platform tool name and every Taiwan-law point is recalled or second-hand.

## 9. What was checked on 2026-10-12, and what was not

Checked (read-only): the generated tables of `rate-card.md` and `revenue-model.md` are in sync with `assumptions.csv`; the 103 model tests pass; `check_kits.py` reports 0 errors on the four kits; the four files written by the offer and contract stream were scanned with the project's zh-TW word lists (`pipeline/scripts/ground_rules.py`) for mainland vocabulary and Simplified characters, and for invented figures, e-mail addresses, phone numbers and registration-number shapes; internal links and backticked paths were resolved.

Not checked: every zh-TW string by a native reader (none has seen any); every platform feature name; every Taiwan-law statement; whether any demand exists for the services; the outreach stream's files beyond listing them.

## 10. Update log

| Date | By | What changed |
|---|---|---|
| 2026-10-12 | Offer and contract stream | README, studio-offer, sponsorship-contract-checklist and decline-list written (draft v0.1) |
