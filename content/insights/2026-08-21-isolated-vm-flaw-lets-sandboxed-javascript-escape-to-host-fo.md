---
title: "isolated-vm Sandbox Escape Flaw Enables Host RCE in All Versions ≤7.0.0"
date: 2026-08-21T11:38:25.806134+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["sandbox-escape", "javascript", "rce"]
cves: []
source: "https://thehackernews.com/2026/08/isolated-vm-flaw-lets-sandboxed.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Any Node.js service using isolated-vm to run untrusted code (plugins, user-submitted scripts, multi-tenant eval) is exposed to host RCE; no public PoC or KEV listing yet, but the impact ceiling is high — audit your dependency tree and upgrade isolated-vm to a version above 7.0.0 this sprint.
- **SOC/IR — Skip**
- **Leader — Skip**
