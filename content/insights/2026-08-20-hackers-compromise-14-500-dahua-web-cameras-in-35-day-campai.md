---
title: "14,500 Dahua IP cameras compromised in 35-day CameraSwarm campaign"
date: 2026-08-20T11:39:11.237527+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["iot-security", "credential-attack", "camera"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-compromise-14-500-dahua-web-cameras-in-35-day-campaign/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If Dahua cameras are in scope, audit all units for default or weak credentials and remove any direct internet exposure; the campaign scale suggests opportunistic credential stuffing across this device class, but no KEV or PoC shifts this below Act.
- **SOC/IR — Learn:** No IOCs or ATT&CK-mappable TTPs are surfaced in this item, and the compromise is geographically concentrated in Ukraine and Russia — limited detection work is actionable for a typical enterprise SOC without more detail.
- **Leader — Skip**
