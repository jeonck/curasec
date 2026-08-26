---
title: "Mirage2FA PhaaS Bypasses M365 MFA, 4,500 US/EU Firms Targeted"
date: 2026-08-26T11:42:13.540622+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["phishing-as-a-service", "microsoft-365", "mfa-bypass"]
cves: []
source: "https://thehackernews.com/2026/08/mirage2fa-surge-hits-4500-us-and-eu.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** AiTM phishing that defeats standard MFA is a config problem, not a patch problem — audit your Entra ID Conditional Access policies and prioritize migrating M365 users to phishing-resistant MFA (FIDO2/passkeys) this quarter, as TOTP and SMS are insufficient against this class of attack.
- **SOC/IR — Act:** This campaign is active and broadly targeting US enterprises via M365; hunt for AiTM indicators in Entra ID sign-in logs now — flag token issuance from unexpected IPs, session establishment followed by unusual API activity, and impossible-travel events from the same session cookie.
- **Leader — Act:** With 4,500 organizations targeted and ~48% of targeted addresses potentially compromised, confirm with your team this week that phishing-resistant MFA is enforced for M365 and assess whether your domain appeared in ANY.RUN's targeting data; this is board-question territory given the scale.
