---
title: "UNC6671 Vishing Campaign Targets SaaS Credentials at Financial Firms"
date: 2026-08-09T11:41:42.823801+00:00
verdict: "Act"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Act"
tags: ["vishing", "social-engineering", "saas-security"]
cves: []
source: "https://thehackernews.com/2026/08/unc6671-vishing-attacks-target-personal.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** UNC6671 exploits human trust rather than software vulnerabilities, so there is no patch or config fix. The campaign reinforces the value of phishing-resistant (FIDO2) MFA on SaaS to limit what a tricked employee can surrender.
- **SOC/IR — Plan:** Named actor with defined TTPs (IT help-desk impersonation via personal phone → SaaS credential handover) but no IOCs published yet; build or tune detections for anomalous SaaS logins and new device enrollments, and consider hunting for suspicious authentication spikes in M365 or Google Workspace logs correlated with help-desk ticket activity.
- **Leader — Act:** An active data extortion group is deliberately targeting employees at financial services, private equity, and professional services firms by phone; if your org is in those sectors, brief employees this week on the IT impersonation lure and verify that help-desk identity-verification procedures are documented and enforced.
