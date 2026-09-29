---
title: "OperTraitor: Tool to Audit Excessive RBAC in Kubernetes Operators"
date: 2026-09-29T16:53:02.010350+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["kubernetes", "rbac", "non-human-identities"]
cves: []
source: "https://unit42.paloaltonetworks.com/agentic-ai-kubernetes-operator-risks/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Plan:** Kubernetes operators routinely accumulate excessive cluster-admin-level RBAC that expands blast radius if compromised; evaluate and run OperTraitor against your clusters this quarter to audit operator service account permissions and remediate over-privileged non-human identities.
- **SOC/IR — Skip**
- **Leader — Skip**
