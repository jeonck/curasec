---
title: "Fake ChatGPT/Claude GitHub Apps Drop Crypto Miners via Signed Loaders"
date: 2026-10-29T17:24:45.058738+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["crypto-miner", "supply-chain", "ai-lure"]
cves: []
source: "https://thehackernews.com/2026/10/fake-chatgpt-and-claude-apps-abuse.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Developers are a likely target audience for fake AI desktop tools distributed via GitHub. Audit endpoints for unauthorized process execution tied to AI app installs and enforce a policy requiring official sources (openai.com, anthropic.com) for any AI desktop clients used internally.
- **SOC/IR — Plan:** The Yoba campaign uses signed loaders to slip past initial defenses before dropping miners — worth building detections for unexpected signed-binary child processes spawning mining activity. No specific IOCs are provided in this summary, so a targeted sweep isn't actionable yet; queue a detection rule for anomalous CPU-spike processes spawned by newly installed apps.
- **Leader — Learn:** This campaign exploits employee enthusiasm for AI tools to sneak malware in via unofficial downloads — a useful data point for refreshing acceptable-use policy around AI desktop applications and reinforcing approved software procurement channels.
