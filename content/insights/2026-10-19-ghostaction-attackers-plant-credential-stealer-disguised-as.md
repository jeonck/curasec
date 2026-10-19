---
title: "GhostAction Expands Supply Chain Attack: Stealer Hidden in Fake Font Across 94 Repos"
date: 2026-10-19T17:27:24.131557+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["supply-chain", "github-actions", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/10/ghostaction-attackers-plant-credential.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Active supply chain campaign targeting GitHub repos via malicious Actions workflows and now fake font files; audit your GitHub Actions workflow dependencies for unexpected changes and scan repos you consume for suspicious binary assets in font or asset directories.
- **SOC/IR — Plan:** GhostAction is actively evolving TTPs—credential stealer delivery disguised as font files through CI/CD pipelines; build or tune detections for credential-theft behaviors originating from build runners and unusual outbound connections from CI environments, even before specific IOCs are published.
- **Leader — Learn:** GhostAction illustrates how supply chain attacks via open-source platforms are growing in sophistication; useful framing for board discussions on OSS risk posture, but no specific widely-used vendor breach or near-term regulatory deadline requires immediate leadership action.
