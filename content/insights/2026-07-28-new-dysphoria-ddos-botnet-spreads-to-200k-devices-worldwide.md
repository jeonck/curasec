---
title: "Dysphoria DDoS Botnet Compromises 200k Devices Globally"
date: 2026-07-28T13:01:43.287328+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["botnet", "ddos", "iot"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/new-dysphoria-ddos-botnet-spreads-to-200k-devices-worldwide/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** No KEV, PoC, or EPSS signal provided; no specific vulnerability or affected software named in the summary. Monitor for follow-up reporting with exploitation details or affected device types that may be in your estate.
- **SOC/IR — Plan:** A 200k-node botnet generating DDoS and relay traffic is worth building or tuning detections for — watch for follow-up IOC releases and prepare to hunt for anomalous outbound traffic patterns consistent with botnet C2 or relay behavior.
- **Leader — Learn:** Awareness-level item for now; if your organization relies on internet-facing services, DDoS resilience posture is worth a periodic review but this report lacks specifics that would require immediate leadership action.
