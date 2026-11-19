---
title: "phpAfterShell CVE-2026-126714: PHP Session Flaw Enables Code Execution"
date: 2026-11-19T19:29:03.442667+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["php", "rce", "cve"]
cves: ["CVE-2026-126714"]
source: "https://thehackernews.com/2026/11/phpaftershell-explained-how-hackers.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Patch all PHP installations to today's releases; audit apps with complex object hierarchies (e.g., Laravel, Symfony, Yii) for gadget chains that could be triggered via session deserialization. Public PoC on GitHub raises exploitation pressure even without KEV listing.
- **SOC/IR — Plan:** Build detections for anomalous PHP session file writes or truncation events on web servers, and hunt for suspicious process spawns from PHP-FPM or mod_php since the PoC dropped. No confirmed active exploitation yet, but the public PoC shortens the window.
- **Leader — Skip**
- **Signals:** CVE-2026-126714 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
