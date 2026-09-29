---
title: "Storm-3068: Identity Compromise to Full Cloud Access via CI/CD"
date: 2026-09-29T16:53:02.010350+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["identity-compromise", "cloud-security", "ci-cd-pipeline"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Plan:** Storm-3068's attack path — compromised identity → pipeline access → cloud escalation — directly targets stacks engineers own. Review CI/CD pipeline service account permissions, OIDC trust configurations, and cloud role bindings against the TTPs described in the post this quarter.
- **SOC/IR — Plan:** Named actor campaign with a documented identity-to-cloud-pivot chain offers a concrete detection opportunity. Extract Storm-3068 TTPs from the post and build or tune detections for unusual identity federation events, pipeline credential usage, and lateral movement from CI runners into cloud APIs.
- **Leader — Learn:** The campaign illustrates how a single compromised developer identity can cascade into full cloud environment access — useful framing for board-level conversations about pipeline security investment and the risk of over-permissioned CI/CD service accounts.
