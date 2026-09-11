---
title: "PaperCut Replaces Emergency Patches for Two Actively Exploited Flaws"
date: 2026-09-11T14:58:57.702490+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["papercut", "active-exploitation", "patch-management"]
cves: []
source: "https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Two actively exploited flaws in PaperCut NG/MF now have proper maintenance releases; patch to version 26.0.5, 25.0.13, or 24.1.10 depending on your supported branch — emergency patches are superseded and these are the authoritative fixes.
- **SOC/IR — Plan:** Active exploitation is confirmed but the item provides no IOCs, TTPs, or detection signatures; plan to review PaperCut server logs and vendor advisory for exploitation indicators, and prepare a hunt query for abnormal print-server outbound connections once technical details surface.
- **Leader — Plan:** Active exploitation of widely deployed print-management software warrants confirming whether PaperCut is in your environment and ensuring the engineering team prioritizes patching this quarter; not a board-level systemic event but relevant if PaperCut is part of your estate.
