---
title: "Internet Scans Probing Solana/Surfpool Developer Endpoints"
date: 2026-08-11T11:54:43.298939+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["blockchain", "scanning", "developer-tools"]
cves: []
source: "https://isc.sans.edu/diary/rss/33230"
source_name: "SANS ISC"
status: "archived"
---
- **Engineer — Learn:** If you expose Solana JSON-RPC or gRPC dev endpoints (e.g., surfpool) on public interfaces, audit firewall rules to ensure they are not internet-reachable; no active exploitation or PoC reported.
- **SOC/IR — Learn:** Awareness item: opportunistic scans targeting Solana dev endpoints are occurring, but no IOCs, TTPs, or confirmed exploitation are provided to act on.
- **Leader — Skip**
