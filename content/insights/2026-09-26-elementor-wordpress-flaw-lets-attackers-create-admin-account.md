---
title: "Elementor CSRF flaw enables unauthenticated admin account creation"
date: 2026-09-26T14:58:08.483782+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["wordpress", "csrf", "privilege-escalation"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/elementor-wordpress-flaw-lets-attackers-create-admin-accounts/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Update Elementor to the patched version immediately if you run WordPress sites using this plugin; no public PoC or KEV listing yet, but admin account creation via CSRF is a critical-severity class of flaw worth prioritizing this week.
- **SOC/IR — Learn:** No active exploitation or IOCs reported; file the CSRF-to-admin-creation TTP for future WordPress-focused detection work, but no hunt or rule tuning warranted now.
- **Leader — Skip**
