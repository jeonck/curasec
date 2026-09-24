---
title: "Malicious Terraform Providers Deliver Go Malware via HashiCorp Registry"
date: 2026-09-24T15:49:46.689252+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["supply-chain", "terraform", "go-malware"]
cves: []
source: "https://thehackernews.com/2026/09/attackers-use-malicious-terraform.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** First documented weaponization of the HashiCorp Terraform registry as a malware distribution vector directly affects IaC pipelines. Audit all Terraform provider lockfiles and go.sum entries for gocommunity-io/dockerd and the kreuzwenker-prefixed module, and check CI/CD artifact logs for downloads of either package.
- **SOC/IR — Plan:** No published IOCs or TTPs beyond package names, but this technique warrants building detection for anomalous Terraform provider fetches in CI/CD telemetry; add queries against build logs for downloads of the named providers and alert on new or unrecognized provider sources in IaC pipeline runs.
- **Leader — Learn:** This marks the first recorded use of HashiCorp's centralized registry as a malware delivery channel, expanding the trusted-tooling supply chain threat surface; useful context for updating third-party software sourcing policies and vendor risk discussions, but download counts are low and there is no systemic breach requiring immediate leadership action.
