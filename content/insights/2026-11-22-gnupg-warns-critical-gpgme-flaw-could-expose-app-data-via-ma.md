---
title: "Critical GPGME Memory Bug Exposes App Data via Malicious OpenPGP Keys"
date: 2026-11-22T16:05:35.915127+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["gpgme", "memory-corruption", "cve"]
cves: ["CVE-2026-129975"]
source: "https://thehackernews.com/2026/11/gnupg-warns-critical-gpgme-flaw-could.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Public PoC on GitHub raises immediate exploitation risk; any application using GPGME before 2.3.0 for key import/processing is exposed. Upgrade GPGME to version 2.3.0 across all systems and audit CI/CD pipelines, email tooling, or package signing workflows that call the library.
- **SOC/IR — Skip**
- **Leader — Skip**
- **Signals:** CVE-2026-129975 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
