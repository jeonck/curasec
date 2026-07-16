---
title: "Mandiant: Hardening Publicly Exposed Serverless Cloud Functions"
date: 2026-07-16T12:18:39.346883+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["cloud-security", "serverless", "hardening"]
cves: []
source: "https://cloud.google.com/blog/topics/threat-intelligence/exposed-cloud-functions-harden/"
source_name: "Google Threat Intelligence"
status: "active"
---
- **Engineer — Plan:** Mandiant assessments routinely find unauthenticated Cloud Run/Functions exposed to the internet; audit your serverless inventory for missing auth controls and apply the hardening patterns (least-privilege service accounts, input validation, network egress restrictions) this quarter. No active exploitation signals elevate this to Act.
- **SOC/IR — Learn:** The LFI/RFI and command-injection paths described could inform detection logic for serverless workloads, but there are no IOCs, no named campaign, and no novel TTPs here — no immediate hunt or rule-writing required.
- **Leader — Skip**
