---
title: "ChainScript RAT Uses Polygon Blockchain for C2 Rotation via ClickFix Lures"
date: 2026-09-21T17:01:38.950105+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["rat", "clickfix", "blockchain-c2"]
cves: []
source: "https://thehackernews.com/2026/09/clickfix-lures-deploy-chainscript-rat.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Using a public blockchain (Polygon) for C2 infrastructure rotation is a novel evasion technique worth understanding for future detection architecture; no running system needs patching, but this reinforces restricting outbound RPC calls from endpoints to blockchain nodes.
- **SOC/IR — Plan:** Build or tune detections for ClickFix-style user-execution lures impersonating Teams/Zoom/Spotify, and add hunting logic for endpoints making Polygon RPC calls; no specific IOCs are published yet, so schedule this as a detection engineering task rather than an immediate sweep.
- **Leader — Skip**
