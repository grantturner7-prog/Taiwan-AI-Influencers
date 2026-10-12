#!/usr/bin/env python3
"""Tests for check_kits.py and kit_figures.py. Standard library only; writes only to a temporary folder.

    python3 -B -m unittest discover -s monetisation/media-kits -p "test_check_kits.py" -v
"""
from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import check_kits as ck  # noqa: E402
import kit_figures as kf  # noqa: E402

BASE = (HERE / "fangcun.md").read_text(encoding="utf-8")
ANCHOR = "## 11. 報價"


def run_template(text: str, name: str = "fangcun.md"):
    ck.errors.clear(); ck.warns.clear(); ck.infos.clear()
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / name
        p.write_text(text, encoding="utf-8")
        ck.check_template(p, False)
    return list(ck.errors)


def inject(line: str) -> str:
    assert ANCHOR in BASE
    return BASE.replace(ANCHOR, line + "\n\n" + ANCHOR, 1)


class TemplateChecks(unittest.TestCase):
    def test_the_four_kits_pass(self):
        for k in ck.KITS:
            with self.subTest(kit=k):
                self.assertEqual(run_template((HERE / k).read_text(encoding="utf-8"), k), [])

    def test_invented_facts_are_caught(self):
        cases = {
            "price": "價格 NT$5,000 起",
            "currency word": "新台幣 3000 元",
            "followers": "目前有 1,200 追蹤者",
            "subscribers": "ten 1200 subscribers",
            "email": "聯絡 abc@example.com",
            "phone": "電話 02-1234-5678",
            "business id": "統一編號 12345678",
            "24 hours": "我們承諾 24 小時內下架",
            "24 hours english": "taken down within 24 hours",
        }
        for label, line in cases.items():
            with self.subTest(case=label):
                self.assertTrue(run_template(inject(line)), f"{label} was not caught")

    def test_zh_tw_problems_are_caught(self):
        for label, line in {"simplified": "这是视频", "mainland word": "請看視頻", "mainland word 2": "請看信息"}.items():
            with self.subTest(case=label):
                self.assertTrue(run_template(inject(line)))

    def test_pronoun_for_the_character_is_caught_but_compounds_are_not(self):
        bad = BASE.replace("| 方寸是由明說角色工作室創作與營運的 AI 虛擬角色，不是真人。 |", "| 她是由明說角色工作室創作與營運的 AI 虛擬角色，不是真人。 |", 1)
        self.assertNotEqual(bad, BASE)
        self.assertTrue(run_template(bad))
        self.assertEqual(run_template(inject("其他品牌與排他條款")), [])

    def test_data_cell_must_stay_the_empty_placeholder(self):
        old = "| 追蹤者或訂閱者數（期末）/ Followers or subscribers at period end | 【待填】 [TO FILL WHEN REAL] |"
        self.assertIn(old, BASE)
        bad = BASE.replace(old, old.replace("【待填】 [TO FILL WHEN REAL]", "1,234"), 1)
        self.assertTrue(any("data cell" in e for e in run_template(bad)))

    def test_placeholder_must_exist_in_both_languages(self):
        old = "| 【待填：工作室信箱（尚未建立）】 | [TO FILL WHEN REAL: studio mailbox (not yet created)] |"
        self.assertIn(old, BASE)
        bad = BASE.replace(old, "| 【待填：工作室信箱（尚未建立）】 | studio mailbox |", 1)
        self.assertTrue(any("only one language" in e for e in run_template(bad)))

    def test_structure_is_enforced(self):
        self.assertTrue(run_template(BASE.replace("## 6. 角色做什麼", "## 66. 角色做什麼", 1)))
        self.assertTrue(run_template(BASE.replace("## Part A", "## Part Z", 1)))

    def test_bilingual_rows_need_both_scripts(self):
        old = "| 方寸是由明說角色工作室創作與營運的 AI 虛擬角色，不是真人。 | 方寸 is an AI-generated virtual character created and run by Plainspoken Studio (明說角色工作室). It is not a real person. |"
        self.assertIn(old, BASE)
        bad = BASE.replace(old, "| 方寸是由明說角色工作室創作與營運的 AI 虛擬角色，不是真人。 | 方寸是虛擬角色 |", 1)
        self.assertTrue(any("no Latin letters" in e for e in run_template(bad)))

    def test_missing_repo_path_is_caught(self):
        self.assertTrue(run_template(BASE.replace("`analytics/README.md`", "`analytics/NOPE.md`", 1)))


class FilledMode(unittest.TestCase):
    def run_filled(self, text: str):
        ck.errors.clear(); ck.warns.clear(); ck.infos.clear()
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "filled.md"
            p.write_text(text, encoding="utf-8")
            ck.check_filled(p)
        return list(ck.errors)

    def test_template_is_not_send_ready(self):
        self.assertGreater(len(self.run_filled(BASE)), 20)

    def test_clean_copy_passes(self):
        self.assertEqual(self.run_filled("# 方寸｜合作簡介\n\n| 欄位 | 內容 |\n|---|---|\n| 追蹤者 | 見截圖 |\n"), [])

    def test_each_marker_is_caught(self):
        for marker in ("【待填：x】", "[TO FILL WHEN REAL: x]", "OPERATOR ONLY", "［D8］", "[D8]", "［待確認］", "[C2]", "## Part A", "## 附錄 C"):
            with self.subTest(marker=marker):
                self.assertTrue(self.run_filled(f"hello {marker} world\n"))


class KitFigures(unittest.TestCase):
    def call(self, argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = kf.main(argv)
        return code, out.getvalue()

    def test_bad_dates(self):
        self.assertEqual(self.call(["--start", "2026-13-01", "--end", "2026-12-01"])[0], 2)
        self.assertEqual(self.call(["--start", "2026-12-10", "--end", "2026-12-01"])[0], 2)

    def test_missing_real_database_stops_cleanly(self):
        code, out = self.call(["--start", "2026-12-01", "--end", "2026-12-28", "--db", str(HERE / "no-such.db")])
        self.assertEqual(code, 1)
        self.assertIn("database not found", out)

    @unittest.skipUnless(kf.tracker.DEMO_DB.exists(), "DEMO database not present")
    def test_demo_database_needs_the_flag_and_carries_a_banner(self):
        code, out = self.call(["--start", "2026-12-01", "--end", "2027-01-04", "--db", str(kf.tracker.DEMO_DB)])
        self.assertEqual(code, 1)
        self.assertIn("DEMO", out)
        code, out = self.call(["--demo", "--persona", "fangcun", "--start", "2026-12-01", "--end", "2027-01-04"])
        self.assertEqual(code, 0)
        self.assertIn("DEMO DATA", out)
        self.assertIn("not reported by platform", out)  # YouTube Shorts saves are blank in the demo data

    @unittest.skipUnless(kf.tracker.DEMO_DB.exists(), "DEMO database not present")
    def test_the_database_is_opened_read_only(self):
        before = kf.tracker.DEMO_DB.stat().st_mtime_ns
        self.call(["--demo", "--start", "2026-12-01", "--end", "2027-01-04"])
        self.assertEqual(kf.tracker.DEMO_DB.stat().st_mtime_ns, before)


if __name__ == "__main__":
    unittest.main()
