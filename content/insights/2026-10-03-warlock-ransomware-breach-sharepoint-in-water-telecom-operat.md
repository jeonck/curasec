---
title: "Warlock ransomware exploits SharePoint in critical infrastructure attacks"
date: 2026-10-03T15:08:49.690527+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["ransomware", "sharepoint", "critical-infrastructure"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/warlock-ransomware-breach-sharepoint-in-water-telecom-operator-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Active exploitation of SharePoint for initial access is confirmed across multiple org types, but no specific CVE, KEV listing, or PoC is surfaced in the signals; ensure SharePoint is fully patched and audit authentication/access logs for anomalous behavior this sprint.
- **SOC/IR — Act:** An active China-linked ransomware campaign is using SharePoint exploitation as the entry point against water, telecom, government, and education targets; hunt for SharePoint exploitation indicators (unusual web shell activity, anonymous auth attempts) and check whether your estate's sector matches the targeting profile.
- **Leader — Act:** A named state-linked ransomware group is actively targeting water utilities, telecom operators, regional governments, and universities via SharePoint — if your organization operates in any of these sectors, brief leadership now and confirm SharePoint patch posture and segmentation with engineering before this surfaces as a board question.
