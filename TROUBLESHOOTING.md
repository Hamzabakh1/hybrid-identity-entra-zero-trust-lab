# Hybrid identity troubleshooting

**DOCUMENTED ONLY.** Preserve correlation ID, tenant ID, UTC timestamp, affected synthetic object and baseline configuration before changes.

1. **Duplicate UPN/proxy address:** compare on-premises attributes and export error; resolve the duplicate at its authoritative source; verify a single cloud object.
2. **Object not synchronized:** inspect OU/filter scope, scheduler/agent health, connector space and export status; correct scope only after blast-radius review; verify object appears.
3. **Authentication fails:** separate sync state from PHS/PTA/federation path; inspect sign-in logs, status code, app, CA and device; test known-good user.
4. **MFA blocked:** inspect method registration and authentication detail; use approved recovery procedure; verify a new sign-in without bypassing controls broadly.
5. **Conditional Access lockout:** check report-only/enforced state, policy scope and emergency account path; disable only the faulty test policy with authorized admin; review sign-ins.
6. **Leaver retains access:** compare AD disable, sync export, cloud account state, refresh tokens and active sessions; revoke sessions and verify access denied.

Never test a lockout by changing tenant-wide policy without authorization.
