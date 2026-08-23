---
title: "Malicious Packagist Packages Weaponize GitHub Actions to Hit cPanel/WHM"
date: 2026-07-23T12:47:45.543557+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["supply-chain", "ci-cd", "php"]
cves: []
source: "https://thehackernews.com/2026/07/attackers-weaponize-github-actions.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Act:** Active supply-chain compromise of 10 Packagist packages tied to developer dinushchathurya (July 12–13); audit your PHP dependency tree for these packages, remove or pin away from any dev/pre-release versions, and inspect CI/CD build logs for unexpected executions since July 12.
- **SOC/IR — Plan:** No IOCs are surfaced in the summary, but the campaign's use of malicious Packagist dev-version installs inside GitHub Actions runners is a detectable pattern — build a detection for unusual package-manager installs of dev/pre-release versions in pipeline logs and hunt for dinushchathurya package executions since July 12.
- **Leader — Learn:** This campaign illustrates how a single compromised developer account can turn a public package registry into attack infrastructure; useful context when reviewing third-party dependency risk in your software supply chain policy.
