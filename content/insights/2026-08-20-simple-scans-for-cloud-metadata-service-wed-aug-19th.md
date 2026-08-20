---
title: "SANS ISC: Observed Scans Targeting Cloud Metadata Service (IMDS)"
date: 2026-08-20T11:39:11.237527+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["cloud-security", "imds", "credential-exposure"]
cves: []
source: "https://isc.sans.edu/diary/rss/33260"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Plan:** Reinforces the need to enforce IMDSv2 (hop-limit 1, require session tokens) on all EC2/GCP/Azure VMs and audit IAM role assignments to minimize credential scope accessible via the metadata endpoint.
- **SOC/IR — Learn:** No new IOCs or campaign detail here, but a useful reminder to verify detections exist for unusual internal requests to 169.254.169.254, which can indicate SSRF or compromised workload attempts to harvest credentials.
- **Leader — Skip**
