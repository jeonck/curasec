---
title: "YARA Rule: Detecting Orphaned VBA Projects in DWG Files"
date: 2026-10-18T14:33:13.167038+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["yara", "malware-detection", "file-analysis"]
cves: []
source: "https://isc.sans.edu/diary/rss/33434"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** Highlights DWG files as a plausible malware delivery surface via embedded VBA projects — worth considering when designing file-upload scanning policies or reviewing which file types are allowed through email/storage pipelines.
- **SOC/IR — Plan:** Concrete YARA rule for detecting hidden VBA projects in AutoCAD DWG files — worth adding to your YARA ruleset to improve coverage of this evasion/delivery technique; no active exploitation signals, so this is a detection gap to close this quarter rather than an urgent hunt.
- **Leader — Skip**
