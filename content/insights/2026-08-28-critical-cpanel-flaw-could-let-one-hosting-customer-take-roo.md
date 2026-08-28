---
title: "Critical cPanel/WHM Flaw Enables Root Code Execution, PoC Public"
date: 2026-08-28T21:21:40.237236+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["cve", "rce", "cpanel"]
cves: ["CVE-2026-65643"]
source: "https://thehackernews.com/2026/08/critical-cpanel-flaw-could-let-one.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC exists for a root-level RCE in cPanel and WHM affecting all supported versions — update cPanel/WHM to the patched release immediately and verify no unauthorized access occurred on any exposed panels.
- **SOC/IR — Plan:** With a public PoC now available, write or enable detections for anomalous root-process spawning from cPanel/WHM processes and unusual web requests to the cPanel/WHM management interfaces before exploitation campaigns begin.
- **Leader — Skip**
- **Signals:** CVE-2026-65643 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
