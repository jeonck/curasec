---
title: "CVE-2026-89775: Linux KVM ARM64 Guest-Escape via Use-After-Free"
date: 2026-09-22T15:30:54.753130+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["linux-kernel", "virtualization", "guest-escape"]
cves: ["CVE-2026-89775"]
source: "https://thehackernews.com/2026/09/new-linux-kernel-flaw-gives-arm64-kvm.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC on GitHub for a guest-to-host escape on ARM64 KVM hosts with nested virtualization enabled demands immediate attention: patch the Linux kernel to the fixed version and, where nested virtualization is not required, disable it now to remove the attack surface.
- **SOC/IR — Learn:** No active exploitation is reported and EPSS is effectively zero, so there is no detection action to take today; however, understanding the KVM guest-escape technique is worth filing for future hunt hypothesis development should exploitation emerge.
- **Leader — Skip**
- **Signals:** CVE-2026-89775 — CISA KEV: not listed, EPSS 0.00, public PoC on GitHub
