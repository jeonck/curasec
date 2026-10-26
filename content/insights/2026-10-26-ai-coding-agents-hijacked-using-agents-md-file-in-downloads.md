---
title: "AI coding agents hijacked via malicious AGENTS.md in Downloads folder"
date: 2026-10-26T17:20:31.892638+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["prompt-injection", "ai-coding-agents", "supply-chain"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/ai-coding-agents-hijacked-using-agentsmd-file-in-downloads-folder/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** A real-world case of indirect prompt injection: a malicious AGENTS.md file in a Downloads folder redirected an AI coding agent to install a rogue npm package. Audit your system for unexpected AGENTS.md (or similar instruction) files in user-accessible directories, and restrict your AI coding agent's trusted file-read scope to the project root.
- **SOC/IR — Plan:** This establishes a new TTP: adversaries plant instruction files (AGENTS.md) in directories that AI coding agents scan, triggering unauthorized package installs. Build a hunt for AGENTS.md or equivalent agent-config files outside expected project roots, and add detections for anomalous package manager invocations spawned by AI agent processes.
- **Leader — Plan:** If your engineering org uses AI coding agents (Claude Code, Copilot, Cursor, etc.), this attack class — poisoning agent instruction files to hijack developer workflows — warrants a policy before it matures further; define which directories agents may trust for instruction files and require developer awareness training this quarter.
