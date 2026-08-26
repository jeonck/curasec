---
title: "Threat actors abuse npm mirrors to host Cloudflare CAPTCHA phishing pages"
date: 2026-08-26T11:42:13.540622+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["supply-chain", "phishing", "npm"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-abuse-npm-mirrors-to-host-phishing-redirect-pages/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Learn:** This highlights npm and its mirrors being misused as hosting infrastructure for phishing redirects — not a package-level supply-chain attack, but a reminder that npm CDN URLs can surface malicious HTML content. No patch or config change needed today; worth noting if internal tooling renders or fetches npm-hosted content for users.
- **SOC/IR — Learn:** A novel phishing delivery technique using trusted npm mirror domains as redirect hosts; without specific IOCs in this report, there is no immediate hunt to run, but analysts should track for follow-on reporting with domains or URLs to add to proxy/DNS blocklists.
- **Leader — Skip**
