---
title: "Cursor breach led to malicious Claude Code extension in marketplace"
date: 2026-11-15T17:41:20.057634+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "ide-extension", "credential-theft"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/cursor-confirms-security-breach-led-to-malicious-claude-code-extension/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** If your developers use Cursor, immediately audit installed extensions and remove any unauthorized Claude Code extension; also review whether your environment uses Fireworks AI credentials that may have been exposed in the upstream breach.
- **SOC/IR — Act:** Sweep developer endpoints for the malicious Cursor extension and hunt for anomalous outbound activity from dev machines during the breach window; developer workstations with trojanized IDE extensions are a high-value pivot point into source code and credentials.
- **Leader — Act:** Determine whether your development teams use Cursor and brief them to check for the malicious extension; a supply-chain compromise through a popular AI coding tool is likely to generate customer and leadership questions about your software development security posture.
