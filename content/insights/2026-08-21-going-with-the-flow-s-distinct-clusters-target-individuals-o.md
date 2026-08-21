---
title: "Russian Clusters UNC6293/UNC7005/UNC5976 Abuse OAuth Flows in Espionage Campaigns"
date: 2026-08-21T11:38:25.806134+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["russian-apt", "oauth-abuse", "espionage"]
cves: []
source: "https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia/"
source_name: "Google Threat Intelligence"
status: "active"
---
- **Engineer — Plan:** OAuth consent-flow abuse by APT29-linked clusters is a real attack surface for any organization using third-party OAuth integrations; audit configured OAuth app permissions and enforce stricter conditional access policies to reduce the social-engineering foothold these groups exploit.
- **SOC/IR — Act:** Three active Russian clusters are running persistent campaigns against high-value sectors using OAuth flow hijacking and captive-portal redirects — pull Google's full IOC list, hunt for anomalous OAuth token grants or device-code auth attempts since mid-2025, and tune detections for captive-portal redirect chains tied to UNC7005 TTPs documented by Reliaquest and Microsoft.
- **Leader — Plan:** If your organization falls in academia, aerospace/defense, government, or think tanks, queue a targeted user-awareness briefing on OAuth and device-code phishing before next quarter; the APT29 lineage of UNC6293 elevates this beyond routine phishing and warrants a conversation with your security team about protective intelligence coverage.
