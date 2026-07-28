---
title: "24,000+ internet-exposed BMCs leaking password hashes via 20-year-old flaw"
date: 2026-07-28T13:01:43.287328+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["bmc", "ipmi", "exposed-infrastructure"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/over-24-000-exposed-server-bmcs-leak-password-hash-via-decades-old-flaw/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Internet-exposed BMC/IPMI interfaces leaking password hashes represent an immediately exploitable misconfiguration — anyone can harvest and crack those hashes for out-of-band server access. Audit all BMC/IPMI interfaces for internet reachability now and move them behind an OOB management network or VPN; rotate any credentials on exposed units.
- **SOC/IR — Plan:** No IOCs or active campaign are cited, so there is no immediate hunt to launch, but external scanning of IPMI port 623 is trivially cheap for attackers. Build or tune detections for inbound connections to BMC management ports from non-management-network sources.
- **Leader — Plan:** Twenty-four thousand exposed instances signals a systemic industry hygiene failure; direct engineering to confirm no BMC interfaces in your estate are internet-reachable this quarter, and add management-plane network segmentation to your next control review.
