---
title: "Progress Kemp LoadMaster Command Injection (CVE-2026-8037) Added to CISA KEV"
date: 2026-08-09T11:41:42.823801+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["cve", "load-balancer", "active-exploitation"]
cves: ["CVE-2026-8037"]
source: "https://thehackernews.com/2026/08/progress-kemp-loadmaster-flaw-hits-cisa.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** CISA KEV-listed, EPSS 0.99, public PoC, and 792 confirmed exploit attempts make this an emergency patch. Apply the Progress Kemp LoadMaster patch immediately or isolate the appliance from untrusted networks until patched.
- **SOC/IR — Act:** Active exploitation of a perimeter load balancer warrants an assume-breach sweep — hunt for command injection patterns in LoadMaster access logs since the first reported attempts, and check downstream hosts for lateral movement indicators.
- **Leader — Act:** CISA KEV listing plus confirmed active exploitation makes this a board-question-level appliance vulnerability; confirm this week whether LoadMaster is in your environment and verify engineering has patched or isolated affected instances.
- **Signals:** CVE-2026-8037 — CISA KEV: listed, EPSS 0.99, public PoC on GitHub
