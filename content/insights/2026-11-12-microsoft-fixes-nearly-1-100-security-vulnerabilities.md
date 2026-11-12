---
title: "Microsoft November 2026 Patch Tuesday: ~1,100 CVEs, Outlook Zero-Day"
date: 2026-11-12T18:52:40.662404+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["patch-tuesday", "microsoft", "zero-day"]
cves: []
source: "https://krebsonsecurity.com/2026/11/microsoft-fixes-nearly-1100-security-vulnerabilities/"
source_name: "Krebs on Security"
status: "active"
---
- **Engineer — Act:** The Outlook zero-day designation implies pre-patch exploitation; prioritize patching Outlook and triage the 63 critical Windows CVEs this week, following your standard critical-patch SLA.
- **SOC/IR — Plan:** The Outlook zero-day warrants building or tuning detections for exploitation attempts (e.g., suspicious Outlook child processes, anomalous MAPI/OLE activity); also consider a retroactive hunt covering the period before today's patch.
- **Leader — Plan:** A zero-day in Outlook at this patch scale may surface in customer security questionnaires or board questions; confirm patch teams have an accelerated SLA on the Outlook zero-day and can report status by end of week.
