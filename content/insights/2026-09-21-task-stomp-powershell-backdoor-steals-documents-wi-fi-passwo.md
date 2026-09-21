---
title: "TASK#STOMP PowerShell Backdoor Harvests Docs, Wi-Fi Creds, Clipboard"
date: 2026-09-21T17:01:38.950105+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["powershell", "data-exfiltration", "malware"]
cves: []
source: "https://thehackernews.com/2026/09/taskstomp-powershell-backdoor-steals.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No CVE, no patch surface, and no enrichment signals indicating active exploitation of a specific software component — the campaign details inform threat modeling but require no immediate engineering action.
- **SOC/IR — Plan:** The documented capabilities — real-time filesystem monitoring, clipboard theft, screenshot capture, and Wi-Fi credential harvesting via PowerShell — map to detectable ATT&CK techniques; build or tune detections for PowerShell processes performing bulk file enumeration and outbound data staging this quarter.
- **Leader — Skip**
