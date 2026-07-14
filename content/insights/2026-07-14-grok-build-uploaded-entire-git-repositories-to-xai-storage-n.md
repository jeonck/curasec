---
title: "Grok Build CLI Silently Uploaded Full Git Repos to xAI Cloud Storage"
date: 2026-07-14T12:08:08.109802+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Act"
tags: ["ai-coding-tools", "data-exfiltration", "supply-chain"]
cves: []
source: "https://thehackernews.com/2026/07/grok-build-uploads-entire-git.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Any developer who ran Grok Build (≤0.2.93) on a repo should assume the full commit history — including historically committed secrets — was sent to xAI-controlled cloud storage. Immediately stop using the tool, audit exposed repos for credentials or sensitive data, and rotate any secrets that ever touched those repos' history.
- **SOC/IR — Plan:** If developers in your org use Grok Build, build a detection for large outbound uploads (git bundle format) from developer workstations to external cloud storage; review DLP or proxy logs for historical hits against GCS endpoints associated with xAI before this was publicized.
- **Leader — Act:** Determine this week whether any developers have used Grok Build, since full repo history — potentially including IP, credentials, or regulated data — may have been exfiltrated to xAI infrastructure; if exposure is confirmed, assess notification obligations and request a data-handling statement from xAI.
