---
title: "737 fake Chrome VPN extensions route traffic via rogue SOCKS5 proxies"
date: 2026-08-13T11:57:16.146981+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["browser-extensions", "supply-chain", "proxy"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hundreds-of-fake-chrome-vpn-extensions-route-traffic-through-a-proxy/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Audit any corporate-managed Chrome extensions against a blocklist of the 737 identified fakes; establish a policy requiring allowlisted extensions only for managed devices.
- **SOC/IR — Plan:** Build detection for unusual SOCKS5 proxy egress from endpoints, and consider hunting for browser extension IDs associated with this campaign in endpoint telemetry.
- **Leader — Learn:** Illustrates scale of Chrome Web Store supply-chain risk for enterprise endpoints; useful context for policy decisions around browser extension governance, but no immediate board-level action required.
