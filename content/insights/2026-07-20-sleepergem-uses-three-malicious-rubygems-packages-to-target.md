---
title: "SleeperGem: Three Malicious RubyGems Target Developer Machines"
date: 2026-07-20T13:16:24.819582+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["supply-chain", "rubygems", "malware"]
cves: []
source: "https://thehackernews.com/2026/07/sleepergem-uses-three-malicious.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** If you have Ruby projects, audit all dependency trees for git_credential_manager versions 2.8.0–2.8.3 and Dendreo versions 1.1.3–1.1.4; remove immediately and treat any developer machine that installed them since July 18 as potentially compromised.
- **SOC/IR — Act:** Hunt for installations of these specific gem versions in developer endpoint EDR telemetry and CI/CD build logs since July 18, 2026; any confirmed install warrants an assume-breach sweep of that machine for secondary payload execution.
- **Leader — Plan:** If your organization has Ruby developers, direct the engineering team to audit for these packages and assess developer workstation exposure this week — credential-stealing supply chain hits on dev machines can pivot to production secrets.
