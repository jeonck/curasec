---
title: "Placeholder domain 'third-party.com' now serves ClickFix malware"
date: 2026-09-24T15:49:46.689252+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["clickfix", "social-engineering", "supply-chain"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/placeholder-domain-used-in-dev-docs-now-serves-clickfix-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Audit your developer documentation, internal wikis, and code examples for placeholder domains that resolve to live addresses — 'third-party.com' is now actively malicious. This quarter, establish a doc review process to catch example domains before they reach users.
- **SOC/IR — Act:** Search proxy and DNS logs for connections to third-party.com; hunt for ClickFix-pattern PowerShell execution following fake Cloudflare CAPTCHA pages, particularly on developer workstations where traffic to doc-linked domains is expected and may slip past scrutiny.
- **Leader — Learn:** A subtle supply-chain-adjacent technique where expired or unclaimed placeholder domains in developer documentation become lure infrastructure — no immediate leadership action required, but useful context for developer-endpoint risk discussions.
