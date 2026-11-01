---
title: "CVSS 10.0 Auth Bypass in Canonical LXD and MicroCloud"
date: 2026-11-01T17:05:59.848527+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["authentication-bypass", "lxd", "container-security"]
cves: []
source: "https://thehackernews.com/2026/11/critical-lxd-and-microcloud-flaw-cvss.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Teams running LXD or MicroCloud clusters should prioritize patching — an authentication bypass at CVSS 10.0 could allow cluster takeover and VM access. No KEV listing or public PoC in the enrichment signals, but the attack surface (network-reachable HTTPS API) warrants patching this sprint rather than waiting for a routine cycle.
- **SOC/IR — Skip**
- **Leader — Skip**
