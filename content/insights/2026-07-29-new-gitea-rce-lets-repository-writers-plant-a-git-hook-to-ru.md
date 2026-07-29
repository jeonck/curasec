---
title: "Gitea RCE (CVE-2026-60004): Write Access Enables Git Hook Shell Exec"
date: 2026-07-29T13:07:14.832066+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["rce", "supply-chain", "gitea"]
cves: ["CVE-2026-60004"]
source: "https://thehackernews.com/2026/07/new-gitea-rce-lets-repository-writers.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Any authenticated repo contributor can plant a malicious Git hook and execute arbitrary commands as the Gitea service account — a very low exploitation bar with a public PoC already on GitHub. Upgrade all Gitea instances from 1.17–1.27.0 to 1.27.1 immediately.
- **SOC/IR — Plan:** No KEV listing or confirmed in-the-wild exploitation yet, but the public PoC makes opportunistic attacks likely soon. Build a detection for unexpected process spawning from the Gitea service account and audit recent git hook creation events on any self-hosted Gitea instances.
- **Leader — Plan:** Self-hosted Gitea instances are common in engineering orgs and often sit inside CI/CD pipelines where a service-account RCE could enable supply-chain compromise. Confirm whether internal Gitea deployments exist and verify they are on the patching roadmap before the public PoC drives active exploitation.
- **Signals:** CVE-2026-60004 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
