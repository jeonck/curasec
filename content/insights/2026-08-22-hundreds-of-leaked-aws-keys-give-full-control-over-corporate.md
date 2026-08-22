---
title: "9,300+ Leaked AWS Keys Still Active, Grant Full Account Control"
date: 2026-08-22T11:32:44.405318+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["aws", "credential-exposure", "cloud-security"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hundreds-of-leaked-aws-keys-give-full-control-over-corporate-accounts/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Still-valid exposed AWS keys require no exploitation sophistication — the credential is the exploit. Audit all active IAM access keys in your AWS accounts, cross-reference against the leaked dataset, rotate any keys created or last-used anomalously, and enforce least-privilege policies with automatic key rotation going forward.
- **SOC/IR — Act:** Active leaked credentials mean unauthorized access may already be occurring. Hunt CloudTrail logs since August 2022 for API calls from unexpected source IPs, new IAM user/role creation, or unusual resource provisioning that could indicate keys were already abused by third parties.
- **Leader — Act:** Hundreds of corporate AWS keys with full-account-control scope being publicly available for up to four years is a material risk requiring same-week action — confirm whether your organization's keys appear in the exposed set and direct engineering to complete a credential audit and rotation before end of week.
