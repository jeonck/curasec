---
title: "SonicWall will not patch two flaws in EOL GMS software"
date: 2026-11-04T18:40:06.241551+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Plan"
tags: ["sonicwall", "eol-software", "vulnerability"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/sonicwall-warns-of-unpatched-flaws-in-end-of-life-gms-software/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Two unpatched flaws with no fix path means the only remediation is migrating off SonicWall GMS or implementing strict network isolation as a compensating control; audit whether GMS is still deployed and prioritize decommission this quarter.
- **SOC/IR — Skip**
- **Leader — Plan:** Confirm whether GMS is in the environment; if so, add it to the risk register as a component with no vendor remediation path and budget a migration — EOL software with disclosed, unpatched flaws is a liability in audit and questionnaire contexts.
