---
title: "GoldenEyeDog Subgroup CylindricalCanine Tied to DigiCert Breach"
date: 2026-07-18T11:51:11.203777+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Act"
tags: ["threat-actor", "supply-chain", "code-signing"]
cves: []
source: "https://thehackernews.com/2026/07/goldeneyedog-subgroup-linked-to.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Plan:** Code-signing certificate theft from a major CA is a trust-chain risk: audit any DigiCert-issued code-signing certificates in your CI/CD pipeline or software distribution path, and confirm with DigiCert whether your certificates were in scope for revocation.
- **SOC/IR — Learn:** Attribution of CylindricalCanine as a GoldenEyeDog subgroup adds context to actor tracking, but the summary is too thin to yield IOCs or mappable TTPs for detection work — monitor for a fuller technical disclosure before building hunts.
- **Leader — Act:** A confirmed breach at DigiCert involving stolen code-signing certificates is a vendor risk event: confirm whether your organization uses DigiCert for code signing or certificate services, and request DigiCert's formal incident attestation and revocation scope this week.
