---
title: "Attackers Targeting miniOrange SAML WordPress Plugin Auth Bypass"
date: 2026-08-25T11:39:54.623847+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["wordpress", "saml", "privilege-escalation"]
cves: ["CVE-2026-61979"]
source: "https://thehackernews.com/2026/08/attackers-target-miniorange-saml-flaws.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** If you run the miniOrange SAML 2.0 SSO WordPress plugin, update it immediately — unauthenticated privilege escalation to admin is high-severity, and active exploitation is claimed by Patchstack, though enrichment signals (EPSS 0.00, no KEV) don't corroborate it yet.
- **SOC/IR — Learn:** No IOCs, ATT&CK mappings, or behavioral TTPs are published; if your estate includes WordPress with SAML SSO, note this as a precursor to watching for unexpected admin account creation, but there is no actionable detection surface today.
- **Leader — Skip**
- **Signals:** CVE-2026-61979 — CISA KEV: not listed, EPSS 0.00, no public PoC found
