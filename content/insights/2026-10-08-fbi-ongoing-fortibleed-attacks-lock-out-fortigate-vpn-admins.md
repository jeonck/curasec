---
title: "FBI: Ongoing FortiBleed attacks locking out FortiGate VPN admins"
date: 2026-10-08T17:51:36.071186+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["fortinet", "vpn-appliance", "active-exploitation"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/fbi-ongoing-fortibleed-attacks-lock-out-fortigate-vpn-admins/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** FortiGate firewalls and SSL VPN gateways are common enterprise edge devices; an active FBI-warned campaign locking out admins signals credential theft or config tampering at scale. Audit all FortiGate admin accounts for unauthorized additions or password changes, verify firmware is at latest patched version, and review admin-access logs from at least the past 30 days.
- **SOC/IR — Act:** Admin lockout is a concrete post-exploitation TTP indicating attackers have achieved privileged access to edge devices before defenders can respond. Hunt for unauthorized admin account creation or privilege changes on FortiGate devices since October 2026, and initiate assume-breach review of any network segments fronted by affected appliances.
- **Leader — Act:** An FBI advisory on a named, ongoing campaign against a widely-deployed enterprise VPN product warrants immediate internal exposure check. Confirm whether your environment runs FortiGate, get a status report from the network team this week, and be prepared to brief leadership on containment posture if exposure is confirmed.
