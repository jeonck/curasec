---
title: "ClickLock macOS Stealer Uses App-Kill Loop to Force Password Entry"
date: 2026-07-17T12:06:10.948288+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["macos", "infostealer", "clickfix"]
cves: []
source: "https://thehackernews.com/2026/07/new-clicklock-macos-stealer-kills-apps.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Learn:** No CVE to patch — this is a social-engineering delivery chain (ClickFix-style Terminal paste) that installs LaunchAgent persistence. Engineers with macOS fleets should understand the vector and consider restricting user ability to run arbitrary Terminal commands via MDM policy.
- **SOC/IR — Plan:** The two-stage behavior — LaunchAgent installation on cancel, then aggressive app-kill loop at next login — is detectable; build or tune rules for unexpected LaunchAgent creation from Terminal sessions and rapid repeated app-termination events on macOS endpoints.
- **Leader — Skip**
