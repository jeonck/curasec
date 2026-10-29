---
title: "Chrome extensions with 13.4M installs caught hijacking searches"
date: 2026-10-29T17:24:45.058738+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["chrome-extensions", "supply-chain", "adware"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/chrome-extensions-with-134-million-installs-caught-hijacking-searches/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Enterprises with unmanaged Chrome deployments have real exposure here. Obtain the list of 319 extension IDs from BleepingComputer's reporting, audit managed Chrome environments via the Extension Management policy, and blocklist or remove any matches.
- **SOC/IR — Plan:** Retrieve the tracking/redirect domains associated with the campaign and create proxy or DNS detections for search queries being routed through third-party advertising servers; also sweep historic proxy logs for hits against those domains since installation dates.
- **Leader — Learn:** A 13.4M-install adware campaign is a useful data point for justifying a browser extension governance policy — this reinforces the case for allowlisting or vetting Chrome extensions in managed enterprise environments, but there is no immediate leadership action unless internal exposure is confirmed.
