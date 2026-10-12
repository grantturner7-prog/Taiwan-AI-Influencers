# 色環 (sehuan) hook library

**Status: DRAFT v0.1, written 2026-10-12 (Phase 5).** 44 hooks for the four pillars of `personas/sehuan/bible.md` section 6, written to be used as the first line of an Instagram cover, a Threads question or card, or a Reel card (Reels are not scheduled in the first 30 days). Every zh-TW line is an AI draft for the wife; the operator reads the English gloss. Nothing here is approved or published. Evidence labels: *assumption* = a planning figure to calibrate; *unverified* = not checked against a primary source; *computed* = calculated in this session.

**How to use this file.** The calendar (`calendar-30d.md`) names hooks by ID. A hook is a promise to explain something with a rule, a diagram or a labelled example; it is never a claim about how anything looks on, feels on or does for a person. Hooks are written for a persona that has not worn, tried or bought anything (Ground rule 4), so none of them says 「我穿」, 「我試」, 「我買」 or describes a result.

## 1. Rules every hook follows

| # | Rule | Source |
|---|---|---|
| 1 | A question or a rule, 8 to 16 characters when possible and **20 at most** (a season or a place name may take it to 20). The "Chars" column below counts characters including punctuation | bible 3.1; the 20 cap is an *assumption* |
| 2 | No shouting or hard sell: no 「你一定要知道」, 「超誇張」, 「震驚」, 「必買」 | bible 3.1, 3.4 |
| 3 | No experience words (試穿, 上身, 開箱, 實測, 心得, 踩雷, 避雷, 入手 as a personal claim) and no 「今日穿搭」 or 「OOTD」 | Ground rule 4; bible 3.4 |
| 4 | No body, skin or age words (顯瘦, 顯白, 顯高, 遮肉, 顯老, 減齡, 膚色); proportion is a property of the picture ("in this layout"), never of a body | Ground rule 6; bible C2, C12 |
| 5 | No fabric-performance or health words (透氣, 排汗, 保暖, 防曬, 抗UV, 防潑水, 親膚) in her own voice | bible C11 |
| 6 | No fortune or lucky colour (開運, 幸運色, 星座色) | bible C13 |
| 7 | No colour-pair headline built on 藍綠, 藍白 or 綠白, and no single saturated blue, green, teal or yellow as the hook's subject. Name hues by tone | bible C3, 3.3 D |
| 8 | No price, discount, sale or 週年慶 figure; no 「最低價」 or 「限時」 | bible 3.4; BRIEF rule 10 |
| 9 | No brand, product or logo named (weeks 1 to 8) | bible C5 |
| 10 | Mainland vocabulary is out (視頻, 信息, 質量, 軟件 and the table in bible 3.3); Traditional characters only | BRIEF section 5 |
| 11 | The studio's method phrase 「先看 X」 (an instruction to look at one source first) belongs to other characters (`personas/README.md` V3); 色環 does not open a hook with it and uses 「先記住」, 「先搞懂」, 「先過三關」 instead. A question that asks about the audience's own habit and happens to contain 先看 (H14) instructs nothing and is allowed. No more than one hook in four opens with an imperative | `personas/README.md` V3; the one-in-four cap is an *assumption* |
| 12 | The first-person 我 appears only to present, organise or state a limit (bible 3.2); the intro hooks H37 to H40 are not used on every post (studio voice rule V3) | bible 3.2 |

Each hook below was run through the pipeline's word scanner (`pipeline/scripts/ground_rules.py`, the same net `queue.py validate` uses); the "Scan" column shows `clean` or the finding codes. **A clean scan is not approval:** the net is blunt, and the wife's tone check (section 6) is the real test.

## 2. The library

| ID | Pillar | Use | Hook (zh-TW, DRAFT) | Gloss | Chars | Used in | Scan | Note |
|---|---|---|---|---|---|---|---|---|
| H01 | P1 | IG cover | 三色口訣：主色、輔色、點綴色怎麼分 | Three-colour rule of thumb: how to tell main, secondary and accent apart | 17 | P01 | clean | Rule of thumb, never 'the rule'; no source claim unless G7 confirms |
| H02 | P1 | Threads question | 點綴色最多一成，你會放在哪裡？ | The accent takes at most a tenth: where would you put it? | 15 | P02 | clean | Asks the audience; no verdict |
| H03 | P1 | Reel on-screen or cover | 同一件外套，換三種內搭色，畫面差在哪？ | Same jacket, three inner-layer colours: what changes in the picture? | 19 | (Reel template, not scheduled) | clean | Asks about the picture, not how it feels or fits (bible S02); garments are flats |
| H04 | P1 | IG cover | 中性色也有冷暖：灰、米、駝放上色環 | Neutrals have a warm and a cool side: place grey, beige and camel on the wheel | 17 | P05 | clean | About swatches and garments only, never skin |
| H05 | P1 | Threads question | 三個灰色放在一起，哪一個偏冷？ | Three greys side by side: which one leans cool? | 15 | P06 | clean | Hex values kept so the answer is checkable |
| H06 | P1 | IG cover | 同色系怎麼配：只改明暗的三種示意 | How to combine one colour family: three illustrations that change only lightness | 16 | P09 | clean | Colour-neutral; fine in the election window |
| H07 | P1 | IG cover | 色環上相鄰與相對：三種關係一次看 | Adjacent and opposite on the wheel: three relationships at a glance | 16 | P17 | clean | HOLD until after the election window; needs the G7 reference for the terms; wife checks every pair |
| H08 | P1 | IG cover | 奶茶色是哪一種？把三個色名放上色環 | Which colour is milk-tea? Placing three colour names on the wheel | 17 | (backlog) | clean | Colour names vary between brands; no brand named; wife rules the names |
| H09 | P1 | IG cover | 點綴色放哪裡：包、鞋、圍巾的比例示意 | Where to put the accent: proportion illustrations for a bag, shoes or a scarf | 18 | (backlog) | clean | Objects are styling items, not gifts; shoes and umbrella never framed as gifts |
| H10 | P1 | Closer line | 公式不變，色環轉一格，換個色相再看一次。 | Same formula; turn the wheel one step; look at a new hue again. | 20 | (series A closer) | clean | Formula posts only (running joke J3) |
| H11 | P1 | IG cover | 深色下半身，加一個點綴色會怎樣？ | A dark lower half plus one accent colour: what happens? | 16 | (backlog) | clean | 'What happens' means in the picture; no effect-on-the-wearer claim |
| H12 | P1 | Threads question | 兩個顏色，在色環上隔幾格？ | Two colours: how many steps apart on the wheel? | 13 | P18 | clean | Quiz card; positions numbered, no colour-pair headline |
| H13 | P2 | IG cover | 東北季風天，濕冷怎麼疊？先記住三層順序。 | On northeast-monsoon days, how do you layer for damp cold? Remember the three-layer order first. | 20 | P03 | clean | Season wording needs the weather-agency page (gate 12); no health or warmth words |
| H14 | P2 | Threads question | 出門前，你會先看氣溫，還是降雨機率？ | Before going out, do you check the temperature first or the chance of rain? | 18 | P04 | clean | Text only; needs the text-only first-line approval |
| H15 | P2 | IG cover | 冷氣房外套怎麼選色：辦公室、捷運、電影院 | Choosing the colour of a layer for air-conditioned rooms: office, MRT, cinema | 20 | P11 | clean | No MRT map, station name or line colour; no warmth or health wording |
| H16 | P2 | IG cover | 雨天褲長與鞋色：一張圖看配色比例 | Rainy-day trouser length and shoe colour: colour proportions in one image | 16 | P19 | clean | Shoes are a styling item, never a gift; no waterproof claim |
| H17 | P2 | IG cover | 同一個月，台北和高雄的外層差在哪？ | In the same month, how do the outer layers differ between Taipei and Kaohsiung? | 17 | (backlog) | clean | Needs the agency's numbers for both cities; the wife judges the regional wording |
| H18 | P2 | IG cover | 濕熱天的淺色搭配：同色系三種明度 | Light-colour combinations for hot, humid days: three lightness steps in one family | 16 | (spring backlog) | clean | Out of season in December; no sun-protection or cooling words |
| H19 | P2 | IG cover | 三層疊穿，內層露出多少面積？ | In a three-layer outfit, how much area of the inner layer shows? | 14 | (backlog) | clean | Area logic of series B1; rule of thumb only |
| H20 | P2 | Threads question | 外層顏色先決定，還是內層先決定？ | Do you decide the outer-layer colour first, or the inner layer's? | 16 | (backlog) | clean | Question only |
| H21 | P3 | IG cover | 尾牙穿搭，先過三關：場合、顏色、鞋子。 | Year-end banquet outfits: pass three checks first: occasion, colour, shoes. | 19 | P21 | clean | Caption adds the etiquette line; no all-white or all-black example; sanity check by a fashion contact |
| H22 | P3 | IG cover | 聖誕與跨年派對：亮色點綴的比例 | Christmas and countdown parties: the proportion for a bright accent | 15 | P15 | clean | Red and green only in a neutral layout, no slogan; no 開運 or lucky-colour wording |
| H23 | P3 | IG cover | 喜宴賓客配色：為什麼常避開全白與全黑？ | Wedding-guest colours: why are all-white and all-black commonly avoided? | 19 | (backlog) | clean | The 'commonly avoided' claim needs the wife's sign-off and a named etiquette source; north–south differences (bible 10.2 Q14) |
| H24 | P3 | IG cover | 新年紅怎麼配：紅色比例示意 | Pairing New Year red: proportion illustrations | 13 | (January backlog) | clean | Red is handled as a taught colour, never as a costume change; the character does not wear red |
| H25 | P3 | IG cover | 面試場合的顏色選擇：三組配色示意 | Colour choices for an interview occasion: three illustrated combinations | 16 | (backlog) | clean | No hiring or outcome claim; no 'you will look' wording |
| H26 | P3 | Threads question | 派對的亮色點綴，你會放在配件還是外套？ | At a party, would you put the bright accent on an accessory or on the jacket? | 19 | P16 | clean | Question only |
| H27 | P3 | IG cover | 邀請函沒寫服裝要求，先確認哪三件事？ | The invitation gives no dress note: which three things do you confirm first? | 18 | (backlog) | clean | The host's request always prevails (etiquette line) |
| H28 | P4 | IG cover | 尺寸表看不懂？先搞懂「平量」兩個字。 | Can't read the size chart? Start with the two words 「平量」. | 18 | P07 | clean | Blocked until the definition source is recorded |
| H29 | P4 | Threads card | 平量和圍度，差在哪？ | Flat measurement and circumference: what is the difference? | 10 | P08 | clean | Example numbers tagged 範例數字，非真實商品 |
| H30 | P4 | IG cover | 色差是什麼：螢幕上的顏色為什麼不同？ | What is colour variance: why do colours differ between screens? | 18 | P13 | clean | Needs a named public source on display and lighting, or stays at 'screens differ' |
| H31 | P4 | IG cover | 洗標符號怎麼看：五個符號整理 | How to read care-label symbols: five of them | 14 | (backlog) | clean | Needs the standard that applies in Taiwan (unverified) and the five symbols chosen from it; no care advice in her own voice |
| H32 | P4 | IG cover | 成分表怎麼讀：看懂纖維的百分比 | How to read a composition list: understanding the fibre percentages | 15 | (backlog) | clean | Example list tagged as an example; performance words only as a brand's quoted spec |
| H33 | P4 | IG cover (monthly at most) | 這季流行色報導怎麼讀：把公開報導放上色環 | How to read this season's trend-colour reports: placing a public report on the wheel | 20 | (backlog) | clean | One named public source and its date; says 報導指出, never 會流行; no brand product or logo; sanity check by a fashion contact |
| H34 | P4 | IG cover | 商品頁的色名怎麼對照？奶茶、燕麥、杏 | How do you compare the colour names on a product page? Milk-tea, oat, apricot | 18 | (backlog) | clean | No brand page shown; the brand's own name prevails |
| H35 | P4 | IG cover | 週年慶之前，先練習看懂商品頁的三個欄位 | Before the anniversary sales, practise reading three fields of a product page | 19 | (backlog) | clean | No price, discount or sale figure; only which fields to read |
| H36 | P4 | Threads card | 色名一樣，螢幕上的顏色一樣嗎？ | Same colour name: is the colour on the screen the same? | 15 | P14 | clean | Label card; no device comparison claim |
| H37 | ID | Intro line | 我是色環，AI 虛擬角色，只整理規則。 | I'm Sehuan, an AI virtual character, and I only organise rules. | 19 | (pinned post, replies) | clean | Not on every post (studio voice rule V3) |
| H38 | ID | Limit line | 我沒有衣櫃，只整理配色和版型邏輯。 | I have no wardrobe; I only organise colour and cut logic. | 17 | (backlog) | clean | A negated limit statement, once per piece (bible 3.4) |
| H39 | ID | Reply or caption line | 圖中的衣服是造型設計，不是商品。 | The clothes in the picture are a costume design, not a product. | 16 | (R-WHERE reply) | clean | Photoreal variant of bible S06 (addendum 12.2) |
| H40 | ID | Footer line | 螢幕有色差，AI 角色也一樣。 | Screens shift colour, even for an AI character. | 15 | (colour posts, at most weekly) | clean | Running joke J4 |
| H41 | P1 | Threads question | 三種明度，你會把哪一格放在外層？ | Three lightness steps: which one would you put on the outer layer? | 16 | P10 | clean | Question only |
| H42 | P2 | Threads question | 冷氣房裡的外層，你會選同色系還是撞色？ | For a layer in an air-conditioned room, would you pick the same colour family or a contrast? | 19 | P12 | clean | Text only; needs the text-only first-line approval; no warmth or health wording |
| H43 | P2 | Threads question | 雨天褲腳，你會選到腳踝還是更長？ | On a rainy day, would you choose a hem at the ankle or longer? | 16 | P20 | clean | Text only; 雙12 (Sat 2026-12-12): no price, discount or sale wording; no waterproof claim |
| H44 | P3 | Threads card | 尾牙穿搭的三個檢查點 | Three checkpoints for a year-end banquet outfit | 10 | P22 | clean | Card of the three checks; etiquette line |

**Count:** 44 hooks. P1 配色公式 13, P2 氣候穿搭 10, P3 場合穿搭 8, P4 看懂標示與趨勢 9, identity and limit lines 4. Longest hook 20 characters; hooks over 16 characters 22 (all within the 20 cap).

## 3. Hooks on hold

| Hook | Hold until | Reason |
|---|---|---|
| H07 | After the election window (not before Mon 2026-11-30; scheduled for P17 on 2026-12-09) and the G7 colour-theory reference is logged | Opposite colours invite camp pairs; the wife judges the colour read of every pair |
| H17 | The weather page (gate 12) is chosen and both cities' numbers are on a slip | Regional claim |
| H23, H24 | The wife's ruling on the wedding and New Year colour customs, and a named etiquette source | Cultural claims; north–south differences |
| H31, H32 | The Taiwan care-label and composition standard is identified (bible open item 26, *unverified*) | Needs a cited standard |
| H33 | One named public trend source and its date; at most once a month | 報導指出 only; no prediction |
| Any hook that mentions a red-and-green pair | After the election window and the wife's ruling on 紅配綠 | Camp-pair risk (bible 3.3 D) |

## 4. Patterns not to use, and what to write instead

| Pattern (do not use) | Why | Write instead |
|---|---|---|
| 今日穿搭, OOTD, GRWM, 穿搭日記 | A wearing and daily-life claim | 搭配示意 |
| 我今天穿…, 我穿給你看 | Past or present wearing | 本篇整理…, 這張圖把…並排 |
| 這樣穿顯瘦／顯高／遮肉 | Body claim | 在這張圖裡，上衣區塊比下身區塊短 |
| 顯白, 適合黃皮／白皮, 冷皮／暖皮, 個人色彩 | Skin and complexion; a diagnosis she cannot make | The colour's own lightness and chroma (明度, 彩度) |
| 必買, 神器, 百搭 (about a product) | Hype | 選購時比對的重點 |
| 踩雷, 避雷, 地雷色 | Experience and taste verdict | 對比比較強／比較弱 |
| 超好穿, 穿起來很舒服, 尺寸準 | Fit and comfort testimony | 請對照品牌尺寸表（平量） |
| 透氣, 保暖, 排汗, 防曬, 抗UV, 防潑水 | Performance and health | Only a brand's own published spec, quoted and dated; none in weeks 1 to 8 |
| 藍綠, 藍白, 綠白 as a headline | Camp pair | Name hues by tone; neutral diagram only |
| 紅配綠很俗 | A taste verdict and a camp-adjacent pair | Hold; the wife rules after the election window |
| 開運色, 幸運色, 流年色 | Fortune-telling | (none) |
| 你一定要知道, 震驚, 超誇張 | Shouting | A question or a rule |
| 最低價, 破盤, 限時, 手慢無 | Price and urgency | (none) |
| 氛圍感, 鬆弛感, 高級感 | Mainland-coded (小紅書) | 氛圍, 輕鬆的感覺; 質感 only as a word about a picture, never a real product |
| 種草, 安利 | Mainland-coded; recommendation | (none) |
| 少女感, 減齡, 顯老, 凍齡 | Age and body | (none) |
| Sets of four; 四 as a count in a list | 四 sounds like 死 | Use three items (the series use threes) |
| 面試穿搭 (the substring 試穿 hides inside it) | The pipeline scanner flags 試穿 as a wearing claim, and a reader may see it too; the bible's pillar title P3-4 uses this wording | 面試場合的顏色選擇 (H25) |
| 上身比例 (the substring 上身 hides inside it) | 上身 is a banned wearing word | 上半部的比例, or 上衣區塊 |

## 5. Rotation and mix

- **Mix over any four posts (*assumption*):** one rule or formula hook, one climate or occasion hook, one label-reading hook, one question for Threads. The calendar already follows this.
- **At most one Reel-style on-screen hook a week** once Reels are switched on; none in the first 30 days.
- **Reuse:** a hook is not reused within 8 weeks; a Threads question may restate its Instagram master's hook in other words, never word for word.
- **Retire a hook** if it drew a political, body-image or "is she real" thread that the team had to hide (log the reason in the weekly report).
- **Never copy** another creator's title. A hook that looks like a copy is dropped.

## 6. The wife's tone check

Use the culture.md 8.1 reply format (APPROVE, SMALL FIX, REJECT; codes V vocabulary, T tone, E experience claim, R regulated topic, P politics or sensitive, X cultural error, C timing). About 10 minutes for a batch of 8 hooks (*assumption*).

| # | Question | Code |
|---|---|---|
| 1 | Does it sound like a Taiwanese person talking, not a translation (no 此外, 因此, 首先)? | T |
| 2 | Is it 工商味 (ad-sounding) or 客服味 (service-desk)? | T |
| 3 | Is any word mainland-leaning or dated? Mark it live, dated or wrong | V |
| 4 | Do the colour words (柿子橘, 灰玫瑰色, 灰紫色, 紅橘色, 冷灰, 暖灰, 駝色, 中性色) sound natural, and does any pair read as a camp? | V, P |
| 5 | Does anything hint at a body, skin, age or taste verdict? | E, R |
| 6 | Is the 20-character cap too long for a phone cover? | T |
| 7 | Is the particle use right (～ only once, 喔 at most once)? | T |

## 7. Adding a hook

1. Write it in the rules of section 1 and give it the next ID.
2. Run `python3 pipeline/scripts/queue.py validate` on a draft that uses it, or `python3 content/sehuan/verify.py`, which re-scans this table.
3. Add a source need in the Note column if it states a fact.
4. The wife rules; the operator records the ruling in the weekly report.
