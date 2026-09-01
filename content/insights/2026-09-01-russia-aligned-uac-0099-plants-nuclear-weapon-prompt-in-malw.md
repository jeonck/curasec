---
title: "UAC-0099 embeds LLM-disrupting prompts in malware to blind AI analysis"
date: 2026-09-01T15:28:52.066055+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["adversarial-ai", "malware-analysis", "uac-0099"]
cves: []
source: "https://thehackernews.com/2026/09/russia-aligned-uac-0099-plants-nuclear.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** GuardBreaker shows that AI-assisted malware scanning can be manipulated at the artifact level; no patch or config change is needed today, but engineers building AI-augmented security pipelines should understand this evasion class.
- **SOC/IR — Plan:** Review any AI/LLM-assisted triage or malware-analysis workflows and add a mandatory human-review layer for suspected APT samples — do not treat LLM output as authoritative when analyzing artifacts from sophisticated actors.
- **Leader — Learn:** Adversaries are now actively engineering around AI-assisted defenses; file this as context for future AI-tool procurement and policy decisions around over-reliance on LLM-based analysis in SOC operations.
