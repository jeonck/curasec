---
title: "Jscrambler npm package backdoored with infostealer malware"
date: 2026-07-14T12:08:08.109802+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["supply-chain", "npm", "infostealer"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-backdoor-jscrambler-npm-package-with-infostealer-malware/"
source_name: "BleepingComputer"
status: "archived"
---
- **Engineer — Act:** Audit all projects and CI/CD pipelines for the malicious Jscrambler npm version; if found, treat the build environment as compromised and rotate any credentials or tokens accessible during that build.
- **SOC/IR — Act:** Search CI/CD and build system logs for installations of the malicious Jscrambler package, then hunt for infostealer exfiltration activity (credential theft, unexpected outbound connections) on any hosts where it executed.
- **Leader — Plan:** A supply-chain attack on a security vendor's npm package (~1,500 downloads) underscores third-party software risk; confirm whether your org consumes Jscrambler's npm package and, if so, request their incident timeline and impact report.
