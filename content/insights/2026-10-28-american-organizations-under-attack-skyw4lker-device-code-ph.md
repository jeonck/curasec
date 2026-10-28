---
title: "Skyw4lker Device Code Phishing Campaign Targets U.S. Orgs"
date: 2026-10-28T17:09:30.637292+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["phishing", "oauth", "cloud-identity"]
cves: []
source: "https://thehackernews.com/2026/10/american-organizations-under-attack.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Device code phishing abuses the OAuth device authorization grant, which many cloud tenants leave unrestricted by default; audit Conditional Access policies in Entra ID to block or scope device code flow to legitimate managed devices only.
- **SOC/IR — Act:** Active named campaign targeting U.S. organizations via device code auth abuse — hunt for anomalous device code authentication events in Entra ID/M365 sign-in logs (filter on 'DeviceCode' grant type) and flag suspicious OAuth token issuances since at least early October 2026.
- **Leader — Learn:** This campaign highlights that modern account takeover can succeed through legitimate auth flows rather than credential theft, making it harder to detect via traditional controls; useful framing for risk conversations but no immediate leadership action required absent a confirmed breach at a dependent vendor.
