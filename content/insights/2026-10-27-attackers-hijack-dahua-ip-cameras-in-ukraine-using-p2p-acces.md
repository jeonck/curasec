---
title: "Dahua IP Cameras Hijacked via P2P Access and Auth Weaknesses"
date: 2026-10-27T16:34:51.683639+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["iot-security", "camera-hijacking", "cert-ua"]
cves: []
source: "https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Dahua cameras are widely deployed beyond Ukraine; disable P2P cloud-access features, audit devices for unauthorized accounts, and verify authentication is hardened against default or weak credentials — no KEV/PoC signals but CERT-UA confirms active exploitation.
- **SOC/IR — Learn:** CERT-UA confirms active compromise of Dahua devices but the summary provides no IOCs, TTPs, or specific actor attribution to build detections from; monitor for a follow-on advisory with indicators before investing hunt time.
- **Leader — Skip**
