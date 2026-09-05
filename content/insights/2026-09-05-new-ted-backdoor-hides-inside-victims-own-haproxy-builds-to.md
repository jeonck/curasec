---
title: "Ted Backdoor Trojanizes HAProxy Builds to Intercept Web Traffic"
date: 2026-09-05T13:51:48.178400+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["linux-malware", "supply-chain", "haproxy"]
cves: []
source: "https://thehackernews.com/2026/09/new-ted-backdoor-hides-inside-victims.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No HAProxy vulnerability is involved — attackers needed prior code execution to recompile and replace the binary. This illustrates why runtime binary integrity checks (e.g., file hashing, dm-verity, or package-manager verification) on critical reverse-proxy binaries matter; no immediate patching action required.
- **SOC/IR — Learn:** The technique — compiling a backdoor directly into a modified HAProxy binary — is a stealthy persistence method worth understanding, but no IOCs, ATT&CK mappings, or broader campaign details are available from this report to act on today.
- **Leader — Skip**
