---
title: "BdThemes Supply Chain Attack Creates Rogue WordPress Admin Accounts"
date: 2026-08-11T11:54:43.298939+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["supply-chain", "wordpress", "web-security"]
cves: []
source: "https://thehackernews.com/2026/08/bdthemes-supply-chain-attack-poisons.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active supply chain compromise affecting BdThemes WordPress plugins meets the Act threshold even without formal enrichment signals — audit all WordPress installations for BdThemes plugins and check admin user lists for unauthorized accounts created during the compromise window.
- **SOC/IR — Act:** The attack surface is concrete: hunt for unexpected WordPress administrator account creation events across managed sites, correlating with BdThemes plugin presence to identify compromised instances.
- **Leader — Plan:** Add WordPress plugin vendor risk to your third-party/supply chain review process; if BdThemes plugins are in use anywhere in the organization, confirm with responsible teams that no rogue admins were introduced.
