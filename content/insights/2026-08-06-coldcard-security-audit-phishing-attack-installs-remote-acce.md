---
title: "COLDCARD phishing lure deploys ScreenConnect RAT on victims"
date: 2026-08-06T13:03:19.955458+00:00
verdict: "Act"
verdict_engineer: "Skip"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["phishing", "remote-access-trojan", "social-engineering"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/coldcard-security-audit-phishing-attack-installs-remote-access-tool/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Skip**
- **SOC/IR — Act:** A phishing campaign is actively distributing ScreenConnect as a RAT using COLDCARD vulnerability lures; hunt for unexpected ScreenConnect installations on endpoints and tune EDR detections for ScreenConnect deployed outside approved baselines.
- **Leader — Learn:** This campaign illustrates how high-profile crypto incidents are rapidly weaponized as phishing lures; useful context for security awareness briefings but no immediate organizational action required.
