---
title: "Weekly Recap: Chrome 0-Day, Router Hijacks, Coder Supply Chain Attack"
date: 2026-09-07T16:27:04.378719+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["supply-chain", "phishing", "weekly-recap"]
cves: []
source: "https://thehackernews.com/2026/09/weekly-recap-chrome-0-day-router.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** The recap references a supply chain attack via a trusted software source and a Chrome 0-day, but the summary lacks package names, versions, or CVEs to act on; follow up on the individual Coder supply chain story to determine if it touches your toolchain.
- **SOC/IR — Plan:** The text-only QR code phishing technique — rendering a scannable code from ASCII characters to survive image-blocking — is a novel lure evasion worth adding to email detection logic; build or tune rules to flag text-pattern QR codes in message bodies.
- **Leader — Skip**
