---
title: "action-dist-verify: audit GitHub Actions dist vs source integrity"
date: 2026-10-07T17:48:59.708516+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["supply-chain", "ci-cd", "github-actions"]
cves: []
source: "https://github.com/quietpelican42/action-dist-verify"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Plan:** Supply-chain tampering via committed dist files in GitHub Actions is a real attack vector; evaluate and integrate action-dist-verify into your CI pipeline to catch dist/source divergence in pinned Actions this quarter.
- **SOC/IR — Skip**
- **Leader — Skip**
