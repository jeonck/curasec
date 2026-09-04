---
title: "77 Open VSX extensions caught harvesting developer environment data"
date: 2026-08-05T13:01:27.566949+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["supply-chain", "malicious-extensions", "developer-tools"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/77-open-vsx-extensions-found-harvesting-developer-info/"
source_name: "BleepingComputer"
status: "archived"
---
- **Engineer — Act:** If your team uses Open VSX (common in VS Code OSS or VSCodium environments), audit installed extensions against the removed list and purge any matches; review extension installation policies in CI/CD or dev container configs to restrict to known-good sources.
- **SOC/IR — Plan:** Build or tune detections for unexpected outbound connections from IDE processes (code, codium) to unknown endpoints; consider hunting for extension-related network activity in EDR telemetry from developer workstations over the past 90 days.
- **Leader — Learn:** This incident illustrates ongoing supply-chain risk in developer tooling marketplaces; useful context for evaluating software vetting policies in engineering onboarding, but no immediate leadership action required.
