---
title: "Claude Code & Gemini CLI Default Configs Expose CI Secrets via GitHub Issues"
date: 2026-08-07T11:54:55.232717+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["prompt-injection", "ci-cd", "ai-coding-agents"]
cves: []
source: "https://thehackernews.com/2026/08/claude-code-and-gemini-cli-flaws-let.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** If your team runs Claude Code or Gemini CLI in CI pipelines under vendor-default configuration, an unprivileged GitHub issue can reach your runner and exfiltrate CI secrets — audit all AI agent CI integrations now, restrict what secrets are scoped to those runners, and disable issue-triggered agent workflows until hardened configurations are documented.
- **SOC/IR — Plan:** This Black Hat presentation defines a new TTP category — prompt injection via issue trackers targeting AI coding-agent CI workflows — worth building detections for; plan to monitor for anomalous CI runner invocations originating from issue events and unexpected secret-access patterns in pipeline logs.
- **Leader — Plan:** Default configurations of AI coding agents from major vendors expose CI secrets to anyone who can open a GitHub issue — assess whether engineering teams have deployed these tools in CI/CD pipelines this quarter and establish an approval policy for AI agent access to production secrets before adoption widens.
