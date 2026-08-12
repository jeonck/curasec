---
title: "DeadLock ransomware uses blockchain to resist infrastructure takedown"
date: 2026-08-12T11:57:00.937865+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["ransomware", "blockchain", "infrastructure"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/deadlock-ransomware-uses-blockchain-to-resist-infrastructure-takedown/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** No patch or configuration action available; the technique signals that traditional domain-takedown mitigations matter less for this operator, which is worth factoring into egress-filtering and backup-isolation architecture reviews.
- **SOC/IR — Learn:** No IOCs or ATT&CK-mapped TTPs are available to hunt or detect; worth absorbing for IR playbook updates, as blockchain-backed C2 limits the value of expecting law-enforcement takedown to cut off active intrusions.
- **Leader — Learn:** Useful framing for board-level ransomware risk discussions: blockchain-anchored infrastructure reduces the effectiveness of law-enforcement disruption as a risk mitigant, which may affect how resilient response plans need to be.
