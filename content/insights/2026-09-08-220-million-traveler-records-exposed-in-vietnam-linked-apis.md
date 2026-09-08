---
title: "220 million traveler records exposed via APIS default credentials"
date: 2026-09-08T15:04:44.915544+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Learn"
tags: ["data-breach", "pii-exposure", "default-credentials"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/220-million-traveler-records-exposed-in-vietnam-linked-apis-leak/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** The root cause — default credentials left on a cloud-exposed system — is a textbook misconfiguration. No specific software or CVE is named, so there is no patch to apply; use this as a prompt to audit your own cloud services for default or uncycled credentials.
- **SOC/IR — Skip**
- **Leader — Learn:** A breach of this scale — spanning nearly a decade of passport and travel data — illustrates third-party government data custody risk. No direct vendor relationship action is needed for most organizations, but it is useful context for board-level discussions on supply-chain and sovereign data exposure.
