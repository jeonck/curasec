---
title: "PowerShell guide for auditing Entra ID login logs and detecting password sprays"
date: 2026-08-21T11:38:25.806134+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["entra-id", "password-spray", "detection"]
cves: []
source: "https://isc.sans.edu/diary/rss/33268"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** Practical reminder that cloud identity login logs (Entra ID sign-in logs) deserve the same daily scrutiny as on-prem logs; useful if you haven't wired these into a monitoring workflow yet, but no patch or config change required.
- **SOC/IR — Plan:** Adopt or adapt the PowerShell queries shown to pull Entra successful/failed login data for routine password-spray hunting; worth scheduling as a log-source coverage improvement if Entra sign-in logs aren't already feeding your SIEM.
- **Leader — Skip**
