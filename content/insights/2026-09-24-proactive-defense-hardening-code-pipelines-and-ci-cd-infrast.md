---
title: "Google TI Blueprint: Hardening CI/CD Pipelines Against Active Supply-Chain TTPs"
date: 2026-09-24T15:49:46.689252+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["ci-cd-security", "supply-chain", "github-actions"]
cves: []
source: "https://cloud.google.com/blog/topics/threat-intelligence/hardening-code-pipelines-and-ci-cd-infrastructure/"
source_name: "Google Threat Intelligence"
status: "active"
---
- **Engineer — Plan:** Covers actively exploited vectors — OIDC token extraction, GitHub Actions cache poisoning, and mutable action tag hijacking — directly relevant to any team running modern pipelines; this quarter, pin all Action references to full commit SHAs, scope OIDC tokens to minimum claims per job, and audit build cache configurations for injection risk.
- **SOC/IR — Plan:** The TTPs described (pipeline cache poisoning, OIDC token exfiltration, compromised scan tools executing in CI) map to credential-access and supply-chain-compromise ATT&CK techniques with a growing log surface; prioritize collecting GitHub Actions audit logs into SIEM and build detections for anomalous OIDC token issuance or unexpected cache write events.
- **Leader — Learn:** Establishes that sophisticated actors are systematically targeting engineering toolchains — useful context for supply chain risk conversations with auditors or customers, but no specific vendor breach or regulatory deadline requiring immediate leadership action.
