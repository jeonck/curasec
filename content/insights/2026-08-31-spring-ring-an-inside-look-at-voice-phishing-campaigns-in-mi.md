---
title: "Spring Ring campaign uses Teams voice phishing to hit domain controllers"
date: 2026-08-31T18:00:29.794564+00:00
verdict: "Act"
verdict_engineer: "Learn"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["vishing", "microsoft-teams", "malware"]
cves: []
source: "https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Learn:** No CVE or patch required; the attack path abuses Teams social engineering rather than a software flaw, so review Teams external-access settings and restrict who can initiate calls from outside the tenant.
- **SOC/IR — Act:** Active enterprise campaign targeting domain controllers via Teams vishing — hunt for anomalous Teams call activity from external tenants followed by process execution or lateral movement, and review Unit 42's published TTPs for detection rule development.
- **Leader — Plan:** Campaign targets enterprise domain controllers through a trusted communication channel (Teams), raising both breach-risk and vendor-trust questions — brief IT leadership and consider tightening external Teams communication policies this quarter.
