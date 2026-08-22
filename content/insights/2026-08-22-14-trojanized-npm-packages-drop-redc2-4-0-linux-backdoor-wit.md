---
title: "14 Trojanized npm Packages Deploy RedC2 4.0 Linux Backdoor via Supply Chain"
date: 2026-08-22T11:32:44.405318+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["supply-chain", "npm", "linux-malware"]
cves: []
source: "https://thehackernews.com/2026/08/14-trojanized-npm-packages-drop-redc2.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active supply-chain compromise in npm packages is an Act signal regardless of KEV status — audit your dependency tree immediately for these 14 packages masquerading as calendar/streak utilities and check CI build logs for processes spawned by node_modules executing detached binaries.
- **SOC/IR — Plan:** The implant's load behavior — extracting a bundled binary, chmod-ing it, and launching it as a detached process — is a detectable Linux TTP; build or tune EDR rules to alert on node/npm processes spawning unexpected child executables, but the summary lacks IOCs or package names needed to hunt right now.
- **Leader — Plan:** An active npm supply-chain campaign using AI-assisted C2 signals an escalating threat class; this quarter, direct engineering to verify SCA tooling covers npm and confirm your CI pipelines would catch a malicious package load before it reaches production.
