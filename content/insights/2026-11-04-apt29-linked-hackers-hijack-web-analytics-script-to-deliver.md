---
title: "APT29 Hijacks Plerdy Analytics Script in iOS/Android Watering Hole Campaign"
date: 2026-11-04T18:40:06.241551+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["apt29", "supply-chain", "watering-hole"]
cves: []
source: "https://thehackernews.com/2026/11/apt29-linked-hackers-hijack-web.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Audit your web properties for use of Plerdy SEO Tracker and any other third-party analytics scripts; remove or isolate if found, and review Content Security Policy coverage to limit blast radius of injected third-party JavaScript.
- **SOC/IR — Act:** Review Sekoia's full research for IOCs and indicators tied to this campaign; hunt proxy/DNS logs for Plerdy-related domains and unexpected JavaScript attribute-harvesting patterns on web properties serving your users or employees.
- **Leader — Plan:** Initiate a vendor-risk review of third-party analytics scripts across corporate web properties; a nation-state supply chain attack on a web analytics provider is precisely the vector that bypasses perimeter controls and warrants a policy on approved script sources.
