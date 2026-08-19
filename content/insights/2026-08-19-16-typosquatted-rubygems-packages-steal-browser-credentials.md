---
title: "16 Typosquatted RubyGems Packages Deploy StubMaker Info-Stealer"
date: 2026-08-19T11:36:35.301683+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["supply-chain", "rubygems", "info-stealer"]
cves: []
source: "https://thehackernews.com/2026/08/16-typosquatted-rubygems-packages-steal.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active malicious packages in a public registry represent a live supply-chain threat. Audit all Gemfile.lock files and CI build logs for the named packages (ubnuler, ubnlder, ri18nr, reaker, rakier, orakw, joxn); rotate browser credentials and secrets from any Windows developer or runner machines where matches are found.
- **SOC/IR — Act:** Sweep Windows developer workstations for StubMaker stealer artifacts and search CI/CD build logs for gem install activity referencing the named packages since August 15, 2026; focus on credential and crypto wallet exfiltration indicators on affected hosts.
- **Leader — Plan:** Confirm Ruby usage across engineering teams and verify that current dependency scanning controls would detect typosquatted packages before they reach production or developer machines; this campaign is a concrete prompt to close any gap in software supply chain policy this quarter.
