---
title: "CDN Tsunami: HTTP/3-to-1.1 Translation Enables 350x DoS Amplification"
date: 2026-08-22T11:32:44.405318+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["cdn", "dos-amplification", "http3"]
cves: []
source: "https://thehackernews.com/2026/08/cdn-tsunami-attack-abuses-http3.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** If your origin sits behind a CDN that terminates HTTP/3, verify your CDN vendor has addressed this class of amplification and ensure your origin enforces its own rate limits independent of CDN-layer protections — CDN Tsunami demonstrates that relying solely on CDN-side controls can leave the origin exposed to amplified floods.
- **SOC/IR — Learn:** No active exploitation or IOCs reported; the attack surface is origin-server availability rather than a detectable intrusion behavior, so there is no detection rule or hunt to build today — file as background on CDN-based availability risk.
- **Leader — Learn:** Novel research with no reported exploitation means no immediate risk-register update is warranted, but CISOs who depend on CDN availability SLAs for customer-facing services should note this as context for future CDN vendor security reviews.
