---
title: "Unit 42: Identity Phishing via Enterprise Collaboration Tools"
date: 2026-08-20T11:39:11.237527+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["identity-abuse", "phishing", "collaboration-tools"]
cves: []
source: "https://unit42.paloaltonetworks.com/communication-channel-identity-risks/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Learn:** Research on how attackers abuse trusted communication channels (Slack, Teams, email) for credential theft; review OIDC/SAML trust configurations and conditional access policies as a follow-up architecture exercise.
- **SOC/IR — Plan:** Unit 42 analysis of TTPs for collaboration-tool identity phishing is worth building detections around this quarter — prioritize tuning alerts for anomalous OAuth consent grants and unusual login sources following collaboration-platform interactions.
- **Leader — Skip**
