---
title: "Citrix warns of two NetScaler Gateway and ADC vulnerabilities"
date: 2026-08-21T11:38:25.806134+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["netscaler", "edge-appliances", "patch"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/citrix-urges-admins-to-patch-new-netscaler-flaws-as-soon-as-possible/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** NetScaler Gateway and ADC are widely deployed edge appliances with a strong exploitation history; apply Citrix's patches within your next maintenance window and verify no unpatched instances are internet-facing. No KEV listing or public PoC present to justify emergency patching, but Citrix's urgency language warrants prioritizing this over routine patching cycles.
- **SOC/IR — Learn:** No active exploitation, IOCs, or TTPs reported yet; file this as context in case exploitation emerges, given NetScaler's track record as a high-value target. Monitor threat intel feeds for follow-on exploitation reports before building detections.
- **Leader — Skip**
