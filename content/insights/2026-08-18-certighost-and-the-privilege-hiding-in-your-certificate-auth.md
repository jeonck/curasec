---
title: "CVE-2026-54121: Domain User to Domain Controller via Enterprise CA"
date: 2026-08-18T11:37:25.033598+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["active-directory", "privilege-escalation", "pki"]
cves: ["CVE-2026-54121"]
source: "https://www.bleepingcomputer.com/news/security/certighost-and-the-privilege-hiding-in-your-certificate-authority/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** A public PoC exists for a flaw that lets any domain user compromise the Enterprise CA at Domain Controller privilege level — patch CVE-2026-54121 immediately, then audit certificate templates and CA permissions for standing privilege that survives the patch.
- **SOC/IR — Plan:** With a public PoC available but no active exploitation confirmed, build detections for anomalous ADCS activity: unusual certificate enrollment requests by standard users, low-privileged accounts invoking CA RPC interfaces, or certificates issued against sensitive templates — these are the behavioral signals that precede weaponization of this class of bug.
- **Leader — Plan:** This is a useful forcing function to confirm your PKI infrastructure is formally classified and defended as Tier 0 — ask your team to verify the Enterprise CA is in scope for your privileged-access model and that the patch is on an expedited timeline given the public PoC.
- **Signals:** CVE-2026-54121 — CISA KEV: not listed, EPSS 0.01, public PoC on GitHub
