---
title: "SharePoint CVE-2026-65660 Reclassified as Authenticated RCE"
date: 2026-09-22T15:30:54.753130+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["sharepoint", "rce", "cve"]
cves: ["CVE-2026-65660"]
source: "https://thehackernews.com/2026/09/sharepoint-flaw-initially-listed-as.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** The CVSS 6.5 spoofing label may have caused teams to deprioritize this patch; full technical details are now public, raising PoC risk. Patch SharePoint Server 2016, 2019, and Subscription Edition to the vendor-supplied fix before a PoC materializes.
- **SOC/IR — Plan:** With detailed exploit mechanics now public, exploitation attempts are more likely in coming weeks. Build or stage SharePoint-targeted authenticated RCE hunt queries now so you can sweep quickly if active exploitation is reported.
- **Leader — Skip**
- **Signals:** CVE-2026-65660 — CISA KEV: not listed, EPSS 0.01, no public PoC found
