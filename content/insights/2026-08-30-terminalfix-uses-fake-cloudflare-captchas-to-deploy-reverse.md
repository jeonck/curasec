---
title: "TerminalFix ClickFix Variant Uses Fake CAPTCHAs to Run PowerShell Backdoor"
date: 2026-08-30T15:19:58.098687+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["clickfix", "social-engineering", "powershell"]
cves: []
source: "https://thehackernews.com/2026/08/terminalfix-uses-fake-cloudflare.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Novel ClickFix variant redirecting victims to Windows Terminal/PowerShell rather than the Run dialog increases execution success for complex payloads; no patch applies, but this is a good prompt to verify PowerShell Script Block Logging and AMSI are enabled and that AppLocker/WDAC policies restrict terminal abuse.
- **SOC/IR — Plan:** Build or tune detections for browser or web-content processes spawning Windows Terminal/PowerShell children that then launch reverse-tunnel tooling; also baseline and alert on known tunnel binaries (ngrok, frp, chisel) appearing post-user-session, since no IOCs are published yet to support an immediate hunt.
- **Leader — Learn:** Awareness of this technique evolution is useful background for refreshing phishing/social-engineering guidance in security awareness programs, but it does not require a leadership statement or risk-register update at this time.
