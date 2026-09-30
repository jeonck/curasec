---
title: "CrowdStrike explains ClickFix social-engineering attack technique"
date: 2026-09-30T16:48:49.184501+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["clickfix", "social-engineering", "endpoint"]
cves: []
source: "https://www.crowdstrike.com/en-us/blog/how-clickfix-attacks-work-and-how-to-stop-them/"
source_name: "CrowdStrike Blog"
status: "active"
---
- **Engineer — Learn:** ClickFix abuses clipboard/paste UI to trick users into running malicious commands; worth understanding to inform developer guidance and hardening of endpoint policies, but no patch or config change required.
- **SOC/IR — Plan:** ClickFix is a growing initial-access technique worth building detections for — hunt for suspicious PowerShell or cmd execution triggered from browser/clipboard context, and review CrowdStrike's behavioral indicators.
- **Leader — Skip**
