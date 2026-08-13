---
title: "City-Forum campaign steals data from misconfigured Salesforce/ServiceNow portals"
date: 2026-08-13T11:57:16.146981+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Act"
tags: ["salesforce", "servicenow", "data-theft"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/city-forum-data-theft-attacks-target-salesforce-servicenow-portals/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Salesforce Experience Cloud and ServiceNow are near-universal enterprise platforms; the attack exploits data exposed to anonymous portal users — a misconfiguration, not a zero-day. Audit both platforms now for anonymous/guest access permissions and tighten portal visibility settings before an attacker runs the same tooling against your instance.
- **SOC/IR — Plan:** No IOCs or ATT&CK mappings are available yet, but the campaign uses custom tooling against anonymous portal endpoints. Queue detection work for anomalous unauthenticated API calls and bulk record retrieval in Salesforce Experience Cloud and ServiceNow access logs.
- **Leader — Act:** Salesforce and ServiceNow portals are in most enterprise environments, and this active campaign targets data exposed through anonymous access — a configuration gap with real breach-disclosure implications. This week, confirm whether your portal configurations restrict anonymous access and what customer or employee data could be exposed.
