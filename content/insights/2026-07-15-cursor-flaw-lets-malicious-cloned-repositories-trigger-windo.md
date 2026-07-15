---
title: "Cursor IDE on Windows auto-executes git.exe found in cloned repo root"
date: 2026-07-15T12:11:39.478598+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["ide-vulnerability", "code-execution", "supply-chain"]
cves: []
source: "https://thehackernews.com/2026/07/cursor-flaw-lets-malicious-cloned.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Any developer who opens an untrusted repo in Cursor on Windows is at risk of credential theft (SSH keys, cloud tokens) with no user interaction required — the attack path is fully described, making it practically exploitable now. Update Cursor to the patched version immediately; until confirmed patched, audit recently cloned project directories for unexpected git.exe files and avoid opening untrusted repos in Cursor on Windows.
- **SOC/IR — Plan:** No active campaign IOCs are reported, but the technique is clear: build a detection for Cursor (or any IDE process) spawning child processes from non-standard project root paths, specifically hunting git.exe executions outside of installed VCS tool directories on Windows endpoints.
- **Leader — Plan:** Cursor is widely adopted among developer teams; this flaw enables silent credential and source-code compromise via a simple repo-clone workflow. Circulate a developer advisory this week, confirm vendor patch availability, and consider a temporary policy restricting Cursor on Windows for repos from untrusted sources until remediated.
