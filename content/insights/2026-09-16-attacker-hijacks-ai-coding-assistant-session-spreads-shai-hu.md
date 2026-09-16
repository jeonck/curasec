---
title: "AI Coding Assistant Session Hijacked, Spreads Worm to 100 Repos"
date: 2026-09-16T15:25:29.032898+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Act"
tags: ["supply-chain", "ai-security", "repository-compromise"]
cves: []
source: "https://thehackernews.com/2026/09/attacker-hijacks-ai-coding-assistant.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active supply-chain attack via AI coding assistant session hijacking is directly relevant to any team using these tools; audit AI assistant session controls, review recently accepted AI-recommended packages for tampering, and scan repository secrets for exfiltration indicators.
- **SOC/IR — Plan:** No published IOCs yet, but the TTPs are mappable — AI session hijacking leading to mass repository writes and secret exfiltration; build detections for anomalous AI coding assistant activity and bulk repository commits from service accounts this quarter.
- **Leader — Act:** A Mandiant-documented supply-chain compromise via AI coding assistant is a systemic risk for any org using similar tools; assess internal AI assistant deployment controls this week and prepare a brief for leadership on AI-enabled developer toolchain risk before customers or the board ask.
