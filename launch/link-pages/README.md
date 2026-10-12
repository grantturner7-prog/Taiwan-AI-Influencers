# link-pages: four static link-in-bio pages (DRAFT v0.1, 2026-10-12)

One page per pilot (方寸, 步驟, 色環) and one for the studio. Plain HTML and one shared CSS file. **No script, no tracker, no web font, no third-party request.** Nothing here is published, no account or URL exists, the avatars are PENDING (no image has been generated), and every Chinese string is an AI draft for the wife.

## 1. Files

| Path | What it is |
|---|---|
| `fangcun/index.html`, `buzhou/index.html`, `sehuan/index.html` | The three pilot pages. Each links only to the studio page (decision D2 in `../README.md`), never to another character |
| `studio/index.html` | The studio page: neutral directory of live characters, how the studio labels, corrections, contact and business placeholders |
| `shared/linkpage.css` | The only stylesheet. Colour tokens per theme (`theme-studio`, `theme-fangcun`, `theme-buzhou`, `theme-sehuan`) |
| `check_pages.py` | Static checks and the list of placeholders. Standard library only, no network. `--final` is the publication gate |
| `screenshot.py` | Full-page screenshots with headless Chromium (needs Pillow). Output goes to `screenshots/` |
| `screenshots/*_390.png` | Phone-width renders of the four draft pages, made 2026-10-12 |

Deploy the **whole `link-pages/` folder** as the site root (the pages share `shared/linkpage.css` by relative path and the studio page links to the three persona pages). Any static host works (examples only, none checked: GitHub Pages, Cloudflare Pages, Netlify). Hosting terms, price, server logs and cookies are *unverified*; the budget line is up to NT$300 a month for hosting and a domain (`strategy/portfolio.md` 7, assumption).

## 2. What every page contains (and what it must never contain)

| Requirement | How it is met |
|---|---|
| `lang="zh-Hant-TW"`, Traditional Chinese, Taiwan vocabulary | `<html lang="zh-Hant-TW">`; English fragments carry `lang="en"`; the project's scanner `pipeline/scripts/ground_rules.py` is run over the visible text by `check_pages.py` (no Simplified characters, no mainland words found; the wife still reads every character) |
| Prominent disclosure | First block under the name, in a bordered card: **`AI 虛擬角色 / 由 明說角色工作室 創作與營運`**, then one line saying the character is AI-generated and not a real person. The checker fails a page that lacks the literal line |
| Placeholder links clearly marked | Yellow dashed boxes with 【待填：…】. A placeholder is a plain list item, not a link, so it can never be tapped or mistaken for a working button. The filled-in form of each link is in an HTML comment next to it |
| No analytics, trackers or third-party scripts | No `<script>`; a Content-Security-Policy meta line (`default-src 'none'; img-src 'self' data:; style-src 'self'`) blocks anything added by mistake; the checker fails on script, iframe, form, embed, inline style or event attributes, tracker strings and any host that is not on its allow-list |
| No invented stats | No numbers about followers, reach, ratings, prices or results. The only figures are the version date and the placeholders |
| Privacy note and contact | Both are placeholders (no mailbox exists; the privacy text is for the studio and the lawyer). The privacy card states only what is true of the page as built: it has no analytics code and loads no third-party script. Server logs and cookies of the host are *unverified* |
| Accessible | Landmarks (`header`, `main`, `footer`), one `h1`, headings in order, 16 px base text, 1.75 line height, tap targets at least 48 px high (buttons 56 px), visible focus ring, no motion, zoom not blocked, text contrast computed per theme (table below), links distinguishable by shape and not by colour alone. Not tested with a screen reader |
| Mobile first | One column. Checked at 320, 390 and 1280 px wide |

### Contrast (computed by `check_pages.py -v`, WCAG 2.x ratio, 4.5:1 needed for text)

| Pair | Studio | 方寸 | 步驟 | 色環 |
|---|---|---|---|---|
| text on page background | 13.88 | 10.52 | 11.24 | 8.85 |
| text on card | 15.64 | 11.26 | 12.28 | 10.63 |
| muted text on page background | 6.64 | 6.43 | 6.27 | **5.56** (lowest) |
| muted text on card | 7.48 | 6.88 | 6.85 | 6.68 |
| button text on button | 13.15 | 6.59 | 8.38 | 9.82 |
| placeholder text on its yellow | 9.80 | 9.80 | 9.80 | 9.80 |
| draft banner text on banner | 10.14 | 10.14 | 10.14 | 10.14 |

The persona accents (sage `#A9B5A0`, fog `#C9D1DA`, persimmon `#CD8B6A`) are used as thin rings only and never carry text. Hex values are the planned palette values from the addenda, not measurements of any photograph; the wife checks the colour read (party-colour impression) of each page, as she does for the images.

## 3. How these were checked (2026-10-12)

* `python3 launch/link-pages/check_pages.py` passes in draft mode for all four pages (0 errors). A negative test on a mutated copy (a script tag, a Google font, an unlisted external link, an inline style, a cross-persona link, `href="#"`) failed on every one of them. `--final` fails today, correctly: 15 placeholders, the draft banner and the PENDING avatars remain.
* Rendered with headless Chromium (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless`) at 390, 320 and 1280 px wide and viewed. Five layout problems were found and fixed: the studio name split across two lines in the disclosure; the 步驟 disclosure pill was pale (bone on bone) and is now dark on every theme; the PENDING text overlapped the AI chip in the avatar placeholder; one orphan character at 320 px; and no space between the studio directory and the note under it.
* **Not tested:** real phones; Safari or the Instagram in-app browser; the fonts on a Taiwan device (the sandbox only has WenQuanYi Zen Hei, which has no bold weight, so headings look lighter here than they will with PingFang TC, Noto Sans TC or Microsoft JhengHei); a screen reader; a slow connection. Do a five-minute phone check after deployment.

## 4. English gloss of the page text (for the operator; the wife reads the Chinese)

Common to all pages.

| zh-TW (DRAFT) | English |
|---|---|
| 草稿：尚未經中文審閱，請勿公開。發布前請移除這個橫幅與所有【待填】。 | Draft: not yet reviewed in Chinese, do not make public. Remove this banner and every 【待填】 (fill in) before publishing. |
| AI 虛擬角色 / 由 明說角色工作室 創作與營運 | AI virtual character / created and run by 明說角色工作室 (Plainspoken Studio, provisional name) |
| 聯絡信箱：【待填：工作室信箱】 內容更正、標示疑問或肖像疑慮，請在信件主旨註明。請勿在來信中附上個人證件。 | Contact email: [fill in: studio mailbox]. For corrections, labelling questions or likeness concerns, say so in the subject line. Please do not attach ID documents. (步驟 says "personal data or account passwords"; 色環 says "personal photos or ID documents".) |
| 【待填：隱私權說明，由工作室與律師確認後填寫】 本頁本身沒有加入分析或追蹤程式碼，也沒有載入第三方腳本。主機商的伺服器紀錄不在這句話涵蓋範圍內，需另行確認（未查證）。 | [Fill in: privacy note, to be written by the studio with the lawyer.] This page itself has no analytics or tracking code and loads no third-party script. The host's server logs are not covered by this sentence and must be checked separately (unverified). |
| 由 明說角色工作室 創作與營運｜版本：草稿 v0.1（2026-10-12） | Created and run by 明說角色工作室 / Version: draft v0.1 (2026-10-12) |

方寸.

| zh-TW (DRAFT) | English |
|---|---|
| 收納與小空間尺寸說明 | Storage and small-space dimensions, explained |
| 方寸是由 AI 生成的虛擬角色，不是真人。 | 方寸 is a virtual character generated by AI. Not a real person. |
| Instagram: 尺寸圖解與檢查清單 / YouTube: 同一主題的短影片 | Instagram: dimension diagrams and checklists / YouTube: short videos on the same topics |
| 資料來源與更正: 數字的出處、資料日期與更正方式 | Sources and corrections: where numbers come from, data dates and how corrections work |
| 明說角色工作室: 創作與營運這個角色的單位 | The studio: the unit that creates and runs this character |
| 方寸是由明說角色工作室創作與營運的 AI 虛擬角色，不是真人。方寸沒有住過任何房子，也沒有用過任何商品；所有圖片都是示意圖，並非實景，角色的圖像為 AI 生成。 | 方寸 is an AI virtual character created and run by the studio, not a real person. 方寸 has never lived in any home and has never used any product; all pictures are illustrations, not real places, and the character's image is AI-generated. |
| 內容以公開規格、標示日期的資料與算式為主，說明、比較與示範小空間的尺寸。 | Content is mainly published specifications, dated data and arithmetic, to explain, compare and demonstrate small-space dimensions. |
| 貼文中的數字若有出處，會標示資料日期；沒有出處的數字會標示「示意數字」。尺寸是否適用於你的空間，請以現場丈量為準。 | Numbers with a source show a data date; numbers without one are labelled "illustrative number". Whether a size suits your space: go by an on-site measurement. |
| 如果發現錯誤，請來信告知。更正會在原貼文中以「【更正】」標示。 | If you find a mistake, please write in. Corrections are marked 【更正】 (Correction) in the original post. |
| 若有業配、分潤連結或廠商提供的商品，會在貼文第一行標示，並使用平台的合作標籤。每張圖片與每支影片都標有「AI 生成」。 | Any sponsored post (業配), affiliate link or brand-supplied item is marked on the post's first line and the platform's partnership label is used. Every image and video is marked "AI 生成" (AI-generated). |

*Changed from the bible (`personas/fangcun/bible.md` 8.1):* the bible says "all room images are AI-generated illustrations". Under the photoreal addendum the room diagrams are human-built and only the character image is AI-generated, so the page now says "all pictures are illustrations, not real places, and the character's image is AI-generated". The wife rules.

步驟.

| zh-TW (DRAFT) | English |
|---|---|
| AI 工具功能對照與提示詞範本，附資料日期 | AI tool feature comparisons and prompt templates, with data dates |
| 步驟是由 AI 生成的虛擬角色，不是真人。影片中的螢幕錄影由工作室真人操作。 | 步驟 is a virtual character generated by AI, not a real person. The screen recordings in the videos are operated by a real person at the studio. |
| YouTube: 螢幕錄影與功能說明的短影片 / Threads: 文字整理與提示詞範本 | YouTube: short videos with screen recordings and feature explanations / Threads: text summaries and prompt templates |
| 資料來源與更正: 工具、版本、方案與日期怎麼標示 | Sources and corrections: how tool, version, plan and date are labelled |
| 步驟是由 AI 生成的虛擬角色，不是真人，由明說角色工作室創作與營運。角色本身沒有使用過任何工具；影片中的螢幕錄影由工作室真人操作，並標示工具、版本、方案與錄製日期。 | 步驟 is an AI-generated virtual character, not a real person, created and run by the studio. The character itself has never used any tool; the screen recordings are operated by a real person at the studio and show the tool, version, plan and recording date. |
| 內容只說明、比較公開資訊，並附上資料來源與日期。工具更新很快，請以官方頁面為準。 | Content only explains and compares public information, with sources and dates. Tools update quickly: the official page prevails. |
| 不提供投資、醫療、法律或賺錢相關的建議。 | No investment, medical, legal or make-money advice. |
| 每支影片都會標示工具、版本、方案與錄製日期，並附上官方頁面名稱與資料日期。示範輸出不代表每次結果相同。 | Every video labels the tool, version, plan and recording date and attaches the official page name and data date. A demo output does not mean the result is the same every time. |
| 如果發現錯誤或資料已過期，請來信告知。更正會標示「【更正】」與日期。 | If you find an error or out-of-date data, please write in. Corrections are marked 【更正】 with the date. |
| 步驟與影片、貼文中提到的工具廠商無隸屬關係。若有業配、廠商提供的方案或分潤連結，會在影片與說明欄清楚標示，並使用平台的合作標籤。… | 步驟 has no affiliation with the tool vendors mentioned in videos and posts. Any sponsored post, vendor-supplied plan or affiliate link is clearly marked in the video and description and the platform's partnership label is used. ... |

色環.

| zh-TW (DRAFT) | English |
|---|---|
| 配色、穿搭公式與台灣氣候疊穿說明 | Colour, outfit formulas and Taiwan-climate layering, explained |
| 色環是由 AI 生成的虛擬角色，不是真人。圖為搭配示意，角色沒有穿著任何商品。 | 色環 is a virtual character generated by AI, not a real person. Pictures are styling illustrations; the character is not wearing any product. |
| Instagram: 配色與穿搭公式的圖文輪播 / Threads: 單張圖卡與一句話的搭配規則 | Instagram: picture carousels on colour and outfit formulas / Threads: single cards with a one-line styling rule |
| 色環是由 AI 生成的虛擬角色，不是真人，由明說角色工作室創作與營運。角色沒有衣櫃，也沒有穿過、試過或買過任何商品。 | 色環 is an AI-generated virtual character, not a real person, created and run by the studio. The character has no wardrobe and has never worn, tried or bought any product. |
| 這裡整理配色、穿搭公式與台灣氣候的疊穿邏輯，並附上資料來源與日期。圖片皆為搭配示意。 | This account organises colour, outfit formulas and Taiwan-climate layering logic, with sources and dates. All pictures are styling illustrations. |
| 色環不是造型師或色彩顧問，不評斷身材與膚色，也不接受個人照片。 | 色環 is not a stylist or colour consultant, does not judge body shape or skin tone, and does not accept personal photos. |
| 引用的資料會標示來源與日期。螢幕有色差，實際顏色、尺寸與材質請以品牌官方資訊為準。 | Cited data shows source and date. Screens differ in colour; real colour, size and material go by the brand's official information. |

Studio.

| zh-TW (DRAFT) | English |
|---|---|
| 明說角色工作室 / Plainspoken Studio（暫定英文名） | 明說角色工作室 / Plainspoken Studio (provisional English name) |
| 本工作室創作與營運的角色，都是由 AI 生成的虛擬角色，不是真人。 | The characters this studio creates and runs are all AI-generated virtual characters, not real people. |
| 明說角色工作室是一個專門創作與營運 AI 虛擬角色的小型工作室。我們的每一位角色都是由 AI 生成的虛構角色，不是真人，也從未親身使用或穿過任何商品，或到訪過任何地方。 | 明說角色工作室 is a small studio that creates and runs AI virtual characters. Each of our characters is a fictional character generated by AI, not a real person, and has never personally used or worn any product or visited any place. |
| 角色的工作是把資訊整理清楚：用圖解、公開資料與標示日期、由工作室真人操作錄製的螢幕畫面，替你說明、比較與示範。每個帳號的簡介都會標明「AI 虛擬角色」與工作室名稱；若有業配、分潤連結或廠商提供的商品，也一定會在貼文中清楚揭露。 | The characters' job is to organise information clearly: with diagrams, public data with dates and screen recordings made by a real person at the studio, they explain, compare and demonstrate. Every account's bio says "AI virtual character" and the studio name; any sponsored post, affiliate link or brand-supplied item is always disclosed in the post. |
| 目前的角色: 方寸（收納與小空間尺寸說明）、步驟（AI 工具功能對照與提示詞範本）、色環（配色、穿搭公式與台灣氣候疊穿說明） | Current characters: 方寸 (storage and small-space dimensions), 步驟 (AI tool feature comparisons and prompt templates), 色環 (colour, outfit formulas, Taiwan-climate layering) |
| 這份列表只是資訊揭露，不是推薦。各角色的帳號不會互相追蹤、留言或推薦對方。 | This list is disclosure only, not a recommendation. The characters' accounts do not follow, comment on or recommend each other. |
| 我們怎麼標示 (6 bullets) | How we label: bios say "AI virtual character" and the studio name; the first line of every post says it is AI-generated; every image and video is marked "AI 生成"; the platform's AI-content label is on for every post; sponsored posts, affiliate links and brand-supplied items are marked on the first line with the platform's partnership label; any automated reply says it is automated |
| 我們的做法 (5 bullets) | Our practice: characters never say they used, wore, ate or visited anything (content explains, compares and demonstrates, with sources and dates); no real-person photo is used as a reference and no specific real person is the model; no bought followers or engagement and no bot comments; at present every post is reviewed by a real person before publishing; no health, medical, investment or financial advice and no politics |
| 如果你發現內容有誤、標示不清，或認為某個角色的外貌與你或你認識的人相似，請來信告知。我們會優先處理，並先暫停相關內容再進行查證。 | If you find an error, unclear labelling, or think a character's appearance resembles you or someone you know, please write in. We handle it with priority and pause the related content first, then investigate. (The internal rule is a 24-hour take-down; the number is deliberately left out of the public text until the lawyer has answered.) |
| 合作洽詢: 【待填：待公司登記完成並經律師確認後再啟用，請勿提前公開】 | Business enquiries: [fill in: enable only after company registration is complete and the lawyer has confirmed; do not publish early] |

## 5. Rulings the pages need from the wife

1. Every string above (tone, Taiwan vocabulary, particles). Specifically: 「示意圖，並非實景」; 「疊穿」; 「標示」 against 「標註」; whether 「揭露」 on the studio page is stiff; whether 「肖像疑慮」 is understood by ordinary readers.
2. Whether the three disclaimer sentences read as disclaimers: 「不提供健康、醫療、投資或理財建議，也不談政治議題。」, 「不提供投資、醫療、法律或賺錢相關的建議。」, 「各角色的帳號不會互相追蹤、留言或推薦對方。」 (`check_pages.py` skips exactly these three in its keyword scan, because the scanner flags 投資, 政治, 賺錢 and 互相追蹤, and says so).
3. The dark disclosure pill and the page colours: any political or camp impression at phone size (the 色環 page is blush with a charcoal button; the 方寸 page is oat with walnut).
4. Whether the studio page's public promises are acceptable: 「目前每則貼文都由真人審閱後才發布」 (update if per-post approval is ever relaxed) and 「製作角色時，不使用任何真人照片作為參考，也不以特定真人為藍本」 (true of the process; the addendum warns that a generator can still produce a face that resembles someone by chance).

## 6. Filling in and publishing (the operator)

1. Wait for the gates in `../README.md` section 3: wife's review of every string, studio name and handle checks, mailbox, avatar approved.
2. For each placeholder link: replace the dashed `<li class="link link--todo">…</li>` with the filled form that sits in the comment above it (keep `rel="noopener noreferrer"`), then delete the comment. Hosts allowed by the checker: instagram.com, threads.net, threads.com, youtube.com, youtu.be. Add a host to `ALLOWED_HOSTS` in `check_pages.py` only on purpose.
3. Avatar: when the approved avatar exists (with the AI chip baked in, see `../templates/avatar-guide.svg` and `../personas/<slug>.md` section 5), save it as `avatar.webp` or `avatar.png` in the persona's folder, replace the placeholder `div` with the `<img>` form in the comment (alt text is in the comment), and log the file in `assets/provenance.csv`.
4. Fill the contact mailbox (a studio mailbox, never a personal address) and the privacy note. Check what the host logs and whether it sets cookies, and write that in.
5. Delete the draft banner, and delete the `robots` noindex line only if you want search engines to list the page.
6. `python3 launch/link-pages/check_pages.py --final` must pass with 0 errors. Then `python3 launch/link-pages/screenshot.py --widths 320 390` and look at the result.
7. Deploy the folder, open the live URL on a phone, put the URL in each bio, and add the date to `../evidence-log.csv`.
8. After any later edit run the check again. If the studio name changes, search all four pages and the comments for `明說角色工作室`.

## 7. Link clicks (Phase 7 decision, not made here)

`strategy/portfolio.md` 6.1 wants link clicks counted at account level, and the Phase 6 brief for these pages says no analytics. The pages therefore carry nothing. Options for later, none checked: the Instagram and YouTube dashboards may report taps on the profile link (*unverified*); a host's own aggregate statistics, if any (*unverified*, and they change the privacy note); a self-hosted counter that sets no cookie. Any choice must be written into the privacy note before it is switched on.
