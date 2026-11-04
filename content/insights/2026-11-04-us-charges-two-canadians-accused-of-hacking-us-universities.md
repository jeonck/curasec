---
title: "US charges two Canadians for hacking universities to mine crypto"
date: 2026-11-04T18:40:06.241551+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["credential-theft", "cryptomining", "higher-education"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/us-charges-two-canadians-accused-of-hacking-us-universities/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** University environments often share infrastructure patterns with enterprises; this case highlights credential compromise leading to unauthorized compute use, worth reviewing your cloud spend alerts and unauthorized instance detection.
- **SOC/IR — Learn:** Cryptomining post-compromise is a useful behavioral signal; no IOCs published here, but reinforces value of tuning alerts for anomalous compute/CPU spikes and outbound mining pool traffic.
- **Leader — Skip**
