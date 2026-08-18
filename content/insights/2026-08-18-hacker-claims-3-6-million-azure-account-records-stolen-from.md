---
title: "Hacker claims 3.6M Azure account records sold from Fortune 500 firms"
date: 2026-08-18T11:37:25.033598+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Act"
tags: ["azure", "credential-theft", "data-breach"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hacker-claims-36-million-azure-account-records-stolen-from-major-companies/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** The alleged vector is compromised credentials, not a platform vulnerability — audit Azure Entra ID sign-in logs for anomalous authentication, verify MFA is enforced on all accounts, and review conditional access policies for gaps.
- **SOC/IR — Plan:** No IOCs or confirmed TTPs are available yet, but if your estate includes Azure, queue a hunt for unusual authentication patterns in Entra ID logs (off-hours logins, new service principals, bulk data exports) and monitor breach-data feeds for your org's domains.
- **Leader — Act:** If Azure is in your estate, contact your Microsoft account team this week to ask whether your tenant appears in this claimed dataset, and prepare a brief for leadership in case the story gains traction or your company is named.
