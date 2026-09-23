---
title: "WordPress 7.1.2 Patches Critical Unauthenticated RCE in Core"
date: 2026-09-23T15:27:03.663698+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["wordpress", "rce", "patch"]
cves: []
source: "https://thehackernews.com/2026/09/wordpress-issues-patch-for-critical.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Unauthenticated PHP file inclusion enabling potential code execution is severe and affects all WordPress branches back to 4.7; no KEV listing or public PoC in signals, but the attack surface is enormous — patch to WordPress 7.1.2 across all managed sites within your normal critical-patch window.
- **SOC/IR — Skip**
- **Leader — Skip**
