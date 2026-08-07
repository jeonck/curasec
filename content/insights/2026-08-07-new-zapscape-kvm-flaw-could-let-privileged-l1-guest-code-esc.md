---
title: "Zapscape KVM Flaw Enables L1 Guest-to-Host Escape via Shadow MMU"
date: 2026-08-07T00:21:58.703649+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["kvm", "vm-escape", "linux-kernel"]
cves: ["CVE-2026-64561"]
source: "https://thehackernews.com/2026/08/new-zapscape-kvm-flaw-could-let.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC is available for this KVM/x86 shadow MMU escape; audit whether nested virtualization is exposed to untrusted guest workloads, then apply the latest Linux kernel patch or disable nested virt for those guests until patched.
- **SOC/IR — Learn:** No active exploitation observed (EPSS 0.00, not KEV-listed); the technique expands the mental model for hypervisor-escape detection, but there is no actionable hunt or IOC sweep to run today.
- **Leader — Skip**
- **Signals:** CVE-2026-64561 — CISA KEV: not listed, EPSS 0.00, public PoC on GitHub
