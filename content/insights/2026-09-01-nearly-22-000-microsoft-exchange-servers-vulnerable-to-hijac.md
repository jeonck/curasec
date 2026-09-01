---
title: "22,000 Microsoft Exchange Servers Exposed to Auth Bypass Hijack"
date: 2026-09-01T15:28:52.066055+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["exchange-server", "authentication-bypass", "email-security"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/nearly-22-000-microsoft-exchange-servers-vulnerable-to-hijack-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If you run on-premises Exchange, audit internet-facing instances and apply the patch for this authentication bypass before exposure becomes exploitation; the scale of 22,000 unpatched servers makes this an attractive target even without current KEV or PoC signals.
- **SOC/IR — Learn:** No IOCs or confirmed active exploitation are cited, so there is no hunt to run today; file the attack surface (full mailbox hijack via auth bypass) to inform detection design if exploitation activity emerges.
- **Leader — Plan:** Confirm this quarter whether your organization runs on-premises Exchange and whether it is patched; the breadth of exposed servers (22,000 globally) makes this a likely board or customer question if exploitation picks up.
