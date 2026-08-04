---
title: "18 Malicious npm Packages Target Alibaba Tool Users with Cross-Platform RAT"
date: 2026-08-04T13:07:50.076253+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["supply-chain", "npm", "malware"]
cves: []
source: "https://thehackernews.com/2026/08/18-malicious-npm-packages-deliver-cross.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Audit your npm dependency tree for any package named 'lib-mtop' or other scoped/unscoped Alibaba-adjacent packages; add registry scoping rules or lockfile scrutiny to your CI pipeline to catch namespace-confusion attacks before they land.
- **SOC/IR — Learn:** No IOCs or ATT&CK mappings are provided in the enrichment signals; file this as context on namespace-confusion supply-chain TTPs and revisit if indicators emerge.
- **Leader — Skip**
