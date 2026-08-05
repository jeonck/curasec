---
title: "New XCSSET variant targets macOS devs via compromised Xcode projects"
date: 2026-08-05T13:01:27.566949+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["macos", "supply-chain", "malware"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/new-xcsset-variant-targets-macos-devs-via-compromised-xcode-projects/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** If your team uses Xcode or pulls macOS Swift/ObjC projects from GitHub, audit your local Xcode project files and CI runners for XCSSET indicators; verify integrity of any third-party Xcode project dependencies before building.
- **SOC/IR — Plan:** Build or tune detections for XCSSET staging behaviors on macOS endpoints (e.g., suspicious Xcode project modifications, unexpected LaunchAgent/LaunchDaemon persistence); review EDR coverage for macOS developer machines.
- **Leader — Learn:** Supply-chain compromise via developer tooling is a recurring risk pattern worth noting for future policy on approved Xcode project sources and macOS developer workstation standards.
