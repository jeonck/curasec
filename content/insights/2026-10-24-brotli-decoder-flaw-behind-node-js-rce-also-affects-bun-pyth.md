---
title: "Brotli Decoder Memory Corruption RCE Affects Bun, Python, Envoy"
date: 2026-10-24T14:29:02.695753+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["rce", "supply-chain", "memory-corruption"]
cves: ["CVE-2026-111497"]
source: "https://thehackernews.com/2026/10/brotli-decoder-flaw-behind-nodejs-rce.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC exists for this buffer-overflow RCE in the Brotli decoder, and the affected surface is wide: update Python brotli and brotlicffi packages to patched versions and audit any Envoy proxy configuration that enables Brotli decompression, since attacker-controlled compressed payloads are the trigger.
- **SOC/IR — Learn:** No active exploitation campaign, no published IOCs, and EPSS sits at effectively zero — there is no hunt or detection to run today, but analysts should understand that Brotli-decompressing endpoints (Envoy, Python services) represent an emerging RCE surface to watch if exploitation picks up.
- **Leader — Skip**
- **Signals:** CVE-2026-111497 — CISA KEV: not listed, EPSS 0.00, public PoC on GitHub
