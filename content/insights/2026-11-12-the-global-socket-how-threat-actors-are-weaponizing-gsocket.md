---
title: "GSocket weaponized for stealthy Linux C2 persistence post-patch"
date: 2026-11-12T18:52:40.662404+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Skip"
tags: ["linux", "c2", "persistence"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Plan:** GSocket can survive patching the initial vulnerability, so audit Linux servers for unexpected GSocket binaries or processes this quarter; review outbound encrypted tunnels in firewall logs as a baseline.
- **SOC/IR — Act:** Microsoft published detection, investigation, and remediation guidance — hunt for GSocket installations on Linux hosts now and build a Sigma/SPL rule to alert on GSocket process execution or its characteristic network behavior.
- **Leader — Skip**
