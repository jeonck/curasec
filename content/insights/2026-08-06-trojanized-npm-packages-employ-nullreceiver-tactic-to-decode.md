---
title: "Trojanized npm Packages Use Blockchain to Hide C2 IP (NullReceiver)"
date: 2026-08-06T13:03:19.955458+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["npm-supply-chain", "c2-evasion", "blockchain"]
cves: []
source: "https://thehackernews.com/2026/08/trojanized-npm-packages-decode-c2-ip.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Act:** Two named malicious packages — 'bianira-ui' and 'fluid-type-ui' — are trojanized with active C2 capability; audit all dependency trees and lock files for these packages and remove them immediately if found.
- **SOC/IR — Plan:** NullReceiver is a novel dead-drop resolver technique that hides C2 IPs inside empty Ethereum transfer destinations, making traditional blocklist-based detections ineffective; build or tune detections for unusual outbound Ethereum RPC calls originating from build pipelines or developer endpoints this quarter.
- **Leader — Learn:** Attackers are using blockchain infrastructure to evade C2 detection in software supply-chain attacks — a technique evolution worth including in risk-posture discussions, but no immediate leadership action is required given the limited scope and absence of a major corroborated campaign.
