---
title: "Two Unpatched Citrix NetScaler RCE Zero-Days Actively Exploited"
date: 2026-09-27T15:38:27.651895+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["zero-day", "rce", "citrix-netscaler"]
cves: []
source: "https://thehackernews.com/2026/09/warning-two-unpatched-citrix-netscaler.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Actively exploited RCE on NetScaler ADC/Gateway with no patch available; take appliances offline or restrict management-plane access immediately, monitor watchTowr's advisory for IOCs and check Citrix for any interim mitigations.
- **SOC/IR — Act:** Active exploitation of internet-facing edge appliances means possible pre-patch compromise; assume-breach posture — hunt for anomalous activity from NetScaler IPs, review watchTowr's analysis for TTPs, and prepare runbooks for NetScaler IR.
- **Leader — Act:** Unpatched RCE on a widely deployed network edge product with confirmed active exploitation is a board-level event; confirm whether NetScaler ADC or Gateway is in your estate, assess exposure, and brief leadership this week in case it escalates before a patch ships.
