---
title: "Fake Notepad++ Plugin Delivers MATCHBOIL.V2 in UAC-0099 Attacks"
date: 2026-07-24T12:43:46.515834+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["malware", "threat-actor", "windows"]
cves: []
source: "https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Social engineering via trojanized software plugins is a recurring delivery vector; audit Notepad++ plugin directories on developer and admin workstations for unexpected DLLs, but no patch exists and no KEV or PoC signals elevate this to urgent action.
- **SOC/IR — Plan:** UAC-0099 is an active Russia-aligned actor with evolving delivery chains; build or tune detections for anomalous files dropped into Notepad++ plugin directories and monitor for MATCHBOIL.V2 indicators once CERT-UA publishes full IOC sets.
- **Leader — Learn:** Russia-aligned UAC-0099 campaign primarily flagged by CERT-UA; relevant context for organizations with Ukraine exposure or in sectors targeted by Russian threat actors, but no board-level event or vendor-breach action required.
