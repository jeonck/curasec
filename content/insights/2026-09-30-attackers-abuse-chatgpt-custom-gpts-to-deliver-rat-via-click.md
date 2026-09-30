---
title: "ChatGPT Custom GPTs Weaponized to Deliver RAT via ClickFix Lures"
date: 2026-09-30T16:48:49.184501+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["clickfix", "ai-abuse", "rat-delivery"]
cves: []
source: "https://thehackernews.com/2026/09/attackers-abuse-chatgpt-custom-gpts-to.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No patch surface here — this is a social-engineering chain exploiting user trust in AI platforms. Worth reviewing whether your org restricts or monitors ChatGPT Custom GPT usage, and factoring this lure vector into developer security-awareness training.
- **SOC/IR — Plan:** ClickFix attacks have a detectable pattern — clipboard-paste triggered PowerShell or command execution — worth tuning EDR and SIEM rules for this behavior; also build detections for RAT C2 beaconing from workstations that recently ran clipboard-sourced commands.
- **Leader — Learn:** Illustrates that enterprise AI platform usage (ChatGPT Custom GPTs) is becoming a malware distribution vector; useful input when reviewing AI tool usage policies, but no immediate board-level action is warranted without specific IOCs or sector targeting.
