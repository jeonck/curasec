---
title: "Lunex Stealer Uses AMD Driver BYOVD to Disable EDR and Steal Browser Creds"
date: 2026-09-27T15:38:27.651895+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["byovd", "credential-theft", "clickfix-lure"]
cves: []
source: "https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** The BYOVD technique abusing a legitimate AMD driver to blind security tooling is worth noting for driver allowlist/blocklist hardening, but no KEV, PoC, or broad enterprise targeting signal means no immediate patching action is required.
- **SOC/IR — Plan:** The four-stage chain—fake CAPTCHA ClickFix lure → PowerShell execution → vulnerable driver sideload → credential harvest—offers multiple detection opportunities; build or tune rules for ClickFix-style CAPTCHA-triggered script execution and for anomalous signed-driver loads that precede EDR tampering events.
- **Leader — Skip**
