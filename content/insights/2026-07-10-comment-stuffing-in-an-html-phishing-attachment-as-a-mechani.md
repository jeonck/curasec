---
title: "HTML phishing attachments use comment stuffing to evade AI detection"
date: 2026-07-10T09:49:54.653216-05:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["phishing", "evasion", "detection-engineering"]
cves: []
source: "https://isc.sans.edu/diary/rss/33144"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** Comment stuffing in HTML attachments is a novel obfuscation technique worth understanding when tuning email security tooling or evaluating AI-based scanning products; no patch or config change required.
- **SOC/IR — Plan:** Build or tune email-gateway detections to flag HTML attachments with abnormally high comment-to-content ratios, as this technique is designed specifically to bypass AI-based filters your stack may rely on.
- **Leader — Skip**
