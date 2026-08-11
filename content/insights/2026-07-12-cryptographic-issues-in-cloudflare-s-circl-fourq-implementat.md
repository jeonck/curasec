---
title: "Cryptographic Flaw in Cloudflare CIRCL FourQ (CVE-2025-8556)"
date: 2026-07-12T11:56:34.126082+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["cryptography", "supply-chain", "go"]
cves: ["CVE-2025-8556"]
source: "https://www.botanica.software/blog/cryptographic-issues-in-cloudflares-circl-fourq-implementation"
source_name: "HN (cve)"
status: "archived"
---
- **Engineer — Plan:** If your Go codebase depends on github.com/cloudflare/circl and uses the FourQ elliptic curve (key exchange or signatures), audit that usage and schedule an upgrade; EPSS is 0.00 and no KEV listing, but a public PoC exists and cryptographic correctness flaws can enable key-recovery or signature-forgery scenarios.
- **SOC/IR — Skip**
- **Leader — Skip**
- **Signals:** CVE-2025-8556 — CISA KEV: not listed, EPSS 0.00, public PoC on GitHub
