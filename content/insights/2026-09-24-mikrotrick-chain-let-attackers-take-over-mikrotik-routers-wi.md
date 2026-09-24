---
title: "MikroTrick chain enables unauthenticated MikroTik router takeover"
date: 2026-09-24T15:49:46.689252+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Skip"
tags: ["mikrotik", "routeros", "ssh-exploit"]
cves: ["CVE-2026-67279", "CVE-2026-86060"]
source: "https://thehackernews.com/2026/09/mikrotrick-chain-let-attackers-take.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** CVE-2026-86060 is CISA KEV listed with a public PoC, and the chain enables unauthenticated admin takeover of internet-exposed RouterOS devices. Immediately patch RouterOS to the vendor-fixed version, disable SSH exposure on WAN interfaces, and audit firewall rules to confirm MikroTik management ports are not reachable from the internet.
- **SOC/IR — Act:** CVE-2026-86060 is KEV listed and attack logs confirm real-world exploitation; hunt for anomalous SSH sessions or new admin accounts on any MikroTik devices in the estate since the earliest known attack date, and add detections for unauthenticated admin-session establishment on edge routers.
- **Leader — Skip**
- **Signals:** CVE-2026-67279 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub · CVE-2026-86060 — CISA KEV: listed, EPSS 0.02, public PoC on GitHub
