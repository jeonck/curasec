---
title: "Fake OpenAI/SpaceX event invites used to phish M365/Google creds"
date: 2026-11-06T17:55:59.437458+00:00
verdict: "Act"
verdict_engineer: "Skip"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["phishing", "credential-theft", "identity"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/fake-openai-spacex-events-used-to-steal-microsoft-google-accounts/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Skip**
- **SOC/IR — Act:** Hunt for phishing-as-a-service lure patterns in email logs referencing fake OpenAI/SpaceX/Anthropic events; tune detections for adversary-in-the-middle session token theft targeting M365 and Google Workspace sign-in flows.
- **Leader — Plan:** Review whether phishing-resistant MFA (passkeys/FIDO2) is enforced for all M365 and Google Workspace users; consider adding this campaign pattern to employee security awareness messaging this quarter.
