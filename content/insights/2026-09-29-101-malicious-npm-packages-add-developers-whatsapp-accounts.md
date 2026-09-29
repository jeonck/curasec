---
title: "101 Malicious npm Packages Enroll Developers in WhatsApp Groups (PhantomSub)"
date: 2026-09-29T16:53:02.010350+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["npm-supply-chain", "malicious-packages", "supply-chain"]
cves: []
source: "https://thehackernews.com/2026/09/101-malicious-npm-packages-add.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** 101 confirmed malicious npm packages are live in the registry; audit your dependency tree against the full package list published by OX Security and remove any matches — the current payload is WhatsApp group enrollment, but the supply-chain foothold could be updated to deliver worse payloads.
- **SOC/IR — Learn:** PhantomSub is a novel abuse of the Baileys WhatsApp library for subscriber manipulation; no IOCs, SIEM-ready signatures, or ATT&CK mappings are surfaced in the summary, so there is no immediate detection work to do but the technique is worth cataloging.
- **Leader — Skip**
