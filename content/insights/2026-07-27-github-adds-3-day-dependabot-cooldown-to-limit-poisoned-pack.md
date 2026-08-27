---
title: "GitHub Adds 3-Day Dependabot Cooldown to Block Poisoned Package PRs"
date: 2026-07-27T13:44:31.918240+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Learn"
tags: ["supply-chain", "dependabot", "dependency-management"]
cves: []
source: "https://thehackernews.com/2026/07/github-adds-3-day-dependabot-cooldown.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Plan:** Review all repos using Dependabot and explicitly configure the cooldown parameter in dependabot.yml; the 3-day default delays auto-PR creation for fresh packages, reducing poisoned-package exposure in automated update pipelines.
- **SOC/IR — Skip**
- **Leader — Learn:** Signals growing industry recognition of time-based supply chain defenses; useful context for maturing your software supply chain policy, though no immediate leadership action is required.
