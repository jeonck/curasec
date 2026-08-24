---
title: "DOUBLECUP Malware Uses PNG Files to Deliver Payloads"
date: 2026-08-24T11:41:22.171346+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["malware", "steganography", "evasion"]
cves: []
source: "https://isc.sans.edu/diary/rss/33274"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** DOUBLECUP embeds payloads inside PNG files as an obfuscation layer rather than true steganography; worth understanding the technique when reviewing file-upload handling and egress filtering in your pipelines, but no patch or config change is required today.
- **SOC/IR — Learn:** The write-up surfaces a payload-delivery method using PNG files, which could inform tuning detections around suspicious image-file execution chains; however, the summary is too truncated to extract IOCs or a concrete detection rule — monitor the full SANS diary for actionable indicators.
- **Leader — Skip**
