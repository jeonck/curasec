---
title: "ModHeader Extension Pulled After Dormant Browser-History Collector Discovered"
date: 2026-07-14T12:08:08.109802+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["supply-chain", "browser-extension", "dormant-malware"]
cves: []
source: "https://thehackernews.com/2026/07/google-and-microsoft-pull-modheader.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Act:** ModHeader is widely used by engineers for API and header debugging — remove it from all developer and CI browsers now and replace with a vetted alternative; dormant or not, undisclosed collection code in a tool with store-level trust is a supply-chain red flag.
- **SOC/IR — Plan:** No active exploitation or IOCs to sweep for, but this is a prompt to audit the browser extension inventory across developer workstations and establish an approved-extension policy or detection for unapproved extension installs.
- **Leader — Learn:** No data was collected and both stores have already pulled the extension, so no breach disclosure or vendor inquiry is warranted; useful data point on browser-extension supply-chain risk when building or updating software-inventory and vendor-vetting policies.
