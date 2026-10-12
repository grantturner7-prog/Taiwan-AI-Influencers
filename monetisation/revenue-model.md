# Revenue model (Phase 8), DRAFT v0.1

Written 2026-10-12 for the operator (English, with the zh-TW term beside each Taiwan-specific concept) and for the wife. Studio name 明說角色工作室 / Plainspoken Studio is provisional and uncleared. Pilots: 方寸 (home organisation), 步驟 (AI tools), 色環 (outfit logic and colour). No account exists, no follower exists, the business is not registered and no image exists.

**No outcome is promised.** This is arithmetic on stated assumptions. It is not a forecast, a target or a commitment, and nobody should plan a purchase or a decision on the strength of a single cell. Phase 1 found no Taiwan rate, commission, payout or engagement benchmark for any route (`research/monetisation.md` section 0), so every input is a sourced figure from a project file, a Phase 1 hypothetical axis value, the studio's own planning assumption or a placeholder. Companion files: [rate-card.md](rate-card.md) (the proposed prices), [assumptions.csv](assumptions.csv) (every input), [model.py](model.py) (recomputes everything) and [test_model.py](test_model.py) (unit tests). The tables below are **generated** by `python3 model.py docs --write`; change an assumption in the CSV, regenerate and read the changed tables. Do not edit the generated tables by hand (a test fails if they drift).

---

## 0. Read this first

1. **The Phase 1 hypothesis range is NT$0 to about NT$200,000 of studio revenue in 12 months** (`research/monetisation.md` 6.3: about NT$1,000, NT$38,000 and NT$202,000 against NT$60,000 of spend at the cap). Section 2 reconciles this model with it.
2. **Money is gross and pre-tax** (before business tax, withholding and the 二代健保 supplementary premium, which are unverified and a 記帳士 question; the recalled rates were deliberately not put into the model, `research/legal.md` 7.2). Amounts are in NT$.
3. **Calendar.** M1 is the month of the first persona post, taken as 2026-11 because the indicative W0 is 2026-11-16. W0 is only a label and is flagged unlikely (`launch/README.md` D7); if it slips, every month label slips with it. M0 (2026-10) is the pre-launch month for registration and set-up. Taiwan's commercial calendar is not modelled: no brand-paid 雙11 content in 2026, the first realistic brand window is December 2026 to February 2027 (農曆新年 is 2027-02-06), and the 2027 ghost month (2027-08-02 to 08-31) is a quiet period for new launches.
4. **Recognised revenue** is booked in the month a job is delivered or a sale happens. **Cash** arrives after a lag (assumption, per route). Anything that would land after M12 is shown as a **receivable at M12**.
5. **Spend.** The base case is the NT$5,000 monthly tools budget (DECISIONS Q1), at 60% in months 1 to 3 (portfolio rule: stay below the cap early), so NT$54,000 over M1 to M12. The NT$10,000 headroom is run as a variant. **The wife's time is not a cash cost**; it is counted in hours and valued only inside the rate card (a sensitivity row pays her in cash). The image-tool tries caused by revenue work sit inside the tools budget and are not added again.
6. **One-time and recurring compliance costs** (registration, 記帳士, lawyer, trade mark filing, bookkeeping) are **placeholders**: Phase 1 found no fee for any of them. They are shown separately so the cash view is readable with and without them, and the user must confirm the amount they are willing to spend (DECISIONS STOP 2 item 6). **They are not quotes.**
7. **Expected values and discrete jobs.** Affiliate commission, own products and stickers are expected values spread across months. B2B jobs and sponsored posts are discrete events spread evenly from the first paid month.
8. **Revenue work competes with the personas for the same hours.** Revenue is priority 3 and is cut before posting (`strategy/portfolio.md` 5.6). The hours caps in the table are flagged, not enforced.
9. **Licensing (spokes-character) and platform payouts are fixed at NT$0** in every scenario: nine to eighteen months and low in year 1, and out of reach of the YouTube thresholds (`research/monetisation.md` 3.5, 3.6, S17).

---

## 1. Headline

<!-- BEGIN GENERATED:model-headline -->
- **Low:** NT$20 recognised in 12 months (NT$15 received in cash by M12), against NT$54,000 of tools spend; net cash -NT$53,985 on tools alone and -NT$112,985 with the placeholder compliance costs. Operator hours on revenue work: 11 (4% of the operator's year).
- **Middle:** NT$24,909 recognised in 12 months (NT$18,986 received in cash by M12), against NT$54,000 of tools spend; net cash -NT$35,431 on tools alone and -NT$94,431 with the placeholder compliance costs. Operator hours on revenue work: 87 (28% of the operator's year).
- **High:** NT$135,300 recognised in 12 months (NT$110,673 received in cash by M12), against NT$54,000 of tools spend; net cash NT$54,553 on tools alone and -NT$4,447 with the placeholder compliance costs. Operator hours on revenue work: 185 (59% of the operator's year).
<!-- END GENERATED:model-headline -->

What the arithmetic says, in words (a unit test checks each sentence against the numbers, so these cannot go stale if an assumption is edited):

1. **Only the high scenario recovers its tools spend inside the 12 months**, and it does so by using more than half of the operator's year on revenue work, which is possible only if posting is cut.
2. **The low scenario is the world in which the week-8 checkpoint shows no signal and the studio stops spending hours on revenue work.** Revenue is close to zero. Phase 1 called this the base case for persona-level income. Tools spend is held at the plan in every scenario; retiring the personas would also stop the spend, which the sensitivity table shows by cutting it.
3. **The middle scenario recovers less than half of the tools spend**, and its revenue per hour worked is below half of the hourly value used to build the rate card. It is not a break-even case.
4. **No scenario recovers the spend once the placeholder compliance costs are included.** The placeholders are unsourced, and their total is of the same order as the 12 months of tools spend, so getting real fees matters as much as any revenue lever (see the sensitivity table). That is a reason to get quotes, not a finding.
5. **Persona-level profit is not the right test in year 1.** B2B income belongs to the studio and the allocated tools cost is shared; section 5 shows the display allocation.

---

## 2. Reconciliation with the Phase 1 hypothesis (NT$0 to about NT$200,000)

The model's inputs are replayed at the Phase 1 values first (a unit test confirms it reproduces about NT$1,000, NT$38,000 and NT$202,000 exactly), then compared with this model.

<!-- BEGIN GENERATED:model-reconcile -->
| Scenario | Phase 1 total (replayed, NT$) | This model, recognised (NT$) | Difference (NT$) | Phase 1 vs NT$60,000 spend (NT$) | This model: net cash, tools only (NT$) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Low | 1,000 | 20 | -980 | -59,000 | -53,985 |
| Middle | 38,000 | 24,909 | -13,091 | -22,000 | -35,431 |
| High | 202,000 | 135,300 | -66,700 | 142,000 | 54,553 |

| Scenario | Route | Phase 1 cell (NT$) | This model (NT$) | Difference (NT$) |
| :--- | :--- | ---: | ---: | ---: |
| Low | B2B creative | 0 | 0 | 0 |
| Low | Sponsored posts | 0 | 0 | 0 |
| Low | Affiliate | 1,000 | 20 | -980 |
| Low | Own products | 0 | 0 | 0 |
| Low | Stickers | 0 | 0 | 0 |
| Middle | B2B creative | 24,000 | 15,440 | -8,560 |
| Middle | Sponsored posts | 5,000 | 3,600 | -1,400 |
| Middle | Affiliate | 5,000 | 1,969 | -3,031 |
| Middle | Own products | 2,000 | 3,180 | 1,180 |
| Middle | Stickers | 2,000 | 720 | -1,280 |
| High | B2B creative | 120,000 | 72,000 | -48,000 |
| High | Sponsored posts | 32,000 | 16,200 | -15,800 |
| High | Affiliate | 30,000 | 27,000 | -3,000 |
| High | Own products | 10,000 | 15,900 | 5,900 |
| High | Stickers | 10,000 | 4,200 | -5,800 |

| Phase 1 scenario | Phase 1 B2B cell | Nearest package by proposed price | Operator hours implied | Share of operator's 312 h | Wife hours implied |
| :--- | :--- | :--- | ---: | ---: | ---: |
| Middle | 3 jobs at NT$8,000 | B3-S (proposed NT$8,200) | 25 | 8% | 8 |
| High | 8 jobs at NT$15,000 | B3-M (proposed NT$15,800) | 132 | 42% | 37 |

To reach NT$200,000 recognised with the high scenario's other routes (NT$63,300) the B2B line must supply NT$136,700. At the high scenario's average realised job of NT$8,000 that is about 17.1 jobs and 154 operator hours (49% of the operator's year), against 9 jobs in the high scenario.
<!-- END GENERATED:model-reconcile -->

How to read the differences:

- **The low end reconciles.** Both put the low scenario at close to zero (Phase 1: about NT$1,000, mostly affiliate).
- **B2B is lower here than in Phase 1 because the price is derived from hours, not assumed.** Phase 1 used hypothetical prices of NT$8,000 (middle) and NT$15,000 (high) per job. Here a job is priced from the minutes it takes (rate card, section 1), then discounted by a realisation rate. The Phase 1 high cell (8 jobs at NT$15,000 each) is closest to eight B3-M jobs at the full proposed price with no discount, which would take the operator hours shown in the table above. Reaching NT$200,000 on this model's logic needs more jobs than the high scenario has, at full price, with the other routes also at their high values. That is why the high scenario stops short of it.
- **Sponsored posts are lower** because the proposed fee is production-cost only: there is no audience to charge a reach component for (the reach component is `[TO FILL WHEN REAL]` and zero here; the sensitivity table tries two hypothetical values).
- **Affiliate is lower** because it is built from a funnel (impressions, link clicks, orders, commission) with ramped reach, not a single guess.
- **Own products are a little higher** because the list price is derived from the production hours (repaid at 40 sales net of the assumed fee), not guessed.
- **Reading.** The Phase 1 range stays as the planning range. This model suggests the top of it is hours-constrained, not demand-constrained: it needs B2B volume that the couple's hours cannot carry unless posting is cut. Both ends rest on assumptions; neither is a prediction.

---

## 3. How the inputs are sourced

<!-- BEGIN GENERATED:model-status-counts -->
| Status | Rows in assumptions.csv | Meaning |
| :--- | ---: | :--- |
| sourced | 12 | taken from a project file with its own confidence label |
| computed | 1 | arithmetic on sourced values |
| assumption | 115 | the studio's own planning figure, logic stated, not market data |
| hypothetical | 3 | equals a Phase 1 hypothetical axis value, not market data |
| placeholder | 8 | no source exists; a stand-in to be replaced with a real quote [TO FILL WHEN REAL] |
| excluded | 2 | fixed at zero by rule |
| **all** | **141** |  |
<!-- END GENERATED:model-status-counts -->

- **Sourced:** the NT$5,000 monthly cap (DECISIONS Q1), the operator's 6 hours a week (DECISIONS Q2), the image-tool cost per try (`pipeline/tools.md` 5, secondary list prices, low to medium confidence, converted at NT$32 per US$ as an assumption), and the Phase 1 replay cells.
- **Hypothetical:** the affiliate average order (NT$500), the commission rates (2%, 5%, 8%) and the sticker studio share (NT$12 per sale). These are Phase 1 axis values for sensitivity (`research/monetisation.md` 6.2). They are not Taiwan data.
- **Assumption:** everything else that is not a placeholder: minutes per task, the hourly values, the margin, job and deal counts, reach, click and order rates, realisation rates, lags, first months and the hours available. The logic is in the note beside each row.
- **Placeholder (8 rows):** marketplace fee rate, sponsored-post reach component, registration, 記帳士 set-up, lawyer launch consult, lawyer contract review, trade mark filing, and monthly bookkeeping. Each is `[TO FILL WHEN REAL]`.
- **Not one input is a Taiwan market price.** The full table with source and logic for every row is in Appendix B.

---

## 4. Scenario definitions

The low scenario is **the studio that keeps posting but earns almost nothing**: the week-8 checkpoint (`strategy/portfolio.md` 6.4) shows no signal, so it spends no hours on products or stickers and does one free sample. The middle scenario is **one paid job per pilot plus one sponsored post and small passive income**. The high scenario is **repeat B2B clients and a few sponsored posts**, with the operator's hours diverted from posting. None is more likely than another; no probability is attached.

<!-- BEGIN GENERATED:model-inputs -->
| Input (from assumptions.csv) | Low | Middle | High |
| :--- | ---: | ---: | ---: |
| B2B paid jobs: small + medium | 0 + 0 | 3 + 0 | 5 + 4 |
| B2B free private samples | 1 | 3 | 5 |
| B2B brands or agencies approached | 5 | 25 | 60 |
| B2B first paid month (M#) | M8 | M6 | M4 |
| B2B share of the proposed price realised | 60% | 80% | 90% |
| Sponsored posts (業配) in total | 0 | 1 | 4 |
| Sponsored post audience tier / first month | T0 / M8 | T1 / M8 | T1 / M6 |
| Sponsored share of the proposed price realised | 60% | 80% | 90% |
| Affiliate: steady monthly impressions per persona | 3,000 | 25,000 | 150,000 |
| Affiliate: link click rate / click-to-order | 0.3% / 1.0% | 0.7% / 2.0% | 1.0% / 2.0% |
| Affiliate: average order / commission | NT$500 / 2% | NT$500 / 5% | NT$500 / 8% |
| Own products made / units sold in 12 months | 0 / 0 | 3 / 12 | 3 / 60 |
| Own products first sale month | M6 | M5 | M4 |
| LINE sticker sets / sales per set per month | 0 / 0 | 1 / 10 | 2 / 25 |
| LINE sticker first sales month / studio share per sale | M8 / NT$12 | M7 / NT$12 | M6 / NT$12 |
| Hours a month available for revenue work: operator / wife | 4 / 5 | 7.5 / 8 | 16 / 12 |
| Months from work to cash: B2B / sponsored / affiliate / products / stickers | 1 / 1 / 2 / 1 / 3 | 1 / 1 / 2 / 1 / 3 | 1 / 1 / 2 / 1 / 3 |
| Platform payouts and licensing | NT$0 (excluded) | NT$0 (excluded) | NT$0 (excluded) |
<!-- END GENERATED:model-inputs -->

Route logic:

- **B2B creative (studio level).** Paid jobs are priced from the rate card (a small or medium package for the persona that is the showroom: B1 for 色環, B2 for 方寸, B3 for 步驟), multiplied by the realisation rate. They are spread evenly between the first paid month and M12. Each job costs operator and wife hours. Free private samples come first, one a month, cycling 色環, 方寸, 步驟, and cost hours and image tries but earn nothing.
- **Sponsored posts (業配).** Priced at the production price for the audience tier (no reach component yet) times the realisation rate, spread from the first sponsored month.
- **Affiliate.** Steady-state monthly impressions per persona, ramped linearly over 8 months from the first live month, times a link click rate, a click-to-order rate, an average order and a commission. Link upkeep costs 30 operator minutes a month.
- **Own digital products.** One pack per pilot, made one a month before the first sale, sold as expected units spread over the active months at the rate-card list price, less an assumed marketplace fee.
- **LINE stickers.** Sets made one a month before the first sale; sales per set per month at the studio share per sale. Photoreal-face sets are untested.

---

## 5. Results by route and by persona

<!-- BEGIN GENERATED:model-summary -->
| Scenario | B2B | Sponsored | Affiliate | Products | Stickers | Licensing | Platform payouts | Total recognised |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Low | 0 | 0 | 20 | 0 | 0 | 0 | 0 | **20** |
| Middle | 15,440 | 3,600 | 1,969 | 3,180 | 720 | 0 | 0 | **24,909** |
| High | 72,000 | 16,200 | 27,000 | 15,900 | 4,200 | 0 | 0 | **135,300** |

All amounts in NT$, gross and pre-tax. Net cash = cash received minus fees minus spend.

| Scenario | Cash received by M12 | Receivable at M12 (not yet paid) | Marketplace fees | Tools spend M0 to M12 | Placeholder compliance costs | Net cash, tools only | Net cash incl. placeholders |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Low | 15 | 5 | 0 | 54,000 | 59,000 | -53,985 | -112,985 |
| Middle | 18,986 | 5,922 | 417 | 54,000 | 59,000 | -35,431 | -94,431 |
| High | 110,673 | 24,627 | 2,120 | 54,000 | 59,000 | 54,553 | -4,447 |
<!-- END GENERATED:model-summary -->

**By persona.** B2B revenue is studio level, tagged to the persona that is the showroom for tracking only (`strategy/portfolio.md` 6.1). Tools spend is shared and never allocated to one persona in the plan; the table shows an equal third as a **display-only allocation (assumption)** so the brief's success criterion 3 (revenue per persona above its running cost) can be looked at. The wife's and operator's hours are shown beside it.

<!-- BEGIN GENERATED:model-persona -->
**Low scenario**

| Persona | B2B (tagged) | Sponsored | Affiliate | Products | Stickers | Total recognised | Allocated tools (1/3, display only) | Revenue minus allocated tools | Operator h | Wife h |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 方寸 (home organisation) | 0 | 0 | 7 | 0 | 0 | 7 | 18,000 | -17,993 | 2 | 0 |
| 步驟 (AI tools) | 0 | 0 | 7 | 0 | 0 | 7 | 18,000 | -17,993 | 2 | 0 |
| 色環 (outfit logic and colour) | 0 | 0 | 7 | 0 | 0 | 7 | 18,000 | -17,993 | 7 | 2 |

**Middle scenario**

| Persona | B2B (tagged) | Sponsored | Affiliate | Products | Stickers | Total recognised | Allocated tools (1/3, display only) | Revenue minus allocated tools | Operator h | Wife h |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 方寸 (home organisation) | 4,240 | 0 | 656 | 1,200 | 0 | 6,096 | 18,000 | -11,904 | 20 | 7 |
| 步驟 (AI tools) | 6,560 | 0 | 656 | 480 | 0 | 7,696 | 18,000 | -10,304 | 27 | 8 |
| 色環 (outfit logic and colour) | 4,640 | 3,600 | 656 | 1,500 | 720 | 11,116 | 18,000 | -6,884 | 40 | 12 |

**High scenario**

| Persona | B2B (tagged) | Sponsored | Affiliate | Products | Stickers | Total recognised | Allocated tools (1/3, display only) | Revenue minus allocated tools | Operator h | Wife h |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 方寸 (home organisation) | 18,180 | 4,050 | 9,000 | 6,000 | 2,100 | 39,330 | 18,000 | 21,330 | 58 | 18 |
| 步驟 (AI tools) | 28,980 | 4,050 | 9,000 | 2,400 | 0 | 44,430 | 18,000 | 26,430 | 56 | 17 |
| 色環 (outfit logic and colour) | 24,840 | 8,100 | 9,000 | 7,500 | 2,100 | 51,540 | 18,000 | 33,540 | 72 | 22 |
<!-- END GENERATED:model-persona -->

**Affiliate funnel, products and stickers (12 months, expected values).**

<!-- BEGIN GENERATED:model-funnel -->
| Scenario | Impressions (12 m) | Link clicks | Orders | GMV (NT$) | Commission (NT$) | Product units | Sticker sales |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Low | 67,500 | 202 | 2 | 1,012 | 20 | 0 | 0 |
| Middle | 562,500 | 3,938 | 79 | 39,375 | 1,969 | 12 | 60 |
| High | 3,375,000 | 33,750 | 675 | 337,500 | 27,000 | 60 | 350 |
<!-- END GENERATED:model-funnel -->

**B2B funnel implied by the scenario inputs.** There is no Taiwan benchmark for these ratios. Read a ratio of one paid job per free sample or more as an optimistic reading in its own right.

<!-- BEGIN GENERATED:model-b2b-funnel -->
| Scenario | Brands or agencies approached | Free samples | Paid jobs | Paid jobs per contact approached | Paid jobs per free sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Low | 5 | 1 | 0 | 0% | 0.00 |
| Middle | 25 | 3 | 3 | 12% | 1.00 |
| High | 60 | 5 | 9 | 15% | 1.80 |
<!-- END GENERATED:model-b2b-funnel -->

---

## 6. Hours

Revenue work uses the same hours as the personas. The caps below are the assumption for what can be found (low: the admin and brand-contact line in the plan; middle: that plus about half the rework reserve; high: the whole reserve plus posting cuts). **Worst backlog** is the most hours of revenue work that exceed the monthly cap at any point and have to be carried forward, which means a later delivery or hours taken from the personas. **Revenue per hour worked** divides recognised revenue by operator plus wife hours; compare it with the assumed blended hourly value beside it.

<!-- BEGIN GENERATED:model-hours -->
| Scenario | Operator h, 12 months | Avg h/month | Cap h/month | Peak month h | Months over cap | Worst backlog h | Share of operator year | Wife h, 12 months | Wife avg h/month | Wife cap h/month | Average within both caps | Assumed blended value (NT$/h) | Revenue per hour worked (NT$/h) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | :--- | ---: | ---: |
| Low | 11 | 0.9 | 4 | 6.2 | 1 | 2.2 | 4% | 2 | 0.2 | 5 | yes | 585 | 2 |
| Middle | 87 | 7.2 | 8 | 18.8 | 5 | 27.6 | 28% | 28 | 2.3 | 8 | yes | 576 | 218 |
| High | 185 | 15.4 | 16 | 26.1 | 4 | 20.3 | 59% | 58 | 4.8 | 12 | yes | 576 | 556 |
<!-- END GENERATED:model-hours -->

The operator is already the binding constraint: `ops/risk-register.md` PPL-1 finds the planned load over the 360 minutes available at 18 approvals a week and only 45 minutes of slack at the adopted 12. Any scenario above the low one therefore spends hours the plan does not have, and the plan's own priority order (accounts first, engagement second, revenue third) says posting wins.

---

## 7. Month-by-month cash view

Columns are cash received by route (after the lag), then marketplace fees, tools spend and placeholder compliance costs (shown as positive amounts of spend), then the net and the running total with and without the placeholders (receipts minus spend, so a negative number means cash out).

**Middle scenario, every month.**

<!-- BEGIN GENERATED:model-cash-mid -->
| Month | B2B | Sponsored | Affiliate | Products | Stickers | Fees | Tools | Placeholder costs | Net (tools only) | Cumulative (tools only) | Net incl. placeholders | Cumulative incl. placeholders |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| M0 2026-10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 23,000 | 0 | 0 | -23,000 | -23,000 |
| M1 2026-11 | 0 | 0 | 0 | 0 | 0 | 0 | 3,000 | 1,500 | -3,000 | -3,000 | -4,500 | -27,500 |
| M2 2026-12 | 0 | 0 | 0 | 0 | 0 | 0 | 3,000 | 1,500 | -3,000 | -6,000 | -4,500 | -32,000 |
| M3 2027-01 | 0 | 0 | 0 | 0 | 0 | 0 | 3,000 | 19,500 | -3,000 | -9,000 | -22,500 | -54,500 |
| M4 2027-02 | 0 | 0 | 33 | 0 | 0 | 0 | 5,000 | 1,500 | -4,967 | -13,967 | -6,467 | -60,967 |
| M5 2027-03 | 0 | 0 | 66 | 0 | 0 | 0 | 5,000 | 1,500 | -4,934 | -18,902 | -6,434 | -67,402 |
| M6 2027-04 | 0 | 0 | 98 | 398 | 0 | 60 | 5,000 | 1,500 | -4,564 | -23,465 | -6,064 | -73,465 |
| M7 2027-05 | 4,240 | 0 | 131 | 398 | 0 | 60 | 5,000 | 1,500 | -291 | -23,756 | -1,791 | -75,256 |
| M8 2027-06 | 0 | 0 | 164 | 398 | 0 | 60 | 5,000 | 1,500 | -4,498 | -28,254 | -5,998 | -81,254 |
| M9 2027-07 | 0 | 3,600 | 197 | 398 | 0 | 60 | 5,000 | 1,500 | -865 | -29,119 | -2,365 | -83,619 |
| M10 2027-08 | 6,560 | 0 | 230 | 398 | 120 | 60 | 5,000 | 1,500 | 2,248 | -26,872 | 748 | -82,872 |
| M11 2027-09 | 0 | 0 | 262 | 398 | 120 | 60 | 5,000 | 1,500 | -4,280 | -31,152 | -5,780 | -88,652 |
| M12 2027-10 | 0 | 0 | 262 | 398 | 120 | 60 | 5,000 | 1,500 | -4,280 | -35,431 | -5,780 | -94,431 |
| **Total** | **10,800** | **3,600** | **1,444** | **2,782** | **360** | **417** | **54,000** | **59,000** | **-35,431** | **-35,431** | **-94,431** | **-94,431** |
<!-- END GENERATED:model-cash-mid -->

**Low scenario, compact.**

<!-- BEGIN GENERATED:model-cash-low -->
| Month | Cash received | Tools | Placeholder costs | Cumulative (tools only) | Cumulative incl. placeholders |
| :--- | ---: | ---: | ---: | ---: | ---: |
| M0 2026-10 | 0 | 0 | 23,000 | 0 | -23,000 |
| M1 2026-11 | 0 | 3,000 | 1,500 | -3,000 | -27,500 |
| M2 2026-12 | 0 | 3,000 | 1,500 | -6,000 | -32,000 |
| M3 2027-01 | 0 | 3,000 | 19,500 | -9,000 | -54,500 |
| M4 2027-02 | 0 | 5,000 | 1,500 | -14,000 | -61,000 |
| M5 2027-03 | 1 | 5,000 | 1,500 | -18,999 | -67,499 |
| M6 2027-04 | 1 | 5,000 | 1,500 | -23,998 | -73,998 |
| M7 2027-05 | 1 | 5,000 | 1,500 | -28,997 | -80,497 |
| M8 2027-06 | 2 | 5,000 | 1,500 | -33,995 | -86,995 |
| M9 2027-07 | 2 | 5,000 | 1,500 | -38,993 | -93,493 |
| M10 2027-08 | 2 | 5,000 | 1,500 | -43,991 | -99,991 |
| M11 2027-09 | 3 | 5,000 | 1,500 | -48,988 | -106,488 |
| M12 2027-10 | 3 | 5,000 | 1,500 | -53,985 | -112,985 |
<!-- END GENERATED:model-cash-low -->

**High scenario, compact.**

<!-- BEGIN GENERATED:model-cash-high -->
| Month | Cash received | Tools | Placeholder costs | Cumulative (tools only) | Cumulative incl. placeholders |
| :--- | ---: | ---: | ---: | ---: | ---: |
| M0 2026-10 | 0 | 0 | 23,000 | 0 | -23,000 |
| M1 2026-11 | 0 | 3,000 | 1,500 | -3,000 | -27,500 |
| M2 2026-12 | 0 | 3,000 | 1,500 | -6,000 | -32,000 |
| M3 2027-01 | 0 | 3,000 | 19,500 | -9,000 | -54,500 |
| M4 2027-02 | 450 | 5,000 | 1,500 | -13,550 | -60,550 |
| M5 2027-03 | 7,437 | 5,000 | 1,500 | -11,378 | -59,878 |
| M6 2027-04 | 7,887 | 5,000 | 1,500 | -8,757 | -58,757 |
| M7 2027-05 | 14,997 | 5,000 | 1,500 | 975 | -50,525 |
| M8 2027-06 | 11,397 | 5,000 | 1,500 | 7,107 | -45,893 |
| M9 2027-07 | 14,337 | 5,000 | 1,500 | 16,178 | -38,322 |
| M10 2027-08 | 14,157 | 5,000 | 1,500 | 25,070 | -30,930 |
| M11 2027-09 | 24,237 | 5,000 | 1,500 | 44,042 | -13,458 |
| M12 2027-10 | 15,777 | 5,000 | 1,500 | 54,553 | -4,447 |
<!-- END GENERATED:model-cash-high -->

**Against the NT$5,000 and NT$10,000 tools budget** (the NT$10,000 line uses 60% of NT$10,000 in months 1 to 3; the portfolio rule is to use the headroom only if a tool clearly earns it):

<!-- BEGIN GENERATED:model-variants -->
| Scenario | Tools budget | Tools spend M0 to M12 (NT$) | Cash received net of fees (NT$) | Share of tools spend covered | Net cash, tools only | Net cash incl. placeholders |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| Low | NT$5,000 cap (base) | 54,000 | 15 | 0% | -53,985 | -112,985 |
| Low | NT$10,000 headroom | 108,000 | 15 | 0% | -107,985 | -166,985 |
| Middle | NT$5,000 cap (base) | 54,000 | 18,569 | 34% | -35,431 | -94,431 |
| Middle | NT$10,000 headroom | 108,000 | 18,569 | 17% | -89,431 | -148,431 |
| High | NT$5,000 cap (base) | 54,000 | 108,553 | 201% | 54,553 | -4,447 |
| High | NT$10,000 headroom | 108,000 | 108,553 | 101% | 553 | -58,447 |
<!-- END GENERATED:model-variants -->

---

## 8. Break-even logic

**Definitions.**

- **Lumpy cover:** the first single month whose cash received, net of fees, is at least that month's tools spend. One invoice can do this; it is not break-even.
- **Sustained cover:** the first month in which the last three months of receipts cover the last three months of tools spend (and, in the right-hand variant, the bookkeeping placeholder).
- **Cumulative break-even:** the first month in which cumulative cash since M0 reaches zero.

<!-- BEGIN GENERATED:model-breakeven -->
| Scenario | First single month in which receipts cover that month's tools spend (lumpy) | First month the trailing 3 months of receipts cover the trailing 3 months of tools spend (sustained) | ... and also the bookkeeping placeholder | Cumulative cash reaches zero (tools only) | Cumulative cash reaches zero (incl. placeholders) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Low | never within 12 months | never within 12 months | never within 12 months | never within 12 months | never within 12 months |
| Middle | M10 (2027-08) | never within 12 months | never within 12 months | never within 12 months | never within 12 months |
| High | M5 (2027-03) | M6 (2027-04) | M7 (2027-05) | M7 (2027-05) | never within 12 months |

| Monthly tools budget (NT$) | Route alone (middle-scenario inputs) | Needed | Unit | Operator h a month | Share of the operator's 26 h |
| ---: | :--- | ---: | :--- | ---: | ---: |
| 5,000 | B2B B1-S | 1.08 | jobs a month | 6.1 | 23% |
| 5,000 | B2B B2-S | 1.18 | jobs a month | 6.2 | 24% |
| 5,000 | B2B B3-S | 0.76 | jobs a month | 6.4 | 24% |
| 5,000 | B2B B1-M | 0.57 | jobs a month | 6.2 | 24% |
| 5,000 | B2B B3-M | 0.40 | jobs a month | 6.5 | 25% |
| 5,000 | Sponsored post (tier 1) | 1.39 | posts a month | 6.4 | 25% |
| 5,000 | Affiliate (this scenario's funnel) | 1,428,571 | impressions a month |  |  |
| 5,000 | Affiliate (Phase 1 axis: 1%, 2%, NT$500, 5%) | 1,000,000 | impressions a month |  |  |
| 5,000 | Product P1 at NT$240 list | 25 | sales a month |  |  |
| 5,000 | Product P3 at NT$300 list | 20 | sales a month |  |  |
| 5,000 | LINE stickers at NT$12 per sale | 417 | sales a month |  |  |
| 10,000 | B2B B1-S | 2.16 | jobs a month | 12.2 | 47% |
| 10,000 | B2B B2-S | 2.36 | jobs a month | 12.5 | 48% |
| 10,000 | B2B B3-S | 1.52 | jobs a month | 12.7 | 49% |
| 10,000 | B2B B1-M | 1.15 | jobs a month | 12.5 | 48% |
| 10,000 | B2B B3-M | 0.79 | jobs a month | 13.1 | 50% |
| 10,000 | Sponsored post (tier 1) | 2.78 | posts a month | 12.8 | 49% |
| 10,000 | Affiliate (this scenario's funnel) | 2,857,143 | impressions a month |  |  |
| 10,000 | Affiliate (Phase 1 axis: 1%, 2%, NT$500, 5%) | 2,000,000 | impressions a month |  |  |
| 10,000 | Product P1 at NT$240 list | 49 | sales a month |  |  |
| 10,000 | Product P3 at NT$300 list | 39 | sales a month |  |  |
| 10,000 | LINE stickers at NT$12 per sale | 833 | sales a month |  |  |
<!-- END GENERATED:model-breakeven -->

**Formulas behind the second table** (each route alone, at the middle-scenario inputs):

- B2B: jobs a month = monthly tools budget divided by (proposed price x realisation rate); operator hours a month = jobs x operator hours per job.
- Sponsored posts: posts a month = budget divided by (production price at the tier + reach component) x realisation.
- Affiliate: GMV needed = budget divided by commission; impressions needed = GMV divided by (link click rate x click-to-order x average order). The Phase 1 row uses its own hypothetical axis values and reproduces its "about a million monthly impressions" check.
- Products: sales a month = budget divided by the list price net of the assumed fee.
- Stickers: sales a month = budget divided by the studio share per sale.

**What it means.** At the cap, break-even through B2B alone would take roughly one small job every month, which is a large share of the operator's 26 monthly hours (last column); at NT$10,000 it would take about half of them. Affiliate alone would need on the order of a million impressions a month, stickers hundreds of sales a month, and products tens of sales a month. These are the numbers that make the recommendation to **stay below the cap in months 1 to 3 and add paid tools only when a revenue line justifies them** (`strategy/portfolio.md` 7).

---

## 9. Sensitivity

One change at a time from the middle scenario. "Net cash, tools only" is revenue received less fees and tools spend; the last column adds the placeholder compliance costs.

<!-- BEGIN GENERATED:model-sens -->
| Case (one change at a time from the middle scenario) | Recognised revenue (NT$) | Change | Net cash, tools only (NT$) | Change | Net cash incl. placeholders (NT$) |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Base: middle scenario | 24,909 | - | -35,431 | - | -94,431 |
| B2B realisation 0.6 (deeper discounts) | 21,049 | -3,860 | -38,131 | -2,700 | -97,131 |
| B2B realisation 1.0 (full proposed price) | 28,769 | +3,860 | -32,731 | +2,700 | -91,731 |
| B2B paid jobs: none (x0) | 9,469 | -15,440 | -46,231 | -10,800 | -105,231 |
| B2B paid jobs: double (x2) | 40,349 | +15,440 | -19,991 | +15,440 | -78,991 |
| B2B paid jobs: triple (x3) | 55,789 | +30,880 | -4,551 | +30,880 | -63,551 |
| B2B jobs delivered earlier (M4 to M10) | 24,909 | 0 | -30,791 | +4,640 | -89,791 |
| B2B jobs all delivered in M12 (cash lands after the 12 months) | 24,909 | 0 | -46,231 | -10,800 | -105,231 |
| Every payment lag +2 months | 24,909 | 0 | -36,872 | -1,441 | -95,872 |
| Operator hourly value NT$400 (prices fall) | 19,419 | -5,490 | -39,604 | -4,173 | -98,604 |
| Operator hourly value NT$800 (prices rise) | 30,529 | +5,620 | -31,141 | +4,290 | -90,141 |
| Margin 10% | 22,309 | -2,600 | -37,379 | -1,948 | -96,379 |
| Margin 40% | 27,639 | +2,730 | -33,366 | +2,065 | -92,366 |
| Sponsored posts: none | 21,309 | -3,600 | -39,031 | -3,600 | -98,031 |
| Sponsored posts: 3 on 色環 | 32,109 | +7,200 | -31,831 | +3,600 | -90,831 |
| Reach component NT$2,000 per sponsored post (hypothetical axis) | 26,509 | +1,600 | -33,831 | +1,600 | -92,831 |
| Reach component NT$5,000 per sponsored post (hypothetical axis) | 28,909 | +4,000 | -31,431 | +4,000 | -90,431 |
| Impressions x0.5 | 23,924 | -984 | -36,153 | -722 | -95,153 |
| Impressions x2 | 26,878 | +1,969 | -33,987 | +1,444 | -92,987 |
| Impressions x5 | 32,784 | +7,875 | -29,656 | +5,775 | -88,656 |
| Affiliate commission 2% (Phase 1 axis) | 23,728 | -1,181 | -36,297 | -866 | -95,297 |
| Affiliate commission 8% (Phase 1 axis) | 26,090 | +1,181 | -34,565 | +866 | -93,565 |
| Link click rate halved | 23,924 | -984 | -36,153 | -722 | -95,153 |
| Own product units x0 (nothing sells) | 21,729 | -3,180 | -37,796 | -2,365 | -96,796 |
| Own product units x3 | 31,269 | +6,360 | -30,701 | +4,730 | -89,701 |
| Own product list prices 40% lower (payback units 67 instead of 40) | 23,679 | -1,230 | -36,346 | -915 | -95,346 |
| No LINE stickers | 24,189 | -720 | -35,791 | -360 | -94,791 |
| Sticker creator share NT$8 (Phase 1 axis) | 24,669 | -240 | -35,551 | -120 | -94,551 |
| Sticker creator share NT$16 (Phase 1 axis) | 25,149 | +240 | -35,311 | +120 | -94,311 |
| Tools budget NT$10,000 (headroom used) | 24,909 | 0 | -89,431 | -54,000 | -148,431 |
| Tools held at 60% of the cap (NT$3,000) all year | 24,909 | 0 | -17,431 | +18,000 | -76,431 |
| Wife's review hours paid in cash at the assumed hourly value | 24,909 | 0 | -49,273 | -13,842 | -108,273 |
| Compliance placeholders x0 (all free) | 24,909 | 0 | -35,431 | 0 | -35,431 |
| Compliance placeholders x2 | 24,909 | 0 | -35,431 | 0 | -153,431 |
<!-- END GENERATED:model-sens -->

Reading the table: the levers that move the 12-month result are the **number of paid B2B jobs** and the **tools spend**; delivery timing matters because work delivered late lands outside the year; the compliance placeholders matter as much as any revenue lever. Affiliate reach, commission rates and stickers move the result by little in year 1 even when multiplied; own products help a little. Paying the wife in cash would make every scenario worse. Reach components for sponsored posts help, but they depend on an audience that does not yet exist and on 3+ real quotes.

---

## 10. What would change this model

| Gap (`research/monetisation.md` 4) | Inputs it replaces |
|---|---|
| G1, G2 agency rate sheets, tier definitions, per-video and CPM | `sp.reach_premium`, tier boundaries, `rate.op_hourly`, `b2b.realisation`, `sp.realisation` |
| G11 public prices of Taiwan AI-creative studios | `rate.op_hourly`, `rate.margin`, `offer.*` minutes, `b2b.realisation` |
| G3, G4 affiliate programme terms | `aff.commission`, `aff.lag`, whether an unregistered individual or a virtual account may join |
| G5 LINE Creators Market | `stk.creator_share`, `stk.lag`, whether an AI photoreal set is accepted |
| G7 to G9 platform payout availability | `excl.platform_payouts` (kept at zero until a Taiwan account shows an eligible programme) |
| G10 spokes-character fees | nothing is modelled; a range appears only after 3+ comparables exist |
| G12 tax and registration by route | which routes can be received before registration; the placeholders; whether business tax enters the model |
| G13 AI-art copyright | usage-rights wording and any licence premium |
| Fees for registration, 記帳士, lawyer and trade mark | the `cost.*` placeholders |
| Marketplace fee rates | `prod.fee_rate` |
| Measured minutes from the first sample | `offer.*` minutes |
| Real reach per post after week 6 | `aff.impressions.*`, `sp.tier` |

**Checkpoints already in the plan** (`strategy/portfolio.md` 6.4): by week 8, at least 5 warm fashion contacts approached, at least 1 free scoped sample delivered, at least 3 written rate quotes gathered, affiliate and LINE Creators Market terms screenshotted. Within 6 months of the first post, at least one written B2B quote or accepted sample; otherwise treat B2B as unproven and hold spend at NT$5,000 a month or below. Do not judge persona-level profit before month 6.

---

## 11. Limits of this model

- No Taiwan market price, rate, commission, payout or engagement benchmark underlies it. It is a structure with assumptions in it.
- Pre-tax, and before the effect of registration form, withholding and the 二代健保 premium (all unverified).
- No seasonality or event calendar, and no repeat-client dynamics beyond the job counts.
- Expected values for affiliate, products and stickers; no variance, no best or worst month.
- Routes are independent: no cannibalisation between B2B work and posting (it is handled only by the hours flag), and no effect of a B2B sample on a persona's reach.
- Hours caps are flagged and not enforced; a scenario that needs more hours than the cap is shown as such, not shrunk.
- Tool prices are secondary list prices and the tool licence terms are unread (HUMAN_TODO 33); if the terms bar commercial use, every B2B line goes to zero.
- Likelihood is not modelled. The three scenarios are not low, expected and high in a statistical sense.
- Exchange rate: NT$32 per US$ for tool prices (assumption).

---

## 12. No outcome is promised

Nothing in this file is a prediction that any revenue will arrive. The honest finding is the width of the range: from about nothing, to some tens of thousands, to at the very most (on these assumptions, with more than half of the operator's year spent) a figure that only roughly covers the tools spend plus the placeholder compliance costs. The model's use is to size spend and effort before they are committed: keep to the NT$5,000 cap, stay below it in the first three months, treat B2B creative as the only route that can matter in year 1, do not budget platform payouts, licensing or sticker income, and let the week-8 and month-6 checkpoints decide whether to continue.

---

## 13. Rerun and tests

```
cd monetisation
python3 model.py                 # summary
python3 model.py rates           # proposed prices and their derivation
python3 model.py cash high       # month by month
python3 model.py sens            # sensitivity
python3 model.py docs --check    # are the generated tables current?
python3 model.py docs --write    # refresh them after editing assumptions.csv
python3 model.py csv             # refresh monthly-cash.csv
python3 -m unittest -v test_model
```

`monthly-cash.csv` holds the month-by-month figures for all three scenarios for a spreadsheet.

---

## 14. Open items

1. Replace the eight placeholders with real figures (fees for registration, 記帳士, lawyer, trade mark; marketplace fees), and tell the model the amount the user will spend on one-time costs (DECISIONS STOP 2 item 6).
2. Collect the 3+ real quotes (rate-card section 5) and re-run.
3. Read the LINE Creators Market and affiliate programme terms (G3 to G5) and the YouTube Studio, Instagram and TikTok monetisation screens (G7 to G9) so the NT$0 exclusions rest on a Taiwan account, not on a recalled rule.
4. Confirm how many hours the couple can really give to revenue work; the plan has almost none to spare (PPL-1).
5. Settle with the 記帳士 which income can be received before registration and how each route is taxed (legal.md Q15 to Q17).
6. Confirm the image tools' commercial-use terms (HUMAN_TODO 33): without them the B2B lines are zero.

---

## Appendix A. Delivery schedules behind the middle and high scenarios

**Middle**

<!-- BEGIN GENERATED:model-schedule-mid -->
| Month | Persona (showroom) | Route | Package | Proposed price (NT$) | Realised (NT$) | Operator h | Wife h |
| :--- | :--- | :--- | :--- | ---: | ---: | ---: | ---: |
| M2 (2026-12) | 色環 (outfit logic and colour) | Free sample | B1-S sample (free, private) | 0 | 0 | 5.7 | 1.9 |
| M3 (2027-01) | 方寸 (home organisation) | Free sample | B2-S sample (free, private) | 0 | 0 | 5.3 | 1.9 |
| M4 (2027-02) | 步驟 (AI tools) | Free sample | B3-S sample (free, private) | 0 | 0 | 8.3 | 2.6 |
| M6 (2027-04) | 方寸 (home organisation) | B2B | B2-S | 5,300 | 4,240 | 5.3 | 1.9 |
| M8 (2027-06) | 色環 (outfit logic and colour) | Sponsored | SP tier 1 | 4,500 | 3,600 | 4.6 | 1.6 |
| M9 (2027-07) | 步驟 (AI tools) | B2B | B3-S | 8,200 | 6,560 | 8.3 | 2.6 |
| M12 (2027-10) | 色環 (outfit logic and colour) | B2B | B1-S | 5,800 | 4,640 | 5.7 | 1.9 |
<!-- END GENERATED:model-schedule-mid -->

**High**

<!-- BEGIN GENERATED:model-schedule-high -->
| Month | Persona (showroom) | Route | Package | Proposed price (NT$) | Realised (NT$) | Operator h | Wife h |
| :--- | :--- | :--- | :--- | ---: | ---: | ---: | ---: |
| M2 (2026-12) | 色環 (outfit logic and colour) | Free sample | B1-S sample (free, private) | 0 | 0 | 5.7 | 1.9 |
| M3 (2027-01) | 方寸 (home organisation) | Free sample | B2-S sample (free, private) | 0 | 0 | 5.3 | 1.9 |
| M4 (2027-02) | 方寸 (home organisation) | B2B | B2-S | 5,300 | 4,770 | 5.3 | 1.9 |
| M4 (2027-02) | 步驟 (AI tools) | Free sample | B3-S sample (free, private) | 0 | 0 | 8.3 | 2.6 |
| M5 (2027-03) | 色環 (outfit logic and colour) | Free sample | B1-S sample (free, private) | 0 | 0 | 5.7 | 1.9 |
| M5 (2027-03) | 方寸 (home organisation) | B2B | B2-S | 5,300 | 4,770 | 5.3 | 1.9 |
| M6 (2027-04) | 方寸 (home organisation) | Free sample | B2-S sample (free, private) | 0 | 0 | 5.3 | 1.9 |
| M6 (2027-04) | 步驟 (AI tools) | B2B | B3-S | 8,200 | 7,380 | 8.3 | 2.6 |
| M6 (2027-04) | 方寸 (home organisation) | Sponsored | SP tier 1 | 4,500 | 4,050 | 4.6 | 1.6 |
| M7 (2027-05) | 步驟 (AI tools) | B2B | B3-S | 8,200 | 7,380 | 8.3 | 2.6 |
| M8 (2027-06) | 色環 (outfit logic and colour) | B2B | B1-S | 5,800 | 5,220 | 5.7 | 1.9 |
| M8 (2027-06) | 步驟 (AI tools) | Sponsored | SP tier 1 | 4,500 | 4,050 | 4.6 | 1.6 |
| M9 (2027-07) | 方寸 (home organisation) | B2B | B2-M | 9,600 | 8,640 | 10.0 | 3.1 |
| M10 (2027-08) | 步驟 (AI tools) | B2B | B3-M | 15,800 | 14,220 | 16.5 | 4.6 |
| M10 (2027-08) | 色環 (outfit logic and colour) | Sponsored | SP tier 1 | 4,500 | 4,050 | 4.6 | 1.6 |
| M11 (2027-09) | 色環 (outfit logic and colour) | B2B | B1-M | 10,900 | 9,810 | 10.9 | 3.1 |
| M12 (2027-10) | 色環 (outfit logic and colour) | B2B | B1-M | 10,900 | 9,810 | 10.9 | 3.1 |
| M12 (2027-10) | 色環 (outfit logic and colour) | Sponsored | SP tier 1 | 4,500 | 4,050 | 4.6 | 1.6 |
<!-- END GENERATED:model-schedule-high -->

## Appendix B. Every assumption, with status and source

<!-- BEGIN GENERATED:model-assumptions -->
**A. Horizon and capacity**

| Key | Unit | Low | Mid | High | Status | Source or logic |
| :--- | :--- | ---: | ---: | ---: | :--- | :--- |
| `model.months` | count | 12 | 12 | 12 | assumption | task statement (12-month scenarios). Horizon. M0 is the pre-launch month (registration and set-up costs). M1 to M12 are the model months. |
| `model.start_year` | year | 2026 | 2026 | 2026 | assumption | strategy/portfolio.md 2A (indicative W0 = 2026-11-16). M1 is the month of the first persona post. W0 is only a label and is flagged unlikely (launch/README.md D7). If it slips, every month label shifts by the same amount. |
| `model.start_month` | month | 11 | 11 | 11 | assumption | strategy/portfolio.md 2A. Month number of M1 (11 = November 2026). Then M0 = 2026-10 and M12 = 2027-10. |
| `cap.op_hours_month_total` | hours | 26 | 26 | 26 | computed | DECISIONS.md Q2: 6 h per week x 52 / 12. The operator's total hours per month. |
| `cap.op_hours_revenue_month` | hours | 4 | 7.5 | 16 | assumption | strategy/portfolio.md 5.3: the admin and brand-contact line is 60 min/week (about 4.3 h/month) and the rework reserve is 60 to 110 min/week (about 4.3 to 7.9 h/month); ops/risk-register.md PPL-1; portfolio 5.6. Hours per month the operator can give to revenue work (B2B, samples, sponsored posts, products, stickers, link upkeep). Low = the admin line only. Mid = the admin line plus about half the rework reserve (7.5 h is 29% of operator time). High = the admin line plus the whole reserve plus posting cuts (16 h is 62%), possible only if posting is cut (portfolio 5.6). Planned load leaves little slack (PPL-1), so mid and high take hours from the personas. |
| `cap.wife_hours_revenue_month` | hours | 5 | 8 | 12 | assumption | strategy/portfolio.md 5.3: headroom to the 510-minute gate is 108 min/week, about 7.8 h/month. The wife's hours per month available to review revenue work. Her time is not a cash cost. |

**B. Rate-card formula**

| Key | Unit | Low | Mid | High | Status | Source or logic |
| :--- | :--- | ---: | ---: | ---: | :--- | :--- |
| `rate.op_hourly` | NT$/h | 600 | 600 | 600 | assumption | research/SUMMARY.md iv: Phase 1 hypothetical reviewer axis NT$300 / 500 / 800 per hour. Assumed hourly value of the operator's production, QA and client time. No wage or freelancer rate was found. Replace after 3+ real quotes (G1, G11). |
| `rate.wife_hourly` | NT$/h | 500 | 500 | 500 | assumption | research/SUMMARY.md iv: same hypothetical axis, middle value. Assumed hourly value of the wife's native zh-TW review time. Not paid in cash. |
| `rate.margin` | fraction | 0.25 | 0.25 | 0.25 | assumption | stated logic. Added to cost: covers rework beyond the included rounds, unpaid scoping and sales time, tool price changes and a contribution to the shared tools budget. Not a profit claim. |
| `rate.round_to` | NT$ | 100 | 100 | 100 | assumption | stated logic. Asks are rounded UP to this step. |
| `rate.cost_per_try` | NT$ | 8.6 | 8.6 | 8.6 | sourced | pipeline/tools.md section 5 (Gemini Pro-class with two paid reference inputs, about US$0.268 at NT$32 per US$); SOURCES.md PT3 (low to medium). Image-API cost of one generation try. Secondary list prices, not checked against an invoice. The commercial-use terms are unread (HUMAN_TODO 33), so no client work may start. |
| `rate.revision_fraction` | fraction | 0.2 | 0.2 | 0.2 | assumption | stated logic. Share of a set redone in each revision round. |
| `rate.rounds_included` | count | 2 | 2 | 2 | assumption | content/sehuan/b2b-pitch.md B5 (two rounds of changes). Revision rounds included in every price. |
| `rate.turnaround_hours_per_week` | hours | 1.5 | 1.5 | 1.5 | assumption | cap.op_hours_revenue_month: 4 to 7.5 h a month is about 0.9 to 1.7 h a week; 1.5 chosen. Operator hours per week that a client job can get. Sets the quoted turnaround. |
| `rate.turnaround_buffer_weeks` | weeks | 1 | 1 | 1 | assumption | stated logic. Added for the client's approval windows. |
| `rate.round_fixed_op_min` | minutes | 20 | 20 | 20 | assumption | stated logic. Operator minutes of handling (messages, re-export, re-check) added to every EXTRA revision round. |
| `rate.round_fixed_wife_min` | minutes | 10 | 10 | 10 | assumption | stated logic. Wife minutes of handling added to every EXTRA revision round. |
| `rate.paid_media_op_min` | minutes | 120 | 120 | 120 | assumption | strategy/portfolio.md 1.4; research/legal.md Q8. Operator minutes to set up the platform AI-disclosure control, the paid-partnership tag and the written boost terms when a client wants to boost a post. Compliance handling, not a rights fee. |
| `rate.paid_media_wife_min` | minutes | 30 | 30 | 30 | assumption | stated logic. Wife minutes to read the boosted creative and labels. |

**C. Offer parameters**

| Key | Unit | Low | Mid | High | Status | Source or logic |
| :--- | :--- | ---: | ---: | ---: | :--- | :--- |
| `offer.B1.fixed_op_min` | minutes | 150 | 150 | 150 | assumption | stated logic: scoping 45 + brief and source slip 45 + client messages 30 + delivery and invoice 30. Operator minutes that do not depend on set size. |
| `offer.B1.fixed_wife_min` | minutes | 75 | 75 | 75 | assumption | stated logic: client correspondence 45 + final label read 30. Wife minutes that do not depend on set size. |
| `offer.B1.unit_op_min` | minutes | 45 | 45 | 45 | assumption | stated logic: about 6 tries, 200% garment-fidelity check, typeset label, provenance row. Operator minutes per still. |
| `offer.B1.unit_wife_min` | minutes | 10 | 10 | 10 | assumption | strategy/portfolio.md 5.1 (10 min per master). Wife minutes per still. |
| `offer.B1.tries` | count | 6 | 6 | 6 | assumption | stated logic (fidelity-heavy). Image-API tries per kept still. |
| `offer.B1.s_units` | units | 3 | 3 | 3 | assumption | content/sehuan/b2b-pitch.md B2 (up to three stills). Stills in the small package. |
| `offer.B1.m_units` | units | 8 | 8 | 8 | assumption | stated logic (two or three products). Stills in the medium package. |
| `offer.B2.fixed_op_min` | minutes | 150 | 150 | 150 | assumption | stated logic as B1. Operator fixed minutes. |
| `offer.B2.fixed_wife_min` | minutes | 75 | 75 | 75 | assumption | stated logic as B1. Wife fixed minutes. |
| `offer.B2.unit_op_min` | minutes | 40 | 40 | 40 | assumption | stated logic: arithmetic check against the client's dimension sheet, labels, export. Operator minutes per diagram. |
| `offer.B2.unit_wife_min` | minutes | 10 | 10 | 10 | assumption | strategy/portfolio.md 5.1. Wife minutes per diagram (zh-TW labels and 示意圖 badge). |
| `offer.B2.tries` | count | 1 | 1 | 1 | assumption | stated logic (character panel reused from the golden set). Image-API tries per diagram. |
| `offer.B2.s_units` | units | 3 | 3 | 3 | assumption | stated logic. Diagrams in the small package. |
| `offer.B2.m_units` | units | 8 | 8 | 8 | assumption | stated logic. Diagrams in the medium package. |
| `offer.B3.fixed_op_min` | minutes | 150 | 150 | 150 | assumption | stated logic as B1. Operator fixed minutes. |
| `offer.B3.fixed_wife_min` | minutes | 75 | 75 | 75 | assumption | stated logic as B1. Wife fixed minutes. |
| `offer.B3.unit_op_min` | minutes | 50 | 50 | 50 | assumption | strategy/portfolio.md 5.1 (N7 extra 20 min per master) plus card build. Operator minutes per card (capture, claims check against the source slip, 測試條件 label). |
| `offer.B3.unit_wife_min` | minutes | 12 | 12 | 12 | assumption | strategy/portfolio.md 5.1. Wife minutes per card. |
| `offer.B3.tries` | count | 3 | 3 | 3 | assumption | stated logic. Image-API tries per card. |
| `offer.B3.s_units` | units | 5 | 5 | 5 | assumption | stated logic (one carousel). Cards in the small package. |
| `offer.B3.m_units` | units | 12 | 12 | 12 | assumption | stated logic. Cards in the medium package. |
| `offer.SP.fixed_op_min` | minutes | 120 | 120 | 120 | assumption | stated logic: brief, contract, brand permission and paid-partnership tag, post-live check, invoice. Operator fixed minutes. |
| `offer.SP.fixed_wife_min` | minutes | 60 | 60 | 60 | assumption | stated logic. Wife fixed minutes. |
| `offer.SP.unit_op_min` | minutes | 90 | 90 | 90 | assumption | stated logic: claims check against the brand's source slip, labels, four-place disclosure check. Operator minutes per master. |
| `offer.SP.unit_wife_min` | minutes | 25 | 25 | 25 | assumption | strategy/portfolio.md 5.1 (10 min per master) plus brand rounds. Wife minutes per master. |
| `offer.SP.tries` | count | 3 | 3 | 3 | assumption | stated logic. Image-API tries. |
| `offer.SP.units` | units | 1 | 1 | 1 | assumption | stated logic. Masters per package. |
| `offer.SP.report_op_min.t0` | minutes | 0 | 0 | 0 | assumption | stated logic. Post-campaign report minutes, tier 0 (no audience): none, no numbers exist to report. |
| `offer.SP.report_op_min.t1` | minutes | 30 | 30 | 30 | assumption | stated logic. Tier 1: platform insights screenshots plus a one-page note, only real numbers. |
| `offer.SP.report_op_min.t2` | minutes | 60 | 60 | 60 | assumption | stated logic. Tier 2: 14-day insights report. |
| `offer.SP.report_op_min.t3` | minutes | 90 | 90 | 90 | assumption | stated logic. Tier 3: 14-day insights report plus a call. |

**D. Own digital products (formula)**

| Key | Unit | Low | Mid | High | Status | Source or logic |
| :--- | :--- | ---: | ---: | ---: | :--- | :--- |
| `prod.P1.op_h` | hours | 8 | 8 | 8 | assumption | stated logic. Operator hours to make the 方寸 printable checklist and template pack. |
| `prod.P1.wife_h` | hours | 3 | 3 | 3 | assumption | stated logic. Wife hours to review it. |
| `prod.P2.op_h` | hours | 8 | 8 | 8 | assumption | stated logic. Operator hours to make the 步驟 template and prompt pack. |
| `prod.P2.wife_h` | hours | 3 | 3 | 3 | assumption | stated logic. Wife hours to review it. |
| `prod.P3.op_h` | hours | 10 | 10 | 10 | assumption | stated logic. Operator hours to make the 色環 colour guide (wheel, chip cards). |
| `prod.P3.wife_h` | hours | 4 | 4 | 4 | assumption | stated logic. Wife hours to review it. |
| `prod.tries` | count | 12 | 12 | 12 | assumption | stated logic. Image-API tries per pack. |
| `prod.payback_units` | units | 40 | 40 | 40 | assumption | stated logic. Sales at which a pack has repaid its hours at the assumed hourly values plus margin. Sets the proposed list price. Not a demand estimate. |
| `prod.fee_rate` | fraction | 0.15 | 0.15 | 0.15 | placeholder | none: marketplace and payment fee rates were not found [TO FILL WHEN REAL]. Share of each product sale lost to marketplace and payment fees. |
| `prod.round_to` | NT$ | 10 | 10 | 10 | assumption | stated logic. List prices are rounded UP to this step. |

**E. Scenario inputs**

| Key | Unit | Low | Mid | High | Status | Source or logic |
| :--- | :--- | ---: | ---: | ---: | :--- | :--- |
| `b2b.fangcun.s_jobs` | jobs | 0 | 1 | 2 | assumption | strategy/portfolio.md H6; Phase 1 hypothetical 3 / 8 jobs. Paid small jobs, room-render set (B2). |
| `b2b.fangcun.m_jobs` | jobs | 0 | 0 | 1 | assumption | as above. Paid medium jobs, room-render set (B2). |
| `b2b.buzhou.s_jobs` | jobs | 0 | 1 | 2 | assumption | strategy/portfolio.md H6. Paid small jobs, explainer stills set (B3). |
| `b2b.buzhou.m_jobs` | jobs | 0 | 0 | 1 | assumption | as above. Paid medium jobs, explainer stills set (B3). |
| `b2b.sehuan.s_jobs` | jobs | 0 | 1 | 1 | assumption | strategy/portfolio.md H5 (about five warm fashion contacts). Paid small jobs, lookbook stills set (B1). |
| `b2b.sehuan.m_jobs` | jobs | 0 | 0 | 2 | assumption | as above. Paid medium jobs, lookbook stills set (B1). |
| `b2b.first_paid_month` | month | 8 | 6 | 4 | assumption | research/monetisation.md 3.7 (1 to 3 months after registration) and strategy/portfolio.md 6.4. First model month with a paid job delivered. Needs registration, the recorded tool licence, the lawyer's paid-gate answers and a free sample first. |
| `b2b.last_month` | month | 12 | 12 | 12 | assumption | stated logic. Jobs are spread evenly from the first paid month to this month. |
| `b2b.realisation` | fraction | 0.6 | 0.8 | 0.9 | assumption | stated logic. Share of the proposed price actually realised after negotiation. No market evidence; recalibrate with 3+ quotes. |
| `b2b.samples` | count | 1 | 3 | 5 | assumption | strategy/portfolio.md 6.4 (at least 1 free scoped sample by week 8) and H5 (five warm contacts); H6 (a sample or enquiry for N9 and N7). Free private samples, small size, one per month, cycling 色環, 方寸, 步驟. They cost hours and image tries and earn nothing. High has more paid jobs than samples because it includes repeat clients. |
| `b2b.sample_first_month` | month | 2 | 2 | 2 | assumption | strategy/portfolio.md 6.4. Month of the first sample; one per month after. |
| `b2b.lag` | months | 1 | 1 | 1 | assumption | stated logic. Months from delivery to cash. Payment terms are not agreed. |
| `b2b.outreach_contacts` | count | 5 | 25 | 60 | assumption | strategy/portfolio.md H5 (5 warm contacts) plus the Phase 8 outreach lists. Brands or agencies approached. Used only to show the implied conversion. |
| `sp.fangcun.deals` | deals | 0 | 0 | 1 | assumption | research/monetisation.md 6.3 (0 / 1 / 4 deals). Sponsored posts on 方寸. |
| `sp.buzhou.deals` | deals | 0 | 0 | 1 | assumption | as above. Sponsored posts on 步驟. |
| `sp.sehuan.deals` | deals | 0 | 1 | 2 | assumption | as above. Sponsored posts on 色環. |
| `sp.tier` | tier | 0 | 1 | 1 | assumption | research/monetisation.md 3.1. Audience tier of the account at the time of the deal (0 to 3). No persona is assumed above tier 1 within 12 months. |
| `sp.first_month` | month | 8 | 8 | 6 | assumption | research/monetisation.md 2 (3 to 6+ months). First sponsored post month. |
| `sp.realisation` | fraction | 0.6 | 0.8 | 0.9 | assumption | stated logic. Share of the proposed price realised. |
| `sp.reach_premium` | NT$ | 0 | 0 | 0 | placeholder | none: no Taiwan reach-based rate was found [TO FILL WHEN REAL]. Reach component added to the production price per deal. Zero until 3+ real quotes exist. |
| `sp.lag` | months | 1 | 1 | 1 | assumption | stated logic. Months from posting to cash. |
| `aff.first_month` | month | 2 | 2 | 2 | assumption | research/monetisation.md 5 (apply before the first post). First month a link is live on the link page. |
| `aff.ramp_months` | months | 8 | 8 | 8 | assumption | stated logic. Months to reach the steady-state monthly impressions (linear). |
| `aff.impressions.fangcun` | count/month | 3000 | 25000 | 150000 | assumption | none: no Taiwan reach benchmark exists. Steady-state monthly impressions across the persona's platforms. A hypothesis, not a forecast. |
| `aff.impressions.buzhou` | count/month | 3000 | 25000 | 150000 | assumption | none. As above. |
| `aff.impressions.sehuan` | count/month | 3000 | 25000 | 150000 | assumption | none. As above. |
| `aff.weight.fangcun` | factor | 1 | 1 | 1 | assumption | none: no evidence on relative reach. Multiplier on the persona's impressions. |
| `aff.weight.buzhou` | factor | 1 | 1 | 1 | assumption | none. As above. |
| `aff.weight.sehuan` | factor | 1 | 1 | 1 | assumption | none. As above. |
| `aff.click_rate` | fraction | 0.003 | 0.007 | 0.01 | assumption | research/monetisation.md 6.2 used 1% of impressions as its hypothetical value. Share of impressions that click through to a tracked affiliate link. High equals the Phase 1 hypothetical 1%; low and mid are lower. Link-in-bio flows typically lose more (unverified). |
| `aff.click_to_order` | fraction | 0.01 | 0.02 | 0.02 | assumption | research/monetisation.md 6.2 used 2% click-to-order. Share of link clicks that become an order. Mid and high equal the Phase 1 hypothetical 2%. |
| `aff.aov` | NT$ | 500 | 500 | 500 | hypothetical | research/monetisation.md 6.2 (average order NT$500). Average order value. Hypothetical axis value. |
| `aff.commission` | fraction | 0.02 | 0.05 | 0.08 | hypothetical | research/monetisation.md 6.2 (commission 2% / 5% / 8%). Commission rate. No Taiwan programme terms were found (G3, G4). |
| `aff.admin_op_min_month` | minutes | 30 | 30 | 30 | assumption | stated logic. Operator minutes a month for link upkeep and disclosure checks, from the first live month. |
| `aff.lag` | months | 2 | 2 | 2 | assumption | none: payout threshold and schedule not found. Months from sale to payout. |
| `prod.fangcun.made` | flag | 0 | 1 | 1 | assumption | stated logic. 1 = the pack is made. Low = the checkpoint shows no signal and the hours are not spent. |
| `prod.buzhou.made` | flag | 0 | 1 | 1 | assumption | as above. As above. |
| `prod.sehuan.made` | flag | 0 | 1 | 1 | assumption | as above. As above. |
| `prod.fangcun.units` | units/year | 0 | 5 | 25 | assumption | research/monetisation.md 6.3 (NT$0 / 2,000 / 10,000 a year). Units sold in the 12 months, spread evenly from the first sale month. Expected values, not a draw. |
| `prod.buzhou.units` | units/year | 0 | 2 | 10 | assumption | as above. As above. |
| `prod.sehuan.units` | units/year | 0 | 5 | 25 | assumption | as above. As above. |
| `prod.first_sale_month` | month | 6 | 5 | 4 | assumption | research/monetisation.md 2 (1 to 3 months to list) and the 記帳士 gate. First month of sales. |
| `prod.lag` | months | 1 | 1 | 1 | assumption | none: marketplace payout terms not found. Months from sale to cash. |
| `stk.fangcun.sets` | sets | 0 | 0 | 1 | assumption | personas/fangcun/photoreal-addendum.md 12.3 item 5. Sticker sets listed for 方寸. |
| `stk.buzhou.sets` | sets | 0 | 0 | 0 | assumption | personas/buzhou/bible.md 9.1 (weak, not planned). Sticker sets for 步驟: none in any scenario. |
| `stk.sehuan.sets` | sets | 0 | 1 | 1 | assumption | personas/sehuan/bible.md 9.1 (weak to medium, later). Sticker sets listed for 色環. |
| `stk.sales_per_set_month` | sales | 0 | 10 | 25 | assumption | research/monetisation.md 6.3 (NT$0 / 2,000 / 10,000 a year). Sales per set per month from the list month. Sticker earnings of unknown creators in Taiwan: not found. |
| `stk.first_month` | month | 8 | 7 | 6 | assumption | research/monetisation.md 3.3 (1 to 2 months to list) and the week-8 review. First month with sales. |
| `stk.creator_share` | NT$/sale | 12 | 12 | 12 | hypothetical | research/monetisation.md 6.2 (creator share NT$8 / 12 / 16 per sale; U1: about half of net sales, unverified). Net amount to the studio per sale. Price tiers and payout threshold not found (G5). |
| `stk.set_op_h` | hours | 12 | 12 | 12 | assumption | stated logic. Operator hours to make and submit one set. |
| `stk.set_wife_h` | hours | 3 | 3 | 3 | assumption | stated logic. Wife hours to review one set. |
| `stk.set_tries` | count | 40 | 40 | 40 | assumption | stated logic (about 16 stickers at 2 to 3 tries). Image-API tries per set. |
| `stk.lag` | months | 3 | 3 | 3 | assumption | none: payout calendar not found. Months from sale to payout. |
| `excl.platform_payouts` | NT$ | 0 | 0 | 0 | excluded | research/monetisation.md 3.5 and 5 (planned at NT$0 in year 1). YouTube Partner Programme thresholds are out of reach in year 1 [S17]. |
| `excl.licensing` | NT$ | 0 | 0 | 0 | excluded | research/monetisation.md 3.6 (9 to 18+ months; low in year 1). Spokes-character licensing: discuss only; no price; nothing modelled. |

**F. Costs**

| Key | Unit | Low | Mid | High | Status | Source or logic |
| :--- | :--- | ---: | ---: | ---: | :--- | :--- |
| `tools.budget` | NT$/month | 5000 | 5000 | 5000 | sourced | DECISIONS.md Q1 (NT$5,000 to 10,000 a month, tools only). Base-case monthly tools budget. The NT$10,000 headroom is run as a variant. |
| `tools.early_fraction` | fraction | 0.6 | 0.6 | 0.6 | assumption | strategy/portfolio.md 7 (stay below the cap in months 1 to 3). Share of the budget spent in the early months. |
| `tools.early_months` | months | 3 | 3 | 3 | assumption | strategy/portfolio.md 7. Number of early months. |
| `tools.m0` | NT$ | 0 | 0 | 0 | assumption | stated logic. Tools spend in M0 (no persona live). |
| `cost.scale` | factor | 1 | 1 | 1 | assumption | stated logic. Multiplier on all placeholder compliance costs below. Used by the sensitivity table. |
| `cost.registration` | NT$ | 10000 | 10000 | 10000 | placeholder | none: registration fees not found [TO FILL WHEN REAL]. One-time: business registration (HUMAN_TODO 4). NOT a quote. |
| `cost.registration.month` | month | 0 | 0 | 0 | assumption | DECISIONS.md Q5 (about 2 weeks). Month paid. |
| `cost.bookkeeper_setup` | NT$ | 3000 | 3000 | 3000 | placeholder | none: 記帳士 fees not found [TO FILL WHEN REAL]. One-time: bookkeeper set-up. NOT a quote. |
| `cost.bookkeeper_setup.month` | month | 0 | 0 | 0 | assumption | stated logic. Month paid. |
| `cost.lawyer_launch` | NT$ | 10000 | 10000 | 10000 | placeholder | none: lawyer fees not found [TO FILL WHEN REAL]. One-time: launch-gate consult (research/legal.md section 12). NOT a quote. |
| `cost.lawyer_launch.month` | month | 0 | 0 | 0 | assumption | HUMAN_TODO 9. Month paid. |
| `cost.lawyer_contract` | NT$ | 8000 | 8000 | 8000 | placeholder | none [TO FILL WHEN REAL]. One-time: contract template review (legal.md Q24). NOT a quote. |
| `cost.lawyer_contract.month` | month | 3 | 3 | 3 | assumption | stated logic (before the first paid deal). Month paid. |
| `cost.trademark` | NT$ | 10000 | 10000 | 10000 | placeholder | none: TIPO fees not found [TO FILL WHEN REAL]. One-time: trade mark filing for the studio name (legal.md Q18). NOT a quote. |
| `cost.trademark.month` | month | 3 | 3 | 3 | assumption | legal.md Q18 is tagged Later. Month paid. |
| `cost.bookkeeper_monthly` | NT$/month | 1500 | 1500 | 1500 | placeholder | none [TO FILL WHEN REAL]. Recurring bookkeeping once registered, from M1. NOT a quote. |

**G. Phase 1 hypothesis replayed**

| Key | Unit | Low | Mid | High | Status | Source or logic |
| :--- | :--- | ---: | ---: | ---: | :--- | :--- |
| `phase1.b2b_jobs` | jobs | 0 | 3 | 8 | sourced | research/monetisation.md 6.3 (hypothetical cells). Phase 1 B2B jobs. |
| `phase1.b2b_price` | NT$ | 4000 | 8000 | 15000 | sourced | research/monetisation.md 6.2 and 6.3 (hypothetical axis). Phase 1 price per B2B job. |
| `phase1.sp_deals` | deals | 0 | 1 | 4 | sourced | research/monetisation.md 6.3. Phase 1 sponsored deals. |
| `phase1.sp_price` | NT$ | 3000 | 5000 | 8000 | sourced | research/monetisation.md 6.2 and 6.3 (hypothetical axis). Phase 1 fee per deal. |
| `phase1.affiliate` | NT$ | 1000 | 5000 | 30000 | sourced | research/monetisation.md 6.3. Phase 1 affiliate commissions. |
| `phase1.stickers` | NT$ | 0 | 2000 | 10000 | sourced | research/monetisation.md 6.3. Phase 1 sticker income. |
| `phase1.products` | NT$ | 0 | 2000 | 10000 | sourced | research/monetisation.md 6.3. Phase 1 own-product income. |
| `phase1.licensing` | NT$ | 0 | 0 | 0 | sourced | research/monetisation.md 6.3. Phase 1 licensing (excluded). |
| `phase1.payouts` | NT$ | 0 | 0 | 0 | sourced | research/monetisation.md 6.3. Phase 1 platform payouts (excluded). |
| `phase1.spend_cap` | NT$ | 60000 | 60000 | 60000 | sourced | research/monetisation.md 6.1 A1 (12 x NT$5,000). Phase 1 twelve-month spend at the cap. |
<!-- END GENERATED:model-assumptions -->
