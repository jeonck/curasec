---
title: "Passkey-themed social engineering enables M365 identity and cloud compromise"
date: 2026-09-10T14:58:06.811051+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["social-engineering", "identity-and-access", "cloud-security"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/09/09/passkey-themed-social-engineering-leads-identity-cloud-compromise/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Plan:** No exploitation-pressure signals, but the MFA persistence and Microsoft Graph abuse techniques described warrant auditing Entra ID registered authentication methods for unexpected passkey enrollments and reviewing conditional access policies governing Graph API access this quarter.
- **SOC/IR — Act:** The article documents TTPs mappable to ATT&CK — MFA persistence registration and Microsoft Graph reconnaissance — against a near-universal enterprise target (M365); implement or tune detections for anomalous Graph API enumeration calls and unexpected MFA method additions, and hunt for such activity since early September 2026.
- **Leader — Plan:** Passkey rollout communications are now a social engineering attack surface; if your organization is mid-deployment, review user-facing passkey enrollment messaging for impersonation risk and include this TTP in the next security-awareness training update.
