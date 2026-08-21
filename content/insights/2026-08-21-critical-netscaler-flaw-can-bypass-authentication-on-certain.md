---
title: "Citrix NetScaler Critical Auth Bypass in Gateway and AAA Configs"
date: 2026-08-21T11:38:25.806134+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["citrix", "authentication-bypass", "netscaler"]
cves: []
source: "https://thehackernews.com/2026/08/critical-netscaler-flaw-can-bypass.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** A critical auth bypass in NetScaler ADC/Gateway is high-severity exposure for any org using these as VPN or AAA endpoints; no KEV listing or public PoC in signals, so patch to the latest Citrix-released version this cycle rather than emergency response.
- **SOC/IR — Learn:** No active exploitation or IOCs reported yet; monitor for KEV addition or PoC release, at which point an assume-breach sweep of edge authentication logs would be warranted.
- **Leader — Skip**
