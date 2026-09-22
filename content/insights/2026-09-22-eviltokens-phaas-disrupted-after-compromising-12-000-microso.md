---
title: "EvilTokens PhaaS disrupted after 12,000 Microsoft account compromises"
date: 2026-09-22T15:30:54.753130+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["phishing-as-a-service", "microsoft-365", "token-theft"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/eviltokens-phaas-disrupted-after-compromising-12-000-microsoft-accounts/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** PhaaS platforms like EvilTokens typically use AiTM techniques that bypass standard MFA; audit Microsoft 365 Conditional Access policies and prioritize rollout of phishing-resistant MFA (FIDO2/passkeys) to eliminate token-theft risk across your tenant.
- **SOC/IR — Act:** Platform disruption does not remediate already-compromised sessions; hunt for anomalous OAuth token grants, impossible-travel sign-ins, and legacy authentication usage in your Microsoft 365 environment covering the campaign's active window.
- **Leader — Act:** With 10,000+ organizations affected, confirm this week whether your organization received a Microsoft DCU breach notification and verify your Microsoft 365 tenants were not among the 12,000 compromised accounts; brief leadership before they encounter the story externally.
