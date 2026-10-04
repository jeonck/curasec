---
title: "action-dist-verify: tool to audit GitHub Actions dist integrity"
date: 2026-10-04T15:46:58.459511+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["supply-chain", "ci-cd", "github-actions"]
cves: []
source: "https://github.com/kofiadeyemiq/action-dist-verify"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Learn:** This tool rebuilds pinned JavaScript Actions from source and diffs the committed dist, addressing the tampered-dist supply-chain vector seen in real incidents. Worth evaluating for inclusion in CI pipelines that pin third-party Actions.
- **SOC/IR — Skip**
- **Leader — Skip**
