---
title: "KVM x86 MMU Context Reset Bug on INIT Emulation (CVE-2026-99312)"
date: 2026-11-22T16:05:35.915127+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["kvm", "linux-kernel", "virtualization"]
cves: ["CVE-2026-99312"]
source: "https://www.cve.org/CVERecord?id=CVE-2026-99312"
source_name: "HN (cve)"
status: "active"
---
- **Engineer — Plan:** Affects Linux KVM hypervisor hosts; patch when your distro ships a kernel update. EPSS is near zero and no active exploitation, but a public PoC exists — plan to patch on next kernel maintenance window and verify KVM-based workloads (cloud VMs, CI runners) are covered.
- **SOC/IR — Skip**
- **Leader — Skip**
- **Signals:** CVE-2026-99312 — CISA KEV: not listed, EPSS 0.00, public PoC on GitHub
