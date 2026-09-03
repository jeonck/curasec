---
title: "DOUBLECUP LaaS Uses ClickFix and PNG Steganography to Drop RAT"
date: 2026-08-04T13:07:50.076253+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["clickfix", "malware-loader", "steganography"]
cves: []
source: "https://thehackernews.com/2026/08/doublecup-uses-clickfix-and-cached-pngs.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Learn:** Novel multi-stage delivery abusing browser cache for steganographic PNG staging is worth understanding when evaluating endpoint controls and browser security policies, but no patch or configuration change is required today.
- **SOC/IR — Plan:** Build or tune detections for ClickFix PowerShell execution patterns and anomalous PNG writes to browser cache directories; the CountLoader → DeviceManager RAT chain provides new TTPs to add to hunt playbooks this quarter.
- **Leader — Skip**
