---
title: "MemTensor npm/PyPI Packages Compromised to Deliver sckit Credential Stealer"
date: 2026-09-23T15:27:03.663698+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["supply-chain", "credential-theft", "package-manager"]
cves: []
source: "https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Multi-source corroboration (Aikido, SafeDep, Socket, StepSecurity) of an active supply-chain compromise in npm and PyPI — a direct Act signal per channel criteria. Audit your dependency trees for @memtensor/memos-cloud-openclaw-plugin and any related MemTensor packages; remove or pin away from affected versions and rotate credentials on any systems where compromised versions were installed or executed.
- **SOC/IR — Act:** Active credential-stealing implant with cross-platform reach on developer and CI/CD systems warrants an immediate sweep. Hunt for sckit process artifacts and anomalous outbound connections from build environments and developer endpoints since the affected package versions were published; prioritize Linux and macOS systems alongside Windows given the cross-platform Go implant.
- **Leader — Plan:** A corroborated supply-chain compromise delivering a credential stealer could expose internal secrets or customer data if engineering teams pulled the affected packages. Confirm whether MemTensor packages appear in any internal dependency inventories and request a scope assessment from your engineering leads this week before this surfaces as a customer security question.
