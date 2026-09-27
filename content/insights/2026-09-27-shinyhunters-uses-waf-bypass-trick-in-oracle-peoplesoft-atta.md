---
title: "ShinyHunters bypasses WAF mitigations for Oracle PeopleSoft CVE-2026-35273"
date: 2026-09-27T15:38:27.651895+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["oracle-peoplesoft", "waf-bypass", "active-exploitation"]
cves: ["CVE-2026-35273"]
source: "https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** CVE-2026-35273 is CISA KEV-listed with active exploitation; WAF-based mitigations are being circumvented via URL-encoding tricks, so apply Oracle's vendor patch directly rather than relying on WAF rules — do not treat a WAF rule as a substitute for patching.
- **SOC/IR — Act:** ShinyHunters is actively exploiting internet-facing PeopleSoft instances; hunt for URL-encoding anomalies in WAF and web server logs, sweep PeopleSoft access logs since KEV listing date for exploitation indicators, and flag any PeopleSoft-exposed assets for assume-breach review.
- **Leader — Act:** ShinyHunters is an extortion actor now actively compromising PeopleSoft (an HR/ERP system often holding sensitive employee and financial data); confirm whether your org runs PeopleSoft, verify patch status with the responsible team, and brief leadership on extortion exposure before this surfaces in the news.
- **Signals:** CVE-2026-35273 — CISA KEV: listed, EPSS 0.09, public PoC on GitHub, reported by 2 collected sources
