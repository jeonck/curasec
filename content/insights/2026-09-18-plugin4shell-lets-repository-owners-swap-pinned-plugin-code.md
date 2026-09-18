---
title: "Plugin4Shell: Pinned Plugin Bypass Affects Four AI Coding Agents"
date: 2026-09-18T14:58:07.079452+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["ai-coding-agents", "supply-chain", "plugin-security"]
cves: []
source: "https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A pinned-version bypass in AI coding agents enables malicious plugin substitution via a controlled upstream repo — a direct supply-chain risk in CI/CD pipelines. Update Claude Code to ≥2.1.179 and OpenAI Codex to ≥0.146.0 immediately; audit all plugin sources across affected agents and restrict GitHub Copilot plugin use until a patch is confirmed.
- **SOC/IR — Plan:** No published IOCs or active exploitation reported, but this introduces a new class of AI coding agent supply-chain abuse worth covering. Build detections on anomalous plugin installation behavior and source-repository mismatches in CI/CD pipeline logs, prioritizing environments running unpatched Copilot.
- **Leader — Plan:** AI coding agents are broadly deployed in engineering orgs and this vulnerability lets a compromised upstream plugin repo silently inject malicious code even with pinned versions. Task the security team to inventory which AI coding agents are in use and confirm patch status — GitHub Copilot appears to lack a fix, warranting a risk assessment before the next sprint cycle.
