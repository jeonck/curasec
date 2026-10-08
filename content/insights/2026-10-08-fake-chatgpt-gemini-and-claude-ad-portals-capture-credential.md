---
title: "Phishing Platform Spoofs AI Ad Portals to Steal Credentials and MFA"
date: 2026-10-08T17:51:36.071186+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["phishing", "credential-theft", "mfa-bypass"]
cves: []
source: "https://thehackernews.com/2026/10/fake-chatgpt-gemini-and-claude-ad.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** No software to patch or config to change; this is a social-engineering campaign. Awareness that AI-branded ad portals are being weaponized is worth knowing when reviewing phishing simulation scope or employee guidance.
- **SOC/IR — Plan:** Build or tune detections for MFA-bypass phishing patterns targeting AI platform lookalikes — review proxy/email logs for suspicious redirects to ChatGPT/Gemini/Claude impersonation domains and flag anomalous token submissions.
- **Leader — Learn:** Active campaign targeting business users of AI advertising tools is worth folding into the next security-awareness cycle, particularly for marketing and finance teams who manage ad-platform accounts.
