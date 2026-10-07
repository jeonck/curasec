---
title: "FBI: FortiBleed Credential Campaign Still Active, 86K+ Devices Hit"
date: 2026-10-07T17:48:59.708516+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["fortinet", "credential-harvesting", "vpn-security"]
cves: []
source: "https://thehackernews.com/2026/10/fbi-warns-fortibleed-remains-active.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** FBI/USSS joint advisory confirms active harvesting against internet-facing FortiGate and SSL VPN devices via reused credentials and legacy SHA-256 password storage. Immediately rotate all Fortinet admin and VPN credentials, disable SHA-256 legacy password configs, and enforce MFA on management interfaces.
- **SOC/IR — Act:** The campaign's scale and active status mean affected devices may already be compromised before patching. Sweep authentication logs for anomalous VPN logins and lateral movement since campaign onset; apply assume-breach posture for any internet-exposed FortiGate or SSL VPN in your estate.
- **Leader — Act:** A joint FBI/Secret Service advisory citing 86,000+ harvested credentials from widely-deployed network perimeter devices is board-question territory. Confirm whether Fortinet FortiGate or SSL VPN is in use, request an exposure assessment from the infrastructure team, and prepare a brief for leadership before they read this in the news.
