---
title: "Greatness PhaaS Adds Device Code Phishing to Bypass MFA"
date: 2026-08-05T13:01:27.566949+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["phishing-as-a-service", "mfa-bypass", "oauth"]
cves: []
source: "https://thehackernews.com/2026/08/greatness-phaas-adds-device-code.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Plan:** Device code flow abuse bypasses MFA by design; audit your identity provider (Entra ID, Okta) and restrict or disable the OAuth Device Authorization Grant for users/apps that don't require it — block or conditional-policy-gate this flow this quarter.
- **SOC/IR — Plan:** No IOCs provided, but Greatness PhaaS commoditizing device code phishing signals growing campaign volume; build detections in Entra/Okta logs for unexpected device code authorization requests, particularly outside normal device-enrollment windows.
- **Leader — Learn:** MFA bypass techniques are now packaged in commercial crimeware toolkits, eroding the assurance value of standard MFA — useful context for risk register updates and for evaluating phishing-resistant auth (FIDO2/passkeys) as a strategic control.
