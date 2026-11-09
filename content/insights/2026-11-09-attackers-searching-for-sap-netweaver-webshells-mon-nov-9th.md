---
title: "Active Scanning for SAP NetWeaver Webshells Observed in Honeypots"
date: 2026-11-09T21:25:24.006803+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["sap-netweaver", "webshell", "active-scanning"]
cves: []
source: "https://isc.sans.edu/diary/rss/33502"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Act:** Active honeypot-observed scanning for SAP NetWeaver webshells indicates ongoing post-exploitation sweep activity tied to the well-documented spring 2025 compromise wave; audit SAP NetWeaver instances for unauthorized webshells under paths like /irj/ and confirm CVE-2025-31324 patches are applied.
- **SOC/IR — Act:** Threat actors are actively sweeping for existing SAP NetWeaver webshells — hunt HTTP logs for anomalous POST requests or server-side script execution on SAP application servers, and treat any SAP NetWeaver exposure as assume-breach until ruled out.
- **Leader — Plan:** Renewed scanning activity suggests SAP NetWeaver remains a live target; confirm with engineering that all SAP instances were audited and patched following the spring 2025 exploitation campaign before the next audit cycle.
