---
title: "Critical Cisco Nexus 9000 RCE Flaw (CVSS 9.8) — PoC Public"
date: 2026-09-04T14:56:27.274495+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["cisco", "network-infrastructure", "rce"]
cves: ["CVE-2026-20212"]
source: "https://thehackernews.com/2026/09/critical-cisco-nexus-9000-flaw-lets.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Public PoC on GitHub for an unauthenticated root RCE on widely deployed data-center switches raises exploitation risk even with low EPSS; apply Cisco's Nexus 9000 patch now and separately assess IOS XR exposure for the two 9.8-rated CVEs that have no available workaround.
- **SOC/IR — Plan:** No active exploitation confirmed yet, but the public PoC means attempts are likely imminent; build detections for anomalous access to Nexus 9000 management interfaces and prepare a hunt query baseline now before KEV listing forces a reactive response.
- **Leader — Plan:** Unauthenticated root RCE on core network switches with a public PoC is a meaningful risk-register item; confirm your network team has the Nexus 9000 patch cycle scheduled and note the IOS XR exposure for environments running that platform.
- **Signals:** CVE-2026-20212 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub
