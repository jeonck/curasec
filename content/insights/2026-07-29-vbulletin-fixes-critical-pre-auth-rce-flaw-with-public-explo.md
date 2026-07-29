---
title: "vBulletin critical pre-auth RCE flaw has public exploit"
date: 2026-07-29T13:07:14.832066+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Skip"
tags: ["rce", "vbulletin", "public-exploit"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/vbulletin-fixes-critical-pre-auth-rce-flaw-with-public-exploit/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Pre-auth RCE with a public exploit in vBulletin's template renderer is actively exploitable right now — patch vBulletin to the vendor-released fixed version immediately if you run any internet-facing vBulletin instance.
- **SOC/IR — Act:** A public exploit for pre-auth PHP code execution means exploitation is likely in progress — sweep vBulletin access logs for anomalous template-rendering requests and hunt for web shells or unexpected PHP processes on any vBulletin host since the disclosure date.
- **Leader — Skip**
