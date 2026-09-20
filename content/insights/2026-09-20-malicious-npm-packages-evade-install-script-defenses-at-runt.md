---
title: "Malicious npm packages evade install-script defenses at runtime"
date: 2026-09-20T14:41:12.964217+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["supply-chain", "npm", "malware-evasion"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/malicious-npm-packages-evade-install-script-defenses-at-runtime/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** This evasion class specifically defeats install-hook-only defenses (e.g., --ignore-scripts, tools that only scan lifecycle scripts); audit whether your SCA/supply-chain tooling monitors runtime behavior, and check all dependency trees for the 'indexed-btree' package.
- **SOC/IR — Learn:** The technique — embedding malicious logic in runtime code rather than install hooks — expands the detection surface for npm supply-chain attacks; no IOCs or TTPs are published here yet, but pipeline and CI runtime behavior monitoring becomes more relevant as a future detection investment.
- **Leader — Learn:** Ongoing npm campaigns are evolving past basic supply-chain controls, reinforcing the case for mature SCA investment; no systemic or board-level event without corroborating signals, but useful context for software supply chain security program reviews.
