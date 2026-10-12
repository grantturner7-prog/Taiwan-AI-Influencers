"""Shared helpers for the unit tests (standard library only). Not part of the pipeline itself."""
import csv
import tempfile
from pathlib import Path

import provenance
import reviewqueue


def make_root(extra_personas=()):
    """A throw-away project folder with personas/<slug>/bible.md for every known persona and an empty
    provenance.csv (header only). Returns (TemporaryDirectory, Path)."""
    tmp = tempfile.TemporaryDirectory()
    root = Path(tmp.name)
    for slug in list(reviewqueue.PERSONAS) + list(extra_personas):
        (root / "personas" / slug).mkdir(parents=True)
        (root / "personas" / slug / "bible.md").write_text("# test\n", encoding="utf-8")
        (root / "assets" / slug / "photoreal").mkdir(parents=True)
    (root / "assets").mkdir(exist_ok=True)
    with open(root / "assets" / "provenance.csv", "w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerow(provenance.COLUMNS)
    return tmp, root


def good_post(**over):
    """A post.json that should pass validate with no ERROR or FLAG (fangcun, Instagram carousel)."""
    p = {
        "id": "fangcun-2026-11-16-01",
        "persona": "fangcun",
        "platform": "instagram",
        "format": "carousel",
        "scheduled_date": "2026-11-16",
        "pillar": "尺寸算給你看",
        "hook_zh": "小套房家具放不下？先算這三個數字",
        "caption_zh": ("【AI 虛擬角色】本篇由 AI 生成的虛擬角色「方寸」發布，圖像為 AI 生成，並非真人。\n"
                       "床、衣櫃、門的開啟範圍，三個尺寸加在一起，才知道走道還剩多少。"
                       "這篇用示意數字示範計算方式，收藏起來，量自己房間的時候照著填～"),
        "caption_gloss_en": "TEST ONLY. Can't fit the furniture? Add up three dimensions first.",
        "hashtags": ["#收納", "#小宅"],
        "on_screen_label_zh": "AI 生成｜虛擬角色",
        "ai_label_flag": True,
        "sponsorship_flag": False,
        "sponsorship_type": "none",
        "sources": [],
        "media": [{"path": "PENDING", "description": "TEST: studio portrait beside a diagram",
                   "shot_prompt": "An original adult woman, plain warm off-white studio backdrop, waist-up, hands outside the frame."}],
        "review": {"wife_language": "pending", "operator_facts": "pending", "approved": False, "notes": ""},
    }
    p.update(over)
    return p


def write_draft(root, post=None, number=1):
    """Scaffold a draft with reviewqueue.new_draft, then replace post.json with `post`."""
    post = post or good_post()
    folder = reviewqueue.new_draft(root, post["persona"], post["platform"], post["format"],
                                   post["scheduled_date"], post["pillar"], number)
    reviewqueue.write_post(folder / "post.json", post)
    return folder
