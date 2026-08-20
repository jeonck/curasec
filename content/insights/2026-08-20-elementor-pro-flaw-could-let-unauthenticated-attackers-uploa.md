---
title: "Elementor Pro Unauthenticated File Upload Enables RCE (CVE-2026-32475)"
date: 2026-08-20T11:39:11.237527+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Skip"
tags: ["wordpress", "remote-code-execution", "file-upload"]
cves: ["CVE-2026-32475"]
source: "https://thehackernews.com/2026/08/elementor-pro-flaw-could-let.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** CVSS 9.0 with a public PoC on GitHub means opportunistic exploitation is imminent; update Elementor Pro to the latest patched release immediately and audit WordPress upload directories for any unexpected PHP files already dropped via the Forms module.
- **SOC/IR — Act:** A public PoC for unauthenticated RCE means mass scanning is likely underway; hunt for unauthorized PHP files in WordPress upload paths and review web server and WAF logs for suspicious POST requests targeting the Elementor Pro Forms endpoint since the disclosure date.
- **Leader — Skip**
- **Signals:** CVE-2026-32475 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
