---
title: "Eight Malicious npm Packages Delivering Overlord RAT and Stealer"
date: 2026-10-07T17:48:59.708516+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["supply-chain", "npm", "malware"]
cves: []
source: "https://thehackernews.com/2026/10/eight-malicious-npm-packages-downloaded.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active supply-chain compromise in npm with RAT and stealer payloads across 8 packages downloaded 40k+ times since Aug 2023. Audit all projects for the named MALFEX packages, remove any matches, and inspect CI/CD build logs for evidence of execution.
- **SOC/IR — Plan:** Named malware (Overlord RAT) and stealer campaign with developer-endpoint reach; obtain full IOC lists from the CloudSEK/Checkmarx reports and build detections for Overlord RAT callbacks and credential-stealer behaviors on developer workstations and CI runners.
- **Leader — Learn:** Illustrates ongoing npm supply-chain risk from low-signal lone-actor campaigns; useful background for a software supply chain risk discussion with engineering leadership, but not a systemic event requiring immediate escalation.
