---
title: "Dysphoria IoT Botnet Adopts Blockchain C2 After JackSkid Takedown"
date: 2026-07-28T13:01:43.287328+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["iot-botnet", "c2-infrastructure", "ddos"]
cves: []
source: "https://thehackernews.com/2026/07/dysphoria-iot-botnet-adds-blockchain-c2.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Learn:** Blockchain-based C2 and peer-relay architecture represent an evasion technique relevant to defenders running IoT-adjacent infrastructure, but there are no specific CVEs, affected products, or actionable mitigations named here.
- **SOC/IR — Plan:** The shift to blockchain name services and victim-device relays changes the detection model for this botnet family; build or tune detections for anomalous outbound connections to blockchain resolvers and unexpected device-to-device relay traffic in your estate.
- **Leader — Learn:** Useful context on botnet resilience trends following law-enforcement disruptions, but no immediate vendor exposure or board-level risk event is indicated here.
