---
title: "FakeGit: 7,600 malicious GitHub repos spread SmartLoader/StealC"
date: 2026-07-22T12:46:13.866991+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["supply-chain", "malware", "github"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/fakegit-campaign-uses-7-600-github-repos-to-push-smartloader-malware/"
source_name: "BleepingComputer"
status: "archived"
---
- **Engineer — Act:** A supply-chain campaign at GitHub scale (14M downloads) meets the Act threshold even without KEV/EPSS signals. Audit CI/CD build logs and dependency fetches for downloads from unknown or newly-created GitHub repos, and scan endpoints for SmartLoader and StealC indicators.
- **SOC/IR — Plan:** The campaign is active but the summary lacks specific IOCs needed for immediate sweeps. Build or tune detections for StealC infostealer behaviors (credential harvesting, C2 beaconing) and generic loader staging patterns; monitor research feeds for published IOC lists to operationalize hunting.
- **Leader — Plan:** Fourteen million downloads signals broad potential exposure across engineering teams. This quarter, review whether developer workflows enforce source verification for GitHub-sourced dependencies and consider a policy requiring reviewed or pinned third-party code.
