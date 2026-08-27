---
title: "Iranian APT Nimbus Manticore Uses NightLedger Backdoor as Covert Relay"
date: 2026-07-28T13:01:43.287328+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["apt", "backdoor", "iranian-threat-actor"]
cves: []
source: "https://thehackernews.com/2026/07/nimbus-manticore-deploys-nightledger.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Learn:** NightLedger is a novel Windows backdoor with WebSocket tunneling capability; no KEV listing or PoC signals exploitation of specific software you'd patch, but understanding the relay technique informs network egress controls and endpoint detection posture.
- **SOC/IR — Plan:** Build detections for anomalous WebSocket tunneling behavior from Windows hosts and hunt for NightLedger IOCs once Recorded Future or similar publishes indicators; ATT&CK mapping to C2-over-WebSocket and proxy relay techniques warrants a new detection rule this quarter.
- **Leader — Learn:** Nimbus Manticore campaign context is useful for sector risk briefings if your organization has exposure in Middle East, Africa, or South Asia operations, but no immediate board-level action required without confirmed targeting of your industry.
