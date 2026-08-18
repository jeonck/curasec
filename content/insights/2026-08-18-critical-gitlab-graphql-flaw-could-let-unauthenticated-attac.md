---
title: "Critical GitLab GraphQL Flaw Lets Unauthenticated Attackers Delete Projects"
date: 2026-08-18T11:37:25.033598+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["gitlab", "graphql", "critical-vulnerability"]
cves: ["CVE-2026-19478"]
source: "https://thehackernews.com/2026/08/critical-gitlab-graphql-flaw-could-let.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC on GitHub for a CVSS 9.4 unauthenticated flaw sharply raises exploitation risk even without KEV listing; patch GitLab CE/EE to the vendor's latest patched release this week and verify no public GraphQL endpoints are exposed without authentication.
- **SOC/IR — Act:** With a public PoC already circulating, hunt for unauthenticated GraphQL mutation requests targeting GitLab's project or user-data endpoints, and alert on anomalous project deletion or modification events since the vulnerability disclosure date.
- **Leader — Plan:** Confirm whether the organization runs self-hosted GitLab and ensure engineering has a same-week patching commitment; unauthorized source-code deletion or tampering carries supply-chain and business-continuity implications worth a brief status check with the team.
- **Signals:** CVE-2026-19478 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
