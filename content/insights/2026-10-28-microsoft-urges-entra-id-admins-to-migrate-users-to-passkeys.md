---
title: "Microsoft sets Feb 2027 deadline to retire Entra ID SMS/voice auth"
date: 2026-10-28T17:09:30.637292+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["entra-id", "passkeys", "mfa-deprecation"]
cves: []
source: "https://www.bleepingcomputer.com/news/microsoft/microsoft-reminds-entra-id-admins-to-migrate-users-to-passkeys/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Hard deadline of February 2027 for Entra ID SMS and voice auth retirement; begin inventorying affected users and roll out FIDO2/passkey or Authenticator app enrollment before the cutover to avoid sign-in disruptions.
- **SOC/IR — Learn:** The eventual deprecation of SMS/voice MFA will shift the phishing and MFA-bypass attack surface — worth tracking to anticipate adjustments to credential-theft detection logic, but no immediate hunting action needed.
- **Leader — Plan:** Microsoft is enforcing a February 2027 hard deadline on SMS/voice auth in Entra ID; allocate team capacity this quarter to scope user migration and avoid service disruptions that could escalate to a leadership incident.
