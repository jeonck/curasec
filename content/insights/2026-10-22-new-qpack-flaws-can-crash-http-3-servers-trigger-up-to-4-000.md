---
title: "QPACK Flaws Allow Unauthenticated DoS and 4,000x Memory Amplification on HTTP/3 Servers"
date: 2026-10-22T15:52:23.930402+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["http3", "denial-of-service", "memory-amplification"]
cves: []
source: "https://thehackernews.com/2026/10/new-qpack-flaws-can-crash-http3-servers.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC now exists for crashing HTTP/3 servers with a single unauthenticated request via QPACK header expansion; audit whether HTTP/3 is enabled on your edge servers (nginx, Caddy, Envoy, etc.) and disable it or apply vendor patches as they arrive — exposure is immediate with PoC code released.
- **SOC/IR — Plan:** No active exploitation campaign is reported, but the public PoC lowers the bar quickly; build detections for anomalous single-connection HTTP/3 sessions paired with server OOM events or abrupt restarts, and add HTTP/3 header-decompression anomalies to your edge-device monitoring coverage.
- **Leader — Skip**
