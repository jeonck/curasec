---
title: "FTP banner abuse used to deliver new Windows RATs E4del and PINHOLE"
date: 2026-08-21T11:38:25.806134+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["malware", "ftp", "windows"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-abuse-ftp-server-banners-to-deliver-new-windows-malware/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** Novel delivery technique hiding commands inside FTP server banners is worth understanding for FTP-exposed environments, but no KEV/PoC/EPSS signals exist to force immediate action — review whether any internal FTP services expose banners to untrusted clients.
- **SOC/IR — Plan:** Two undocumented RATs with an unusual delivery vector warrant new detection logic; build rules to flag anomalous FTP banner content and hunt for E4del/PINHOLE behavioral patterns (process spawning from FTP client sessions) once IOCs are published.
- **Leader — Skip**
