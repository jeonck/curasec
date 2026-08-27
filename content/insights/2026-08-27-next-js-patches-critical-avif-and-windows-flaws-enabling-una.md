---
title: "Next.js Critical AVIF and Windows Path Traversal RCE Flaws Patched"
date: 2026-08-27T21:01:55.123618+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["nextjs", "rce", "critical-cve"]
cves: ["CVE-2026-75604"]
source: "https://thehackernews.com/2026/08/nextjs-patches-critical-avif-and.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Public PoC on GitHub for unauthenticated RCE in a ubiquitous web framework clears the bar for immediate action — upgrade Next.js to the patched release now, prioritizing any Windows-hosted deployments and any apps accepting untrusted image uploads.
- **SOC/IR — Plan:** With a public PoC and no KEV listing yet, build detections for suspicious AVIF uploads and Windows-style path traversal sequences (e.g. ..\) in HTTP requests targeting Next.js routes before active exploitation begins.
- **Leader — Plan:** Two critical unauthenticated RCE flaws with public PoC in a widely-deployed framework warrant confirming this quarter that your engineering teams have inventoried Next.js usage and applied patches — flag for a status check if any customer-facing apps are affected.
- **Signals:** CVE-2026-75604 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
