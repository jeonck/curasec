---
title: "PHP2Shell + Kernel Privesc Used to Root 25 Servers Including US Gov Network"
date: 2026-10-28T17:09:30.637292+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["php-exploitation", "china-nexus", "privilege-escalation"]
cves: []
source: "https://thehackernews.com/2026/10/php2shell-attack-roots-25-servers.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Active nation-state exploitation of PHP2Shell combined with a kernel privilege escalation chain is confirmed as of Oct 25; audit all internet-exposed PHP applications for signs of compromise and track vendor advisories for a specific CVE and patch version.
- **SOC/IR — Act:** China-nexus actor ran an active campaign on Oct 25 combining PHP webshell deployment with kernel priv-esc — hunt for anomalous PHP process trees, unexpected kernel exploits, and new root-level persistence in web server logs since that date.
- **Leader — Learn:** A suspected China-nexus threat actor used AI-assisted techniques to breach a US government-affiliated network; useful context for board discussions on AI-enabled adversary tradecraft, but no immediate leadership action required unless your organization has direct government or defense-sector exposure.
