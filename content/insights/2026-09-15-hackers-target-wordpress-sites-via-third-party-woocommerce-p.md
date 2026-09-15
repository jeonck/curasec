---
title: "Hackers Exploit WooCommerce Wholesale Lead Capture Plugin for PHP Backdoor"
date: 2026-09-15T15:32:56.195900+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Skip"
tags: ["wordpress", "active-exploitation", "web-shell"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-target-wordpress-sites-via-third-party-woocommerce-plugin/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Active exploitation of a critical file-upload flaw is in progress; if you run WooCommerce Wholesale Lead Capture, update or disable it immediately and audit wp-content for recently created PHP files that could be backdoors.
- **SOC/IR — Act:** PHP backdoor upload attacks against WordPress sites are active; hunt for anomalous PHP files in wp-content/uploads and similar directories, and review web logs for suspicious POST requests to this plugin's endpoints since the campaign began.
- **Leader — Skip**
