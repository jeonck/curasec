---
title: "ShinyHunters breaches Clop ransomware leak site, steals server data"
date: 2026-09-19T14:22:25.332089+00:00
verdict: "Learn"
verdict_engineer: "Skip"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["ransomware", "threat-actor", "extortion"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Skip**
- **SOC/IR — Learn:** Intra-criminal conflict between ShinyHunters and Clop has no immediate detection action, but the potential leak of Clop's onion private keys and server data could expose victim data or Clop TTPs — monitor for any published data that surfaces IOCs or infrastructure details.
- **Leader — Learn:** If your organization was previously extorted by Clop, stolen server data could resurface victim information — monitor threat intel for any published Clop victim data and brief legal if your org is among known prior targets.
