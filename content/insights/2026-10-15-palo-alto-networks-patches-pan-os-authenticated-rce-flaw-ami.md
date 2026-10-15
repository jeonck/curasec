---
title: "PAN-OS Authenticated RCE CVE-2026-0322 Actively Exploited, CISA KEV Listed"
date: 2026-10-15T15:35:13.586755+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["pan-os", "rce", "cisa-kev"]
cves: ["CVE-2026-0322"]
source: "https://thehackernews.com/2026/10/palo-alto-networks-patches-pan-os.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** CISA KEV listed plus a public PoC and confirmed active exploitation make this urgent — apply the PAN-OS patch immediately and restrict management interface access to trusted IP ranges only.
- **SOC/IR — Act:** Active exploitation of a perimeter security appliance warrants an assume-breach posture — hunt for anomalous management-plane activity and lateral movement from PAN-OS devices dating back to initial disclosure.
- **Leader — Act:** PAN-OS is perimeter infrastructure for many enterprises; confirm whether it is in use, verify engineering has an emergency patch window in progress, and be ready to respond to customer or board questions given the CISA KEV designation and confirmed active exploitation.
- **Signals:** CVE-2026-0322 — CISA KEV: listed, EPSS 0.01, public PoC on GitHub, reported by 2 collected sources
