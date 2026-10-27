---
title: "Microsoft Authenticator Android flaw enables permissionless work token theft"
date: 2026-10-27T16:34:51.683639+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["mfa-vulnerability", "android", "token-theft"]
cves: ["CVE-2026-80097"]
source: "https://thehackernews.com/2026/10/microsoft-authenticator-flaw-let.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Public PoC exists on GitHub but EPSS is 0.01 and not KEV-listed, so no active exploitation pressure yet. Push Authenticator for Android version 6.2606.4246 via MDM to all enrolled devices and verify compliance through your endpoint management console.
- **SOC/IR — Learn:** The technique — a permissionless Android app impersonating a trusted Microsoft app to harvest Entra/work tokens — is worth understanding for future detection work (e.g., anomalous sign-in source patterns in Entra logs), but no IOCs or active campaign have been reported.
- **Leader — Skip**
- **Signals:** CVE-2026-80097 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub
