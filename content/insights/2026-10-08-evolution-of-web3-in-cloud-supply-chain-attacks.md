---
title: "Unit 42: Web3 Infrastructure Abused in Cloud Supply Chain Attacks"
date: 2026-10-08T17:51:36.071186+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["supply-chain", "cloud-security", "web3"]
cves: []
source: "https://unit42.paloaltonetworks.com/web3-cloud-supply-chain-attacks/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Learn:** No enrichment signals (no KEV, PoC, or EPSS), but the technique of using Web3 infrastructure as a staging layer in supply chain attacks is worth reviewing to evaluate whether your package pipeline or CI/CD logs have unexpected outbound calls to decentralized endpoints.
- **SOC/IR — Learn:** No IOCs or ATT&CK mappings surfaced in the summary, making immediate detection work impractical; the research is worth reading to understand emerging supply chain TTP patterns for future hunt hypothesis development.
- **Leader — Skip**
