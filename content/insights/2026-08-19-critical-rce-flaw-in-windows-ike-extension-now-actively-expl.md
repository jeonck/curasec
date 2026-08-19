---
title: "Critical RCE flaw in Windows IKE Extension now actively exploited"
date: 2026-08-19T11:36:35.301683+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["windows", "rce", "active-exploitation"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/cisa-critical-windows-ike-extension-flaw-now-exploited-in-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** CISA confirmed active exploitation of this critical Windows IKE RCE — patch all Windows systems running IPsec/VPN services immediately; treat as emergency patch given KEV-level signal from CISA warning.
- **SOC/IR — Act:** Active exploitation confirmed by CISA — hunt for anomalous IKE/IPsec traffic and suspicious activity originating from VPN-adjacent or edge Windows systems since the campaign began; assume-breach sweep warranted for internet-exposed IKE endpoints.
- **Leader — Plan:** Confirm with infrastructure teams that Windows IPsec/VPN systems are prioritized in the current patch cycle; active exploitation elevates this above routine cadence but it falls short of board-level disclosure unless a breach is discovered.
