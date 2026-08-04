---
title: "Code-Poisoning Property Inference Attack Leaks ML Training Data"
date: 2026-07-20T14:31:24.569284+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Learn"
tags: ["ml-security", "supply-chain", "privacy"]
cves: []
source: "https://arxiv.org/abs/2607.15970"
source_name: "arXiv cs.CR"
status: "archived"
---
- **Engineer — Learn:** Novel attack vector where malicious code from public repos or coding agents embeds property-inference backdoors into ML training pipelines — no active exploitation or PoC, but teams training models on sensitive data (PII, clinical records) should factor code provenance auditing into their ML supply chain reviews.
- **SOC/IR — Skip**
- **Leader — Learn:** Research demonstrates that outsourced or open-source ML training code can be weaponized to leak properties of private training datasets; useful framing for AI governance policies covering code provenance in sensitive ML pipelines, but no immediate action is warranted.
