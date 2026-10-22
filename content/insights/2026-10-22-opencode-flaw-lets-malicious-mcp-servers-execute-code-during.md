---
title: "OpenCode AI agent flaw lets malicious MCP server run code on dev machines"
date: 2026-10-22T15:52:23.930402+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["ai-coding-tools", "mcp-security", "code-execution"]
cves: []
source: "https://thehackernews.com/2026/10/opencode-flaw-lets-malicious-mcp.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Developers using OpenCode on Windows or WSL should update to version 1.18.33; the vulnerability allows a compromised or rogue MCP server to execute code under the developer's credentials at sign-in. No KEV listing or public PoC reported, so patching on normal schedule is appropriate rather than emergency response.
- **SOC/IR — Learn:** This introduces a novel attack surface where AI coding agent tool integrations (MCP servers) can be used as a code execution vector against developer workstations; no IOCs, TTPs, or active exploitation reported yet, so no immediate detection work is warranted.
- **Leader — Skip**
