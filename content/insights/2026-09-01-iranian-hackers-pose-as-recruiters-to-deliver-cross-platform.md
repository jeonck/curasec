---
title: "Nimbus Manticore Delivers Cross-Platform Node.js RATs via Fake Recruiting Coding Tests"
date: 2026-09-01T15:28:52.066055+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["apt", "malware", "social-engineering"]
cves: []
source: "https://thehackernews.com/2026/09/iranian-hackers-pose-as-recruiters-to.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No KEV or PoC; the threat is primarily social-engineering toward developers, not a patchable software flaw. Worth reviewing whether developer workstations enforce controls on arbitrary Node.js execution from downloaded archives.
- **SOC/IR — Plan:** Two new undocumented cross-platform RAT families using Node.js/JavaScript targeting Linux and macOS; build behavioral detections for suspicious Node.js child-process spawning on developer endpoints following unsolicited external file execution.
- **Leader — Learn:** Iranian state actor expanding toolset to target developers on Linux and macOS via recruitment lures — useful background for the next security-awareness cycle, but no immediate leadership action is indicated without published IOCs or sector-specific targeting data.
