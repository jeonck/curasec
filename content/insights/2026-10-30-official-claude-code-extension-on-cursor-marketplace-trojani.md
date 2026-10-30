---
title: "Claude Code Cursor Extension Trojanized with Persistent SSH Backdoor"
date: 2026-10-30T17:01:08.601601+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "ssh-backdoor", "developer-tools"]
cves: []
source: "https://thehackernews.com/2026/10/official-claude-code-vs-code-extension.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** If your team uses the Claude Code extension on Cursor, audit all affected machines for version 2.1.313, check ~/.ssh/authorized_keys and running SSH tunnel processes for unauthorized entries, and rotate any credentials accessible from those developer workstations.
- **SOC/IR — Act:** Hunt across developer endpoints for the malicious extension version 2.1.313 and sweep for unauthorized SSH key additions or anomalous outbound SSH sessions from developer machines since the update was distributed; treat any hit as a potential persistent-access incident requiring IR.
- **Leader — Act:** Determine whether any engineers in your organization use the Claude Code extension on Cursor; if so, initiate an IR review — a supply-chain compromise on developer tooling means potential persistent access to source code, secrets, and cloud credentials, which warrants a leadership brief before it surfaces externally.
