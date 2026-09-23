---
title: "Rogue external MFA provider registration can harvest passwords at login"
date: 2026-09-23T15:27:03.663698+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["identity", "mfa", "attack-technique"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/rogue-external-mfa-providers-can-steal-passwords-during-logins/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Audit who holds privileges to register external MFA providers in your identity platform (Entra ID, Okta, etc.) and restrict that permission to a minimal group; no active exploitation reported, but the attack surface is real for orgs using federated MFA.
- **SOC/IR — Plan:** Instrument your identity-platform audit logs to alert on new external MFA provider registrations — this technique leaves a trace there; no IOCs or active campaign to hunt for today.
- **Leader — Learn:** Research demonstrates that a privileged insider or compromised admin account could silently intercept credentials via a rogue MFA provider; informs insider-threat and vendor-risk conversations but requires no immediate action given no reported exploitation.
