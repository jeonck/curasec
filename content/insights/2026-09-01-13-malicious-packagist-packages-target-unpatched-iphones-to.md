---
title: "13 Malicious Packagist Packages Deploy iOS Spyware via JS Injection"
date: 2026-09-01T15:28:52.066055+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["supply-chain", "packagist", "ios-spyware"]
cves: []
source: "https://thehackernews.com/2026/09/13-malicious-packagist-packages-target.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Packagist supply-chain compromise is relevant to any team running PHP/Composer-based web properties; audit your Composer dependency tree against the 13 named packages and enable automated SCA scanning in CI to catch future malicious packages.
- **SOC/IR — Learn:** The attack chain — trojanized Packagist packages injecting JavaScript that fingerprints and exploits unpatched iOS visitors — is a useful TTP reference, but no IOCs or SIEM-ready indicators are provided, making immediate detection work impractical.
- **Leader — Skip**
