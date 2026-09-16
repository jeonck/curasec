---
title: "Atomic macOS Stealer (AMOS) Uses Fake Setup Guides to Steal Credentials"
date: 2026-09-16T15:25:29.032898+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["macos-malware", "credential-theft", "infostealer"]
cves: []
source: "https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/"
source_name: "Unit 42"
status: "active"
---
- **Engineer — Learn:** AMOS targets macOS endpoints via social engineering, not a vulnerability in software you patch — review whether your macOS fleet enforces Gatekeeper and restricts unsigned app installs.
- **SOC/IR — Plan:** Unit 42's analysis maps AMOS TTPs worth building detections for; queue a review of EDR telemetry for suspicious macOS credential-access patterns and staged data exfiltration consistent with this stealer.
- **Leader — Skip**
