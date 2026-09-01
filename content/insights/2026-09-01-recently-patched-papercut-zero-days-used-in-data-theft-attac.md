---
title: "PaperCut NG/MF zero-days exploited in active data theft attacks"
date: 2026-09-01T15:28:52.066055+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["zero-day", "active-exploitation", "print-management"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/recently-patched-papercut-zero-days-used-in-data-theft-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** PaperCut NG/MF was exploited as a zero-day and attacks are ongoing — patch to the latest released version immediately and audit server logs for signs of unauthorized access or data exfiltration.
- **SOC/IR — Act:** Active data theft via PaperCut exploitation means assume-breach posture for any organization running PaperCut — hunt for anomalous outbound traffic and lateral movement from PaperCut servers since before the patch date.
- **Leader — Plan:** PaperCut is widely used in enterprise and education; confirm whether the organization runs it and verify that engineering has applied the patch — brief leadership only if patch status is unconfirmed or delayed.
