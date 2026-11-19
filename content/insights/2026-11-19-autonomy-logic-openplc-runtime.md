---
title: "OpenPLC Runtime Race Condition Enables Unauthenticated Admin Account Creation"
date: 2026-11-19T19:29:03.442667+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["ics-ot", "race-condition", "critical-infrastructure"]
cves: ["CVE-2026-126088"]
source: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-01"
source_name: "CISA Advisories"
status: "active"
---
- **Engineer — Act:** Public PoC on GitHub and CVSS 4.0 score of 9.2 make exploitation practical now — if you run OpenPLC Runtime in any OT/ICS environment, upgrade to version 4.3.0 immediately and audit existing admin accounts for any unauthorized entries.
- **SOC/IR — Plan:** With a public PoC available, build a detection for unexpected admin account creation events on OpenPLC Runtime instances; hunt for anomalous authentication activity on OT/ICS hosts since the advisory publication date.
- **Leader — Plan:** If your organization operates in Critical Manufacturing, Energy, Transportation, or Water sectors and uses OpenPLC Runtime, assess exposure and confirm remediation is scheduled — this is not yet KEV-listed or causing headline incidents, but the public PoC shortens your window.
- **Signals:** CVE-2026-126088 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
