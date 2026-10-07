---
title: "headerscrub: Go lib strips auth headers on cross-origin redirects"
date: 2026-10-07T17:48:59.708516+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["go", "http-security", "open-source"]
cves: []
source: "https://github.com/quietpelican42/headerscrub"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Learn:** Addresses a real credential-leak risk: Go's default http.Client follows redirects with all headers intact, which can expose tokens like X-Api-Key to unintended origins. Evaluate this library if your Go services make authenticated outbound HTTP requests that may follow redirects.
- **SOC/IR — Skip**
- **Leader — Skip**
