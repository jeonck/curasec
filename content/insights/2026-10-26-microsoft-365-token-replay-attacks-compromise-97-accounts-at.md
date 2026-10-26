---
title: "Microsoft 365 Token-Replay AitM Campaign Hits 79 Organizations"
date: 2026-10-26T17:20:31.892638+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["m365", "token-replay", "aitm-attack"]
cves: []
source: "https://thehackernews.com/2026/10/microsoft-365-token-replay-attacks.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Active AitM campaign bypasses MFA via stolen session tokens — no patch exists, but hardening is actionable: enable Entra ID Token Protection in Conditional Access policies and audit sign-in logs for anomalous token-replay patterns since July 14, 2026.
- **SOC/IR — Act:** Huntress documented 497 confirmed M365 sign-in events across 79 orgs from July 14–September 22, 2026; sweep Entra ID and M365 unified audit logs for token reuse from mismatched IP geographies or device states consistent with AitM relay behavior.
- **Leader — Act:** M365 email accounts at 79 organizations were compromised via session-token hijacking — brief leadership now given M365's ubiquity in your estate, confirm Entra ID token protection and phish-resistant MFA are enforced, and assess whether any internal accounts show anomalous sign-in activity.
