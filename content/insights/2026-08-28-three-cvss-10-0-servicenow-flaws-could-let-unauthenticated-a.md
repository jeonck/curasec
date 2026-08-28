---
title: "ServiceNow Patches Three CVSS 10.0 Flaws Allowing Unauth RCE and SQLi"
date: 2026-08-28T21:21:40.237236+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Plan"
tags: ["servicenow", "rce", "critical-vulnerability"]
cves: []
source: "https://thehackernews.com/2026/08/three-cvss-100-servicenow-flaws-could.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Three unauthenticated RCE/SQLi flaws at maximum severity demand prompt action, but no KEV listing or public PoC elevates this to Act yet. If running self-hosted ServiceNow, apply the patch this week and verify hosted instances received the automated update.
- **SOC/IR — Skip**
- **Leader — Plan:** Three CVSS 10.0 flaws in a widely deployed ITSM platform warrant confirming whether your organization runs self-hosted ServiceNow and ensuring the patch was applied; hosted tenants should receive confirmation from ServiceNow that their instances were updated.
