---
title: "REVSTEALER Drops 4 Persistent Modules to Kill Defender and Mine Crypto"
date: 2026-09-06T14:08:28.650854+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["windows-malware", "defense-evasion", "crypto-mining"]
cves: []
source: "https://thehackernews.com/2026/09/four-revstealer-linked-modules-disable.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Elastic documents a novel persistence pattern where the initial stealer self-deletes but leaves behind four modules (ProManager, WinUpdate, SoftManager, +1) that disable Defender and Windows Update before mining crypto; no exploitation signals, but the defense-bypass design informs endpoint hardening strategy.
- **SOC/IR — Plan:** Build or tune detections for the named module artifacts (ProManager, WinUpdate, SoftManager) and hunt for Windows Update / Defender service-disablement events paired with subsequent outbound crypto-mining traffic; check Elastic's published research for YARA rules and ATT&CK mappings.
- **Leader — Skip**
