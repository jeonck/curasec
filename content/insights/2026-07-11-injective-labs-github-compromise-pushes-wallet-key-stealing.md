---
title: "Injective Labs GitHub Compromise Plants Wallet-Stealing npm Package"
date: 2026-07-11T11:49:48.413664+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["supply-chain", "npm", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/07/injective-labs-github-compromise-pushes.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Confirmed supply-chain attack: audit all dependency trees and package-lock files for @injectivelabs/sdk-ts@1.20.21; if found in any build artifact or runtime environment, treat wallet private keys and seed phrases as compromised and rotate immediately.
- **SOC/IR — Act:** Sweep CI/CD build logs, container image layers, and package manifests across all repositories for @injectivelabs/sdk-ts version 1.20.21; any positive hit should trigger an incident investigation for outbound exfiltration from build environments.
- **Leader — Learn:** A confirmed GitHub-to-npm supply-chain attack targeting crypto wallet credentials; worth referencing in supply-chain security policy discussions, and escalate to Act if the organization has products or vendors with Web3/DeFi dependencies.
