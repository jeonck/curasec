---
title: "Hackers Exploit miniOrange SAML Plugin Auth Bypass on WordPress"
date: 2026-08-25T11:39:54.623847+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["wordpress", "saml", "auth-bypass"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/hackers-target-wordpress-sites-in-miniorange-auth-bypass-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** If you run the miniOrange SAML 2.0 SSO plugin on any WordPress site, update it immediately — active exploitation attempts are underway and successful attacks yield unauthenticated admin access via forged SAML responses. Audit recent admin accounts and session logs for signs of unauthorized logins.
- **SOC/IR — Act:** Active exploitation is in progress; hunt for anomalous SAML authentication events and unexpected admin account creation or logins on any WordPress instances in your estate, and tune detections for unusual authentication source patterns against WordPress admin endpoints.
- **Leader — Plan:** If your organization operates WordPress sites with the miniOrange SAML SSO plugin, direct teams to patch this week — a successful exploit grants full admin takeover, which could expose customer data or be used as a pivot point. Verify your WordPress plugin inventory and patch cadence.
