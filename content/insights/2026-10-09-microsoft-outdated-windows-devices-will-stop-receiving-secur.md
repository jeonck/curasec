---
title: "Microsoft: Unsupported Windows loses updates after cert rotation"
date: 2026-10-09T17:26:04.474256+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Skip"
verdict_leader: "Plan"
tags: ["windows", "eol", "patch-management"]
cves: []
source: "https://www.bleepingcomputer.com/news/microsoft/microsoft-outdated-windows-devices-will-lose-security-protection-next-year/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Audit the estate for devices running unsupported Windows versions and schedule upgrades before the Windows Update certificate rotation deadline next year — after that point, those devices will be permanently cut off from security updates.
- **SOC/IR — Skip**
- **Leader — Plan:** Request an inventory of unsupported Windows endpoints from the engineering team; devices that fall off the update chain raise compliance risk under frameworks like PCI DSS and SOC 2, and increase exposure to unpatched vulnerabilities — factor upgrade budget into next quarter's planning.
