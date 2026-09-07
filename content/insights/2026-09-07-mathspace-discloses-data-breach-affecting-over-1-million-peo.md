---
title: "Mathspace breach via Metabase exposes 1M+ student and staff records"
date: 2026-09-07T16:27:04.378719+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Learn"
tags: ["data-breach", "metabase", "education"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/mathspace-discloses-data-breach-affecting-over-1-million-people/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Metabase is widely self-hosted as an internal analytics/BI tool; audit your own Metabase instance for misconfigurations or unpatched CVEs that may match the attack vector used here, and verify network exposure of the service.
- **SOC/IR — Skip**
- **Leader — Learn:** A 1M+ record breach via an internal BI tool (Metabase) at an ed-tech vendor illustrates third-party analytics platform risk, but requires no immediate leadership action for organizations not using Mathspace.
