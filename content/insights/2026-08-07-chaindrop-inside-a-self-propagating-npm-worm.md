---
title: "ChainDrop: Self-Propagating npm Worm Steals CI/CD Secrets via Blockchain C2"
date: 2026-08-07T00:21:58.703649+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["supply-chain", "npm", "ci-cd"]
cves: []
source: "https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/"
source_name: "Unit 42"
status: "archived"
---
- **Engineer — Act:** A self-propagating npm worm targeting GitHub Actions runner secrets is a direct threat to any CI/CD pipeline using npm packages; audit your runner logs for unexpected outbound calls to Ethereum RPC endpoints and review recently installed or updated npm dependencies for malicious scripts.
- **SOC/IR — Plan:** The blockchain-based C2 technique (Ethereum smart contracts for routing) is a novel evasion method worth building detections for; develop hunt queries for unusual npm postinstall script execution and outbound connections to Ethereum JSON-RPC endpoints from CI runners.
- **Leader — Learn:** This campaign illustrates how supply chain attacks are adopting decentralized infrastructure to evade takedowns — relevant context for board-level discussions on software supply chain risk and CI/CD security investment.
