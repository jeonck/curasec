---
title: "NatJack: NAT Manipulation Enables TCP Hijack and DNS Spoofing"
date: 2026-08-07T11:54:55.232717+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["network-attack", "tcp-hijacking", "dns-spoofing"]
cves: []
source: "https://thehackernews.com/2026/08/new-natjack-attacks-hijack-tcp-sessions.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Learn:** Novel attack class affecting multiple NAT implementations including Windows — no active exploitation or patches announced yet, so monitor for vendor advisories and evaluate whether firewall rule hardening or NAT timeout tuning applies to your perimeter.
- **SOC/IR — Learn:** NatJack introduces TCP session hijacking and DNS spoofing via NAT state manipulation; no IOCs or ATT&CK-mapped TTPs are available yet, so track for detection research as the community digests the Black Hat presentation.
- **Leader — Skip**
