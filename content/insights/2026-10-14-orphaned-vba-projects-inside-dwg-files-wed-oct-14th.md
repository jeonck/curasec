---
title: "Orphaned VBA Projects Found Embedded in AutoCAD DWG Files"
date: 2026-10-14T15:48:57.203933+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["vba-macros", "file-format", "malware-delivery"]
cves: []
source: "https://isc.sans.edu/diary/rss/33420"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Learn:** Highlights that DWG files can carry embedded VBA projects, a non-obvious attack surface if AutoCAD or DWG-processing pipelines are in scope; no exploitation signal or patch action required today.
- **SOC/IR — Learn:** Awareness that DWG files can conceal executable macro content is useful for tuning file-type inspection rules, but no IOCs or active campaign are described here.
- **Leader — Skip**
