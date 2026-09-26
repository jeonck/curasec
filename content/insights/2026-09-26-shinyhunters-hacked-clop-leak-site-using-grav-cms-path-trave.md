---
title: "ShinyHunters exploit Grav CMS path traversal to breach Clop leak site"
date: 2026-09-26T14:58:08.483782+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["grav-cms", "path-traversal", "shinyhunters"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/shinyhunters-hacked-clop-leak-site-using-grav-cms-path-traversal-flaw/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** An unauthenticated path traversal in Grav CMS was exploited in the wild — if you run Grav CMS on any public-facing server, audit your version and apply the latest patch immediately to close this pre-auth attack surface.
- **SOC/IR — Learn:** Confirms ShinyHunters actively weaponizes web CMS vulnerabilities, but the item provides no IOCs or ATT&CK-mappable TTPs applicable to enterprise defenses — useful actor context, no hunt action required.
- **Leader — Skip**
