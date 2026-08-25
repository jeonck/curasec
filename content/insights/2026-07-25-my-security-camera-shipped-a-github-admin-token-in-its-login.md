---
title: "Hanwha security camera firmware leaked GitHub admin token in login page"
date: 2026-07-25T12:08:50.257932+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["supply-chain", "credential-exposure", "iot"]
cves: []
source: "https://hhh.hn/hanwha-github-token/"
source_name: "HN (security)"
status: "archived"
---
- **Engineer — Act:** If you run Hanwha/Samsung security cameras, audit firmware or network-exposed login pages for embedded credentials; more broadly, scan your own build artifacts and container images for hardcoded tokens using tools like truffleHog or gitleaks, as this pattern recurs in IoT and embedded firmware.
- **SOC/IR — Learn:** No IOCs or active exploitation reported, but the incident illustrates how IoT device web UIs can leak credentials visible to anyone on the network — worth noting for device inventory reviews and camera network segmentation practices.
- **Leader — Learn:** Illustrates third-party hardware supply-chain risk: vendor-embedded credentials in devices deployed on corporate networks can expose upstream source repositories; factor into hardware procurement and vendor security assessment criteria.
