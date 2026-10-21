---
title: "Stolen UpdraftCentral keys used to backdoor WordPress sites"
date: 2026-10-21T15:56:43.831517+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["wordpress", "supply-chain", "credential-compromise"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/stolen-updraftcentral-keys-used-to-backdoor-wordpress-sites/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Active supply-chain compromise: stolen UpdraftCentral connection keys give attackers remote command execution over any connected WordPress site. Immediately rotate all UpdraftCentral connection keys and audit connected WordPress sites for unauthorized files, new admin accounts, or modified plugins.
- **SOC/IR — Act:** Sites connected to UpdraftCentral may already be backdoored; sweep WordPress environments for unexpected file changes, newly created admin accounts, or outbound C2 traffic since the TeamUpdraft breach, even without published IOCs.
- **Leader — Act:** A developer managing popular WordPress backup plugins was breached, with active backdooring of customer sites reported. Confirm this week whether any organizational WordPress properties use UpdraftCentral, and if so request an incident summary from TeamUpdraft to assess exposure.
