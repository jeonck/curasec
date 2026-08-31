---
title: "Flawed Noise Sampling Breaks Differential Privacy in MPC Systems"
date: 2026-08-31T19:07:02.788857+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["differential-privacy", "mpc", "cryptography"]
cves: []
source: "https://arxiv.org/abs/2608.27766"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** The paper exposes a fundamental flaw in sample-and-scale DP noise protocols, achieving near-100% membership-inference success against Orchard and DP-BREM+; engineers building federated analytics or DP aggregation pipelines should audit whether their noise-sampling implementation uses the vulnerable scaling approach.
- **SOC/IR — Skip**
- **Leader — Skip**
