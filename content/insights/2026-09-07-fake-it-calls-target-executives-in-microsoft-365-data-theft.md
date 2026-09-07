---
title: "Vishing + AitM Campaign Targets Executives for M365 Data Theft"
date: 2026-09-07T16:27:04.378719+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["vishing", "aitm", "microsoft-365"]
cves: []
source: "https://thehackernews.com/2026/09/microsoft-365-attackers-use-help-desk.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Enforce phishing-resistant MFA (FIDO2) for all executive accounts and audit conditional access policies to block residential-proxy sign-ins; no active PoC or KEV signal, but AitM token theft bypasses standard MFA.
- **SOC/IR — Act:** Hunt for anomalous M365 sign-ins from residential proxy ranges targeting director/VP accounts, especially preceded by IT help-desk call activity; tune detections for impossible-travel or token-replay events in your SIEM.
- **Leader — Act:** Brief executive staff on IT impersonation vishing tactics this week and confirm your help-desk verification procedures prevent social-engineering escalation; this campaign explicitly targets directors and VPs and is likely to surface as a board question.
