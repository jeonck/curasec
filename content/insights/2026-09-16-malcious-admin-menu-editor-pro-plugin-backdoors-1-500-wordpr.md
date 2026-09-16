---
title: "Malicious Admin Menu Editor Pro plugin backdoors 1,500 WordPress sites"
date: 2026-09-16T15:25:29.032898+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["supply-chain", "wordpress", "backdoor"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/malcious-admin-menu-editor-pro-plugin-backdoors-1-500-wordpress-sites/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** If you distribute or run WordPress with Admin Menu Editor Pro, audit all admin-level user accounts immediately for hidden/unauthorized entries and remove or replace the plugin with a verified clean version.
- **SOC/IR — Act:** Sweep WordPress admin user tables across managed estates for accounts created after plugin update dates; hunt for unexpected privileged-user creation events in web application logs correlated with this plugin's presence.
- **Leader — Learn:** A small-scale but clean example of plugin supply-chain compromise via maintainer-site takeover; useful context for vendor/third-party software risk discussions, but scale (~200 customers) does not rise to board-level action unless your org runs this specific plugin.
