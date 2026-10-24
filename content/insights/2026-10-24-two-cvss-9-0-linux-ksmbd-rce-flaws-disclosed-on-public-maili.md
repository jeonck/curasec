---
title: "Two CVSS 9.0 Pre-Patch KSMBD RCE Flaws Disclosed Publicly"
date: 2026-10-24T14:29:02.695753+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["linux", "ksmbd", "rce"]
cves: []
source: "https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A pre-authentication RCE (ZDI-CAN-33774) in the Linux kernel's built-in SMB server is publicly disclosed with no mainline fix yet. Audit all Linux servers for ksmbd running (`lsmod | grep ksmbd`), disable the service where SMB is not required, and firewall SMB ports (445/TCP) at the network edge until a kernel patch is available.
- **SOC/IR — Plan:** No active exploitation or IOCs reported yet, but public mailing-list disclosure of a pre-auth RCE raises the PoC timeline. Identify estate assets running ksmbd, and build detections for anomalous inbound SMB traffic to Linux hosts before a working exploit emerges.
- **Leader — Skip**
