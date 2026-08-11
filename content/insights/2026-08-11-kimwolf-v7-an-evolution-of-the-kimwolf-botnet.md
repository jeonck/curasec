---
title: "Kimwolf v7 Botnet Uses Ethereum ENS for C2 and Tor Backup Routing"
date: 2026-08-11T11:54:43.298939+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["botnet", "android-iot", "c2-evasion"]
cves: []
source: "https://unit42.paloaltonetworks.com/kimwolf-v7-botnet-malware/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Learn:** Kimwolf v7's use of Ethereum Name Service for C2 resolution and Tor as a fallback is a novel evasion pattern worth incorporating into threat models for IoT/edge assets, but no patch or config change applies to typical cloud/AppSec environments.
- **SOC/IR — Plan:** The ENS-based C2 resolution and Tor backup routing introduce detection gaps in traditional domain-block and DNS monitoring approaches; plan detection coverage for anomalous Ethereum ENS lookups and unexpected Tor traffic from IoT segments this quarter.
- **Leader — Skip**
