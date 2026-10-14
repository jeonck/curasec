---
title: "CISA KEV: Ivanti Connect Secure Auth Bypass CVE-2026-104935 Actively Exploited"
date: 2026-10-14T15:48:57.203933+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["ivanti", "vpn-appliance", "authentication-bypass"]
cves: ["CVE-2026-104935"]
source: "https://thehackernews.com/2026/10/cisa-urges-immediate-ivanti-connect.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** CVE-2026-104935 is CISA KEV-listed with a public GitHub PoC and confirmed honeypot exploitation — if you run Ivanti Connect Secure, patch to the latest version immediately and audit authentication logs for anomalous access patterns prior to patch deployment.
- **SOC/IR — Act:** Active exploitation of an edge VPN appliance warrants an assume-breach posture — hunt for anomalous authentication events on ICS gateways since disclosure, and sweep for lateral movement indicators originating from VPN-assigned IPs, particularly over the past week.
- **Leader — Act:** A CISA KEV-listed authentication bypass in a widely deployed enterprise VPN with confirmed active exploitation is a material risk event — confirm whether Ivanti Connect Secure is in your environment, verify patching is escalated to this week, and prepare a brief for leadership if it is deployed.
- **Signals:** CVE-2026-104935 — CISA KEV: listed, EPSS 0.26, public PoC on GitHub
