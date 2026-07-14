---
title: "148 Malicious npm Packages Weaponized Browsers as DDoS Botnet"
date: 2026-07-14T12:08:08.109802+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["npm", "supply-chain", "ddos"]
cves: []
source: "https://thehackernews.com/2026/07/148-npm-packages-disguised-as-student.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Novel abuse of npm as free hosting infrastructure to serve malicious browser-side JavaScript to site visitors rather than targeting package consumers directly; review whether your org hosts any user-facing content via npm and revisit supply-chain threat models to include registry-as-CDN attack patterns.
- **SOC/IR — Learn:** No IOCs or ATT&CK-mapped TTPs are published from this research, so there is nothing actionable to hunt or detect today; file as a reference technique — browser-based DDoS recruited via malicious proxy sites — for future detection engineering when lure sites targeting your sector emerge.
- **Leader — Skip**
