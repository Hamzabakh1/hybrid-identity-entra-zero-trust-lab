import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate_ca_policy", ROOT / "scripts/validation/validate_ca_policy.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
BASE = json.loads((ROOT / "examples/synthetic-data/ca-report-only-template.json").read_text(encoding="utf-8"))


class PolicyTests(unittest.TestCase):
    def test_safe_report_only_pilot_template(self):
        self.assertEqual(checker.validate(BASE), [])

    def test_reject_enforced_policy(self):
        policy = copy.deepcopy(BASE)
        policy["state"] = "enabled"
        self.assertIn("POLICY_NOT_REPORT_ONLY", checker.validate(policy))

    def test_reject_all_users_and_missing_emergency_exclusion(self):
        policy = copy.deepcopy(BASE)
        policy["conditions"]["users"] = {"includeUsers": ["All"], "excludeGroups": []}
        findings = checker.validate(policy)
        self.assertIn("POLICY_SCOPE_NOT_PILOT_GROUP_ONLY", findings)
        self.assertIn("EMERGENCY_ACCESS_EXCLUSION_MISSING", findings)


if __name__ == "__main__":
    unittest.main()
