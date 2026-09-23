---
title: "Malicious npm Package tw-pkgprobe-7731 Targets Twilio Devs, Steals Creds"
date: 2026-09-23T15:27:03.663698+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Skip"
tags: ["supply-chain", "npm", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/09/malicious-npm-package-poses-as-twilio.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A live malicious npm package impersonating a Twilio security tool can exfiltrate credentials from developer environments. Audit npm dependency trees and CI/CD install logs for 'tw-pkgprobe-7731' and ensure no project has pulled it since mid-August 2026.
- **SOC/IR — Act:** The package name 'tw-pkgprobe-7731' (uploaded by 'twdepprobe7731') is a concrete IOC; sweep CI/CD pipeline logs and artifact registries since mid-August 2026 for any installation or download of this package to identify potential credential exposure.
- **Leader — Skip**
