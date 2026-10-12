# Rate card (Phase 8), DRAFT v0.1

Written 2026-10-12 for the operator (English, with the zh-TW term beside each Taiwan-specific concept) and for the wife to check. Studio name 明說角色工作室 / Plainspoken Studio is provisional and uncleared. **Internal working document. Nothing here has been sent, quoted to anyone or published, and no client, price enquiry or price list exists.**

Companion files in this folder: [revenue-model.md](revenue-model.md) (what the prices add up to), [assumptions.csv](assumptions.csv) (every input), [model.py](model.py) (recomputes everything) and [test_model.py](test_model.py) (unit tests). The price tables below are **generated** from `assumptions.csv` by `python3 model.py docs --write`; to change a price, change the assumption and regenerate. Do not edit the tables by hand (a test fails if they drift).

---

## 0. Read this first

1. **Every price here is the studio's own PROPOSED ask, labelled assumption.** It is derived from stated hours, an assumed hourly value, an image-tool cost and a margin (section 1). It is not market data. Phase 1 could not find a Taiwan price for any route (`research/monetisation.md` section 0 and 3): no 業配 rate by follower tier, no CPM or per-video rate, no affiliate commission or cookie window, no LINE sticker payout threshold, no 品牌代言人 fee, no price for AI ad creative. Where a Phase 1 bracket is needed below, the cell says **not found**.
2. **The rates must be recalibrated against 3+ real quotes before they are used on a client** (monetisation gaps G1, G2, G10 and G11; section 5). Until then the table is an internal ask and a walk-away floor, not a price list.
3. **A price is a proposal with a floor.** The floor is the same arithmetic without the margin. The studio does not sell below the floor (section 5, rule R1).
4. **Gates before any number leaves the house** (all open on 2026-10-12):
   1. Business registered and the registrant question settled, so the studio can invoice and sign (HUMAN_TODO 4, 7). Which income can be received before registration is unverified, 記帳士 question (research/legal.md Q15 to Q17).
   2. The commercial-use terms of the exact image tool and plan are read and recorded (HUMAN_TODO 33). Until then every image is internal design material and **no client work is made**.
   3. The lawyer has answered the paid-gate questions that apply: Q5 (agency joint liability), Q8 (AI-person ad disclosure duty), Q19 (AI copyright and assignments), Q21 (what can be warranted about foreign generative tools) and Q24 (contract review). All Taiwan-law points in this file are **unverified, lawyer question**.
   4. The wife has read every zh-TW string (section 6), and the studio name is cleared (HUMAN_TODO 18, 20).
   5. At least three real quotes per offer family have been collected (section 5).
5. **On hold, not offered:** a photoreal character shown in a client's garment (虛擬試穿示意) until the lawyer answers whether labelled try-on creative can mislead, who carries garment-accuracy liability and whether a free public sample is an advertisement (HUMAN_TODO 27, 37); photoreal product-in-room images (invented-detail risk, `personas/fangcun/photoreal-addendum.md` 5.5); video, voice, lip-sync or any animation of a photoreal face (decision D6 allows only stills and slow pans or zooms of stills inside a Reel or Short).
6. **Nothing is sent by Claude.** Outreach is sent by the humans only.

Labels used: **sourced** (from a project file, with its own confidence label); **assumption** (the studio's planning figure; the logic is stated); **hypothetical** (a Phase 1 hypothetical axis value, not market data); **placeholder** (no source exists; a stand-in; `[TO FILL WHEN REAL]`); **not found** (Phase 1 looked and had no figure); **unverified, lawyer question**.

---

## 1. The pricing method

**Price = (operator hours x operator hourly value + wife hours x wife hourly value + image-tool cost) x (1 + margin), rounded up to the next NT$100.**

- **Hours** = fixed minutes (scoping, brief and source slip, client messages, delivery and invoice) + per-unit minutes x units x (1 + included revision rounds x share of a set redone per round). The minutes are in `assumptions.csv`, keys `offer.*`; they are estimates and are replaced by measured minutes after the first sample (portfolio H8).
- **Hourly values** are an assumed opportunity value of the couple's time, not a wage and not a market rate. They lie within the range of the Phase 1 hypothetical reviewer axis of NT$300 / 500 / 800 an hour (`research/SUMMARY.md` iv); NT$600 is not itself an axis value, and that axis priced native zh-TW review, not production, so it is a borrowed scale, not evidence. The wife's time is **not paid in cash** (DECISIONS: reviewer is the wife, no cash budget); it is priced so the arithmetic shows what the work is worth, and the revenue model reports cash separately.
- **Image-tool cost** = tries x cost per try x unit-works. The cost per try is from `pipeline/tools.md` section 5 (secondary list prices, low to medium confidence, not checked against an invoice).
- **Margin** covers rework beyond the included rounds, unpaid scoping and sales time, tool price changes and a contribution to the shared tools budget. It is not a profit claim.
- **Floor** = hours at the assumed values + tool cost, no margin.
- **Turnaround** = operator hours divided by the hours a week a client job can get (about 1.5, because the personas use the rest), rounded up, plus a week for the client's approvals. It is slow on purpose: the plan has almost no slack (ops/risk-register.md PPL-1). Rush delivery is not offered.
- **Not in any price:** business tax or withholding (unverified, 記帳士 question); platform or marketplace fees; the client's media spend; a **rights-value premium** for wider usage `[TO FILL WHEN REAL]`; a **reach component** for a sponsored post `[TO FILL WHEN REAL]`.

<!-- BEGIN GENERATED:rate-params -->
| Parameter | Value | Status | Source or logic |
| :--- | ---: | :--- | :--- |
| Operator hourly value (NT$/h) | 600 | assumption | stated logic, chosen between the Phase 1 hypothetical axis points NT$500 and NT$800 per hour (research/SUMMARY.md iv); 600 is not itself an axis value, and that axis priced native zh-TW review, not production |
| Wife hourly value (NT$/h) | 500 | assumption | research/SUMMARY.md iv: same hypothetical axis, middle value |
| Margin on cost | 0.25 | assumption | stated logic |
| Asks rounded up to (NT$) | 100 | assumption | stated logic |
| Image-API cost of one try (NT$) | 8.6 | sourced | pipeline/tools.md section 5 (Gemini Pro-class with two paid reference inputs, about US$0.268 at NT$32 per US$; tools.md itself calls the 0.268 a one-source guess); SOURCES.md PT3 (low to medium) |
| Share of a set redone per revision round | 0.2 | assumption | stated logic |
| Revision rounds included | 2 | assumption | content/sehuan/b2b-pitch.md B5 (two rounds of changes) |
| Operator hours per week a client job can get | 1.5 | assumption | cap.op_hours_revenue_month: 4 to 7.5 h a month is about 0.9 to 1.7 h a week; 1.5 chosen |
| Approval buffer (weeks) | 1 | assumption | stated logic |
<!-- END GENERATED:rate-params -->

### Summary of proposed prices (middle-scenario parameters)

<!-- BEGIN GENERATED:rate-summary -->
| ID | Offer | Scope | Operator h | Wife h | Floor or cost (NT$) | Proposed price (NT$) | Turnaround (weeks) |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| B1-S | Lookbook stills set (fashion) | 3 stills | 5.7 | 1.9 | 4,582 | **5,800** | 5 |
| B1-M | Lookbook stills set (fashion) | 8 stills | 10.9 | 3.1 | 8,676 | **10,900** | 9 |
| B2-S | Room-render diagram set (home) | 3 diagrams | 5.3 | 1.9 | 4,191 | **5,300** | 5 |
| B2-M | Room-render diagram set (home) | 8 diagrams | 10.0 | 3.1 | 7,635 | **9,600** | 8 |
| B3-S | Explainer stills set (software and SMEs) | 5 cards | 8.3 | 2.6 | 6,506 | **8,200** | 7 |
| B3-M | Explainer stills set (software and SMEs) | 12 cards | 16.5 | 4.6 | 12,638 | **15,800** | 12 |
| SP-T0 | Sponsored post (業配), tier 0, production price only | 1 master + 1 variant | 4.1 | 1.6 | 3,288 | **4,200** | 4 |
| SP-T1 | Sponsored post (業配), tier 1, production price only | 1 master + 1 variant | 4.6 | 1.6 | 3,588 | **4,500** | 5 |
| P1 | 方寸 printable checklist and template pack | 1 pack | 8 | 3 | 6,403 | **240** | n/a |
| P2 | 步驟 template and prompt pack | 1 pack | 8 | 3 | 6,403 | **240** | n/a |
| P3 | 色環 colour guide (wheel and chip cards) | 1 pack | 10 | 4 | 8,103 | **300** | n/a |
<!-- END GENERATED:rate-summary -->

Prices are in NT$, exclusive of any tax (to be settled with the 記帳士 once the studio is registered). Operator and wife hours are the estimated working hours, not a promise of availability.

---

## 2. Terms that apply to every offer

| Term | Standing rule |
|---|---|
| **Disclosure** | The character is an AI virtual character, never a person. Anything published carries the four places: bio, first caption line, on-screen label, platform AI label. A client may not ask to remove, shrink or move a label. Paid or client content on a persona account carries 【業配】 or 【合作內容】 on the first line plus the platform's paid-partnership tool; gifted goods carry 【廠商提供】; affiliate links carry 【含分潤連結】 (`strategy/portfolio.md` 1.4). |
| **Boosted posts** | If the client boosts or runs a post as an ad, the platform's AI-disclosure control is switched on for that ad. A duty to disclose AI-generated personal images in ads is reported (Fraud Crime Hazard Prevention Act, Meta reportedly fined NT$5 million; decision date and articles unverified, research/monetisation.md S13). Whether it reaches the advertiser or an organic post is **unverified, lawyer question** (legal.md Q8). Boost handling is a priced add-on (section 3.9). |
| **No testimonial** | The character has not worn, used, tested, eaten or visited anything. No experience claim, review, 開箱, 實測, 愛用, 心得, customer quote or result, written or implied (Ground rule 4). A brief that needs one is declined or rewritten. |
| **Not accepted at any price** | Health, medical, weight-loss or cosmetic-efficacy claims, supplements and beauty sold on efficacy; investment or financial products and any referral link for them (brokers, funds, ETFs, cards, loans, loan apps, buy-now-pay-later, insurance, crypto); gambling and lotteries; politics, elections and cross-strait topics; face-swap, voice-cloning or any deepfake-capable tool; anything illegal. The per-persona decline lists in each bible, section 9.2, apply in addition. |
| **No outcome promised** | No views, reach, followers, engagement or sales are promised or implied (Ground rule 10). |
| **Client supplies** | Product photographs or specifications with a written usage licence, and sources with dates for every claim. The client warrants accuracy and indemnifies the studio for the claims it supplies; the studio may refuse any claim that touches Ground rule 6 (legal.md Q5, Q24). No photograph of a real person is ever used as an image reference. |
| **Approvals** | Nothing is used until the client has approved each image in writing. The operator and the wife approve before anything is sent. A factual error is corrected or taken down within 24 hours. |
| **Revisions** | Two rounds are included in every price (a round redoes about a fifth of a set). More rounds are priced in the add-ons. A change of scope is re-quoted. |
| **Usage rights (default, assumption)** | Non-exclusive licence to use the deliverables on the client's own channels, Taiwan, 12 months. No model training on the studio's character or assets. The studio keeps the character, its designs and its name. The studio does not warrant that purely AI-generated output is protected by copyright (**unverified, lawyer question**, legal.md 8.2 and Q19). Paid-media use is an add-on. No exclusivity, no perpetual buy-out. Wider terms are a quote with a rights-value premium `[TO FILL WHEN REAL]`. |
| **Invoicing and payment** | Only the registered business invoices. Tax treatment and payment terms are `[TO FILL WHEN REAL]` (HUMAN_TODO 4; legal.md Q15). The revenue model assumes cash one month after delivery (assumption). |
| **Quote validity** | 14 days from the date of the written quote (assumption). |
| **Tool licence** | No client work starts until the exact tool and plan's commercial-use terms are read and recorded (HUMAN_TODO 33). The studio does not promise a client that an output is unique or free of look-alike risk beyond its documented provenance and look-alike process (bible 9.4). |

---

## 3. Offer sheets

Each sheet gives scope, deliverables, revisions, usage rights, turnaround, the proposed price with its derivation, the Phase 1 sourced bracket with its label, and what is explicitly excluded. B2B income belongs to the **studio**; the persona is the showroom, tagged for tracking only (`strategy/portfolio.md` 2C, 6.4).

### 3.1 B1. Lookbook stills set (fashion; showroom 色環)

| | |
|---|---|
| **Scope** | Still images of an original AI-generated character shown with the client's garment, built only from the client's own product-only photographs (flat lay, ghost mannequin or hanger), for the client's own lookbook or channels. |
| **Deliverables** | Small: 3 stills. Medium: 8 stills (two or three products). Each in 4:5 and 1:1, with alt text, a typeset on-image label 「虛擬試穿示意｜AI 生成示意，角色未實際穿著」, and the provenance rows. |
| **Revisions** | 2 rounds included. |
| **Usage rights** | Section 2 default. Posting on a persona account makes it a 【合作內容】 post with the platform tool. |
| **Turnaround** | In the table below (weeks from complete brief and assets, approvals in parallel). |
| **Phase 1 sourced bracket** | Price of comparable Taiwan AI-creative studios or freelancers per image or video: **not found**. Brand budgets per image or video: **not found** (monetisation.md 3.7; gap G11). Hypothetical axis only: NT$4,000 / 8,000 / 15,000 per job (monetisation.md 6.2). Demand signals are inference: Life8 likeness dispute and IKEA Taiwan's distorted hands (S31, S32, medium), the reported Meta fine (S13). |
| **Excluded** | Fit, comfort, size, body, skin, slimming or health wording; any statement the character wore or liked the garment; invented or "improved" garment detail (200% fidelity check; if the tool cannot hold the detail, the image is dropped); a real model's photograph or a look-alike; a generated logo; video, voice or animation; colour correction that flatters the garment. |
| **Status** | **The virtual-model stills are ON HOLD** (gate 5 in section 0). Two face-free options need no lawyer answer on try-on and can be tested first: a **colour-story board** and a **flat-lay lookbook layout**, both built from the client's product-only photographs and labelled 搭配示意 (`content/sehuan/b2b-pitch.md` A4, options 1 and 2). Until a first sample measures their real minutes, price them with the **B2 table** (same kind of work: layout and colour arithmetic checked against the client's published information; no image-model face). Assumption. |

<!-- BEGIN GENERATED:rate-B1 -->
| Step | B1-S Small (stills) | B1-M Medium (stills) |
| :--- | ---: | ---: |
| Deliverable units | 3 | 8 |
| Unit-works incl. 2 revision rounds at 20% of a set | 4.2 | 11.2 |
| Operator hours | 5.65 | 10.90 |
| Wife hours | 1.95 | 3.12 |
| Operator time at NT$600/h (NT$) | 3,390 | 6,540 |
| Wife time at NT$500/h (NT$) | 975 | 1,558 |
| Image-tool cost (NT$) | 217 | 578 |
| Floor: walk-away cost, no margin (NT$) | 4,582 | 8,676 |
| Plus margin 25% (NT$, before rounding) | 5,727 | 10,845 |
| **Proposed price, rounded up (NT$)** | **5,800** | **10,900** |
| Quoted turnaround (weeks, from complete brief and assets) | 5 | 9 |
<!-- END GENERATED:rate-B1 -->

### 3.2 B2. Room-render diagram set (home and storage; showroom 方寸)

| | |
|---|---|
| **Scope** | Dimension-accurate 示意 diagrams (flat or isometric, vector) of a room or zone using the client's **published** dimensions and capacities, with the character in a framed panel beside the diagram, never inside the plan. Drawn as vector by Claude and checked by a human (decision D3). |
| **Deliverables** | Small: 3 diagrams. Medium: 8 diagrams. Each with the badge 「AI 生成｜示意圖」, a source-and-date line and alt text. |
| **Revisions** | 2 rounds included. |
| **Usage rights** | Section 2 default. |
| **Turnaround** | In the table below. |
| **Phase 1 sourced bracket** | Price per image or per package for comparable work: **not found** (monetisation.md 3.7; G11). Hypothetical axis only, as for B1. |
| **Excluded** | Photoreal rooms and product-in-room renders (not offered; invented-detail risk and "her flat" implication); mould, damp, allergy, sleep or air-quality claims; installation, gas, electrical, structural or load advice (cite the maker's manual or decline); lease-law advice; a result such as "space doubled"; a before-and-after; any dimension the client cannot document in writing. |
| **Status** | Needs registration, the recorded tool licence (the character panel is reused from the golden set), and the lawyer's Q5, Q24. |

<!-- BEGIN GENERATED:rate-B2 -->
| Step | B2-S Small (diagrams) | B2-M Medium (diagrams) |
| :--- | ---: | ---: |
| Deliverable units | 3 | 8 |
| Unit-works incl. 2 revision rounds at 20% of a set | 4.2 | 11.2 |
| Operator hours | 5.30 | 9.97 |
| Wife hours | 1.95 | 3.12 |
| Operator time at NT$600/h (NT$) | 3,180 | 5,980 |
| Wife time at NT$500/h (NT$) | 975 | 1,558 |
| Image-tool cost (NT$) | 36 | 96 |
| Floor: walk-away cost, no margin (NT$) | 4,191 | 7,635 |
| Plus margin 25% (NT$, before rounding) | 5,239 | 9,543 |
| **Proposed price, rounded up (NT$)** | **5,300** | **9,600** |
| Quoted turnaround (weeks, from complete brief and assets) | 5 | 8 |
<!-- END GENERATED:rate-B2 -->

### 3.3 B3. Explainer stills set (software and Taiwan SMEs; showroom 步驟)

| | |
|---|---|
| **Scope** | Explainer cards for a software product or process: the character as a small picture-in-picture beside a dated screen capture supplied by the client or recorded by the operator, with 「測試條件」 (tool, version, plan, date) on screen. Stills only. |
| **Deliverables** | Small: 5 cards (one carousel). Medium: 12 cards. Each with a source-and-date line, the AI label and alt text. |
| **Revisions** | 2 rounds included. |
| **Usage rights** | Section 2 default. |
| **Turnaround** | In the table below. |
| **Phase 1 sourced bracket** | Price per explainer video or still: **not found** (monetisation.md 3.7; G11). Hypothetical axis only. |
| **Excluded** | **Video, voice and lip-sync** (not offered: the operator edits any video, and face animation or a synthetic voice on a photoreal face is barred until a separate review); "make money with AI", side-hustle (副業) or income framing; trading, forex, crypto or betting bots; AI answering medical, legal, investment or gambling questions; claims about security, privacy or accuracy the client cannot document; collecting viewers' personal data or leads; superlatives and undated prices. |
| **Status** | Needs registration, the recorded tool licence and Q5, Q24. The operator checks every claim against the client's source slip. |

<!-- BEGIN GENERATED:rate-B3 -->
| Step | B3-S Small (cards) | B3-M Medium (cards) |
| :--- | ---: | ---: |
| Deliverable units | 5 | 12 |
| Unit-works incl. 2 revision rounds at 20% of a set | 7.0 | 16.8 |
| Operator hours | 8.33 | 16.50 |
| Wife hours | 2.65 | 4.61 |
| Operator time at NT$600/h (NT$) | 5,000 | 9,900 |
| Wife time at NT$500/h (NT$) | 1,325 | 2,305 |
| Image-tool cost (NT$) | 181 | 433 |
| Floor: walk-away cost, no margin (NT$) | 6,506 | 12,638 |
| Plus margin 25% (NT$, before rounding) | 8,132 | 15,798 |
| **Proposed price, rounded up (NT$)** | **8,200** | **15,800** |
| Quoted turnaround (weeks, from complete brief and assets) | 7 | 12 |
<!-- END GENERATED:rate-B3 -->

### 3.4 SP. Sponsored post (業配) by tier

| | |
|---|---|
| **Scope** | One master (a carousel of up to 6 slides, or a still-based Short under decision D6) plus one platform variant, published on **one persona's** account as an explanation, comparison or demonstration of public information. Briefs that ask for a first-hand experience are declined. |
| **Deliverables** | The master and the variant; the first-line label 【業配】, the platform's paid-partnership tool (with the brand's permission), the AI label on every post; a post-live four-place check; for tiers 1 to 3 a short insights report using real platform numbers only. |
| **Revisions** | 2 rounds included. |
| **Usage rights** | Organic post on the persona's account for as long as the platform keeps it. The brand may re-share it with the platform's branded-content tool. Boosting, ads and use off the platform are add-ons. Section 2 otherwise. |
| **Turnaround** | In the table below. |
| **Phase 1 sourced bracket** | **Every tier row is "not found"**: Nano, Micro, Mid, Macro tier boundaries for Taiwan, and the 業配 rate per post or video, and CPM, CPC or per-view rates (monetisation.md 3.1; G1, G2). Related signals: a Taiwan VTuber agency says corporate collaborations are budgeted case by case with no fixed rate card (S7, medium); Taiwan's influencer-marketing market is reported at about US$239 million, +11.7% a year, with Instagram on 57.7% of campaigns (S1, medium, regional report as summarised in Taiwan press); virtual-influencer sponsored-post engagement is weak (Lil Miquela on BMW posts 0.6% against 3.6% for human creators; Imma 0.2% to 0.3%; Rozy 1.9%; S3 to S5, medium, third-party trackers and a vendor release). Hypothetical axis only: NT$3,000 / 8,000 / 20,000 per post (monetisation.md 6.2). |
| **How the tiers work here** | The follower boundaries below are the studio's working assumption, to be replaced by the agencies' own definitions (G1). The production price comes from hours and is the same kind of number at every tier; only the report time differs. The **reach component** is `[TO FILL WHEN REAL]` for tiers 1 to 3: it will be median verified reach per post times a CPM taken from 3+ real quotes. **Tier 0 has no reach to price**, so a tier-0 account is sold only for its creative, never for its audience. Every pilot is expected to be tier 0 or 1 in its first year (assumption). |
| **Excluded** | Testimonial or "I tried it" copy; health, weight-loss, cosmetic-efficacy, supplement, financial, gambling and political briefs; required superlatives or unsourced numbers; a request to hide or shrink a label; seeded likes or friends' comments (Ground rule 7); the same brand on two personas in the same ISO week; persona-to-persona recommendation. |
| **Status** | Needs registration, the paid-partnership permission, the Instagram AI-label check on the real account, and legal.md Q4, Q8. |

<!-- BEGIN GENERATED:rate-SP -->
| Tier | Followers on the platform (assumption; replace with agency definitions, G1) | Report minutes | Floor (NT$) | Production price, rounded up (NT$) | Reach component | Turnaround (weeks) |
| :--- | :--- | ---: | ---: | ---: | :--- | ---: |
| T0 | no audience yet (under 1,000 followers on the platform) | 0 | 3,288 | 4,200 | none (no reach to price) | 4 |
| T1 | 1,000 to under 10,000 | 30 | 3,588 | 4,500 | [TO FILL WHEN REAL] | 5 |
| T2 | 10,000 to under 100,000 | 60 | 3,888 | 4,900 | [TO FILL WHEN REAL] | 5 |
| T3 | 100,000 and above | 90 | 4,188 | 5,300 | [TO FILL WHEN REAL] | 5 |
<!-- END GENERATED:rate-SP -->

Derivation:

<!-- BEGIN GENERATED:rate-SP-derivation -->
| Step | T0 | T1 | T2 | T3 |
| :--- | ---: | ---: | ---: | ---: |
| Deliverable units | 1 | 1 | 1 | 1 |
| Unit-works incl. 2 revision rounds at 20% of a set | 1.4 | 1.4 | 1.4 | 1.4 |
| Operator hours | 4.10 | 4.60 | 5.10 | 5.60 |
| Wife hours | 1.58 | 1.58 | 1.58 | 1.58 |
| Operator time at NT$600/h (NT$) | 2,460 | 2,760 | 3,060 | 3,360 |
| Wife time at NT$500/h (NT$) | 792 | 792 | 792 | 792 |
| Image-tool cost (NT$) | 36 | 36 | 36 | 36 |
| Floor: walk-away cost, no margin (NT$) | 3,288 | 3,588 | 3,888 | 4,188 |
| Plus margin 25% (NT$, before rounding) | 4,110 | 4,485 | 4,860 | 5,235 |
| **Proposed price, rounded up (NT$)** | **4,200** | **4,500** | **4,900** | **5,300** |
| Quoted turnaround (weeks, from complete brief and assets) | 4 | 5 | 5 | 5 |
<!-- END GENERATED:rate-SP-derivation -->

### 3.5 Affiliate (聯盟行銷, 分潤)

| | |
|---|---|
| **Scope** | The studio places tracked affiliate links on a persona's link page and, where a post uses one, marks it. There is no fee: the studio receives the programme's commission. |
| **Deliverables** | None to a client. Each link is disclosed with 【含分潤連結】 (「透過連結購買，工作室可能獲得分潤。」) in the post and on the link page. |
| **Revisions / usage / turnaround** | Not applicable. |
| **Price** | **None proposed.** The commission is set by the programme and the studio does not negotiate it. |
| **Phase 1 sourced bracket** | Commission, cookie window, payout threshold and whether individuals or virtual accounts are accepted: **not found** for every programme (monetisation.md 3.2; G3, G4). Taiwan is on YouTube Shopping's affiliate country list, and a Shopee pilot ran 2025-11-19 to 2025-12-31 (S19, medium). Hypothetical axis only: commission 2% / 5% / 8% (monetisation.md 6.2). |
| **Programmes to check** (existence from background knowledge, terms not opened; **verify existence and current contact route before outreach**) | Shopee 蝦皮分潤計畫, momo, PChome 24h, and the affiliate networks Accesstrade, ValueCommerce, Rakuten and CJ. Applications state plainly that the account is a disclosed AI persona run by a named studio. |
| **Excluded** | "I tried it" copy; any health, weight-loss, cosmetic-efficacy or supplement product; any financial product (brokers, funds, cards, loans, insurance, crypto) and any referral link for one; unlabelled links. |
| **Status** | Whether a programme accepts an unregistered individual or a virtual account is unverified (G3, G4, G12). |

### 3.6 Own digital products (checklists, templates, colour guides)

| | |
|---|---|
| **Scope** | One downloadable pack per pilot, original human-written text and human-built diagrams: P1 方寸 printable checklist and template pack (move-in and measure-before-you-buy); P2 步驟 template and prompt pack; P3 色環 colour guide (printable wheel and chip cards). |
| **Deliverables** | A PDF or template file, with the AI label and a source-and-date line on every factual page. |
| **Revisions** | Not applicable (a product, not a service). |
| **Usage rights** | A personal, single-user licence for the buyer; no redistribution. The digital-goods return rules and business-identity disclosure are **unverified, lawyer question** (legal.md 9 and Q23). The AI-art copyright caveat applies mainly to images (legal.md 8.2). |
| **Turnaround** | Not applicable. |
| **Phase 1 sourced bracket** | Taiwan marketplace terms and prices for digital products: **not found** (monetisation.md 3.8). Pinkoi, 方格子 (vocus), PressPlay and ECPay 綠界 are recalled as existing and were not checked (U5, unverified; verify existence and current contact route before outreach). Marketplace fee rates: **not found** (the model uses a placeholder). |
| **Proposed list price** | Production cost plus margin, repaid at 40 sales net of the assumed marketplace fee, rounded up to NT$10. **The number of sales is a payback target, not a demand estimate.** |
| **Gate before listing** | Compare at least five comparable Taiwan listings. If comparable packs sell for clearly less than the table's price, make the pack smaller or do not make it: the hours do not repay. |
| **Excluded** | Budgeting, investing or other finance templates (money-literacy only, if ever, and lawyer-gated); health, nutrition, workout or weight templates; any outcome promise; a "side-hustle" prompt pack. Not sold before the 記帳士 answers. |

<!-- BEGIN GENERATED:rate-products -->
| ID | Product | Operator h | Wife h | Tools (NT$) | Cost (NT$) | Price before rounding (NT$) | Proposed list price (NT$) | Net of assumed fees (NT$) | Sales to repay the hours at zero margin |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| P1 | 方寸 printable checklist and template pack | 8 | 3 | 103 | 6,403 | 235 | **240** | 204 | 31 |
| P2 | 步驟 template and prompt pack | 8 | 3 | 103 | 6,403 | 235 | **240** | 204 | 31 |
| P3 | 色環 colour guide (wheel and chip cards) | 10 | 4 | 103 | 8,103 | 298 | **300** | 255 | 32 |
<!-- END GENERATED:rate-products -->

### 3.7 LINE stickers (貼圖)

| | |
|---|---|
| **Scope** | A sticker set from a persona's expression set (E01 to E10 are designed as sticker poses), submitted through LINE Creators Market. |
| **Price** | **Not set by the studio.** LINE sets the price tiers (not found, G5). The table gives the studio's production cost and the sales needed to repay it. |
| **Phase 1 sourced bracket** | Revenue share: about half of net sales after store fees and tax (U1, recalled, **unverified**). Minimum payout, payout calendar, price tiers, pack sizes and Taiwan creators' earnings: **not found** (monetisation.md 3.3; G5). The Creators Market terms do not ban AI sets and LINE may display an AI label (S21, medium; clause number unconfirmed). Taiwan users send about 60 million stickers a day (S22, medium), which shows demand for characters with distribution, not what an unknown creator earns. Hypothetical axis only: studio share NT$8 / 12 / 16 per sale (monetisation.md 6.2). |
| **Status** | **Later, uncertain.** A photoreal-face sticker set is untested and the clay-figure route no longer applies (方寸 addendum 12.3). Not before the week-8 review and not before the Creators Market terms and review guideline are read (G5). Copyright in AI-made sticker art is **unverified, lawyer question** (legal.md 8.2). |
| **Excluded** | Any text on the sticker that has not been read by the wife; look-alikes of existing characters; a "real person" reading. |

<!-- BEGIN GENERATED:rate-stickers -->
| Item | Value |
| :--- | ---: |
| Production cost of one set (hours at assumed values + image tries), NT$ | 9,044 |
| Studio share per sale, hypothetical axis value (NT$) | 12 |
| Sales needed to repay one set's hours at zero margin | 754 |
| Studio-set sale price | none: LINE sets the price tiers (not found, G5) |
<!-- END GENERATED:rate-stickers -->

### 3.8 Character licensing and spokes-character (品牌代言人): discuss only, no price

- **No price, and no price range, will be given.** Every Taiwan precedent found is a corporate-owned or agency-owned character with distribution (中華電信 光音凱伶, Yahoo TV 虎妮, 7-ELEVEN OPEN將; research/monetisation.md S23, S27, S28, medium) and **no fee is public** (Phase 1: not found; G10). A solo studio's realistic entry, in the second year or later, is a small brand borrowing a persona for one campaign, quoted from scoping.
- **What would be discussed** (terms, not numbers): scope and channels, term, territory, a narrow and time-limited category scope in place of any exclusivity, AI-disclosure duties and who sets the labels, approvals and takedown within 24 hours, the studio keeping the character and name, no model training on assets, no real-person likeness, no testimonial, liability and termination.
- **What must exist first:** an audience with real numbers; a trade mark decision for the name (legal.md Q18; fees and timeline not found); a lawyer-reviewed contract (Q24); a documented origin and look-alike record for the face (provenance file, bible 9.4); three real comparables. Because purely AI-generated art may not be protected by copyright in Taiwan (U2, unverified, lawyer question), trade mark and contract carry the weight.
- **Excluded:** testimonials; health, finance, gambling and politics; a brand wanting the character to say it has used the product.
- **Revenue model:** nothing modelled in any scenario (excluded by rule, 9 to 18+ months and low in year 1, monetisation.md 3.6).

### 3.9 Add-ons

<!-- BEGIN GENERATED:rate-addons -->
| Offer | Extra revision round, small (NT$) | Extra revision round, medium (NT$) | Extra unit (NT$) |
| :--- | ---: | ---: | ---: |
| B1 Lookbook stills set (fashion) | 800 | 1,600 | 1,100 |
| B2 Room-render diagram set (home) | 800 | 1,400 | 900 |
| B3 Explainer stills set (software and SMEs) | 1,200 | 2,300 | 1,100 |

| Add-on | Floor (NT$) | Proposed price (NT$) | Derivation |
| :--- | ---: | ---: | :--- |
| Paid-media (boost) handling on a delivered piece | 1,450 | 1,900 | 120 operator minutes + 30 wife minutes of compliance handling at the assumed hourly values, plus margin; a rights-value premium is [TO FILL WHEN REAL] |
| Extra revision round on a sponsored post | 510 | 700 | revision share of one master plus 20 operator and 10 wife minutes of handling |
| Rush delivery | not offered | not offered | operator hours are shared with the personas (ops/risk-register.md PPL-1) |
| Exclusivity, perpetual buy-out, model-training rights | not offered | not offered | red flags in the persona bibles 9.3; discuss only a narrow, time-limited category scope, no price |
<!-- END GENERATED:rate-addons -->

---

## 4. Phase 1 sourced rate brackets, consolidated

Everything the Phase 1 research found for rates, with its label. Source: `research/monetisation.md` (IDs S and U as keyed there). **No row contains a Taiwan market price.** Foreign rate cards and unsourced blog ranges were deliberately not used as substitutes.

| Route | Rate Phase 1 found | Label |
|---|---|---|
| 業配, Nano tier | not found (tier boundaries not found; agencies define tiers differently) | not found |
| 業配, Micro tier | not found | not found |
| 業配, Mid tier | not found | not found |
| 業配, Macro tier | not found | not found |
| CPM, CPC, per-view | not found | not found |
| Agency practice | Corporate collaborations are budgeted case by case, not from a rate card (Taiwan VTuber agency, 2024) | S7, medium |
| Affiliate commission, cookie, threshold | not found for Shopee, momo, PChome and the networks | not found |
| LINE stickers | Creator share about half of net sales after store fees and tax; payout threshold and price tiers not found | U1 unverified; threshold not found |
| LINE Official Account | NT$0 (輕用量); NT$800 to NT$1,000 (中用量) and NT$1,200 to NT$1,400 (高用量) from 2026-11-01, ex-tax. A cost, not income | S24, medium |
| Platform payouts | Plan NT$0 in year 1 (YouTube Partner Programme thresholds out of reach; TikTok and Meta in Taiwan not found) | S17, medium (secondary) |
| Spokes-character / licensing | not found | not found |
| B2B AI ad creative | not found | not found |
| Own digital products | not found | not found |
| Fine range for false advertising (endorsement rules) | NT$50,000 to NT$25 million reported; statute text not seen | S11, medium (secondary); unverified, lawyer question |

Hypothetical axis values that Phase 1 used for break-even sensitivity (monetisation.md 6.2) and for its scenario cells (6.3). **They are not data.** They appear in this folder only as labelled sensitivity inputs and in the Phase 1 replay in the revenue model:

| Route | Axis values |
|---|---|
| B2B creative, price per job | NT$4,000 / 8,000 / 15,000 |
| 業配, fee per post | NT$3,000 / 8,000 / 20,000 (scenario cells: NT$5,000 and NT$8,000) |
| Affiliate commission | 2% / 5% / 8%, average order NT$500, click-to-order 2%, link click 1% |
| LINE stickers, studio share per sale | NT$8 / 12 / 16 |

---

## 5. Recalibration against 3+ real quotes (gaps G1, G2, G10, G11)

Rates must be recalibrated against three or more real quotes before they are used. The Phase 1 checkpoint (`strategy/portfolio.md` 6.4) wants at least three written rate quotes by week 8.

**What to collect** (humans send; nothing is sent by Claude):

1. **Agency rate sheets and tier definitions** for 業配 by tier, per post and per video, with the date, platform and whether virtual personas are accepted. Targets named in Phase 1: iKala (Kolr) and AnyMind Taiwan (both well known; **verify existence and current contact route before outreach**). Phase 1 also listed a third agency that it could not verify; pick a third one yourself, after confirming that it exists and what it sells. Read the Kolr (iKala) 2026 report as well (G1).
2. **Public price lists** of three to five Taiwan AI-photo or AI-video studios and freelancers (their own pages and social accounts; the job and freelance boards 104 and Yourator that Phase 1 named, existence recalled, **verify before use**), per image, per video, per package, with revision terms (G11).
3. **Media kits of five comparable Taiwan fashion creators**, to compute an effective CPM from rate and average reach (G2).
4. **Any brand contact's range** for a spokes-character or campaign character (G10), asked in conversation only.
5. **Comparable product listings** (five, for section 3.6) and the **LINE Creators Market** terms (G5), with dated screenshots.

**How to record** (one row per quote; empty until real): `[TO FILL WHEN REAL]`

| Date | Source (name, how obtained) | Scope in words | Deliverable count | Revisions | Usage terms | Price (NT$) | Price per unit (NT$) | Notes |
|---|---|---|---|---|---|---|---|---|
| [TO FILL WHEN REAL] | | | | | | | | |

**Rules for using them** (all assumption; change them if the first quotes show a reason):

- **R1, floor rule.** Never sell below the floor. If the median comparable price per unit is below the floor per unit for an offer, do not sell it as specified: cut scope (units, rounds) until the floor fits, or drop the offer.
- **R2.** If the median lies between floor and ask, quote the median, not below the floor.
- **R3.** If the median is above the ask, keep the ask for the first three jobs (they are the portfolio), then revisit.
- **R4, implied hourly value.** From any one quote: implied operator value = (quoted price divided by (1 + margin), minus tool cost, minus wife time value) divided by operator hours. If that is below NT$300 an hour, the route does not pay for the operator's time at the Phase 1 axis minimum; say so in the next weekly review.
- **R5, how to update.** Put the real figure into `assumptions.csv`, set its status to `sourced`, write the date and source in the source column, run `python3 model.py docs --write` and `python3 -m unittest test_model`, and read the changed tables.
- **R6, measured minutes.** After the first sample and each job, replace the assumed minutes with the measured ones (portfolio hypothesis H8).

---

## 6. Quote sheet: what every written quote contains, and zh-TW draft lines

A written quote names: the registered seller `[TO FILL WHEN REAL]`; the package and the number of units; the deliverables and formats; two revision rounds; the usage licence (channel, territory, term, no model training); the disclosure and approval terms; what is excluded; the turnaround in weeks from complete assets; the price in NT$ and whether tax is included `[TO FILL WHEN REAL]`; payment terms `[TO FILL WHEN REAL]`; validity of 14 days; and a signature line. A contract template is a lawyer task (legal.md Q24). Claude does not sign or send anything.

**zh-TW draft lines for the wife (all AI drafts, to be read and rewritten in her own voice):**

| Use | zh-TW (DRAFT) | English gloss |
|---|---|---|
| Scope | 本報價內容為公開標示的 AI 生成圖像／示意圖創作。角色為 AI 生成的虛構角色，不是真人，也沒有實際使用、穿著或測試過任何商品。 | Openly labelled AI-generated images or illustrations. The character is a fictional AI character, not a person, and has not used, worn or tested any product |
| Exclusions | 本報價不含使用心得、見證或推薦語，也不保證任何觀看數、觸及、互動或銷售成效；不接受健康、醫療、減重、美容功效、投資或金融商品、賭博與政治相關內容。 | No testimonial or recommendation wording, no promise of views, reach, engagement or sales; no health, medical, weight-loss, cosmetic-efficacy, investment or financial-product, gambling or political content |
| Revisions | 含 2 輪修改；額外修改或範圍變更另行報價。 | Two rounds included; extra rounds or a change of scope are quoted separately |
| Approval | 所有圖像須經貴公司書面確認後才會使用；若發現資訊有誤，雙方應於 24 小時內更正或下架。 | Every image is used only after written approval; errors are corrected or taken down within 24 hours |
| Disclosure | 合作內容發布時須標示「業配」或「合作內容」、使用平台的付費合作標籤，並開啟 AI 生成內容標示；貴公司不得要求移除或縮小標示。 | Collaboration content is labelled, the platform's paid-partnership tag and AI label are used, and the client may not ask to remove or shrink a label |
| Usage | 授權為非獨家，限貴公司自有頻道，地區為臺灣，期間 12 個月；不得用於訓練 AI 模型。廣告投放（加強推廣）請另行報價。 | Non-exclusive, the client's own channels, Taiwan, 12 months, no AI model training; ad boosting is quoted separately (assumption) |
| Copyright | 本工作室不保證 AI 生成內容可受著作權法保護。 | The studio does not warrant that AI-generated content is protected by copyright (lawyer Q19) |
| Fees and tax | 報價以新臺幣計算；是否含稅及發票開立方式，待工作室完成登記後以書面約定。 | Prices in NT$; tax and invoicing agreed in writing after registration `[TO FILL WHEN REAL]` |
| Turnaround | 交期自收到完整素材與書面確認的範圍起算，以週為單位；貴公司確認所需時間另計。 | Weeks from complete assets and the confirmed scope; the client's approval time is extra |
| Validity | 本報價自提出日起 14 日內有效。 | Valid for 14 days (assumption) |

**For the wife to rule on:** whether 「業配」 or 「合作內容」 reads better to a B2B buyer; whether 貴公司 or 您 is the right address; whether 「加強推廣」 is the term Taiwan brands use for boosting; whether 「見證」 reads as a testimonial or as something else.

---

## 7. Open items

1. Collect the 3+ real quotes (section 5) and replace the assumed hourly values, margin and unit minutes (HUMAN_TODO 11).
2. Read and record the image tools' commercial-use terms (HUMAN_TODO 33). No client work before.
3. Registration, the registrant question and the 記帳士 answers: tax treatment, invoicing, which income may be received before registration (legal.md Q14 to Q17).
4. Lawyer: Q5, Q8, Q19, Q21, Q24 for paid work; Q18 and a spokes-character contract before any licensing conversation.
5. Read the LINE Creators Market terms and the affiliate programmes' terms (G3 to G5).
6. Decide whether the face-free B1 options (colour-story board, flat-lay lookbook) are tested before the lawyer answers on try-on.
7. Confirm the wife is comfortable with her hours being priced in the table (not paid in cash) and with the reading of 「見證」, 「業配」 and 「加強推廣」.

---

## 8. Review log (independent review, 2026-10-12)

Checked: ground rules and hard rules line by line; every Phase 1 citation (S1, S3 to S5, S7, S11, S13, S17, S19, S21 to S24, S27, S28, U1, U2, U5, G-numbers) against `research/monetisation.md`; HUMAN_TODO and `research/legal.md` question numbers; `portfolio.md` 1.4 disclosure strings and 5.x capacity figures; all asks, floors, product prices, sticker break-even, the middle-scenario B2B and sponsored revenue and the NT$59,000 placeholder total recomputed independently; `python3 -m unittest test_model` (103 pass) and `python3 model.py docs --check` (in sync). No invented client, follower, result, contact, URL or registration number found; named platforms and agencies are well known and carry the verify flag; Phase 1's unverified third agency is not named; forbidden categories and the no-testimonial rule are present in sections 2 and 3; no outcome is promised; the zh-TW lines are Traditional with Taiwan vocabulary (no mainland terms or Simplified forms found).

Fixed in place:
1. Hourly value wording (section 1 and `rate.op_hourly`): NT$600 was described as sitting on the Phase 1 axis; it is between axis points NT$500 and NT$800, and the axis priced native zh-TW review, not production. Now stated as a borrowed scale, not evidence.
2. `rate.cost_per_try`: the source note now carries pipeline/tools.md's own label, "one-source guess", so "sourced" is not read as a verified price.
3. `revenue-model.md` section 12: "at the very most" for the high scenario was an overclaim (the Phase 1 range runs to about NT$200,000); reworded, and B2B changed from "the only route that can matter" to "the route that matters most on these assumptions". Generated tables refreshed (`docs --write`); tests still pass.

Not fixed, for the humans: the author summary's counts (139 rows, 113 assumption) are stale, the files say 141 and 115 and are internally consistent; every number remains an internal ask until 3+ real quotes exist; the wife must rule on the section 6 strings (the platform's own Chinese name for the paid-partnership tag, 「付費合作」 versus the in-app wording, should be copied from a live Taiwan account screen).
