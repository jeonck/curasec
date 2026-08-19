---
title: "CISA KEV: macOS, SharePoint, vCenter, IKE Flaws Actively Exploited"
date: 2026-08-19T11:36:35.301683+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["cisa-kev", "active-exploitation", "critical-cve"]
cves: ["CVE-2026-65400"]
source: "https://thehackernews.com/2026/08/critical-macos-sharepoint-vcenter-and.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Four KEV-listed critical vulns across platforms you likely run — patch macOS (CVE-2026-65400, CVSS 9.8), SharePoint, vCenter, and Microsoft IKE immediately; a public PoC exists for the macOS flaw, making exploitation trivial.
- **SOC/IR — Act:** Active exploitation of vCenter and SharePoint warrants an assume-breach sweep — hunt for post-exploitation activity (credential dumping, lateral movement) on these systems dating back at least 30 days, and tune detections for anomalous SharePoint API calls and vCenter admin actions.
- **Leader — Act:** KEV-listed active exploitation across macOS endpoints, SharePoint, and vCenter is a systemic risk event — confirm patch status and exposure scope with engineering this week, and be prepared to brief leadership if any of these systems host sensitive data or are business-critical.
- **Signals:** CVE-2026-65400 — CISA KEV: listed, EPSS 0.00, public PoC on GitHub
