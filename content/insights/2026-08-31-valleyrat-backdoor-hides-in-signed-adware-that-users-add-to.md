---
title: "ValleyRAT Backdoor Delivered via Signed Adware Abusing AV Exclusions"
date: 2026-08-31T18:00:29.794564+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["valleyrat", "malware", "evasion"]
cves: []
source: "https://thehackernews.com/2026/08/valleyrat-backdoor-hides-in-signed.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Silver Fox's technique of bundling a backdoor inside a legitimately-signed application and relying on user-added AV exclusions to stay resident is a design reminder to enforce allowlisting policies and audit AV exclusion lists across managed endpoints, but no direct cloud/app patch action follows from this report.
- **SOC/IR — Plan:** The evasion pattern — malware sheltered under a trusted signed process in a user-granted AV exclusion — is worth building a detection for: create or tune rules to alert on AV exclusion additions for unusual signed binaries and look for ValleyRAT IOCs once Kaspersky publishes them; no IOCs are available in this report to sweep against today.
- **Leader — Learn:** Silver Fox's use of signed software to bypass endpoint controls illustrates how attacker-signed supply-chain lures undermine trust models; useful context for future board discussions on endpoint policy, but no same-week leadership action is warranted given no confirmed enterprise-sector targeting or widely-used vendor exposure.
