---
title: "24 npm Packages Abuse unpkg CDN to Host ClickFix Phishing Pages"
date: 2026-08-26T11:42:13.540622+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["phishing", "npm", "supply-chain"]
cves: []
source: "https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Novel abuse of unpkg CDN as free phishing infrastructure — developers who install the packages are not the target, but this technique shows how legitimate CDN reputation can carry malicious payloads. Worth factoring into proxy/WAF policy reviews for unpkg.com egress.
- **SOC/IR — Plan:** ClickFix-style fake CAPTCHA pages hosted on unpkg.com may bypass domain-reputation filters; build or tune proxy detections for unpkg.com redirects to non-package HTML content and correlate with clipboard-execution behaviors downstream.
- **Leader — Skip**
