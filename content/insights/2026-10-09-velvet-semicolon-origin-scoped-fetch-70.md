---
title: "origin-scoped-fetch: fetch wrapper strips auth headers on cross-origin redirect"
date: 2026-10-09T17:26:04.474256+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["web-security", "credential-leakage", "open-source"]
cves: []
source: "https://github.com/velvet-semicolon/origin-scoped-fetch"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Learn:** Addresses a real fetch footgun where custom auth headers can leak to unintended origins on redirect; worth evaluating as a drop-in for any frontend or server-side code that calls third-party URLs with bearer tokens.
- **SOC/IR — Skip**
- **Leader — Skip**
