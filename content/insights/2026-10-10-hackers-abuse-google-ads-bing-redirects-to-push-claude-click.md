---
title: "Malvertising campaign uses Bing redirects in Google Ads to push fake Claude ClickFix"
date: 2026-10-10T16:14:00.225657+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["clickfix", "malvertising", "social-engineering"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-abuse-google-ads-bing-redirects-to-push-claude-clickfix-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** ClickFix via AI-tool search ads is a growing supply-chain entry point for endpoints; no patch needed, but reinforce approved-software-only policies and consider blocking known malicious installer domains once IOCs are published.
- **SOC/IR — Plan:** ClickFix attacks produce detectable behavior — PowerShell or mshta spawned from browser or fake-installer processes; build or tune Sigma/EDR rules for that parent-child chain to catch this and future ClickFix campaigns without waiting for campaign-specific IOCs.
- **Leader — Learn:** Malvertising targeting popular AI-tool searches is a rising awareness gap; useful context for refreshing user guidance on approved software procurement, but no immediate board-level or vendor-exposure action required.
