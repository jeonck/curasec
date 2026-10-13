---
title: "SAP patches max-severity SSRF flaw in Cloud SDK for Python (Oct 2026)"
date: 2026-10-13T18:14:34.078200+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["sap", "ssrf", "oauth2"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/sap-warns-of-maximum-severity-oauth2-ssrf-security-flaw/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Maximum-severity SSRF in SAP Cloud SDK for Python could allow unauthenticated server-side request forgery via the OAuth2 layer; patch is available but no KEV listing or public PoC. Update SAP Cloud SDK for Python to the October 2026 patched release this sprint, and audit any internal-only endpoints reachable from BTP workloads.
- **SOC/IR — Skip**
- **Leader — Skip**
