---
title: "Internet-Exposed DICOM Services: 3,979 Vulnerable After Noise Filtering"
date: 2026-07-20T14:31:24.569284+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["dicom", "medical-imaging", "exposure-measurement"]
cves: []
source: "https://arxiv.org/abs/2607.15839"
source_name: "arXiv cs.CR"
status: "archived"
---
- **Engineer — Plan:** If your organization runs DICOM infrastructure, audit all services for internet exposure: the research confirms 3,979 deployments accept unauthenticated connections with no encryption, and ~50% show zero maintenance activity. Verify DICOM ports are not internet-reachable and enforce TLS and auth for any legitimate external access.
- **SOC/IR — Learn:** Pure measurement research with no IOCs, TTPs, or active exploitation data; useful background on healthcare attack surface but yields no detection or hunting work today.
- **Leader — Learn:** Provides credible benchmarking data on medical imaging infrastructure exposure — useful context for healthcare sector risk conversations or vendor assessments, but no board-level action is required absent a breach or regulatory deadline.
