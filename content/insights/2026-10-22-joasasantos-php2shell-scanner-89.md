---
title: "php2shell-scanner: public recon tool for PHP core RCE CVEs"
date: 2026-10-22T15:52:23.930402+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["php", "rce", "vulnerability-scanner"]
cves: ["CVE-2026-109618", "CVE-2026-109619"]
source: "https://github.com/JoasASantos/php2shell-scanner"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Plan:** PHP core RCE with public PoC and now a trending mass-scanner lowers the bar for attackers to identify unpatched targets; neither CVE is in KEV and EPSS is low (0.05/0.06), but patch PHP to the fixed version this sprint before exploitation pressure rises.
- **SOC/IR — Plan:** The scanner performs subdomain recon and banner grabbing to fingerprint PHP versions — build or tune detections for high-rate HTTP requests probing PHP version banners or /phpinfo endpoints originating from external IPs.
- **Leader — Skip**
- **Signals:** CVE-2026-109618 — CISA KEV: not listed, EPSS 0.05, public PoC on GitHub, reported by 4 collected sources · CVE-2026-109619 — CISA KEV: not listed, EPSS 0.06, public PoC on GitHub, reported by 4 collected sources
