#!/usr/bin/env python3
"""Tests for check_outreach.py and render_lists.py. Standard library only.

    python3 -B monetisation/outreach/test_check_outreach.py
"""
from __future__ import annotations

import csv
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_outreach as co  # noqa: E402
import render_lists as rl  # noqa: E402


def tracking_file(tmp: Path, rows: list[dict]) -> Path:
    path = tmp / "tracking.csv"
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=co.TRACK_COLS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in co.TRACK_COLS})
    return path


def row(**kw):
    base = dict(contact_id="C001", list_id="F03", entity_name="Example Label", niche="fashion", entity_type="brand",
                priority="P1", route="cold", template="T1", sender="wife", wife_checked_zh="Y", compliance_checked="Y",
                first_sent_date="2026-12-01", follow_up_due="2026-12-08", status="sent", channel="web_form")
    base.update(kw)
    return base


class RepoFiles(unittest.TestCase):
    def test_lists_clean(self):
        rep = co.Report()
        co.check_lists(rep)
        self.assertEqual(rep.errors, [])

    def test_generated_pages_current(self):
        rep = co.Report()
        co.check_generated(rep)
        self.assertEqual(rep.errors, [])

    def test_drafts_clean(self):
        rep = co.Report()
        co.check_drafts(rep)
        self.assertEqual(rep.errors, [])

    def test_playbook_clean(self):
        rep = co.Report()
        co.check_playbook(rep)
        self.assertEqual(rep.errors, [])

    def test_links_clean(self):
        rep = co.Report()
        co.check_links(rep)
        self.assertEqual(rep.errors, [])

    def test_every_row_says_verify_and_has_no_status(self):
        for key in co.LISTS:
            _, rows = co.read_csv(HERE / f"target-list-{key}.csv")
            for r in rows:
                self.assertEqual(r["verify"], co.VERIFY)
                self.assertEqual(r["status"], "")
                self.assertTrue(r["contact_route"].startswith(co.STD_ROUTE))

    def test_hold_and_skip_never_actionable(self):
        _, rows = co.read_csv(HERE / "target-list-home.csv")
        for r in rows:
            if r["priority"] in ("HOLD", "SKIP"):
                self.assertTrue(r["lead_with"].startswith("Do not contact"))

    def test_dnc_seed_matches_lists(self):
        seeded = {r["list_id"] for r in co.read_csv(HERE / rl.DNC_FILE)[1]}
        expected = set()
        for key in co.LISTS:
            for r in co.read_csv(HERE / f"target-list-{key}.csv")[1]:
                if r["priority"] in ("HOLD", "SKIP"):
                    expected.add(r["id"])
        self.assertEqual(seeded, expected)

    def test_tracking_template_header(self):
        self.assertEqual(co.read_csv(HERE / "tracking-template.csv")[0], co.TRACK_COLS)


class ListMutations(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        for key in co.LISTS:
            shutil.copy(HERE / f"target-list-{key}.csv", self.tmp / f"target-list-{key}.csv")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def edit(self, key, fn):
        path = self.tmp / f"target-list-{key}.csv"
        header, rows = co.read_csv(path)
        fn(rows)
        with path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=header, quoting=csv.QUOTE_ALL)
            w.writeheader()
            w.writerows(rows)

    def run_checks(self):
        rep = co.Report()
        co.check_lists(rep, directory=self.tmp)
        return rep.errors

    def test_untouched_copy_is_clean(self):
        self.assertEqual(self.run_checks(), [])

    def test_email_in_a_field_is_an_error(self):
        self.edit("fashion", lambda rows: rows[0].update(why_it_fits="write to brand@example.test"))
        self.assertTrue(any("e-mail" in e for e in self.run_checks()))

    def test_web_address_is_an_error(self):
        self.edit("fashion", lambda rows: rows[0].update(lead_with="see https://example.test"))
        self.assertTrue(any("web address" in e for e in self.run_checks()))

    def test_phone_is_an_error(self):
        self.edit("home", lambda rows: rows[0].update(compliance_flags="call 02-1234-5678"))
        self.assertTrue(any("phone" in e for e in self.run_checks()))

    def test_price_is_an_error(self):
        self.edit("ai-tools", lambda rows: rows[0].update(why_it_fits="would pay NT$50,000"))
        self.assertTrue(any("price" in e for e in self.run_checks()))

    def test_route_wording_enforced(self):
        self.edit("home", lambda rows: rows[0].update(contact_route="info@somewhere"))
        self.assertTrue(any("contact_route" in e for e in self.run_checks()))

    def test_simplified_in_name_is_an_error(self):
        self.edit("fashion", lambda rows: rows[0].update(name_zh="视频品牌"))
        self.assertTrue(any("Simplified" in e or "SIMPLIFIED" in e for e in self.run_checks()))

    def test_mainland_word_in_name_is_an_error(self):
        self.edit("fashion", lambda rows: rows[0].update(name_zh="信息公司"))
        self.assertTrue(any("MAINLAND" in e for e in self.run_checks()))

    def test_skip_row_must_say_do_not_contact(self):
        def f(rows):
            for r in rows:
                if r["priority"] == "SKIP":
                    r["lead_with"] = "Pitch them"
                    break
        self.edit("home", f)
        self.assertTrue(any("Do not contact" in e or "do not contact" in e for e in self.run_checks()))

    def test_also_in_must_be_symmetric(self):
        self.edit("fashion", lambda rows: rows[0].update(also_in="H"))
        self.assertTrue(any("also_in" in e for e in self.run_checks()))

    def test_sorted_by_priority(self):
        def f(rows):
            rows[0], rows[-1] = rows[-1], rows[0]
        self.edit("fashion", f)
        self.assertTrue(any("sorted" in e or "id should be" in e for e in self.run_checks()))


class Filled(unittest.TestCase):
    def check(self, text):
        tmp = Path(tempfile.mkdtemp())
        try:
            p = tmp / "msg.md"
            p.write_text(text, encoding="utf-8")
            return co.check_filled(p).errors
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_placeholder_left_is_an_error(self):
        self.assertTrue(any("TO FILL" in e for e in self.check("您好 [SENDER NAME: TO FILL] 我們是 AI 虛擬角色工作室")))

    def test_clean_message_passes(self):
        self.assertEqual(self.check("您好，我們是創作 AI 虛擬角色的小型工作室。若不需要，請回覆「不需要」。"), [])

    def test_price_is_an_error(self):
        self.assertTrue(any("price" in e for e in self.check("AI 虛擬角色示範，費用 NT$5,000。不需要請回覆。")))

    def test_experience_claim_is_an_error(self):
        self.assertTrue(self.check("AI 虛擬角色。我試用了一個月，覺得很好。不需要請回覆。"))

    def test_must_say_ai(self):
        self.assertTrue(any("AI" in e for e in self.check("您好，歡迎合作。")))


class Tracking(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def errors(self, rows):
        rep, funnel = co.check_tracking(tracking_file(self.tmp, rows))
        return rep.errors, funnel

    def test_valid_row(self):
        errs, funnel = self.errors([row()])
        self.assertEqual(errs, [])
        self.assertEqual(funnel["approached (first message sent)"], 1)

    def test_bad_enum(self):
        errs, _ = self.errors([row(status="sent_maybe")])
        self.assertTrue(any("status" in e for e in errs))

    def test_bad_date(self):
        errs, _ = self.errors([row(first_sent_date="12/01/2026")])
        self.assertTrue(any("YYYY-MM-DD" in e for e in errs))

    def test_follow_up_due_must_be_day_seven(self):
        errs, _ = self.errors([row(follow_up_due="2026-12-05")])
        self.assertTrue(any("7 days" in e for e in errs))

    def test_two_open_threads_for_one_entity(self):
        errs, _ = self.errors([row(contact_id="C001"), row(contact_id="C002", first_sent_date="2026-12-02", follow_up_due="2026-12-09")])
        self.assertTrue(any("open threads" in e for e in errs))

    def test_skip_row_contacted(self):
        errs, _ = self.errors([row(priority="SKIP")])
        self.assertTrue(any("never be contacted" in e for e in errs))

    def test_dnc_needs_reason_and_closed_status(self):
        errs, _ = self.errors([row(do_not_contact="Y")])
        self.assertTrue(any("do_not_contact = Y" in e for e in errs))

    def test_opt_out_reply_forces_dnc(self):
        errs, _ = self.errors([row(reply_type="opt_out", reply_date="2026-12-02")])
        self.assertTrue(any("opt_out" in e for e in errs))

    def test_contact_after_dnc(self):
        rows = [row(contact_id="C001", do_not_contact="Y", dnc_reason="asked to stop", dnc_date="2026-12-03",
                    status="do_not_contact", reply_type="opt_out", reply_date="2026-12-03"),
                row(contact_id="C002", first_sent_date="2027-03-01", follow_up_due="2027-03-08", status="closed_no_reply")]
        errs, _ = self.errors(rows)
        self.assertTrue(any("after the entity was marked do-not-contact" in e for e in errs))

    def test_recontact_inside_90_days(self):
        rows = [row(contact_id="C001", status="closed_no_reply"),
                row(contact_id="C002", first_sent_date="2027-01-15", follow_up_due="2027-01-22", status="closed_no_reply")]
        errs, _ = self.errors(rows)
        self.assertTrue(any("90 days" in e for e in errs))

    def test_recontact_after_90_days_is_fine(self):
        rows = [row(contact_id="C001", status="closed_no_reply"),
                row(contact_id="C002", first_sent_date="2027-03-15", follow_up_due="2027-03-22", status="sent")]
        errs, _ = self.errors(rows)
        self.assertEqual(errs, [])

    def test_email_in_notes_is_an_error(self):
        errs, _ = self.errors([row(notes="replied from someone@example.test")])
        self.assertTrue(any("e-mail" in e for e in errs))

    def test_funnel_counts(self):
        rows = [row(contact_id="C001", entity_name="A", reply_date="2026-12-03", reply_type="interested", sample_scope="3 boards",
                    sample_delivered_date="2026-12-20"),
                row(contact_id="C002", entity_name="B", route="warm", status="sent"),
                row(contact_id="C003", entity_name="C", written_quote_received="Y", quote_date="2026-12-10")]
        errs, funnel = self.errors(rows)
        self.assertEqual(errs, [])
        self.assertEqual(funnel["replied"], 1)
        self.assertEqual(funnel["interested (interested or more_info)"], 1)
        self.assertEqual(funnel["samples delivered"], 1)
        self.assertEqual(funnel["written quotes or rate sheets received"], 1)
        self.assertEqual(funnel["warm fashion contacts approached"], 1)


class Regexes(unittest.TestCase):
    def test_detectors(self):
        rep = co.Report()
        co.no_contact_details("a@b.test", "x", rep)
        co.no_contact_details("see www.example.tw", "x", rep)
        co.no_contact_details("0912-345-678", "x", rep)
        co.no_contact_details("12345678", "x", rep)
        self.assertEqual(len(rep.errors), 4)

    def test_dates_and_percentages_are_not_phones(self):
        rep = co.Report()
        co.no_contact_details("2026-10-12 and 2027-02-06 and 57.7% and 2026-11-16", "x", rep)
        self.assertEqual(rep.errors, [])


if __name__ == "__main__":
    unittest.main(verbosity=1)
