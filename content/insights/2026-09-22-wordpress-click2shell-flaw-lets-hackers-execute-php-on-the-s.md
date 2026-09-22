---
title: "WordPress Core 'Click2Shell' CSRF flaw enables PHP execution"
date: 2026-09-22T15:30:54.753130+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["wordpress", "csrf", "rce"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/wordpress-click2shell-flaw-lets-hackers-execute-php-on-the-server/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** A public PoC now lowers the exploitation bar for this CSRF-to-PHP-execution flaw in WordPress Core; patch WordPress to the latest patched release and verify that admin-facing endpoints require nonce validation.
- **SOC/IR — Plan:** No confirmed active exploitation yet, but a public PoC means campaigns are likely imminent; build or tune detections for anomalous PHP execution originating from WordPress admin paths and unexpected file-write activity on web roots.
- **Leader — Learn:** A meaningful WordPress Core vulnerability with a published exploit — not yet at systemic scale, but worth confirming your engineering team has patched any WordPress instances; no board-level action required unless exploitation becomes widespread.
