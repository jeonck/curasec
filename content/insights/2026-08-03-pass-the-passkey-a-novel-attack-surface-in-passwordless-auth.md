---
title: "Passkey UV Flag Bypass Reduces Passwordless Auth to Single Factor"
date: 2026-08-03T13:48:19.180160+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["passkeys", "authentication", "webauthn"]
cves: []
source: "https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Plan:** Audit your WebAuthn/passkey relying party implementation to confirm the User Verified flag is enforced; if your app accepts assertions without UV=true, you've silently degraded MFA to single-factor auth.
- **SOC/IR — Learn:** No exploitation in the wild reported and no IOCs available; useful for understanding how passkey bypass could appear in authentication logs if UV flag checks are absent.
- **Leader — Skip**
