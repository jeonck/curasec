---
title: "AOMEI Backupper Update Servers Tampered to Deliver Backdoor"
date: 2026-10-17T14:12:31.177036+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "backdoor", "windows"]
cves: []
source: "https://thehackernews.com/2026/10/attackers-tampered-with-aomei.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Supply-chain compromise of a popular Windows backup utility's update mechanism meets Act criteria regardless of KEV listing — corroborated by Google TIG and Mandiant. Audit all systems running AOMEI Backupper for backdoor IOCs and check whether any update checks occurred during May–July 2026 attack windows.
- **SOC/IR — Act:** Confirmed backdoor delivery via tampered update server with Mandiant and Google TIG involvement implies IOCs are available or imminent. Hunt for suspicious processes or persistence artifacts on hosts with AOMEI Backupper installed that were active May–July 2026, and watch for published IOC sets from these investigations.
- **Leader — Act:** A supply-chain backdoor in widely deployed backup software investigated by Mandiant and Google TIG is board-question territory. Confirm whether AOMEI Backupper is present in your environment, scope which systems may have updated during the attack window, and prepare a brief before this surfaces in mainstream news.
