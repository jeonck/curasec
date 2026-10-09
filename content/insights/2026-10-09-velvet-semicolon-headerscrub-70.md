---
title: "Go library strips sensitive headers on cross-origin HTTP redirects"
date: 2026-10-09T17:26:04.474256+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["go", "appsec", "open-source-tool"]
cves: []
source: "https://github.com/velvet-semicolon/headerscrub"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Learn:** Go's default http.Client forwards all headers through redirects, potentially leaking API keys to unintended origins; this library demonstrates the fix pattern worth evaluating for any Go service that follows redirects with bearer tokens or API keys.
- **SOC/IR — Skip**
- **Leader — Skip**
