---
title: "Telerik UI Padding-Oracle Chained to Unauthenticated RCE — PoC Public"
date: 2026-09-07T16:27:04.378719+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["telerik-ui", "padding-oracle", "rce"]
cves: []
source: "https://thehackernews.com/2026/09/telerik-ui-padding-oracle-bug-chained.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A working unauthenticated RCE exploit chain against Telerik UI for ASP.NET AJAX is now public; apply the July Progress patch immediately and audit whether any deployments use the affected non-default AES-CBC configuration that enables the oracle.
- **SOC/IR — Plan:** No confirmed wild exploitation or published IOCs yet, but the public PoC warrants building detections for anomalous HTTP requests targeting Telerik AJAX endpoints — prepare Sigma/SPL rules now so you're ready if exploitation picks up.
- **Leader — Skip**
