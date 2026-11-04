---
title: "NIKKE game launcher supply-chain attack drops credential-stealing malware"
date: 2026-11-04T18:40:06.241551+00:00
verdict: "Learn"
verdict_engineer: "Skip"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["supply-chain", "malware", "credential-theft"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/nikke-pc-game-launcher-hacked-to-spread-remote-access-data-stealing-malware/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Skip**
- **SOC/IR — Learn:** Confirmed supply-chain compromise via tampered launcher scripts distributing credential and crypto wallet stealers; if employees run gaming clients on corporate endpoints, check EDR telemetry for NIKKE launcher process activity, but no specific IOCs are published yet.
- **Leader — Skip**
