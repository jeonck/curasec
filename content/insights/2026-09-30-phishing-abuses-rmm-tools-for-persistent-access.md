---
title: "Phishing Campaigns Abuse MSP360 RMM to Deploy ScreenConnect Backdoors"
date: 2026-09-30T16:48:49.184501+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["rmm-abuse", "phishing", "persistent-access"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/09/29/phishing-abuses-rmm-tools-persistent-access/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Plan:** Audit your environment for unauthorized ScreenConnect or MSP360 installations; enforce an approved-software allowlist for remote management tools and review recent RMM deployments against your IT change log.
- **SOC/IR — Plan:** Build or tune detections for unexpected RMM binary executions (MSP360, ScreenConnect) outside your approved management estate; create a hunt query for remote-access tools installed in the past 30 days that don't match IT provisioning records.
- **Leader — Learn:** Documents a growing pattern of threat actors weaponizing legitimate remote-management software to evade controls; useful context for a quarterly risk review of MSP or RMM-tool exposure, but no immediate leadership action is indicated by the available signals.
