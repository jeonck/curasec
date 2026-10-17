---
title: "UAT-11985 APT Uses AitM Phishing to Bypass Google MFA at Taiwan Research Orgs"
date: 2026-10-17T14:12:31.177036+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["apt", "aitm-phishing", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/10/uat-11985-uses-fake-event-invites-to.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** The AitM technique harvests session tokens post-MFA, meaning standard TOTP/SMS MFA offers no protection; this reinforces the case for deploying phishing-resistant MFA (FIDO2/hardware keys) for privileged Google Workspace accounts.
- **SOC/IR — Learn:** No IOCs are published in the current disclosure, so there is nothing to sweep for now; the AitM-against-Google pattern maps to ATT&CK T1557 and T1566, and is worth incorporating into hunt hypotheses if your estate includes Taiwan-affiliated research partnerships.
- **Leader — Skip**
