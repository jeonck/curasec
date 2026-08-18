---
title: "Coldcard Hardware Wallet PRNG Flaw Linked to $70M Bitcoin Theft"
date: 2026-08-03T13:48:19.180160+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Learn"
tags: ["cryptography", "hardware-wallet", "supply-chain"]
cves: []
source: "https://thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Learn:** A 2021 firmware error routed Coldcard seed generation to a deterministic software PRNG instead of a hardware source, enabling full wallet recovery at scale — a textbook cautionary example for any engineer implementing cryptographic key generation. If your organization holds BTC in Coldcard devices, treat this as Act and audit key provenance immediately.
- **SOC/IR — Skip**
- **Leader — Learn:** A $70M theft traced to a firmware-level entropy flaw in a widely trusted hardware security device illustrates that hardware vendor supply chain risk extends to firmware quality; useful context if your organization holds crypto assets or relies on hardware security modules, but unlikely to require immediate board action for most enterprises.
