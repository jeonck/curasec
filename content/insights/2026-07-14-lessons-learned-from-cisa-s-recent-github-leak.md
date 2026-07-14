---
title: "CISA Postmortem: Contractor AWS Keys Leaked to Public GitHub for 6 Months"
date: 2026-07-14T12:08:08.109802+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["secrets-management", "credential-leak", "postmortem"]
cves: []
source: "https://krebsonsecurity.com/2026/07/lessons-learned-from-cisas-recent-github-leak/"
source_name: "Krebs on Security"
status: "active"
---
- **Engineer — Plan:** This postmortem highlights systemic gaps in detecting committed credentials and contractor offboarding. Audit your GitHub org repos and CI config files for exposed secrets, enable GitHub Advanced Security secret scanning org-wide, and verify pre-commit hooks or equivalent controls are enforced across contractor-accessible repos.
- **SOC/IR — Learn:** CISA's documented response gaps — including the near-six-month detection delay — are worth absorbing when refining your own IR playbook for credential-exposure scenarios, but no IOCs or active exploitation are present to drive immediate hunt or detection work.
- **Leader — Plan:** A federal agency's own postmortem on contractor-driven credential exposure is a direct governance signal: this quarter, validate that your third-party access controls, contractor off-boarding procedures, and secrets-exposure detection capabilities don't share the same gaps CISA identified.
