---
title: "ToxicPanda 2.0 Android Malware Expands Targeting with 167 Remote Commands"
date: 2026-08-20T11:39:11.237527+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["android-malware", "mobile-banking", "fraud"]
cves: []
source: "https://thehackernews.com/2026/08/toxicpanda-20-and-golddigger-expand.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No infrastructure or cloud exposure here; this is a mobile banking trojan. Worth understanding the PIN-harvesting technique if your org develops mobile banking apps, but no patch or configuration action required.
- **SOC/IR — Plan:** No IOCs published in this item, but the expanded 140+ targeted app list and new remote-command capability warrant building or tuning mobile threat detections; review Zimperium's full report for indicators to add to mobile MDM alerting.
- **Leader — Learn:** Relevant if your org operates a banking or crypto app; file as emerging mobile fraud risk for the next risk-register review, but no immediate board-level action indicated without corroborating incident data.
