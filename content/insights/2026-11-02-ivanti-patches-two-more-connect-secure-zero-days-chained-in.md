---
title: "Ivanti Connect Secure zero-days chained in active attacks, patches released"
date: 2026-11-02T20:44:36.815553+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["ivanti", "zero-day", "remote-access"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/ivanti-patches-two-more-connect-secure-zero-days-chained-in-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Two chained zero-days in Ivanti Connect Secure have been actively exploited since at least October 1 — apply Ivanti's latest ICS patches immediately and treat any unpatched gateways as potentially compromised before patching.
- **SOC/IR — Act:** Active exploitation dating back to October 1 means assume-breach posture for any Ivanti ICS gateways in your estate — hunt for lateral movement or persistence established through the VPN edge since that date and review ICS authentication and session logs for anomalies.
- **Leader — Act:** Confirm this week whether your organization runs Ivanti Connect Secure and demand a patch status and exposure assessment from your engineering team; Ivanti ICS has a pattern of nation-state exploitation that is likely to trigger customer or board questions.
