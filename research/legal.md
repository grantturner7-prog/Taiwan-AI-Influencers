# Legal research: advertising, AI, tax, IP and data rules for a studio of disclosed AI influencers in Taiwan

**RESEARCH, NOT LEGAL ADVICE.** Phase 1 deliverable `research/legal.md`. Written 2026-10-10. Nothing here is a legal, tax or accounting opinion. Every conclusion marked "my inference" is an unreviewed reading and must be checked by a Taiwan-qualified lawyer (律師) and a licensed bookkeeper or accountant (記帳士 / 會計師) before anyone acts on it. The question list at the end (section 12) is the hand-off.

Scope: a solo operator, 6 h/week, NT$5,000/month for tools, not good at Traditional Chinese, no registered Taiwan business yet (about 2 weeks to register), niches fitness, personal finance and fashion, refuses anything illegal [S17]. Ground rules from `BRIEF.md` apply: openly virtual, no invented experience, no health/medical/weight-loss/cosmetic-efficacy claims, no investment advice, no gambling, no politics [S17].

---

## 0. Read this first: what I could and could not verify

**I could not read a single primary legal source for this file.** The task asked for statute text and regulator pages (law.moj.gov.tw 全國法規資料庫, FTC, MODA, NCC, MOHW, FSC, TFDA). In this session:

- `WebSearch` refused every query: the run-wide budget of 200 calls was already spent.
- `WebFetch` failed with a DNS error on `law.moj.gov.tw`.
- One `curl` attempt through the sanctioned egress proxy to `law.moj.gov.tw` returned `403` on CONNECT. The proxy's own log also shows rejected CONNECTs earlier in the session (not by me) to `www.ftc.gov.tw`, `www.ncc.gov.tw`, `www.cna.com.tw`, `udn.com`, `www.bnext.com.tw` and platform help centres. The proxy documentation says a 403 is an organisation egress-policy denial that must be reported, not worked around. I stopped after that one attempt and did not look for another route or use a third-party reader or archive.

So **every claim below is one of three kinds**. Treat them differently.

| Tag | Meaning | How far to trust it |
|---|---|---|
| `[S#]` | Second-hand: facts gathered earlier today by sibling research files (`platforms.md`, `competitors.md`, `monetisation.md`) from search-result summaries of news, law-firm and regulator-reporting pages. I re-keyed them as S1 to S17 and did not re-open them | At most the confidence the sibling gave; see the Sources table |
| `[U#]` | Recalled from my own background knowledge. Not checked in this session, possibly stale for Taiwan 2026 | **Unverified.** Use only as a "go and check this" pointer. Nothing in the recommendations depends on a `[U#]` item being true |
| "not found" | The task asks for it and I have nothing | Fill from section 2 |

**Items the task told me to CONFIRM, and their status:**

| Task item | Status |
|---|---|
| Current Fair Trade Act fine range "from the statute text, with article numbers" | **NOT CONFIRMED.** A secondary source gives NT$50,000 to NT$25 million for false advertising [S1]. The article numbers (Art. 21 for the prohibition, Art. 42 for the fine) are from memory only [U1][U2]. I have not seen the statute text, so I cannot say whether the range is current |
| FTC 薦證廣告規範說明: disclosure duties, endorser liability | **PARTLY.** Existence, disclosure of material connections and endorser liability confirmed by secondary sources [S1]. Detailed content is recalled [U4] |
| AI Basic Act in force 14 Jan 2026; content; labelling duties | **NOT CONFIRMED.** Date comes from the brief [S17] and one unnamed search summary [S7]. Content is recalled with low confidence [U6]. I found nothing on labelling duties or implementing guidance |
| Fraud Crime Hazard Prevention Act: articles and duties | **PARTLY.** Platform AI-person disclosure duty and the Meta fine are reported with article numbers (Art. 31(1)(4), Art. 40(2)) [S5]; advertiser verification and 24-hour takedown by secondary sources [S4]. No statute text read |
| Sector rules, tax, registration, trademark, copyright, PDPA | **NOT VERIFIED.** All recalled [U8] to [U22]. Fees and timelines: not found |

---

## 1. Bottom line

1. **The one fine range I can report is secondary and unconfirmed.** Reporting on the Fair Trade Act says false or misleading advertising is fined NT$50,000 to NT$25 million, and that influencers who sell or endorse can be liable [S1]. I recall the prohibition in Art. 21 and the fine in Art. 42 [U1][U2], but I have not read either, so the range, the article numbers and any 2023 or later amendment are open. Verify before it goes in any document the operator relies on.
2. **A disclosed virtual character does not escape the endorsement rules, and Ground rule 4 is a legal control, not only a brand policy.** The FTC's definition of an endorsement is about another party's "opinion, belief, finding or experience" [S1]. A character that has never eaten, trained or worn anything cannot honestly report any of those. Any "I tried it" line is a false statement about a non-existent experience (my inference). The studio that runs the persona is the real party behind the words; the persona is not a separate liable person (my inference, section 3.2).
3. **The paid-relationship duty covers the studio's own money, not just brand fees.** Affiliate commissions, gifted goods and a studio stake in the product are material connections to disclose [S1][U4]. The Meta partnership label does not discharge Taiwan law [S13].
4. **Regulators are moving on AI in ads, not yet on virtual endorsers.** The FTC said on 2026-04-23 that AI-using ads are in its monitoring scope, illegal cases have been found, and mandatory AI disclosure is under evaluation [S2]. I found no FTC or NCC guidance specific to virtual influencers [S2][S3]. Expect the rules to tighten during the studio's first year.
5. **Paid ads that show a persona fall under the anti-fraud ad regime, and Taiwan already fines for it.** The Digital Industry Administration (數位產業署) fined Meta NT$5 million on 2026-08-14 for ads with undisclosed AI-generated personal images (Art. 31(1)(4), Art. 40(2)) [S5]. Platforms must verify advertisers and take down notified scam ads within 24 hours [S4]. Practical consequence (my inference): a boosted persona post needs the platform's AI-disclosure control set and a verified advertiser identity, which probably leans on the business registration.
6. **The AI Basic Act is probably a framework law with little direct private-sector bite, but I could not check.** The brief says it bars AI use for false advertising and that it has been in force since 2026-01-14 [S17]. Neither point is verified; the date may be the promulgation date rather than the effective date [U5][U6]. The enforceable false-advertising bar is the existing Fair Trade Act, not the new Act.
7. **Fitness and wealth carry licensing and criminal-law edges that ad-wording rules do not capture.** Fitness touches food, health-food, cosmetics, medical-device and medical-practice regimes [U8 to U11]. Wealth touches the securities-investment-advisory licence regime and bank, insurance and crypto rules [U12][U13]. The deepfake-investment-fraud climate in Taiwan makes an AI face talking about money start at a trust deficit [S11]. Fashion has the thinnest regulation but gets risky when it drifts into cosmetics claims, "slimming" garments, AI try-on imagery that misstates the real product, and real-brand marks [U10][U18].
8. **Business registration is a gating item with an unknown dependency: the operator's residency and nationality.** Entity type, foreign-investment approval, income-tax status, withholding on platform payouts and even the right to work in Taiwan all branch on that fact, which DECISIONS.md does not record. I have not assumed an answer (section 7.3).
9. **Purely AI-generated persona images may not be protected by copyright in Taiwan.** I recall the IP office's position that output without human creative input is not a work, but I have not verified it [U19] (the same unverified recall sits in `monetisation.md` as U2). If true, trademark, contract, human-authored layers and provenance records carry the protection, and the "license the character to a brand" route is weaker than it looks.
10. **Likeness risk is live in Taiwan.** In July 2026 a male model accused a Taiwan apparel brand of an AI image that copied his eyelids, tattoo and stance; the brand apologised and stopped using it. Commentary pointed to Civil Code Art. 18 portrait rights [S8]. Ground rule 2 and the provenance file are the right controls; a look-alike check should be added (section 8.3).

---

## 2. Verification pack: what a human should open first

Ordered by how much of this file depends on it. Each is a single open-and-screenshot job for `SOURCES.md`. Hosts are recalled domain names; check them. To close these gaps automatically in a later session, the session's egress policy would need to allow these hosts (or a person pastes the text).

| # | Open | Confirm |
|---|---|---|
| 1 | law.moj.gov.tw, 公平交易法 (Fair Trade Act), Art. 21 and the penalty article | Exact text; current fine range and the escalation for continued non-compliance; last amendment date; whether an ordinary-consumer endorser exception exists as I recall [U1][U2] |
| 2 | ftc.gov.tw, 公平會對於薦證廣告之規範說明 (latest version) | Effective date; disclosure wording, placement and timing rules; the "actual experience" requirement; whether a non-human endorser is addressed; affiliate and gifted-product treatment [U4] |
| 3 | law.moj.gov.tw, 人工智慧基本法; nstc.gov.tw (國科會) and moda.gov.tw announcements | Promulgation date versus effective date; competent authority; any private-sector duty, penalty or labelling clause; whether the "false advertising" bar the brief mentions exists; any guidance issued under it [U5][U6] |
| 4 | law.moj.gov.tw, 詐欺犯罪危害防制條例, the ad-platform chapter and penalties | Full text of Art. 31(1) (item 4 on AI-generated personal images), Art. 32 to 40; any duty on advertisers or creators; what counts as an "ad"; the designated-platform list from MODA [S4][S5] |
| 5 | fda.gov.tw (TFDA) and law.moj.gov.tw: 食品安全衛生管理法, 食品及相關產品標示宣傳廣告涉及不實誇張易生誤解或醫療效能認定準則, 健康食品管理法, 化粧品衛生安全管理法 and TFDA's published lists of allowed and disallowed cosmetic claims | Claim limits; fine ranges (not found); permitted wording lists [U8 to U10] |
| 6 | mohw.gov.tw: 醫療法 medical-advertising articles, 藥事法 drug-ad approval, 醫療器材管理法 | What a non-clinic may say about health; device classes for wearables and measuring devices [U11] |
| 7 | fsc.gov.tw and sfb.gov.tw (證期局): 證券投資信託及顧問法, FSC statements on 財經網紅 | Definition of investment advisory; unlicensed-advice penalties; what FSC has said about stock-tip influencers; 2026 status of virtual-asset rules [U12][U13] |
| 8 | mof.gov.tw and the National Taxation Bureau (國稅局) pages on 網紅 income, 所得稅法 Art. 14, 營業稅 small-scale thresholds, foreign-platform payouts | Income category by stream; threshold for 統一發票; withholding on resident and non-resident payees; overseas-income reporting [U14 to U16] |
| 9 | gcis.nat.gov.tw (商工登記) and moea.gov.tw: 商業登記法, 公司法, rules for foreign applicants | Fees and processing times (not found); entity options for a foreign national; approval steps [U17] |
| 10 | tipo.gov.tw (智慧財產局): trademark fee table, classification search, average examination time, AI-and-copyright guidance | Fees and timeline (not found); classes; TIPO position on AI works [U18][U19] |
| 11 | 個人資料保護法 on law.moj.gov.tw and the 2025-2026 amendment status | Notice, purpose, marketing opt-out, cross-border rules; whether a Personal Data Protection Commission now exists [U21] |
| 12 | 消費者保護法 and the 通訊交易解除權合理例外情事適用準則 | Advertising-truth article; 7-day return; digital-content exception [U22] |

---

## 3. Fair Trade Act (公平交易法) and endorsement advertising (薦證廣告)

### 3.1 What the evidence supports

| Point | Status | Source |
|---|---|---|
| The FTC (公平交易委員會, 公平會) treats sponsored posts as 薦證廣告 | Supported | [S1] |
| Material connections between endorser and advertiser must be disclosed | Supported | [S1] |
| Influencers who sell or endorse can be liable; 2023 handling principles bring them in | Supported (secondary) | [S1] |
| Fines for false advertising of NT$50,000 to NT$25 million | **Secondary only; not checked against the statute** | [S1] |
| The 規範說明 defines an endorsement as another party's statement of opinion, belief, finding or experience in an ad; the definition does not say "human" | Supported by sibling reading of the guidance; the "does not say human" point is an inference | [S1] |
| FTC said 2026-04-23: AI-using ads monitored; illegal cases found; mandatory AI disclosure under evaluation with other agencies | Supported (medium) | [S2] |
| FTC generative-AI competition statement 2026-03-18: AI can enable false marketing; FTC will not intervene prematurely in AI development | Supported (medium) | [S3] |
| No FTC or NCC guidance specific to virtual influencers or AI customers found | Search-limited negative | [S2][S3] |
| No Taiwan law specific to virtual personas | Academic source (2025), medium | [S15] |

### 3.2 Recalled statute content (unverified; confirm at item 1 and 2 of section 2)

- **Art. 21 prohibition [U1].** I recall it bars false or misleading representations about price, quantity, quality, content, use, origin and other attention-getting matters, in the product, the ad or any public communication. I recall three joint-liability rules (my recall is that the statutory wording is 連帶損害賠償責任, i.e. civil joint liability for damages with the advertiser, which is separate from the administrative fine; unverified), each limited to "knew or should have known": the advertiser's ad agency (廣告代理業), the ad medium (廣告媒體業), and the endorser (廣告薦證者). I recall an exception for an endorser who is only an ordinary consumer and not a well-known public figure, professional or institution. I recall the definition of endorser as a person or institution other than the advertiser who reflects in an ad their opinion, trust, discovery or **personal-experience result**.
- **Art. 42 fine [U2].** I recall that the FTC may order a stop and correction and impose a fine, with a higher fine tier if the violator does not comply. The NT$50,000 to NT$25 million range in [S1] matches my recollection of the base tier. The continuing-violation amounts are **not found**.
- **Civil remedies [U3].** I believe the Act also gives injunction and damages claims, including enhanced damages for intentional breach. Article numbers not recalled reliably.
- **FTC 規範說明 detail [U4].** My recollection of the guidance, low to medium confidence: endorsements must reflect the endorser's genuine opinion; a claimed experience must be one the endorser actually had; connections (payment, free goods, commission) must be disclosed clearly where a consumer will see them rather than buried; advertisers must be able to substantiate claims; the rules apply to social posts. The brief's cited headline from ETtoday (2017), 「網路業配文要先說清楚講明白嗎?」, points the same way, but I did not read it [S17].

### 3.3 How this applies to a virtual endorser (my inference, not an FTC statement)

| Question | Reading | Confidence in the reading |
|---|---|---|
| Is the persona itself an "endorser" (薦證者) with liability? | The definition speaks of a person or institution [U1]. A fictional character is neither. The studio operating it, and the advertiser, are the parties a regulator can reach. The studio is likely treated as the endorser, or as the advertiser if it earns affiliate income | Low. No guidance found [S2][S3]. Lawyer question 1 |
| Can the persona say "I tried it for a month"? | No. It is a false representation about a non-existent experience. This is the FTC's core concern with endorsements, and it is also a Fair Trade Act misrepresentation about the product's effect if the claimed result is attached to the product | Medium on the principle, low on the exact provision |
| Does "openly virtual" remove the need to disclose a paid relationship? | No. The duty is about the commercial connection, not about whether the speaker is human. The studio still gets paid or earns commission | Medium |
| Do "demonstrations" create risk? | Yes for physical products. An AI-generated picture of a garment, bag or gadget on a virtual body can misstate fit, colour, material or function. Taiwan example of AI imagery going visibly wrong: IKEA Taiwan's showroom image with distorted hands [S8] | Medium (inference from incidents, not law) |
| Is repeating a brand's claim safe if the brand supplied it? | Endorser and agency liability turns on "knew or should have known" [U1]. So the studio needs the brand's substantiation (test reports, permit numbers) for any functional claim and should keep it | Low to medium |
| Does the studio's B2B AI-ad-creative route add exposure? | Yes if the recalled ad-agency joint liability applies [U1]. The studio would need claim substantiation from the client in the contract | Low. Lawyer question 5 |

### 3.4 Working disclosure checklist (derived; for the native reviewer to refine)

| Situation | Minimum treatment |
|---|---|
| Paid post from a brand | Caption disclosure at the start in plain words (for example 業配 or 合作), plus the platform paid-partnership tool. Draft only; the native reviewer fixes the wording |
| Affiliate link or code | Same: say so in the caption near the link. Studio income counts as a connection [S1][U4] |
| Gifted product, no fee | Treat as a connection and disclose. Meta defines branded content as including "other value" such as gifts and free trips [S13] |
| Persona statement about a product | Attribute to specifications, a documented source or the studio's published comparison, never to the persona's experience |
| Bio | AI character plus studio name, as the brief requires |
| Boosted or branded-content ad | Also set the platform's AI-disclosure control [S5] |

---

## 4. AI Basic Act (人工智慧基本法)

| Item | Finding | Status |
|---|---|---|
| In force 14 Jan 2026 | The brief says so [S17]. One unnamed search summary said the Legislative Yuan passed it 2025-12-23 and it was promulgated 2026-01-14 [S7]. I did not open a primary page | **Unverified** |
| Promulgation versus effect | In Taiwan, a law that says it applies "from the date of promulgation" generally takes effect from the third day counting the promulgation day itself (roughly two days later; verifier's recall of 中央法規標準法 Art. 13, unverified) [U5]. So 2026-01-14 could be the promulgation date with effect days later, or the Act may set its own commencement date. Check the Act's final article | Recalled; verify |
| Nature | Framework law: principles, government duties, a central competent authority (I recall the National Science and Technology Council, 國科會, with MODA tasks such as a risk-classification framework) [U6]. One search summary attributed the authority inconsistently between NSTC and MODA [S7] | Low |
| Principles | I recall principles covering sustainability and well-being, human autonomy, privacy and data governance, security and safety, transparency and explainability, fairness and non-discrimination, and accountability [U6] | Low. Check the article text |
| Bar on "false advertising" (brief) | **Not verified.** I cannot say the Act contains this. If it exists it is probably a principle rather than an enforceable duty on private users | Unverified |
| Labelling or transparency duty for AI-generated content | Not found. I recall no direct private-sector labelling duty or penalty in the Act itself [U6]. Low confidence | Unverified |
| Implementing guidance | The brief cites "NCC guidelines under the AI Basic Act" (Taiwan News) and an IAPP piece on the governance framework; I did not open either and do not know what they contain [S7]. No NCC, MODA or FTC guidance for advertising or social content was found | Not found |
| Related regulator signals | FTC: AI ads monitored, mandatory AI disclosure under evaluation (2026-04-23) [S2]. NCC wrote to 民視 in 2023 over its AI news anchor; principle was disclose clearly, humans write and check scripts [S10] | Supported (medium) |

**Implication for the studio.** Do not rely on the AI Basic Act as either a shield or a source of duties until the text is read. The disclosed-persona design already meets the likeliest transparency expectations. If a labelling rule arrives it will probably come from the FTC, NCC or the Fraud Act regime rather than from this Act.

---

## 5. Fraud Crime Hazard Prevention Act (詐欺犯罪危害防制條例) and ad disclosure

### 5.1 What is reported

| Point | Finding | Source |
|---|---|---|
| Designated ad platforms | Google, YouTube, LINE, Facebook, Instagram, TikTok; Threads added later per secondary reports | [S4] |
| Platform duties | Verify who commissions and pays for ads; remove notified scam ads within 24 hours; publish transparency reports | [S4] |
| AI-person disclosure duty | Platforms must disclose ads that use AI-generated personal images (deepfake or AI faces). Cited as Art. 31(1)(4) | [S5] |
| Enforcement | Digital Industry Administration fined Meta NT$5 million on 2026-08-14 under Art. 40(2) for undisclosed AI-generated personal images in ads, plus NT$5 million for late takedown. Meta says it labels AI-made ads "AI info". A cumulative total of NT$28.5 million over six fines is single-source and low confidence | [S5] |
| Blocking power | The Interior Ministry used Art. 42 to order a one-year DNS block of Xiaohongshu from 2025-12-04 (1,706 cases, about NT$247.7 million losses) | [S6] |
| Context | Deepfake investment-fraud ads impersonating exchange officials ran in August 2026; fake-investment fraud has the largest loss share per police data cited (second-hand, low) | [S11] |

### 5.2 What falls on advertisers and creators (open)

The duty described in [S5] sits on the **platform**. I recall the wider chapter as platform-focused (advertiser verification, display of advertiser and payer, takedown, AI labelling, penalties) but no article beyond those in [S5] [U7]. What I could not establish:

- Whether the **advertiser** (the studio, or a brand paying to boost the persona) has its own statutory duty to declare AI-generated personal images, or only has to use the platform's control. Not found.
- What documents an advertiser must supply for identity verification [S4]. Individual versus registered business: not found. This is why paid promotion likely waits for the registration [S4][S17].
- Whether **organic** posts, or creator branded-content posts that the brand does not boost, count as "advertisements" for Art. 31. I recall the regime being aimed at paid platform ads, but this is unverified. Lawyer question 8.
- Whether platform-specific financial-product advertiser verification applies. Meta separately requires pre-authorisation for some partner categories including crypto, gambling, pharmacies and dating [S13]. Taiwan-specific financial-advertiser verification rules: not found.

**Default position on referral links (added by verifier to keep Ground rules 5, 6 and the no-financial-advice rule intact):** until a Taiwan lawyer answers questions 11 to 13, the studio places no affiliate, referral or "best pick" links for brokers, funds, credit cards, loans, insurance, crypto exchanges, supplements or health-measuring devices, and takes no paid placements in those categories.

**Working rule until verified:** set the platform AI-disclosure control on every paid or boosted post that shows a persona, keep the advertiser account verified in the registered studio's name, and log each boosted post in `assets/provenance.csv`.

---

## 6. Sector advertising rules

All article numbers and contents in this section are `[U]` recalled unless a source tag is shown. They name the regime so that the right page can be opened. No fine ranges are given because I could not check any.

### 6.1 Regime map

| Sector | Law and regulator | What it restricts (recalled) | Persona must avoid | Tag |
|---|---|---|---|---|
| General food and supplements | 食品安全衛生管理法 Art. 28 (labelling and ads must not be false, exaggerated or misleading, and must not claim medical efficacy); 食品及相關產品標示宣傳廣告涉及不實誇張易生誤解或醫療效能認定準則; MOHW and TFDA, local health bureaus enforce | Claims of treating, preventing or curing disease; exaggerated function claims | Weight-loss, fat-burn, "detox", "boosts metabolism" or disease-related outcomes for a food or supplement. Before/after body results | [U8] |
| Health food (健康食品) | 健康食品管理法 (Art. 14 on labelling and ads, recalled): only products with an approved permit may make the approved health claim, and not beyond it | Unapproved health claims; wording beyond the permit | Any health-effect claim unless the permit and claim are documented; repeating a brand's health claim without the permit number | [U9] |
| Cosmetics (化粧品) | 化粧品衛生安全管理法 (Art. 10, recalled); TFDA publishes lists of claim wording that is allowed and disallowed | False or exaggerated claims; any medical-efficacy claim | Medical-type wording (treat, repair, anti-inflammatory, hair-growth, fat-reduction) and results promises | [U10] |
| Medical services, drugs, devices | 醫療法 medical-advertising articles (Art. 84 to 87 recalled); 藥事法 drug-ad approval; 醫療器材管理法 (2021); MOHW | Who may advertise medical services; drug and device ads need approval; testimonials restricted | Anything that reads as medical advice, diagnosis, rehab or a device's medical function; promoting a drug or prescription-type product | [U11]; deepfake-doctor ads show the fraud overlap [S12] |
| Fitness and gym services | 消費者保護法 and standard-contract rules for fitness centres; FTC for ad claims; medical-practice laws if advice crosses into treatment | Misleading price, contract and result claims | Result guarantees (kilos lost, muscle gained, time frames). Rehab or injury-treatment advice. Gym membership claims you cannot substantiate | [U22]; the weight-loss service rule is a lawyer question |
| Securities and investment advice | 證券投資信託及顧問法 (definition Art. 4, licence Art. 16, unlicensed-business penalty Art. 107, recalled); FSC and its Securities and Futures Bureau | Providing analysis or recommendations on securities or related products for a fee needs a licence; verifier's recall is that unlicensed business carries criminal penalties (imprisonment) as well as fines, so treat this as the highest-severity line in the file (unverified) | Naming securities, ETFs or crypto with buy/sell/hold views; target prices; return promises; paid stock-tip groups; teaching "signals" for a fee | [U12] |
| Banking and lending | 銀行法 and FSC credit rules; agencies and "loan helper" ads are a fraud vector | Deposit-taking by non-banks; loan-ad rules | Referral or comparison content pushing a lender or credit card as the best choice without confirmed rules | [U13] |
| Insurance | 保險法 and agent/broker rules; FSC | Soliciting insurance needs a licence | Recommending specific policies | [U13] |
| Crypto and virtual assets | Money-laundering-control VASP registration; a virtual-asset act was in the pipeline; 2026 status not found. Meta needs pre-authorisation for crypto partners [S13] | Unregistered exchanges; promotions | Any crypto promotion, exchange referral or token mention | [U13]; [S13] |
| Fashion product description | 公平交易法 Art. 21 on product, origin and quality representations [U1]; 商品標示法 labelling rules; 商標法 for brand names | Misstated material, size, origin, "Made in Taiwan" claims; use of others' marks | AI try-on or product images that do not match the real item; implying a brand relationship that does not exist; counterfeit-looking items | [U1][U18]; 商品標示法 and the labelling regulator's role are recalled and unverified |
| Paid-ad categories needing platform pre-authorisation | Meta branded content: dating, gambling, pharmacies and prescription drugs, crypto | Platform rule, not Taiwan law | These categories are out for the persona anyway | [S13] |

### 6.2 Niche matrix: what each persona must avoid, and the angle that is probably compliant

Probably-compliant angles follow the DECISIONS.md flag (exercise technique, gear and routines with no health claim; money literacy with no financial advice). Whether they are acceptable is the operator's decision at STOP 1, and a lawyer's call on the line.

| Niche | Highest-risk content | Likely regulators | Probably-compliant angle | Residual risk to ask about |
|---|---|---|---|---|
| Fitness | Weight-loss or fat-loss outcomes; supplements and "burners"; recovery or pain advice; wearables with health readings | TFDA/MOHW; FTC; local health bureau | Technique explainers, equipment spec comparisons, routine templates, gym-etiquette culture, with no outcome promises | Where "fitness education" ends and 物理治療 or medical advice begins; affiliate links to supplements; the persona's own body image as proof of results (it has none to show) |
| Personal finance (wealth) | Named securities, ETFs, funds, crypto; return claims; "teach you to earn"; paid chat groups; credit card or loan referrals | FSC / SFB; MOF; FTC; Fraud Act regime for ads | Budgeting templates, vocabulary and concept explainers, how a financial term works, tax-calendar reminders | Whether comparing fees or product features counts as a recommendation; licence needs for affiliate referral; trust penalty from deepfake-fraud climate [S11] |
| Fashion | Cosmetics or skincare efficacy words; "slimming" garments; AI imagery that misstates the real product; brand-mark use; look-alike faces | FTC; TFDA (cosmetics); the standards-and-inspection bureau (BSMI) for product labelling (recalled, unverified); TIPO / courts for marks and likeness | Style systems, colour and fit guides based on published size charts, trend and calendar content, outfit-building | Virtual try-on accuracy; Life8-type likeness claims [S8]; beauty crossover |

Independent 2026 commentary also says AI personas work better in fashion, entertainment and gaming than in health, family, finance and wellness [S16] (low confidence). That lines up with the compliance load.

### 6.3 Screening list for the native reviewer (heuristic only; not an official list)

A reviewer cannot judge legality, but can flag review triggers. Whether each term is actually prohibited depends on the product category; check the TFDA and MOHW lists in section 2.

| Area | zh-TW review triggers |
|---|---|
| Fitness / food | 瘦身, 減肥, 減脂, 燃脂, 排毒, 促進代謝, 治療, 改善 plus a symptom or disease, 預防, 舒緩 plus pain, 保證, 見效, "N 週瘦 N 公斤", before/after body images |
| Finance | 保證獲利, 穩賺, 零風險, 翻倍, 明牌, 飆股, 目標價, 買進 / 賣出 as advice, 老師帶單, 入群, 跟單 |
| Cosmetics / beauty | 抗老, 除皺, 消炎, 修復, 再生, 淡斑, 生髮, 抗敏, any claim about skin function or body-fat change |
| Any | 親身體驗 or 我用過 from a persona; 真實見證; fake customer quotes; unsourced numbers; Simplified or mainland vocabulary |

---

## 7. Business registration and tax on creator income

Everything here is `[U]` recalled or "not found". Fees and processing times were not retrievable. The operator's own estimate for registration is about two weeks [S17].

### 7.1 Entity options (recalled)

| Option | zh-TW | Registrar | Invoicing | Tax shape (recalled) | Fit | Tag |
|---|---|---|---|---|---|---|
| Unregistered individual | 未登記 | none | Payer may issue a withholding slip (勞報單) instead of an invoice. Whether brands accept it: unverified | Income reported by the individual under a category in 7.2 | Possible for platform payouts and small affiliate income; weak for brand deals | [U14] |
| Sole proprietorship | 商號 (獨資) | Local government under 商業登記法 | Can register for business tax and issue 統一發票 | Owner is taxed on profit as 營利所得 on the personal return (recalled); small-scale business-tax regime may apply (7.2) | Light, cheap, fast; unlimited personal liability | [U17] |
| Limited company | 有限公司 (single-member allowed) | MOEA / local authority under 公司法 | 統一發票 | Company-level income tax and business tax; no statutory minimum capital recalled | Stronger for brand contracts, trademark ownership and liability shield; heavier bookkeeping | [U17] |

Fees: not found. Timeline: about 2 weeks per the operator [S17]; official processing time: not found. Foreign-investment approval (for a non-Taiwan-national operator) could add time and conditions: not found.

### 7.2 Income categories and invoicing questions

The ten income-tax categories (所得稅法 Art. 14, recalled with good confidence) are: 營利所得, 執行業務所得, 薪資所得, 利息所得, 租賃及權利金所得, 自力耕作漁牧林礦所得, 財產交易所得, 競技競賽及機會中獎獎金, 退職所得, and 其他所得 [U14]. Which one fits each stream is **not found**; the tax authority's published position on 網紅 income was not retrieved.

| Stream | Category and invoicing question | Status |
|---|---|---|
| 業配 from a Taiwan brand | Depends on whether the studio is registered; a brand's finance team will usually want an invoice or a withholding slip | Not found. Lawyer/記帳士 question 15 |
| Affiliate commission | Commission network pays a studio or an individual; withholding and invoice rules vary | Not found |
| YouTube, Meta, TikTok payouts | Foreign payer. Reporting as overseas income; US tax forms and any US-source withholding; the Taiwan side of business tax on cross-border services | Not found. Question 16 |
| LINE sticker royalties | Royalty (權利金) type income; payer is LINE | Not found. Creators Market terms do not ban AI stickers and LINE may label them [S14] |
| B2B AI ad creative | Service fee; invoice from the registered studio | Not found. Needs registration [S17] |
| Own digital products | Business sales; consumer-protection rules apply (section 9) | Not found |

Other items recalled and not verified [U15][U16]:
- Tax residency: roughly a 183-day test in a calendar year for someone without a Taiwan domicile. Non-residents are withheld at a higher flat rate than residents on Taiwan-source income. Rates: not found.
- A national health-insurance supplementary premium (二代健保補充保費) applies to some payments above a per-payment threshold. Rate and threshold: not found.
- Business tax (營業稅): a standard rate (recalled 5%) and a lower small-scale rate (recalled 1%) for 小規模營業人, with monthly-sales thresholds. **Recalled numbers, unverified; do not put them in the revenue model until checked.**
- Overseas-income threshold for the alternative minimum tax: not found.

### 7.3 Residency and nationality: the dependency to resolve first

DECISIONS.md does not say whether the operator is a Taiwan resident, a foreign national in Taiwan or abroad. Each branch changes the answer, and I have not assumed one.

| If the operator is | What changes (all unverified) |
|---|---|
| Taiwan national or resident with full work rights | Ordinary 商號 or 有限公司 registration; resident tax treatment; platform payouts are overseas income to report |
| Foreign national living in Taiwan | Residence and work authorisation, and possibly foreign-investment approval, before registering or providing paid services; tax residency by days present |
| Abroad | Whether a Taiwan entity can be set up at all and by whom; non-resident withholding on Taiwan-source income; a local address and bank account; Taiwan-US tax relief position for US-platform income is not verified |

**Action:** add "operator's nationality, visa/residence status and tax residence" to `HUMAN_TODO.md` before the 記帳士 meeting, because it determines what to ask.

---

## 8. Intellectual property

### 8.1 Trademark (商標) for names, logos and character art

| Point | Finding | Tag |
|---|---|---|
| System | Taiwan registers marks at TIPO (經濟部智慧財產局). Priority goes to the first to file (recalled) | [U18] |
| Term | 10 years from registration, renewable (recalled) | [U18] |
| Classes | Goods and services classes follow the Nice scheme. Candidate classes by my reading, to be confirmed at TIPO's classification search: 41 (entertainment, online video and content), 35 (advertising and influencer-marketing services), 9 (downloadable images, audio-visual files, digital stickers), 16 (printed matter), 25 (clothing, if merchandise is planned) | Low |
| Refusal grounds | Include marks conflicting with another's portrait, name or stage name without consent (Art. 30(1), recalled; subparagraph not recalled) | [U18] |
| Foreign applicants | A foreign applicant without a Taiwan domicile or business address may need a local trademark agent (recalled; verifier's recall is that appointing an agent is mandatory in that case, 商標法 Art. 6, unverified) | [U18] |
| Fees and timeline | **Not found** | n/a |

Practical points: registrable character names must be distinctive rather than descriptive; check the TIPO search for conflicts before any persona is named publicly (Phase 3); decide whether the applicant is the operator or the future company, because an assignment later costs time and money. Handle squatting on social platforms is a platform issue, but a registered mark helps in a dispute.

### 8.2 Copyright (著作權法) and AI-generated images

| Point | Finding | Tag |
|---|---|---|
| Authorship | Copyright subsists in a work of human authorship; the author is a natural person (recalled) | [U19] |
| TIPO position | I recall TIPO's view (since about 2018, restated more recently) that output generated autonomously by AI with no human creative input is not a protected work, while human-directed output can be protected for the human's creative contribution | [U19] low-medium; `monetisation.md` U2 is the same unverified recall |
| Consequence if right | A purely AI-generated persona face or sticker set may be copied without a copyright claim. Protection must come from trademark, contract, unfair-competition law, platform ownership rules and any human-authored layer (hand-drawn character sheet, retouching, composition, written scripts and brand voice) | Inference |
| Evidence trail | Keep prompts, iterations, selections and edits in `assets/provenance.csv` to document the human contribution and origin, as the brief already requires [S17] | Inference |
| Client IP assignments | If the studio sells AI-generated ad creative, an "assignment of copyright" may transfer little; contract wording should avoid warranting what the studio may not own | Inference; question 18 |
| LINE Creators Market | The terms do not ban AI stickers and LINE may display an AI label (clause 8.13 per sibling) | [S14] |
| Tool licences | Commercial-use rights, ownership of outputs, indemnity, limits on realistic people and voices, voice-cloning consent: **I read no provider terms**. Compare in `pipeline/tools.md` and have the lawyer check what the studio can warrant to brands | Not found |

### 8.3 Likeness and personality rights (人格權), and rules against resembling real people

| Point | Finding | Source |
|---|---|---|
| Civil Code Art. 18 protects personality rights; commentary on the July 2026 Life8 dispute cited portrait right (肖像權) under it | Medium | [S8]; [U20] |
| Taiwan has no law specific to virtual personas | Medium (academic) | [S15] |
| What the Life8 case shows | A brand first said its AI image was not based on anyone, then discussed a licence, then apologised and withdrew it. A claimed resemblance, not proven copying, triggered the dispute | [S8] |
| Lookalike threshold | Whether a resemblance claim needs actual copying or only likeness: not found | Question 20 |
| Related claims | Images of real people are personal data (PDPA); damages for non-pecuniary harm under Civil Code Art. 195 (recalled); deceptive trading under the Fair Trade Act | [U20][U21] |
| Real-person voice | A cloned or close-sounding voice raises the same personality-right questions. Not researched | Not found |

Controls to add beyond the brief: a reverse-image and look-alike check on each face before launch, a written "design brief with no reference to any real person" in the bible, and a takedown-response procedure (Phase 9 crisis playbook).

---

## 9. Personal data, DM/chatbot automation and consumer protection

| Topic | What applies (recalled; verify) | Tag |
|---|---|---|
| Personal Data Protection Act (個人資料保護法) | Names, handles, LINE IDs and message contents that identify a person are personal data. The studio is a non-government collector. Duties I recall: notice at collection (Art. 8), purpose limitation (Art. 19 and 20), security measures (Art. 27), data-subject rights, and a marketing opt-out (Art. 20) | [U21] |
| Marketing messages | The PDPA marketing opt-out applies; I recall no general anti-spam statute, so LINE OA broadcasts rely on PDPA plus platform terms. Unverified | [U21] |
| Cross-border transfer | Sending DMs to foreign LLM providers is a cross-border transfer of personal data. Restrictions are limited and conditional (recalled); a privacy notice that names the processing is advisable | [U21] |
| PDPA reform | A Personal Data Protection Commission and amendments were in progress; 2026 status not found | Not found |
| Automated replies | Ground rule 9 requires every automated reply or DM to say it is automated [S17]. The legal basis: not found. It is also consistent with the transparency expectation in AI policy | Inference |
| Minors | Personas are written as 25+, but audiences on TikTok and Instagram include under-18s; 72.5% of 16-25s have watched TikTok content [S17]. Rules on collecting minors' data and on content for minors: not researched | Not found |
| Consumer Protection Act (消費者保護法) | Advertising must be truthful and the ad content can bind the advertiser (Art. 22 recalled). If the studio sells digital goods, the distance-selling rules (7-day right to return, with an exception for digital content once supplied) and business-identity disclosure would apply | [U22] |
| Giveaways, lotteries (抽獎) and group buys (團購) | Fair Trade Act promotion rules and prize-income tax may apply. Not researched; avoid until a lawyer or 記帳士 reviews | Not found |
| Consumer-group pressure | Taiwan consumer groups called for mandatory AI labels after the TVBS/Guardian "fake customers" story | [S9] |

---

## 10. Where this research complicates the brief or the operator's niches

1. **The brief's AI Basic Act bullet is unverified in two ways.** The "bar on AI use for false advertising" is not confirmed, and "in force 14 January 2026" may be the promulgation date [S17][S7][U5]. Do not cite either to a brand or a platform until the Act is read.
2. **The brief says "confirm the current fine range." I could not.** The only figure available is secondary (NT$50,000 to NT$25 million) and the article numbers are recalled. Anyone who needs the figure must open the statute (section 2, item 1).
3. **Ground rule 4 is stronger than the brief presents it.** It is the main legal safeguard under the endorsement rules, not just brand hygiene. It also needs extending to AI product imagery that adds invented detail.
4. **Ground rule 5 should be widened.** The studio's own affiliate income and gifted goods count as connections. A platform partnership tool alone is not compliance [S13][S1].
5. **The fitness and wealth niches are riskier than "avoid claims" implies.** Wealth sits next to a licensing regime and a high-fraud, high-distrust environment [U12][S11]. Fitness sits next to food, device and medical-practice rules [U8 to U11]. The compliant sub-angles in DECISIONS.md are plausible but their boundary is a lawyer's decision, not the native reviewer's. Fashion is the cleanest niche but beauty crossover is its weak point.
6. **Registration is needed for more than invoicing.** Paid promotion needs a verified advertiser [S4], B2B, 業配 and licensing need invoices, and trademark ownership is cleaner under the final entity [U17][U18].
7. **The operator's residency and nationality are unknown and gate registration, tax and work rights.** Resolve before the 記帳士 meeting (section 7.3).
8. **The "license the character to a brand" route in `monetisation.md` is weaker if AI-generated art has no copyright.** Trademark and contract carry the weight; trademark fees and timeline are not found [U19][U18].
9. **Budget.** A lawyer consultation and trademark filing are not priced anywhere in the files, and NT$5,000 a month does not obviously cover them plus a native reviewer. Add a one-time legal line to `COSTS.md` once a quote exists.
10. **Capacity.** At 6 h/week the studio cannot also track regulatory change. Assign a quarterly check of the FTC AI-disclosure evaluation [S2] and the Fraud Act designations [S4] to the weekly routine.

---

## 11. Open questions and unverifiable items

| Item | Why open | Where to resolve |
|---|---|---|
| Statute text of Fair Trade Act Art. 21 and the penalty article; current fine range; 2023 amendment effect | Primary source unreachable | Section 2 item 1 |
| FTC 規範說明 current text, effective date, treatment of non-human endorsers | Unreachable | Section 2 item 2 |
| AI Basic Act date, effective date, authority, content, labelling duty, guidance | Unreachable; sources conflict on authority | Section 2 item 3 |
| Fraud Act: full Art. 31 to 40 text, advertiser duties, organic-post scope, platform list as of 2026 | Statute not read | Section 2 item 4 |
| Sector fine ranges and permitted-claim lists (food, health food, cosmetics, medical, finance) | Not retrieved | Section 2 items 5 to 7 |
| Registration fees and timelines; tax category per stream; withholding rates; 統一發票 thresholds; small-scale business-tax figures | Not retrieved | Section 2 items 8 and 9 |
| Operator residency, nationality and work rights | Not recorded in DECISIONS.md | Operator |
| TIPO fees, classes, examination time; TIPO's current AI-copyright position | Not retrieved | Section 2 item 10 |
| Tool-provider commercial-use terms | Not read | `pipeline/tools.md` |
| PDPA reform status; cross-border transfer limits | Not retrieved | Section 2 item 11 |
| Whether the FTC will mandate AI disclosure and when | Evaluation announced 2026-04-23 [S2] | FTC site, quarterly |
| Statistic reliability for fraud figures (41.09% share; 107,000+ ads removed) | Second-hand [S11] | Police and regulator releases |

---

## 12. Questions for a Taiwanese lawyer

Tagged by when the answer is needed: **[Gate: launch]** before the first public post, **[Gate: paid]** before the first brand deal or boosted ad, **[Later]** within the first year.

1. **[Gate: launch]** Under the Fair Trade Act and the FTC 薦證廣告規範說明, is a disclosed virtual character a 廣告薦證者, or is the operating studio (and the advertiser) the only liable party? Does the answer change when the studio earns affiliate commission on sales?
2. **[Gate: launch]** Is any statement of experience or personal use by an openly-virtual persona a false or misleading representation per se? What wording lets the persona "present, compare and demonstrate" a product without falling inside the endorsement definition?
3. **[Gate: launch]** Please confirm the current Fair Trade Act text for false advertising (Art. 21 and the penalty article), the present fine range, the escalation for continuing violations, whether fines can reach a sole proprietor or a one-person company, and any criminal exposure after an FTC order.
4. **[Gate: launch]** What disclosure wording, placement and timing does the FTC accept today for short video, Stories, Threads and LINE OA messages? Is the platform's paid-partnership tool alone enough? Must gifted products with no fee, and the studio's own affiliate links, be disclosed?
5. **[Gate: paid]** If the studio sells AI-generated ad creative to brands, does it carry advertising-agency joint liability (knew or should have known)? What claim-substantiation warranties, approvals and indemnities should the contract contain?
6. **[Gate: launch]** What is the AI Basic Act's actual effective date (promulgation versus effect), which regulator issues rules for advertising and social content, and does the Act or any guidance impose a transparency, labelling or false-advertising duty on private operators of AI personas?
7. **[Later]** What is the status of the FTC's evaluation of mandatory AI-ad disclosure announced 2026-04-23, and should the studio adopt a stricter voluntary disclosure standard now?
8. **[Gate: paid]** Which studio activities count as "advertisements" under the Fraud Crime Hazard Prevention Act's AI-generated-personal-image rule (Art. 31(1)(4)): boosted posts, brand-boosted creator posts, organic posts with affiliate links? Does the advertiser, not just the platform, bear any duty or penalty if the label is missing?
9. **[Gate: paid]** What identity documents are required for advertiser verification as an individual versus a registered business, and can a non-resident or foreign-national operator qualify?
10. **[Gate: launch]** For a fitness persona, where is the line between exercise education and 醫療 or 物理治療 advice, and between permitted fitness-outcome language and prohibited weight-loss claims? Can you give an approved and a prohibited phrase list in zh-TW?
11. **[Gate: paid]** If the persona links to supplements, protein products or wearables, who is liable under the food, health-food and medical-device rules when the brand's claim is false but the studio repeats it?
12. **[Gate: launch]** For a personal-finance persona, where does financial education end and 證券投資顧問 activity under 證券投資信託及顧問法 begin? Does comparing broker, ETF-wrapper or credit-card fees, or naming products at all, cross the line? Does paid sponsorship or an affiliate commission change the answer?
13. **[Gate: paid]** Do affiliate or referral links to brokers, credit cards, loans, insurance and crypto exchanges require a licence or special FSC-related disclosure, and what is the current virtual-asset regulatory position?
14. **[Gate: launch]** Given the operator's residency and nationality (to be supplied), which of 商號, single-member 有限公司 or an unregistered status is lawful and sensible for a year-one studio? What approvals, fees and timeline apply, and what happens if the operator needs a work permit or foreign-investment approval?
15. **[Gate: paid]** How should 業配, affiliate commission, platform payouts, LINE sticker royalties, B2B creative fees and digital-product sales each be classified for income tax, and when is a 統一發票 required? What are the small-scale business-tax thresholds?
16. **[Gate: paid]** How are YouTube, Meta and TikTok payouts treated for Taiwan tax, including overseas-income reporting, any alternative-minimum-tax threshold, 二代健保 premium, and US tax-form and withholding questions? What changes if the operator is a non-resident?
17. **[Gate: paid]** During the roughly 2-week registration gap, may the operator receive any income (for example a first 業配 fee), and how should it be documented (勞報單 or otherwise) without penalty?
18. **[Later]** Which trademark classes and applicant (operator personally or the future company) should be used for the studio name, each character name in Chinese and romanised form, and a logo? Can a character's face be protected as a figurative mark? What are the fees, examination time and refusal risks (including names resembling real persons)?
19. **[Gate: paid]** Given TIPO's position (to be confirmed) that purely AI-generated output lacks copyright, how should the studio structure human authorship, assignments with freelancers and reviewers, and brand contracts so it does not warrant ownership it may not have?
20. **[Gate: launch]** What due diligence reduces 肖像權, 姓名權 and 人格權 risk for AI faces and voices? Does a look-alike claim need actual copying or only resemblance? What is the response procedure if a person complains, as in the Life8 case?
21. **[Gate: paid]** What can the studio safely warrant to brands about outputs from foreign generative tools (commercial-use licence, training-data claims, indemnity), and are there Taiwan-specific issues with realistic AI voices?
22. **[Gate: launch]** For DM and LINE OA chatbots running on foreign LLM APIs, what notice, consent, retention and cross-border-transfer steps does the 個人資料保護法 require? How should the marketing opt-out, minors' data and data-subject requests be handled, and is a privacy policy mandatory?
23. **[Later]** If the studio sells digital goods or merchandise, or runs 抽獎 or 團購, which consumer-protection, promotion and prize-tax rules apply, and what business information must be shown?
24. **[Gate: paid]** Please review a standard sponsorship contract for: claim warranties, approval rights, takedown duties, AI-use disclosure clause, IP and likeness clause, exclusivity, and liability caps.
25. **[Later]** What regulatory changes in the next 12 months (FTC AI-disclosure, AI Basic Act rules, Fraud Act amendments, PDPA reform, virtual-asset law) should the studio monitor, and what is the cheapest way to be told about them?

---

## Sources

Dates accessed are 2026-10-10 for every row. **S rows were gathered by sibling files from search-result summaries; I did not open them, and their confidence is at most what the sibling gave.** U rows were recalled and **not opened**; the URL column says where to verify, and confidence is "unverified".

| id | claim supported | URL | date published (if known) | date accessed | confidence |
|---|---|---|---|---|---|
| S1 | FTC treats sponsored posts as 薦證廣告; material connections must be disclosed; endorsement defined as another party's statement of opinion, belief, finding or experience in an ad (sibling reading of the Lee and Li page); influencers who sell or endorse can be liable; false-advertising fines NT$50,000 to NT$25 million (range not checked against statute) | https://www.leeandli.com/TW/Newsletters/2501.htm ; https://www.inside.com.tw/article/30951-Taiwan-amendment-passed-KOL-main-advertisements-are-false-the-maximum-penalty-is-25-million | 2025-01 (Lee and Li); inside.com.tw date unconfirmed (the author's "2023-02" is not verified and the page may predate the 2023 amendment, so the fine range may reflect an older amendment) | 2026-10-10 | low to medium (secondary; not re-opened by author or verifier) |
| S2 | FTC acting chair, 2026-04-23: AI-using ads in monitoring scope; illegal cases found; mandatory AI disclosure under evaluation with other agencies; no virtual-endorser guidance found | https://technews.tw/2026/04/23/ftc-to-assess-mandatory-disclosure-rules-for-ai-ads/ | 2026-04-23 | 2026-10-10 | medium |
| S3 | FTC generative-AI competition policy statement; AI can enable false marketing; FTC will not intervene prematurely | https://finance.technews.tw/2026/03/18/ftc-will-not-intervene-prematurely-in-the-development-of-generative-ai/ ; https://www.cna.com.tw/news/afe/202603180299.aspx | 2026-03-18 | 2026-10-10 | medium |
| S4 | Fraud Crime Hazard Prevention Act: ad platforms designated (Google, YouTube, LINE, Facebook, Instagram, TikTok; Threads later); advertiser identity verification; 24-hour takedown; transparency reports | https://technews.tw/2024/11/13/platform-advertising-real-name-system/ ; https://www.thenewslens.com/article/245675 ; https://finance.ettoday.net/news/2854187 | 2024-11 | 2026-10-10 | medium |
| S5 | Digital Industry Administration fined Meta NT$5 million on 2026-08-14 for undisclosed AI-generated personal images in ads (Art. 31(1)(4), Art. 40(2)), plus NT$5 million for late takedown; Meta says it labels AI-made ads "AI info"; NT$28.5 million cumulative is single-source | https://www.cna.com.tw/news/afe/202609230333.aspx ; https://ec.ltn.com.tw/article/breakingnews/5583322 ; https://www.blocktempo.com/meta-fined-twice-taiwan-scam-ads-ai-disclosure-lawmaker-amendment/ | 2026-09-23 (report) | 2026-10-10 | medium (fine; not re-opened by author or verifier; the fine date 2026-08-14 precedes the report date 2026-09-23 by five weeks, so confirm which date is the decision date); low (cumulative total) |
| S6 | Interior Ministry ordered one-year DNS block of Xiaohongshu from 2025-12-04 under Fraud Act Art. 42 (1,706 cases, about NT$247.7 million losses) | https://cna.com.tw/news/asoc/202512040238.aspx ; https://www.nownews.com/news/6761458 ; https://verfassungsblog.de/taiwans-xiaohongshu-ban-and-freedom-of-expression/ | 2025-12-04 | 2026-10-10 | medium (downgraded from high; not re-opened by author or verifier) |
| S7 | AI Basic Act: unnamed search summary said Legislative Yuan passed 2025-12-23, promulgated 2026-01-14; authority attributed inconsistently (NSTC vs MODA). Brief cites Taiwan News on NCC guidelines and IAPP on the governance framework (not opened) | https://www.taiwannews.com.tw/en/news/6380429 ; https://iapp.org/news/a/taiwan-s-ai-governance-framework-unveiled | not known | 2026-10-10 | unverified |
| S8 | Life8 AI model likeness dispute (July 2026); brand apologised and withdrew the image; Civil Code Art. 18 portrait-right commentary. IKEA Taiwan AI image with distorted hands (2026-06-01) | https://oecd.ai/en/incidents/2026-07-18-2fa7 ; https://today.line.me/tw/v3/article/3NPozZP ; https://unwire.hk/2026/06/01/ikea-taiwan-ai-image-zombie-hand-controversy/ai/ | about 2026-07-17/18; 2026-06-01 | 2026-10-10 | medium |
| S9 | TVBS report on Guardian investigation of brands using AI influencers as fake customers; consumer groups called for mandatory AI labels | https://news.tvbs.com.tw/news/searchresult/虛擬網紅/news ; https://techstrong.ai/articles/brands-secretly-deploy-ai-influencers-to-mimic-authentic-reviews-report/ | 2026-06-21 (Guardian); 2026-06-23 (TVBS) | 2026-10-10 | medium |
| S10 | NCC wrote to 民視 over its AI news anchor (2023); principle: disclose clearly, humans write and check scripts | https://technews.tw/?p=1086575 ; https://news.pts.org.tw/article/648630 | 2023-06 | 2026-10-10 | medium |
| S11 | Deepfake investment fraud impersonating exchange officials (August 2026); fraud statistics (41.09% share; 107,000+ ads removed) | https://uanalyze.com.tw/articles/5438653390 ; https://www.cna.com.tw/news/afe/202608050308.aspx ; https://money.udn.com/money/story/5607/9690165 | 2026-08 | 2026-10-10 | medium (events); low (statistics) |
| S12 | AI deepfakes of doctors in medical ads | https://oecd.ai/en/incidents/2026-06-15-3c15 | 2026-06-15 (record date) | 2026-10-10 | medium |
| S13 | Meta branded-content rules: tagging with permission; gifts and "other value" count; pre-authorisation for dating, gambling, pharmacies/prescription drugs, crypto; the tool does not discharge Taiwan law | https://help.instagram.com/1695974997209192 ; https://help.instagram.com/1372533836927082 ; https://help.instagram.com/1123581461537025 ; https://creators.instagram.com/earn-money/branded-content | not known | 2026-10-10 | medium |
| S14 | LINE Creators Market terms do not ban AI stickers; LINE may display an AI label (clause 8.13) | https://creator.line.me/en/terms/ ; https://creator.line.me/en/review_guideline/ | not known | 2026-10-10 | medium |
| S15 | Taiwan has no law specific to virtual personas (academic source) | https://www.airitilibrary.com/Article/Detail/U0020-1101202518053100 | 2025 | 2026-10-10 | medium |
| S16 | Independent commentary: AI influencers succeed in entertainment, fashion, gaming; health, finance, wellness are liabilities; "viral but can't close the sale" | https://finance.technews.tw/2026/03/30/ai-creators-can-go-viral-they-just-cant-close-the-sale/ | 2026-03-30 | 2026-10-10 | low (page not read) |
| S17 | Operator constraints and starting facts: NT$5,000 budget, 6 h/week, not fluent in Traditional Chinese, no registered business (about 2 weeks), niches, ground rules; brief states AI Basic Act in force 2026-01-14 and Fraud Act AI-image disclosure | /home/user/Taiwan-AI-Influencers/BRIEF.md ; /home/user/Taiwan-AI-Influencers/DECISIONS.md | 2026-10-10 | 2026-10-10 | operator-provided; brief facts unverified by me |
| U1 | Fair Trade Act Art. 21: false or misleading representations; joint liability for ad agency, ad medium and endorser when they knew or should have known; ordinary-consumer exception; definition of endorser includes "personal experience result" (recalled) | https://law.moj.gov.tw (search 公平交易法) | n/k | 2026-10-10 | unverified |
| U2 | Fair Trade Act penalty article (recalled as Art. 42): stop order, fine, higher tier for continued non-compliance; base range consistent with S1 | https://law.moj.gov.tw (search 公平交易法) | n/k | 2026-10-10 | unverified |
| U3 | Fair Trade Act civil remedies: injunction, damages, enhanced damages for intentional breach (recalled) | https://law.moj.gov.tw (search 公平交易法) | n/k | 2026-10-10 | unverified |
| U4 | FTC 薦證廣告規範說明 detail: genuine opinion, actual experience, conspicuous disclosure, substantiation (recalled) | https://www.ftc.gov.tw (search 薦證廣告) | n/k | 2026-10-10 | unverified |
| U5 | Central Regulations Standards Act (中央法規標準法, Art. 13 recalled): a law applying "from promulgation" takes effect from the third day counting the promulgation day (recalled; author's "third day after" wording corrected by verifier, still unverified) | https://law.moj.gov.tw (search 中央法規標準法) | n/k | 2026-10-10 | unverified |
| U6 | AI Basic Act content: framework; principles list; NSTC authority; MODA risk framework; no direct private-sector penalty (recalled, low confidence) | https://law.moj.gov.tw (search 人工智慧基本法) | n/k | 2026-10-10 | unverified |
| U7 | Fraud Act article details beyond those in S5 (recalled structure only) | https://law.moj.gov.tw (search 詐欺犯罪危害防制條例) | n/k | 2026-10-10 | unverified |
| U8 | Food Safety and Sanitation Act Art. 28 and the 認定準則 on false, exaggerated, misleading or medical-efficacy claims (recalled) | https://law.moj.gov.tw (search 食品安全衛生管理法) ; https://www.fda.gov.tw | n/k | 2026-10-10 | unverified |
| U9 | Health Food Control Act: permit required for health claims; Art. 14 on ads (recalled) | https://law.moj.gov.tw (search 健康食品管理法) | n/k | 2026-10-10 | unverified |
| U10 | Cosmetics Hygiene and Safety Act Art. 10 on labelling and ads; TFDA lists of allowed and disallowed claim wording (recalled) | https://law.moj.gov.tw (search 化粧品衛生安全管理法) ; https://www.fda.gov.tw | n/k | 2026-10-10 | unverified |
| U11 | Medical Care Act ad provisions (Art. 84 to 87 recalled); Pharmaceutical Affairs Act drug-ad approval; Medical Devices Act (2021) | https://law.moj.gov.tw (search 醫療法, 藥事法, 醫療器材管理法) ; https://www.mohw.gov.tw | n/k | 2026-10-10 | unverified |
| U12 | Securities Investment Trust and Consulting Act: advisory definition, licence, unlicensed-business penalty (Art. 4, 16, 107 recalled); FSC warnings to 財經網紅 | https://law.moj.gov.tw (search 證券投資信託及顧問法) ; https://www.fsc.gov.tw ; https://www.sfb.gov.tw | n/k | 2026-10-10 | unverified |
| U13 | Banking Act, Insurance Act intermediary licensing, VASP registration and virtual-asset legislation (recalled; 2026 status not found) | https://law.moj.gov.tw ; https://www.fsc.gov.tw | n/k | 2026-10-10 | unverified |
| U14 | Income Tax Act Art. 14: ten income categories (recalled with good confidence) | https://law.moj.gov.tw (search 所得稅法) | n/k | 2026-10-10 | unverified |
| U15 | Tax residency 183-day test; higher flat withholding for non-residents; supplementary health-insurance premium (recalled; rates not found) | https://law.moj.gov.tw (search 所得稅法, 各類所得扣繳率標準) ; https://www.mof.gov.tw | n/k | 2026-10-10 | unverified |
| U16 | Business tax: standard rate and small-scale rate (recalled 5% and 1%); 統一發票 duty for registered businesses | https://law.moj.gov.tw (search 加值型及非加值型營業稅法) | n/k | 2026-10-10 | unverified |
| U17 | Business Registration Act and Company Act: 商號 vs 有限公司; single-member company allowed; no minimum capital recalled | https://law.moj.gov.tw (search 商業登記法, 公司法) ; https://gcis.nat.gov.tw | n/k | 2026-10-10 | unverified |
| U18 | Trademark Act: first-to-file; 10-year term; Art. 30 refusal grounds including others' portrait or name; agent for foreign applicants | https://law.moj.gov.tw (search 商標法) ; https://www.tipo.gov.tw | n/k | 2026-10-10 | unverified |
| U19 | Copyright Act: human authorship; TIPO position that purely AI-generated output is not a work (recalled; same as monetisation.md U2) | https://law.moj.gov.tw (search 著作權法) ; https://www.tipo.gov.tw | n/k | 2026-10-10 | unverified |
| U20 | Civil Code Art. 18 and Art. 195 on personality rights and non-pecuniary damages; portrait right recognised by case law (recalled; partly echoed by S8) | https://law.moj.gov.tw (search 民法) | n/k | 2026-10-10 | unverified |
| U21 | Personal Data Protection Act duties (Art. 8, 19, 20, 27 recalled); marketing opt-out; cross-border transfer | https://law.moj.gov.tw (search 個人資料保護法) | n/k | 2026-10-10 | unverified |
| U22 | Consumer Protection Act advertising-truth article (Art. 22 recalled); distance-selling 7-day return and digital-content exception | https://law.moj.gov.tw (search 消費者保護法, 通訊交易解除權合理例外情事適用準則) | n/k | 2026-10-10 | unverified |

---

## Verification note

Date: 2026-10-10. Independent verifier pass (not the author).

**What I attempted.** I tried to re-fetch the highest-stakes primary and secondary sources: the Fair Trade Act Art. 21 page on law.moj.gov.tw, and the Lee and Li, technews.tw, CNA and inside.com.tw pages cited as S1, S2 and S5. WebFetch failed on every host with a DNS error (`getaddrinfo ENOTFOUND`). WebSearch refused all queries because the shared 200-call budget is spent. The proxy status endpoint shows 403 CONNECT denials for cna.com.tw, udn.com, bnext.com.tw and support.google.com, among others. I did not use curl, archives or third-party readers to get around this, per the proxy and search-tool instructions.

**Result: no claim in this file was independently re-verified against a source.** No source row has been upgraded. Confidence in S rows is at most what the sibling files gave.

**What I did check, by reading and by my own recall (recall is not verification):**
- Internal consistency of fine range, article numbers, dates and tags across sections 1, 3, 5, 10, 11 and the Sources table. The file is consistent: every article number is tagged [U] unless a reported source gives it, and no fee, threshold or sector fine is stated.
- My recall agrees with the author's recall on: Fair Trade Act Art. 21 (misleading representations; endorser definition including personal experience; ordinary-consumer exception), the Art. 42 fine tier of NT$50,000 to NT$25 million, Income Tax Act Art. 14 (ten categories), PDPA Art. 8/19/20/27, Consumer Protection Act Art. 22, Civil Code Art. 18 and 195, the TIPO human-authorship position, and the trademark 10-year term. All remain unverified.
- Corrections made: (1) the "third day after promulgation" rule restated as "third day counting the promulgation day" and flagged; (2) civil joint liability under Art. 21 noted as 連帶損害賠償責任, distinct from the fine; (3) trademark agent for foreign applicants flagged as possibly mandatory; (4) criminal exposure for unlicensed investment advice flagged; (5) S5 and S6 downgraded from high to medium because neither was re-opened; (6) S1 date and confidence corrected (the inside.com.tw page date "2023-02" is unconfirmed and the fine range may reflect an older amendment); (7) S5 fine date versus report date gap flagged.
- Ground rules: no recommendation breaks them. I added an explicit default of no affiliate or referral links for finance, supplement and health-device categories pending lawyer answers, because section 6.2 and question 13 left that open. The "probably compliant" angles are labelled as the operator's and lawyer's call, not a clearance.
- Vocabulary and script: scanned for Simplified characters and mainland terms (視頻, 信息, 博主 and similar). None found; zh text is Traditional and uses Taiwan terms (業配, 薦證廣告, 網紅, 記帳士).
- Sources table: present, with id, claim, URL, date published, date accessed (2026-10-10) and confidence for S1 to S17 and U1 to U22.

**Still unverified (the whole legal substance):** the fine range and article numbers; the AI Basic Act effective date, authority and content; Fraud Act Art. 31/40/42 details and the 2026-08-14 Meta fine; the FTC 2026-04-23 statement; the platform designation list; all sector rules and Art. 107-type penalties; all tax and business-tax figures; registration, trademark and PDPA points; Life8, IKEA and Guardian incidents; fraud statistics. The file's own verification pack in section 2 remains the correct next step, and needs either an egress policy that allows law.moj.gov.tw, ftc.gov.tw, fda.gov.tw, fsc.gov.tw, tipo.gov.tw and the cited news hosts, or a human pasting the text.
