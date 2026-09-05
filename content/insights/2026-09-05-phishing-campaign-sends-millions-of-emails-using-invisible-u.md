---
title: "High-Volume Phishing Campaign Uses Invisible Unicode to Split Keywords"
date: 2026-09-05T13:51:48.178400+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["phishing", "email-security", "evasion"]
cves: []
source: "https://thehackernews.com/2026/09/phishing-campaign-sends-millions-of.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Audit email security gateway and filtering pipeline for Unicode normalization support; configure rules to strip or flag invisible Unicode tag characters (U+E0000 block) before keyword matching, as current filter logic may silently pass these.
- **SOC/IR — Act:** Active high-volume campaign with a specific, huntable TTP: query recent inbound email logs for messages containing invisible Unicode tag characters interleaved within financial keywords; tune SEG/SIEM detections to flag this pattern going forward.
- **Leader — Learn:** Novel evasion technique shows email filtering products may have a systematic blind spot around Unicode normalization; useful context when next reviewing email security vendor capabilities or during security questionnaire assessments.
