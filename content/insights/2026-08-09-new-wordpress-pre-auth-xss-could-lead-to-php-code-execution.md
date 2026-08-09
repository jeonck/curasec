---
title: "WordPress Pre-Auth XSS (CVE-2026-64638) Chains to PHP RCE"
date: 2026-08-09T11:41:42.823801+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["wordpress", "xss", "rce"]
cves: ["CVE-2026-64638"]
source: "https://thehackernews.com/2026/08/new-wordpress-pre-auth-xss-could-lead.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Public PoC exists on GitHub for a flaw affecting every WordPress version; update WordPress core to the patched release immediately, as the chain to server-side PHP execution is demonstrated even though it requires an admin to visit an attacker page.
- **SOC/IR — Plan:** With a public PoC but EPSS of 0.01 and no KEV listing, active exploitation is not yet confirmed; build or tune a detection for anomalous reflected XSS patterns hitting the WordPress login endpoint and alert on unexpected admin-session activity following external link clicks.
- **Leader — Skip**
- **Signals:** CVE-2026-64638 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub
