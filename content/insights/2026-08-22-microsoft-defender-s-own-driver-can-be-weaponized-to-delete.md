---
title: "Microsoft Defender's BTR.sys Driver Abused to Delete Security Tools at Boot"
date: 2026-08-22T11:32:44.405318+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["windows-driver", "edr-bypass", "kernel-level"]
cves: []
source: "https://thehackernews.com/2026/08/microsoft-defenders-own-driver-can-be.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No exploitable flaw and no patch exists — this is abuse of a legitimately signed Defender component, so there's nothing to patch; understand the technique and evaluate whether existing attack surface reduction or kernel driver allow-listing policies limit BTR.sys invocation outside Defender's normal use.
- **SOC/IR — Plan:** Novel boot-time EDR-disablement technique worth building detections for: plan to hunt for anomalous BTR.sys loading events or unexpected security product file/registry removal at boot, and check whether your EDR vendor provides detection coverage for this abuse pattern.
- **Leader — Learn:** Research disclosure with no active exploitation signals; relevant background if stakeholders ask about Defender's reliability as a security control, but no leadership action is required at this time.
