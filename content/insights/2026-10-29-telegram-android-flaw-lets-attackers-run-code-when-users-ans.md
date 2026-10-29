---
title: "Telegram Android RCE Triggered by Answering Voice Calls, Patched in v12.10.4"
date: 2026-10-29T17:24:45.058738+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["rce", "android", "mobile"]
cves: []
source: "https://thehackernews.com/2026/10/telegram-android-flaw-lets-attackers.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** One-interaction RCE requiring only an attacker Telegram account is a high-severity mobile risk; verify corporate or BYOD devices are running Telegram ≥ 12.10.4 via MDM policy or device-compliance checks. No exploitation signals yet, so this is a patch-window item rather than emergency.
- **SOC/IR — Learn:** No active exploitation, IOCs, or ATT&CK-mappable TTPs have been published; the voice-call RCE vector is worth logging for context when triaging future mobile-related incidents, but there is nothing actionable to detect or hunt today.
- **Leader — Skip**
