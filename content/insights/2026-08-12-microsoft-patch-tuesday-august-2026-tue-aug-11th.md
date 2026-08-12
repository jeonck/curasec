---
title: "Microsoft Patch Tuesday Aug 2026: 418 CVEs, 1 Exploited Zero-Day"
date: 2026-08-12T11:57:00.937865+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["patch-tuesday", "microsoft", "zero-day"]
cves: []
source: "https://isc.sans.edu/diary/rss/33236"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Act:** With 62 critical CVEs including remote code execution in QUIC and DNS Server plus one actively exploited privilege escalation zero-day, prioritize patching Windows systems this week — target the exploited zero-day and RCE bugs in DNS Server and QUIC-enabled stacks first.
- **SOC/IR — Act:** One vulnerability is confirmed exploited in the wild; hunt for privilege escalation activity on Windows endpoints since August 11 and tune EDR/SIEM detections for post-exploit behavior while engineering patches.
- **Leader — Plan:** The scale (418 patches, 62 critical, active exploitation) warrants confirming your patch SLA is on track and reviewing exposure of any internet-facing Windows DNS infrastructure with your team this quarter.
