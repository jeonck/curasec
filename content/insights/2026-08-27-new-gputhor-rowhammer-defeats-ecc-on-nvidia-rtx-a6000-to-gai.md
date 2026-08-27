---
title: "GPUThor Rowhammer Defeats ECC on NVIDIA RTX A6000, Achieves Root"
date: 2026-08-27T21:01:55.123618+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["rowhammer", "gpu-security", "privilege-escalation"]
cves: []
source: "https://thehackernews.com/2026/08/gputhor-rowhammer-defeats-ecc-on-nvidia.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** Novel academic research showing ECC — NVIDIA's own recommended Rowhammer mitigation — is bypassable on GDDR6 workstation GPUs; no public PoC, KEV listing, or active exploitation, but engineers running NVIDIA A6000s in multi-tenant or shared ML environments should revisit GPU isolation assumptions and monitor for a NVIDIA advisory.
- **SOC/IR — Learn:** No IOCs, no mapped TTPs, and no known exploitation in the wild; file for awareness and revisit if a weaponized PoC surfaces or campaigns emerge targeting GPU-equipped workstations.
- **Leader — Skip**
