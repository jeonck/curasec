---
title: "Microsoft removes WMIC LOLBin from Windows 11 24H2 and 25H2"
date: 2026-08-18T11:37:25.033598+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["lolbin", "windows-hardening", "wmic"]
cves: []
source: "https://www.bleepingcomputer.com/news/microsoft/microsoft-removes-wmic-lolbin-tool-in-windows-11-beta-builds/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Audit internal scripts, pipelines, and automation that call WMIC and migrate them to PowerShell WMI cmdlets before the 24H2/25H2 rollout reaches your fleet; breakage is silent until WMIC is absent.
- **SOC/IR — Plan:** Update detection logic: WMIC execution on Windows 11 24H2+ will become anomalous and warrant a higher-fidelity alert; also build coverage for alternative WMI access paths (PowerShell, wbemtest) that threat actors will pivot to.
- **Leader — Learn:** Microsoft's removal of a widely abused built-in tool reduces Windows 11 attack surface over time; no leadership action needed, but useful context when discussing OS hardening posture with auditors or the board.
