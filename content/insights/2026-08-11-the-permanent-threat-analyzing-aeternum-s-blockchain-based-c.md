---
title: "Aeternum Botnet Uses Polygon Blockchain for Decentralized C2"
date: 2026-08-11T11:54:43.298939+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["botnet", "c2-infrastructure", "blockchain"]
cves: []
source: "https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Learn:** Blockchain-based C2 is an emerging evasion technique that may bypass traditional domain-blocking controls; no patch or configuration action required, but architects should consider that blocking Polygon RPC endpoints could disrupt legitimate Web3 tooling.
- **SOC/IR — Plan:** Build or tune detections for outbound calls to Polygon RPC endpoints (e.g., polygon-rpc.com) from non-Web3 workloads, and develop hunting queries for processes that query smart contract ABI methods as a C2 channel.
- **Leader — Learn:** Blockchain-anchored C2 represents a structural evasion of perimeter controls; useful context for future investments in DNS/network monitoring that can handle decentralized infrastructure, but no immediate leadership action required.
