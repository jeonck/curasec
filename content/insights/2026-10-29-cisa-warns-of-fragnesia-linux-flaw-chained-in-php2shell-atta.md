---
title: "CISA KEV: Linux Kernel Flaw Chained with PHP2Shell in Active Attacks"
date: 2026-10-29T17:24:45.058738+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["linux-kernel", "privilege-escalation", "active-exploitation"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/cisa-warns-of-fragnesia-linux-flaw-chained-in-php2shell-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** CISA KEV listing confirms active exploitation; patch Linux kernel to the remediated version immediately on any internet-facing or multi-tenant Linux hosts, prioritizing those running PHP-based web applications where the PHP2Shell initial-access vector applies.
- **SOC/IR — Act:** Active chained exploitation means assume-breach posture on Linux web servers; hunt for PHP web shell artifacts (unusual PHP child process spawning, outbound connections from web server processes) followed by local privilege escalation behavior since the CISA advisory date.
- **Leader — Plan:** CISA KEV listing signals active exploitation but this is a patch-and-detect operational issue; confirm engineering teams have the Linux kernel patch queued as priority-one this sprint and verify SOC has added detection coverage for the attack chain.
