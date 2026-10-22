---
title: "Critical GitLab Unauthenticated RCE Affects All Releases Since 2014"
date: 2026-10-22T15:52:23.930402+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Plan"
tags: ["gitlab", "rce", "critical-vulnerability"]
cves: []
source: "https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** If you run self-managed GitLab, apply the October 21 release immediately — the October 12 patch only covered 19.2+ and left older versions fully exposed to unauthenticated RCE. No KEV or public PoC is confirmed yet, but CVSS 10.0 with universal version coverage warrants patching ahead of your normal window.
- **SOC/IR — Skip**
- **Leader — Plan:** Confirm your engineering team has applied the October 21 GitLab patch, not just the October 12 one — a widespread false sense of being patched exists for self-managed deployments, and unauthenticated RCE on source-code infrastructure would be a material incident if exploited.
