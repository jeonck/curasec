---
title: "Clop-Linked JSP Web Shell Targets PTC Windchill/FlexPLM for Extortion"
date: 2026-08-19T11:36:35.301683+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["web-shell", "clop-ransomware", "plm-security"]
cves: []
source: "https://thehackernews.com/2026/08/clop-linked-windchill-web-shell.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Clop-linked actors are actively exploiting a critical flaw in PTC Windchill and FlexPLM to deploy a purpose-built JSP web shell; if you run either platform, immediately audit PLM servers for rogue JSP files and apply the underlying critical patch.
- **SOC/IR — Act:** Active Clop-linked intrusion campaign targeting PLM servers with a web shell that harvests and decrypts credentials and maps vault contents — hunt for anomalous JSP execution and credential-access activity on Windchill/FlexPLM hosts, and review ReliaQuest's analysis for behavioral indicators.
- **Leader — Plan:** A Clop-affiliated extortion tool specifically engineered to steal engineering IP from PLM systems is a sector-specific risk for manufacturing, aerospace, and defense organizations; if Windchill or FlexPLM is in your environment or your supply chain, verify exposure and confirm vendor incident posture this quarter.
