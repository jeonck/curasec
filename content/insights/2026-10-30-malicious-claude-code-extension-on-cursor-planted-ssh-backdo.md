---
title: "Malicious Claude Code extension on Cursor planted SSH backdoors"
date: 2026-10-30T17:01:08.601601+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "ide-extension", "ssh-backdoor"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** If you use Cursor with the Claude Code extension, check whether you installed or updated it during the ~11-hour window on Oct 29; audit ~/.ssh/authorized_keys for unrecognized keys and rotate credentials accessible from the potentially compromised machine.
- **SOC/IR — Act:** Sweep developer workstations for unauthorized SSH authorized_keys entries added around Oct 29 and hunt for outbound beacon activity from machines running Cursor; prioritize developers with access to production systems or CI/CD pipelines.
- **Leader — Act:** Determine whether developers in your org use Cursor with the Claude Code extension; if so, direct an immediate sweep and assess whether compromised dev machines had access to sensitive systems or source code — this is the kind of developer-tooling supply-chain incident that can cascade into broader breaches.
