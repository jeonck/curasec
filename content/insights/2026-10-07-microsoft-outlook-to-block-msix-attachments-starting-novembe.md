---
title: "Microsoft Outlook to block MSIX attachments starting November"
date: 2026-10-07T17:48:59.708516+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["msix", "email-security", "microsoft-outlook"]
cves: []
source: "https://www.bleepingcomputer.com/news/microsoft/microsoft-outlook-to-block-msix-attachments-used-in-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** MSIX packages have been abused as a malware delivery vector; Outlook Web and new Windows client will block them in November. Audit any internal tooling or deployment pipelines that send MSIX files via email and migrate to an alternative distribution method before the deadline.
- **SOC/IR — Learn:** MSIX attachment delivery has been an active malware distribution channel; this announcement confirms the technique has been widely abused. No new detection work required — the platform control handles it — but worth understanding MSIX-based lure campaigns when triaging historical email-borne threats.
- **Leader — Skip**
