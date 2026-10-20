---
title: "Rank Math PRO WordPress Plugin Backdoored via Official Site"
date: 2026-10-20T15:39:31.280324+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["supply-chain", "wordpress", "backdoor"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/wordpress-seo-plugin-rank-math-compromised-to-backdoor-websites/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Official-channel supply-chain compromise means any Rank Math PRO install fetched last week may carry a backdoor; immediately audit all WordPress sites for the plugin's presence, remove or replace with a verified clean version, and inspect for indicators of hidden backdoor files or unauthorized admin accounts.
- **SOC/IR — Plan:** No IOCs or TTPs are published yet, blocking immediate hunting; plan to draft WordPress-focused detection rules (anomalous plugin file writes, unexpected admin account creation) and queue a sweep of WordPress estates as soon as vendor or community publishes specific file hashes or behavioral indicators.
- **Leader — Plan:** Confirm with web and platform teams whether any company-owned WordPress properties run Rank Math PRO, and request a clean-bill attestation or removal; if third-party vendors host affected sites on your behalf, initiate vendor risk follow-up this week.
