---
title: "UAT-10147 Deploys SPECTRE Malware with EDR Bypass and Linux Rootkit"
date: 2026-08-24T11:41:22.171346+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["threat-actor", "linux-rootkit", "edr-bypass"]
cves: []
source: "https://thehackernews.com/2026/08/uat-10147-uses-ai-to-scale-server.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Novel Linux rootkit and EDR bypass technique targeting web servers is worth understanding for hardening posture, but no specific CVE, PoC, or KEV signal means no immediate patch action required.
- **SOC/IR — Plan:** Build or tune detections for EDR bypass behavior and Linux rootkit indicators on web-facing servers; prioritize collecting relevant Linux endpoint telemetry if not already sourced, ahead of potential targeting expansion beyond current sectors.
- **Leader — Learn:** Chinese-speaking cybercrime group targeting education, media, and tech sectors globally; useful for sector risk awareness and future board briefings, but no immediate vendor or regulatory action required based on available signals.
