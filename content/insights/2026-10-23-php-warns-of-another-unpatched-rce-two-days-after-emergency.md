---
title: "PHP Discloses New RCE CVE-2026-115560 with Public PoC, No Emergency Patch"
date: 2026-10-23T15:44:28.729261+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["php", "rce", "cve"]
cves: ["CVE-2026-115560"]
source: "https://thehackernews.com/2026/10/urgent-php-warns-of-another-unpatched.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC on GitHub raises exploitation probability despite PHP's 'unlikely' framing; audit your PHP application configurations for the affected feature and disable it per PHP's mitigation guidance before a patch ships.
- **SOC/IR — Plan:** The public PoC makes opportunistic exploitation attempts plausible; build or tune detections for anomalous process spawning from web server processes and new webshell activity on PHP-serving hosts this sprint.
- **Leader — Skip**
- **Signals:** CVE-2026-115560 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
