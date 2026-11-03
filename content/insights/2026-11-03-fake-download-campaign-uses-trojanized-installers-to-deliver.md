---
title: "Trojanized Inno installers used in fake-download monetization campaign"
date: 2026-11-03T18:24:39.173812+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["malware", "supply-chain", "endpoint"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/11/03/fake-download-campaign-uses-trojanized-installers-deliver-monetization-payloads/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Learn:** No supply-chain compromise of a legitimate package — this is user-initiated fake-download lures, so no direct patch or config action needed; review software distribution controls to ensure internal builds use signed, verified installers.
- **SOC/IR — Plan:** Microsoft provides detection and investigation guidance for the full installer session; build or tune detections for Inno installer execution chains spawning unexpected child processes, and review EDR telemetry for this behavior pattern.
- **Leader — Skip**
