---
title: "AI Coding Agents Leaked 13,000 Internal Images to Public GitHub Repos"
date: 2026-09-30T16:48:49.184501+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["ai-coding-agents", "data-exposure", "github"]
cves: []
source: "https://thehackernews.com/2026/09/ai-coding-agents-exposed-13000-internal.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** AI coding agents in your dev workflow may be silently pushing screenshots—including sensitive internal data—to public GitHub repos under personal developer accounts. Audit GitHub for AI-agent-created image artifacts now, and restrict AI agent configurations to prevent writing to public repositories.
- **SOC/IR — Act:** Over 13,000 internal images from 300+ orgs are already publicly reachable on GitHub. Hunt for unexpected image file commits (PNG/JPEG) in developer personal repos linked to your organization's accounts, and check whether any internal-origin images are indexed publicly.
- **Leader — Act:** Customer billing records are confirmed among the exposed data, implicating potential GDPR/SEC disclosure obligations. This week, confirm whether your organization is among the 300+ affected by querying your security team for AI agent GitHub activity, and engage legal on exposure scope before regulators or customers surface it first.
