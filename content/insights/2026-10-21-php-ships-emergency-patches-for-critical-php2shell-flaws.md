---
title: "PHP ships emergency patches for critical PHP2Shell RCE flaws"
date: 2026-10-21T15:56:43.831517+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["rce", "php", "vulnerability"]
cves: ["CVE-2026-109618", "CVE-2026-109619"]
source: "https://www.bleepingcomputer.com/news/security/php-ships-emergency-patches-for-critical-php2shell-flaws/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Two critical RCE flaws with public PoCs on GitHub mean exploitation is practical now; patch all PHP installations to the emergency-release version immediately and audit web server logs for signs of pre-patch exploitation.
- **SOC/IR — Act:** Public PoCs for both CVEs make exploitation attempts imminent if not already occurring; hunt for web shell creation events and anomalous PHP process execution since PoC publication, and tune WAF/EDR rules for PHP shell upload patterns.
- **Leader — Plan:** Critical RCE in a widely deployed runtime with public PoCs warrants confirming your PHP inventory and ensuring engineering prioritizes the emergency patch this week; not yet at board-briefing threshold absent confirmed mass exploitation.
- **Signals:** CVE-2026-109618 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub, reported by 4 collected sources · CVE-2026-109619 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub, reported by 3 collected sources
