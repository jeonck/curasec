---
title: "Hackers hijack Google domains after breaching ccTLD registries"
date: 2026-10-08T17:51:36.071186+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["dns-hijacking", "certificate-misissuance", "supply-chain"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-hijack-google-domains-after-breaching-cctld-registries/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Registry-level DNS tampering enabled unauthorized certificate issuance — audit DNS records and check Certificate Transparency logs (crt.sh) for any unexpected cert issuances on domains your org owns, especially in .gh/.as/.sl ccTLDs; confirm DNSSEC is enabled where possible.
- **SOC/IR — Act:** Active DNS hijacking via compromised registry operators is in progress — query CT logs for unexpected certificate issuances against your org's domains, and hunt for anomalous DNS record changes since early October 2026 across your monitored domain portfolio.
- **Leader — Plan:** Breach of ccTLD registry operators affecting multiple country-code TLDs warrants an inventory check — confirm whether your organization holds domains in .gh, .as, or .sl ccTLDs and request a DNS record integrity attestation from your registrar or domain management vendor.
