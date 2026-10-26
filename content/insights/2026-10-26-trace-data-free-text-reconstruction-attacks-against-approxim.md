---
title: "TRACE: Attack Reconstructs Supposedly Unlearned LLM Training Data"
date: 2026-10-26T18:39:19.902923+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Learn"
tags: ["llm-security", "privacy-risk", "ai-unlearning"]
cves: []
source: "https://arxiv.org/abs/2610.31995"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** Novel research showing that maintaining pre/post unlearning model snapshots creates a recoverable side channel — relevant if you operate LLMs with approximate unlearning workflows. No patch exists; redesign signal is to avoid retaining both snapshots together or treat unlearning as non-binding from a data-exposure standpoint.
- **SOC/IR — Skip**
- **Leader — Learn:** Organizations using approximate LLM unlearning to satisfy GDPR right-to-erasure or similar data removal obligations may be overstating compliance guarantees — this research undermines the privacy claim of that approach. Worth flagging to DPO and AI governance leads if the company relies on unlearning in customer-data contexts.
