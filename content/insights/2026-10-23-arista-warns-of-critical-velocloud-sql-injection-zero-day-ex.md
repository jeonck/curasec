---
title: "Arista VeloCloud Orchestrator Zero-Day SQL Injection Under Active Attack"
date: 2026-10-23T15:44:28.729261+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["sd-wan", "sql-injection", "zero-day"]
cves: []
source: "https://thehackernews.com/2026/10/arista-warns-of-critical-velocloud-sql.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Actively exploited zero-day with no patch yet; any authenticated VCO user can escalate to operator. Immediately restrict network access to the VCO management interface to trusted IPs only, audit all existing VCO accounts, and review recent operator-level activity for unauthorized escalations.
- **SOC/IR — Act:** Active exploitation of SD-WAN management plane means assume-breach posture is warranted if you have VeloCloud. Sweep VCO audit logs for privilege escalations from low-privilege accounts since at least October 22 and tune alerts for anomalous operator-level configuration changes.
- **Leader — Act:** Zero-day exploitation of a widely-deployed SD-WAN management system is a material risk event. Confirm whether your organization uses Arista VeloCloud Orchestrator, assess exposure with the network team, and prepare a brief for leadership before this generates inbound questions.
