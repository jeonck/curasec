---
title: "BragJack PoC hijacks AI browser agents via malicious extensions"
date: 2026-09-20T14:41:12.964217+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["ai-agents", "browser-security", "supply-chain"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/bragjack-attacks-hijack-ai-browser-agents-through-malicious-extensions/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** Novel PoC technique shows how a malicious browser extension can subvert AI agent behavior through prompt injection — no active exploitation, but engineers building AI browser integrations should review extension permission boundaries and agent trust models now.
- **SOC/IR — Learn:** No IOCs, no active campaigns, and no mapped TTPs yet; file the malicious-extension-as-AI-hijack vector for future detection engineering as AI browser agents proliferate in enterprise estates.
- **Leader — Plan:** Two CVEs and a $20K bounty signal vendors take this seriously — assess whether any enterprise AI browser tooling (Perplexity Comet, Claude in Chrome, Edge Copilot) is deployed in the environment and add browser-agent risk to the AI governance policy review this quarter.
