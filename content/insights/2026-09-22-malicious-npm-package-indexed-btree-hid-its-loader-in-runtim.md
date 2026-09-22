---
title: "Malicious npm Package indexed-btree Hid Loader in Runtime Code"
date: 2026-09-22T15:30:54.753130+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["supply-chain", "npm", "malware"]
cves: []
source: "https://thehackernews.com/2026/09/malicious-npm-package-indexed-btree-hid.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Audit lock files and build artifacts for indexed-btree (a typosquat of sorted-btree); more broadly, review whether your static analysis and SCA tooling scans runtime-embedded code, not just lifecycle scripts, since this tactic shift evades install-hook detections.
- **SOC/IR — Learn:** The shift from lifecycle-script loaders to runtime-embedded payloads is a meaningful detection-evasion evolution worth tracking — no IOCs or ATT&CK-mappable TTPs were published, so no immediate hunt is actionable.
- **Leader — Skip**
