---
title: "Check Point gateways exploited via PHP2Shell to deploy ESXi wiper"
date: 2026-11-14T17:01:43.117086+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["check-point", "esxi-wiper", "active-exploitation"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/check-point-gateways-hacked-via-php2shell-to-deploy-vmware-esxi-wiper/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Active exploitation of Check Point Security Gateways is delivering destructive VMware ESXi wiper malware. Patch Check Point gateways to the latest available release immediately and audit ESXi hosts for signs of wiper activity or unexpected filesystem modification.
- **SOC/IR — Act:** Active campaign uses PHP2Shell web shells on Check Point gateways to pivot to ESXi and execute wiper malware. Hunt for PHP2Shell artifacts in gateway logs and anomalous ESXi mass-delete or volume-encryption events; treat any Check Point gateway as potentially compromised until swept.
- **Leader — Act:** Destructive wiper malware being deployed via Check Point gateway compromises could cause irreversible data loss in VMware environments. Confirm whether the organization runs Check Point Security Gateways and direct the team to assess exposure; wiper-class attacks warrant a leadership heads-up before they surface externally.
