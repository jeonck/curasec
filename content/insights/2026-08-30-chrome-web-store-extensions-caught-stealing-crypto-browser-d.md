---
title: "Chrome/Edge extensions caught stealing crypto and browser data"
date: 2026-08-30T15:19:58.098687+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["browser-extension", "infostealer", "supply-chain"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/chrome-web-store-extensions-caught-stealing-crypto-browser-data/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Audit installed Chrome/Edge extensions across your managed fleet and enforce an allowlist policy; no CISA KEV or active enterprise exploitation signal, but browser extension supply-chain risk is real for developer workstations.
- **SOC/IR — Act:** Hunt for suspicious extension IDs from the reported malicious set in browser inventory logs and EDR telemetry; also look for ClickFix lure behavior (fake captcha/update prompts triggering clipboard/PowerShell execution) as a detection pattern since this reporting date.
- **Leader — Plan:** Browser extension governance is a gap in most enterprise policies — use this as a prompt to task the team with drafting an approved-extension policy before the next audit cycle.
