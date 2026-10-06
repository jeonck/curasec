---
title: "Rejetto HFS servers actively scanned for RCE via weak signing key"
date: 2026-10-06T17:10:43.586006+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Skip"
tags: ["rce", "active-scanning", "cve"]
cves: ["CVE-2026-61500"]
source: "https://www.bleepingcomputer.com/news/security/rejetto-hfs-servers-now-actively-scanned-for-critical-rce-flaw/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Active scanning for CVE-2026-61500 with a public PoC means exploitation is imminent for any exposed Rejetto HFS instance; identify and patch or take offline any internet-facing HFS servers immediately.
- **SOC/IR — Act:** Active scanning is underway — hunt for anomalous authentication or session-related traffic against HFS servers and sweep for signs of session forgery or RCE activity since the scanning began.
- **Leader — Skip**
- **Signals:** CVE-2026-61500 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub, reported by 2 collected sources
