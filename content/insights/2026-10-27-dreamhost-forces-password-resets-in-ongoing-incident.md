---
title: "DreamHost forces FTP/SFTP/email password resets amid ongoing incident"
date: 2026-10-27T16:34:51.683639+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Plan"
tags: ["credential-reset", "web-hosting", "vendor-incident"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/dreamhost-forces-email-ftp-sftp-password-resets-in-ongoing-incident/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If your org hosts anything on DreamHost, verify the forced credential resets completed for all FTP/SFTP and email accounts and review access logs since the incident began for any unauthorized file access.
- **SOC/IR — Skip**
- **Leader — Plan:** Confirm whether your organization uses DreamHost for any hosting services; if so, request an incident scope update from them and verify all affected credentials have been rotated by impacted teams.
