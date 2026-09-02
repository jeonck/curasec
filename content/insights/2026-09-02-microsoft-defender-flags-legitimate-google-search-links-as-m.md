---
title: "Microsoft Defender for Office 365 false-positives block Google links"
date: 2026-09-02T15:05:08.783541+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["false-positive", "email-security", "defender"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/microsoft-defender-flags-legitimate-google-search-links-as-malicious/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If your org uses Defender for Office 365, check whether Safe Links is blocking legitimate Google URLs and configure allow-list exceptions or monitor Microsoft's investigation for a fix.
- **SOC/IR — Plan:** Expect a spike in user-reported blocked links; tune alert triage to deprioritize Safe Links hits on google.com domains until Microsoft issues a resolution.
- **Leader — Skip**
