---
title: "Star Blizzard Uses Fake Event Invites to Backdoor 100+ Orgs"
date: 2026-09-30T16:48:49.184501+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["state-sponsored", "spear-phishing", "russia"]
cves: []
source: "https://thehackernews.com/2026/09/russias-star-blizzard-targets-100.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No patchable vulnerability — the attack relies entirely on social engineering to install a Windows backdoor. Review whether email gateways and endpoint controls adequately block unsolicited event-invite attachments from external senders.
- **SOC/IR — Plan:** No IOCs surfaced in this report, but the campaign is active since January against US/UK Ukraine-adjacent organizations; build or tune detections for spear-phishing lures mimicking event invitations and hunt for anomalous backdoor install activity on Windows endpoints if your estate fits the targeting profile.
- **Leader — Learn:** A Russian state actor with confirmed infections across 100+ US/UK organizations is worth tracking for situational awareness; if your organization has Ukraine-related partnerships, policy work, or government contracts, escalate to Plan and brief leadership on potential targeting.
