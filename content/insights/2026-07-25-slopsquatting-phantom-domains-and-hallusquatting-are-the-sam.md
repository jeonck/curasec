---
title: "AI Hallucinated Package Names Enable Supply-Chain Squatting Attacks"
date: 2026-07-25T12:08:50.257932+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["supply-chain", "ai-security", "dependency-management"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/slopsquatting-phantom-domains-and-hallusquatting-are-the-same-ai-attack/"
source_name: "BleepingComputer"
status: "archived"
---
- **Engineer — Plan:** If your team uses AI coding assistants to generate dependency names or package imports, audit your pipeline for pre-fetch verification steps that confirm packages exist before installation; add a governed allowlist or lockfile discipline to block hallucinated names from resolving to malicious registries.
- **SOC/IR — Learn:** Understanding that AI agents can introduce malicious packages via hallucinated names expands the threat model for build-pipeline anomaly detection, but no IOCs or active campaign details are present to act on now.
- **Leader — Plan:** If your engineering teams use AI coding assistants, evaluate whether your software supply-chain policy requires dependency verification controls that cover AI-generated package references — this is a governance gap worth closing this quarter.
