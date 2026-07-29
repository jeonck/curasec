---
title: "Compromised @joyfill npm Packages Deliver RAT on Import"
date: 2026-07-29T13:07:14.832066+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["supply-chain", "npm", "malware"]
cves: []
source: "https://thehackernews.com/2026/07/two-compromised-joyfill-npm-packages.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Supply-chain compromise with import-time execution is an immediate threat to any project pulling these beta versions; audit node_modules and lockfiles for @joyfill/layouts@0.1.2-2773.beta.0 and @joyfill/components@4.0.0-rc24-2773-beta.4, remove them, and inspect CI/CD build artifacts from affected hosts for signs of RAT persistence.
- **SOC/IR — Act:** The DEV#POPPER malware family has prior campaign IOCs — hunt for outbound connections and process spawns originating from npm install/build steps on developer workstations and CI runners; prioritize any host that ran builds pulling @joyfill packages since these beta versions were published.
- **Leader — Plan:** Confirm whether engineering teams use @joyfill beta packages and use this incident to validate that npm supply chain controls — lockfiles, dependency auditing, and private registry mirroring — are enforced across your development pipeline this quarter.
