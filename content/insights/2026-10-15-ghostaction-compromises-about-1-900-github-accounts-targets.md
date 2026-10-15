---
title: "GhostAction Steals CI Secrets from 30K+ GitHub Repositories"
date: 2026-10-15T15:35:13.586755+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "github", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/10/ghostaction-compromises-about-1900.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active campaign extracted CI secrets from public repositories on October 8-9; audit all public repos for exposed secrets in CI config files and rotate GitHub PATs and any credentials stored in workflows immediately.
- **SOC/IR — Act:** Campaign has a tight activity window (Oct 8-9); hunt for unauthorized GitHub OAuth activity, anomalous CI/CD pipeline triggers, and unexpected secret-access events in organizational repos since that date.
- **Leader — Act:** Approximately 1,900 accounts compromised at scale warrants a same-week check: confirm with engineering whether any organizational GitHub accounts were among those affected and request an audit of CI secret exposure before this surfaces as a supply-chain incident.
