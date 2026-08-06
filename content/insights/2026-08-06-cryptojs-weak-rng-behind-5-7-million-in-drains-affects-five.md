---
title: "CryptoJS Weak RNG Linked to $5.7M Crypto Wallet Drains"
date: 2026-08-06T13:03:19.955458+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["weak-rng", "supply-chain", "cryptography"]
cves: []
source: "https://thehackernews.com/2026/08/cryptojs-weak-rng-behind-57-million-in.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Audit any use of CryptoJS.lib.WordArray.random() in your codebase — it provides insufficient entropy for cryptographic key generation; replace with Web Crypto API's crypto.getRandomValues() immediately and review whether any generated secrets need rotation.
- **SOC/IR — Learn:** Active drains are targeting end-user crypto wallets rather than enterprise estates; no enterprise-relevant IOCs or ATT&CK-mappable TTPs are present, but the weak-RNG exploitation pattern is worth tracking for future detection design.
- **Leader — Skip**
