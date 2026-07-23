---
title: "CVE-2026-64600: XFS race condition enables Linux local root escalation"
date: 2026-07-23T12:47:45.543557+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["linux-kernel", "privilege-escalation", "local-exploit"]
cves: ["CVE-2026-64600"]
source: "https://www.bleepingcomputer.com/news/linux/new-refluxfs-linux-flaw-lets-attackers-gain-root-privileges/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Public PoC on GitHub makes this LPE practically weaponizable on any Linux system using XFS (common on RHEL/CentOS derivatives); patch the kernel to the version fixing CVE-2026-64600 and prioritize systems where XFS is the root or primary filesystem.
- **SOC/IR — Learn:** Local privilege escalation via a kernel race condition offers a thin detection surface — no active campaign and no IOCs reported; note as a post-foothold escalation path attackers may chain after initial access, and revisit if exploit tooling appears in threat-actor toolkits.
- **Leader — Skip**
- **Signals:** CVE-2026-64600 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub, reported by 2 collected sources
