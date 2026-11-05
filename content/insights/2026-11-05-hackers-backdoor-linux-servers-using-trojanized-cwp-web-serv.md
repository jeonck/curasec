---
title: "CWPdoor backdoor distributed via trojanized CWP web server binary"
date: 2026-11-05T18:42:10.964026+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["linux-malware", "supply-chain", "web-server"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-backdoor-linux-servers-using-trojanized-cwp-web-server/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If you run Control Web Panel on Linux hosts, verify the integrity of the cwpsrv binary against a known-good hash and audit for signs of compromise; no KEV or public PoC listed, but active trojanizing of a management-layer binary warrants prompt inspection this sprint.
- **SOC/IR — Plan:** Build or tune detections for anomalous behavior from the cwpsrv process (unexpected outbound connections, new listener ports, dropped files); pull IOCs from the full BleepingComputer article and add them to your threat-intel feed for retrospective hunting in environments running CWP.
- **Leader — Learn:** A supply-chain-style trojan targeting Linux server management panels is a useful data point for vendor/software risk discussions, but no enrichment signals indicate systemic or sector-wide impact requiring leadership action today.
