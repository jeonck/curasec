---
title: "SCKit abuses ScreenConnect to hijack technician remote sessions"
date: 2026-11-14T17:01:43.117086+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["screenconnect", "remote-access", "threat-actor"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/11/13/sckit-abuses-screenconnect-deploy-remote-access-target-technician-sessions/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Plan:** If your environment uses ScreenConnect for IT support, audit active session configurations and restrict who can initiate technician sessions; review ScreenConnect access controls and consider network segmentation for support tooling this quarter.
- **SOC/IR — Act:** Microsoft published Defender XDR hunting queries tied to SCKit's attack chain — run those hunts now against your estate and tune detections for unusual ScreenConnect session initiations, especially activity targeting privileged technician accounts.
- **Leader — Learn:** This campaign illustrates risk from legitimate remote-access tools being weaponized against IT staff; useful context for reviewing your remote-support tool policy, but no immediate board-level action required unless ScreenConnect is broadly deployed in your organization.
