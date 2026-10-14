---
title: "curl 8.23.0 Patches HTTP/2 Upload Memory Corruption with Public PoC"
date: 2026-10-14T15:48:57.203933+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["curl", "memory-corruption", "http2"]
cves: []
source: "https://thehackernews.com/2026/10/curl-patches-http2-upload-flaw-after.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC demonstrating client-side code execution exists; curl is present in virtually every container base image, CI/CD runner, and server. Patch to curl 8.23.0 now — check container base images, pipeline runners, and any service that uploads via HTTP/2.
- **SOC/IR — Learn:** No IOCs, no active exploitation reported, and the attack surface (malicious server exploiting an uploading client) offers limited detection opportunity; understanding the attack vector is useful for triage context if crashes or anomalous curl behavior surface later.
- **Leader — Skip**
