---
title: "JetBrains Cadence Breached via TeamCity Flaw; AWS Creds Extracted"
date: 2026-09-06T14:08:28.650854+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["teamcity", "supply-chain", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/09/attackers-breached-jetbrains-cadence.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** If you use JetBrains Cadence, immediately revoke and rotate all credentials and secrets used in Cadence executions; also patch any self-hosted TeamCity instances to eliminate the exploited critical vulnerability.
- **SOC/IR — Act:** If Cadence is in your environment, treat extracted AWS credentials as compromised and hunt for anomalous IAM activity or unexpected AWS API calls originating from CI/CD workloads since last month's breach window.
- **Leader — Act:** Confirm whether your organization uses JetBrains Cadence, request an incident attestation from JetBrains, and brief leadership on potential exposure of AWS credentials and CI/CD secrets before they read it elsewhere.
