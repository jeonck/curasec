---
title: "White House Staffers Running Residential Proxy Services on Devices"
date: 2026-11-05T18:42:10.964026+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["residential-proxy", "insider-threat", "endpoint-security"]
cves: []
source: "https://krebsonsecurity.com/2026/11/want-to-rent-an-internet-address-at-the-white-house/"
source_name: "Krebs on Security"
status: "active"
---
- **Engineer — Learn:** Residential proxy clients silently turning sensitive endpoints into exit nodes is a risk class worth understanding when designing MDM and approved-software policies; no immediate patch or configuration change required.
- **SOC/IR — Plan:** Build or tune endpoint detection for known residential proxy clients (e.g., Honeygain, IPRoyal, Peer2Profit) running on corporate devices — their presence means external traffic may egress under a trusted corporate IP, undermining network-based controls.
- **Leader — Learn:** This incident illustrates geopolitical and insider-risk exposure when employees run unauthorized proxy software on work or BYOD devices; useful input for a BYOD/approved-software policy review, but no immediate board-level action is required for most organizations.
