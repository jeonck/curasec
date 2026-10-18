---
title: "ConnectWise Cloud Backup breach compromises M365 tenants via app identities"
date: 2026-10-18T14:33:13.167038+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain-attack", "microsoft-365", "connectwise"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-breach-microsoft-365-tenants-via-connectwise-supply-chain-attack/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Organizations using ConnectWise Cloud Backup (formerly SkyKick) should immediately audit M365 OAuth application permissions and service principal activity for unauthorized delegated access; revoke any ConnectWise-related app registrations until the vendor confirms scope and remediation.
- **SOC/IR — Act:** Hunt M365 unified audit logs and Entra ID sign-in logs for anomalous OAuth app consent events or application identity authentications tied to ConnectWise/SkyKick since the compromise window; treat impacted tenants as assume-breach and sweep for mailbox rule creation, exfiltration signals, and new delegated permissions.
- **Leader — Act:** Confirm this week whether your organization or your MSP uses ConnectWise Cloud Backup, then request ConnectWise's incident report and attestation of scope; assess whether compromised M365 tenant data triggers disclosure obligations under SEC, GDPR, or applicable state rules.
