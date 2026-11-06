---
title: "Malicious Extensions Can Abuse Claude Dispatch for RCE on Desktop"
date: 2026-11-06T17:55:59.437458+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["browser-extension", "remote-code-execution", "ai-tooling"]
cves: []
source: "https://thehackernews.com/2026/11/malicious-browser-extensions-could-use.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Engineers running Claude Desktop with Dispatch enabled are exposed to a still-unpatched code-execution path via malicious browser extensions that script claude.ai; audit whether Dispatch is enabled in your Claude Desktop config and disable it until Anthropic ships a fix.
- **SOC/IR — Learn:** Novel attack chain — malicious extension scripts claude.ai, which triggers Dispatch to execute code on the paired Claude Desktop — is worth understanding as AI tool adoption grows, but no IOCs or detection signatures are available yet to operationalize.
- **Leader — Skip**
