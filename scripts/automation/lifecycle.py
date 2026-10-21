"""Offline synthetic joiner/mover/leaver planner. No tenant or AD writes."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

DEPARTMENTS = {"IT", "Human Resources", "Finance", "Operations", "Engineering", "Management"}
STATES = {"planned", "active", "disabled"}


def plan_transition(record: dict, action: str, department: str | None = None) -> dict:
    if record.get("id", "").startswith("lab.") is False:
        raise ValueError("Only lab.* synthetic identities are permitted")
    if record.get("state") not in STATES:
        raise ValueError("Invalid current state")
    if record.get("department") not in DEPARTMENTS:
        raise ValueError("Invalid department")
    if action == "join":
        if record["state"] != "planned":
            raise ValueError("Join requires planned state")
        new_state, new_department = "active", record["department"]
        steps = ["create AD account", "assign approved group", "sync identity", "verify sign-in"]
    elif action == "move":
        if record["state"] != "active" or department not in DEPARTMENTS or department == record["department"]:
            raise ValueError("Move requires active state and a different valid department")
        new_state, new_department = "active", department
        steps = ["approve role change", "remove old group", "assign new group", "sync identity", "review access"]
    elif action == "leave":
        if record["state"] != "active":
            raise ValueError("Leave requires active state")
        new_state, new_department = "disabled", record["department"]
        steps = ["disable AD account", "revoke sessions", "remove groups", "sync disable", "preserve records per policy"]
    else:
        raise ValueError("Action must be join, move or leave")
    return {"id": record["id"], "previous_state": record["state"], "next_state": new_state,
            "previous_department": record["department"], "next_department": new_department,
            "proposed_steps": steps, "evidence_type": "SIMULATED_PLAN_NO_DIRECTORY_CHANGE"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--id", required=True)
    parser.add_argument("--action", choices=["join", "move", "leave"], required=True)
    parser.add_argument("--department")
    args = parser.parse_args()
    with args.input.open(newline="", encoding="utf-8") as stream:
        matches = [row for row in csv.DictReader(stream) if row["id"] == args.id]
    if len(matches) != 1:
        raise ValueError("Expected exactly one synthetic identity")
    print(json.dumps(plan_transition(matches[0], args.action, args.department), indent=2))


if __name__ == "__main__":
    main()
