---
title: "Critical Unauthenticated RCE in Bifrost AI Gateway (CVE-2026-90898)"
date: 2026-09-24T15:49:46.689252+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["rce", "ai-infrastructure", "open-source"]
cves: ["CVE-2026-90898"]
source: "https://thehackernews.com/2026/09/critical-bifrost-ai-gateway-flaw-lets.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Public PoC exists for a CVSS 9.8 unauthenticated RCE affecting all Bifrost HTTP transport versions before 2.1.0 — if you run this AI gateway in any environment, patch to 2.1.0 immediately and audit for signs of exploitation in management endpoint logs.
- **SOC/IR — Plan:** No active exploitation signals yet (EPSS 0.01, not KEV-listed), but a public PoC raises near-term risk — if Bifrost appears in your estate, write a detection for unauthenticated HTTP requests to its management interface before campaigns emerge.
- **Leader — Skip**
- **Signals:** CVE-2026-90898 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub
