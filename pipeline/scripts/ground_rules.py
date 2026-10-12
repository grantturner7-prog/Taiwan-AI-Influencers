#!/usr/bin/env python3
"""ground_rules.py - shared, deliberately blunt text scanners for the pipeline.

Standard library only. Used by reviewqueue.py (and tested in test_ground_rules.py).

WHAT THIS IS: a keyword/regex net that FLAGS wording a human must look at. It never
rewrites text ("flag, do not auto-fix") and it can both miss things and flag harmless
things. It is NOT a replacement for the wife's language review or the operator's fact
check, and it is NOT legal clearance.

Where the word lists come from (all project files, none verified against a primary
source):
  * lived-experience words: research/culture.md 2.3, personas/fangcun/bible.md 3.4
  * mainland vocabulary: research/culture.md 3.1 (high-confidence rows -> FLAG,
    medium-confidence "both forms heard in Taiwan" rows -> WARN)
  * health / finance / gambling / politics: BRIEF.md section 3 rule 6, strategy/portfolio.md 2C
  * Simplified characters: a hand-made list of characters that are NOT in the Big5
    (Taiwan) repertoire, plus a few clearly-simplified ones that Big5 also carries.
    It is incomplete by nature; the wife reads every character anyway.

Every zh-TW word below is an AI draft list for the wife to correct.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

# --------------------------------------------------------------------------- findings

LEVELS = ("ERROR", "FLAG", "WARN", "INFO")


@dataclass(frozen=True)
class Finding:
    """One thing a human should look at.

    ERROR = breaks the post format or a hard rule; FLAG = banned wording found, human must
    edit it; WARN = advisory; INFO = context note (for example a denial sentence).
    """

    level: str
    code: str
    field: str
    message: str

    def render(self) -> str:
        return f"{self.level:<5} {self.code:<18} {self.field}: {self.message}"


# --------------------------------------------------------------------------- word lists

# Lived-experience wording (Ground rule 4). A virtual character has not tried, worn, eaten
# or used anything. Plain substrings.
LIVED_ZH = [
    "愛用", "回購", "開箱", "實測", "親測", "試用", "試穿", "試吃", "心得", "踩雷", "避雷",
    "神器", "必買", "好用", "改造", "我家", "我的房間", "我租的", "今天穿", "今日穿搭",
    "我今天", "上身", "穿起來", "用起來", "吃起來", "住起來", "坐起來", "睡起來",
    "打卡", "我量", "我測", "GRWM", "OOTD", "vlog", "我的一天", "日常記錄",
    "組裝心得", "使用心得",
    # added in the Phase 4 review: invented-life nouns and "I experienced it myself" phrases
    "我的衣櫃", "我的衣服", "我的穿搭", "我的家", "我的房子", "我的公寓", "我的書桌", "我的桌面", "我的電腦",
    "我的手機", "我的日常", "我的生活", "親自體驗", "親身體驗", "親身", "自己用過", "自己試過", "自己穿過",
    "實際使用後", "使用後發現", "用完發現", "穿完發現",
]
# Experience-aspect verbs with no 'I' in sight ("這個角色用過", "如果你用過"). WARN only: the subject decides
# whether it is a claim, and a human has to read it.
LIVED_ASPECT_ZH = ["用過", "穿過", "吃過", "試過", "買過", "去過", "住過", "使用過", "體驗過", "測試過"]
_ADV = (r"(?:剛|剛剛|已經|有|曾|曾經|才|還|也|都|昨天|今天|昨日|前天|上週|上周|上個月|最近|之前|先前|以前|前陣子|"
        r"早就|每天|每週|每周|每次|平常|常常|常|經常|一直|正在|現在|目前|親自|實際|確實|真的|已|又|再|先|後來|終於)*")
_VERB = r"(?:試|用|使用|吃|喝|穿|戴|買|去|住|測|測試|逛|練|跑|睡|坐|量|裝|租|搬|體驗)"

# Regex patterns for first-person experience claims.
LIVED_ZH_RE = [
    # 我試了 / 我用過 / 我去了 / 我剛買了 / 我已經穿過 ...
    (r"我" + _ADV + _VERB + r"(?:了|過|到|著|完)",
     "first-person experience claim (我...了/過)"),
    # 我在用 / 我正在使用 / 我每天都用 / 我平常都穿 (habitual or ongoing use)
    (r"我" + _ADV + r"(?:在|正在)" + _VERB, "first-person ongoing-use claim (我在用...)"),
    (r"我(?:每天|每週|每周|平常|常常|常|經常|一直|都|也)+" + _VERB, "first-person habitual-use claim (我每天都用...)"),
    # 用了三個月 / 穿了兩週 / 試了30天
    (r"(?:用|穿|試|吃|喝|住|睡|坐|玩|養)了?[一二三四五六七八九十百兩\d]+(?:個?月|週|周|天|年|次|趟)",
     "duration-of-use claim"),
    (r"(?:連續|持續)[一二三四五六七八九十百兩\d]+(?:個?月|週|周|天)", "duration-of-use claim"),
]

LIVED_EN_RE = [
    (r"\bI\s+(?:have\s+|'ve\s+)?(?:tried|tested|used|wore|worn|ate|eaten|bought|visited|stayed|tasted|owned|own)\b",
     "first-person experience claim (English)"),
    (r"\bI(?:'ve| have)\s+been\s+(?:using|wearing|eating|testing)\b", "first-person experience claim (English)"),
    (r"\b(?:my\s+(?:flat|apartment|room|wardrobe|closet|desk|home)|in my experience|personally tested|unboxing|day in the life)\b",
     "invented-life wording (English)"),
]

# Phrases that deny an experience. Used to downgrade a hit to INFO (never to hide it).
NEGATORS = (
    "沒有", "沒辦法", "沒能", "沒在", "不是", "並非", "並沒有", "不曾", "未曾", "從未", "從來沒", "從沒",
    "尚未", "無法", "不能", "不會", "不代表", "並不", "不做", "不談", "不講", "不提", "不說",
)
CLAUSE_BREAKS = "，。！？；：、\n,.;!?:"

# Mainland vocabulary. High-confidence rows of culture.md 3.1 -> FLAG.
MAINLAND_HIGH = {
    "視頻": "影片", "短視頻": "短影音", "信息": "資訊", "博主": "網紅 / 創作者", "博客": "部落格",
    "點贊": "按讚", "私信": "私訊", "帖子": "貼文", "發帖": "發文", "社交媒體": "社群媒體",
    "快拍": "限時動態", "表情包": "貼圖 / 迷因圖", "網絡": "網路", "賬號": "帳號", "賬戶": "帳戶",
    "賬單": "帳單", "登錄": "登入", "鏈接": "連結", "軟件": "軟體", "硬件": "硬體", "鼠標": "滑鼠",
    "屏幕": "螢幕", "內存": "記憶體", "默認": "預設", "設置": "設定", "打印": "列印",
    "分辨率": "解析度", "激活": "啟用", "兼容": "相容", "郵箱": "信箱", "服務器": "伺服器",
    "數據庫": "資料庫", "人工智能": "人工智慧", "數字化": "數位化", "數字人": "數位人",
    "充電寶": "行動電源", "移動支付": "行動支付", "二維碼": "QR Code", "軟廣": "業配",
    "商單": "業配", "恰飯": "業配", "質量": "品質", "性價比": "CP值", "外賣": "外送",
    "便利店": "便利商店 / 超商", "轉賬": "轉帳", "項目": "專案 / 內容 / 重點", "反饋": "回饋",
    "身份證": "身分證", "地鐵": "捷運", "公交車": "公車", "出租車": "計程車", "小區": "社區",
    "塑料": "塑膠", "衛生間": "洗手間", "煤氣": "瓦斯", "電飯煲": "電鍋", "厘米": "公分",
    "平方米": "平方公尺", "公元": "西元", "普通話": "國語", "土豆": "馬鈴薯", "西紅柿": "番茄",
    "紅薯": "地瓜", "西蘭花": "青花菜", "菠蘿": "鳳梨", "獼猴桃": "奇異果", "酸奶": "優格",
    "奶酪": "起司", "方便麵": "泡麵", "盒飯": "便當", "雪糕": "冰棒", "薯片": "洋芋片",
    "俯臥撐": "伏地挺身", "力量訓練": "肌力訓練", "動感單車": "飛輪", "連衣裙": "洋裝",
    "衛衣": "帽T", "打底褲": "內搭褲", "人字拖": "夾腳拖", "雙肩包": "後背包", "斜挎包": "斜背包",
    "面料": "布料", "周年慶": "週年慶", "給力": "讚 / 厲害", "牛逼": "厲害", "家人們": "大家",
    "寶子": "大家", "絕絕子": "(mainland slang)", "yyds": "(mainland slang)", "種草": "推薦 (no experience wording)",
    "安利": "推薦", "剁手": "手滑", "栓Q": "(mainland slang)", "鍛煉": "鍛鍊",
    # added in the Phase 4 review (AI-tools and home topics); the wife confirms each
    "硬盤": "硬碟", "插件": "外掛 / 擴充功能", "字節": "位元組", "寬帶": "寬頻",
    "不銹鋼": "不鏽鋼", "平米": "坪 / 平方公尺",
    "網盤": "雲端硬碟", "雲盤": "雲端硬碟", "U盤": "隨身碟", "優盤": "隨身碟", "文本框": "文字方塊",
}

# Medium-confidence: both forms are heard in Taiwan or the contrast is soft -> WARN only.
MAINLAND_SOFT = {
    "關注": "追蹤 (as 'follow')", "評論": "留言", "轉發": "分享 / 轉貼", "保存": "儲存",
    "支持": "支援 (software)", "快遞": "宅配", "酒店": "飯店 / 旅館", "空調": "冷氣",
    "摩托車": "機車", "打車": "叫車", "積分": "點數", "錢包": "皮夾", "墨鏡": "太陽眼鏡",
    "瑜伽": "瑜珈", "拉伸": "伸展", "熱身": "暖身", "硬拉": "硬舉", "乾貨": "重點整理",
    "攻略": "懶人包", "靠譜": "可靠", "吐槽": "(reviewer to rule)", "小姐姐": "(reviewer to rule)",
    "小哥哥": "(reviewer to rule)", "閨蜜": "好姊妹", "爆款": "(reviewer to rule)",
    "硬核": "(reviewer to rule)", "賦能": "(reviewer to rule)", "落地": "(reviewer to rule)",
    "優化": "最佳化", "周年": "週年",
    "用戶": "使用者", "代碼": "程式碼", "程序": "程式", "文檔": "文件", "智能": "智慧", "搜索": "搜尋",
    "界面": "介面", "接口": "介面 / API", "運行": "執行", "訪問": "存取 / 瀏覽", "刷新": "重新整理",
    "裝修": "裝潢", "氛圍感": "(mainland slang; reviewer to rule)", "顏值": "(reviewer to rule)",
    "高級感": "(reviewer to rule)", "鬆弛感": "(mainland slang; reviewer to rule)", "松弛感": "(Simplified/mainland)",
    "渠道": "管道", "賽道": "領域", "落地頁": "(mainland)", "戶型": "格局 / 房型", "租房": "租屋", "高清": "高畫質",
}

# Characters that are Simplified-only (or Simplified in practice) and so should never appear
# in zh-TW copy. Built from characters that Python's 'big5' codec cannot encode, plus a few
# clearly-Simplified ones that Big5 carries as variants. Deliberately omits ambiguous
# characters that are also valid in Traditional writing (台 里 后 干 云 面 只 表 制 范 划 洒 涂 胜 适 ...).
SIMPLIFIED_ONLY = (
    "们这个为说时国对会学实见现应无过还进动开关门问间长车东视频质资讯软数库电脑场总经营业务费买卖货财产样"
    "点线单页条给让认记许论设计该试语误请谢读调谈谁转输达边运远连选递钱银铁链错针钟镜阅难顺须预领题额风飞"
    "饭馆馈鱼鸟麦黄齐龙龄岁属币帮师带帐张归当录态惯战户扩护报担拥择换损摄敌断旧显暂术杂标栏桥档检欢毕汇汉"
    "沟没济浏测湿满滚灭灯热爱爷牵状独环画疗监码礼称稳竞笔纸级纪约红纤组细织终结绘统继续维综绿缘罗艺节药获"
    "虑虽补装览观规觉订讨训议讲证评识译变贝负贡责败购贴贵赚赛赞赠迁迟钉闲阳阴阶际陆陈队专两严临丽举义乐书"
    "乱争亏亚亲仅从仓众传伤侧俭储兰兴养兽写军农冲决况冻净凉减凤击刘则刚创删别剧劝办励势区医华协卫厅历厉压"
    "县参双叙叶号叹吗启员响哑唤园围图圆块坚坛垫墙壮声壳处备够头夹夺奋奖妇妈妆娱孙宝宠审宫宽宾寻导将尔尘尝"
    "层岛岗峡帅广庆废弃弹彻径忆忧恋恶戏执扫扬抢拟拦挤捡摆摇撑权杀杨枪树栈梦楼横欧毁汤沪泪泽浅浓涨润渐湾滤"
    "灵灾炉炼烂烦烧猪献畅疯盘础祸积穷窃简类粮紧纯纲纳纵纷练绍络绝绩缓编缩罚职联聪肃肠肤肿脚脸舰舱艰苏莱蓝"
    "虚蚁访词诗话详课账贸贺赋赏赖赵趋跃轨轮轻载较辅辆辈辉邮邻郑酿释钓钢钥钮铃铜铺销锁锅键镇闪闭闯闷闹阵随"
    "隐雏顶项顾顿颜饮饰饱饼驱驶驻骑骗骤鲜鸡鸭鸿齿龟网体据机种价气极构确离赶优儿吨圣坏怀惊扰挂柜洁苹茧荐触晒厂"
)
SIMPLIFIED_SET = frozenset(SIMPLIFIED_ONLY)

# Health, medical, weight-loss and cosmetic-efficacy wording (Ground rule 6).
HEALTH_HIGH = [
    "瘦身", "減脂", "減肥", "燃脂", "燃燒脂肪", "顯瘦", "遮肉", "瘦小腹", "瘦腿", "美白", "淡斑",
    "除皺", "抗老", "緊緻", "排毒", "療效", "治療", "治癒", "根治", "消炎", "殺菌", "抗菌", "防霉",
    "防蟎", "除濕效果", "空氣更乾淨", "過敏", "失眠", "助眠", "降血糖", "降血壓", "增強免疫",
    "提升免疫", "養生", "保健", "痠痛", "抗痘", "護膚", "改善體質",
    "睡眠", "變瘦", "會瘦", "更瘦", "減重", "體脂", "紓壓", "舒壓", "減壓", "緩解", "對身體好", "有益健康",
]
HEALTH_RE = [
    (r"瘦\s*[一二三四五六七八九十\d]+\s*(?:公斤|kg|KG|斤)", "weight-loss result"),
    (r"[一二三四五六七八九十\d]+\s*(?:週|周|天|個月)\s*(?:瘦|減重|減脂)", "weight-loss timeline"),
]
# Fabric-performance and comfort words: allowed only as the brand's own published spec,
# quoted and dated (portfolio.md 2C). WARN so a human checks the source.
HEALTH_SOFT = [
    "透氣", "排汗", "抗UV", "吸濕", "涼感", "防潑水", "保暖", "防曬", "舒適", "舒服", "修身", "顯高",
    "瘦", "顯胖", "胖", "身材", "體型",  # body-shape wording: a human decides whether it is a cosmetic or body claim
]

FINANCE_HIGH = [
    "投資", "理財", "股票", "股市", "基金", "ETF", "存股", "當沖", "融資", "期貨", "選擇權", "外匯",
    "加密貨幣", "虛擬貨幣", "比特幣", "幣圈", "報酬率", "年化報酬", "獲利", "賺錢", "穩賺", "保證獲利",
    "被動收入", "財富自由", "副業", "躺賺", "月入", "貸款", "信貸", "保險", "信用卡", "買進", "賣出",
    "停利", "停損", "配息", "殖利率", "定期定額", "債券", "年金",
]
GAMBLING_HIGH = ["賭", "博弈", "下注", "娛樂城", "百家樂", "彩券", "運動彩券", "運彩", "威力彩", "大樂透", "老虎機"]
GAMBLING_SOFT = ["抽卡", "轉蛋", "課金"]

POLITICS_HIGH = [
    "選舉", "選情", "投票", "政黨", "國民黨", "民進黨", "民眾黨", "時代力量", "總統", "立委", "立法委員",
    "候選人", "兩岸", "統獨", "台獨", "中共", "共產黨", "習近平", "賴清德", "蔡英文", "柯文哲", "韓國瑜",
    "侯友宜", "朱立倫", "白色恐怖", "公投", "罷免", "政治",
]
POLITICS_SOFT = ["藍綠", "藍白", "市長", "縣市長"]

# Fake popularity (Ground rule 7): follow-for-follow / like-for-like and bought engagement.
FAKE_POPULARITY = [
    "互粉", "互讚", "互追", "互相追蹤", "回追", "買粉", "刷讚", "f4f", "l4l", "like4like",
    "follow4follow", "followback", "follow4followback", "sfs", "互助",
]

# Wording that undermines the "openly virtual" disclosure (Ground rule 1).
UNDISCLOSING = ["真人實拍", "真人出鏡", "真人出境", "我是真人", "非AI", "不是AI", "實拍", "純素人",
                "非 AI", "不是 AI", "真人拍攝", "真人示範", "真人演出", "真人代言", "本人出鏡", "本人實測", "沒有用 AI",
                "沒用 AI", "未使用 AI", "不是虛擬", "並非虛擬"]

# Unsourced superlatives and guarantees (portfolio.md 2C; bible 3.4).
SUPERLATIVES = ["最好", "第一名", "最划算", "最便宜", "保證", "絕對", "一定放得下", "一定進得去"]

# --------------------------------------------------------------------------- claim detection

STRONG_CLAIM_WORDS = [
    "官方", "公告", "資料日期", "根據", "依據", "出處", "統計", "調查", "研究", "報導", "規定", "法規",
    "條文", "辦法", "補助", "價格", "售價", "定價", "NT$", "版本", "更新", "規格", "公布", "公佈",
]
_DIGIT_RE = re.compile(r"[0-9０-９]")


def has_strong_claim(text: str) -> bool:
    """True if the text uses source-dependent wording (official, spec, price, rule ...) that is not
    itself denied ('沒有外部出處' does not count as a claim)."""
    for w in STRONG_CLAIM_WORDS:
        for m in re.finditer(re.escape(w), text):
            if not _is_denied(text, m.start()):
                return True
    return False


def has_numeric(text: str) -> bool:
    return bool(_DIGIT_RE.search(text))


# --------------------------------------------------------------------------- scanning

def _ctx(text: str, start: int, end: int, pad: int = 8) -> str:
    s = max(0, start - pad)
    e = min(len(text), end + pad)
    return text[s:e].replace("\n", " / ")


def _is_ascii_term(term: str) -> bool:
    return all(ord(c) < 128 for c in term)


def _term_spans(text: str, term: str):
    if _is_ascii_term(term):
        pat = re.compile(r"(?<![A-Za-z0-9])" + re.escape(term) + r"(?![A-Za-z0-9])", re.IGNORECASE)
    else:
        pat = re.compile(re.escape(term))
    for m in pat.finditer(text):
        yield m.start(), m.end()


def _is_denied(text: str, start: int) -> bool:
    """True if a negator sits in the same clause just before `start`."""
    seg = text[max(0, start - 10):start]
    cut = max((seg.rfind(c) for c in CLAUSE_BREAKS), default=-1)
    seg = seg[cut + 1:]
    if seg.endswith(("沒", "未", "不", "別", "無")):
        return True  # '沒試穿過', '不開箱': the negator is glued to the term. ('沒想到我試用了' is NOT a denial.)
    return any(n in seg for n in NEGATORS)


def _dedupe_spans(hits):
    """hits: list of (start, end, label). Drop hits fully inside a longer hit."""
    hits = sorted(hits, key=lambda h: (h[0], -(h[1] - h[0])))
    out, last_end = [], -1
    for h in hits:
        if h[0] < last_end:
            continue
        out.append(h)
        last_end = h[1]
    return out


def _scan_terms(text, field, terms, level, code, message, *, note_map=None, check_denial=False):
    hits = []
    for term in sorted(set(terms), key=len, reverse=True):
        for s, e in _term_spans(text, term):
            hits.append((s, e, term))
    findings = []
    for s, e, term in _dedupe_spans(hits):
        denied = check_denial and _is_denied(text, s)
        alt = f" Use instead: {note_map[term]}." if note_map and term in note_map else ""
        if denied:
            findings.append(Finding(
                "INFO", code + "_DENIED", field,
                f"'{term}' appears inside what looks like a denial ('...{_ctx(text, s, e)}...'). "
                "Confirm a human agrees it is a disclaimer, not a claim."))
        else:
            findings.append(Finding(level, code, field, f"{message}: '{term}' (...{_ctx(text, s, e)}...).{alt}"))
    return findings


def _scan_regex(text, field, patterns, level, code, *, flags=0, check_denial=False):
    findings = []
    for pat, label in patterns:
        for m in re.finditer(pat, text, flags):
            if check_denial and _is_denied(text, m.start()):
                findings.append(Finding("INFO", code + "_DENIED", field,
                                        f"{label}: '{m.group(0)}' looks denied ('...{_ctx(text, m.start(), m.end())}...'). Confirm."))
            else:
                findings.append(Finding(level, code, field,
                                        f"{label}: '{m.group(0)}' (...{_ctx(text, m.start(), m.end())}...)"))
    return findings


def scan_text(text: str, field: str) -> list[Finding]:
    """Scan one audience-visible string. Returns findings; never changes the text."""
    if not isinstance(text, str) or not text:
        return []
    out: list[Finding] = []

    out += _scan_terms(text, field, LIVED_ASPECT_ZH, "WARN", "LIVED_ASPECT",
                       "experience-aspect verb (check the subject: the character has never used, worn, eaten or tried anything)",
                       check_denial=True)
    out += _scan_terms(text, field, LIVED_ZH, "FLAG", "LIVED_EXPERIENCE",
                       "lived-experience wording (Ground rule 4: a virtual character has not tried, worn, eaten or used anything)",
                       check_denial=True)
    out += _scan_regex(text, field, LIVED_ZH_RE, "FLAG", "LIVED_EXPERIENCE", check_denial=True)
    out += _scan_regex(text, field, LIVED_EN_RE, "FLAG", "LIVED_EXPERIENCE", flags=re.IGNORECASE, check_denial=True)

    out += _scan_terms(text, field, list(MAINLAND_HIGH), "FLAG", "MAINLAND_VOCAB",
                       "mainland vocabulary (zh-TW needed)", note_map=MAINLAND_HIGH)
    out += _scan_terms(text, field, list(MAINLAND_SOFT), "WARN", "MAINLAND_SOFT",
                       "possibly mainland-leaning wording (both forms heard in Taiwan; wife rules)", note_map=MAINLAND_SOFT)

    simp = sorted({c for c in text if c in SIMPLIFIED_SET})
    if simp:
        out.append(Finding("FLAG", "SIMPLIFIED_CHARS", field,
                           "Simplified character(s) found: " + " ".join(simp) + ". zh-TW copy must be Traditional."))

    out += _scan_terms(text, field, HEALTH_HIGH, "FLAG", "HEALTH_CLAIM",
                       "health / medical / weight-loss / cosmetic-efficacy wording (Ground rule 6)", check_denial=True)
    out += _scan_regex(text, field, HEALTH_RE, "FLAG", "HEALTH_CLAIM")
    out += _scan_terms(text, field, HEALTH_SOFT, "WARN", "PERFORMANCE_CLAIM",
                       "fabric-performance / comfort / fit wording: only as the brand's own published spec, quoted and dated")

    out += _scan_terms(text, field, FINANCE_HIGH, "FLAG", "FINANCE_CLAIM",
                       "investment / financial wording (Ground rule 6: no investment or financial advice)", check_denial=True)
    out += _scan_regex(text, field, [(r"[\d.]+\s*[%％]\s*(?:報酬|獲利|收益|年化)", "return claim")], "FLAG", "FINANCE_CLAIM")
    out += _scan_terms(text, field, GAMBLING_HIGH, "FLAG", "GAMBLING", "gambling wording (Ground rule 6)")
    out += _scan_terms(text, field, GAMBLING_SOFT, "WARN", "GAMBLING_ADJACENT", "gacha / gambling-adjacent wording")
    out += _scan_terms(text, field, POLITICS_HIGH, "FLAG", "POLITICS", "politics / elections / cross-strait wording (Ground rule 6)")
    out += _scan_terms(text, field, POLITICS_SOFT, "WARN", "POLITICS_ADJACENT",
                       "could carry a party-colour or political reading")

    out += _scan_terms(text, field, FAKE_POPULARITY, "ERROR", "FAKE_POPULARITY",
                       "fake-popularity wording (Ground rule 7: no follow-for-follow, pods or bought engagement)")
    out += _scan_terms(text, field, UNDISCLOSING, "FLAG", "UNDISCLOSING",
                       "wording that undermines the openly-virtual disclosure (Ground rule 1)", check_denial=True)
    out += _scan_terms(text, field, SUPERLATIVES, "WARN", "SUPERLATIVE",
                       "unsourced superlative or guarantee (state a dated, sourced comparison instead)", check_denial=True)
    return out
