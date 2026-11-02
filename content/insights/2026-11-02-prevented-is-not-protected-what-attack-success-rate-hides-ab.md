---
title: "RAG Knowledge Poisoning Defenses Overstate Effectiveness via ASR Metric"
date: 2026-11-02T21:42:19.798907+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Learn"
tags: ["rag-security", "ai-ml", "research"]
cves: []
source: "https://arxiv.org/abs/2610.40742"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** If you're deploying RAG pipelines, this research shows that defenses evaluated purely on attack success rate can still introduce unexpected target-positive outputs — worth reviewing your evaluation framework before trusting any poisoning defense you've implemented.
- **SOC/IR — Skip**
- **Leader — Learn:** Useful context for AI governance discussions: defenses on enterprise RAG systems may have overstated efficacy, which matters when briefing on AI risk posture or assessing vendor claims about RAG security controls.
