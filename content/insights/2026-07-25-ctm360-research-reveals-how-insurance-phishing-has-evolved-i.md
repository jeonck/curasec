---
title: "Insurance phishing evolves to real-time AiTM account hijacking"
date: 2026-07-25T12:08:50.257932+00:00
verdict: "Plan"
verdict_engineer: "Skip"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["phishing", "account-takeover", "aitm"]
cves: []
source: "https://thehackernews.com/2026/07/ctm360-research-reveals-how-insurance.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Skip**
- **SOC/IR — Plan:** AiTM (adversary-in-the-middle) phishing bypasses MFA by proxying sessions in real time; build or tune detections for impossible-travel, session token anomalies, and auth from new ASNs immediately after login events.
- **Leader — Learn:** Real-time session hijacking erodes MFA as a control — useful context for risk register and security awareness program updates, but no immediate action required given no corroborating signals or named breach.
