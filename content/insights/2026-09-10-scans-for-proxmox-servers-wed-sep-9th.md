---
title: "Active Scanning Targets EOL Proxmox VE 7 Vulnerability"
date: 2026-09-10T14:58:06.811051+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["virtualization", "vulnerability", "scanning"]
cves: []
source: "https://isc.sans.edu/diary/rss/33324"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Plan:** If your environment includes any Proxmox VE 7 instances, treat them as actively targeted and prioritize upgrading to a supported version; v7 has been EOL for years and will receive no patches for this or future issues.
- **SOC/IR — Learn:** Opportunistic scanning is occurring against Proxmox VE 7 hosts, but no IOCs or specific exploit TTPs are published yet — worth noting for asset-aware alerting if Proxmox is in scope, but no detection action warranted now.
- **Leader — Skip**
