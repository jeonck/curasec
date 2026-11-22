---
title: "AI Agents Exploited Zero-Day in MONAI Label Medical Imaging Server for Root"
date: 2026-11-22T16:05:35.915127+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["zero-day", "medical-imaging", "ai-attack"]
cves: []
source: "https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Actively exploited unauthenticated file-write-to-root in MONAI Label 0.8.5 and earlier default installs; audit all deployments and either upgrade or block external access to the MONAI Label API immediately.
- **SOC/IR — Learn:** The use of autonomous AI agents to discover a previously unknown vulnerability and achieve root access represents a meaningful escalation in attacker capability worth tracking, but the summary provides no actionable IOCs or ATT&CK-mappable TTPs to enable immediate detection work.
- **Leader — Plan:** China-linked actors operationalizing AI agents for zero-day discovery in medical/research software is a threat-capability shift worth raising with the board this quarter; healthcare or research organizations should audit whether MONAI Label is deployed and assess exposure before next review cycle.
