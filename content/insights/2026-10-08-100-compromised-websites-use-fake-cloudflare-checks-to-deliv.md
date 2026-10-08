---
title: "100+ Compromised Sites Use Fake Cloudflare Checks to Drop LunexStealer"
date: 2026-10-08T17:51:36.071186+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["info-stealer", "fake-captcha", "drive-by"]
cves: []
source: "https://thehackernews.com/2026/10/100-compromised-websites-use-fake.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** The fake Cloudflare verification lure (ClickFix-style JS injection) is an evolving delivery pattern worth factoring into web security design, but no specific software patch or configuration action is indicated today.
- **SOC/IR — Plan:** The fake CAPTCHA/Cloudflare check TTP is gaining traction as a malware delivery vector; build or tune detections for unexpected script execution following browser verification prompts, and monitor for CERT-UA's LunexStealer IOC release to enable retrospective hunting.
- **Leader — Skip**
