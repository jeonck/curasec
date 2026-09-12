---
title: "Florida DMV DAVID database breached via stolen police credentials"
date: 2026-09-12T14:04:45.501336+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["credential-theft", "data-breach", "government"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/florida-confirms-dmv-database-breached-via-stolen-police-account/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** No exploited software CVE here — the attack vector was stolen third-party credentials with privileged database access, a reminder to audit external-party access grants and enforce MFA on any federated or shared accounts that touch sensitive datastores.
- **SOC/IR — Learn:** No IOCs or ATT&CK-mapped TTPs are available, so there is nothing to hunt or tune on now; the breach pattern (compromised partner account → direct DB query) is worth filing as context for anomalous privileged-access hunting rules.
- **Leader — Learn:** This is a post-mortem lesson on third-party credential risk — law enforcement or partner organizations with standing database access can become an uncontrolled entry point; useful for reviewing your own partner-access inventory and attestation process.
