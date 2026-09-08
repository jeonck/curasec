---
title: "WeChat Zero-Click Worm Spreads via Incoming Calls on iOS and Android"
date: 2026-09-08T15:04:44.915544+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["zero-click", "mobile-security", "worm"]
cves: []
source: "https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** If WeChat is in your enterprise environment (especially for Asia-region business communications), verify the app is updated to a post-July 2026 patched version; the zero-click, no-answer-required attack surface makes unpatched installs high-severity even without active exploitation signals.
- **SOC/IR — Learn:** No IOCs, no mapped TTPs, and no evidence of active exploitation are provided; the worm propagation technique is notable for future detection design, but there is no actionable hunt or rule to write today.
- **Leader — Learn:** A research-stage demo with no confirmed active exploitation and an apparent Tencent patch in progress; revisit if Tencent confirms a breach or if exploitation surfaces, particularly if your org relies on WeChat for business communication with China-based partners.
