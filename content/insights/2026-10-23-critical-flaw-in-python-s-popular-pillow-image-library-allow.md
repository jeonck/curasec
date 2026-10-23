---
title: "Critical Pillow EPS Flaw Allows RCE via Crafted Image Filename"
date: 2026-10-23T15:44:28.729261+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["python", "rce", "supply-chain"]
cves: ["CVE-2026-112900"]
source: "https://thehackernews.com/2026/10/critical-flaw-in-pythons-popular-pillow.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Pillow is ubiquitous in Python web apps that accept image uploads; a public PoC exists on GitHub making exploitation straightforward. Patch Pillow to the fixed release immediately, or disable EPS/Ghostscript support via environment variable if a patch window is unavailable.
- **SOC/IR — Plan:** No active exploitation yet (EPSS 0.00, not in KEV), but the public PoC lowers the bar. Build or tune a detection for web-tier processes (Python/Gunicorn) spawning Ghostscript, which should not normally invoke child shells — flag any unexpected child process tree from gs/gswin.
- **Leader — Skip**
- **Signals:** CVE-2026-112900 — CISA KEV: not listed, EPSS 0.00, public PoC on GitHub
