---
title: "BdThemes WordPress plugin supply-chain hack drops rogue admins"
date: 2026-08-11T11:54:43.298939+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "wordpress", "credential-access"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/bdthemes-plugins-supply-chain-hack-creates-rogue-wordpress-admins/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Supply-chain compromise of a plugin developer pushing malicious content to admin browsers is an Act trigger regardless of KEV status. Audit all WordPress admin accounts for unauthorized additions made recently, disable BdThemes plugins until a clean version is confirmed, and rotate admin credentials on affected sites.
- **SOC/IR — Act:** The attack results in rogue admin account creation — a concrete, detectable IOC. Sweep WordPress site logs and admin user tables for accounts created in the past week that were not provisioned through normal change management; flag and disable any unauthorized entries.
- **Leader — Act:** If the organization runs WordPress properties using BdThemes plugins, this is an active vendor supply-chain event requiring same-week exposure confirmation. Verify whether any company or client WordPress instances use BdThemes products and request an integrity check of admin accounts from the teams responsible.
