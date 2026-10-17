---
title: "Critical RCE in BlockStrap plugin for Magento/Adobe Commerce"
date: 2026-10-17T14:12:31.177036+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["rce", "magento", "php"]
cves: ["CVE-2026-103849"]
source: "https://www.bleepingcomputer.com/news/security/critical-blockstrap-flaw-lets-hackers-run-code-on-magento-servers/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** A public PoC on GitHub makes exploitation practical despite the low EPSS; RCE on an e-commerce server likely handling payment data warrants immediate action. Update or remove the BlockStrap plugin on all Magento/Adobe Commerce instances and verify no post-exploitation artifacts exist.
- **SOC/IR — Plan:** No confirmed active exploitation yet, but a public PoC means attacks could begin soon. Build or tune detections for anomalous PHP execution and unexpected outbound connections from Magento web server processes in preparation for exploitation attempts.
- **Leader — Skip**
- **Signals:** CVE-2026-103849 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub
