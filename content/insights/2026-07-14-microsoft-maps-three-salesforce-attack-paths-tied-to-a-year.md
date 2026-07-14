---
title: "Microsoft Maps Three Salesforce OAuth Attack Paths Used by ShinyHunters"
date: 2026-07-14T12:08:08.109802+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["oauth-abuse", "salesforce", "shinyhunters"]
cves: []
source: "https://thehackernews.com/2026/07/microsoft-maps-year-long-shinyhunters.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** No platform CVE to patch — the attack surface is over-trusted OAuth connections and third-party integrations. Audit all connected apps in your Salesforce org, revoke unused OAuth grants, and review third-party vendor permissions this quarter.
- **SOC/IR — Act:** Microsoft has detailed three concrete attack paths from an active, year-long campaign — hunt for anomalous OAuth authorization events and unusual connected-app activity in Salesforce audit logs going back at least 12 months to check for prior compromise.
- **Leader — Act:** ShinyHunters is an active data-extortion group and this campaign abuses third-party SaaS trust, not software flaws — confirm your organization's Salesforce OAuth integrations are inventoried, brief leadership on third-party SaaS risk exposure, and ask your Salesforce-connected vendors for attestation of their OAuth hygiene.
