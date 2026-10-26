---
title: "Gheist Campaign Steals GitHub Repo Secrets via Malicious Actions Logs"
date: 2026-10-26T17:20:31.892638+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["github-actions", "ci-cd", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/10/gheist-uses-stolen-github-tokens-to.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active campaign directly targeting CI/CD pipelines: stolen tokens plant workflows that echo secrets to Actions logs, then delete the runs. Immediately audit GitHub Actions logs for unexpected workflow runs, rotate all repository and org-level secrets, and tighten token scopes to least privilege.
- **SOC/IR — Act:** The delete-run-after-exfiltration pattern is a concrete hunt target in GitHub audit logs. Search for workflow run creation followed by rapid deletion, and sweep for tokens with unusual write-workflow permissions used outside normal pipelines since the campaign began.
- **Leader — Plan:** Active exfiltration campaign targeting private GitHub and GitHub Enterprise repos is worth a this-week check-in: confirm with engineering that no unauthorized workflow runs exist in your org and that secret rotation is scheduled if any anomalies are found.
