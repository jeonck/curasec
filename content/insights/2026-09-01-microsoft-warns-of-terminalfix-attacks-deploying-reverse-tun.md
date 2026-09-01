---
title: "TerminalFix ClickFix variant lures users into running PowerShell via fake CAPTCHA"
date: 2026-09-01T15:28:52.066055+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["clickfix", "social-engineering", "powershell"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/microsoft-warns-of-terminalfix-attacks-deploying-reverse-tunnels/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** No patchable CVE — this is a user-execution social engineering chain. Evaluate whether your environment enforces PowerShell Constrained Language Mode or WDAC policies that would limit blast radius if a user runs attacker-supplied terminal commands.
- **SOC/IR — Plan:** Build or tune detections for PowerShell processes spawned from browser-related parent processes, and alert on known reverse-tunnel binaries (chisel, ngrok, etc.); the ClickFix TTP pattern is well-documented and Sigma rules exist to template from.
- **Leader — Learn:** Active campaign exploiting user behavior rather than software flaws; useful context for refreshing security awareness training around CAPTCHA-themed lures, but no board-level action is warranted without wider impact data.
