import importlib.util
import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("lifecycle", ROOT / "scripts/automation/lifecycle.py")
lifecycle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lifecycle)


class LifecycleTests(unittest.TestCase):
    def test_join(self):
        result = lifecycle.plan_transition({"id":"lab.amal.atlas","state":"planned","department":"IT"}, "join")
        self.assertEqual(result["next_state"], "active")
        self.assertEqual(result["evidence_type"], "SIMULATED_PLAN_NO_DIRECTORY_CHANGE")

    def test_move(self):
        result = lifecycle.plan_transition({"id":"lab.salma.atlas","state":"active","department":"Finance"}, "move", "Operations")
        self.assertEqual(result["next_department"], "Operations")
        self.assertIn("remove old group", result["proposed_steps"])

    def test_leave(self):
        result = lifecycle.plan_transition({"id":"lab.nora.atlas","state":"active","department":"Engineering"}, "leave")
        self.assertEqual(result["next_state"], "disabled")
        self.assertIn("revoke sessions", result["proposed_steps"])

    def test_reject_real_identity(self):
        with self.assertRaises(ValueError):
            lifecycle.plan_transition({"id":"alice","state":"active","department":"IT"}, "leave")

    def test_reject_invalid_move(self):
        with self.assertRaises(ValueError):
            lifecycle.plan_transition({"id":"lab.amal.atlas","state":"planned","department":"IT"}, "move", "Finance")

    def test_200_identity_pilot_dataset_is_synthetic(self):
        with (ROOT / "examples/synthetic-data/identities-200.csv").open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(len(rows), 200)
        self.assertEqual(len({row["id"] for row in rows}), 200)
        self.assertTrue(all(row["id"].startswith("lab.") and row["state"] == "planned" for row in rows))


if __name__ == "__main__":
    unittest.main()
