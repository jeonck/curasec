---
title: "Kali365 Abuses Microsoft Device Code Flow to Steal OAuth Tokens"
date: 2026-08-05T13:01:27.566949+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["phishing", "microsoft-entra", "token-theft"]
cves: []
source: "https://thehackernews.com/2026/08/kali365-weaponizes-microsoft.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Device code flow phishing is a real and growing vector for M365/Azure tenants; audit Conditional Access policies to block or restrict device code flow for user accounts that don't require it, and enforce compliant-device requirements where the flow must remain enabled.
- **SOC/IR — Plan:** Build or tune detections on Entra ID sign-in logs for device code authorization events originating from unexpected locations or apps; also hunt for refresh token reuse anomalies that may indicate post-phishing lateral movement within M365.
- **Leader — Learn:** A named actor targeting US M365 tenants via Microsoft's own authentication UI is useful context for the risk register and customer security questionnaire responses, but no confirmed breaches or near-term regulatory deadlines make this a monitor-and-track item rather than an executive action.
