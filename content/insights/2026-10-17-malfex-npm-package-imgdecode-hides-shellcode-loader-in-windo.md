---
title: "Malicious npm Package 'imgdecode' Delivers Shellcode Loader via Windows Native Addon"
date: 2026-10-17T14:12:31.177036+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["supply-chain", "npm", "malware"]
cves: []
source: "https://thehackernews.com/2026/10/malfex-npm-package-imgdecode-hides.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active supply-chain threat still live on npm; audit all dependency trees (including transitives) for 'imgdecode' and remove it immediately if found, then scan CI/CD build logs for any unexpected native addon compilation on Windows hosts.
- **SOC/IR — Act:** Hunt for 'imgdecode' in software inventories and package-lock/yarn.lock files across the estate; on Windows endpoints, look for anomalous child processes spawned under node.exe as a behavioral indicator of the shellcode loader executing.
- **Leader — Learn:** Another npm supply-chain implant in a live campaign (MALFEX) reinforces the risk of unvetted open-source dependencies; useful justification for prioritizing software composition analysis (SCA) tooling investment if not already in place.
