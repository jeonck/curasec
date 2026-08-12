---
title: "Microsoft August Patch Tuesday: 398 Fixes, Windows Driver LPE Zero-Day Exploited"
date: 2026-08-12T11:57:00.937865+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["windows-lpe", "patch-tuesday", "zero-day"]
cves: ["CVE-2026-68820"]
source: "https://thehackernews.com/2026/08/microsoft-patches-398-flaws-including.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** CVE-2026-68820 is CISA KEV-listed with a public GitHub PoC and confirmed active exploitation — apply August 2026 Patch Tuesday updates immediately, prioritizing this kernel driver fix to close the SYSTEM-level LPE path.
- **SOC/IR — Act:** Active in-the-wild exploitation of a SYSTEM-level LPE means attackers may already have escalated on unpatched endpoints — hunt for anomalous SYSTEM-privilege process spawns from unexpected parent processes and tune EDR alerts for T1068 kernel-driver abuse since the public PoC widens attacker access.
- **Leader — Plan:** A 398-patch batch with one actively exploited zero-day may strain standard patch SLAs — confirm your teams have triaged CVE-2026-68820 as this week's priority and verify compliance with your critical-patch SLA before the next board or audit checkpoint.
- **Signals:** CVE-2026-68820 — CISA KEV: listed, EPSS n/a, public PoC on GitHub
