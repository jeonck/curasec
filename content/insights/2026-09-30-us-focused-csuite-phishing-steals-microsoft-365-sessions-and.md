---
title: "CSuite Phishing Campaign Steals M365 Sessions, Deploys RMM Tools"
date: 2026-09-30T16:48:49.184501+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["phishing", "rmm-abuse", "microsoft-365"]
cves: []
source: "https://thehackernews.com/2026/09/us-focused-csuite-phishing-steals.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Session token theft bypasses MFA controls — review M365 Conditional Access policies for continuous access evaluation and token binding; audit which RMM tools are permitted to execute in your environment to limit post-phishing persistence.
- **SOC/IR — Act:** Active campaign with a clear behavioral signature: hunt for unauthorized RMM tool installations on endpoints and anomalous M365 sessions (new device or geolocation logins shortly following phishing delivery) since campaign has 351 tracked sandbox submissions concentrated in the US.
- **Leader — Plan:** Campaign explicitly targets C-suite at technology, manufacturing, government, and consulting organizations — brief senior executives and their assistants on the risk this quarter and confirm whether your sector shows up in threat intel targeting lists.
