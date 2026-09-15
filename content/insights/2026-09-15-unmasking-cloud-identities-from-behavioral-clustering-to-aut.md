---
title: "Unit 42: Behavioral Clustering to Map Cloud Identities from Audit Logs"
date: 2026-09-15T15:32:56.195900+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["cloud-security", "threat-detection", "identity"]
cves: []
source: "https://unit42.paloaltonetworks.com/behavioral-clustering-map-to-cloud-identities/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Learn:** Novel approach to deriving identity role profiles from cloud audit logs via behavioral clustering; no patch or config change needed today, but worth evaluating this technique when designing cloud detection pipelines.
- **SOC/IR — Plan:** The SQL-based detection queries and clustering methodology are worth adapting for SIEM coverage of anomalous cloud identity behavior; schedule time to evaluate and prototype rules against your cloud audit log sources.
- **Leader — Skip**
