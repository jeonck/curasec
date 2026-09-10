---
title: "Check Point Patches Two CVSS 9.8 Unauthenticated RCE Flaws in VPN/Firewall Products"
date: 2026-09-10T14:58:06.811051+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["check-point", "vpn", "critical-rce"]
cves: []
source: "https://thehackernews.com/2026/09/check-point-discloses-two-98-rated-vpn.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Two 9.8-rated unauthenticated RCE flaws in Check Point Security Gateways and management products warrant prompt patching, but no KEV listing, public PoC, or confirmed exploitation shifts this to planned rather than emergency action — schedule patching to the latest fixed releases within your next patch window.
- **SOC/IR — Learn:** No IOCs, TTPs, or exploitation details have been disclosed yet, so there is no actionable detection surface; monitor threat intel feeds for follow-on exploitation reports and be ready to sweep Check Point edge device logs if active attacks emerge.
- **Leader — Plan:** If Check Point firewalls or VPN gateways are in your estate, confirm engineering has inventoried affected appliances and scheduled patches — CVSS 9.8 perimeter RCE will attract attacker interest quickly even without current exploitation evidence.
