---
title: "Adobe Patches 8 Critical Campaign Classic RCE and Privilege Escalation Flaws"
date: 2026-10-28T17:09:30.637292+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["adobe-campaign-classic", "rce", "code-injection"]
cves: ["CVE-2026-104351"]
source: "https://thehackernews.com/2026/10/adobe-fixes-8-critical-campaign-classic.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC on GitHub for a CVSS 9.9 code injection flaw (CVE-2026-104351) makes exploitation pressure real despite the low EPSS; patch Adobe Campaign Classic to the latest released version immediately.
- **SOC/IR — Plan:** With a public PoC available, build or tune detections for exploitation attempts against Campaign Classic endpoints — look for anomalous process spawning or outbound connections from the Campaign Classic application process.
- **Leader — Skip**
- **Signals:** CVE-2026-104351 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub
