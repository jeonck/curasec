---
title: "TheHatman Claims Mass Credential Theft from Microsoft Entra Tenants"
date: 2026-08-19T11:36:35.301683+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["microsoft-entra", "credential-theft", "identity-security"]
cves: []
source: "https://unit42.paloaltonetworks.com/large-scale-credential-attacks/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Plan:** Organizations running Microsoft Entra are directly in scope for this credential theft campaign; review MFA coverage and conditional access policies, audit Entra sign-in logs for anomalous authentication, and apply Unit 42's hardening guidance this sprint.
- **SOC/IR — Act:** An active claimed credential-theft campaign targeting Entra tenants creates an immediate hunt requirement — sweep Entra/M365 sign-in logs for impossible travel, anomalous service principal usage, and bulk authentication failures since mid-August when the campaign surfaced.
- **Leader — Act:** If the organization uses Microsoft Entra, direct the security team this week to confirm whether anomalous authentication activity is present and request a status brief; prepare talking points for leadership in case credential exposure is confirmed.
