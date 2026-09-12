---
title: "Passkey-themed phishing by ShinyHunters targets Microsoft 365"
date: 2026-09-12T14:04:45.501336+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["phishing", "microsoft-365", "social-engineering"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/passkey-themed-phishing-attacks-lead-to-microsoft-365-data-theft/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Active campaign exploiting passkey/SSO trust to bypass MFA means now is the time to enforce phishing-resistant authentication (FIDO2 hardware keys, not app-based) in M365 conditional access policies and audit OAuth app consent grants in Entra ID.
- **SOC/IR — Act:** Named extortion actors (ShinyHunters, Helix) are running active M365 credential theft campaigns — hunt for anomalous Entra ID sign-ins, suspicious OAuth consent grants, and new delegated permissions added to M365 tenants since this campaign surfaced.
- **Leader — Plan:** ShinyHunters is a data-publication extortion group; their targeting of M365 raises breach-disclosure risk for organizations holding regulated data in that platform — schedule a review of M365 data residency, DLP controls, and phishing-awareness coverage for passkey/SSO lure themes this quarter.
