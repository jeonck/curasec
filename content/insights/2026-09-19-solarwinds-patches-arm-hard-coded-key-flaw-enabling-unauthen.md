---
title: "SolarWinds ARM Hard-Coded Key Flaw Allows Unauthenticated RCE"
date: 2026-09-19T14:22:25.332089+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["solarwinds", "rce", "patch"]
cves: ["CVE-2026-28326"]
source: "https://thehackernews.com/2026/09/solarwinds-patches-arm-hard-coded-key.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** CVSS 8.8 unauthenticated RCE via hard-coded key is a serious class of flaw, but EPSS is 0.01 with no KEV listing and no public PoC — patch ARM beyond version 2026.2 on your next patch cycle rather than treating it as emergency.
- **SOC/IR — Skip**
- **Leader — Skip**
- **Signals:** CVE-2026-28326 — CISA KEV: not listed, EPSS 0.01, no public PoC found
