---
title: "NTP Pool Servers Abused to Harvest and Scan IPv6 Client Addresses"
date: 2026-07-27T15:10:27.090935+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["ipv6", "ntp", "reconnaissance"]
cves: []
source: "https://arxiv.org/abs/2607.21903"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Plan:** If your systems query the NTP Pool and expose IPv6 addresses, those addresses may be harvested and subsequently port-scanned or enumerated by rogue pool members. Plan to evaluate replacing NTP Pool entries with specific trusted NTP servers (cloud-provider NTP, dedicated stratum-2 servers) in IPv6-enabled environments.
- **SOC/IR — Learn:** The research identifies a mechanism — rogue NTP Pool membership — by which adversaries can build targeted IPv6 address lists for reconnaissance; useful context for understanding scanning sources, but no specific IOCs or ATT&CK-mapped TTPs are provided here for immediate detection work.
- **Leader — Skip**
