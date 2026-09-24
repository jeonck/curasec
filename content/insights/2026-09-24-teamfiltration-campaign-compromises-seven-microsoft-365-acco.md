---
title: "TeamFiltration Sprays M365 Tenants via Default Passwords, 7 Accounts Compromised"
date: 2026-09-24T15:49:46.689252+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["credential-spraying", "microsoft-365", "cloud-identity"]
cves: []
source: "https://thehackernews.com/2026/09/teamfiltration-compromises-seven.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** TeamFiltration targets M365 tenants using default/weak credentials; audit your tenant for accounts lacking MFA and enforce Conditional Access policies requiring phishing-resistant auth before this campaign broadens its target geography.
- **SOC/IR — Act:** Active M365 credential-spray campaign is live and compromising accounts; hunt for TeamFiltration enumeration patterns in Azure AD sign-in logs and flag clusters of authentication attempts originating from AWS EC2 CIDR ranges with mixed failure/success ratios.
- **Leader — Learn:** Seven-account compromise across 28 tenants is low scale and currently regional (Chilean retail/finance), but the default-password attack path is a useful data point for board-level conversations about basic credential hygiene and MFA adoption metrics.
