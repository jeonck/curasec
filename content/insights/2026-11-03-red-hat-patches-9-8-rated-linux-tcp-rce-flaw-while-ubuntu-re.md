---
title: "Red Hat patches CVSS 9.8 Linux kernel TCP RCE; Ubuntu fix still in testing"
date: 2026-11-03T18:24:39.173812+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["linux-kernel", "rce", "patch"]
cves: ["CVE-2026-98432"]
source: "https://thehackernews.com/2026/11/red-hat-patches-98-rated-linux-tcp-rce.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Unauthenticated remote RCE via use-after-free in the IPv4 TCP stack is serious, but EPSS 0.01 and no KEV listing temper urgency despite the public PoC. Patch RHEL 8/9/10 systems this sprint; for Ubuntu LTS, enable the testing channel or monitor for the stable backport before it reaches your standard update window.
- **SOC/IR — Skip**
- **Leader — Skip**
- **Signals:** CVE-2026-98432 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub, reported by 2 collected sources
