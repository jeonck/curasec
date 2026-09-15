---
title: "Telegram Desktop HTML Export Feature Enables Stored JS Injection"
date: 2026-09-15T15:32:56.195900+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["telegram", "javascript-injection", "data-exfiltration"]
cves: []
source: "https://thehackernews.com/2026/09/telegram-desktop-flaw-lets-hidden.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** If Telegram Desktop is used in your environment for work communications, advise users to stop using the HTML chat export feature until Telegram ships a fix; no patch version cited and no KEV/PoC, but the attack chain (malicious bot message → export → browser open) is realistic enough to warrant a policy change this quarter.
- **SOC/IR — Learn:** Novel stored-JS-in-export technique is worth understanding for threat modeling chat-app abuse, but no IOCs, no ATT&CK mapping, and no evidence of active exploitation means there is no detection or hunt work to act on now.
- **Leader — Skip**
