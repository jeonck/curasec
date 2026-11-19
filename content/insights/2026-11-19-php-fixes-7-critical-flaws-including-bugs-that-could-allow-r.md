---
title: "PHP patches 7 critical RCE flaws, public PoC available"
date: 2026-11-19T19:29:03.442667+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["php", "rce", "critical-patch"]
cves: ["CVE-2026-115560"]
source: "https://thehackernews.com/2026/11/php-fixes-7-critical-flaws-including.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** PHP RCE flaws affecting all supported versions with a public PoC on GitHub significantly raises exploitation risk even without KEV listing. Upgrade PHP to the patched release immediately and audit any internet-facing PHP applications for indicators of exploitation.
- **SOC/IR — Plan:** With a public PoC now available, opportunistic exploitation of PHP endpoints is likely near-term. Build or tune detections for anomalous process spawning from web server processes (e.g., apache/nginx spawning shells) and monitor WAF logs for CVE-2026-115560 probing signatures.
- **Leader — Plan:** Seven critical PHP RCEs with a public PoC represent a credible escalation risk for any org running PHP web applications. Confirm engineering teams are on an accelerated patch timeline and revisit exposure if CISA adds this to KEV.
- **Signals:** CVE-2026-115560 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
