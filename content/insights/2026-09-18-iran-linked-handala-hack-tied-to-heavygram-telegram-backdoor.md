---
title: "Iran-Linked Handala Hack Group Deploys HEAVYGRAM Telegram Backdoor"
date: 2026-09-18T14:58:07.079452+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["threat-actor", "backdoor", "nation-state"]
cves: []
source: "https://thehackernews.com/2026/09/iran-linked-handala-hack-tied-to.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** HEAVYGRAM's DLL sideloading and Telegram session file exfiltration techniques are worth factoring into threat models for environments where Telegram is used and where DLL loading paths are not locked down, but no patch or configuration action is indicated with zero exploitation signals.
- **SOC/IR — Learn:** The TTP set — remote command execution, screenshot capture, DLL sideloading, and Telegram session theft — maps roughly to ATT&CK T1574/T1113/T1552, but no IOCs are published here and targeting appears geopolitically scoped, so no immediate hunt is warranted; worth cataloguing for future detection logic around Telegram credential theft.
- **Leader — Skip**
