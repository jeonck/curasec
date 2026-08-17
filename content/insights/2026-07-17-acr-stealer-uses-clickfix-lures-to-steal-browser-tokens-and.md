---
title: "ACR Stealer ClickFix Campaign Targets M365 Sessions and Browser Credentials"
date: 2026-07-17T12:06:10.948288+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["infostealer", "clickfix", "microsoft-365"]
cves: []
source: "https://thehackernews.com/2026/07/acr-stealer-uses-clickfix-lures-to.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Plan:** ClickFix is a social-engineering delivery vector, not a patchable vuln — review AppLocker/WDAC policies to restrict arbitrary Run-dialog execution, and audit M365 Conditional Access token-lifetime and revocation settings to limit stolen-session utility.
- **SOC/IR — Act:** Microsoft Defender Experts documented two active delivery chains; hunt for PowerShell or cmd.exe spawned via user-initiated Run dialog (explorer.exe lineage), and sweep M365 Unified Audit Log for anomalous OAuth grants, bulk file access, or SharePoint/OneDrive exfiltration events since the campaign is live.
- **Leader — Plan:** Session-token theft bypasses MFA and directly targets M365 documents — worth a leadership brief this quarter on lure-based infostealer risk, and a review of whether security-awareness training covers ClickFix-style social engineering.
