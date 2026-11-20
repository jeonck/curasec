---
title: "Unpatched Windows FastUnlock 0-Day Grants Limited Access via Physical Touch"
date: 2026-11-20T19:04:41.748130+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["windows", "zero-day", "physical-access"]
cves: []
source: "https://thehackernews.com/2026/11/new-unpatched-windows-0-day-fastunlock.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Physical access requirement and limited (non-admin) privilege outcome narrow the blast radius significantly; no patch exists yet and no exploitation signals, but engineers managing Windows endpoints should monitor for a Microsoft advisory and evaluate whether compensating controls like disabling fast startup or enforcing full-disk encryption are already in place.
- **SOC/IR — Learn:** No IOCs, no active exploitation, and no remote attack vector means there is no detection or hunting action today; relevant only as background context for insider-threat or stolen-laptop scenarios.
- **Leader — Skip**
