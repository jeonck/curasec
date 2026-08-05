---
title: "npm Worm from keyv@6.0.0 Poisons 868+ Packages, Plants IDE Hooks"
date: 2026-08-05T13:01:27.566949+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "npm", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/08/keyv-linked-npm-worm-poisons-hundreds.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Audit your full dependency tree immediately for any of the ~79–353 poisoned package names; packages downloaded since August 4 may contain credential-stealing code and rogue VS Code/Claude Code hooks. Rotate any secrets accessible from affected build environments and re-run CI pipelines from clean, verified dependency locks.
- **SOC/IR — Act:** Hunt for anomalous outbound connections and credential-use anomalies from developer workstations and CI/CD runners since August 4, 2026; also sweep for unexpected VS Code extension modifications or Claude Code hook installations that could indicate a compromised dev environment.
- **Leader — Act:** This is a systemic npm supply-chain event touching 868+ package versions—brief engineering leadership now, confirm whether any internal products or pipelines depend on keyv or Cacheable-namespace packages, and request an exposure report before the week ends.
