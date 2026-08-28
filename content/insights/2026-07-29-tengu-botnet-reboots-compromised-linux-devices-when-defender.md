---
title: "Tengu Botnet Uses Hardware Watchdog to Survive Process Kills on Linux"
date: 2026-07-29T13:07:14.832066+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["botnet", "linux", "persistence"]
cves: []
source: "https://thehackernews.com/2026/07/tengu-botnet-reboots-compromised-linux.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Plan:** Any Linux device with Telnet exposed and weak credentials is a candidate target; audit your estate for Telnet listeners, disable them, and review hardware watchdog configurations on edge/IoT devices so defenders can't be stymied by the reboot-on-kill mechanism.
- **SOC/IR — Plan:** Build or tune detections for Telnet brute-force login bursts against Linux endpoints and flag unexpected device reboots following process termination events; update IR runbooks to account for the watchdog reboot loop before attempting to kill botnet processes on compromised hosts.
- **Leader — Learn:** A novel DDoS botnet persistence technique that complicates incident response on Linux devices — no immediate leadership action required, but useful context if DDoS risk or IoT/edge device exposure comes up in a risk review.
