---
title: "40 Malicious Firefox Extensions Steal Crypto Wallet Secrets via Web3 Lures"
date: 2026-08-20T11:39:11.237527+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["browser-extensions", "crypto-theft", "supply-chain"]
cves: []
source: "https://thehackernews.com/2026/08/40-malicious-firefox-extensions-pose-as.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** If your org uses Web3 tooling or allows browser extensions in managed environments, audit installed Firefox extensions against the 77 flagged add-ons (OKX, Rabby Wallet, TronLink impersonators) and enforce extension allowlisting via policy.
- **SOC/IR — Plan:** Build or tune detections for browser extension installs from unofficial sources in managed endpoints; hunt for any of the 77 flagged extensions identified by Socket in your EDR extension inventory.
- **Leader — Skip**
