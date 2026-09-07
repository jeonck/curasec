---
title: "Rogue ScreenConnect Clients Spread Four-Stage VBScript Worm to New Hosts"
date: 2026-09-07T16:27:04.378719+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["screenconnect", "rmm-abuse", "vbscript-malware"]
cves: []
source: "https://thehackernews.com/2026/09/rogue-screenconnect-clients-spread-four.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Three confirmed incidents show worm-like spread via ScreenConnect to newly connected hosts — if you run ScreenConnect, audit your relay configuration for unauthorized clients and review logs for unexpected new-host onboarding activity since the worm spreads automatically on connection.
- **SOC/IR — Act:** Hunt for VBScript execution chains spawned from ScreenConnect parent processes across your estate, and sweep RMM logs for abnormal new-client connection events; initial access spans tech-support scam lures, phishing MSIs, and at least one other vector, so assume diverse entry points.
- **Leader — Plan:** RMM tool abuse as a worm vector is a growing pattern — use this quarter to review governance of ScreenConnect and similar remote-access tools (access restrictions, audit logging, approved-relay allowlists) before an incident forces the conversation.
