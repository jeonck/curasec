---
title: "SonicWall GMS 9.5.2 EoL Gets No Patch for CVSS 9.1 File-Read Flaw"
date: 2026-11-04T18:40:06.241551+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["sonicwall", "eol-software", "unauthenticated-vuln"]
cves: ["CVE-2026-109593"]
source: "https://thehackernews.com/2026/11/sonicwall-wont-patch-eol-gms-flaws-that.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Public PoC exists for a CVSS 9.1 unauthenticated file-read with no patch ever coming; if GMS 9.5.2 or earlier is running, migrate to a supported version or immediately isolate the management interface from untrusted networks.
- **SOC/IR — Plan:** No active exploitation confirmed (EPSS 0.01, not KEV), but the public PoC raises the probability of near-term attempts; build a detection for unusual HTTP requests against GMS endpoints matching the PoC's access pattern.
- **Leader — Plan:** An unfixable critical flaw in an EoL SonicWall management product is a technology lifecycle risk — confirm whether GMS 9.5.2 is in inventory and allocate migration budget this quarter before exploitation pressure rises.
- **Signals:** CVE-2026-109593 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub
