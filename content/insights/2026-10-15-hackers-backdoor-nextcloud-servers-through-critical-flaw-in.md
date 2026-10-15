---
title: "Collabora CODE Server Flaw Used to Backdoor Nextcloud Servers"
date: 2026-10-15T15:35:13.586755+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["nextcloud", "web-shell", "active-exploitation"]
cves: []
source: "https://thehackernews.com/2026/10/hackers-backdoor-nextcloud-servers.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active exploitation confirmed with web shells planted on Nextcloud servers since at least September 10. If you run Nextcloud with the Collabora Online Built-in CODE Server app, audit for web shell files in the web root and disable or patch the plugin immediately.
- **SOC/IR — Act:** Confirmed active exploitation with web shell deployment provides a concrete hunt target — sweep Nextcloud server logs for anomalous command execution spawned by the web server process dating back to September 10, and look for unauthorized files in Nextcloud's web-accessible directories.
- **Leader — Plan:** Active backdooring of Nextcloud deployments via an optional collaboration plugin is a real risk if the organization runs self-hosted Nextcloud — confirm with engineering whether this plugin is in use and that incident response is underway; not yet a board-level event.
