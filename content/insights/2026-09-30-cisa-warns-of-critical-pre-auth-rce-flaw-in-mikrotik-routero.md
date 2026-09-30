---
title: "CISA warns of critical pre-auth RCE in MikroTik RouterOS"
date: 2026-09-30T16:48:49.184501+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["mikrotik", "pre-auth-rce", "network-devices"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/cisa-warns-of-critical-pre-auth-rce-flaw-in-mikrotik-routeros/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Pre-authentication RCE on a widely deployed network OS with a CISA advisory is high-priority regardless of missing EPSS/PoC signals; patch MikroTik RouterOS to the latest available version immediately, and until patched, restrict or disable remote management interfaces (Winbox, SSH, web) to trusted networks only.
- **SOC/IR — Plan:** The summary provides no IOCs, TTPs, or ATT&CK mappings to hunt on today; queue a detection build for anomalous management-plane traffic to MikroTik devices and prepare an assume-breach sweep playbook for network infrastructure in case active exploitation evidence surfaces.
- **Leader — Plan:** Confirm whether MikroTik RouterOS appears in your network or vendor inventory and direct engineering to treat patching as this-sprint priority; CISA advisories on critical network-device flaws frequently precede board-level questions when exploitation becomes public.
