---
title: "Active AitM Phishing Campaign Hijacks M365 Accounts Targeting Finance"
date: 2026-08-07T11:54:55.232717+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["phishing", "microsoft-365", "aitm"]
cves: []
source: "https://thehackernews.com/2026/08/microsoft-365-aitm-phishing-hijacks.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Plan:** Active campaign bypasses MFA via session-token theft on M365 — no KEV or PoC signals, but the exposure is real. Prioritize enforcing phishing-resistant MFA (FIDO2/passkeys) for finance and payroll accounts in Entra ID conditional access policies this quarter.
- **SOC/IR — Act:** Widespread active campaign with clear TTPs: AitM proxy intercept, residential proxy blend-in, and finance-account targeting. Hunt M365 sign-in logs for logins from residential proxy ASNs, and sweep finance/payroll mailboxes for new unauthorized forwarding rules or OAuth app grants added since the campaign was reported.
- **Leader — Plan:** An active, widespread BEC-style campaign harvesting payroll and finance email warrants directing the security team to assess phishing-resistant MFA coverage for high-risk financial roles and briefing finance leadership on social-engineering risk this quarter.
