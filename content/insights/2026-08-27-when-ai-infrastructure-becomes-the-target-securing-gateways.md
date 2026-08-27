---
title: "Microsoft TI: LiteLLM gateways actively exploited for cred theft and cryptomining"
date: 2026-08-27T21:01:55.123618+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["ai-infrastructure", "credential-harvesting", "cryptomining"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/08/26/when-ai-infrastructure-becomes-target-securing-gateways-control-points/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Plan:** Microsoft Threat Intelligence documents active exploitation of exposed LiteLLM gateways leading to credential theft and persistence — no KEV or PoC signal, but if you run LiteLLM or similar AI proxies, audit internet exposure, rotate API keys, and verify no unauthorized processes are running on those hosts.
- **SOC/IR — Act:** Active attack chain with detectable post-exploitation stages (credential harvesting, persistence, cryptomining) reported by Microsoft TI — pull the blog post for IOCs, then hunt for anomalous processes and outbound connections on any hosts running AI gateway software since the publication date.
- **Leader — Plan:** AI workloads are now an established attack surface for credential theft and resource abuse; this quarter, ensure AI infrastructure (gateways, API proxies, GPU hosts) is included in your hardening and access-review scope alongside traditional edge assets.
