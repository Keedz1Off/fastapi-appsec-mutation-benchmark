"""Offline checks of the evidence shipped with this portfolio entry."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class RecordedEvidenceTests(unittest.TestCase):
    def test_boundary_catalog_matches_static_comparison(self):
        rows = read_json("matrices/boundaries.json")["rows"]
        comparison = read_json("evidence/comparison.json")
        self.assertEqual(len(rows), comparison["seed_root_causes"])
        indexed = {row["seed_id"]: row for row in comparison["rows"]}
        self.assertEqual(len(rows), len(indexed))
        for row in rows:
            with self.subTest(boundary=row["id"]):
                recorded = indexed[row["id"]]
                self.assertEqual(row["invariant"], recorded["invariant"])
                self.assertEqual(row["finding_ids"], recorded["blind_static_matches"])
                self.assertTrue(recorded["static_detected"])
                self.assertEqual(row["runtime_status"], "not_performed")

    def test_seven_recorded_normal_requests_completed(self):
        report = read_json("evidence/runtime-smoke.json")
        self.assertEqual(len(report["checks"]), 7)
        for check in report["checks"]:
            with self.subTest(case=check["name"]):
                self.assertEqual(check["status"], 200)
        self.assertTrue(report["listener_closed"])
