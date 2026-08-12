---
title: "Sandworm targets IT pros with trojanized WireGuard via fake job offers"
date: 2026-08-12T11:57:00.937865+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["apt", "supply-chain", "social-engineering"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/sandworm-hackers-target-it-pros-with-trojanized-wireguard-vpn-client/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Sandworm is delivering trojanized WireGuard VPN installers through fake recruitment outreach targeting sysadmins — people with elevated access like yours are the intended victims. Verify all VPN client installs trace to official sources, and alert IT staff to treat unsolicited job offers that include software downloads as high-risk.
- **SOC/IR — Act:** An active Sandworm campaign has been running since at least May against high-privilege IT users using trojanized VPN software as the payload delivery mechanism. Hunt for anomalous WireGuard process behavior and unexpected software installations by IT/admin accounts; map activity to T1195/T1566 and extend your Sandworm TTP coverage in your SIEM from May onward.
- **Leader — Plan:** Russian GRU-linked Sandworm is specifically targeting sysadmins and IT professionals — the people with the highest internal access — via fake job offers this quarter. Brief IT leadership on the campaign and confirm your acceptable-use policies cover software install restrictions and vetting of recruitment-related communications.
