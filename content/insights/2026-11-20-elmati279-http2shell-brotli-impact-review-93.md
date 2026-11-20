---
title: "Research: HTTP/2 shell transport with Brotli compression reviewed"
date: 2026-11-20T19:04:41.748130+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["http2", "c2-techniques", "research"]
cves: []
source: "https://github.com/elmati279/http2shell-brotli-impact-review"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Learn:** Research exploring HTTP/2 as a shell transport channel with Brotli compression warrants awareness for teams designing egress controls or WAF rules, but no CVE, patch, or active exploitation is present to act on.
- **SOC/IR — Learn:** If this research documents HTTP/2-based shell tunneling techniques, it's worth reading to inform future detection logic for covert C2 over compressed HTTP/2 streams, but no IOCs or Sigma/KQL rules accompany the summary.
- **Leader — Skip**
