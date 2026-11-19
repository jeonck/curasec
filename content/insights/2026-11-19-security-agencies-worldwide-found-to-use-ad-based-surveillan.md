---
title: "Citizen Lab: Global Security Agencies Exploit Ad-Tech for Surveillance"
date: 2026-11-19T19:29:03.442667+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["ad-tech-surveillance", "privacy", "threat-intelligence"]
cves: []
source: "https://citizenlab.ca/security-agencies-worldwide-found-to-use-ad-based-surveillance-system/"
source_name: "HN (security)"
status: "active"
---
- **Engineer — Learn:** Research confirms that ad SDKs embedded in apps can be weaponized as surveillance infrastructure; factor third-party ad SDK risk into your mobile/app supply-chain reviews, but no patch or config change is actionable today.
- **SOC/IR — Learn:** Citizen Lab's findings expand the threat model for data exfiltration via ad networks, but no IOCs or ATT&CK-mappable TTPs are surfaced in this item, so no detection work is immediately actionable.
- **Leader — Plan:** This research supports tightening mobile-device policy this quarter — specifically, restrict corporate-device apps that bundle broad ad SDKs for employees handling sensitive data, and add ad-network data brokers to your next vendor-risk review cycle.
