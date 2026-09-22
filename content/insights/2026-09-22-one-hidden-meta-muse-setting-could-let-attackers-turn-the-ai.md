---
title: "Meta Muse AI assistant can be hijacked post-compromise via hidden setting"
date: 2026-09-22T15:30:54.753130+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["ai-assistant", "macos", "post-exploitation"]
cves: []
source: "https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** The attack requires malware already present on the host, making this a post-exploitation primitive rather than an initial-access flaw. No patch details are provided yet; review AI assistant permission grants on macOS endpoints and consider restricting Muse accessibility access where it isn't needed.
- **SOC/IR — Plan:** Wardle's PoC establishes a concrete post-compromise technique where an attacker redirects Muse microphone input by flipping a hidden setting; build a detection or hunt for unexpected modifications to Muse configuration files on managed Macs.
- **Leader — Learn:** This illustrates how broad OS permissions granted to AI assistants can become an attacker tool after initial compromise — useful background for refining enterprise AI-assistant usage policies, but not an immediate action item without active exploitation evidence.
