---
title: "Police Dismantle Kratos MFA-Bypass Phishing Kit; Developer Arrested"
date: 2026-07-22T12:46:13.866991+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["phishing", "mfa-bypass", "microsoft-365"]
cves: []
source: "https://thehackernews.com/2026/07/police-dismantle-kratos-phishing-kit.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Kratos used adversary-in-the-middle techniques to steal M365 session tokens and bypass MFA — a reminder that TOTP/push-based MFA is insufficient against phishing; engineers should evaluate phishing-resistant MFA (FIDO2/passkeys) for privileged M365 accounts.
- **SOC/IR — Learn:** No IOCs or detection specifics are provided, so no immediate hunt is actionable; the takedown does validate that AiTM session-token theft against M365 was widespread, which reinforces monitoring for anomalous token reuse and impossible-travel sign-ins if not already covered.
- **Leader — Learn:** The scale of Kratos confirms that MFA bypass via phishing is not theoretical — useful evidence when making the case for phishing-resistant MFA investment or reviewing identity risk with the board; no immediate action required given the infrastructure has been seized.
