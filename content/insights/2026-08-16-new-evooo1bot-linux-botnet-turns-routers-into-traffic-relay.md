---
title: "Evooo1Bot Linux botnet hijacks routers as SOCKS5 relay nodes"
date: 2026-08-16T11:32:38.301111+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["botnet", "linux", "router-security"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Audit internet-facing gateway devices and routers for signs of Mirai-variant compromise; harden by restricting management interfaces, disabling unused services, and ensuring firmware is current — no active KEV or PoC signals yet to force immediate action.
- **SOC/IR — Plan:** Build or tune detections for anomalous SOCKS5 proxy traffic originating from edge/gateway devices; hunt for unexpected outbound relay behavior on routers in your estate since no specific IOCs are currently published.
- **Leader — Skip**
