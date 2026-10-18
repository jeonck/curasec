---
title: "ConnectWise Suspends Cloud Backup After M365 Tenant Compromise"
date: 2026-10-18T14:33:13.167038+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["vendor-breach", "oauth-compromise", "m365"]
cves: []
source: "https://thehackernews.com/2026/10/connectwise-suspends-cloud-backup-after.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** If ConnectWise Cloud Backup or any of the seven disabled application identities are authorized in your Azure AD/Entra tenant, immediately revoke those OAuth consent grants and audit M365 unified audit logs for unauthorized data access using the published application identity GUIDs.
- **SOC/IR — Act:** Hunt M365/Entra audit logs for activity by the compromised ConnectWise application identity GUIDs (e.g., 506e08f9-6e9a-4da4-942b-a099a03644ae) — focus on anomalous OAuth token issuance, mailbox access, and SharePoint reads since the earliest possible compromise window.
- **Leader — Act:** Confirm whether ConnectWise Cloud Backup or related products are used by your organization; if so, request ConnectWise's incident report, assess M365 tenant exposure, and evaluate whether any data access triggers breach-notification obligations.
