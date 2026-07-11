---
title: "Progress urges ShareFile Storage Zone Controller shutdown over active threat"
date: 2026-07-11T11:49:48.413664+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["sharefile", "progress-software", "file-sharing"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/progress-urges-sharefile-customers-to-shut-down-servers-over-credible-threat/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** If you run ShareFile Storage Zone Controllers on-premises, shut them down immediately per Progress's emergency guidance — this is the same vendor that disclosed the MoveIt zero-day. Monitor Progress's advisory channel for patch availability before bringing servers back online.
- **SOC/IR — Act:** Progress issuing an emergency shutdown recommendation implies an unpatched, actively targeted vulnerability; treat any org running on-prem ShareFile Storage Zone Controllers as potentially exposed. Initiate a sweep for anomalous file-transfer or lateral-movement activity from those hosts since at least 72 hours prior to today.
- **Leader — Act:** Progress Software — the MoveIt vendor — is issuing emergency shutdown orders for ShareFile on-premises deployments, a pattern consistent with imminent or in-progress exploitation. This week: confirm whether your org or any critical SaaS vendors run on-prem ShareFile Storage Zone Controllers and request attestations; brief leadership before this surfaces in news as a repeat of the MoveIt incident.
