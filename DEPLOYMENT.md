# Tenant-safe deployment path

**DOCUMENTED ONLY; not executed.**

1. Record tenant ID, owner, license, emergency access accounts and rollback authority. Validate those accounts before policy work.
2. Fix UPN/domain mapping and duplicate attributes in synthetic AD objects. Select a dedicated OU scope and export baseline counts.
3. Choose Connect Sync or Cloud Sync after comparing required features and support; install current supported build on SYNC01. Use staging mode or pilot scope as supported.
4. Sync a few synthetic users, compare immutable/source anchor and UPN, check export errors and tenant object state. Do not sync all 200 until pilot is verified.
5. Validate the selected authentication method separately. Register test MFA methods. Create narrowly scoped Conditional Access in report-only mode; analyze sign-in results and preserve emergency accounts when enforcing restrictions.
6. Test join, move and leave with approvals, access review, token/session revocation and cloud/on-premises evidence. Retain audit logs and screenshots.

Any actual tenant-wide policy or identity mutation requires the tenant owner's explicit authorization.
