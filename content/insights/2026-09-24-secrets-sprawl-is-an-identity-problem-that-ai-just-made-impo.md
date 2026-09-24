---
title: "AI-Assisted Code Leaks Secrets at 2x Rate of Human-Written Code"
date: 2026-09-24T15:49:46.689252+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Plan"
tags: ["secrets-sprawl", "ai-coding", "credential-exposure"]
cves: []
source: "https://thehackernews.com/2026/09/secrets-sprawl-is-identity-problem-that.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** GitGuardian's 2026 data showing AI-assisted commits leak secrets at twice the rate of human-written code is worth internalizing; audit whether your CI/CD pipelines have automated secret scanning enabled on AI-heavy repos before this statistic becomes your incident.
- **SOC/IR — Skip**
- **Leader — Plan:** If your engineering teams are adopting AI coding assistants, this report's doubling of credential exposure rates warrants establishing or tightening AI tool policies and mandatory secrets-scanning requirements this quarter before an exposed credential becomes a breach.
