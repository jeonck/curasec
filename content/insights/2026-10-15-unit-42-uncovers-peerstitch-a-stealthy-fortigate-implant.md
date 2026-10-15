---
title: "Unit 42: PEERSTITCH Memory Implant Deployed via FortiManager CVE-2024-47575"
date: 2026-10-15T15:35:13.586755+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["fortigate", "memory-implant", "cve-2024-47575"]
cves: ["CVE-2024-47575"]
source: "https://unit42.paloaltonetworks.com/fortimanager-cve-2024-47575-peerstitch-malware/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Act:** CVE-2024-47575 is KEV-listed with EPSS 0.95 and a public PoC; patch FortiManager immediately to the vendor-fixed release, then audit FortiGate devices for PEERSTITCH IOCs published in the Unit 42 report.
- **SOC/IR — Act:** Memory-resident implant on a network edge device means assume-breach posture: sweep firewall estate for PEERSTITCH IOCs from the Unit 42 post, hunt for post-exploitation lateral movement originating from FortiGate/FortiManager hosts since the CVE disclosure window (late 2024 onward).
- **Leader — Act:** Over 500 firewalls were compromised in this campaign; confirm whether your organization runs FortiManager, assess whether you fall within the affected population, and brief leadership before this surfaces in mainstream news — board questions are likely given the scale.
- **Signals:** CVE-2024-47575 — CISA KEV: listed, EPSS 0.95, public PoC on GitHub
