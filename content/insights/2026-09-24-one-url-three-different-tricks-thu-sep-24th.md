---
title: "SANS ISC: Phishing URL Using Three Obfuscation Tricks to Bypass Controls"
date: 2026-09-24T15:49:46.689252+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["phishing", "url-obfuscation", "detection-evasion"]
cves: []
source: "https://isc.sans.edu/diary/rss/33366"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** Technique analysis of a crafted phishing URL designed to fool automated security controls; no patch or configuration change required, but useful context for tuning email gateway URL inspection policies.
- **SOC/IR — Plan:** SANS ISC breaks down specific URL obfuscation methods used to evade scanners — review the full diary to extract patterns and consider adding corresponding URL-decoding or pattern-matching rules to your email security or SIEM pipeline.
- **Leader — Skip**
