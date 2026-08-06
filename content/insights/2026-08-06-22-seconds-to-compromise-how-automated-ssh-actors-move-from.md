---
title: "Automated SSH Attacks Achieve Persistence in ~22 Seconds"
date: 2026-08-06T13:03:19.955458+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["ssh", "attack-automation", "detection"]
cves: []
source: "https://isc.sans.edu/diary/rss/33220"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** Research on automated SSH attack timelines underscores why key-only auth, login alerting, and session monitoring must be in place before an attacker lands — no specific patch needed, but validates hardening posture on any SSH-exposed host.
- **SOC/IR — Plan:** The ~22-second login-to-persistence window is a concrete benchmark: review SSH authentication alert latency in your SIEM and ensure post-login activity (new cron jobs, authorized_keys writes, shell spawns) triggers faster than that window closes.
- **Leader — Skip**
