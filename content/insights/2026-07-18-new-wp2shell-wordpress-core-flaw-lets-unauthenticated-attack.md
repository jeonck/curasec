---
title: "WordPress Core wp2shell Flaw Enables Unauthenticated RCE"
date: 2026-07-18T11:51:11.203777+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["wordpress", "rce", "unauthenticated"]
cves: []
source: "https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Public PoC is available for an unauthenticated RCE in WordPress core affecting 6.9 and 7.0 with no plugins required — patch every WordPress instance to the fixed version immediately and audit web server file systems for newly dropped shells or unexpected PHP files.
- **SOC/IR — Act:** A public PoC for unauthenticated RCE in WordPress core means active exploitation is likely underway; sweep web access logs for anomalous POST patterns against wp-admin and wp-includes endpoints, and hunt for new or modified PHP files and unexpected child processes spawned by the web server process since the disclosure date.
- **Leader — Act:** Unauthenticated RCE in WordPress core with a working public exploit is a systemic exposure for any org running WordPress-powered properties; confirm inventory of WordPress versions across customer-facing and internal sites, verify engineering has prioritized emergency patching, and assess whether key SaaS or media vendors in your supply chain are exposed.
