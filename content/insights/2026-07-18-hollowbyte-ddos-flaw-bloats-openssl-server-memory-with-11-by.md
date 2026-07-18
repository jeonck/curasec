---
title: "HollowByte: 11-byte payload triggers OpenSSL memory DoS"
date: 2026-07-18T11:51:11.203777+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["openssl", "denial-of-service", "unauthenticated"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hollowbyte-ddos-flaw-bloats-openssl-server-memory-with-11-byte-payload/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** OpenSSL is universally deployed across Linux servers, TLS termination points, and containers, so exposure is near-universal; however, no KEV listing, EPSS score, or public PoC is present, meaning no active exploitation pressure. Track the OpenSSL patch release and schedule deployment within your normal critical-patch window.
- **SOC/IR — Skip**
- **Leader — Skip**
