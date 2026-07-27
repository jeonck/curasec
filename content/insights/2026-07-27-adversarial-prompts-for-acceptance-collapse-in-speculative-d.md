---
title: "ADSD Attack Collapses Speculative Decoding Acceptance, Slows LLM Inference 62%"
date: 2026-07-27T15:10:27.090935+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["adversarial-ml", "llm-security", "speculative-decoding"]
cves: []
source: "https://arxiv.org/abs/2607.21804"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** Novel prompt-suffix attack degrades speculative decoding throughput without corrupting outputs, affecting any deployment using draft-target inference acceleration (vLLM, TGI, etc.). No patch or mitigation exists yet; file this when designing LLM serving infrastructure to justify input validation and rate controls at the prompt layer.
- **SOC/IR — Skip**
- **Leader — Skip**
