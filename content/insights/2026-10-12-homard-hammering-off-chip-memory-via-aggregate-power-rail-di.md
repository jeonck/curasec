---
title: "HOMARD: Power-rail side channel recovers DRAM data on ARM SoCs"
date: 2026-10-12T21:14:27.524617+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["side-channel", "dram", "arm-soc"]
cves: []
source: "https://arxiv.org/abs/2610.12621"
source_name: "arXiv cs.CR"
status: "archived"
---
- **Engineer — Learn:** Novel attack class: unprivileged power-telemetry sensors can reverse-engineer DRAM addressing and recover secret bytes without timing, bypassing existing timer-based mitigations. No patch exists; relevant if you run sensitive workloads on ARM SoCs (Jetson, Pi-class boards) where power rail access is attacker-accessible.
- **SOC/IR — Skip**
- **Leader — Skip**
