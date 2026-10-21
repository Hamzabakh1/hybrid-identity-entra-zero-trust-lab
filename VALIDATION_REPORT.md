# Validation report — 2026-10-21

Local execution: Windows x64, bundled Python 3.12.14, PowerShell 7.6.5. No AD forest, Entra tenant or Graph session was connected.

| Test | Expected | Actual | Environment | Timestamp UTC | Evidence | Status |
|---|---|---|---|---|---|---|
| Synthetic JML/policy unit suite and 200-identity dataset | 9 pass | 9 pass, exit 0 | Local Python | 2026-10-21 06:01 | [unittest.txt](tests/evidence/unittest.txt) | PASS |
| Report-only CA template check | No unsafe finding; no tenant write | PASS, offline template only | Local Python | 2026-10-21 06:01 | [ca-policy.json](tests/evidence/ca-policy.json) | PASS |
| PowerShell parser | 0 errors | 0 errors in 1 file | Local PowerShell | 2026-10-21 05:28 | [parser.txt](tests/evidence/parser.txt) | PASS |
| Example move | Explicit simulated marker | Finance → Operations plan, no directory change | Local Python | 2026-10-21 05:28 | [move.json](tests/evidence/move.json) | PASS |
| Sync/MFA/CA/Graph integration | Tenant-backed result | Not executed | Tenant/roles/licenses unavailable | N/A | [audit](ENVIRONMENT_AUDIT.md) | BLOCKED |
| Deprovisioning/incident drills | Real denied sign-in and logs | Not executed | Tenant unavailable | N/A | [runbooks](TROUBLESHOOTING.md) | BLOCKED |

The planner proposes actions; it cannot create, sync or disable identities. Tenant quality gates and target score remain open.
