---
title: "UAC-0145 (Sandworm) Uses ClickFix CAPTCHAs to Deliver Info-Stealer"
date: 2026-07-20T13:16:24.819582+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["apt", "social-engineering", "sandworm"]
cves: []
source: "https://thehackernews.com/2026/07/uac-0145-uses-clickfix-captchas-to.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** ClickFix is a social-engineering technique, not a software vulnerability — no patch or config change applies. Understand the attack pattern (fake CAPTCHA prompts users to paste and run malicious commands) to inform user-awareness training and browser hardening policies.
- **SOC/IR — Plan:** ClickFix produces detectable behavioral patterns — browser processes spawning cmd.exe or PowerShell, clipboard-sourced command execution — worth building or tuning detections for this quarter; no specific IOCs were published to support an immediate hunt.
- **Leader — Learn:** Sandworm/GRU campaign currently focused on Ukrainian targets, making direct exposure unlikely for most US enterprises; useful situational awareness about adversary tradecraft evolution, but no immediate leadership action required.
