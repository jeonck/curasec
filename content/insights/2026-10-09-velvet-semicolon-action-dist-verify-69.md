---
title: "action-dist-verify: Tool to Audit GitHub Actions dist Integrity"
date: 2026-10-09T17:26:04.474256+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["supply-chain", "ci-cd", "github-actions"]
cves: []
source: "https://github.com/velvet-semicolon/action-dist-verify"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Plan:** This tool addresses a real supply-chain vector where committed dist/ in a pinned Action can diverge from source — a technique used in past compromises like tj-actions. Evaluate and integrate into your repo audit process this quarter to verify Actions you pin haven't had tampered dist artifacts.
- **SOC/IR — Learn:** Provides useful framing for the dist-vs-source discrepancy attack surface in GitHub Actions supply-chain attacks, but no IOCs, active campaigns, or detection rules are surfaced by this tool release itself.
- **Leader — Skip**
