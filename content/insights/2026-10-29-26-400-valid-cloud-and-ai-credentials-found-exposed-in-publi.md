---
title: "26,400 Valid Cloud/AI Credentials Exposed in Public Gitee Repos"
date: 2026-10-29T17:24:45.058738+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["secret-sprawl", "cloud-credentials", "supply-chain"]
cves: []
source: "https://thehackernews.com/2026/10/26400-valid-cloud-and-ai-credentials.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Exposed credentials are confirmed valid and immediately usable by anyone. Audit your org's public Gitee repositories for hardcoded cloud and AI API keys, then rotate any discovered secrets and enforce pre-commit secret scanning across all public code-hosting platforms.
- **SOC/IR — Plan:** No specific IOCs or active campaign are reported, but the scale of valid exposed credentials signals likely ongoing abuse. Build or tune detections for anomalous cloud API authentication — unusual geos, times, or access patterns for cloud/AI service keys — to catch credential misuse before it surfaces as a breach.
- **Leader — Plan:** At 26,400 working credentials, this research underscores systemic secret sprawl risk beyond GitHub. This quarter, confirm whether developer activity extends to Gitee or similar platforms, and verify that automated secrets scanning is enforced on all public repositories your org controls.
