---
title: "Mior and Skyfall Attacks Break AMD SEV-SNP VM Isolation"
date: 2026-11-14T17:01:43.117086+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Learn"
tags: ["confidential-computing", "amd-sev-snp", "hypervisor"]
cves: []
source: "https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** These attacks fundamentally challenge the trust model of AMD SEV-SNP confidential VMs by showing a malicious hypervisor can read guest memory and that Mior can forge attestation reports; no public PoC or active exploitation, but engineers relying on SEV-SNP for data isolation should re-evaluate their threat model assumptions.
- **SOC/IR — Skip**
- **Leader — Learn:** If your organization uses confidential computing on AMD hardware to meet data-isolation compliance claims, this research weakens those assurances and is worth flagging to your cloud risk review — file for the next vendor risk assessment cycle, no immediate action required.
