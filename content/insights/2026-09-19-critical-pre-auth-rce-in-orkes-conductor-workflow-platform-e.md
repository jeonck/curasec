---
title: "Critical Pre-Auth RCE in Orkes Conductor Exploited in the Wild"
date: 2026-09-19T14:22:25.332089+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["rce", "active-exploitation", "workflow-orchestration"]
cves: ["CVE-2026-58138"]
source: "https://thehackernews.com/2026/09/critical-pre-auth-rce-in-orkes.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Actively exploited pre-auth RCE with a public PoC on GitHub overrides the low EPSS; patch Orkes Conductor to 3.30.2 or later immediately if running any version before that.
- **SOC/IR — Act:** Active exploitation confirmed by Fortinet means assume-breach posture for any environment running Orkes Conductor — sweep for anomalous process spawns from the Conductor service and pull Fortinet's report for available IOCs to hunt against SIEM data.
- **Leader — Plan:** Verify whether Orkes Conductor is in your tech stack; if confirmed, escalate to engineering as urgent given active exploitation of a 9.8 CVSS pre-auth RCE — this is not yet a board-level systemic event unless your org is exposed.
- **Signals:** CVE-2026-58138 — CISA KEV: not listed, EPSS 0.09, public PoC on GitHub
