---
title: "AOMEI update servers hijacked to distribute malware via backup software"
date: 2026-10-20T15:39:31.280324+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["supply-chain", "malware", "software-update"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-hijack-aomei-update-servers-to-secretly-spread-malware/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If AOMEI backup products are in your environment, audit endpoints that ran the software during the compromise window for malware indicators and verify current update server integrity; no KEV or PoC signals yet to escalate to Act.
- **SOC/IR — Act:** Sweep endpoints running AOMEI backup software for unexpected processes or outbound connections spawned during the compromise window; hunt for lateral movement from hosts where the promotional feature may have delivered a payload.
- **Leader — Learn:** A reminder that backup and recovery tooling is an attractive supply-chain vector; no broad systemic impact confirmed yet, but file for vendor risk review discussions around update-mechanism security in critical software.
