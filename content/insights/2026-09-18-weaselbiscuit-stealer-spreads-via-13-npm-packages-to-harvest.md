---
title: "WeaselBiscuit JS Stealer Delivered via 13 Malicious npm Packages"
date: 2026-09-18T14:58:07.079452+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["npm-supply-chain", "dprk", "stealer-malware"]
cves: []
source: "https://thehackernews.com/2026/09/weaselbiscuit-stealer-spreads-via-13.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Supply-chain compromise via npm is directly in scope — audit your package-lock.json and dependency trees for these 13 named packages immediately, remove any matches, and rotate credentials and tokens accessible from affected developer workstations or CI runners.
- **SOC/IR — Plan:** The overlap with DPRK's Contagious Interview campaign (BeaverTail TTPs) gives a detection anchor — build or tune rules for suspicious npm package installs on developer endpoints and Chrome extension storage access patterns consistent with credential harvesting.
- **Leader — Learn:** A DPRK-linked supply-chain operation targeting developer npm environments is worth adding to the developer-risk section of the risk register, but no systemic or vendor-level exposure is confirmed yet — monitor for follow-on reporting.
