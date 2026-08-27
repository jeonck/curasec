---
title: "TeamCity On-Premises Critical RCE CVE-2026-63077 (CVSS 9.8)"
date: 2026-07-28T13:01:43.287328+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["ci-cd", "rce", "critical-vulnerability"]
cves: ["CVE-2026-63077"]
source: "https://thehackernews.com/2026/07/critical-teamcity-flaw-could-let.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Act:** A public PoC on GitHub combined with a CVSS 9.8 unauthenticated RCE makes exploitation imminent — patch all on-premises TeamCity instances to 2025.11.7 or 2026.1.3 immediately; Cloud instances are already remediated.
- **SOC/IR — Act:** With a public PoC now available, begin hunting for unauthenticated requests to TeamCity build/run endpoints and review build agent logs for unexpected OS command execution patterns since the PoC publication date.
- **Leader — Plan:** Confirm whether your organization runs TeamCity On-Premises and verify the engineering team has prioritized emergency patching this week — a compromise of CI/CD pipelines carries supply-chain risk that could generate customer or board questions if exploitation is later confirmed.
- **Signals:** CVE-2026-63077 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
