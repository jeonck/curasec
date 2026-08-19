---
title: "Clop custom Java web shell targets PTC Windchill and FlexPLM servers"
date: 2026-08-19T11:36:35.301683+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["clop", "web-shell", "plm"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/clop-created-custom-web-shell-for-windchill-data-theft-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** If you run PTC Windchill or FlexPLM, audit those servers for this Java web shell immediately — it is purpose-built to decrypt stored credentials and exfiltrate file repositories. Pull IOCs from the BleepingComputer article and sweep web-accessible directories on those hosts.
- **SOC/IR — Act:** Clop's use of a bespoke web shell against Windchill/FlexPLM indicates an active, ongoing campaign with credential theft as a precursor step; hunt for anomalous Java process activity and unauthorized file enumeration on any PLM servers in your estate, and ingest the published IOCs into your SIEM.
- **Leader — Plan:** Clop is expanding its toolset to target PLM systems common in manufacturing and engineering sectors — verify whether Windchill or FlexPLM appears in your environment or third-party supply chain, and direct your security team to audit those systems this quarter.
