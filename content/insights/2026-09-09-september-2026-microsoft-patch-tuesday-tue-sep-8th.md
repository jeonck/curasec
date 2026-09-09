---
title: "Microsoft Sept 2026 Patch Tuesday: 973 CVEs, 2 Actively Exploited"
date: 2026-09-09T15:05:56.552281+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["patch-tuesday", "microsoft", "rce"]
cves: []
source: "https://isc.sans.edu/diary/rss/33320"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Act:** Two vulnerabilities are confirmed exploited in the wild, including a Windows privilege escalation; prioritize patching those plus the critical RCEs in Skype for Business, MSMQ, and RRAS within your emergency patch window — review the full advisory to identify the two KEV-grade CVEs by number and verify patch deployment within 48–72 hours.
- **SOC/IR — Plan:** With two actively exploited vulns (including a Windows privesc) but no IOCs provided here, queue detection work this week: pull the specific CVE IDs from Microsoft's release, map the exploited privesc to relevant ATT&CK techniques, and tune alerts for anomalous privilege elevation on unpatched Windows hosts.
- **Leader — Learn:** The 973-CVE release is the largest Patch Tuesday on record and may surface in board or customer conversations; useful context for communicating why patch velocity investment matters, but the two actively exploited issues are not yet a named systemic event requiring leadership escalation.
