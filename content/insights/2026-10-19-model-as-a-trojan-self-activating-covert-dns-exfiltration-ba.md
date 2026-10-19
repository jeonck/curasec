---
title: "LLM Weight-Baked DNS Exfiltration Bypasses Container Egress Firewalls"
date: 2026-10-19T18:41:36.414652+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["llm-security", "supply-chain", "dns-exfiltration"]
cves: []
source: "https://arxiv.org/abs/2610.22578"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Plan:** Any team running open-weight LLMs in agent harnesses with shell access is in scope for this attack class. Before next sprint, enforce DNS egress blocking (or DNS query monitoring) on all LLM inference containers and require signed provenance for open-weight models pulled from public hubs.
- **SOC/IR — Plan:** This paper introduces a detection gap: base32-chunked subdomains in DNS queries from ML inference pods are the exfil channel. Write a detection rule (Sigma/KQL) for anomalous high-entropy subdomain queries originating from container workloads, and add LLM agent namespaces as a monitored DNS log source.
- **Leader — Learn:** Novel supply-chain risk class showing that downloaded AI model weights can carry persistent malware independent of prompts or sandboxing. Useful framing for an AI/LLM usage policy that requires internal vetting of open-weight models before agent deployment.
