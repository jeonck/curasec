---
title: "TanStack npm Supply Chain Attack Led to CrowdSec GitHub Repo Exfiltration"
date: 2026-09-19T14:22:25.332089+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Act"
tags: ["supply-chain", "npm", "github-breach"]
cves: []
source: "https://thehackernews.com/2026/09/crowdsec-says-tanstack-npm-attack-led.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** The TanStack npm supply chain attack in May stole credentials from developer machines; audit your lockfiles for malicious TanStack package versions from that window and rotate any npm tokens or GitHub credentials that may have been exposed. Also verify offboarding checklists immediately revoke GitHub org access upon employee departure.
- **SOC/IR — Plan:** This incident had roughly a 4-month dwell time before discovery; build or tune detections for bulk GitHub repository cloning events and unusual API access patterns from recently offboarded accounts — no specific IOCs are published yet to enable an immediate sweep.
- **Leader — Act:** CrowdSec, a security vendor, confirmed ~170 private repositories were exfiltrated; if your organization uses CrowdSec products, request an incident attestation to understand whether any shared intelligence or configurations were exposed. Separately, this breach stemmed from a failed offboarding — review your own access-revocation policy and confirm it mandates same-day removal of all VCS and cloud access.
