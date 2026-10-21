---
title: "300+ Tor Exit Relays Hijacked to Steal SSH Passwords (Oct 1-5)"
date: 2026-10-21T15:56:43.831517+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["tor", "ssh", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/10/attackers-hijacked-over-300-tor-exit.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Only password-based SSH sessions routed through Tor during October 1-5 are affected. Audit SSH access logs for Tor-origin connections in that window, rotate any credentials that may have been exposed, and enforce key-only SSH authentication on all servers.
- **SOC/IR — Plan:** The active interception window closed October 5; build a hunt for any Tor-exit-routed SSH sessions in that period and trace subsequent authentication events from potentially stolen credentials to detect follow-on access.
- **Leader — Skip**
