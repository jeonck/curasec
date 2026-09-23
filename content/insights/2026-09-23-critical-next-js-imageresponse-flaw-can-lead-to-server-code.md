---
title: "Critical Next.js ImageResponse SVG Input Can Trigger Server-Side RCE"
date: 2026-09-23T15:27:03.663698+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["nextjs", "rce", "web-security"]
cves: []
source: "https://thehackernews.com/2026/09/critical-nextjs-imageresponse-flaw-can.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Patch Next.js to the version released 2026-09-22 that fixes the ImageResponse RCE; audit any app that passes user-controlled input (e.g. URL parameters) into ImageResponse calls. No KEV listing or public PoC in signals, so patching this sprint is prudent but not emergency-level.
- **SOC/IR — Skip**
- **Leader — Skip**
