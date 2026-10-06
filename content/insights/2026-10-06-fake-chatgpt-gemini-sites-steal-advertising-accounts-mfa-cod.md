---
title: "Fake AI chatbot sites steal ad account credentials via BiTB attacks"
date: 2026-10-06T17:10:43.586006+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["phishing", "credential-theft", "browser-in-browser"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/fake-chatgpt-gemini-sites-steal-advertising-accounts-mfa-codes/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** Browser-in-browser phishing targeting SaaS credentials is a technique worth understanding for security awareness programs and evaluating whether your SSO/FIDO2 posture would resist it; no patch or config change needed today.
- **SOC/IR — Plan:** Build or tune detections for browser-in-browser lure patterns targeting ad platform logins; consider hunting for anomalous OAuth grant activity in M365/Google Workspace logs from users in marketing or growth roles.
- **Leader — Skip**
