---
title: "Compromised AsyncAPI npm Packages Deliver Multi-Stage Botnet Malware"
date: 2026-07-15T12:11:39.478598+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["supply-chain", "npm", "malware"]
cves: []
source: "https://thehackernews.com/2026/07/compromised-asyncapi-npm-packages.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Act:** Active supply-chain compromise with four named @asyncapi package versions confirmed by four independent security firms. Audit lockfiles and dependency manifests for @asyncapi/generator-helpers@1.1.1, @asyncapi/generator-components@0.7.1, @asyncapi/generator@3.3.1, and @asyncapi/specs v6.11.2/v6.11.2-alpha.1; pin to clean versions and re-run any build that pulled these.
- **SOC/IR — Act:** Multi-stage botnet loader distributed through CI/CD dependency chains means build infrastructure and developer machines are the compromise surface. Hunt for these specific package versions in npm install logs and artifact registries, and look for anomalous outbound connections from build runners or developer endpoints since the compromised versions' publish dates.
- **Leader — Plan:** Corroborated supply-chain compromise in a popular API-tooling namespace warrants directing engineering to complete a dependency audit this week; if these packages appear in shipped products, assess whether customer disclosure or SBOM updates are required under existing contractual or regulatory obligations.
