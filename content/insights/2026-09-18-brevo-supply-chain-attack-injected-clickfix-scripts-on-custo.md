---
title: "Brevo supply-chain attack injected ClickFix scripts on customer sites"
date: 2026-09-18T14:58:07.079452+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "clickfix", "saas-breach"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** If your web properties embed Brevo JavaScript, audit those pages now for ClickFix script injection and remove or replace the embed; also audit your own Cloudflare API key scopes and rotation practices to prevent analogous key theft.
- **SOC/IR — Act:** Hunt for ClickFix execution artifacts—browser-spawned PowerShell, clipboard-injected command execution—on endpoints whose users visited Brevo-embedded pages during the compromise window; check EDR for downstream post-exploitation activity from any hits.
- **Leader — Act:** Confirm whether your organization uses Brevo's embedded JS on customer-facing sites; if so, determine the exposure window and assess whether visitors received malicious scripts triggering breach-notification or disclosure obligations under applicable regulations.
