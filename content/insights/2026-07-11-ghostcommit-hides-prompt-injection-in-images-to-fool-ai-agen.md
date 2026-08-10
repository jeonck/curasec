---
title: "Ghostcommit: image-hidden prompt injection fools AI code review agents"
date: 2026-07-11T11:49:48.413664+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["prompt-injection", "ai-agents", "supply-chain"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/"
source_name: "BleepingComputer"
status: "archived"
---
- **Engineer — Plan:** Research-grade but practical: any AI coding agent with access to .env or secrets files is a potential exfiltration path via a malicious image in a PR. Audit what filesystem scope your AI code-review agents hold, and restrict or deny access to credential files and secret stores.
- **SOC/IR — Learn:** Novel TTP — prompt injection embedded in images bypasses AI reviewers that never inspect image content, then coerces coding agents into exfiltrating secrets. No active exploitation or IOCs reported; file for future detection work around anomalous AI-agent file reads.
- **Leader — Plan:** Demonstrates that AI coding-agent tools carry unchecked secret-exfiltration risk through a non-obvious vector. Before broader AI agent adoption, establish a policy governing what repository paths and credentials these tools may access, and confirm existing vendor tools have equivalent controls.
