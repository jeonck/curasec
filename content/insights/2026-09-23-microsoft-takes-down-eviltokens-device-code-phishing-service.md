---
title: "Microsoft Dismantles EvilTokens AI-Assisted Device-Code Phishing Service"
date: 2026-09-23T15:27:03.663698+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["phishing", "oauth", "ai-threats"]
cves: []
source: "https://thehackernews.com/2026/09/microsoft-takes-down-eviltokens-device.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Device-code phishing bypasses MFA by abusing the OAuth device-authorization flow; review Conditional Access policies to restrict or block device-code grant type for untrusted networks or users who don't need it.
- **SOC/IR — Plan:** The service is dismantled but the TTP persists — build or tune detections for anomalous device-code authentication requests (unusual tenant, geolocation, or off-hours token grants) in your SIEM before copycats emerge.
- **Leader — Learn:** Takedown of a 12,000-inbox-compromise phishing platform reinforces the AI-enhanced threat narrative worth including in the next leadership or board briefing on evolving phishing sophistication; no immediate exposure action required given the service is offline.
