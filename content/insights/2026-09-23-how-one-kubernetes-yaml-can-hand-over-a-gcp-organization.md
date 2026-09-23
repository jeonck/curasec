---
title: "Kubernetes Config Connector Allows GCP Org-Wide Privilege Escalation"
date: 2026-09-23T15:27:03.663698+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["kubernetes", "gcp", "privilege-escalation"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/how-one-kubernetes-yaml-can-hand-over-a-gcp-organization/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** GKE users running Config Connector should audit the service account's IAM permissions and restrict who can submit YAML to affected clusters — a limited K8s principal could escalate to GCP org-level access via the connector's delegated authority. No public PoC or active exploitation, but the attack path is now documented; tighten Config Connector RBAC and review org-level bindings this quarter.
- **SOC/IR — Learn:** A new confused-deputy escalation path from K8s YAML to GCP org control is worth adding to the analyst mental model for GKE environments, but there are no IOCs or active campaigns to hunt. File as a technique to watch if hunting lateral movement in GCP-connected clusters.
- **Leader — Skip**
