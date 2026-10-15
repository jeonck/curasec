---
title: "Langflow Critical RCE CVE-2026-105740 Actively Exploited in the Wild"
date: 2026-10-15T15:35:13.586755+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["langflow", "rce", "ai-security"]
cves: ["CVE-2026-105740"]
source: "https://thehackernews.com/2026/10/langflows-critical-authenticated-rce.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Public PoC and 1,423 honeypot exploitation attempts confirm active in-the-wild attacks against Langflow (CVSS 9.9); if you run Langflow for AI workflow development, patch immediately or restrict access to authenticated users on trusted networks.
- **SOC/IR — Act:** Active exploitation campaign with over 1,400 observed attempts warrants an immediate sweep of internal and exposed Langflow instances for compromise indicators; hunt for unusual outbound connections or code execution from Langflow processes since the PoC became public.
- **Leader — Plan:** If your organization has AI/ML engineering teams building agentic workflows, confirm whether Langflow is in use and verify patching status — active exploitation is confirmed but the blast radius is limited to teams that have deployed this platform.
- **Signals:** CVE-2026-105740 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub
