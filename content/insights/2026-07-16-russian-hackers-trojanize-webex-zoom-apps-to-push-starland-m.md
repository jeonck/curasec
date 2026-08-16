---
title: "Russian UAT-11795 trojanizes WebEx/Zoom apps to deploy Starland RAT"
date: 2026-07-16T12:18:39.346883+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["trojanized-software", "credential-theft", "threat-actor"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/russian-hackers-trojanize-webex-zoom-apps-to-push-starland-malware/"
source_name: "BleepingComputer"
status: "archived"
---
- **Engineer — Plan:** Trojanized installers for widely-deployed conferencing tools represent a real supply-chain-adjacent risk; no exploitation signals provided. Audit all WebEx/Zoom deployments to confirm they originate from official signed packages or MDM-managed distribution, and block unapproved installer sources.
- **SOC/IR — Act:** Active campaign using trojanized enterprise conferencing apps to drop a credential-stealing RAT; hunt for unsigned or anomalous WebEx/Zoom process trees since the compromise starts before any patch can help. Pull Starland RAT IOCs from the BleepingComputer article and sweep endpoint logs for suspicious child processes or C2 traffic from conferencing app directories.
- **Leader — Learn:** Financially motivated Russian actor targeting enterprise collaboration tools is worth noting as sector-level context, but with no confirmed breach at a shared vendor and no enrichment signals, this does not yet require leadership action or customer communication.
