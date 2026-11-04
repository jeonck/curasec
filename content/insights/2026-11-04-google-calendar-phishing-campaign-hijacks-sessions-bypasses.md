---
title: "Google Calendar phishing campaign hijacks sessions, bypasses MFA"
date: 2026-11-04T18:40:06.241551+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["phishing", "mfa-bypass", "google-workspace"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/google-calendar-phishing-campaign-hijacks-sessions-bypasses-mfa/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** No patch target here — the attack abuses trusted Google services and legitimate redirect chains to steal sessions post-MFA. Use this to inform a review of phishing-resistant MFA (FIDO2/passkeys) adoption in Google Workspace and session-lifetime policy tightening.
- **SOC/IR — Plan:** The technique (Calendar invite → trusted redirect → fake login → session cookie theft) is well-documented enough to build Workspace audit-log detections for anomalous OAuth token issuance and login events following Calendar invite interactions; no published IOCs yet to sweep against.
- **Leader — Learn:** This campaign illustrates that standard TOTP/push MFA does not stop session-hijacking phishing, which is relevant when reporting MFA coverage as a control to auditors or the board; note the gap in the risk register and revisit phishing-resistant MFA roadmap.
