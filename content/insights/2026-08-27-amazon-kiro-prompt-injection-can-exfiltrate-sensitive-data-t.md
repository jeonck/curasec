---
title: "Amazon Kiro IDE prompt injection enables data exfiltration via Kiro Powers"
date: 2026-08-27T21:01:55.123618+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["prompt-injection", "ai-ide", "data-exfiltration"]
cves: []
source: "https://thehackernews.com/2026/08/amazon-kiro-prompt-injection-can.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** If your developers run Amazon Kiro IDE 0.7.45 on Windows, verify whether a patched version is available and update; the prompt injection → data exfiltration path via Kiro Powers is a real supply-chain risk for dev environments. No KEV or PoC signals elevate this to Act.
- **SOC/IR — Learn:** No IOCs, active exploitation evidence, or ATT&CK-mappable detection surface are present; the item illustrates a prompt injection exfiltration pattern in agentic IDEs worth tracking as AI dev tooling becomes a threat surface.
- **Leader — Learn:** Useful data point for AI tool governance: agentic IDEs can become data-exfiltration vectors via prompt injection, with no CVE or patch timeline disclosed yet — worth a line item when reviewing AI-assisted development tool policies.
