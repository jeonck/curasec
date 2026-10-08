---
title: "Tensorlake npm SDK v0.5.144 Compromised with Credential-Stealing Worm"
date: 2026-10-08T17:51:36.071186+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["supply-chain", "npm", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Confirmed supply-chain compromise: audit package-lock.json and yarn.lock across all repos for tensorlake@0.5.144, remove immediately if found, and rotate any credentials or secrets accessible during builds on affected systems.
- **SOC/IR — Act:** Active worm establishes persistence and phones home for remote code execution — sweep CI/CD runners and developer workstations that may have installed this version for anomalous outbound connections and new persistence artifacts since the package was published.
- **Leader — Plan:** Niche but confirmed supply-chain compromise with credential exfiltration; direct engineering to audit dependency manifests for tensorlake SDK usage this week and escalate to incident response if any instances are found.
