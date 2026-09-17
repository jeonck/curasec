---
title: "BIND 9 Patches 14 Flaws Including Unauthenticated DoH Crash"
date: 2026-09-17T15:32:45.721902+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["dns", "bind", "patch"]
cves: []
source: "https://thehackernews.com/2026/09/bind-9-update-fixes-14-flaws-including.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Any BIND server with DNS-over-HTTPS enabled can be crashed unauthenticated with a single malformed request; update to BIND 9.20.29 or 9.21.26 and audit whether DoH is exposed externally. No KEV listing or public PoC yet, but the zero-credential DoS lowers the exploitation bar significantly.
- **SOC/IR — Skip**
- **Leader — Skip**
