---
title: "BigBear 2.0 PhaaS bypassed MFA at 258 orgs, stole 5,000 M365 credentials"
date: 2026-09-07T16:27:04.378719+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["phishing-as-a-service", "mfa-bypass", "microsoft-365"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/bigbear-microsoft-365-phishing-service-bypassed-mfa-at-258-organizations/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Active AiTM phishing at scale demonstrates that TOTP/push MFA is insufficient for M365; audit Conditional Access policies and plan a phishing-resistant MFA (FIDO2/passkeys) migration this quarter.
- **SOC/IR — Act:** With 258 confirmed victim orgs, treat this as an active campaign: hunt Entra ID and unified audit logs for anomalous session token reuse, impossible-travel sign-ins, and OAuth consent grants since mid-2026.
- **Leader — Plan:** A campaign compromising 258 organizations via MFA bypass is a concrete argument for budgeting phishing-resistant MFA; assess current MFA tier across the enterprise and bring a gap analysis to the next leadership review.
