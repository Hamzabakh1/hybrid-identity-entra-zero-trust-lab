"""Offline safety check for a synthetic report-only Conditional Access template."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def validate(policy: dict) -> list[str]:
    findings = []
    if policy.get("state") != "enabledForReportingButNotEnforced":
        findings.append("POLICY_NOT_REPORT_ONLY")
    users = policy.get("conditions", {}).get("users", {})
    included = users.get("includeGroups", [])
    excluded = users.get("excludeGroups", [])
    if not included or users.get("includeUsers") or users.get("includeRoles"):
        findings.append("POLICY_SCOPE_NOT_PILOT_GROUP_ONLY")
    if "PILOT_GROUP_ID" not in included:
        findings.append("PILOT_GROUP_MISSING")
    if "EMERGENCY_ACCESS_GROUP_ID" not in excluded:
        findings.append("EMERGENCY_ACCESS_EXCLUSION_MISSING")
    if "mfa" not in policy.get("grantControls", {}).get("builtInControls", []):
        findings.append("MFA_GRANT_MISSING")
    return findings


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, required=True)
    args = parser.parse_args()
    policy = json.loads(args.policy.read_text(encoding="utf-8"))
    findings = validate(policy)
    print(json.dumps({"findings": findings, "status": "PASS" if not findings else "REVIEW_REQUIRED",
                      "evidence_type": "OFFLINE_TEMPLATE_CHECK_NO_TENANT_CHANGE"}, indent=2))
    if findings:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
