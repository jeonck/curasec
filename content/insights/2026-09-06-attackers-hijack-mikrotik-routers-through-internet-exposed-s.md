---
title: "Attackers Hijack MikroTik Routers via Unauthenticated SSH"
date: 2026-09-06T14:08:28.650854+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["mikrotik", "edge-device", "active-exploitation"]
cves: []
source: "https://thehackernews.com/2026/09/attackers-hijack-mikrotik-routers.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active exploitation of internet-exposed MikroTik SSH granting full admin access is confirmed by CERT Polska; immediately audit all MikroTik devices for internet-reachable SSH, restrict SSH to management-only networks, and review recent device configurations for unauthorized changes since September 2.
- **SOC/IR — Act:** Edge device full-takeover with confirmed active exploitation since at least September 2 is an assume-breach signal; sweep MikroTik routers for unauthorized admin sessions and configuration changes, and check for anomalous outbound traffic from these devices as a lateral-movement indicator.
- **Leader — Plan:** MikroTik is common in SMB and branch-office environments; direct the security team to inventory internet-facing MikroTik SSH exposure and confirm whether any devices were reachable since September 2 — not yet a systemic board-level event but escalate if exposure is confirmed.
