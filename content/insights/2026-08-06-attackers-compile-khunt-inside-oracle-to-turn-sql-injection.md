---
title: "khunt Toolkit Exploits Oracle Java Compilation for Fileless SYSTEM Access"
date: 2026-08-06T13:03:19.955458+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["sql-injection", "oracle", "post-exploitation"]
cves: []
source: "https://thehackernews.com/2026/08/attackers-compile-khunt-inside-oracle.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Active exploitation chain: SQL injection in a public-facing app leads to fileless SYSTEM access via Oracle's Java stored procedure compilation. Audit web app inputs for SQLi, disable Oracle Java execution capabilities if unused (`DBMS_JAVA` grants), and inspect Oracle schema objects for unauthorized compiled Java classes.
- **SOC/IR — Act:** Huntress is tracking this active toolkit (khunt); the fileless approach bypasses standard file-write detections. Hunt for anomalous Java stored-procedure compilation events in Oracle audit logs and alert on SYSTEM-level process spawning from Oracle service accounts since at least the date of this report.
- **Leader — Plan:** Active exploitation of SQL injection against Oracle databases reaching OS-level access is a credible risk for any organization with public-facing Oracle-backed apps. Ask your team to confirm SQLi controls and Oracle hardening are in place this quarter.
