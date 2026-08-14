---
title: "Akira ransomware evades EDR by rebooting victim into Safe Mode"
date: 2026-08-14T11:54:18.881431+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["ransomware", "edr-evasion", "akira"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Verify your EDR agent is configured to load and protect in Safe Mode, and audit whether bcdedit or safeboot registry keys can be modified by non-admin processes — most EDR platforms have a specific setting for this that is not always on by default.
- **SOC/IR — Act:** Hunt for bcdedit commands setting safeboot (T1562.001) and unexpected Safe Mode reboots in Windows event logs since Akira affiliates actively use this to blind EDR before data theft; tune alerts on bcdedit execution from unexpected parent processes.
- **Leader — Learn:** Akira affiliates are successfully exfiltrating data even when encryption fails, confirming that ransomware incidents now carry extortion risk independent of operational disruption — worth a note in the next risk-register review.
