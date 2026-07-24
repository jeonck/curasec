---
title: "Bing malvertising campaign delivers SectopRAT via fake Claude installer"
date: 2026-07-24T12:43:46.515834+00:00
verdict: "Act"
verdict_engineer: "Learn"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["malvertising", "sectoprat", "ai-lure"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/fake-claude-app-promoted-by-bing-ads-pushes-sectoprat-malware/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** No direct infrastructure vulnerability here; the attack targets end users via social engineering. Worth noting that AI-tool-themed lures are an emerging pattern that should inform employee software-download guidance.
- **SOC/IR — Act:** Active SectopRAT delivery campaign in progress — query EDR telemetry for downloads of unofficial Claude installers and sweep endpoints for SectopRAT indicators; the BleepingComputer writeup likely contains file hashes and C2 indicators to feed into your SIEM.
- **Leader — Learn:** AI-tool-themed malvertising is a growing employee-targeting vector; useful context for justifying security-awareness investment, but no immediate leadership action required absent evidence of internal compromise.
