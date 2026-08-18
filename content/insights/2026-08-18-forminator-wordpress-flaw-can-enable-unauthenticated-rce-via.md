---
title: "Forminator WordPress Plugin Critical RCE via Unauthenticated File Upload"
date: 2026-08-18T11:37:25.033598+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["wordpress", "rce", "cve"]
cves: ["CVE-2026-15748"]
source: "https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC exists for this unauthenticated file upload RCE (CVSS 9.8) affecting 600,000+ WordPress installs; update Forminator Forms to the patched version immediately and verify no malicious PHP files were uploaded to wp-content directories.
- **SOC/IR — Plan:** With a public PoC available, exploitation attempts are likely imminent; build or tune WAF/SIEM rules to detect unauthenticated multipart file upload requests to Forminator endpoints and alert on unexpected PHP file creation under wp-content.
- **Leader — Skip**
- **Signals:** CVE-2026-15748 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
