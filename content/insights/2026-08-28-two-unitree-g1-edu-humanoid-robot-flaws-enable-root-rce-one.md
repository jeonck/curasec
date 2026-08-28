---
title: "Unitree G1 EDU Robot: Dual Root RCE Flaws, One via Bluetooth"
date: 2026-08-28T21:21:40.237236+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["rce", "iot-security", "embedded"]
cves: ["CVE-2026-76639", "CVE-2026-76640"]
source: "https://thehackernews.com/2026/08/two-unitree-g1-edu-humanoid-robot-flaws.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** If your environment uses Unitree G1 EDU robots, review network segmentation and disable unnecessary BLE/network services; no KEV listing and near-zero EPSS suggest limited active exploitation pressure, but public PoCs exist so schedule patching.
- **SOC/IR — Skip**
- **Leader — Skip**
- **Signals:** CVE-2026-76639 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub · CVE-2026-76640 — CISA KEV: not listed, EPSS 0.00, public PoC on GitHub
