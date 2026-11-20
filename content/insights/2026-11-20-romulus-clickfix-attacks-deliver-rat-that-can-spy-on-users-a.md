---
title: "ROMULUS ClickFix Campaign Delivers Undocumented RAT via Sideloading"
date: 2026-11-20T19:04:41.748130+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["malware", "clickfix", "rat"]
cves: []
source: "https://thehackernews.com/2026/11/romulus-clickfix-attacks-deliver-rat.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** ClickFix combined with signed binary sideloading is an increasingly common delivery chain worth understanding for endpoint and browser hardening decisions, but no specific software to patch or CVE to track here.
- **SOC/IR — Plan:** Build or tune detections for ClickFix social-engineering patterns (clipboard-paste execution) and signed-binary sideloading (T1574.002); no IOCs are published in this report, so immediate hunting isn't actionable yet.
- **Leader — Skip**
