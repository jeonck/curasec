---
title: "headerscrub: Go lib strips auth headers on cross-origin redirects"
date: 2026-10-11T16:38:10.899521+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["go", "supply-chain", "appsec"]
cves: []
source: "https://github.com/typesafe-docs/headerscrub"
source_name: "GitHub Trending"
status: "archived"
---
- **Engineer — Learn:** Go's http.Client follows redirects and carries caller-set headers by default, which can leak API keys to unintended origins; this library enforces a drop-on-origin-change policy worth evaluating if your Go services make outbound API calls with sensitive headers.
- **SOC/IR — Skip**
- **Leader — Skip**
