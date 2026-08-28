---
title: "19 Malicious Chrome/Edge Extensions Drain Crypto Wallets"
date: 2026-08-28T21:21:40.237236+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["browser-extensions", "supply-chain", "crypto-theft"]
cves: []
source: "https://thehackernews.com/2026/08/19-chrome-and-edge-extensions-found.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Audit managed Chrome and Edge extension allowlists against the 19 identified malicious extensions (details in the Socket/Hacker News report); enforce an extension allowlisting policy to block unapproved installs in managed browser deployments.
- **SOC/IR — Plan:** Pull endpoint telemetry to hunt for these extension IDs across managed devices; build or tune a detection for novel extension installations that request broad permissions aligned with credential or clipboard access.
- **Leader — Learn:** A coordinated six-month extension campaign highlights browser add-ons as a persistent supply-chain risk; useful context for reviewing whether your browser governance policy enforces an approved extension allowlist.
