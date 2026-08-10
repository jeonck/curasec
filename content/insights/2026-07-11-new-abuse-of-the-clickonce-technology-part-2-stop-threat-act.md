---
title: "ClickOnce Abused for Persistent Threat Actor Access (Part 2)"
date: 2026-07-11T11:49:48.413664+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["windows", "persistence", "ttp"]
cves: []
source: "https://www.crowdstrike.com/en-us/blog/new-abuse-of-the-clickonce-technology-part-two/"
source_name: "CrowdStrike Blog"
status: "archived"
---
- **Engineer — Learn:** Describes how attackers abuse the ClickOnce deployment mechanism for persistence in Windows environments — no patch or config change indicated, but worth understanding if you deploy .NET apps or manage Windows estates.
- **SOC/IR — Plan:** New ClickOnce-based persistence TTP with public CrowdStrike analysis — build or tune detections around ClickOnce application installations and associated scheduled tasks or registry run keys in your SIEM/EDR.
- **Leader — Skip**
