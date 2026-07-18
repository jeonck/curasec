---
title: "Seven Malicious Vite npm Packages Deploy RAT via Blockchain C2"
date: 2026-07-18T11:51:11.203777+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["supply-chain", "npm", "malware"]
cves: []
source: "https://thehackernews.com/2026/07/seven-malicious-vite-npm-packages-use.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Supply chain compromise targeting a widely-used frontend toolchain is a direct risk to any team using Vite or related npm packages; audit your dependency tree immediately for the seven ViteVenom packages and inspect CI/CD build logs for unexpected outbound connections to Tron blockchain endpoints.
- **SOC/IR — Plan:** The four-tier blockchain-based C2 using Tron is a novel evasion technique worth building detections for; develop hunt logic to flag anomalous blockchain API calls originating from build runners or developer workstations, and add this TTP to your supply-chain detection backlog.
- **Leader — Learn:** This campaign illustrates how adversaries are embedding resilient, blockchain-routed C2 in developer tooling supply chains; worth referencing in future discussions about secure software development lifecycle risk and third-party dependency governance.
