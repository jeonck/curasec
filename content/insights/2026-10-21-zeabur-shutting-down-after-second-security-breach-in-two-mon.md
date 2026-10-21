---
title: "Zeabur dev platform shuts down after second breach; 3.2M env vars stolen"
date: 2026-10-21T15:56:43.831517+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Act"
tags: ["data-breach", "credential-theft", "developer-tooling"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/zeabur-shutting-down-after-second-security-breach-in-two-months/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** If Zeabur was used in any environment — dev, staging, or prod — treat all environment variables stored there as compromised and rotate them immediately, prioritizing database credentials, API keys, and cloud provider tokens.
- **SOC/IR — Learn:** No IOCs, TTPs, or detection-ready artifacts are published; the breach offers a case study in plaintext credential storage risk but yields no immediate hunt or detection work.
- **Leader — Act:** Scan your developer tooling inventory for Zeabur usage; if found, confirm the scope of exposed secrets, trigger a credentials rotation sprint, and note that the vendor is shutting down — no incident report will be forthcoming after closure.
