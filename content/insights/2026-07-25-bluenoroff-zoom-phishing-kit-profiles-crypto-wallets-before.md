---
title: "BlueNoroff Phishing Kit Profiles Crypto Wallets Before Malware Drop"
date: 2026-07-25T12:08:50.257932+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["bluenoroff", "phishing", "social-engineering"]
cves: []
source: "https://thehackernews.com/2026/07/bluenoroff-zoom-phishing-kit-profiles.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Plan:** Configure DNS/URL filtering to block typosquatted Zoom and Teams domains; audit endpoint policies to detect script execution spawned from video-conferencing app processes, which is an anomalous ClickFix-style delivery path.
- **SOC/IR — Plan:** Build or tune detections for ClickFix-style prompts (unexpected clipboard/script-paste behavior) and process chains where msiexec or PowerShell launches as a child of a meeting application; no IOCs are published yet but the TTPs are specific enough to act on this quarter.
- **Leader — Learn:** North Korean BlueNoroff is maturing its crypto-sector targeting by combining compromised industry contacts with wallet-profiling before payload delivery — useful context for risk posture briefings if your org has cryptocurrency holdings or operates in financial services.
