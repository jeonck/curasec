---
title: "BGP Hijack Poisons Virtualizor Update Channel, 5+ Hypervisors Root-Compromised"
date: 2026-09-02T15:05:08.783541+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["bgp-hijack", "supply-chain", "virtualizor"]
cves: []
source: "https://thehackernews.com/2026/09/bgp-hijack-delivers-malicious.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Any Virtualizor installation that auto-updated after August 28 at ~20:57 UTC may have received the trojanized package and should be treated as compromised; immediately audit those hypervisors for persistence mechanisms (cron, SSH keys, kernel modules) and isolate pending forensic review.
- **SOC/IR — Act:** Confirmed root-level compromise on 5 hypervisors with an update-window starting August 28 at 20:57 — sweep all Virtualizor hosts for new root SSH authorized_keys, unexpected cron jobs, or novel init services added after that timestamp; initiate assume-breach IR process for any positive hits.
- **Leader — Plan:** If your infrastructure or a managed hosting vendor runs Virtualizor, request a written attestation from them confirming whether their hypervisors fell within the compromised update window, and add BGP-hijack supply-chain risk to the next vendor risk review cycle.
