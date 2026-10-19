---
title: "KV Cache Reuse in LLM Reasoning Traces Enables Stealthy Poisoning"
date: 2026-10-19T18:41:36.414652+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["llm-security", "cache-poisoning", "ai-security"]
cves: []
source: "https://arxiv.org/abs/2610.22873"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** Novel black-box attack class against LLM inference systems using shared KV caches for reasoning trace reuse — engineers building or deploying such systems should audit whether their architecture exposes shared cache state across users or sessions, and treat this as a design constraint before enabling reasoning-cache reuse features.
- **SOC/IR — Skip**
- **Leader — Skip**
