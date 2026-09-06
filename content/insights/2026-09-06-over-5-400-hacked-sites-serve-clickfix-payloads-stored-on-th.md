---
title: "5,400 Hacked Sites Deliver ClickFix Payloads via Blockchain Smart Contracts"
date: 2026-09-06T14:08:28.650854+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["clickfix", "supply-chain", "malware-campaign"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/over-5-400-hacked-sites-serve-clickfix-payloads-stored-on-the-blockchain/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If you manage any public-facing web properties, audit them for injected ClickFix loader scripts; the blockchain storage makes payload URLs resilient to takedown, so perimeter blocklists alone won't suffice.
- **SOC/IR — Act:** Active campaign at scale — tune detections for ClickFix behavior patterns: browser-spawned mshta or PowerShell, clipboard-manipulation sequences, and outbound calls to BNB Chain RPC endpoints from endpoints since this campaign began.
- **Leader — Learn:** The use of blockchain smart contracts as an abuse-resistant payload store is a meaningful evasion evolution worth noting; no immediate leadership action needed unless an internal investigation reveals your web presence among the 5,400 compromised sites.
