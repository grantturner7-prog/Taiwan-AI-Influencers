# Culture research: tone, language, calendar, taboos, AI reception and visual detail for Taiwan audiences

Phase 1 deliverable `research/culture.md`. Written 2026-10-10. Scope: a studio of openly-virtual (disclosed AI) personas for audiences in Taiwan, run by one operator at 6 h/week with a NT$5,000/month tools budget, who is not good at Traditional Chinese and therefore needs a native zh-TW reviewer (審稿者) on every post [B3]. This is research for a content team, not legal advice and not a native-speaker audit.

Contents: 0 Method and limits, 1 Bottom line, 2 Tone and register by platform, 3 Language (Taiwan Mandarin vs mainland, characters, particles, 台語/客語, 注音文, emoji, slang), 4 Commercial calendar 2026-10 to 2027-12, 5 Topics and imagery to avoid, 6 How Taiwanese audiences react to AI and virtual characters, 7 Visual settings and generator errors, 8 Reviewer brief (English and zh-TW), 9 Where this complicates the brief or the niches, 10 Open questions, then Sources.

---

## 0. Method, limits and how to read the tags

**Read this first, because it changes how far you can trust the file.**

- **No live web source was opened in this session.** My first four `WebSearch` calls (slang, holiday calendar, AI-influencer attitudes) all returned "web search budget used up (limit 200 per turn, shared by every agent)". `WebFetch` failed with DNS errors (`ENOTFOUND`) on every host I tried: www.dgpa.gov.tw, zh.wikipedia.org, focustaiwan.tw, www.mof.gov.tw. A request to read the proxy's README was refused by the permission system; I did not retry it and I did not try to reach any search engine, reader or archive by another route.
- **Consequence for the brief to "verify slang and dates with recent sources":** I could not. This file contains **no claim that any slang term is "current in 2026"**, no verified 2027 government holiday calendar, and no verified department-store or e-commerce campaign dates. Those items are labelled `unverified` and each has a "where to verify" pointer.
- **Three kinds of evidence are used, each tagged:**

| Tag | Meaning | How far to trust it |
|---|---|---|
| `[B#]` | A project requirement in BRIEF.md or DECISIONS.md | High: it is the operator's own rule |
| `[S#]` | A source read by a sibling research agent (as a search summary, not a fetched page) and re-used here with its original id shown in the Sources table | As the sibling file labelled it, usually `medium` |
| `[C#]` | **Computed** by me in this session: lunar-calendar dates from the `lunardate` library, cross-checked with an independent astronomical calculation I wrote, plus weekday arithmetic | High for arithmetic; see 4.1 for the one near-midnight edge case |
| `[U#]` | **Recalled** from my training data, not checked this session | `unverified` by definition. The native reviewer's sign-off is the verification step |

- **Vocabulary pairs in 3.1 are `[U1]`**, with four pairs also named in the brief [B2]. I list only pairs I am confident about. Pairs I am not confident about are listed separately in 3.1 so the reviewer can rule on them.
- "Not found" means I had no citable source and did not fill the gap with an estimate. Planning assumptions are labelled "assumption".
- **Draft zh-TW example lines are written by an AI.** Every line in sections 2 and 8 must be read by the native reviewer before use.
- Working-document language: English with the zh-TW term beside Taiwan-specific concepts. Emoji are shown by name in this file to keep it plain text.

---

## 1. Bottom line

1. **The strongest evidence in this file is the calendar I computed [C1][C2][C3]; the weakest is anything about "current" slang.** Treat sections 4.1 to 4.3 as reliable arithmetic and section 3.8 as a watchlist for the reviewer, not a trend report.
2. **The single most important voice constraint is that Taiwan's recommendation genre is built on personal experience words, and the personas may not use them.** 愛用, 回購, 開箱, 實測, 心得, 上身, 踩雷 all claim that the speaker used, wore or tested something. Ground rule 4 bars that [B1]. The same data that make experience content powerful (60.3% of 25-34s say another person's shared experience makes them want to try something, from an MIC survey, n=1,091, Q4 2024 fieldwork, as reported in `platforms.md` [S1]; not re-opened by me) mean the persona must win by explanation, comparison and a clearly-AI character voice. Section 2.3 gives replacement wording.
3. **Platform register differs sharply.** Instagram is polished but warm; Threads (脆) is conversational and reply-driven; Facebook skews older and more formal; Dcard and PTT are hostile to anything that smells like 業配 and the platforms ban or police promotion [S11][S12]. For a persona that cannot tell personal anecdotes, the workable Threads moves are questions, polls, general observations and open "I am an AI" humour (2.2).
4. **Mainland vocabulary is the fastest way to lose a Taiwan audience [B2], and the operator cannot self-check.** Section 3.1 lists more than 100 avoid/use pairs; 3.3 lists the Simplified-to-Traditional converter traps (后/後, 发/髮, 周/週, 历/曆 and others). Never let an image generator render text; add text in post-production with a Taiwan-glyph font (3.3, 7.2).
5. **Computed 2027 dates that matter [C1][C2][C3]:** 除夕 Fri 2027-02-05; 農曆新年初一 Sat 2027-02-06 (2027 is a 丁未 / goat year [C5]); 情人節 Sun 2027-02-14 falls on lunar 1/9 (天公生); 元宵 Sat 2027-02-20; 母親節 Sun 2027-05-09; 端午 Wed 2027-06-09; 七夕 and 父親節 coincide on Sun 2027-08-08; 中秋 Wed 2027-09-15.
6. **The 2026 ghost month (鬼月) ended 2026-09-10 [C1]; the 2027 one runs 2027-08-02 to 2027-08-31 and 中元節 is Mon 2027-08-16 [C1].** Launching accounts between now and mid-2027 avoids the ghost month; planning a big 2027 campaign in August does not.
7. **Time to the next peaks from today (2026-10-10) [C3]:** 雙11 in 32 days, 雙12 in 63 days, 跨年 in 82 days, 農曆新年 in 119 days. With a business registration that takes about two weeks [B3] and a reviewer still to be found, a brand-paid post for 雙11 is unrealistic (inference). Organic positioning content for 雙12, 跨年 and 年終獎金 / 農曆新年 is the realistic first window.
8. **Taiwan's nine-in-one local elections are, as I recall, on Sat 2026-11-28 [U12].** That sits inside the first weeks of any launch. Avoid election hooks, polling-day posts and party-colour palettes; keep the persona outside politics per Ground rule 6 [B1]. Verify the date at the Central Election Commission (中央選舉委員會).
9. **I found no Taiwan survey on acceptance of disclosed AI influencers.** Taiwan-specific signals are mixed: visible AI mistakes get mocked quickly (IKEA Taiwan hands, 2026-06-01 [S19]); an AI likeness dispute hit a Taiwan apparel brand (Life8, July 2026 [S18]); stylised virtual characters (VTubers, mascots) are clearly accepted and monetised [S28][S29][S30]. The safest design reading is a stylised, high-quality, openly-AI character, not a realistic fake human (section 6).
10. **Generator failures that read as "not Taiwan" are predictable:** garbled or Simplified signage, wrong plates, a convenience store that looks Japanese or American, a temple mixed with a shrine, a bubble-tea cup with a dome lid. Section 7.6 is a 20-point "Taiwan-ness" check to merge into `pipeline/qa-checklist.md`.

---

## 2. Tone and register by platform

### 2.1 Cross-platform principles for Taiwan Mandarin social writing

All of this is `[U5]` practitioner knowledge of Taiwan social media, not measured; the reviewer should correct it.

| Principle | What it means in practice | Why it matters for these personas |
|---|---|---|
| Friendly-soft, not shouty | Short sentences, softeners (喔, 啦, 耶), a tilde (～) at the end of a friendly line, few exclamation-only hooks. Hard-sell claims read as pushy | Fits a "helpful character" persona; avoids 工商味 (ad-sounding) |
| Audiences scan for 業配味 | Anything that sounds like paid copy is called out as 業配 or 工商 (see Dcard/PTT 2.2). Disclosing early reduces the sting | Sponsored posts must be marked anyway [B1] |
| 你 versus 您 | Most social content uses 你 / 你們 (a friendly peer). 您 is used by brand customer-service voices, Facebook pages aimed at 45+, and LINE OA service messages | Pick one per persona and keep it |
| Self-deprecating humour is the default charm | Playing small ("我只是 AI") is more likeable than claiming authority | Lets the persona turn "I cannot try things" into its identity |
| Light English code-mixing is normal | "OK", "so", "chill", brand names, hashtags in English | Do not mix in mainland-style English-letter slang such as "yyds" (3.2) |
| Line breaks over punctuation | Casual posts use short lines, spaces and line breaks rather than full punctuation; formal posts use full-width punctuation | Threads and Instagram captions: short lines |
| Local anchors beat generic ones | Naming a district, a convenience-store item or an MRT line makes content feel local | Handled in section 7 |
| Not-quite-translation voice | The most common AI tell is translation-ese: stiff connectors (因此, 此外, 總而言之), long noun chains, and "首先...其次...最後" structures | Reviewer should rewrite these; Taiwanese speakers say 然後, 所以, 不過, 其實 |

### 2.2 Platform-by-platform register, with example lines

Audience figures are from the MIC social survey (fieldwork Q4 2024) and the NCC / MIC releases cited in `platforms.md` [S1][S2][S3][S4]. All example lines are **drafts for reviewer rewrite** and are written so that they do **not** claim personal experience (2.3).

| Platform | Who is there [S1][S3][S4] | Register | Length, emoji, tags | Example lines (zh-TW, with gloss) | Watch-outs |
|---|---|---|---|---|---|
| **Instagram** (貼文 / 限時動態 / Reels) | 18-24: 78%; 25-34: 59.3% frequent use [S1]. Reels reach 43.0% of Taiwan short-video users [S4] | Polished but warm; visual first; caption supports the image | 1 to 4 short lines; 1 to 3 emoji; 3 to 8 hashtags at the end (reviewer to calibrate) | Carousel cover: 「薄外套怎麼選？一張圖看懂三種版型」 (How to choose a light jacket: three cuts in one image). Caption: 「早晚溫差大的季節，薄外套最好入手。這篇整理三種常見版型的差別，先收藏起來，逛街時可以對照看看～」 (Summary, then a save prompt). Reel opener: 「三個重點，一分鐘講完。」 Closing: 「想看哪個主題，留言告訴我。」 | Saves and shares are the measured goal [B1], so end with a save or send prompt. "AI-generated profile" label rules apply [S8] |
| **Threads (脆)** | 18-24: 44%; 25-34: 28.4%; frequent use 17.5% overall [S1] | Conversational, quick, reply-driven; mild irony | 1 to 4 lines; one idea per post; a question or an opinion; at most one tag | Question: 「問個問題：換季的時候，你是先買衣服，還是先整理衣櫃？」 (Asks the audience; no persona experience). Open AI humour: 「先說明，我是 AI 虛擬角色，沒辦法真的穿給你看，所以我只整理版型和搭配邏輯，實際尺寸請以品牌官方資訊為準喔。」 Reply: 「這個問題我整理成三點：」 (verifier removed "often asked", which implies an audience history the persona may not have) | Highest slang density and highest reviewer burden per post [S13]. Do not copy the genre of personal anecdotes ("今天...") |
| **TikTok** | 72.5% of 16-25 have watched; 47.5% overall; 23.8% hold an account [S3] | Fast, spoken, Gen Z; hook in the first 1 to 2 seconds; on-screen captions in Traditional Chinese | Very short caption; 2 to 4 tags | Hook: 「先別滑！尺寸表有三個地方要看清楚。」 (Don't scroll yet; three things to check on a size chart. Verifier changed this from a draft that claimed "many people misread it", an unsourced audience claim). Education hook: 「三十秒搞懂：深蹲和硬舉差在哪？」 | Wave-2 platform per `platforms.md`. Manual posting only. Label rules [S9] |
| **YouTube Shorts / YouTube** | YouTube Shorts used by 68.1% of Taiwan short-video users; YouTube users lean to search and knowledge [S4] | Informational, keyword-titled, slightly more neutral | Title carries the keyword; description has sources and the AI/sponsor disclosure | Title: 「【一分鐘搞懂】帽T 和大學T 差在哪？」 (【】 brackets are a common Taiwan title device [U5]) | AI label rules [S10]. Explainers suit a character that cannot testify |
| **Facebook (Page)** | Core is 45+ (79.4% of 45-54); roughly six in ten of 18-34 [S1][S34]. Reels reach 58.4% of short-video users [S4] | More formal, longer sentences, greeting words, 您 acceptable; shareable infographics | Longer text is fine; few hashtags | 「各位朋友午安，今天整理了挑選運動水壺的三個重點，歡迎分享給需要的朋友。」 | A persona must be a Page, not a personal profile: Meta treats personal profiles for non-human entities as fake accounts [S14]. Do not use youth slang for a 45+ persona |
| **LINE Official Account (官方帳號)** | LINE is universal: 98.2% hold an account [S2]; about 14 opens a day among users [S5] | Friend-like, short, rich-menu driven; stickers (貼圖) are part of the voice | Short; avoid over-sending (unfollow/block risk, inference) | Broadcast: 「Hi，本週整理來囉！點下方選單就能看完整內容～（此為自動發送訊息）」. Auto-reply: 「這是自動回覆訊息。我是 AI 虛擬角色，真人團隊會在上班時間回覆你。」 | Brief rule 9: automated replies must say so [B1]. LINE VOOM closed 2026-09-30 [S6] |
| **Dcard** (listening only) | 18-24: 45.9%; 25-34: 30.9% [S1] | Anonymous, confessional, board-based; opens with 「各位卡友好」; long help-seeking posts | n/a | A typical help post: 「各位卡友好，最近想買一件薄外套，有推薦的版型嗎？」 Typical wary reply: 「疑似業配」 (suspected sponsored post) | Commercial/promotional posts are banned; three violations bring a 7-day suspension [S11]. Do not post |
| **PTT** (listening only) | Largest share of its users is 35-44, then 25-34 [S1] | Terse, ironic, rule-bound; replies use 推 / 噓 / → | n/a | Advert posts get the prefix 【工商】 or are called 「有業配味」 [U5] | Founder said controls target coordinated volume inflation [S12]. Do not post |

Use Dcard and PTT as a **free listening post** for how Taiwanese people phrase needs and complaints. Nothing here needs a login-based scrape and none is allowed [B1].

### 2.3 Words that claim personal experience: banned for personas, with replacements

Ground rule 4 says a virtual character has not eaten, worn, used or tested anything and must never testify [B1]. Taiwan's recommendation vocabulary is full of such words. `[U1]`

| Do not use (claims use or presence) | Why it breaks Ground rule 4 | Use instead (zh-TW) |
|---|---|---|
| 愛用, 愛用品, 回購 | Says the speaker uses it and bought it again | 「選購重點」「熱門款式整理」「常被問到的款式」 |
| 實測, 親測, 試用, 我試了 | Says the speaker tested it | 「規格比較」「官方資料整理」「比較表」 |
| 開箱 | Says the speaker received and opened it | 「商品資訊整理」「款式介紹」 |
| 心得, 使用心得, 評價 (as own view of use) | Own experience report | 「重點整理」「購買前確認清單」 |
| 上身, 穿起來, 我今天穿 | Says the speaker wore it | 「版型說明」「搭配示意（AI 生成圖）」 |
| 好吃, 好喝, 口感 (as own taste) | Says the speaker ate it | 「成分與規格」「口味有哪些」 |
| 我練了, 我今天練腿, 我跑了 | Says the speaker trained | 「動作重點」「課表範例（一般資訊）」 |
| 我去了, 我在士林夜市, 打卡 (as presence) | Says the speaker was there | 「士林夜市逛法整理」；圖片標示「AI 生成場景，非實際到訪」 |
| 踩雷 / 避雷 (from own bad purchase) | Implies a past bad purchase | 「購買前要確認的三件事」 |
| Day-in-my-life or GRWM ("get ready with me") vlogs | Invented daily life | Do not use; use explainers, comparisons, Q&A |

**Formats that fit versus formats that break the rule** (assessment is mine; `[U3]`)

| Format | Fit |
|---|---|
| 懶人包 (summary pack), 一張圖看懂 (one-image explainer), 三個重點 (three points), 新手必看 (beginner guide) | Fits |
| A 對 B 比較 (A vs B comparison), 選購指南, 尺寸表怎麼看 | Fits |
| Q&A / 留言問答, 迷思整理 (myth explainer; avoid health topics) | Fits |
| Poll formats and perennial food debates (鹹甜豆花, 北部粽 vs 南部粽, 蛋餅加不加醬) | Fits: asks the audience, no persona experience |
| 長輩圖 (greeting images), seasonal greeting cards | Fits for 45+ personas |
| 開箱, 實測, 試穿, GRWM, day-in-my-life, "我的一週菜單" | Breaks Ground rule 4 |
| Before/after body results | Breaks Ground rule 6 and Taiwan food/cosmetic advertising rules (`legal.md`) |

### 2.4 Disclosure and sponsorship phrasing (drafts; legal wording lives in `legal.md`)

| Where | Draft zh-TW | Note |
|---|---|---|
| Bio (brief rule 1 and 8) | 「AI 虛擬角色｜〇〇工作室 製作」or「我不是真人，是 AI 虛擬角色，由〇〇工作室企劃製作。」 | Studio name is mandatory in every bio [B1] |
| First line of a caption with realistic images | 「【AI 虛擬角色】本篇圖像與影片皆為 AI 生成。」 | Disclosure must sit in the caption and the label, not only the bio, because a buried bio disclosure failed in the Mia Zelu case [S22] |
| On-screen text in video | 「AI 生成影片」 (corner label, first 3 seconds) | In addition to the platform label [S8][S9][S10] |
| Sponsored post (業配) | 「【業配】本篇與〇〇合作，品牌提供產品資訊。」 and the platform paid-partnership tool | The FTC treats sponsored posts as 薦證廣告 and requires material connections to be disclosed [S15]. Do not write "我用過" |
| Automated reply | 「這是自動回覆訊息。」 | Brief rule 9 [B1] |
| Persona self-reference | 「我是 AI，所以我沒辦法真的吃、穿、試，只能幫你整理資訊。」 | Turns the limitation into the brand |

---

## 3. Language

### 3.1 Taiwan Mandarin versus mainland vocabulary

Column "Conf": **H** = I am certain the pair is correct as a Taiwan-versus-mainland contrast; **M** = correct, but both forms are heard in Taiwan or the contrast is softer. All rows `[U1]` unless noted; rows 1, 3, 4 and 45 are named in the brief [B2]. The reviewer should sign off the whole table.

**A. Digital, social and media**

| # | Avoid (mainland) | Use (Taiwan) | Meaning | Conf | Note |
|---|---|---|---|---|---|
| 1 | 視頻 | 影片 | video (clip) | H | 視訊 = video call [B2] |
| 2 | 短視頻 | 短影音 | short-form video | H | |
| 3 | 信息 | 資訊 | information | H | [B2] |
| 4 | 博主 | 網紅 / 創作者 | influencer / creator | H | KOL is also used in the industry [B2] |
| 5 | 博客 | 部落格 | blog | H | |
| 6 | 主播 (streamer) | 直播主 / 實況主 | live-streamer | H | In Taiwan 主播 means a TV news anchor |
| 7 | 關注 | 追蹤 | follow | H | |
| 8 | 點贊 | 按讚 | like | H | |
| 9 | 評論 (on a post) | 留言 | comment | H | |
| 10 | 轉發 | 分享 / 轉貼 | share / repost | H | |
| 11 | 私信 | 私訊 | DM | H | |
| 12 | 帖子 / 發帖 | 貼文 / 發文 | post | H | |
| 13 | 社交媒體 | 社群媒體 / 社群平台 | social media | H | |
| 14 | 快拍 / 故事 | 限時動態 | Instagram Stories | H | |
| 15 | 表情包 | 貼圖 (LINE) / 迷因圖 | sticker / meme image | H | |
| 16 | 網絡 | 網路 | internet / network | H | |
| 17 | 賬號 / 賬戶 | 帳號 / 帳戶 | account | H | 賬 is also a character trap (3.3) |
| 18 | 登錄 | 登入 | log in | H | |
| 19 | 鏈接 | 連結 | link | H | |
| 20 | 軟件 / 硬件 | 軟體 / 硬體 | software / hardware | H | |
| 21 | 鼠標 | 滑鼠 | mouse | H | |
| 22 | 屏幕 | 螢幕 | screen | H | |
| 23 | 內存 | 記憶體 | memory | H | |
| 24 | U盤 | 隨身碟 | USB drive | H | |
| 25 | 程序 (software) | 程式 | program | H | |
| 26 | 默認 | 預設 | default | H | |
| 27 | 設置 | 設定 | settings | H | |
| 28 | 保存 (save in an app) | 儲存 | save | M | 保存 also exists in Taiwan for "preserve" |
| 29 | 打印 | 列印 | print | H | |
| 30 | 分辨率 | 解析度 | resolution | H | |
| 31 | 激活 | 啟用 | activate | H | |
| 32 | 兼容 | 相容 | compatible | H | |
| 33 | 支持 (tech support) | 支援 | support (software) | M | |
| 34 | 短信 | 簡訊 | SMS | H | |
| 35 | 郵箱 | 信箱 | mailbox | H | |
| 36 | 服務器 | 伺服器 | server | H | |
| 37 | 數據庫 | 資料庫 | database | H | |
| 38 | 智能 | 智慧 | smart | H | 智慧型手機 |
| 39 | 人工智能 | 人工智慧 | artificial intelligence | H | The statute is called the 人工智慧基本法 per the brief; its date and content are unconfirmed in `legal.md` |
| 40 | 數字化 / 數字人 | 數位化 / 數位人 (虛擬人) | digital / digital human | H | The ministry is 數位發展部 |
| 41 | 充電寶 | 行動電源 | power bank | H | |
| 42 | 移動支付 | 行動支付 | mobile payment | H | |
| 43 | 二維碼 | QR Code | QR code | H | |
| 44 | 軟廣 / 商單 / 恰飯 | 業配 | sponsored post | H | 業配 = 業務配合 |

**B. Commerce, money and delivery**

| # | Avoid (mainland) | Use (Taiwan) | Meaning | Conf | Note |
|---|---|---|---|---|---|
| 45 | 質量 | 品質 | quality | H | In Taiwan 質量 = physical mass [B2] |
| 46 | 性價比 | CP值 | value for money | H | CP = cost/performance |
| 47 | 快遞 | 宅配 | home parcel delivery | M | 快遞 is used for international express |
| 48 | 外賣 | 外送 (delivery) / 外帶 (take-away) | food delivery / take-away | H | |
| 49 | 便利店 | 便利商店 / 超商 | convenience store | H | |
| 50 | 轉賬 | 轉帳 | bank transfer | H | |
| 51 | 賬單 | 帳單 | bill | H | |
| 52 | 項目 (project) | 專案 | project | H | |
| 53 | 反饋 | 回饋 | feedback | H | |
| 54 | 積分 | 點數 / 集點 | loyalty points | M | |
| 55 | 打車 | 叫車 / 搭計程車 | hail a cab | M | |
| 56 | 郵編 | 郵遞區號 | postal code | H | |
| 57 | 身份證 | 身分證 | ID card | H | 分 not 份 |

**C. Daily life, transport, place**

| # | Avoid (mainland) | Use (Taiwan) | Meaning | Conf | Note |
|---|---|---|---|---|---|
| 58 | 地鐵 | 捷運 | metro (MRT) | H | |
| 59 | 公交車 | 公車 | bus | H | |
| 60 | 出租車 | 計程車 (小黃) | taxi | H | |
| 61 | 摩托車 / 電動車 (scooter) | 機車 | scooter / motorcycle | M | 摩托車 is also used in Taiwan, mostly formally; 電動車 is mainland for e-scooters, Taiwan says 電動機車 [U1] |
| 62 | 酒店 | 飯店 / 旅館 | hotel | H | In Taiwan 酒店 can mean a hostess bar |
| 63 | 小區 | 社區 / 大樓 | residential compound | H | |
| 64 | 空調 | 冷氣 | air conditioner | M | 空調 is also used in Taiwan for building systems (中央空調); 冷氣 is the everyday home word |
| 65 | 塑料 | 塑膠 | plastic | H | |
| 66 | 衛生間 | 洗手間 / 廁所 | toilet | H | |
| 67 | 煤氣 | 瓦斯 | gas | H | |
| 68 | 電飯煲 | 電鍋 | rice cooker | H | The Tatung 大同電鍋 is a cultural icon |
| 69 | 厘米 / 米 | 公分 / 公尺 | cm / metre | H | |
| 70 | 平方米 | 平方公尺 / 坪 | area | H | 坪 is the everyday housing unit |
| 71 | 公元 | 西元 | CE year | H | Government forms use 民國 years (115年 = 2026) |
| 72 | 普通話 | 國語 (華語 for learners) | Mandarin | H | Sensitive identity word; see 5.8 |

**D. Food and fitness education** (technique, gear and exercise names only; no health or weight-loss claims [B1])

| # | Avoid (mainland) | Use (Taiwan) | Meaning | Conf | Note |
|---|---|---|---|---|---|
| 73 | 土豆 | 馬鈴薯 | potato | H | In Taiwan 土豆 can mean peanut |
| 74 | 西紅柿 | 番茄 | tomato | H | |
| 75 | 紅薯 | 地瓜 | sweet potato | H | |
| 76 | 西蘭花 | 青花菜 | broccoli | H | |
| 77 | 菠蘿 | 鳳梨 | pineapple | H | |
| 78 | 獼猴桃 | 奇異果 | kiwi | H | |
| 79 | 酸奶 | 優格 / 優酪乳 | yoghurt / drinking yoghurt | H | |
| 80 | 奶酪 | 起司 / 乳酪 | cheese | H | |
| 81 | 方便麵 | 泡麵 | instant noodles | H | |
| 82 | 盒飯 | 便當 | boxed meal | H | |
| 83 | 雪糕 | 冰棒 | ice lolly | H | |
| 84 | 薯片 | 洋芋片 | crisps | H | |
| 85 | 俯臥撐 | 伏地挺身 | push-up | H | |
| 86 | 硬拉 | 硬舉 | deadlift | M | Both forms are heard in Taiwan gyms; reviewer to rule |
| 87 | 力量訓練 | 肌力訓練 / 重訓 | strength training | H | |
| 88 | 鍛煉 | 鍛鍊 | exercise / train | H | Character variant |
| 89 | 瑜伽 | 瑜珈 | yoga | M | 瑜珈 is the common Taiwan business spelling; 瑜伽 also appears in Taiwan and I could not check the Ministry of Education dictionary form. Reviewer to rule |
| 90 | 動感單車 | 飛輪 | spin class | H | |
| 91 | 拉伸 | 伸展 | stretching | M | 拉伸 is also heard in Taiwan gyms |
| 92 | 熱身 | 暖身 | warm-up | M | 熱身 is also normal in Taiwan (e.g. 熱身賽); 暖身 is the more common exercise word |

**E. Fashion**

| # | Avoid (mainland) | Use (Taiwan) | Meaning | Conf | Note |
|---|---|---|---|---|---|
| 93 | 連衣裙 | 洋裝 / 連身裙 | dress | H | |
| 94 | 衛衣 | 帽T / 大學T | hoodie / sweatshirt | H | |
| 95 | 打底褲 | 內搭褲 | leggings | H | |
| 96 | 人字拖 | 夾腳拖 | flip-flops | M | |
| 97 | 墨鏡 | 太陽眼鏡 | sunglasses | M | |
| 98 | 雙肩包 | 後背包 | backpack | H | |
| 99 | 斜挎包 | 斜背包 / 側背包 | crossbody bag | H | |
| 100 | 錢包 | 皮夾 | wallet | M | |
| 101 | 面料 | 布料 | fabric | H | |
| 102 | 周年慶 | 週年慶 | anniversary sale | H | 週 not 周 (3.3) |

**F. Address forms and hype words (mainland-coded)**

| # | Avoid (mainland-coded) | Use (Taiwan) | Meaning | Conf | Note |
|---|---|---|---|---|---|
| 103 | 給力 | 讚 / 厲害 / 很強 | great | H | |
| 104 | 牛 / 牛逼 | 厲害 / 強 | awesome | H | 牛逼 is also vulgar |
| 105 | 家人們 | 大家 / 各位 / 朋友們 | "everyone" (streamer greeting) | H | |
| 106 | 寶子 | 大家 / 各位 | friendly address | H | |
| 107 | 親 (Taobao-style address) | 你 / 您 | "dear" | H | |
| 108 | 乾貨 (useful content) | 重點整理 / 懶人包 | useful summary | M | 乾貨 in Taiwan mostly means dried goods |
| 109 | 種草 / 安利 | 推薦 / 推坑 (colloquial) | recommend | M | Still avoid the experience wording in 2.3 |
| 110 | 剁手 | 手滑 / 荷包失守 | impulse-buy joke | M | |

**Pairs I am not confident about. Do not enforce either side until the reviewer rules:** 顏值 versus 顏質; 靠譜 versus 可靠; 吐槽; 攻略 versus 懶人包; 打卡; 小姐姐 / 小哥哥 (reads mainland-coded, but some Taiwanese youth use it ironically); 閨蜜 versus 好姊妹; 爆款; 硬核; 賦能; 落地; 優化 versus 最佳化; 工資 versus 薪水 (工資 is a standard Taiwan legal term, so it is **not** a mainland marker); 保存 versus 儲存 (both legitimate); 快遞 versus 宅配 (both legitimate).

**Taiwan-coded words worth using** (stable, high-utility) `[U1][U3]`: CP值, 懶人包, 口袋名單 (go-to list), 小資 (budget-minded), 平價, 必買, 入手 (to acquire; avoid as personal claim), 網美 (photogenic Instagram-style woman), 超商取貨, 蝦皮, 悠遊卡 (EasyCard), 載具 (e-invoice carrier), 手搖飲, 珍奶, 微糖少冰.

### 3.2 Mainland-coded slang and phrasing to avoid

| Item | Why avoid | Taiwan alternative |
|---|---|---|
| 絕絕子, yyds (永遠的神), 家人們誰懂啊 | Mainland short-video slang, 2021 to 2023 era; reads as 抖音 / 小紅書 vocabulary `[U3]` | 真的超讚, 太神了, 有人懂嗎 (reviewer to choose) |
| 栓Q (thank-you meme), 破防 | Mainland origin; Taiwan currency uncertain | Leave to reviewer |
| Bracketed text emoji such as 「[微笑]」「[捂臉]」 | These are WeChat / Weibo codes and look mainland | Use real emoji or text emoticons (3.7) |
| 「親，」 or 「寶子們」 sales greeting | Taobao and mainland live-selling | 「Hi」「各位」「大家好」 |
| Hard-sell livestream rhythm ("三二一上鏈接") | Mainland 帶貨 style | Calm explanation |
| Flowery formal register, 四字成語 chains | Reads like state-media copy | Short spoken sentences |

Context: Xiaohongshu (小紅書), the usual discovery channel for fashion and food, is blocked in Taiwan for a provisional year from 2025-12-04 [S7]; that period would run to about 2026-12-04 unless extended (inference from "one year"; current status unverified). Its "種草" vocabulary entered Taiwan through its 3-million-plus users, so it may still be understood, but it marks the writer as mainland-adjacent.

### 3.3 Characters, fonts and punctuation

**Simplified-to-Traditional converter traps** (a machine converter that maps one Simplified character to one Traditional character produces these). `[U4]`

| Simplified | Taiwan Traditional, right | Wrong output to catch | Example |
|---|---|---|---|
| 后 | 後 (after) | 后 | 以後, 然後. 后 is only for 皇后 / 王后 |
| 发 | 髮 (hair) / 發 (emit) | 頭發 | 頭髮, 理髮; 發展, 發生 |
| 干 | 乾 / 幹 / 干 | 干淨 | 乾淨, 乾燥; 幹部; 干涉 |
| 面 | 麵 (noodle/flour) / 面 | 面包 | 麵包, 泡麵; 面膜 |
| 表 | 錶 (watch) / 表 | 手表 | 手錶; 表格, 表現 |
| 制 | 製 (make) / 制 | 制作 | 製作, 製造; 制度, 限制 |
| 周 | 週 (week/cycle) / 周 | 周末, 周年慶 | 週末, 週年慶, 一週; 周到, 周圍, surname 周 |
| 历 | 曆 (calendar) / 歷 | 農歷 | 農曆, 日曆; 歷史, 經歷 |
| 松 | 鬆 (loose) / 松 | 放松 | 放鬆; 松樹 |
| 系 | 係 / 繫 / 系 | 關系, 聯系 | 關係, 聯繫; 系統 |
| 范 | 範 / 范 | 范圍 | 範圍; surname 范 |
| 里 | 裡 / 里 | 這里, 里面 | 這裡, 裡面; 公里, 鄰里 |
| 台 | 臺 / 台 / 檯 / 颱 | 台風 | 臺灣 or 台灣 (both accepted); 颱風; 檯燈 |
| 么 | 麼 | 什么, 怎么 | 什麼, 怎麼 |

**Taiwan standard glyph forms versus Hong Kong or Japanese forms** `[U4]`: Taiwan writes 著 (not 着), 為 (not 爲), 啟 (not 啓), 說 (not 説), 裡 (Hong Kong often 裏), 於 (not 于), and 帳 (帳號, 帳單, 轉帳) where Hong Kong and other Traditional-script text often use 賬 (賬號, 賬單, 轉賬), which reads as non-Taiwan. Many image models and fonts default to other regional forms. Pick fonts with a **Taiwan (TC)** glyph set, for example Noto Sans TC (Source Han Sans TC), and set the language tag to `zh-TW` in any HTML or design file. If a generator draws 嘅, 咗, 唔, 冇, 啲 it is writing Hong Kong Cantonese; if it draws 気, 国, 学, 会 it is using Japanese forms. Both are failures.

**Punctuation and numerals** `[U4]`: Taiwan uses 「 」 and 『 』 for quotation, not “ ”; full-width ，。、？！：；; 《 》 for titles; the ellipsis 「……」. Ordinary social posts often skip end punctuation. Prices are written NT$1,280 or 1,280 元 (colloquially 塊); do not use ¥ or RMB. Dates in social copy use 西元 or just month and day (10/10, 10月10日); government and invoice contexts use 民國 years (115年).

**Romanisation on signs is inconsistent in Taiwan** (Hanyu Pinyin, Tongyong Pinyin and older spellings co-exist) `[U13]`, which is realistic for a street sign but a trap for a generator that prints perfectly consistent pinyin. For pronunciation guides to Taiwanese learners, 注音 (bopomofo) rather than pinyin is the local convention.

### 3.4 Particles and sentence-final words

`[U2]`. These carry most of the "sounds Taiwanese" effect. Over-use makes a persona sound childish or fake; under-use sounds translated. Calibrate per persona age and tone; the reviewer decides.

| Particle | Function | Example (zh-TW) | Register note |
|---|---|---|---|
| 喔 | Soft, friendly reminder | 「記得先收藏喔」 | Taiwan-typical; mainland writes 哦 more |
| 啦 | Casual emphasis or reassurance | 「沒那麼難啦」 | Frequent in Taiwan speech; avoid in formal or 您 voice |
| 耶 | Delight, surprise, agreement | 「這個版型好好看耶」 (a statement about the design, not a use claim) | Strongly Taiwan-coded |
| 欸 | Attention getter, "hey" | 「欸，你看這張尺寸表」 | Young, casual |
| 囉 | Signals "here it comes" or new information | 「這週的整理來囉」 | Friendly; Taiwan-coded |
| 齁 | "See, I told you" (from Hokkien) | 「齁，這就是重點」 | Playful; use sparingly |
| 蛤 | "Huh?" (from Hokkien) | 「蛤？真的假的？」 | Casual; fine for reactions |
| 吧 / 嘛 / 啊 / 呢 | Standard Mandarin softeners | | Safe |
| ～ (full-width tilde) | Lengthens and softens | 「好喔～」 | Normal in captions and chats |

**Taiwan-coded sentence patterns** `[U2]`: 「有 + verb」 (我有看到; but for personas, in a non-experience sense only), 「超 + adjective」 (超實用), 「蠻 / 滿 + adjective」 (a milder "quite", where mainland writers often say 挺), 「真的假的」, 「對不對」, 「是不是」, 「有夠 + adjective」 (from Hokkien, casual). Avoid the stiff 「此外」「因此」「總而言之」 chains.

### 3.5 Taiwanese Hokkien (台語) and Hakka (客語) touches

`[U2]`. Taiwan is multilingual, and light use of 台語 or 客語 can add warmth, but the operator cannot judge pronunciation or taste, and a virtual character that "performs" a regional identity can read as stage dialect. **Rule for this studio: only use items the reviewer approves one by one; never invent Han characters for Hokkien sounds.**

| Language | Safe, widely understood touches | Avoid |
|---|---|---|
| 台語 (Hokkien) | 歹勢 (pháinn-sè, sorry / excuse me), 多謝 (to-siā, thanks), 呷飽沒 (have you eaten?), 古錐 (kóo-tsui, cute), 好家在 (lucky it turned out OK), 阿嬤 / 阿公 (grandma / grandpa), 有夠 (very) | Vulgar words (幹, 靠北, 三小, 機掰), insults (北七), invented characters, long stretches of 台語 text |
| 客語 (Hakka) | 恁仔細 (thanks; Sixian Hakka), Hakka foods such as 擂茶, 粄, 客家小炒, festivals such as 桐花祭 (April to May) and 義民節 (lunar 7/20: 2026-09-01, 2027-08-21) [C1] | Using Hakka floral cloth (客家花布) as a generic "Taiwan" motif without understanding; mixing Hokkien and Hakka as if the same |

For spelling Hokkien in Han characters, the Ministry of Education publishes recommended characters (臺灣閩南語推薦用字); ask the reviewer to use those or the romanisation (台羅) instead of guessing. The Hakka Affairs Council (客家委員會) is the authority for Hakka material. Both authorities' pages were not accessible, so the exact resources are `unverified`.

### 3.6 Bopomofo (注音文) and 火星文

`[U2]`. 注音文 means writing a Mandarin word with only its first bopomofo symbol, for example:

| Written | Stands for | Register |
|---|---|---|
| ㄅㄅ | 掰掰 (bye-bye) | cute, chat |
| ㄏㄏ | 呵呵 / 哈哈 | chat |
| ㄉ | 的 | chat |
| ㄛ / ㄚ / ㄟ | 喔 / 啊 / 欸 | chat |
| ㄇㄉ | 媽的 | mild profanity: avoid |

`[U2]` is medium confidence for the whole table; the reviewer should confirm. Notes: 注音文 and its older cousin 火星文 (character substitution style of the mid-2000s) peaked in the 2000s and 2010s, so heavy use now looks dated or ironic. It is allowed only as a rare cute touch for a young persona, never in brand-facing copy. Bopomofo characters also appear as a design motif (stationery, tote bags); image models often mix them with random symbols, so check any bopomofo on an image.

### 3.7 Emoji, text emoticons and meme habits

`[U2]`. Emoji are shown by name.

| Habit | Detail |
|---|---|
| Moderation | 1 to 3 emoji per caption is typical for brand-like voices; spamming a whole row reads as "小編" (admin) energy |
| Commonly seen in Taiwan casual text | face with tears of joy, loudly crying face (used for laughter or "I'm moved"), pleading face, folded hands (thanks or "please"), sparkles, red heart, pointing-down (to a link or menu), check mark (lists) |
| Text emoticons | XD, XDD, QQ (crying), orz (kneeling), ^^, >< ; Japanese-style kaomoji are common among young users |
| Avoid | Bracketed WeChat codes (「[微笑]」), and the slightly sinister reading some young users give the plain smiling face |
| LINE stickers (貼圖) | Stickers, not emoji, are the main chat expression in LINE; 60 million are sent a day [S5]. A persona's own sticker set is also a revenue route (see `monetisation.md`) |
| 長輩圖 (greeting images) | Sunrise or flower pictures with 「早安」 and a blessing, shared in family LINE groups; a recognisable format for 45+ audiences |
| Meme formats | Reaction images, screenshot memes, 「一張圖看懂」 infographics, POV videos, poll debates. Formats that need personal experience are barred for personas (2.3) |

**Cute-character culture** `[U2]`: Taiwan audiences are heavy consumers of character goods and stickers (LINE FRIENDS, Sanrio, Chiikawa, 7-ELEVEN's OPEN將, with more than 10 million cumulative sticker downloads according to a 7-ELEVEN statement, date not shown [S30]). That supports a character-first, stylised design (section 6), and also means copying any existing character is a real risk, which Ground rule 2 already covers [B1].

### 3.8 Slang and meme formats for 2025 to 2026: watchlist only

**Status: unverified.** I could not check any term against a 2025-2026 source (section 0). The table lists terms I know circulated in Taiwan up to about mid-2026 `[U3]`. For each, the reviewer should mark **live / dated / cringe-if-used-by-a-brand**. Slang ages fast; a term can turn from charming to cringe within a year, and brands using it too late are mocked.

| Term | Rough meaning | Era (my recall) | Notes for personas |
|---|---|---|---|
| 母湯 (m-thang, from Hokkien) | "not allowed, no way" | popular as a meme around 2018 | Probably dated; reviewer call |
| 小確幸 | small, certain happiness | since the mid-2000s | Stable and safe |
| 社死 | "social death", mortification | about 2019 on | Stable |
| 擺爛 | give up trying, let it rot (Hokkien-influenced) | about 2022 on | Has been used in political contexts; avoid |
| 傻眼貓咪 | "dumbfounded cat" reaction meme | 2020s | Probably understood; reviewer call |
| 母胎單身 | single since birth (Korean-origin) | about 2019 on | Relationship humour only |
| 天菜 | "dream type", very attractive person | 2010s on | Can objectify; avoid |
| 笑死, 真的假的, 蛤, 超, 爆, 有夠, 厭世 | reactions and intensifiers | stable | Safe building blocks |
| 小丑 / 我是小丑 | self-deprecating "I'm the clown" | 2020s | Casual |
| 手滑, 衝一波 | impulse-buy jokes | 2020s e-commerce | Persona may not claim to have bought anything |
| 酸民, 鄉民, 炎上, 洗版 | netizen words from the PTT era | stable | Useful for listening, not for persona voice |
| 懶人包, CP值, 口袋名單 | content and shopping words | stable | Safe and useful |
| 北部粽 vs 南部粽; 鹹豆花 vs 甜豆花 | perennial food-debate formats | stable annual cycles | Good poll fodder, especially around 端午 |
| Character-merch crazes (Chiikawa, Labubu) | collectible hype | 2024 to 2025 (my recall) | Context only; do not reference without checking currency |

**Process to refresh this table every week (assumption: fits the Phase 5 trend-check routine)**, using only free official or public sources and no login-based scraping [B1]:
1. The reviewer reads the Dcard popular board and Threads search for the persona's topic and notes new phrases (2 to 3 per week). Manual reading by a human only: no automated collection, and nothing behind a login that automation would have to bypass [B1].
2. Check Google Trends for Taiwan and the TikTok Creative Center (Taiwan region) trend pages for sounds and hashtags. Both are public pages; I did not open them this session.
3. In December, scan the year-end lists that Taiwan media publish (portal "year in search" lists, annual character or word selections). I did not verify their schedules or results.

---

## 4. Commercial calendar, 2026-10 to 2027-12

### 4.1 Method and the near-midnight edge case

- **Lunar festivals and solar terms are computed** `[C1][C2][C4]`: I installed the pure-Python `lunardate` 0.3.0 library (table-based, 1900 to 2100) and converted each lunar date. I then wrote an independent check from first principles (new moon times by the Meeus method, and the Sun's apparent longitude for solar terms), evaluated in UTC+8. All lunar-month starts agreed with the library. There is no leap month in lunar years 2026 or 2027 `[C1]`.
- **Edge case:** the new moon that starts lunar year 2027 falls at about 23:56 on 2027-02-06 in UTC+8, only minutes before midnight, so the first day of the lunar year depends on a fine-grained moon calculation `[C2]`. Both calculations give Sat 2027-02-06, and this matches the widely published date, but confirm with the Taiwan government almanac when it is available. A second near-midnight case is the new moon at about 23:50 on 2026-10-10, which starts lunar month 9 and therefore fixes 重陽 (lunar 9/9) at Sun 2026-10-18; had the moon fallen after midnight, 重陽 would be Mon 2026-10-19. Both calculations agree on the earlier date, but treat 重陽 2026 as `medium` until checked against the almanac.
- **Weekdays and rule-based Gregorian dates** (second Sunday of May, fourth Thursday of November) are computed `[C3]`; whether a festival *follows that rule* in Taiwan is `[U6]` where noted.
- **Official holiday lengths and make-up days (補假, 補班) are not verified.** The 2027 Directorate-General of Personnel Administration (行政院人事行政總處) calendar was not accessible. 4.6 states the standing rules I recall and what to check.
- Taiwan uses UTC+8 for these calculations; the lunar calendar is the Chinese calendar as published in Taiwan.

### 4.2 Table A: lunar-calendar festivals and solar terms (computed)

`[C1][C2][C4]`; dates in bold fall inside the 2026-10 to 2027-12 planning window.

| Event (zh-TW) | Rule | 2026 | 2027 | Commercial or cultural note |
|---|---|---|---|---|
| 除夕 (New Year's Eve, reunion dinner 圍爐) | day before 初一 | Mon 2026-02-16 (past) | **Fri 2027-02-05** (lunar 12/29; the 2026 lunar year has no 12/30) | 年菜 pre-orders, family content |
| 農曆新年 初一 | lunar 1/1 | Tue 2026-02-17 (past) | **Sat 2027-02-06**; 丁未 / goat year [C5] | New clothes and red are customary [U16] |
| 初二 (married daughters visit their parents' home, 回娘家) | lunar 1/2 | | Sun 2027-02-07 | [U9] |
| 初三 | lunar 1/3 | | Mon 2027-02-08 | Traditionally a day to stay in and avoid visiting [U9] |
| 初五 (back to work, 開工, welcoming the wealth god) | lunar 1/5 | | Wed 2027-02-10 | Business start-of-year content [U9] |
| 初九 天公生 (Jade Emperor's birthday) | lunar 1/9 | | **Sun 2027-02-14, same day as Valentine's Day** | Religious observance (offerings the night before); avoid joking on it [U9] |
| 元宵 / 上元 (Lantern Festival) | lunar 1/15 | Tue 2026-03-03 | **Sat 2027-02-20** | Lanterns, 湯圓. Tainan's 鹽水蜂炮 runs around lunar 1/14 to 1/15 (2027-02-19 to 02-20) [U14] |
| 頭牙 (lunar 2/2, earth god) | lunar 2/2 | | Tue 2027-03-09 | Traditional business-owner offering day [U9] |
| 清明 (solar term, tomb-sweeping) | Sun at 15 degrees | Sun 2026-04-05 (about 02:34) | **Mon 2027-04-05** (about 08:13) | Grave-sweeping; respectful tone [C4] |
| 媽祖誕辰 (lunar 3/23) | lunar 3/23 | Sat 2026-05-09 | Thu 2027-04-29 | Major folk-religion season; pilgrimage dates not checked [U9] |
| 端午 (Dragon Boat) | lunar 5/5 | Fri 2026-06-19 | **Wed 2027-06-09** | 粽子, dragon boats. Annual 北部粽 vs 南部粽 debate |
| 七夕 | lunar 7/7 | Wed 2026-08-19 | **Sun 2027-08-08** | Taiwan's second Valentine's day; coincides with 父親節 in 2027 |
| 鬼月 (ghost month) | lunar 7/1 to month end | 2026-08-13 to 2026-09-10 (29 days; ended) | **2027-08-02 to 2027-08-31** (30 days) | Sensitive period (5.4) |
| 中元節 (Ghost Festival) | lunar 7/15 | Thu 2026-08-27 | **Mon 2027-08-16** | Offerings (普渡). Do not market on the day |
| 義民節 (Hakka) | lunar 7/20 | Tue 2026-09-01 | Sat 2027-08-21 | Hakka religious observance, inside ghost month [U2] |
| 中秋 (Mid-Autumn) | lunar 8/15 | Fri 2026-09-25 (past) | **Wed 2027-09-15** | 烤肉 (barbecue) tradition, mooncakes, pomelo |
| 重陽 / 敬老節 | lunar 9/9 | **Sun 2026-10-18** | Fri 2027-10-08 | Senior Citizens' Day in Taiwan [U9] |
| 冬至 (solar term) | Sun at 270 degrees | **Tue 2026-12-22** (about 04:46) | Wed 2027-12-22 (about 10:39) | Eating 湯圓 [C4][U9] |
| 尾牙 (year-end company banquet) | traditional date lunar 12/16 | Tue 2026-02-03 (for lunar year 2025) | **Sat 2027-01-23** (lunar year 2026) | Companies hold them in January and February [U9] |
| 小年 (kitchen god sent off) | lunar 12/24 | Wed 2026-02-11 | Sun 2027-01-31 | Starts the final New Year preparations [U9] |
| Next lunar new year | lunar 1/1 | | Wed 2028-01-26 (除夕 Tue 2028-01-25) | Look-ahead for 2027 Q4 planning |

### 4.3 Table B: fixed-date and rule-based Gregorian events (weekday computed)

`[C3]`; "Taiwan relevance" is `[U6]` or `[U7]` unless noted.

| Event | Rule | 2026 | 2027 | Note |
|---|---|---|---|---|
| 元旦 / 開國紀念日, 跨年 (countdown on 12-31) | Jan 1; Dec 31 | Thu 2026-12-31 → **Fri 2027-01-01** | Fri 2027-12-31 | 跨年 concerts and fireworks; party and fashion peak |
| 情人節 | Feb 14 | Sat | **Sun 2027-02-14** (also 初九, in the New Year week) | Flowers, chocolate, dinners |
| 228 和平紀念日 | Feb 28 | Sat | **Sun 2027-02-28** | Solemn; no promotion (5.1) |
| 白色情人節 | Mar 14 | Sat | Sun | Observed in Taiwan [U6] |
| 青年節 / 先賢先烈紀念日 | Mar 29 | Sun | Mon | Holiday status after the 2025 amendment: unverified [U6] |
| 兒童節 | Apr 4 | Sat | Sun 2027-04-04 (day before 清明) | Often combined with 清明 into a long weekend |
| 勞動節 | May 1 | Fri | Sat | Holiday for all workers since 2025 (recalled) [U6] |
| 母親節 | second Sunday of May | Sun 2026-05-10 | **Sun 2027-05-09** | Restaurants, cakes, jewellery, bags |
| 520 (「我愛你」 date) | May 20 | Wed | Thu | Also the presidential inauguration date in 2016, 2020 and 2024; none in 2027. Keep away from political overtones [U12] |
| 618 | Jun 18 | Thu | Fri 2027-06-18 | Mid-year sale (4.4) |
| 父親節 | Aug 8 | Sat | **Sun 2027-08-08 (same day as 七夕)** | |
| 開學 (back to school) | about Sept 1 | | | Elementary to senior high start around 1 September; universities mid-September. Exact dates unverified [U6] |
| 教師節 | Sep 28 | Mon | Tue | Holiday status after 2025 amendment: unverified [U6] |
| 雙十 / 國慶日 | Oct 10 | **Sat 2026-10-10 (today)** | Sun | National Day. Political; do not tie promotions to it |
| 光復節 | Oct 25 | Sun | Mon | Holiday status after 2025 amendment: unverified [U6] |
| 萬聖節 (Halloween) | Oct 31 | Sat | Sun | Costume events; retail theme |
| 雙11 (11.11) | Nov 11 | **Wed 2026-11-11** | Thu | Biggest online sale (4.4) |
| 黑色星期五 (Black Friday) | day after fourth Thursday of Nov | **Fri 2026-11-27** | Fri 2027-11-26 | Cross-border and local promos |
| 雙12 (12.12) | Dec 12 | **Sat 2026-12-12** | Sun | Second-wave online sale |
| 聖誕節 / 行憲紀念日 | Dec 25 | **Fri 2026-12-25** | Sat 2027-12-25 | Retail event; gift-exchange parties; also a holiday after the 2025 amendment (unverified) [U6] |
| Double-date shopping days: 9.9, 10.10 | Sep 9, Oct 10 | Wed, Sat | Thu, Sun | E-commerce campaign dates (4.4) |

### 4.4 Table C: retail and e-commerce campaigns (dates not verified)

None of these windows were verified; each needs checking on the organiser's own site or app before any plan depends on it. `[U7]`

| Campaign | What I recall | 2026-2027 dates | Where to verify | Relevance |
|---|---|---|---|---|
| 週年慶 (department-store anniversary sales: Shin Kong Mitsukoshi, SOGO, Far Eastern, Breeze, Taipei 101 and others) | The big autumn round usually runs from mid or late October into November; chains set their own windows; some chains also hold a spring round | **Not found** for autumn 2026 (it is running or about to run) | Each chain's official site and app | Fashion, beauty, gifts; as I recall, the biggest offline fashion sales period |
| 618 | Mid-year online sale (momo, PChome and others) | Fri 2027-06-18 is the date; campaign window not found | Platform sites | Mid-year fashion and gear |
| 蝦皮 (Shopee) double-date campaigns | A campaign on each double-date such as 9.9, 10.10, 11.11, 12.12 | Dates follow the double-date rule; terms not found | Shopee Taiwan campaign pages | Affiliate route in `monetisation.md` |
| 雙11 | Taiwan's largest online shopping festival | Wed 2026-11-11 [C3]; platform mechanics not found | Platform sites | Price-comparison explainers; no unverified price claims |
| 年貨 / 福袋 (lucky bags) | New Year goods and lucky bags sell in the weeks before 農曆新年; apparel lucky bags are a Taiwan tradition | About mid-January 2027 on; not found | Retailer sites | In May 2026 a customer allegedly used an AI image to claim a mouse was in a lucky-bag parcel from the apparel brand ALT [S20]: keep lucky-bag content strictly factual |
| 母親節檔期 | Late April to the Sunday | Sun 2027-05-09 [C3] | | Gift guides, restaurants |
| 開學季 | Mid-August to mid-September | Dates not found | Education ministry and school sites | Bags, shoes, phones |

### 4.5 Table D: niche-specific peaks, with compliance guardrails

"Peak" timings are `[U7][U8][U16]` (recalled, not measured). Hooks are written to stay inside Ground rule 6 [B1].

**Fitness-education niche (technique, gear, programme structure; no health, medical or weight-loss claims)**

| Peak | Approximate timing | Compliant hook | Do not |
|---|---|---|---|
| New Year resolutions | December to February; 跨年 on 2026-12-31, 元旦 2027-01-01 | 「新手第一週課表範例（一般資訊）」「動作要點」 (programme samples edge toward health advice: keep to structure and technique, no outcome or injury claims, and have `legal.md` confirm) | 瘦身, 減脂, 體態 transformation promises, weight-loss numbers |
| Post-New Year return to routine | After 初五 (2027-02-10) and 元宵 (2027-02-20) | 「回到日常作息」 routine and habit-planning explainers | Guilt-based 「年後吃太多」 hooks (body shaming) |
| Gear sales | 雙11 (2026-11-11), 雙12, 618, 週年慶 | Neutral spec comparison tables of racks, bands, shoes | Claiming to have tested the gear |
| Cooler-season outdoor exercise and road running | Roughly autumn to early spring; event dates not checked | Gear and route-planning information | Medical advice, injury treatment |
| 敬老節 (2026-10-18, 2027-10-08) | Fixed dates | Family and seniors' activity themes | Any health-benefit claim |

**Fashion niche**

| Peak | Approximate timing | Compliant hook | Do not |
|---|---|---|---|
| Season changes and temperature swings | Autumn change; cold fronts from the northeast monsoon (東北季風) bring coat shopping, roughly late October to December [U16] | Layering logic (洋蔥式穿搭), fabric and fit explainers | 「顯瘦」「遮肉」 body-shaming language; "I wore it" |
| 週年慶 | Autumn 2026 (dates not found) | Lookbook-style "how to read a sale" explainers | Pricing or discount claims without a source |
| 跨年 / 聖誕 / 尾牙 outfits | Dec 2026 to Jan 2027 | Occasion dress-code explainers | White head-to-toe or black head-to-toe for celebrations (5.5) |
| 農曆新年 | 2027-02-06 | Red and festive colour palettes; "new clothes for the New Year" is a custom [U16] | Red used in mourning contexts |
| Spring and summer collections, 梅雨 (plum rain, about May to June) | Feb to Jun | Rain-ready outfit logic | |
| 618, 畢業季 (graduation season, June) | June 2027 | Graduation outfit explainers | |
| Wedding season | Autumn to winter; couples avoid the ghost month | Guest dress-code etiquette (avoid all-white and all-black) | Wedding advice presented as personal experience |

**Money-literacy niche (budgeting and process explainers only; no investment or financial advice [B1])**

| Peak | Timing | Compliant hook | Do not |
|---|---|---|---|
| 年終獎金 (year-end bonus) | Usually paid before 農曆新年: January 2027 for the 2027-02-06 New Year [U8] | Budgeting-framework explainers (not "what to buy") | Naming investments, funds, or yields |
| 紅包 and family-gift budgeting | December to February | Neutral budgeting explainers | Specifying amounts as advice |
| 牌照稅 (vehicle licence tax) | April | Process explainers sourced only from government pages | Tax advice |
| 綜合所得稅 filing (報稅) | Annual filing period 1 to 31 May (so 2027-05-01 Sat to 2027-05-31 Mon) [U8] | "Steps of filing" explainers paraphrased from, and linked to, Ministry of Finance (財政部) pages (do not copy text verbatim; check the site's reuse terms) | Tax-saving tips |
| 房屋稅 | May | Process explainers | |
| 地價稅 | November (2026-11-01 to 2026-11-30) | Process explainers | |
| 統一發票 (receipt lottery) draws | 25th of every odd month: 2026-11-25 Wed, 2027-01-25 Mon, 2027-03-25 Thu, 2027-05-25 Tue, 2027-07-25 Sun, 2027-09-25 Sat, 2027-11-25 Thu [C3][U8] | E-invoice and 載具 (carrier) how-to | Treat as a game or gambling frame |
| Scam-awareness | Any time; heavier around 雙11 and 農曆新年 | Pointing to the 165 anti-fraud hotline (反詐騙諮詢專線) [U8] | Specific fraud accusations |

Important cultural context for this niche: the biggest mainstream personal-finance conversation in Taiwan is 存股 (buy-and-hold investing, ETFs) [U8]. That is exactly what Ground rule 6 forbids [B1]. The compliant money-literacy angle therefore ignores the main audience interest, and the 2026 environment of deepfake investment scams using officials' faces [S32] makes an AI face talking about money start with a trust deficit.

### 4.6 Public-holiday mechanics, and a rolling 15-month view

**Mechanics (recalled; verify on the Directorate-General of Personnel Administration calendar, 行政院人事行政總處 辦公日曆表).** `[U6]`
- A national holiday on a Saturday normally gives a Friday make-up day off (補假); on a Sunday, a Monday make-up day. Special dates (農曆春節, 端午, 中秋) are often given adjusted long weekends with make-up working days (補班) on Saturdays.
- I recall that a 2025 amendment added days off for 3/29, 9/28, 10/25 and 12/25 and extended 勞動節 to all workers. This is **unverified**.
- **Likely consequences (unverified):** 228 on Sunday 2027-02-28 → Monday 2027-03-01; 雙十 on Saturday 2026-10-10 → Friday 2026-10-09; 光復節 on Sunday 2026-10-25 → Monday 2026-10-26; 雙十 on Sunday 2027-10-10 → Monday 2027-10-11.
- Long weekends change what content works (travel and leisure up, B2B down). **Plan holiday-dependent posting only after reading the official 2027 calendar.**

**Rolling view** (dates computed unless marked)

| Month | Dates (2026-10 to 2027-12) | Planning note |
|---|---|---|
| 2026-10 | 10/10 Sat 雙十 (today); 10/18 Sun 重陽; 10/25 Sun 光復節; 10/31 Sat Halloween and probable Pride date (5.7); 週年慶 running | Observe, build bibles; no brand deals yet (registration pending [B3]) |
| 2026-11 | 11/11 Wed 雙11; 11/25 invoice draw; 11/27 Fri Black Friday; 11/28 Sat local elections [U12] | Organic only; election quiet period |
| 2026-12 | 12/12 Sat 雙12; 12/22 Tue 冬至; 12/25 Fri 聖誕; 12/31 Thu 跨年 | First realistic seasonal content window |
| 2027-01 | 1/1 Fri 元旦; 1/23 Sat 尾牙; 1/31 Sun 小年; 年貨 and 年終獎金 | Fitness resolutions; money-literacy 年終 explainers |
| 2027-02 | 2/5 Fri 除夕; 2/6 Sat 初一; 2/10 Wed 初五; 2/14 Sun 情人節 and 天公生; 2/20 Sat 元宵; 2/28 Sun 228 | Plan a quiet 除夕 to 初三; no jokes on 228 |
| 2027-03 | 3/1 Mon probable 228 make-up day; 3/9 頭牙; 3/14 Sun 白色情人節; 3/29 Mon | Spring fashion |
| 2027-04 | 4/4 Sun 兒童節; 4/5 Mon 清明; 4/29 Thu 媽祖誕辰; 牌照稅 | Respectful tone on 清明 |
| 2027-05 | 5/1 Sat 勞動節 and 報稅 start; 5/9 Sun 母親節; 5/20 Thu 520 | Gift guides; tax process explainers |
| 2027-06 | 6/9 Wed 端午; 6/18 Fri 618; graduations | 粽子 poll formats |
| 2027-07 | Summer vacation; typhoon season [U16] | Weather-sensitive posting |
| 2027-08 | **鬼月 from 8/2 Mon**; 8/8 Sun 父親節 and 七夕; 8/16 Mon 中元節; 8/21 Sat 義民節 | No launches or big campaigns in the ghost month |
| 2027-09 | 開學; 9/9 Thu; 9/15 Wed 中秋; 9/28 Tue 教師節 | BBQ and mooncake content |
| 2027-10 | 10/8 Fri 重陽; 10/10 Sun 雙十; 10/25 Mon 光復節; 10/30 Sat probable Pride date; 10/31 Sun Halloween | 週年慶 season |
| 2027-11 and 12 | 11/11 Thu 雙11; 11/26 Fri Black Friday; 12/12 Sun 雙12; 12/22 Wed 冬至; 12/25 Sat; 12/31 Fri | Q4 peaks again; 2028-01-26 is the next 農曆新年 |

**Assumption (not a finding):** content for a peak should clear the reviewer at least two weeks before it. Calibrate in the first 30 days.

---

## 5. Topics and imagery to avoid

Items in 5.1 follow from the brief's ground rules [B1]. The rest are cultural judgements `[U9][U10][U11][U12][U13][U15]` that the reviewer should confirm.

### 5.1 Hard no (ties to ground rules)

| Area | Avoid | Why | Safer approach |
|---|---|---|---|
| Politics and elections | Candidates, parties, voting, recalls, party colour palettes (blue, green, white combinations with slogans), national flags as props | Ground rule 6 [B1]; local elections as I recall on 2026-11-28 [U12] | Neutral colours; no election hooks; do not post on polling day |
| Cross-strait | Any mention of China-Taiwan relations, "unification", military, maps that show or omit territories, the PRC flag or red-star icons (a risk with image models) | Ground rule 6 [B1] | Keep locations to Taiwan; check generated maps and flags |
| 228 and the White Terror (白色恐怖) | Jokes, sales, puns, "long weekend deals" on or around Feb 28 | The anniversary of 1947 events is solemn [U12] | Skip posting on 228, or post only a neutral pause notice if the persona has a following |
| Health, weight loss, cosmetic efficacy | Any claim of body change, treatment, or product effect | Ground rule 6 [B1] and Taiwan advertising rules (`legal.md`) | Technique, gear, general information |
| Investment and financial advice | Stock, ETF, fund, crypto, forex picks; yield claims | Ground rule 6 [B1] | Budgeting-literacy and scam-awareness only |
| Gambling | Casino, betting, lottery-as-game | Ground rule 6 [B1] | Frame 統一發票 draws as a receipt how-to only |
| Minors | Anyone who looks under 18; school uniforms and student settings as a styling trope; content aimed at children | Ground rule 3 (25+) [B1]; Taiwan's age of majority is 18 since 2023-01-01 (recalled) [U15] | Adult, workplace and neighbourhood settings |

### 5.2 Topic table

| Topic | Avoid | Safe alternative |
|---|---|---|
| Religion | Treating deities as costume, jokes about 媽祖, 關公, 觀音; using incense, joss paper or altars as decor; showing people stepping on temple thresholds (門檻) | Neutral, respectful explainers of etiquette if the persona's niche calls for it; reviewer approval |
| Superstition | Dismissing or mocking beliefs; promoting fortune-telling or 算命 claims | Cultural-explainer tone without endorsing predictions |
| Identity | Mainland vs Taiwan identity quarrels; calling Taiwan a province or "中國台灣" | Use 台灣; avoid the topic |
| Language politics | Presenting 國語 / 普通話 / 華語 as a debate | Use 國語 or just Mandarin without comment |
| Disasters and anniversaries | Promotional tone around the 921 earthquake anniversary (1999-09-21), the 2024-04-03 Hualien earthquake, the 2021-04-02 Taroko train accident, typhoon or flood disasters [U12] | Pause scheduled promotions during an active disaster; keep a "pause switch" in the weekly routine |
| Death and funerals | Using funeral objects or imagery as decoration | See 5.5 |

### 5.3 Superstitions and gifting taboos

`[U9]`; widely known in Taiwan, still verify with the reviewer.

| Item | Taboo | Reason |
|---|---|---|
| 鐘 (clock) | Do not gift or feature as a gift | 送鐘 sounds like 送終 (attending a death) |
| 傘 (umbrella) | Do not gift, especially to couples | 傘 sounds like 散 (to part) |
| 梨 (pear) | Avoid gifting or sharing one to a couple | 梨 sounds like 離 (to leave) |
| 鞋 (shoes) | Be careful gifting to a partner | Implies walking away |
| 扇子 (fan), 剪刀 / 刀 (scissors, knives), 手帕 (handkerchief) | Avoid as gifts | Association with parting, cutting, or tears |
| Number 4 (四) | Avoid prices, quantities, floors or sets of four | 四 sounds like 死 (death) |
| Number 8 (八), 6 (六), 9 (九) | Lucky | 發, 順, 久 associations |
| Green hat (綠帽) | Do not gift or style a man with a green hat | 戴綠帽 means being cheated on |
| Chopsticks upright in rice | Do not depict | Resembles incense for the dead |
| White envelope (白包) | Funeral money; do not use white envelopes in festive imagery | Red envelopes (紅包) are for festive occasions |
| Chrysanthemum (菊花) bouquets | Avoid in celebration imagery | Used at funerals |

### 5.4 Ghost month (鬼月) rules for 2026 and 2027

`[C1][U9]`. Dates computed: 2026-08-13 to 2026-09-10 (ended); **2027-08-02 to 2027-08-31**, 中元節 on 2027-08-16. During the ghost month, many people avoid: moving house, weddings, buying cars or houses, launching a business, swimming, going out late at night, drying clothes outdoors overnight, whistling at night, and taking photos at haunted places. Brands often delay launches and avoid ghost-themed jokes on the day itself, and some do run respectful 普渡 (offering) content. For this studio:
- Do not launch accounts or start a new persona in the ghost month. **The 2026 ghost month is over, so launching from now is clear until 2027-08-02.**
- Do not post jokes about ghosts, haunted places, "scary stories" or horror imagery aimed at the persona's own niche.
- 普渡 or 中元 content only as respectful etiquette explainers, with reviewer approval.

### 5.5 Mourning colours and festive colour use

`[U9]`. White and black are the mourning colours in Taiwan, and red is avoided by mourning families. Therefore: no all-white or all-black outfits for festive or celebratory content (weddings, 農曆新年); no white flowers and chrysanthemums in celebration imagery; use red, gold and warm colours for 農曆新年. For weddings, guests usually avoid all-white (bride's colour) and all-black. During 清明 or a public tragedy, keep tone subdued.

### 5.6 Indigenous peoples (原住民族)

`[U10]`. Taiwan officially recognises 16 Indigenous peoples (Amis, Atayal, Paiwan, Bunun, Puyuma, Rukai, Tsou, Saisiyat, Yami / Tao, Thao, Kavalan, Truku, Sakizaya, Seediq, Hla'alua, Kanakanavu) and a separate group of Pingpu (平埔) peoples that I recall are not on the official list (their legal status has been contested and may have changed; unverified). Guidance:
- Use 原住民族 (not 山胞, 山地人 or 番). When referring to a specific people, name it (阿美族, 排灣族, ...).
- Patterns, clothing, names and designs of a specific people are cultural property; I recall the Act on Protection of Traditional Intellectual Creations of Indigenous Peoples (原住民族傳統智慧創作保護條例, enacted 2007) requires consent for commercial use of registered creations. **Treat any commercial use of Indigenous patterns or names as legal and ethical risk and ask a lawyer (add to `legal.md` questions).**
- Never give a persona an invented Indigenous identity, never use facial tattoos (such as Atayal 紋面) as an aesthetic, and never frame culture as costume or "exotic".
- Stereotypes to avoid: drinking jokes, "naturally good at singing and dancing" tropes.

### 5.7 LGBTQ+

`[U11]`. Taiwan legalised same-sex marriage on 2019-05-24 (recalled; first in Asia), and Taipei's Pride march (台灣同志遊行) is held in late October, normally the last Saturday (so probably 2026-10-31 and 2027-10-30; unverified). For personas:
- Be inclusive by default, and respectful in Pride month without rainbow-washing (rainbow imagery used only as a sales hook draws criticism).
- Use 同志 or LGBTQ+, 跨性別 (not 變性 or 人妖), 同性伴侶. Avoid 娘, 娘砲 and "gay best friend" tropes as jokes.
- Do not weigh in on legal or political debates about marriage or adoption (Ground rule 6 [B1]).

### 5.8 Other people-related sensitivities

| Topic | Guidance | Basis |
|---|---|---|
| Migrant workers and new residents | Use 移工 (not the older 外勞) and 新住民 (not 外籍新娘) | [U10] |
| Body image | Avoid 胖, 瘦, 顯瘦, 遮肉 as value words; no comparisons of bodies | Ground rule 6 and respect [B1] |
| Gender roles | Avoid in-law, marriage-pressure and "剩女" jokes | [U10] |
| Mental health | Do not joke about depression, self-harm or suicide; if a reply thread touches it, point to the 1925 helpline (安心專線, recalled) and do not give advice | [U10] |
| Age and elders | Avoid 老人 as an insult; 長輩 is respectful | [U10] |
| Disability | Do not use 智障, 殘廢 as insults | [U10] |
| Terminology for the mainland | When unavoidable, 中國 or 中國大陸. 祖國 and 內地 read as the mainland's own viewpoint; "大陸" alone is also common in Taiwan (e.g. 大陸委員會) but its tone varies by speaker, so the reviewer rules. The safest course is to avoid the subject | [U12] |

---

## 6. How Taiwanese audiences react to AI and virtual characters, and to disclosure

### 6.1 What the evidence shows

I found **no Taiwan-representative survey** of attitudes to disclosed AI influencers (section 0; `competitors.md` section 7 also found none). The signals below are the best available; most are press coverage and secondary reports.

| Signal | What it shows | Taiwan-specific? | Strength | Source |
|---|---|---|---|---|
| TVBS (headline dated 2026-06-23; the cited URL is a search-results page, not the article) and UDN reported the Guardian investigation into brands using realistic AI "customers"; the headline figure is that 70% could not tell real from fake (attributed to Which? data, second-hand) | Audiences cannot tell, and consumer groups call for mandatory AI labels | The coverage is Taiwanese, the data is UK | low | [S16] |
| 民視 AI news anchor, 2023: viewers praised the look but found lips and eyes unnatural; the NCC said it would write to the station | Visible artefacts draw criticism; regulators accept AI presenters when disclosed | Yes | medium | [S21] |
| IKEA Taiwan showroom AI family image, 2026-06-01: distorted hands, criticism on Threads | Taiwanese users spot and ridicule AI errors quickly | Yes | medium | [S19] |
| Life8 AI model dispute, July 2026: a real model said the brand's AI image copied his features; brand apologised | Likeness risk is live in Taiwan | Yes | medium | [S18] |
| Hootsuite 2026 as quoted in Taiwan press: one third of consumers say AI-made brand ads lower their purchase intent (primary report not read by anyone in this chain) | AI ads may reduce purchase intent | Global, second-hand | unverified | [S25] |
| NielsenIQ (Dec 2024): AI ads rated more annoying, boring and confusing | Same direction | Not Taiwan; vendor study | medium | [S24] |
| Kolr / iKala 2026: brands prize verifiable human creators | Agency view of authenticity as the scarce asset | Yes (agency) | medium | [S23] |
| Fair Trade Commission (2026-04-23): AI-using ads are now in its monitoring scope, illegal cases have been found, and mandatory AI disclosure is under evaluation | The regulator is moving toward AI disclosure; no virtual-endorser guidance yet | Yes | medium | [S31] |
| About 2,595 Taiwan VTubers (2024); Springfish states 1.8 million combined subscribers (company figure, mid-2025) and announced a Universal Music partnership on 2026-01-16; 7-ELEVEN states that its OPEN將 stickers passed 10 million downloads | Clearly stylised virtual characters are accepted and monetised | Yes | medium | [S28][S29][S30] |
| Southeast Asia six-market survey (N=6,000): mostly positive views of virtual influencers; Singapore most likely to find them "weird" | Regional acceptance of virtual influencers is mixed-positive | Not Taiwan | low | [S26] |
| A KOL Radar article cites a 2022 survey in which 58% follow at least one AI virtual influencer | Unclear source | Unclear | low | [S27] |
| Mia Zelu: disclosure buried behind "Read More" led to mass confusion and backlash (2025-07) | Buried disclosure fails | Not Taiwan | medium | [S22] |
| Taiwan fraud context: deepfake investment scams using officials' faces (August 2026); Meta was reportedly fined NT$5 million over undisclosed AI-generated personal images in ads (single-outlet report, decision date and legal basis unverified) | An AI face already triggers fraud associations | Yes | medium | [S32][S33] |
| Instagram "AI-generated profile" label and recommendation limit (announced 2026-08-31) | Platform pressure to disclose; Taiwan scope unconfirmed | Platform | medium (existence; reported by trade press, not re-opened) | [S8] |

### 6.2 What is missing

- A Taiwan survey on acceptance of AI influencers by age, gender or niche.
- Any experiment on disclosure placement or label wording in Taiwan.
- Data on reaction to photoreal versus stylised characters in Taiwan.
- Sentiment of the 18-24 and 25-34 audiences specifically toward AI characters.

### 6.3 Design implications (inference from the signals above)

1. **Character-first, not fake-human.** Taiwan's proven virtual successes are clearly stylised characters (VTubers, mascots, idols) [S28][S29][S30]. A stylised-but-polished look may also ease the Instagram label burden (the label rule targets "photorealistic" AI people [S8]) and portrait-right exposure (`platforms.md`, `legal.md`); this is inference, and Taiwan scope of the label is unconfirmed. Photoreal faces carry the highest trust deficit in finance and health-adjacent topics [S32].
2. **Disclosure in three places:** bio, first line of the caption, and an on-screen label on video, in addition to the platform label [S22][S8][S9][S10].
3. **Lean into the limitation.** 「我是 AI，所以我沒辦法真的吃、穿、試」 is more trusted than concealing it, and it neatly satisfies Ground rule 4.
4. **Quality bar over volume.** Ridicule for AI errors (hands, text) is fast and public [S19]. The native reviewer and the QA checklist (7.6) are not optional.
5. **No expert costumes.** Avoid doctor, trainer, adviser or "financial planner" looks and titles. An AI face talking about money already meets fraud associations [S32], and agencies say brands want verifiable humans [S23].
6. **Do not rely on global stats.** The 70% figure is UK data [S16].

### 6.4 Hypotheses to test in the first 6 weeks (labelled as hypotheses)

| # | Hypothesis | Measure |
|---|---|---|
| H1 | A stylised character earns more saves and shares per reach than a photoreal one | Saves, shares per reach, per persona |
| H2 | Open AI self-humour increases comments without lowering completion | Comments per reach; video completion |
| H3 | Stating "AI 虛擬角色" in the first 3 seconds does not reduce completion | Completion rate by video |
| H4 | Finance-adjacent and health-adjacent topics draw more "是真人嗎" or distrust comments | Reviewer tags comment sentiment weekly |

Terminology audiences use (reviewer to confirm): 虛擬網紅, 虛擬偶像, 虛擬角色, 虛擬人, 數位人, VTuber / 虛擬實況主, AI 網紅. The bio phrase in the brief, 「AI 虛擬角色」, is consistent with these [B1].

---

## 7. Recurring Taiwan visual settings and details generators get wrong

I did not run any image generator for this file. The "common errors" below combine general failure modes of text-to-image models (garbled text, wrong regional forms, default Korean or Japanese looks) with Taiwan-specific facts I recall `[U13]`. A mainland-China e-commerce report notes that AI product imagery can add details a real product lacks [S17]. **Test the actual tools in Phase 4 and record real failures here.**

### 7.1 Setting library

| Setting | Signature details to include | Typical generator errors | Reviewer check |
|---|---|---|---|
| **夜市 (night market)** | Rows of stalls with canopies, bare yellow bulbs, hanging banners; foods such as 雞排, 鹽酥雞, 蚵仔煎, 臭豆腐, 胡椒餅, 大腸包小腸, 豆花; game stalls (撈金魚, 彈珠, 射飛鏢); dense crowds with plastic bags of food; signboards in Traditional Chinese | Garbled or Simplified signs; neon in Japanese style; empty, tidy street; ramen or yakitori stalls | Read every sign |
| **捷運 (MRT)** | Taipei lines by colour: 文湖線 brown, 淡水信義線 red, 松山新店線 green, 中和新蘆線 orange, 板南線 blue, 環狀線 yellow, 機場捷運 purple; platform screen doors; station names in Chinese and English; EasyCard (悠遊卡) gates; priority seats (博愛座); no food or drink | Wrong line colours; made-up station names on maps; Tokyo or Seoul interior; LED destination text in nonsense characters | Match line colour to name |
| **便利商店 (7-ELEVEN, 全家 FamilyMart)** | Bright interior; hot-food counter with 關東煮 and 茶葉蛋; coffee machine (City Cafe at 7-ELEVEN, Let's Café at 全家); ibon / FamiPort kiosks; seating area; parcel pickup (超商取貨); chime on entry; 7-ELEVEN's red-orange-green stripes (the final "n" in the logo is lowercase), 全家 green-blue stripes | Japanese konbini layout or US-style; wrong logos; no seating area | Compare to a real store photo |
| **機車與街道 (scooters and streets)** | Traffic on the right; scooters in dense packs at red lights; helmets (open-face or three-quarter styles) are mandatory; rain ponchos; hook-turn waiting boxes (機車待轉區) and two-stage left turns on big roads; pedestrian signals with an animated walking figure and countdown; overhead cable tangles; bilingual street signs | Left-hand traffic or wrong steering side; riders without helmets; scooter with a front plate; plates with garbled text | Count helmets and check plate side |
| **騎樓 (arcade walkways) and 巷弄 (alleys)** | Covered arcades with parked scooters and shop goods; vertical shop signs; iron window grilles (鐵窗); rooftop water tanks (水塔); wiring; air-conditioner outdoor units | Western or Japanese storefronts; glass towers instead; tidy cables | Look for 騎樓 continuity |
| **廟宇 (temple)** | Swallowtail roof ridges (燕尾脊) with ceramic or cut-porcelain dragons and phoenixes; red lanterns; incense burner (香爐); gold-paper furnace (金爐); stone lions; door gods (門神); divination blocks (筊杯); vermilion and gold palette | A Japanese shrine (torii) or Beijing-style palace; mixed Buddhist and Taoist figures; wrong incense handling (hold with both hands) | Reviewer checks respect and accuracy |
| **咖啡廳 and 老屋 cafés** | Renovated old houses, hand-drip counters, wood and tile; chains such as Louisa Coffee (路易莎) and Starbucks; no time limits | Tokyo kissaten or Parisian default; garbled menu boards | Menu text |
| **早餐店 / 小吃店 / 手搖飲店** | Breakfast shop: 蛋餅, 蘿蔔糕, 鐵板麵, 豆漿, 紅茶 in plastic bags; bubble-tea shop: cup **sealed with film and pierced by a wide straw** (no dome lid), order sheets such as 微糖少冰 | Dome-lid cups; Western cafe pastries; wrong drink menus | Cup sealing; menu text |
| **住家 (home)** | Shoes off at the entrance with a shoe cabinet; tiled floors; rice cooker (電鍋); window grilles; balcony with washing machine and drying rack; split air-conditioner; 110V Type A or B sockets; fan | Western carpeted house with shoes on; wrong sockets; large kitchen island | Entrance and sockets |
| **運動場景 (gyms, parks)** | Municipal sports centres (運動中心), commercial gyms such as World Gym and Anytime Fitness; riverside parks (河濱公園) with cycle paths; morning park exercise by older adults | Generic Western gym with garbled equipment labels | Equipment labels; no body-transformation imagery |
| **商圈 and 百貨 (fashion)** | 西門町, 東區, 信義商圈, Taichung 一中街 and 逢甲, Kaohsiung 新堀江; department stores with Chinese floor directories; 週年慶 banners | Korean or Japanese street signs; Simplified signage | Floor directory text |
| **交通工具** | Yellow taxis (小黃); Taiwan Railways lunch boxes (台鐵便當); orange-white High Speed Rail; YouBike stations; delivery riders with pink or green bags (brand and market status in 2026 not checked) | Wrong bus or train liveries; right-hand-drive vehicles | Livery and signage |
| **市場 (wet market)** | Early-morning stalls, tarps, plastic crates; hand-written price tags; scooters nearby | Clean supermarket look | Price tags |

### 7.2 Text on images: the rule

**Do not let a generator render Chinese text.** Generate the picture without text, then add all text in post-production with a Taiwan-glyph font (Noto Sans TC or similar) [B2][U4]. Check every sign, label, menu and screen by eye, for Simplified, Japanese or Hong Kong forms, garbled strokes, mirrored characters, and wrong direction (vertical signs read top to bottom, right to left in older styles; modern horizontal signs read left to right).

### 7.3 Plates, maps and logos

- **Plates:** cars have front and rear plates, scooters have a rear plate only. Plate colours vary by vehicle class (white, green, yellow and red are all in use on scooters; reviewer to confirm); do not rely on memory for exact formats. **Never render a legible real plate**; use a plausible but fictional plate or crop it out `[U13]`.
- **Maps and station signs:** do not let an AI invent a MRT map. Use a real public map or leave blank.
- **Logos:** do not render real brand logos (7-ELEVEN, 全家, banks, department stores) as persona endorsements; background presence is fine, but a persona holding a brand's product implies an endorsement and may need permission and a sponsorship label (`legal.md`).

### 7.4 People, clothing and climate

`[U16]`. Taiwan is subtropical: hot, humid summers (sun-protective sleeves and umbrellas used for both sun and rain), a long damp cool season in the north, plum rains, and typhoons from about July to October. Image generators default to four-season scenes (maple leaves, heavy snow coats, Japanese autumn): wrong for most of Taiwan. Check that characters do not default to a generic "K-pop" or "Japanese idol" look; style references should be ordinary Taiwanese street fashion (a mix of Korean, Japanese and American influences). Avoid defaulting to kimono, hanbok or mainland-style hanfu / cheongsam unless the post is explicitly about them.

### 7.5 Neighbourhood notes (the task named Yilan, Taichung and Tainan)

`[U14]`. Light-touch, unverified, for the reviewer:

| Place | Recognisable ingredients | Cautions |
|---|---|---|
| **Taipei / New Taipei** | 101 and Xinyi district, 西門町, 大稻埕 and 迪化街 (New Year goods street), 士林夜市, 永康街, 九份 and 淡水 (New Taipei) | Do not assume every Taiwan scene is Taipei |
| **Yilan (宜蘭)** | Rice paddies and farmhouse villas on the 蘭陽平原, 礁溪 hot springs, 羅東夜市, 蘇澳 cold springs, 太平山, 龜山島 offshore, frequent rain | Landscape is greener and wetter than the Taipei basin |
| **Taichung (台中)** | 審計新村, 宮原眼科, 草悟道, 逢甲夜市, 第二市場, 高美濕地; the city is often called the home of bubble tea (the origin is disputed with Tainan) | Stylish, café-heavy, mild climate |
| **Tainan (台南)** | 赤崁樓, 安平, 神農街, 國華街, 孔廟; beef soup (牛肉湯), danzai noodles (擔仔麵), milkfish (虱目魚); dense old temples; slow-paced, heritage feel | Tainan reads "old capital"; avoid generic glass-city look |
| **Kaohsiung** | 駁二, 愛河, 蓮池潭, port and harbour | |
| **Hualien / Taitung / Nantou** | 太魯閣, 七星潭; 池上 rice fields; 日月潭, tea plantations | After the 2024-04-03 earthquake, keep tone respectful [U12] |

### 7.6 "Taiwan-ness" QA checklist (merge into `pipeline/qa-checklist.md`)

1. Every character on the image is Traditional, in a Taiwan-glyph form, and legible.
2. No garbled strokes, mirrored text or pseudo-characters.
3. No Simplified, Japanese or Hong Kong Cantonese characters.
4. No real brand logos used as an implied endorsement.
5. No legible real licence plate; plate side correct (scooters: rear only).
6. Driving side is right-hand traffic; steering wheel on the left.
7. Riders wear helmets; no bare-head scooter shots.
8. MRT line colours match names; no invented station maps.
9. Convenience store looks like 7-ELEVEN or 全家, with seating, a hot-food counter, and no foreign layouts.
10. Bubble-tea cup is film-sealed, not dome-lidded.
11. Temple scenes are accurate and respectful (no threshold stepping, correct incense holding, no mixing with Japanese shrines).
12. Home scenes: shoes off, tile floor, Type A/B sockets, window grilles.
13. Weather and clothing suit the season (no maples in Taipei in November).
14. People look locally plausible, not a default "idol" template; adult (25+) appearance [B1].
15. No red-star, PRC flag or political symbols; no party colours.
16. No funeral objects, white-and-black pairing, or number 4 in celebration imagery.
17. Caption and on-screen text use Taiwan vocabulary (3.1) and no experience words (2.3).
18. AI label and bio disclosure present; sponsorship flag set when needed [B1].
19. Calendar check: not a ghost-month launch, not 228, not during a disaster pause.
20. The scene is labelled as AI-generated, not as a place the persona visited.

---

## 8. Reviewer brief (hand this to a native Taiwanese reviewer)

Short enough for one page. Fill the bracketed fields before sending.

### 8.1 English version

**Who we are.** An independent studio running several openly-virtual, AI-generated characters for Taiwan audiences. Every character says in its bio that it is an AI character made by the studio. The operator is not fluent in Traditional Chinese, so we need you to review every post before it goes out.

**What you check on each post (caption, hashtags, on-image text, video script and subtitles):**
1. **Taiwan vocabulary.** No mainland terms (視頻, 質量, 信息, 博主, 軟件, 鼠標...), no Simplified characters, no Hong Kong or Japanese forms.
2. **Natural voice.** Reads like a Taiwanese person, not a translation. Particles (喔, 啦, 耶, 欸) are used lightly and suit the character.
3. **No personal-experience claims.** The characters are virtual and have not tried, worn, eaten or used anything. Flag 愛用, 回購, 開箱, 實測, 心得, 我今天..., or anything that sounds like testimony.
4. **Out-of-bounds content.** No health, medical, weight-loss or cosmetic-efficacy claims; no investment or financial advice; no gambling; no politics or cross-strait topics.
5. **Disclosure.** AI disclosure is present; sponsored posts say 業配 or 合作 clearly.
6. **Images and video.** Chinese text, signs, plates, MRT, convenience-store details look right and Taiwan-like; people look adult.
7. **Timing and taboos.** Not a bad moment (ghost month, 228, a disaster, mourning); no gift taboos; no number four or white-black pairings in a festive post.

**Reply format.** For each post: APPROVE / SMALL FIX (please edit directly) / REJECT, plus reason codes: V vocabulary, T tone, S script or font, E experience claim, R regulated topic, P politics or sensitive, D disclosure missing, X cultural or visual error, C timing.

**Please also tell us:** any slang that is dated or sounds like a brand trying too hard; anything that sounds robotic.

**Onboarding questions for you:** (1) Which platforms are you comfortable reviewing (Instagram, Threads, TikTok, YouTube, Facebook, LINE)? (2) Do you have experience in fitness, personal finance or fashion? (3) Are you comfortable judging 台語 or 客語 touches? (4) Please mark the vocabulary table and slang watchlist in this study as live / dated / wrong. (5) Typical turnaround and rate: [to be agreed].

### 8.2 zh-TW version (AI-drafted; the reviewer may correct it)

**我們是誰。** 我們是一個獨立的工作室，為台灣受眾經營數個「公開標示為 AI 虛擬角色」的帳號。每個角色的自介都會寫明它是由本工作室製作的 AI 角色。營運者的繁體中文不夠流利，所以每一篇貼文發出前，都需要請你把關。

**每篇貼文（文案、標籤、圖上文字、影片腳本與字幕）請檢查：**
1. **用詞是否為台灣用語**：有沒有中國大陸用語（視頻、質量、信息、博主、軟件、鼠標…）、簡體字、港式或日式字形。
2. **語氣是否自然**：像台灣人說話，不是翻譯腔；語助詞（喔、啦、耶、欸）用得適量，符合角色個性。
3. **有沒有親身經驗的說法**：虛擬角色沒有吃過、穿過、用過、試過任何東西。請標出「愛用、回購、開箱、實測、心得、我今天…」或任何像見證的句子。
4. **不能碰的內容**：不得出現醫療、減重、功效宣稱，不得有投資或理財建議、賭博、政治與兩岸話題。
5. **標示**：有沒有 AI 標示；業配或合作貼文是否清楚寫出「業配」或「合作」。
6. **圖片與影片**：圖上的中文字、招牌、車牌、捷運、超商細節是否正確、像台灣；人物看起來是否為成年人。
7. **時機與禁忌**：是否遇到不適合的時間（鬼月、228、災難、哀悼）；有沒有送禮禁忌、數字四，或在喜慶貼文中用全白、全黑。

**回覆格式。** 每篇請回覆：核准／小修（請直接修改）／退回，並附原因代碼：V 用詞、T 語氣、S 字形、E 親身經驗、R 受規範內容、P 政治或敏感、D 缺少標示、X 文化或視覺錯誤、C 時機。

**也請順手告訴我們**：哪些流行語已經過時、哪些用法聽起來像品牌在硬跟風、哪裡讀起來有機器人味。

**接案前想先請教你**：(1) 你願意審哪些平台（Instagram、Threads、TikTok、YouTube、Facebook、LINE）？(2) 你對健身、理財或時尚有沒有經驗？(3) 你是否適合判斷台語或客語的用法？(4) 請協助標記本研究中的用詞對照表與流行語清單：仍在用／過時／有誤。(5) 時效與酬勞：【待雙方約定】。

---

## 9. Where this research complicates the brief or the operator's niches

1. **Ground rule 4 versus the Taiwan content genre.** The words Taiwanese audiences expect in recommendations (愛用, 開箱, 實測, 踩雷, 心得) are all banned for personas. The 25-34 band, which `platforms.md` treats as the core commercial band, responds most to experience content (60.3%, MIC) [S1]. The persona must become an explainer and comparison character, which is a weaker lever. `platforms.md` reached the same conclusion.
2. **Fitness.** Taiwan's default fitness hooks (減脂, 瘦身, 體態, before-and-after) are exactly what Ground rule 6 bars. A compliant fitness persona has to build on technique, gear and structure, and cannot ride the "年後瘦身" or "夏天前瘦" cycles that drive demand.
3. **Wealth.** The dominant Taiwan finance conversation is 存股 and ETFs [U8]; the compliant angle is budgeting, process and scam-awareness explainers. That is a smaller audience, and an AI face on money starts at a trust deficit after the August 2026 deepfake investment scams [S32].
4. **Fashion.** The best-fit niche, but the vocabulary of fashion content (上身, 開箱, 顯瘦, 愛用) mostly claims use or body outcomes. Replace with fit, fabric and styling logic.
5. **Operator language gap.** Everything on Threads, Dcard and PTT depends on slang and tone that the operator cannot judge, and slang ages quickly. The reviewer becomes the quality gate and must be hired before any launch, and the reviewer's cost is not yet in the budget (DECISIONS Q1 [B3]). I found no Taiwan reviewer rate (not found), so do not size the budget until quotes are in hand.
6. **Timing.** 雙11 is 32 days away, and the business registration takes about two weeks [B3], so no brand-paid 雙11 content is realistic; the first sensible commercial window is the end-of-year to 農曆新年 period (2026-12 to 2027-02).
7. **Election window.** The local elections (as I recall, 2026-11-28 [U12]) fall in the first weeks of any launch; politics is barred anyway [B1], but the practical consequence is the colour palette and hooks.
8. **Brief section 4 says "TikTok, YouTube and Meta all require a label".** True (per `platforms.md`), but label placement in the caption and on-screen is also needed, because bio-only disclosure failed in practice [S22].
9. **The brief's "mainland phrasing gets called out fast"** is consistent with the culture evidence, but its example list is far from complete: see 3.1, 3.2, 3.3 for the full set, including the character-level traps that a machine converter produces.
10. **Xiaohongshu is blocked** [S7]. The discovery channel Taiwan fashion audiences used most is gone, which raises the importance of Instagram and Threads for the fashion niche.

---

## 10. Open questions and unverified items

| Item | Status | What would settle it |
|---|---|---|
| Whether any listed slang is live in 2026 | Not verified (section 3.8) | Reviewer scan of Threads and Dcard; Google Trends Taiwan; TikTok Creative Center |
| 2027 government holiday calendar and make-up days | Not found | Directorate-General of Personnel Administration (行政院人事行政總處) calendar |
| The 2025 holiday amendment (3/29, 9/28, 10/25, 12/25 holidays; 勞動節 for all) | Recalled only | DGPA notice; Ministry of Interior |
| Autumn 2026 and spring 2027 週年慶 dates by department store | Not found | Each chain's official site |
| 618, 蝦皮 and momo campaign dates and mechanics | Not found | Platform campaign pages |
| Taiwan 2026 local election date (recalled 2026-11-28) | Unverified | Central Election Commission (中央選舉委員會) |
| Taiwan Pride 2026 date (guess: Sat 2026-10-31) | Unverified | Organisers' site |
| 報稅 window (1 to 31 May), 牌照稅, 房屋稅, 地價稅 months; 統一發票 draw rule | Recalled | Ministry of Finance (財政部) |
| Taiwan survey on acceptance of disclosed AI influencers | None found | Commission a small survey, or ask agencies |
| Vocabulary table (110 pairs) and the "not confident" list | Recalled; reviewer sign-off needed | Native reviewer |
| Hokkien and Hakka items; bopomofo examples | Recalled; reviewer sign-off needed | Reviewer; MOE and Hakka Affairs Council resources |
| Indigenous-patterns law (consent for commercial use) | Recalled | A Taiwan lawyer; Council of Indigenous Peoples (原住民族委員會) |
| Plate colours and formats; MRT line details | Recalled | Photos and official transport sites |
| Native-reviewer rate and turnaround | Not found | Two or three quotes |
| Question for the lawyer list: do AI-generated scene depictions of real places or real shopfronts need any permission or label beyond the AI label? | Not researched | Add to the `legal.md` question list |

---

## Sources

All rows: date accessed 2026-10-10. **No page was opened in this session** (section 0). `[S#]` rows are second-hand: each is a source a sibling research file (`platforms.md`, `competitors.md`) reported from search summaries, with the sibling's own id shown. Confidence is carried over or lowered. `[C#]` rows are computations I ran. `[U#]` rows are recalled from training data and have no URL.

| id | claim supported | URL | date published (if known) | date accessed | confidence |
|---|---|---|---|---|---|
| B1 | Ground rules: openly virtual, original likeness, adults only, no invented experience, disclose paid relationships, no health or finance advice, no politics, no fake popularity, studio named in bio, official APIs only | /home/user/Taiwan-AI-Influencers/BRIEF.md section 3 | 2026-10-10 (project file) | 2026-10-10 | high (project requirement) |
| B2 | Language rules: Traditional Chinese as written in Taiwan; 影片 not 視頻, 品質 not 質量, 資訊 not 信息, 網紅 or 創作者 not 博主; generators garble characters or output Simplified | /home/user/Taiwan-AI-Influencers/BRIEF.md section 5 | 2026-10-10 (project file) | 2026-10-10 | high (project requirement) |
| B3 | Operator constraints: NT$5,000/month; 6 h/week; not good at Traditional Chinese so a native reviewer is needed on every post; no registered Taiwan business (about 2 weeks); niches health-fitness, wealth, fashion | /home/user/Taiwan-AI-Influencers/DECISIONS.md | 2026-10-10 (project file) | 2026-10-10 | high (project requirement) |
| S1 | MIC social survey: 18-24 Instagram 78%, Dcard 45.9%, Threads 44%; 25-34 Instagram 59.3%, Dcard 30.9%, Threads 28.4%; Threads 17.5%, Dcard 17.6%, PTT 17.1% overall; Facebook 79.4% of 45-54; PTT biggest share 35-44; experience-sharing conversion 52.5% (25-34: 60.3%); fieldwork Q4 2024, n=1,091, margin of error +/-3.0% (via platforms.md S5) | https://mic.iii.org.tw/news.aspx?id=744 | 2025-12-04 | 2026-10-10 | medium (platforms.md rated it high; page not re-opened by the author or the verifier) |
| S2 | NCC 2025 account ownership: LINE 98.2%, Facebook 82.4%, YouTube 68.6%, Instagram 47.8%; TikTok below 30% in this source (the 23.8% TikTok figure comes from S3; via platforms.md S2, where the verifier there downgraded it) | https://news.nextapple.com/life/20260116/B179FADDD8297A4BE6D2F4C22549D035 | 2026-01-16 | 2026-10-10 | medium (single outlet; not re-fetched) |
| S3 | TikTok watched by 47.5% overall and 72.5% of 16-25; 23.8% hold an account (via platforms.md S3) | https://focustaiwan.tw/culture/202601040012 | 2026-01-04 | 2026-10-10 | medium (not re-opened) |
| S4 | MIC video survey: 70.5% short-video users; YouTube Shorts 68.1%, Facebook Reels 58.4%, Instagram Reels 43.0%; YouTube for search and knowledge (via platforms.md S8) | https://money.udn.com/money/story/7307/9704523 ; https://wantrich.chinatimes.com/news/20260820900336-420501 | 2026-08-20 | 2026-10-10 | medium |
| S5 | LINE Taiwan: about 60 million stickers a day; Nielsen: 93% used in the past 7 days, about 14 opens a day (via platforms.md S10) | https://ec.ltn.com.tw/article/breakingnews/5511215 | 2025-06 | 2026-10-10 | medium |
| S6 | LINE VOOM Taiwan closed 2026-09-30 (via platforms.md S11) | https://www.ettoday.net/news/20260803/3212389.htm ; https://www.nownews.com/news/6878748 | 2026-08-03 | 2026-10-10 | medium (two outlets per platforms.md; not re-opened) |
| S7 | Xiaohongshu blocked in Taiwan from 2025-12-04 for a provisional year; over 3 million Taiwan users (via platforms.md S13); the verifier's own recollection of the 2025-12-04 announcement agrees, but this is not a live check | https://cna.com.tw/news/asoc/202512040238.aspx ; https://www.nownews.com/news/6761458 | 2025-12-04 | 2026-10-10 | medium |
| S8 | Instagram "AI-generated profile" label and recommendation limit; announced 2026-08-31; Taiwan scope unconfirmed (via platforms.md S27, S28) | https://techcrunch.com/2026/08/31/instagram-puts-new-limits-on-undisclosed-ai-profiles/ ; https://help.instagram.com/313829416281232/ | 2026-08-31 | 2026-10-10 | medium (existence, trade press; platforms.md found one uncorroborated US-only claim); unverified (Taiwan scope) |
| S9 | TikTok AI-content label rules; guidelines effective 2026-09-24 (via platforms.md S46) | https://www.tiktok.com/community-guidelines/en/integrity-authenticity ; https://www.tiktok.com/tns-inapp/pages/ai-generated-content | 2026-08-25 | 2026-10-10 | medium |
| S10 | YouTube realistic-synthetic-content disclosure and auto-labelling from May 2026 (via platforms.md S40) | https://support.google.com/youtube/answer/14328491 ; https://blog.youtube/news-and-events/improving-ai-labels-viewers-creators/ | 2026-05 | 2026-10-10 | medium |
| S11 | Dcard bans promotional and commercial posts; three violations bring a 7-day suspension (via platforms.md S54) | https://www.dcard.tw/f/announcement/p/234243656 ; https://www.dcard.tw/terms | 2025-01-13 | 2026-10-10 | medium |
| S12 | PTT controls and founder's statement on coordinated volume inflation (via platforms.md S26) | https://tfc-taiwan.org.tw/?p=105500 | 2022 | 2026-10-10 | low |
| S13 | Threads brand-voice and engagement-velocity commentary (via platforms.md S24) | https://www.cw.com.tw/article/5131412 ; https://www.managertoday.com.tw/articles/view/72894 | 2024-2026 | 2026-10-10 | low |
| S14 | Meta Community Standards: personal profiles created to represent a business or non-human entity count as fake accounts, so a persona on Facebook must be a Page (via platforms.md S34) | https://transparency.meta.com/policies/community-standards/inauthentic-behavior/ ; https://transparency.meta.com/policies/community-standards/authentic-identity-representation/ | n/k | 2026-10-10 | medium |
| S15 | Fair Trade Commission treats sponsored posts as endorsement advertising (薦證廣告); material connections must be disclosed (via platforms.md S52) | https://www.leeandli.com/TW/Newsletters/2501.htm | 2025-01 | 2026-10-10 | medium |
| S16 | TVBS headline (2026-06-23; the URL is a site-search page, the article itself was not found, competitors.md rated it low) and UDN coverage of the Guardian investigation into AI "customers"; 70% could not tell real from fake (attributed to Which? data; Guardian original not read); consumer groups call for AI labels (via competitors.md S1-S3) | https://news.tvbs.com.tw/news/searchresult/虛擬網紅/news ; https://udn.com/news/story/6812/9583886 | 2026-06-23 | 2026-10-10 | low |
| S17 | Mainland-China e-commerce report: AI product images can add details a real product lacks (via competitors.md S32) | https://www.worldjournal.com/wj/amp/story/121617/9062017 | n/k | 2026-10-10 | low |
| S18 | Life8 AI model likeness dispute, July 2026; Civil Code Art. 18 portrait-right commentary (via competitors.md S7) | https://oecd.ai/en/incidents/2026-07-18-2fa7 ; https://today.line.me/tw/v3/article/3NPozZP | about 2026-07-17/18 | 2026-10-10 | medium |
| S19 | IKEA Taiwan AI family image with distorted hands drew criticism on Threads, 2026-06-01 (via competitors.md S8) | https://unwire.hk/2026/06/01/ikea-taiwan-ai-image-zombie-hand-controversy/ai/ | 2026-06-01 | 2026-10-10 | medium |
| S20 | ALT apparel lucky-bag "mouse" case with an AI image, May 2026; NT$10 million claim (via competitors.md S9) | https://www.ettoday.net/news/20260511/3164208.htm | 2026-05 | 2026-10-10 | medium |
| S21 | Taiwan AI news presenters 2023: viewer reaction; NCC said it would write to the station; disclosure principle (via competitors.md S14) | https://technews.tw/?p=1086575 ; https://news.pts.org.tw/article/648630 | 2023-06 | 2026-10-10 | medium |
| S22 | Mia Zelu: disclosure behind "Read More" caused mass confusion (via competitors.md S45) | https://www.tennis.com/news/articles/ai-influencer-mia-zelu-went-viral-wimbledon-artificial-intelligence-social-media | 2025-07 | 2026-10-10 | medium |
| S23 | Kolr (iKala) 2026 AI marketing report: verifiable human creators framed as scarce (via competitors.md S51) | https://www.bnext.com.tw/article/90807/ikala_kolr_2026_04 | 2026-04 | 2026-10-10 | medium |
| S24 | NielsenIQ: AI ads rated more annoying, boring and confusing (via competitors.md S52) | https://nielseniq.com/global/en/news-center/2024/niq-research-uncovers-hidden-consumer-attitudes-toward-ai-generated-ads/ | 2024-12 | 2026-10-10 | medium (vendor study) |
| S25 | Hootsuite 2026 trends: one third say AI-made brand ads lower purchase intent, as quoted in 遠見 (primary report not read; competitors.md S37 marks the figure unverified) | https://www.gvm.com.tw/article/127642 | 2026-01-30 | 2026-10-10 | unverified |
| S26 | Southeast Asia six-market survey of virtual influencers (N=6,000); Singapore most likely to find them "weird" (via competitors.md S46) | https://www.tatlerasia.com/power-purpose/innovation/asian-ai-influencers | n/k | 2026-10-10 | low |
| S27 | A KOL Radar article citing a 2022 survey: 58% follow at least one AI virtual influencer, origin unspecified (via competitors.md S59) | https://www.kolr.ai/en/?p=19757 | 2024-06 | 2026-10-10 | low |
| S28 | About 2,595 Taiwan VTubers (2024); no Taiwan law specific to virtual personas (via competitors.md S28) | https://www.airitilibrary.com/Article/Detail/U0020-1101202518053100 | 2025 | 2026-10-10 | medium |
| S29 | Springfish (春魚創意): company-stated 1.8 million combined subscribers (4Gamers, mid-2025); Universal Music partnership for the mainstream debut of 極深空計畫 announced 2026-01-16 (via competitors.md S18, S19) | https://www.4gamers.com.tw/news/detail/72720/springfish-studio-vtuber-3d-live-concert-nexus ; https://www.setn.com/klist/352443 | 2025; 2026-01-16 | 2026-10-10 | medium (company-reported) |
| S30 | 7-ELEVEN OPEN將: more than 10 million cumulative LINE sticker downloads (7-ELEVEN statement, date not shown; via competitors.md S27) | https://www.setn.com/news/1594957 | n/k | 2026-10-10 | medium (company-stated) |
| S31 | Fair Trade Commission (2026-04-23): AI-using ads in monitoring scope, illegal cases found, mandatory AI disclosure under evaluation (via competitors.md S4) | https://technews.tw/2026/04/23/ftc-to-assess-mandatory-disclosure-rules-for-ai-ads/ | 2026-04-23 | 2026-10-10 | medium |
| S32 | Deepfake investment fraud using exchange officials' faces, August 2026 (via competitors.md S55) | https://www.cna.com.tw/news/afe/202608050308.aspx ; https://money.udn.com/money/story/5607/9690165 | 2026-08 | 2026-10-10 | medium |
| S33 | Meta reportedly fined NT$5 million by the Digital Industry Administration (數位產業署) over undisclosed AI-generated personal images in ads (single-source per platforms.md; a further NT$5 million for late takedown is also reported); decision date and article numbers unverified (via platforms.md S51) | https://www.cna.com.tw/news/afe/202609230333.aspx ; https://ec.ltn.com.tw/article/breakingnews/5583322 | 2026-09-23 (article date) | 2026-10-10 | medium (existence); unverified (details) |
| S34 | Press coverage of the MIC survey: Facebook used by about six in ten of 18-34s; 45+ core (via platforms.md S6) | https://money.udn.com/money/story/5613/9182136 | n/k | 2026-10-10 | medium (not re-opened) |
| C1 | Lunar-calendar dates 2026-2027 (農曆新年, 元宵, 端午, 七夕, 鬼月, 中元, 義民節, 中秋, 重陽, 尾牙, 小年, 媽祖誕辰 and others) computed with the `lunardate` 0.3.0 library, UTC+8; no leap month in lunar years 2026 or 2027 | https://pypi.org/project/lunardate/ (library used; computation run locally) | n/a | 2026-10-10 | high (arithmetic); medium until matched to Taiwan's government almanac |
| C2 | Independent cross-check: new moon times by the Meeus method (Astronomical Algorithms ch. 49) evaluated in UTC+8; all lunar-month starts matched; the new moon starting lunar year 2027 is about 23:56 on 2027-02-06 (4-minute margin); 2026-10-10 about 23:50 | local computation, no URL | n/a | 2026-10-10 | medium-high (re-run independently by the verifier with the Python `ephem` 4.2.1 astronomy library: see C6; the margin case matches the widely published 2027-02-06 date) |
| C3 | Weekdays and rule-based Gregorian dates (second Sunday of May, fourth Thursday of November, days-from-today counts) computed with Python `datetime` | local computation, no URL | n/a | 2026-10-10 | high (arithmetic); the rules themselves are in `[U6]` |
| C4 | Solar-term times in UTC+8: 清明 2026-04-05 about 02:34 and 2027-04-05 about 08:13; 冬至 2026-12-22 about 04:46 and 2027-12-22 about 10:39; 立春 2027-02-04 about 09:43 (times corrected by the verifier from the author's 02:28, 08:15, 04:49, 10:37; the minute values carry a few minutes' uncertainty, the calendar days do not) | local computation, no URL | n/a | 2026-10-10 | medium (days: high; minutes: low) |
| C5 | Sexagenary year: 2026 = 丙午 (horse), 2027 = 丁未 (goat / sheep, 羊), 2028 = 戊申 (monkey); computed from the 60-year cycle | local computation, no URL | n/a | 2026-10-10 | high |
| C6 | Verifier re-check on 2026-10-10: `lunardate` 0.3.0 library and `ephem` 4.2.1 (new moons and solar longitude, UTC+8) reproduce every lunar-calendar date in Table A (e.g. 2026-10-10 23:50:01 new moon; 2027-02-06 23:56:02 new moon; 初一 2027-02-06; 重陽 2026-10-18), and Python `datetime` reproduces every weekday and day-count in sections 1, 4.3, 4.5 and 4.6 | local computation, no URL (PyPI packages) | n/a | 2026-10-10 | high (arithmetic); the near-midnight cases remain a 4-minute margin, so confirm with the government almanac |
| U1 | Taiwan versus mainland vocabulary pairs and usage notes; "Taiwan-coded words" | no URL; linguistic knowledge (BRIEF names four pairs [B2]) | n/a | 2026-10-10 | unverified; reviewer sign-off |
| U2 | Particles, sentence patterns, 台語 and 客語 items, bopomofo (注音文) examples, emoji and meme habits, Hakka festival notes | no URL; recalled | n/a | 2026-10-10 | unverified; reviewer sign-off |
| U3 | Slang and meme watchlist and format-fit assessments (known to me up to about mid-2026; current status unknown) | no URL; recalled | n/a | 2026-10-10 | unverified |
| U4 | Simplified/Traditional converter traps, Taiwan glyph forms versus HK / JP forms, fonts, punctuation and numeral conventions | no URL; recalled (resources to check: Ministry of Education standard forms) | n/a | 2026-10-10 | unverified |
| U5 | Platform tone conventions on Instagram, Threads, TikTok, YouTube, Facebook, LINE, Dcard and PTT (practitioner knowledge; not measured) | no URL; recalled | n/a | 2026-10-10 | unverified |
| U6 | Public-holiday rules (make-up days), 2025 holiday additions, 勞動節, observance of 白色情人節, 開學 timing; DGPA 2027 calendar not seen | no URL; recalled (verify at https://www.dgpa.gov.tw). The verifier's own recollection agrees that a 2025 amendment added 3/29, 9/28, 10/25 and 12/25 as holidays and made 勞動節 a holiday for all, but that is not independent evidence | n/a | 2026-10-10 | unverified |
| U7 | Retail calendar: 週年慶 windows, 618, 蝦皮 double-date campaigns, 雙11, Black Friday, 年貨 and lucky bags | no URL; recalled | n/a | 2026-10-10 | unverified |
| U8 | Tax and civic calendar (報稅 1-31 May; 牌照稅 April; 房屋稅 May; 地價稅 November; 統一發票 draw on the 25th of odd months; 年終獎金 before 農曆新年; 存股 culture; 165 hotline) | no URL; recalled (verify at https://www.mof.gov.tw) | n/a | 2026-10-10 | unverified |
| U9 | Folk beliefs and custom: ghost-month practices, New Year day-by-day customs, gift taboos, number 4, mourning colours, wedding dress, 重陽 as Senior Citizens' Day | no URL; recalled | n/a | 2026-10-10 | unverified; reviewer sign-off |
| U10 | Indigenous peoples (16 recognised; 原住民族; traditional intellectual creations act of 2007), migrant workers and new residents terminology, body image, mental health, disability language | no URL; recalled | n/a | 2026-10-10 | unverified |
| U11 | LGBTQ+: marriage equality 2019-05-24; Pride in late October; terminology | no URL; recalled | n/a | 2026-10-10 | unverified |
| U12 | Politics and sensitive dates: 228; local elections 2026-11-28; 520 and the inauguration pattern; 921, 0403 and Taroko train accident anniversaries; cross-strait terminology | no URL; recalled (niches.md independently recalls "late November 2026"; the verifier also recalls Saturday 2026-11-28 for the nine-in-one local elections, but could not open the Central Election Commission site) | n/a | 2026-10-10 | unverified |
| U13 | Visual details: plates, MRT lines, convenience-store features, scooters, temples, interiors, street furniture, romanisation inconsistency | no URL; recalled | n/a | 2026-10-10 | unverified |
| U14 | Neighbourhood notes (Taipei, Yilan, Taichung, Tainan, Kaohsiung, Hualien, Taitung, Nantou); 鹽水蜂炮 timing | no URL; recalled | n/a | 2026-10-10 | unverified |
| U15 | Age of majority 18 since 2023-01-01; minors guidance | no URL; recalled | n/a | 2026-10-10 | unverified |
| U16 | Climate and seasonality: subtropical climate, plum rains (about May-June), typhoon season (about July-October), northeast monsoon cold fronts, New Year new-clothes custom, marathon season | no URL; recalled | n/a | 2026-10-10 | unverified |

---

## Verification note

**Date:** 2026-10-10. **Verifier:** independent skeptical re-check of the author's file. Tags in this file are unchanged: [B] project rule, [S] second-hand source carried from sibling files, [C] computed, [U] recalled.

**Limits of this check (read first).** I could not verify any web source live. `WebSearch` returned "budget used up" on my first two calls, `WebFetch` failed with DNS errors (`ENOTFOUND www.cec.gov.tw`), and the egress proxy answered 403 to Taiwanese news and government hosts (www.dgpa.gov.tw, www.cna.com.tw, udn.com, www.bnext.com.tw). I did not route around any of these. So every [S] row remains second-hand, and no confidence above `medium` is claimed for any web-sourced row.

**What I checked, and how**

| Check | Method | Result |
|---|---|---|
| All lunar-calendar dates in Table A (除夕, 初一, 天公生, 元宵, 頭牙, 媽祖誕辰, 端午, 七夕, 鬼月, 中元, 義民節, 中秋, 重陽, 尾牙, 小年, 2028 new year) | Re-ran the `lunardate` 0.3.0 library and recomputed new moons with the `ephem` 4.2.1 astronomy library in UTC+8 | All matched. New moons 2026-10-10 23:50:01 and 2027-02-06 23:56:02 confirm the two near-midnight cases (重陽 Sun 2026-10-18; 初一 Sat 2027-02-06). Lunar year 2026 has 12/29 as its last day, so 除夕 is Fri 2027-02-05 |
| Solar-term times (清明, 冬至, 立春) | `ephem` solar longitude | Days correct. Minute values were off by up to 6 minutes and are corrected in Table A and row C4 |
| Weekdays and day counts (about 55 dates; 32, 63, 82, 119 days to 雙11, 雙12, 跨年, 農曆新年) | Python `datetime` | All correct. Rule-based dates (母親節 2027-05-09, 黑色星期五 2026-11-27 and 2027-11-26, 報稅 window days) correct |
| Cross-check of [S] claims against the sibling files that originally reported them | Compared figures and wording with `platforms.md` and `competitors.md` | Found and fixed: TikTok 23.8% was attributed to the wrong source row (S2 vs S3); S1/S2/S3/S6/S7/S8 had higher confidence than the siblings supported; S16 rests on a TVBS search-results URL (now `low`); Hootsuite one-third figure (now `unverified`); Springfish "signed with Universal Music" was stronger than the source (a partnership announcement); Meta NT$5 million fine stated as fact, now "reportedly" and single-source; NCC "wrote to" the station was "said it would write"; "roughly six in ten of 18-34 on Facebook" had no source row (added S34); added n=1,091, +/-3.0% to the MIC survey |
| Ground rules | Read all draft zh-TW lines, hooks and process steps against [B1] | No health/finance advice, undisclosed AI, testimonials or login scraping found. Fixed two draft lines that implied audience history or an audience claim (TikTok hook 「很多人會看錯」, Threads reply 「很常被問到」); added a "manual reading by a human only" limit to the slang-refresh process; reworded "copied from Ministry of Finance pages" to "paraphrased and linked"; flagged fitness programme samples as close to health advice |
| Taiwan versus mainland vocabulary | Read all 110 pairs; searched the file for Simplified characters | Every Simplified character appears only inside intentional "avoid" or "converter trap" cells. Six pairs downgraded from H to M (61, 64, 86, 89, 91, 92) because both forms occur in Taiwan or I could not check the Ministry of Education dictionary form (瑜珈 vs 瑜伽). The 大陸 note in 5.8 was too absolute and is softened |
| Structure | Sources table has id, claim, URL, date published, date accessed (2026-10-10) and confidence for every row | Present; S34 and C6 added |

**Still unverified (no live source reached)**
- Taiwan 2026 local-election date 2026-11-28; Taipei Pride dates; the 2025 holiday amendment (3/29, 9/28, 10/25, 12/25, 勞動節) and every make-up-day consequence in 4.6; the 2027 official calendar.
- 週年慶, 618, 蝦皮 and 雙11 campaign dates (not found).
- Tax, invoice-draw and hotline facts in U8 and U10 (報稅 1-31 May, 統一發票 draw on the 25th of odd months, 165, 1925) match my own recollection but were not checked at the Ministry of Finance or the agencies.
- All vocabulary, particle, 台語/客語, 注音文, slang, visual-detail and neighbourhood claims ([U1]-[U5], [U13], [U14]) need the native reviewer. Nothing here is a claim that slang is current in 2026.
- All [S] web claims: Xiaohongshu ban, LINE VOOM closure, FTC 2026-04-23 statement, Meta fine, Instagram/TikTok/YouTube label rules, MIC/NCC survey figures, Life8, IKEA Taiwan, ALT, Springfish, OPEN將, VTuber count. They were not re-opened by the author or by me.
- Minute-level solar-term times; the 4-minute margin on 初一 2027 still deserves a look at the government almanac, though 2027-02-06 matches the widely published date.
