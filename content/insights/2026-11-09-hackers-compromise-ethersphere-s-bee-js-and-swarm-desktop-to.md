---
title: "bee-js and Swarm Desktop Compromised via Release Automation Hijack"
date: 2026-11-09T21:25:24.006803+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["supply-chain", "npm", "malware"]
cves: []
source: "https://thehackernews.com/2026/11/hackers-compromise-etherspheres-bee-js.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Confirmed supply-chain compromise via release automation: if bee-js 13.3.0 or Swarm Desktop 0.56.2 appears in any dependency tree or build artifact, treat the build environment as potentially backdoored — remove the malicious versions, audit CI/CD logs for outbound connections, and rotate any Swarm wallet credentials accessible from those builds.
- **SOC/IR — Act:** Malicious npm package with backdoor installation capability warrants an immediate sweep of build and developer systems for bee-js 13.3.0 or Swarm Desktop 0.56.2; look for anomalous outbound network activity from CI runners or developer workstations that installed these versions during the exposure window.
- **Leader — Learn:** This is a confirmed release-automation hijack enabling malware distribution — a pattern increasingly used against software supply chains; relevant for evaluating whether software supply chain controls (signed releases, dependency pinning, pipeline integrity checks) belong in this year's investment priorities.
