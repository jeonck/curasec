---
title: "DDRop Attack Breaks Intel TDX and AMD SEV-SNP Memory Isolation"
date: 2026-09-15T15:32:56.195900+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Learn"
tags: ["confidential-computing", "hardware-attack", "intel-amd"]
cves: []
source: "https://thehackernews.com/2026/09/new-ddrop-attack-breaks-intel-tdx-and.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** DDRop undermines the threat model for confidential computing by exploiting memory write-drop behavior — engineers relying on TDX or SEV-SNP for workload isolation should understand this weakens TEE guarantees when supply-chain or physical access is a concern. No patch is applicable; audit whether your confidential-computing deployments assume physical integrity of the host.
- **SOC/IR — Skip**
- **Leader — Learn:** If your organization uses confidential computing (Intel TDX/AMD SEV-SNP) to satisfy compliance or data-isolation commitments, this research narrows the assurance claim — physical access plus software control can defeat those guarantees. File for the next risk-register review, no immediate action required.
