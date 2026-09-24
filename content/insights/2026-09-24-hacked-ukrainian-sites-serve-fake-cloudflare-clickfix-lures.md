---
title: "Fake Cloudflare ClickFix Lures on Hacked Ukrainian Sites Drop Psychedelic Stealer"
date: 2026-09-24T15:49:46.689252+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["clickfix", "information-stealer", "social-engineering"]
cves: []
source: "https://thehackernews.com/2026/09/hacked-ukrainian-sites-serve-fake.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** The ClickFix clipboard-injection technique via spoofed Cloudflare verification pages is a growing social engineering vector that could target your users or abuse your own web properties; no patch or config change required, but worth incorporating into developer awareness and reviewing whether your own sites could be compromised to serve similar lures.
- **SOC/IR — Plan:** The ClickFix TTP — fake CAPTCHA/verification page copies a Windows Installer command to clipboard and prompts the user to run it — is a detectable execution pattern worth adding coverage for; build or tune detections for msiexec/installer invocations spawned from interactive shell sessions with no parent process chain typical of a legitimate installer flow.
- **Leader — Learn:** ClickFix campaigns exploiting trusted-brand spoofing (Cloudflare here) represent a maturing social engineering category that increasingly bypasses traditional security awareness training; no immediate leadership action required, but relevant context for the next user-risk conversation with your team.
