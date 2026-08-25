---
title: "Hotel Wi-Fi DNS hijacked to phish Microsoft 365 credentials"
date: 2026-07-25T12:08:50.257932+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["phishing", "dns-hijacking", "microsoft-365"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-hijack-hotel-wi-fi-dns-to-steal-microsoft-365-accounts/"
source_name: "BleepingComputer"
status: "archived"
---
- **Engineer — Plan:** Review whether corporate travel policy requires VPN enforcement on untrusted Wi-Fi; audit M365 tenant for conditional access policies that would block logins from non-compliant networks or flag impossible-travel anomalies.
- **SOC/IR — Act:** Hunt for M365 sign-ins from hotel/conference-center IP ranges or unexpected geolocations since this campaign began; tune Conditional Access or SIEM rules to flag credential use immediately after untrusted-network logins.
- **Leader — Learn:** A reminder that credential phishing via rogue DNS is an ongoing risk for traveling employees; no board-level action warranted without evidence of organizational impact, but useful context for travel security awareness programs.
