---
title: "Microsoft warns of surge in ACR Stealer attacks on customers"
date: 2026-07-19T12:05:51.752202+00:00
verdict: "Act"
verdict_engineer: "Learn"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["infostealer", "credential-theft", "endpoint"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/microsoft-warns-of-surge-in-acr-stealer-attacks-on-customers/"
source_name: "BleepingComputer"
status: "archived"
---
- **Engineer — Learn:** ACR Stealer targets browser-stored credentials and tokens — review whether your CI/CD pipelines or developer workstations enforce short-lived tokens and MFA to limit blast radius if credentials are harvested.
- **SOC/IR — Act:** Microsoft is actively observing this campaign; hunt for ACR Stealer IOCs across EDR telemetry and SIEM, and tune detections for credential-access behaviors (browser credential dumping, token theft) across enterprise endpoints.
- **Leader — Plan:** A confirmed surge targeting enterprise customers elevates infostealer risk on your risk register; consider briefing on phishing-resistant MFA adoption and reviewing credential hygiene posture this quarter.
