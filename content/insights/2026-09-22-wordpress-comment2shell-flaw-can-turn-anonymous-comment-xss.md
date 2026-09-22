---
title: "WordPress Comment2Shell CVE-2026-93485: Anonymous XSS to RCE via Admin"
date: 2026-09-22T15:30:54.753130+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["wordpress", "xss-to-rce", "supply-chain"]
cves: ["CVE-2026-93485"]
source: "https://thehackernews.com/2026/09/wordpress-comment2shell-flaw-can-turn.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC on GitHub makes exploitation practical despite a low EPSS score; the anonymous-commenter-to-admin-RCE chain is severe. Patch WordPress core to version 7.1.1 immediately across all managed sites.
- **SOC/IR — Plan:** No confirmed in-the-wild exploitation yet, but the public PoC makes detection work urgent this quarter. Build rules to flag suspicious JavaScript payloads in WordPress comment submissions and unexpected server-side execution correlated with admin page visits.
- **Leader — Skip**
- **Signals:** CVE-2026-93485 — CISA KEV: not listed, EPSS 0.00, public PoC on GitHub
