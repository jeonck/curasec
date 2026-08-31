---
title: "DP Bounds on LLM Memorization vs. Extraction Are Not Interchangeable"
date: 2026-08-31T19:07:02.788857+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["differential-privacy", "llm-security", "research"]
cves: []
source: "https://arxiv.org/abs/2608.27782"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** If you rely on DP guarantees to protect training data in ML pipelines, this research shows that controlling memorization and controlling extraction are formally separate — a model can be memorized yet unextractable, or vice versa. Revisit your threat model assumptions, but no system change is required today.
- **SOC/IR — Skip**
- **Leader — Skip**
