---
title: "witness-vault: AES-256-GCM self-decrypting HTML vaults (no install)"
date: 2026-10-14T15:48:57.203933+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["encryption-tooling", "html-smuggling", "webcrypto"]
cves: []
source: "https://github.com/Hamidooh/witness-vault"
source_name: "GitHub Trending"
status: "active"
---
- **Engineer — Learn:** Interesting pattern for offline/air-gapped secret sharing using native WebCrypto — worth evaluating if your team needs zero-dependency encrypted file handoff, but no action required on running systems.
- **SOC/IR — Learn:** Self-decrypting HTML files are a known smuggling vector; this open-source implementation illustrates the technique and may inform tuning of HTML smuggling detections in your email/proxy pipeline.
- **Leader — Skip**
