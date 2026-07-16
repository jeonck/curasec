---
title: "AsyncAPI npm supply chain compromise via weaponized CI/CD workflows"
date: 2026-07-16T12:18:39.346883+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "npm", "ci-cd"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Act:** Confirmed supply chain compromise of AsyncAPI npm packages with import-time malware execution — audit all projects for AsyncAPI dependencies, check CI/CD build logs for the affected package versions, and rotate any secrets accessible from compromised build environments.
- **SOC/IR — Act:** Active campaign with malware delivered at import time via npm means CI/CD runner telemetry is the primary hunt surface — sweep build system logs for suspicious outbound connections or process spawns during npm install/import phases since the compromise window, and tune EDR rules to flag unusual child processes from package managers.
- **Leader — Act:** A weaponized CI/CD supply chain attack of this type can expose credentials and intellectual property across every project that consumed the affected packages — confirm internally whether AsyncAPI packages are in use, request an exposure assessment from engineering, and prepare to brief leadership given the potential scope.
