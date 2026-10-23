---
title: "Mass Campaign Breaches Fortinet and Palo Alto Edge Devices, 70k Creds Exposed"
date: 2026-10-23T15:44:28.729261+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["edge-devices", "vpn", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/10/hackers-breach-enterprise-firewalls-and.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** FortiGate and GlobalProtect are common enterprise fixtures; active access obtained at organizations worldwide means assume-breach posture is warranted now. Audit both platforms for unauthorized sessions or config changes, force credential rotation for all VPN users, and cross-reference your logs against any IOCs released by the researchers.
- **SOC/IR — Act:** This is a live campaign with confirmed access at multiple orgs — edge device compromise typically precedes patching, so run an assume-breach hunt now. Search SIEM for anomalous lateral movement sourced from your FortiGate or GlobalProtect IPs since at least early October, and monitor the researcher disclosure for IOC drops to build detection rules.
- **Leader — Act:** Seventy thousand exposed credentials across a worldwide enterprise campaign is a credible board-level event if your org runs either product. Confirm with engineering whether FortiGate or GlobalProtect is in scope, request a status report on credential exposure and any observed unauthorized access, and prepare a brief for leadership before this surfaces in mainstream press.
