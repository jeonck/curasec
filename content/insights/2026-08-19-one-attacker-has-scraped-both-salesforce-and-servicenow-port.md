---
title: "Attacker Scraping Salesforce and ServiceNow Portals Since 2025"
date: 2026-08-19T11:36:35.301683+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["saas-threat", "data-scraping", "threat-intel"]
cves: []
source: "https://thehackernews.com/2026/08/one-attacker-has-scraped-both.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Salesforce and ServiceNow are near-universal in enterprise estates; audit portal access logs for IP 158.220.87.79 going back to early 2025, and review guest-user permissions and external sharing rules on both platforms.
- **SOC/IR — Act:** A confirmed, long-running campaign with a published IOC (158.220.87.79) hitting widely deployed enterprise SaaS — sweep Salesforce and ServiceNow access logs in your SIEM for that IP since January 2025 and build a persistent detection for it.
- **Leader — Act:** Active multi-industry data-scraping of Salesforce and ServiceNow portals lasting over a year raises potential customer-data exposure; confirm whether your organization's portals were targeted and assess notification obligations before customers ask.
