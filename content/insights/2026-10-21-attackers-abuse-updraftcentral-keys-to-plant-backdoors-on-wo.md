---
title: "Stolen UpdraftCentral Keys Used to Backdoor WordPress Sites"
date: 2026-10-21T15:56:43.831517+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["wordpress", "supply-chain", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/10/attackers-abuse-updraftcentral-keys-to.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** TeamUpdraft's own website was breached and customer connection keys were exfiltrated; if you use UpdraftCentral, UpdraftVault, or UpdraftClone, rotate all connection keys immediately and audit WordPress file systems for newly planted backdoors or unexpected PHP files.
- **SOC/IR — Act:** Active backdoor-planting campaign is underway against WordPress sites with UpdraftCentral credentials; sweep managed WordPress estates for unauthorized file writes or new PHP scripts in plugin/theme directories since the breach disclosure, and prioritize sites confirmed to use UpdraftCentral products.
- **Leader — Act:** A confirmed vendor breach at TeamUpdraft has cascaded into active compromises of customer WordPress sites — if your organization operates WordPress with any Updraft-branded remote management products, request an exposure statement from TeamUpdraft and verify no backdoors were introduced on company properties before this week.
