---
title: "Fake LastPass GitHub repos distribute new Rapuncel infostealer"
date: 2026-09-19T14:22:25.332089+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["infostealer", "supply-chain", "social-engineering"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/fake-lastpass-authenticator-github-repos-push-new-rapuncel-infostealer/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Add LastPass Authenticator and similar impersonation repos to your developer guidance; audit internal wikis and Slack channels for links to unofficial GitHub repos distributing security tools, and remind teams to verify publisher identity before cloning auth-related software.
- **SOC/IR — Plan:** Build or tune detections for Rapuncel infostealer behaviors once IOCs are published; in the meantime, hunt for developer endpoints that recently cloned security-tool repos from unverified GitHub accounts, as credential theft from dev machines is a high-value pivot.
- **Leader — Learn:** This campaign illustrates ongoing abuse of developer trust in open-source platforms; useful context for security awareness program updates and vendor-tool procurement policies, but no immediate leadership action required.
