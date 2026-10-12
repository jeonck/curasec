---
title: "Empirical Study: Vulnerable AI Models Widely Adopted Across OSS Repos"
date: 2026-10-12T21:14:27.524617+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["ai-supply-chain", "ml-security", "open-source"]
cves: []
source: "https://arxiv.org/abs/2610.12893"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Plan:** If your team loads models from HuggingFace, audit dependencies against InsightDB's flagged-model list and add provenance verification and model-scanning steps to your ML pipelines; the study found no sanitization logic in any of the observed integration patterns.
- **SOC/IR — Learn:** The research maps recurring integration anti-patterns (bypassed safety parameters, delegated trust) that improve understanding of how malicious models could persist post-compromise, but no IOCs or ATT&CK-mapped TTPs are provided for immediate detection work.
- **Leader — Plan:** The finding that 22% of publicly flagged vulnerable models are actively referenced across 5,000+ repositories quantifies AI supply chain exposure well enough to drive a policy and tooling review this quarter; use this data to scope an internal audit of third-party model usage before the board asks.
