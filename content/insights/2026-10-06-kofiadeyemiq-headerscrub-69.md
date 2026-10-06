---
title: "Go headerscrub: drops auth headers on cross-origin redirects"
date: 2026-10-06T17:10:43.586006+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["go", "header-leakage", "http-client"]
cves: []
source: "https://github.com/kofiadeyemiq/headerscrub"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Learn:** Go's default http.Client forwards all caller-set headers (including API keys and auth tokens) through cross-origin redirects — this library demonstrates the risk pattern and a mitigation worth evaluating for any Go service making outbound HTTP calls with sensitive headers.
- **SOC/IR — Skip**
- **Leader — Skip**
