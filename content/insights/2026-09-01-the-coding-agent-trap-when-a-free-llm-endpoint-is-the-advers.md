---
title: "Malicious Free LLM Endpoints Silently Harvesting Coding-Agent Context"
date: 2026-09-01T15:28:52.066055+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["ai-agents", "supply-chain", "llm-security"]
cves: []
source: "https://isc.sans.edu/diary/rss/33298"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** Honeypot research shows that untrusted 'free' LLM backends receive full coding-agent context — filesystem paths, conversation history, tool manifests — before any response is sent. Audit every LLM endpoint configured in your coding agents and ensure all traffic goes to verified, first-party providers.
- **SOC/IR — Learn:** Demonstrates a passive exfiltration path: coding agents silently send working paths and tool manifests to whatever endpoint they're pointed at. No IOCs or active campaign here, but useful context for future detections around unexpected outbound HTTPS from dev tools to novel LLM API hosts.
- **Leader — Plan:** Employees using unofficial 'free' AI coding tools may be routing sensitive codebase context and filesystem details to unverified third parties; establish or enforce an approved-LLM-provider policy for coding agents this quarter before an incident forces a reactive response.
