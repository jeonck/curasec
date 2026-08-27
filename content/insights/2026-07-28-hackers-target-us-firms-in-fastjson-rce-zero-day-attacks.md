---
title: "FastJson RCE zero-day actively exploited against US firms"
date: 2026-07-28T13:01:43.287328+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["zero-day", "rce", "java"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-target-us-firms-in-fastjson-rce-zero-day-attacks/"
source_name: "BleepingComputer"
status: "archived"
---
- **Engineer — Act:** FastJson is widely used in Java applications; if your codebase or dependencies include it, audit immediately and apply any available patch or mitigations — if no patch exists, consider disabling unsafe deserialization features or replacing the library.
- **SOC/IR — Act:** Active exploitation is underway against US firms; hunt for anomalous outbound connections or process spawning from Java application servers since this week, and tune detections for RCE post-exploitation behavior (e.g., web shells, unexpected child processes).
- **Leader — Plan:** Active zero-day targeting US organizations warrants asking your engineering team this week whether FastJson is in use and what the mitigation timeline is — this may generate customer questions if it widens.
