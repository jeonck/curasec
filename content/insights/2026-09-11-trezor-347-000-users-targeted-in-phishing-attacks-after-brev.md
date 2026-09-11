---
title: "Trezor phishing campaign via Brevo breach hits 347K users"
date: 2026-09-11T14:58:57.702490+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["phishing", "supply-chain", "email-security"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/trezor-347-000-users-targeted-in-phishing-attacks-after-brevo-breach/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If your org uses Brevo (Sendinblue) as an email/marketing service provider, audit your account for unauthorized access and review what customer data is stored there; this breach shows ESP compromise can expose your customer lists to targeted phishing.
- **SOC/IR — Learn:** The attack chain—ESP breach leading to targeted customer phishing—is a useful lure pattern to understand, but no IOCs or ATT&CK-mappable TTPs are provided in this item to act on.
- **Leader — Learn:** A clear example of third-party SaaS vendor risk: a breach at email provider Brevo exposed Trezor's customer list and enabled downstream phishing; worth citing in vendor risk review discussions, but no immediate action required unless your org uses Brevo.
