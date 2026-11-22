---
title: "Rackspace Spot breach exposed customer Kubernetes secrets"
date: 2026-11-22T16:05:35.915127+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["kubernetes", "cloud-breach", "vendor-risk"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/rackspace-spot-breach-let-hackers-access-customer-kubernetes-secrets/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** If Rackspace Spot is in your environment, immediately rotate all Kubernetes secrets stored in affected clusters and audit workloads for unauthorized deployments that may have exfiltrated additional credentials or pivoted further.
- **SOC/IR — Act:** If Rackspace Spot is in scope, hunt for unauthorized Kubernetes workloads deployed since the breach window and check for lateral movement using secrets that may have been harvested; focus on API server audit logs for anomalous service account activity.
- **Leader — Act:** Confirm whether your organization uses Rackspace Spot, request Rackspace's incident report with breach timeline and scope, and assess whether any exposed Kubernetes secrets held data subject to breach-notification obligations.
