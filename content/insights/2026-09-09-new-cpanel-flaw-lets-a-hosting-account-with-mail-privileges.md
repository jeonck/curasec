---
title: "cPanel EmailTrack flaw allows hosting account to gain root code execution"
date: 2026-09-09T15:05:56.552281+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["cpanel", "privilege-escalation", "web-hosting"]
cves: []
source: "https://thehackernews.com/2026/09/new-cpanel-flaw-lets-hosting-account.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Every supported cPanel and WHM version is affected; a mail-privileged hosting account can write arbitrary files and escalate to root via EmailTrack. Patch to the latest cPanel/WHM release (advisory published Sep 8) within your next patch window — no PoC or active exploitation is confirmed yet, but root-level impact makes this high priority.
- **SOC/IR — Skip**
- **Leader — Skip**
