---
title: "origin-scoped-fetch: drops auth headers on cross-origin redirects"
date: 2026-10-07T17:48:59.708516+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["web-security", "auth-headers", "open-source-tool"]
cves: []
source: "https://github.com/quietpelican42/origin-scoped-fetch"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Learn:** Addresses a real auth-header leakage risk where custom credentials follow HTTP redirects to unexpected origins; worth evaluating if your app issues authenticated server-side or client-side fetches that may redirect. No exploitation signals or active risk — review as a candidate hardening library.
- **SOC/IR — Skip**
- **Leader — Skip**
