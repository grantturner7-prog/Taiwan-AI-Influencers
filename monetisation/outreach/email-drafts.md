# Outreach email drafts (zh-TW with English gloss), DRAFT v0.1

Written 2026-10-12 for the operator (who reads the English gloss) and the wife (who reads, corrects and signs off every zh-TW line). Studio name 明說角色工作室 / Plainspoken Studio is provisional and uncleared. **Every zh-TW string here is an AI draft for the wife. Nothing has been sent. Claude never sends, posts or contacts anyone: the humans send, by hand, from the studio mailbox, after the gates in [outreach-playbook.md](outreach-playbook.md) section 1 are closed.** On 2026-10-12 none of those gates is closed (no registered business, no cleared name, no studio mailbox, no lawyer answer), so none of these messages can be sent yet.

## 0. Read this first

1. **What these drafts say, and what they do not.** They say, truthfully: the studio is a very small studio of disclosed AI-generated characters; the characters are not people and have never used, worn or tested anything; the studio is new and has **no past work, no client, no follower count and no result to show**; it makes no promise of reach, engagement or sales; it offers (only where the operator chooses) a free, private, scoped sample; and anyone can say 「不需要」 and be left alone. They never name a client, a case, a figure, a prize or a testimonial, because none exists (Ground rule 10). If a recipient asks for one, the answer is "there is none yet" (playbook section 7).
2. **No price appears in any draft.** The rate card is an internal proposal, not yet checked against any real quote (`monetisation/rate-card.md` section 0). Quotes are given only after scoping, after registration, and after the gates in that file.
3. **Placeholders.** Every slot is written `[LIKE THIS: TO FILL]` in capitals, so nothing can be sent by accident (the checker `check_outreach.py --filled` refuses a text that still contains `TO FILL`). Required slots: `[STUDIO LEGAL NAME / REGISTRATION: TO FILL]` (the registered name once it exists; until then the draft cannot be sent), `[SENDER NAME: TO FILL]`, `[ROLE: TO FILL]`, `[STUDIO EMAIL: TO FILL]`, `[PHONE OR 「僅以電子郵件聯絡」: TO FILL]`, `[LINK PAGE URL: TO FILL WHEN IT EXISTS]`, `[RECIPIENT / TEAM NAME: TO FILL]`, `[WHY THIS RECIPIENT: ONE TRUE SENTENCE TO FILL]`. **No name, email address, phone number, registration number or web address is invented anywhere in this folder.**
4. **One true sentence about the recipient.** The `[WHY THIS RECIPIENT]` slot must be something the sender actually saw on the recipient's own published pages (for example "your site publishes dimension tables for each storage box"). No flattery, no claim that the studio uses or likes the recipient's products, no guess about the recipient's plans.
5. **The free-sample paragraph is optional and is the operator's choice, per recipient.** Keep it only where the operator has decided to offer it and the gates for samples are closed (image-tool commercial terms read, `HUMAN_TODO.md` 33). **For fashion the sample is face-free** (a colour-story board or a flat-lay lookbook layout from the brand's own product photos); a photoreal virtual try-on is ON HOLD until the lawyer answers (`content/sehuan/b2b-pitch.md` A2 and A4; rate card section 0 item 5). Never offer video, voice, lip-sync or animation of a photoreal face.
6. **Who sends.** The wife is the natural sender of record for the zh-TW messages (she reads and writes the language, and is the likely registrant). The operator sends nothing in Chinese that she has not read. Decide together who is named in the signature: a named person must consent (studio kit section 10). The English gloss may be adapted for a recipient whose only route is an English form (for example a multinational's global site); the wife checks that wording too.
7. **Format.** Plain text, no images, no attachments, no tracking pixel, no link shortener, one link at most (the studio link page, once it exists). One message per recipient; no mail-merge tool and no automated sequence (the humans type and send each one, Ground rule 9's spirit).
8. **Taiwan vocabulary.** 影片, 資訊, 品質, 專案, 軟體, 網路, 聯絡, 回覆, 寄送, 創作者. Not the mainland forms (視頻, 信息, 質量, 項目, 軟件, 網絡, 聯繫, 回復, 發送, 博主). The checker scans for these.
9. **For the wife to rule on** (also in section 9): 您 versus 貴公司 in the greeting; whether 「AI 虛擬角色」 reads naturally to a business reader; whether the opt-out sentence is polite enough; whether offering a free sample in the first message is too forward in Taiwan business culture (it is optional for that reason); whether 「商祺」 is the right close for each type of recipient.

## 1. Before any message is sent: the pre-send check (one page)

| # | Check | Done by |
| :-- | :-- | :-- |
| 1 | The playbook gates (section 1) are closed, and the date is written in the tracking sheet | both |
| 2 | The row in the target list has `verified_on` filled; the recipient exists, is not in a declined category, is not on the do-not-contact list, and its site does not say it refuses unsolicited proposals | operator |
| 3 | The channel is the recipient's own published business-inquiry route (form or business address), not a personal address, a personal social account or a guessed address | operator |
| 4 | The right template (T1 brand, T2 agency or platform) and the right niche block (fashion, home or tools) are chosen | operator |
| 5 | The free-sample paragraph is kept only if the operator chose it for this recipient | operator |
| 6 | Every `TO FILL` slot is replaced; the text contains no price, figure, client, result or claim of experience | wife |
| 7 | The wife has read the zh-TW line by line | wife |
| 8 | The message is sent by hand from the studio mailbox, and the same day the tracking row is filled and one `outreach_sent` row is added to `analytics/templates/lead_signals.csv` | sender |

## 2. Shared blocks (used by several templates)

| Block | zh-TW (DRAFT for the wife) | English gloss |
| :-- | :-- | :-- |
| **B-INTRO** | 我是 [SENDER NAME: TO FILL]，來自 [STUDIO LEGAL NAME / REGISTRATION: TO FILL]（暫定名稱：明說角色工作室）。我們是一個很小的工作室，專門創作與營運「AI 虛擬角色」。每一位角色都明確標示為 AI 生成，不是真人，也不會說自己用過、穿過或測試過任何商品。 | I am [SENDER NAME: TO FILL] from [STUDIO LEGAL NAME / REGISTRATION: TO FILL] (working name: Plainspoken Studio). We are a very small studio that creates and runs "AI virtual characters". Every character is clearly labelled as AI-generated, is not a real person, and never says it has used, worn or tested any product. |
| **B-STATUS** | 目前我們剛起步：還沒有可展示的合作案例，也沒有可供參考的追蹤人數或成效數據，因此不做任何成效承諾。我們能說明的只有做法與標示規則。 | We are only starting: there is no finished collaboration to show and no follower or performance figure to refer to, so we promise no results. All we can describe is how we work and our labelling rules. |
| **B-RULES** | 所有內容在使用前，都需經貴方逐項書面確認。角色只做說明、比較與示意，不做使用心得或推薦。若是付費或合作內容，一律在貼文第一行標示【業配】或【合作內容】，並使用平台的付費合作標籤，同時開啟平台的 AI 標示；這些標示不接受移除或縮小。 | Nothing is used before you have approved it, item by item, in writing. The character only explains, compares and illustrates; it gives no first-hand review or recommendation. Paid or collaborative content always carries 【業配】 or 【合作內容】 on the first line, the platform's paid-partnership tool and the platform's AI label; these labels are not removed or shrunk on request. |
| **B-SAMPLE-OPT** | [OPTIONAL: 僅在營運者決定提供時保留] 如果貴方有興趣評估，我們可以先免費、不公開地製作一份小範圍的示範內容供貴方檢視。示範內容不會張貼在任何地方，也不附帶任何義務；範圍與修改次數會先以書面約定。 | [OPTIONAL: keep only if the operator chooses to offer it] If you would like to evaluate, we can first make a small sample for you to look at, free of charge and in private. It will not be posted anywhere and carries no obligation; the scope and the number of revisions are agreed in writing first. |
| **B-RATESHEET-OPT** (agencies only) | [OPTIONAL: 僅在營運者決定詢問時保留] 另外，我們正在為這間新工作室蒐集市場上的報價單與網紅分級定義作為參考。如果貴公司有可以公開提供的資料，煩請惠予提供；這並非承諾任何合作，也請不必為此特別準備。 | [OPTIONAL: keep only if the operator chooses to ask] Separately, as a new studio we are collecting reference price sheets and creator-tier definitions from the market. If you have anything you can share publicly, we would be grateful; this is not a commitment to any collaboration and please do not prepare anything specially. |
| **B-OPTOUT** | 這封信是依據貴公司官網公開的合作聯絡方式寄出的。若不希望再收到我們的來信，請直接回覆「不需要」，我們會立即停止聯絡，並將貴公司記入不再聯絡名單。 | This message was sent using the business-contact route published on your website. If you do not wish to hear from us again, simply reply 「不需要」 ("not needed") and we will stop at once and add your company to our do-not-contact list. |
| **B-CLOSE** | 謝謝您撥冗閱讀。敬祝　商祺 | Thank you for your time. With best regards. |
| **B-SIG** | [SENDER NAME: TO FILL]<br>[ROLE: TO FILL]<br>[STUDIO LEGAL NAME / REGISTRATION: TO FILL]<br>[STUDIO EMAIL: TO FILL]　[PHONE OR 「僅以電子郵件聯絡」: TO FILL]<br>[LINK PAGE URL: TO FILL WHEN IT EXISTS]<br>本信由工作室成員親自撰寫並寄出。 | Name, role, studio legal name and registration, studio email, phone or "email only", link-page address. This message was written and sent by a member of the studio in person. |

**Niche blocks** (choose one for the "what we are asking about" paragraph):

| Block | zh-TW (DRAFT for the wife) | English gloss |
| :-- | :-- | :-- |
| **N-F fashion** (face-free) | 以貴品牌提供的商品圖片為基礎，製作標示為「搭配示意」的配色與穿搭示意圖，例如色彩搭配板或平拍商品的版面。每張圖都會註明由 AI 生成；不含任何合身度、舒適度或體型效果的說法；商品外觀與顏色一律以貴品牌提供的資訊為準。 | Colour and outfit illustrations labelled 「搭配示意」, built from the brand's own product pictures, for example a colour-story board or a flat-lay layout. Every image says it is AI-generated; there is no claim about fit, comfort or body effect; the garment's look and colour always go by the information the brand provides. |
| **N-H home** | 以貴品牌公開的尺寸與容量資料，製作標示為「示意圖」的尺寸圖解（向量圖），讓消費者在購買前先量好空間。我們不使用擬真的房間渲染圖，也不加入貴品牌無法以文件佐證的說法。 | Dimension diagrams (vector drawings) labelled 「示意圖」, built from the brand's published sizes and capacities, so shoppers can measure before they buy. We do not use photoreal room renders and add no claim the brand cannot support with a document. |
| **N-T tools** | 針對貴公司公開的某一項功能，製作有標示日期與資料來源的圖卡式功能說明，並附上「測試條件」（工具、版本、方案、日期）。我們只提供靜態圖卡，不含影片與語音。 | A card-style explainer of one published feature, with a date and source line and a 「測試條件」 line (tool, version, plan, date). Static cards only; no video and no voice. |

---

## 3. T1. First contact: brand (also software vendors; use N-T for those)

**Subject (zh-TW):** 【合作詢問】公開標示的 AI 虛擬角色創作｜[STUDIO LEGAL NAME / REGISTRATION: TO FILL]
**Gloss:** [Collaboration enquiry] Openly labelled AI virtual-character creative | studio name

| zh-TW (DRAFT for the wife) | English gloss |
| :-- | :-- |
| [RECIPIENT / TEAM NAME: TO FILL] 您好： | Dear [recipient or team]: |
| 打擾了。{{B-INTRO}} | Sorry to trouble you. {{B-INTRO}} |
| 寫信給貴品牌，是因為 [WHY THIS RECIPIENT: ONE TRUE SENTENCE TO FILL]。想請教貴品牌是否有興趣評估一種做法：[NICHE BLOCK: 選用 N-F、N-H 或 N-T 其中一段]。 | I am writing because [one true sentence about the recipient]. May I ask whether you would be interested in evaluating one approach: [one niche block]. |
| {{B-STATUS}} | {{B-STATUS}} |
| {{B-RULES}} | {{B-RULES}} |
| {{B-SAMPLE-OPT}} | {{B-SAMPLE-OPT}} |
| 若方便，想請教貴品牌負責合作提案的窗口，或較適合的聯絡方式。 | If convenient, could you tell us who handles collaboration proposals, or the better way to reach them. |
| {{B-OPTOUT}} | {{B-OPTOUT}} |
| {{B-CLOSE}}<br>{{B-SIG}} | {{B-CLOSE}}<br>{{B-SIG}} |

(`{{B-...}}` means paste the block of that name from section 2 unchanged; `check_outreach.py` expands these markers before it scans the text.)

---

## 4. T2. First contact: agency, platform or vendor (supplier or partner route)

Three versions of the middle paragraph; keep one. The rest is the same as T1.

**Subject (zh-TW):** 【合作詢問】公開標示的 AI 虛擬角色圖像製作（外包或轉介）｜[STUDIO LEGAL NAME / REGISTRATION: TO FILL]
**Gloss:** [Collaboration enquiry] Openly labelled AI virtual-character image production (subcontract or referral) | studio name

| zh-TW (DRAFT for the wife) | English gloss |
| :-- | :-- |
| [RECIPIENT / TEAM NAME: TO FILL] 您好： | Dear [recipient or team]: |
| 打擾了。{{B-INTRO}}我們不是代理商，也不經紀任何創作者；只是一間小型製作工作室，製作公開標示的 AI 虛擬角色與靜態圖像內容。 | Sorry to trouble you. {{B-INTRO}} We are not an agency and do not represent any creator; we are only a small production studio that makes openly labelled AI virtual characters and still-image content. |
| **Version A, agency:** 寫信給貴公司，是因為 [WHY THIS RECIPIENT: ONE TRUE SENTENCE TO FILL]。想請教：貴公司的客戶（[CLIENT CATEGORY: TO FILL，例如 服飾、居家、軟體]）是否曾詢問過「公開標示的 AI 虛擬角色」形式的內容？若有，我們願意以外包製作或轉介的方式提供靜態圖像，例如：[NICHE BLOCK: 選用 N-F、N-H 或 N-T 其中一段]。 | **Version A, agency:** I am writing because [one true sentence]. May I ask whether your clients ([client category]) have ever asked for content in the form of an "openly labelled AI virtual character"? If so, we would supply still images on a subcontract or referral basis, for example: [one niche block]. |
| **Version B, platform or media:** 寫信給貴公司，是因為 [WHY THIS RECIPIENT: ONE TRUE SENTENCE TO FILL]。想請教貴公司是否有接受「公開標示的 AI 虛擬角色」帳號或內容的廣告主、創作者或內容合作管道；若有，應向哪個窗口提出。我們可提供的內容例如：[NICHE BLOCK: 選用 N-F、N-H 或 N-T 其中一段]。 | **Version B, platform or media:** I am writing because [one true sentence]. May I ask whether you have an advertiser, creator or content-partnership route that accepts an openly labelled AI-virtual-character account or content; if so, whom to approach. What we could provide, for example: [one niche block]. |
| **Version C, software vendor or SaaS partner programme:** 寫信給貴公司，是因為 [WHY THIS RECIPIENT: ONE TRUE SENTENCE TO FILL]。想請教貴公司是否有合作夥伴或轉介計畫，可接受我們製作貴公司公開功能的圖卡式說明（[NICHE BLOCK: 使用 N-T]）。 | **Version C, software vendor or SaaS partner programme:** I am writing because [one true sentence]. May I ask whether you have a partner or referral programme that could accept our card-style explainers of your published features ([N-T block]). |
| {{B-STATUS}} | {{B-STATUS}} |
| {{B-RULES}} | {{B-RULES}} |
| {{B-SAMPLE-OPT}} | {{B-SAMPLE-OPT}} |
| {{B-RATESHEET-OPT}} | {{B-RATESHEET-OPT}} |
| 若方便，想請教適合接洽這類供應商或合作提案的窗口。 | If convenient, could you tell us who the right contact is for supplier or collaboration proposals of this kind. |
| {{B-OPTOUT}} | {{B-OPTOUT}} |
| {{B-CLOSE}}<br>{{B-SIG}} | {{B-CLOSE}}<br>{{B-SIG}} |

Notes for the sender: (a) do not argue with an agency's view that brands prefer verifiable human creators (the Kolr 2026 report, Phase 1); say only what the studio is; (b) the optional rate-sheet paragraph is an honest information request from a new studio, not a disguised pitch, and it must not be sent to a recipient the operator is also treating as a prospect without saying so; (c) never mention another brand's or agency's name, work or problems (including any public AI-image mistake in Phase 1's notes) to a recipient.

---

## 5. T3. Follow-up (once only, about 7 days after T1 or T2 with no reply)

**Subject (zh-TW):** Re: 【合作詢問】公開標示的 AI 虛擬角色創作｜[STUDIO LEGAL NAME / REGISTRATION: TO FILL]　（同一封信件串；若原本是網站表單，則沿用同一個表單，不加主旨）
**Gloss:** Reply in the same thread (if the first message was a web form, use the same form, with no subject).

| zh-TW (DRAFT for the wife) | English gloss |
| :-- | :-- |
| [RECIPIENT / TEAM NAME: TO FILL] 您好： | Dear [recipient or team]: |
| [DATE SENT: TO FILL] 曾寄信給貴公司，想確認是否已送達適合的窗口。簡單重述：我們是 [STUDIO LEGAL NAME / REGISTRATION: TO FILL]，創作並營運公開標示的 AI 虛擬角色，想了解貴公司是否有興趣評估 [ONE-LINE NICHE: TO FILL，例如：以貴品牌提供的商品圖片製作標示為「搭配示意」的配色示意圖]。 | We wrote to you on [date sent] and want to check that it reached a suitable contact. In short: we are [studio], we create and run openly labelled AI virtual characters, and we would like to know whether you would be interested in evaluating [one-line description of the niche offer]. |
| 若目前不需要，回覆「不需要」即可，我們不會再來信；若有更適合的窗口，也請不吝告知。我們不會重複催促，謝謝您。 | If you do not need this now, simply reply 「不需要」 and we will not write again; if there is a better contact, please tell us. We will not chase you again. Thank you. |
| {{B-SIG}} | {{B-SIG}} |

After this message: no further message to this recipient for 90 days (playbook section 4).

---

## 6. T4. Reply to interest (within 2 business days of a positive reply)

Send only after the wife has read it. Remove any paragraph that does not apply. **No price, no promise, no sample unless the operator chose it and the sample gates are closed.** The studio's one-page offer ([studio-offer.md](../studio-offer.md)) may be attached here, never to T1 or T2, and only as a filled working copy after its own gates close.

**Subject (zh-TW):** Re: （沿用對方信件主旨）
**Gloss:** Re: (keep the recipient's subject)

| zh-TW (DRAFT for the wife) | English gloss |
| :-- | :-- |
| [RECIPIENT NAME OR TEAM: TO FILL] 您好： | Dear [recipient or team]: |
| 謝謝您的回覆，也謝謝貴公司願意花時間了解。 | Thank you for replying and for taking the time. |
| 先再次說明目前的狀況，避免誤會：我們的角色是 AI 生成的虛擬角色，不是真人；工作室剛起步，沒有已完成的合作案例，也沒有追蹤人數或成效數據可以提供；我們不承諾任何曝光、觸及或銷售結果。 | First, to avoid any misunderstanding: our characters are AI-generated, not people; the studio is new and has no finished collaboration and no follower or performance figure to give; we promise no exposure, reach or sales. |
| **If a sample was chosen:** [ONLY IF THE OPERATOR CHOSE: 如果貴公司同意，建議的第一步是一份免費、不公開的小範圍示範內容：範圍為 [SCOPE: TO FILL，例如 1 至 3 張圖]，包含兩次修改，私下傳送給貴公司檢視，不張貼在任何地方，也不附帶任何義務。]<br>**If no sample:** 如果貴公司同意，建議的第一步是先以書面確認合作範圍與雙方需求，再由我們提供書面報價。 | **If a sample was chosen:** [only if the operator chose] If you agree, we suggest as a first step a small free sample in private: scope [scope, for example 1 to 3 images], two rounds of revisions, sent to you privately, posted nowhere, no obligation.<br>**If no sample:** If you agree, we suggest as a first step to confirm the scope and both sides' needs in writing, after which we give a written quote. |
| **What we would need** (keep the line for your niche).<br>**Fashion:** 一至兩項商品的商品圖片（平拍、人台或衣架拍攝；不含真人模特兒的照片）、書面的使用授權、官方色名與成分標示文字、尺寸表。<br>**Home:** 公開的尺寸、容量與承重等規格文件，以及可使用這些資料與商品圖片的書面授權。<br>**Tools:** 要說明的功能頁面、版本與方案資訊，以及同意我們錄製畫面的書面許可。 | **What we would need** (keep your niche's line).<br>**Fashion:** one or two products as product-only pictures (flat lay, mannequin or hanger; no photographs of real models), a written usage licence, the official colour name and composition text, the size chart.<br>**Home:** published specification documents for size, capacity and load, and a written licence to use that data and the product pictures.<br>**Tools:** the feature page to explain, version and plan information, and written permission for us to record the screen. |
| 為了雙方都清楚，先說明我們的作法：(1) 每一項內容需經貴公司逐項書面確認後才會使用；(2) 角色不做使用心得、開箱或推薦；(3) 付費或合作內容一律標示【業配】或【合作內容】，並開啟 AI 標示，這些標示不接受移除或縮小；(4) 貴公司提供的資料與說法，需附來源與日期，並由貴公司確認其正確性；(5) 我們不做與健康、療效、投資理財、賭博或政治相關的內容。 | So that both sides are clear, here is how we work: (1) nothing is used before you approve each item in writing; (2) the character gives no first-hand review, unboxing or recommendation; (3) paid or collaborative content always carries 【業配】 or 【合作內容】 and the AI label, which are not removed or shrunk on request; (4) the information and statements you supply need a source and a date and you confirm they are correct; (5) we do not make content on health, medical effect, investment and finance, gambling or politics. |
| 關於費用：我們會在確認範圍之後再提供書面報價，目前不先報價。另外，工作室目前的登記狀態為 [REGISTRATION STATUS: TO FILL]；正式合作、簽約與開立發票，需在登記與相關程序完成後進行。 | On fees: we give a written quote after the scope is confirmed and do not quote yet. Also, the studio's registration status is [registration status]; formal collaboration, contract and invoicing happen only after registration and related steps are complete. |
| 想請教三件事：(1) 適合接洽的窗口與回覆方式；(2) 貴公司期待的時程；(3) 貴公司是否同意示範內容不公開。 | Three questions: (1) the right contact and how to reach them; (2) the timing you expect; (3) whether you agree that any sample stays private. |
| 如需通話，我們可配合 [TIME WINDOWS: TO FILL]（台北時間）。 | If you would like a call, we can do [time windows] (Taipei time). |
| 若之後不希望再收到我們的信，隨時回覆「不需要」即可。<br>{{B-CLOSE}}<br>{{B-SIG}} | If you ever prefer not to hear from us, reply 「不需要」 at any time. |

---

## 7. T5. Opt-out confirmation (send the same day someone says no, stop or 不需要)

| zh-TW (DRAFT for the wife) | English gloss |
| :-- | :-- |
| [RECIPIENT / TEAM NAME: TO FILL] 您好：已收到您的來信。我們已將貴公司從聯絡名單中移除，之後不會再主動來信。打擾了，謝謝您。<br>[SENDER NAME: TO FILL]　[STUDIO LEGAL NAME / REGISTRATION: TO FILL] | Hello: we have received your message. We have removed your company from our contact list and will not write again. Sorry for the trouble, and thank you. |

Same day: set `do_not_contact` in the tracking sheet and stop (playbook section 5). Do not send a second message asking why.

## 8. T6. Decline a brief we cannot take (a recipient asks for an experience review, a hidden label, or a declined category)

This is the short version for an outreach reply. [decline-list.md](../decline-list.md) section 4 has fuller decline wording for fifteen situations (its template numbers are its own, not T1 to T6 here); use whichever fits and let the wife read it.

| zh-TW (DRAFT for the wife) | English gloss |
| :-- | :-- |
| [RECIPIENT / TEAM NAME: TO FILL] 您好： | Dear [recipient or team]: |
| 謝謝您的來信與提案。經過內部檢視，其中的 [WHICH ITEM: TO FILL，例如 使用心得或體驗類內容、移除 AI 標示、某類產品的說明] 不在我們能承接的範圍：我們的角色是 AI 生成的虛擬角色，沒有實際使用過任何商品，也不製作這類內容。 | Thank you for your message and proposal. After an internal review, [the item] is outside what we can take on: our characters are AI-generated, have not used any product in person, and we do not make this kind of content. |
| 若貴公司願意調整為 [WHAT WE CAN DO: TO FILL，例如 依公開規格與資料的功能說明、標示為示意的圖解]，我們很樂意再討論；若不方便，也謝謝您的考量。 | If you are willing to change it to [what we can do], we would be glad to discuss further; if not, thank you for considering us. |
| {{B-SIG}} | {{B-SIG}} |

---

## 9. For the wife: points to rule on, and wording never used

**To rule on.** (1) Greeting and register: [RECIPIENT / TEAM NAME] 您好 and 貴公司 versus 貴品牌 for each kind of recipient. (2) Whether 「AI 虛擬角色」 is the right term for a business reader, or 「虛擬角色」 with 「AI 生成」 next to it. (3) Whether 「商祺」 suits a retailer, a platform and a software vendor alike. (4) Whether 「不需要」 is the most natural one-word opt-out, or 「不用了」, 「請勿再聯絡」. (5) Whether the free-sample paragraph reads as generous or as pushy. (6) Whether naming a free private sample in a first message to a large company or a multinational is wise. (7) Whether the sentence about the labels 「不接受移除或縮小」 is too blunt for a first message (it can move to T4). (8) Whether a sender needs to give a registered address in the signature (a 記帳士 and lawyer point; do not default to a home address, studio kit section 10).

**Wording never used in a draft** (the checker looks for these): any claim of experience or use by the character or the studio (用過, 穿過, 試過, 愛用, 實測, 開箱, 心得); any client, case, result, follower, reach or engagement figure; superlatives and guarantees (最好, 第一, 保證, 一定); urgency (限時, 最後機會); health, medical, weight-loss, cosmetic-efficacy, investment, gambling or political wording except where a draft states that the studio does not make it (T4 item 5, T6); mainland vocabulary and Simplified characters.

**Lawyer and 記帳士 points raised by these drafts** (unverified): whether a first-contact B2B email needs more than the opt-out line; what the signature must contain before registration; whether offering a free sample to a company's employees has any gift or tax consequence; whether a free sample posted publicly is an advertisement (already `HUMAN_TODO.md` 27, 37). See [outreach-playbook.md](outreach-playbook.md) section 8.
