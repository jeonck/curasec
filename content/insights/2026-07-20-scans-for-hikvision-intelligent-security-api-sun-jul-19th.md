---
title: "Active scans detected targeting Hikvision camera API endpoints"
date: 2026-07-20T13:16:24.819582+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["iot-security", "network-scanning", "cameras"]
cves: []
source: "https://isc.sans.edu/diary/rss/33164"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Plan:** If your environment includes Hikvision cameras, audit whether their Intelligent Security API is exposed to the internet and place them behind a firewall or VPN; no new CVE is cited but active scanning indicates exploitation interest.
- **SOC/IR — Plan:** Add or tune detections for inbound probes against Hikvision API paths (e.g., /ISAPI/ endpoints) in perimeter logs; SANS honeypots are detecting active internet-wide scans worth tracking as a precursor to exploitation.
- **Leader — Skip**
