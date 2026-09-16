---
title: "N0va Phishkit Targets US/EU Businesses via Auth Flow Abuse"
date: 2026-09-16T15:25:29.032898+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["phishing", "identity-theft", "aitm"]
cves: []
source: "https://thehackernews.com/2026/09/n0va-phishkit-targets-us-and-eu.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** AiTM-style phishing that bypasses MFA by hijacking legitimate auth flows warrants reviewing phishing-resistant MFA (FIDO2/passkeys) and conditional access policies; audit identity provider logs for anomalous session tokens this quarter.
- **SOC/IR — Plan:** No IOCs are provided, but the technique — abusing legitimate auth flows to harvest session tokens — is worth building detections for: tune SIEM rules to flag impossible-travel logins and anomalous OAuth token grants from new IP ranges.
- **Leader — Learn:** Broad US/EU targeting of businesses via identity compromise is a useful data point for risk discussions around MFA strength, but no named victims or sector-specific details make this a board-level action item yet.
