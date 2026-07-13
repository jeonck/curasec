---
title: "Exposed Server Leaks Three Evilginx M365 Phishing Operations"
date: 2026-07-13T13:18:50.242173+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["phishing", "microsoft-365", "aitm"]
cves: []
source: "https://thehackernews.com/2026/07/misconfigured-server-reveals-three.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Evilginx bypasses TOTP-based MFA by proxying credentials; if your M365 tenant uses authenticator-app OTP rather than FIDO2/hardware keys, plan migration to phishing-resistant MFA and enforce Entra ID Conditional Access requiring compliant devices this quarter.
- **SOC/IR — Act:** Three live AiTM operations were exposed with their full toolkits; pull the IOCs Lexfo published, sweep M365/Entra ID sign-in logs for unfamiliar token-issuing IP ranges, and tune detections for impossible-travel or session-token reuse patterns since AiTM bypasses MFA alerts entirely.
- **Leader — Learn:** The exposure of three concurrent industrial-scale M365 phishing operations illustrates why TOTP MFA is insufficient as a control; useful context when building the case for phishing-resistant MFA investment in the next budget cycle.
