---
title: "FakeGit Campaign: 7,600 Malicious GitHub Repos Deliver SmartLoader Malware"
date: 2026-07-21T12:43:35.631021+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["supply-chain", "malware", "github"]
cves: []
source: "https://thehackernews.com/2026/07/fakegit-campaign-uses-7600-github.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active campaign targeting developers who clone AI tools and MCP server repos from GitHub; audit recent GitHub clone activity and ZIP downloads on developer and CI/CD systems for SmartLoader indicators, and remove any untrusted AI/MCP repos from your dependency chain.
- **SOC/IR — Act:** Ongoing SmartLoader delivery campaign through GitHub social engineering targeting developer workstations; hunt for suspicious ZIP extraction followed by execution artifacts on developer endpoints, and query EDR for SmartLoader process lineage since the campaign is active.
- **Leader — Plan:** Scale and targeting of developer tooling (7,600 repos, AI/MCP lures) makes this a supply-chain risk to the development environment; engage engineering leads this quarter on vetting controls for GitHub-sourced AI components before broader adoption.
