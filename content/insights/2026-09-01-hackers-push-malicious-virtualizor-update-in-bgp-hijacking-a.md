---
title: "BGP Hijack Delivers Malicious Updates to Virtualizor VPS Software"
date: 2026-09-01T15:28:52.066055+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["supply-chain", "bgp-hijacking", "virtualizor"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-push-malicious-virtualizor-update-in-bgp-hijacking-attack/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Any environment running Virtualizor may have received a trojaned update; immediately verify installed binary integrity against known-good checksums and audit servers for post-compromise artifacts. If update timestamps align with the hijack window, treat the host as compromised and scope accordingly.
- **SOC/IR — Act:** Identify all Virtualizor-managed hosts in the estate and flag them for assume-breach review; hunt for unusual process execution, outbound connections, or file modifications following recent update activity on those hosts.
- **Leader — Learn:** BGP hijacking to intercept software update traffic is a sophisticated supply-chain vector that bypasses code-signing assumptions when the update mechanism itself is redirected; useful context for reviewing how third-party software update trust is modeled in your vendor risk program.
