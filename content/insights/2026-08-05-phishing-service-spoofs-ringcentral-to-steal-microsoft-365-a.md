---
title: "Greatness PhaaS expands to AiTM and device-code attacks on M365"
date: 2026-08-05T13:01:27.566949+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["phishing-as-a-service", "microsoft-365", "adversary-in-the-middle"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/phishing-service-spoofs-ringcentral-to-steal-microsoft-365-accounts/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** AiTM and device-code phishing bypass standard MFA; audit your M365 conditional access policies to restrict or block device code flow, and prioritize phishing-resistant MFA (FIDO2 or certificate-based) for privileged accounts this quarter.
- **SOC/IR — Plan:** Build or tune detections for suspicious device-code OAuth grant flows and anomalous session token reuse in Entra ID / M365 audit logs — the AiTM component means valid MFA completion is not a reliable innocence signal.
- **Leader — Learn:** Confirms that commodity phishing platforms are now routing around standard MFA at scale; useful background when justifying a phishing-resistant MFA upgrade on the roadmap or fielding customer security questionnaires about M365 identity controls.
