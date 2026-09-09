---
title: "Hackers deploy fileless Linux rootkit on F5 BIG-IP APM devices"
date: 2026-09-09T15:05:56.552281+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["f5-big-ip", "rootkit", "fileless-malware"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-breach-f5-big-ip-apm-devices-to-deploy-linux-rootkit/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Active breach campaign targeting F5 BIG-IP APM appliances — a common enterprise edge device. Audit your BIG-IP APM fleet for indicators of compromise: look for anomalous PHP interpreter activity, unexpected in-memory web shell behavior, and verify firmware/software versions against F5's latest advisories.
- **SOC/IR — Act:** The fileless, memory-resident web shell evades file-based detection, so standard endpoint scans will miss it. Hunt for anomalous PHP file-load interception and unusual outbound connections from F5 BIG-IP APM processes; if your org runs BIG-IP APM, treat as assume-breach and initiate a memory forensics sweep.
- **Leader — Plan:** Active compromise campaign against widely-deployed F5 BIG-IP APM appliances — confirm with your network/infra team whether your org runs these devices, verify that monitoring and patching processes are in place, and be prepared to brief leadership if exposure is confirmed.
