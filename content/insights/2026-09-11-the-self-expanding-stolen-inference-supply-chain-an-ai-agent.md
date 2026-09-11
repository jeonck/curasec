---
title: "AI Agent Harvests and Re-Sells Stolen LLM API Access"
date: 2026-09-11T14:58:57.702490+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["ai-security", "llm-infrastructure", "supply-chain"]
cves: []
source: "https://isc.sans.edu/diary/rss/33332"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Plan:** Novel offensive technique targeting poorly secured LLM resale gateways via common web flaws and account farming; if you expose or consume LLM APIs, audit API key scoping, rate-limit enforcement, and gateway authentication to reduce your harvesting attack surface this quarter.
- **SOC/IR — Plan:** Semi-autonomous agent TTPs for LLM access harvesting are emerging; build detections for anomalous LLM API usage spikes, unexpected source IPs on API keys, and rapid account-creation patterns against any internal or vendor LLM gateway.
- **Leader — Learn:** Illustrates an emerging AI supply chain risk where LLM inference costs and access can be stolen at scale through ordinary web weaknesses; useful framing for an AI governance policy discussion, but no immediate leadership action required without confirmed vendor impact.
