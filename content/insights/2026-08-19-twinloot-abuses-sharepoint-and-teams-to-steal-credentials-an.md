---
title: "TWINLOOT Python Implant Uses SharePoint/Teams for C2"
date: 2026-08-19T11:36:35.301683+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["malware", "microsoft-365", "c2"]
cves: []
source: "https://thehackernews.com/2026/08/twinloot-abuses-sharepoint-and-teams-to.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No exploitation signals or patch action required, but this technique highlights the risk of trusting M365 egress unconditionally; review whether SharePoint/Teams API access from non-user contexts is logged and anomaly-monitored in your environment.
- **SOC/IR — Plan:** TWINLOOT's C2-over-SharePoint-Online pattern blends into legitimate M365 traffic — build or tune detections for unusual SharePoint file polling cadence and Teams API calls from non-interactive service contexts to catch implants using this framework.
- **Leader — Learn:** Newly documented implant class that weaponizes trusted M365 services, useful context for future conversations about M365 security controls and monitoring investment, but no confirmed active campaigns require immediate leadership action.
