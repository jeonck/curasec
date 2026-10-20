---
title: "OVHcloud CLI backdoored on GitHub to distribute info-stealer"
date: 2026-10-20T15:39:31.280324+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Act"
tags: ["supply-chain", "info-stealer", "developer-tools"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/ovhcloud-cli-releases-backdoored-on-github-to-steal-developer-secrets/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Confirmed supply-chain compromise of a developer CLI tool; audit all developer machines for the backdoored OVHcloud CLI version and immediately rotate any API keys, tokens, or credentials that the tool could have accessed.
- **SOC/IR — Plan:** Active info-stealer deployed via compromised CLI; without published IOCs, queue a hunt for anomalous credential access or exfiltration activity originating from developer endpoints that run cloud CLI tooling.
- **Leader — Act:** A cloud provider's official CLI was weaponized to steal developer secrets — confirm this week whether engineering teams use OVHcloud CLI and request OVHcloud's incident report detailing which versions were affected and what credentials may be at risk.
