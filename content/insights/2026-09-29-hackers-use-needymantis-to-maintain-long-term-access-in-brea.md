---
title: "NeedyMantis Malware Used for Long-Term Persistence in Targeted Networks"
date: 2026-09-29T16:53:02.010350+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["malware", "persistence", "threat-intel"]
cves: []
source: "https://thehackernews.com/2026/09/hackers-use-needymantis-to-maintain.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No CVEs or patchable components identified; this is a post-breach persistence tool, not a vulnerability in software engineers typically run. Understanding long-term access techniques can inform detection instrumentation in logging pipelines.
- **SOC/IR — Plan:** Microsoft's technical analysis on NeedyMantis likely contains TTPs and behavioral indicators worth translating into detection rules; review the full report and develop or tune persistence-detection logic (scheduled tasks, registry run keys, lateral movement patterns) for the affected verticals.
- **Leader — Skip**
