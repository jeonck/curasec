---
title: "Malicious File Tricks AI Coding Agent Into Installing npm Malware"
date: 2026-10-26T17:20:31.892638+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["prompt-injection", "ai-coding-agents", "supply-chain"]
cves: []
source: "https://thehackernews.com/2026/10/malicious-file-in-downloads-folder.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active prompt-injection technique caught targeting real developer machines: restrict AI coding agents to project directories only and disable auto-execution of package-install commands to eliminate this ambient-file attack surface.
- **SOC/IR — Plan:** New TTP worth covering: build detections for package manager processes (npm/pip/etc.) spawned as child processes of AI coding agent binaries, especially when triggered outside expected project paths.
- **Leader — Plan:** AI coding agents in your developer toolchain now represent a prompt-injection risk from ambient files; establish a policy governing agent filesystem scope and command permissions before an undetected attempt succeeds.
