---
title: "Compromised ConnectWise Credential Used to Access 173 M365 Tenants"
date: 2026-10-17T14:12:31.177036+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["m365", "supply-chain", "msp"]
cves: []
source: "https://thehackernews.com/2026/10/hackers-use-compromised-connectwise.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** If your org or your MSP uses ConnectWise Cloud Backup (formerly SkyKick), audit M365 unified audit logs and sign-in logs immediately for delegated-access activity from ConnectWise service accounts, and review/revoke any delegated admin permissions granted to ConnectWise.
- **SOC/IR — Act:** Active campaign accessing M365 tenants via compromised MSP tool credentials — hunt M365 sign-in logs for authentication events tied to ConnectWise Cloud Backup service principals or delegated admin access since this campaign began, and alert on anomalous third-party delegated logins.
- **Leader — Act:** If your organization uses an MSP that relies on ConnectWise Cloud Backup, confirm your exposure this week by requesting an attestation from that vendor; 173 confirmed tenant compromises via a single supply-chain credential is a board-question-level supply chain trust event.
