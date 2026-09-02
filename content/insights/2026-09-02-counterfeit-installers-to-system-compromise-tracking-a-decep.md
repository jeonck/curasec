---
title: "Counterfeit software installers campaign delivers malware via fake download sites"
date: 2026-09-02T15:05:08.783541+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["malware", "supply-chain", "initial-access"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/09/01/counterfeit-installers-system-compromise-tracking-deceptive-software-download-campaign/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Plan:** Audit software procurement and build pipelines to ensure installers are sourced from verified vendor URLs or checksummed official releases; review SBOM/dependency sources for any unverified binaries introduced via download steps.
- **SOC/IR — Act:** Microsoft published IOCs and Defender XDR detection logic for this active campaign — sweep for the provided IOCs now and tune detections to flag execution of installer-dropped payloads from user download directories.
- **Leader — Learn:** This campaign illustrates ongoing risk from uncontrolled software procurement; useful for reinforcing software sourcing policy requirements, but no immediate leadership action is warranted absent a confirmed internal incident.
