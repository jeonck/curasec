---
title: "origin-scoped-fetch: drop auth headers on cross-origin redirects"
date: 2026-10-06T17:10:43.586006+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["web-security", "fetch-api", "credential-leakage"]
cves: []
source: "https://github.com/kofiadeyemiq/origin-scoped-fetch"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Learn:** Highlights a subtle but real risk: custom auth headers can follow fetch redirects to unintended origins, leaking credentials. Worth reviewing your fetch usage patterns in web apps — no active exploitation, so no immediate action required.
- **SOC/IR — Skip**
- **Leader — Skip**
