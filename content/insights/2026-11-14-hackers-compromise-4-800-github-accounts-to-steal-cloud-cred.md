---
title: "4,800 compromised GitHub accounts used to steal cloud credentials"
date: 2026-11-14T17:01:43.117086+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["github-supply-chain", "cloud-credentials", "secrets-theft"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-compromise-4-800-github-accounts-to-steal-cloud-credentials/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Active campaign pushing credential-stealing code via GitHub pull requests across tens of thousands of repos; audit recent PRs from unfamiliar contributors, review CI/CD pipeline history for unauthorized commits, and rotate any cloud credentials accessible from your repositories.
- **SOC/IR — Act:** Campaign has distinct behavioral fingerprint — bulk PR openings from compromised accounts at scale; hunt for anomalous PR creation patterns in GitHub audit logs and correlate with unusual cloud API calls or credential-use spikes following recent merges.
- **Leader — Plan:** Widespread active operation targeting cloud credentials stored in or accessible via GitHub repos; direct your security team this quarter to audit org-level GitHub activity for suspicious PRs and confirm cloud secrets are managed via vaults rather than repo configuration.
