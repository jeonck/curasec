---
title: "Classic CGI Email Script Vulnerabilities (CVE-2000-0411) Revisited"
date: 2026-11-04T18:40:06.241551+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["legacy-vulnerabilities", "cgi-scripts", "web-application"]
cves: ["CVE-2000-0411"]
source: "https://isc.sans.edu/diary/rss/33488"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** A retrospective on 26-year-old CGI email script flaws (env variable leakage, header injection, sendmail command injection) that may still lurk in legacy environments; worth auditing for any surviving CGI-bin scripts, but EPSS 0.08 and no KEV listing mean there's no urgent patching pressure.
- **SOC/IR — Skip**
- **Leader — Skip**
- **Signals:** CVE-2000-0411 — CISA KEV: not listed, EPSS 0.08, no public PoC found
