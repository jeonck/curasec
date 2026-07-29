---
title: "Critical OpenWrt DHCPv6 RCE (CVE-2026-53921) — PoC Public, Patch Out"
date: 2026-07-29T13:07:14.832066+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["openwrt", "rce", "network-devices"]
cves: ["CVE-2026-53921"]
source: "https://thehackernews.com/2026/07/critical-openwrt-dhcpv6-flaw-could-let.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC exists for this CVSS 9.8 unauthenticated stack overflow in odhcpd, which is enabled by default. Upgrade all OpenWrt devices to 24.10.8 immediately, or disable DHCPv6/odhcpd on devices that don't need it.
- **SOC/IR — Plan:** With a public PoC now available, exploitation of internet- or LAN-exposed OpenWrt edge devices is imminent. Build detections for anomalous DHCPv6 traffic volumes and unexpected child processes from odhcpd, and queue a sweep of managed OpenWrt-based appliances for signs of prior compromise.
- **Leader — Skip**
- **Signals:** CVE-2026-53921 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
