---
title: "Wraith: modern browser-hooking framework for red teams"
date: 2026-08-04T13:07:50.076253+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["browser-exploitation", "red-team", "xss"]
cves: []
source: "https://github.com/Arcanum-Sec/wraith"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Learn:** A BeEF successor with modern browser-hooking capabilities signals evolving client-side attack surface; useful for understanding what blind-XSS scenarios look like in 2026 to inform CSP and output-encoding posture reviews.
- **SOC/IR — Plan:** Evaluate Wraith's hooking techniques against current detection coverage for browser-side implants and blind-XSS callbacks; consider adding detections for outbound beacon patterns it generates if not already covered by existing XSS hunting rules.
- **Leader — Skip**
