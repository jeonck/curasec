---
title: "LiHA: Lightweight MAC-based IP source authentication via eBPF/FPGA"
date: 2026-11-02T21:42:19.798907+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["ip-spoofing", "network-security", "research"]
cves: []
source: "https://arxiv.org/abs/2610.40928"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** Novel eBPF-implementable approach to source IP authentication that requires no per-flow state or handshakes — worth tracking for future network hardening designs, but no running system to patch or reconfigure today.
- **SOC/IR — Learn:** Provides useful conceptual framing for how IP spoofing could be constrained at the data plane, but the paper yields no IOCs, TTPs, or detection rules to act on now.
- **Leader — Skip**
