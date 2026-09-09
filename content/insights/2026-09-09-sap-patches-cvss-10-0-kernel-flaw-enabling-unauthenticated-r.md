---
title: "SAP Patches CVSS 10.0 Unauthenticated RCE in Extended Passport Processing"
date: 2026-09-09T15:05:56.552281+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["sap", "remote-code-execution", "critical-vulnerability"]
cves: ["CVE-2026-44756"]
source: "https://thehackernews.com/2026/09/sap-patches-cvss-100-kernel-flaw.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC on GitHub for a CVSS 10.0 unauthenticated memory-corruption RCE in SAP EPP meets the Act bar even without KEV listing. Apply SAP's September 2026 security patch for CVE-2026-44756 immediately if you run SAP Extended Passport Processing.
- **SOC/IR — Plan:** No active exploitation observed (EPSS 0.00, no KEV), but a public PoC raises the likelihood of imminent attempts; build or tune detections for anomalous unauthenticated requests targeting SAP EPP endpoints before exploitation materializes.
- **Leader — Plan:** A maximum-severity publicly-PoC'd RCE in SAP — widely deployed in enterprise environments — warrants confirming this quarter whether your organization runs SAP EPP and ensuring the engineering team has this patch scheduled in their current sprint.
- **Signals:** CVE-2026-44756 — CISA KEV: not listed, EPSS 0.00, public PoC on GitHub
