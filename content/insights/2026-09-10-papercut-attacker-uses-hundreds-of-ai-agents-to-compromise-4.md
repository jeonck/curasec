---
title: "Russian Actor Uses AI Agents to Compromise 440+ PaperCut Instances"
date: 2026-09-10T14:58:06.811051+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["papercut", "active-exploitation", "ai-assisted-attack"]
cves: []
source: "https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active exploitation of recently disclosed PaperCut NG/MF flaws at scale — patch PaperCut to the latest version immediately and audit instances for IOC 45.142.193[.]132 in access logs.
- **SOC/IR — Act:** Multi-source-corroborated (Blackpoint Cyber + GreyNoise) campaign with a concrete IOC: sweep for 45.142.193[.]132 across network and proxy logs, and run an assume-breach hunt on any PaperCut NG/MF hosts in your estate.
- **Leader — Act:** 440+ compromised PaperCut instances attributed to a Russian-speaking actor is board-relevant scale — confirm whether PaperCut NG/MF is in your environment and verify patching status before this surfaces in news cycles.
