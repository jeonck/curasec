---
title: "GIDS-Eval: Graph-Based NIDS Benchmarks Show Major Evaluation Gaps"
date: 2026-09-14T18:03:45.849563+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["network-intrusion-detection", "detection-evasion", "security-research"]
cves: []
source: "https://arxiv.org/abs/2609.12263"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** Research reveals that graph-based NIDS benchmarks are largely artifacts of preprocessing and windowing choices, not detector quality — relevant if evaluating or procuring NIDS solutions, but no running system to change today.
- **SOC/IR — Learn:** The finding that two crafted edges achieve full evasion against multiple detector-dataset pairs is a meaningful signal about coverage gaps in graph-based NIDS; useful context when assessing your network detection stack's real-world reliability, though no detection tuning is actionable from this paper alone.
- **Leader — Skip**
