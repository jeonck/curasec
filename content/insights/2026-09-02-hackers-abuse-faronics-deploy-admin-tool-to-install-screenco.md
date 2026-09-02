---
title: "Hackers abuse Faronics Deploy to silently install ScreenConnect RAT"
date: 2026-09-02T15:05:08.783541+00:00
verdict: "Act"
verdict_engineer: "Learn"
verdict_soc: "Act"
verdict_leader: "Skip"
tags: ["remote-access", "phishing", "endpoint"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-abuse-faronics-deploy-admin-tool-to-install-screenconnect/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** No CVE or patch involved — attackers are abusing a legitimate admin tool's functionality. Review whether Faronics Deploy is in your environment and whether its deployment permissions are appropriately scoped.
- **SOC/IR — Act:** Hunt for unexpected ScreenConnect installations originating from Faronics Deploy processes; build detections for remote-management tool deployments not initiated by IT change management workflows.
- **Leader — Skip**
