---
title: "Trojanized Claude Code Extension on Cursor Traced to Stolen Fireworks AI Key"
date: 2026-11-15T17:41:20.057634+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "ai-tools", "extension-compromise"]
cves: []
source: "https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** If your team uses the Claude Code extension on Cursor, treat endpoints where it was installed as potentially compromised; audit those machines for credential theft or backdoor artifacts and confirm you are running the clean replacement version.
- **SOC/IR — Act:** Identify all developer endpoints in your estate that had the Claude Code Cursor extension installed during the compromise window, then hunt for post-exploitation activity (credential access, lateral movement, C2 beaconing) originating from those hosts.
- **Leader — Act:** Determine whether your engineering team uses Cursor with the Claude Code extension; if so, assess potential credential and source-code exposure, and brief leadership given the supply-chain nature of the incident — a third-party AI vendor breach (Fireworks AI) cascaded into a trojanized developer tool.
