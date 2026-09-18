---
title: "Check Point Management Server: Unauthenticated RCE as Root"
date: 2026-09-18T14:58:07.079452+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["check-point", "rce", "network-security"]
cves: []
source: "https://thehackernews.com/2026/09/critical-check-point-management-server.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Unauthenticated root RCE on the management plane that controls all firewall policy is extremely high impact, but no KEV listing, PoC, or active exploitation is confirmed; apply Check Point's LivePatch update to all Security Management and Log Servers within your next patch window, prioritizing internet-accessible instances.
- **SOC/IR — Plan:** No IOCs or confirmed exploitation yet, but compromise of the Check Point management server would let an attacker silently rewrite firewall policy — establish a baseline of expected connections to your management server ports now and prepare a hunt query to surface anomalous pre-auth traffic if exploitation activity is reported.
- **Leader — Plan:** If Check Point Security Management is in your environment, confirm with your engineering team this quarter that the LivePatch update has been applied; unauthenticated control-plane RCE would hand attackers the keys to your entire perimeter policy, but no active exploitation has been reported yet.
