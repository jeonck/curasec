---
title: "Microsoft Patches CVSS 10.0 Privilege Escalation in Azure AI Foundry"
date: 2026-09-18T14:58:07.079452+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["azure", "privilege-escalation", "cloud-security"]
cves: ["CVE-2026-85889"]
source: "https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** No customer-side patch action is needed — Microsoft fixed this server-side — but a public PoC existed before the fix, so audit Azure AI Foundry activity and IAM logs for unauthorized privilege escalations that may have occurred during the exposure window.
- **SOC/IR — Act:** A public PoC on GitHub combined with a CVSS 10.0 network-accessible privilege escalation means exploitation attempts are plausible; hunt for anomalous privilege escalation events in Azure AI Foundry audit logs and Azure Entra activity logs predating the patch.
- **Leader — Plan:** Confirm whether Azure AI Foundry is in use and have the team verify no exploitation occurred during the pre-patch window; the CVSS 10.0 score and public PoC will likely generate customer or board inquiries, so prepare a brief noting Microsoft resolved it server-side with no customer action required.
- **Signals:** CVE-2026-85889 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
