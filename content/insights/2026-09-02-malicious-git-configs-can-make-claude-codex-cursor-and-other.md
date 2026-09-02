---
title: "Malicious .git Configs Trigger Code Execution in AI Coding Agents"
date: 2026-09-02T15:05:08.783541+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["ai-coding-agents", "supply-chain", "code-execution"]
cves: []
source: "https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Four of the seven affected agents remain unpatched, making this an active exposure for any team whose developers clone untrusted repos while running AI coding assistants. Audit which agents (Claude Code, Codex CLI, Cursor, etc.) are in use, update those that have received patches, and enforce policy against running agents against repositories from untrusted sources until remaining fixes ship.
- **SOC/IR — Learn:** This research introduces a new attack class—git-config-triggered code execution via AI agent trust boundaries—that is worth understanding for future detection work on developer endpoints, but no IOCs, exploited campaigns, or mappable TTPs are published yet to act on immediately.
- **Leader — Plan:** With four tools still unpatched, any organization where developers use CLI AI coding agents carries uncontrolled supply-chain risk from malicious repository clones. This quarter, inventory which agents are deployed, confirm patched versions are standardized, and establish a policy on approved repositories before AI agent use.
