---
title: "DIVD breach traced to chained Zammad zero-days"
date: 2026-10-01T17:21:52.102295+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["zero-day", "zammad", "open-source"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/divd-says-zammad-zero-days-enabled-ai-driven-network-breach/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If you self-host Zammad, identify available patches for these two chained zero-days and schedule an emergency upgrade; no KEV listing or public PoC is confirmed yet, but exploitation was demonstrated in a real breach.
- **SOC/IR — Learn:** The breach illustrates how chained zero-days in support tooling can pivot to broader network access, but the summary provides no IOCs or ATT&CK-mappable TTPs to act on today.
- **Leader — Plan:** Audit whether Zammad is in your internal or vendor tooling stack; if so, request patch confirmation from the responsible team before month end given confirmed real-world exploitation.
