---
title: "GitLab Issue Email Address Is a Credential That Can Push Code and Trigger CI"
date: 2026-09-24T15:49:46.689252+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["gitlab", "ci-cd", "credential-exposure"]
cves: []
source: "https://thehackernews.com/2026/09/a-leaked-gitlab-issue-email-address.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** If your team uses GitLab's email-to-issue feature, those per-project addresses are live credentials — audit whether any have appeared in screenshots, bug reports, logs, or Slack, and rotate them via GitLab profile settings; also evaluate whether to disable the feature organization-wide if it isn't actively used.
- **SOC/IR — Learn:** No exploitation evidence or IOCs, but this expands the CI/CD abuse surface worth knowing for future hunts — an attacker who obtains one of these addresses could trigger pipeline jobs without touching a keyboard in a way most SIEM rules wouldn't catch.
- **Leader — Skip**
