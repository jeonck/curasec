---
title: "UNC6671 Vishing-AiTM Campaign Targets Financial Services, Enterprise Cloud"
date: 2026-08-07T00:21:58.703649+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["vishing", "aitm", "cloud-security"]
cves: []
source: "https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/"
source_name: "Google Threat Intelligence"
status: "archived"
---
- **Engineer — Plan:** Active group uses AiTM to bypass MFA on M365 and Okta; implement phishing-resistant FIDO2/hardware-key MFA and tighten Conditional Access or Okta device-trust policies to invalidate intercepted session tokens.
- **SOC/IR — Act:** Active campaign with mappable TTPs — hunt for anomalous Okta and M365 session activity (unexpected token origins, bulk SharePoint/OneDrive exfil) since May 2026 and pull the GTIG report for infrastructure IOCs tied to Redact, Pink, Helix, and Falcon brands.
- **Leader — Act:** Extortion group is actively hitting financial services, private equity, and professional services — if your org falls in these verticals, brief leadership this week on the campaign and verify that helpdesk impersonation and personal-device contact scenarios are covered in your security awareness program.
