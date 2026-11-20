---
title: "SonicWall Gen 6 Firewalls Reach Permanent EOL — No Patches Ever"
date: 2026-11-20T19:04:41.748130+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Act"
tags: ["sonicwall", "end-of-life", "edge-devices"]
cves: []
source: "https://thehackernews.com/2026/11/sonicwall-warns-gen-6-firewalls-wont.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Any internet-facing Gen 6 SonicWall is permanently unpatched; immediately move them off the network edge or segment them from internet exposure, and open a replacement project — SonicWall itself is warning active exploitation is imminent.
- **SOC/IR — Plan:** No confirmed exploitation yet, but unpatched edge devices are high-value targets; inventory Gen 6 SonicWall assets in the estate, build detection coverage for lateral movement originating from those segments, and coordinate with engineers on monitoring during transition.
- **Leader — Act:** The vendor has declared these devices will never receive security patches — this is an unmitigable risk; this week, confirm whether the organization runs Gen 6 SonicWall, approve an accelerated replacement budget, and brief leadership before an exploitation event forces the conversation.
