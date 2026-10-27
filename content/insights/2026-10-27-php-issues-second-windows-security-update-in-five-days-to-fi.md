---
title: "PHP Windows packages patched for Brotli RCE flaw CVE-2026-111497"
date: 2026-10-27T16:34:51.683639+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["php", "rce", "supply-chain"]
cves: ["CVE-2026-111497"]
source: "https://thehackernews.com/2026/10/php-issues-second-windows-security.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** EPSS 0.55 plus a public GitHub PoC make this Act: update Windows PHP packages to the latest 8.2–8.5 builds immediately, and audit any application that enables cURL's CURLOPT_ENCODING (automatic Brotli decompression), since that is the exploitable path.
- **SOC/IR — Plan:** No active exploitation or KEV listing yet, but a public PoC and high EPSS warrant building a detection for anomalous PHP-CGI/FastCGI process behavior on Windows hosts; queue a hunt for known PoC signatures once they stabilize.
- **Leader — Skip**
- **Signals:** CVE-2026-111497 — CISA KEV: not listed, EPSS 0.55, public PoC on GitHub
