---
title: "Widespread PHP RCE Flaws Actively Exploited, 70% of Sites at Risk"
date: 2026-10-21T15:56:43.831517+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["php", "rce", "active-exploitation"]
cves: []
source: "https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/"
source_name: "Krebs on Security"
status: "active"
---
- **Engineer — Act:** Working exploits are in use against a pair of PHP flaws enabling full server takeover, affecting the majority of PHP deployments. Patch PHP to the latest stable release immediately and verify no web shells or unauthorized processes exist on PHP-backed servers.
- **SOC/IR — Act:** Active in-the-wild exploitation of a widespread PHP RCE means assume-breach posture is warranted for any PHP-backed systems. Hunt for anomalous child processes spawned from web server processes and audit PHP server logs for signs of exploitation since today.
- **Leader — Act:** A pair of actively exploited PHP flaws affecting roughly 70% of websites is a systemic event likely to generate board and customer questions. Confirm whether company-operated PHP properties and key SaaS vendors are exposed, and be prepared to brief leadership this week.
