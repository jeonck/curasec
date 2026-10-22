---
title: "php_uploadprogress_guard: virtual patch for php2shell CVEs"
date: 2026-10-22T15:52:23.930402+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["php", "web-shell", "virtual-patch"]
cves: ["CVE-2026-109618", "CVE-2026-109619"]
source: "https://github.com/HOSTED-POWER/php_uploadprogress_guard"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Plan:** Public PoCs exist for CVE-2026-109618/109619 but EPSS is low (0.05/0.06) and neither is KEV-listed; if you run PHP across shared-hosting stacks (cPanel, DirectAdmin) where upgrading lags, evaluate this extension as a temporary mitigation while scheduling the official PHP engine update.
- **SOC/IR — Plan:** php2shell exploitation delivers web shells via the upload-progress path — with public PoCs now circulating, build or tune detections for anomalous PHP upload-progress requests and unexpected shell artifacts in web directories.
- **Leader — Skip**
- **Signals:** CVE-2026-109618 — CISA KEV: not listed, EPSS 0.05, public PoC on GitHub, reported by 4 collected sources · CVE-2026-109619 — CISA KEV: not listed, EPSS 0.06, public PoC on GitHub, reported by 4 collected sources
