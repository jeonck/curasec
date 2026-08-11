---
title: "jscrambler 8.14.0 npm Supply-Chain Compromise Drops Infostealer"
date: 2026-07-12T11:56:34.126082+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "npm", "infostealer"]
cves: []
source: "https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Act:** A preinstall hook in jscrambler 8.14.0 drops and executes a cross-platform native infostealer — this is live supply-chain compromise. Audit all CI/CD pipelines and developer machines for installs of this exact version, remove or pin away from 8.14.0, and treat any affected environment as potentially credential-compromised.
- **SOC/IR — Act:** Hunt for jscrambler 8.14.0 installs in npm audit logs, CI runner job histories, and artifact caches since July 11, 2026; on affected endpoints look for unexpected native binary drops or executions spawned from the npm install process, as infostealer data exfiltration may have already occurred.
- **Leader — Act:** Confirm this week whether jscrambler 8.14.0 reached any company build pipeline or developer workstation; if so, treat as a credential-theft incident — initiate credential rotation and brief relevant stakeholders, since infostealers harvest tokens, SSH keys, and secrets stored on the machine.
