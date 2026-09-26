---
title: "Storm-3168 Uses Compromised Azure Service Principals for Cloud Attacks"
date: 2026-09-26T14:58:08.483782+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["azure", "service-principals", "threat-actor"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Plan:** Active campaign targeting Azure service principals with credential access and resource deletion is a real exposure for any Azure tenant; audit service principal permissions, review Entra ID sign-in and audit logs for anomalous SP activity, and apply Microsoft's published hardening guidance this quarter.
- **SOC/IR — Act:** Microsoft reports this as an active campaign with named TTPs (cloud recon, credential access, resource deletion) mappable to ATT&CK; hunt for unusual service principal authentication patterns in Entra ID and Azure activity logs, and pull detection queries from Microsoft's defender guidance included in the post.
- **Leader — Learn:** Named actor campaign confirms cloud identity (service principals) is a live attack surface; useful for contextualizing identity security investment priorities, but no board-level action required unless your team surfaces specific indicators of exposure in your Azure environment.
