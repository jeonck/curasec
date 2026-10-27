---
title: "Attackers Abuse Teams External Chat for IT Support Impersonation and Malware"
date: 2026-10-27T16:34:51.683639+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["microsoft-teams", "social-engineering", "ransomware"]
cves: []
source: "https://thehackernews.com/2026/10/attackers-use-microsoft-teams-it.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** Teams' external-chat feature is being abused at scale; audit your tenant's external access policy and consider restricting or requiring approval for inbound external chat requests in the Teams admin center.
- **SOC/IR — Act:** Hundreds of confirmed cases share a pattern of throwaway tenants with IT-themed names initiating chats that precede malware drops; hunt for Teams external-chat sessions from newly created tenants and correlate with unusual child-process creation from Teams.exe since at least early October 2026.
- **Leader — Plan:** A high-volume campaign is using Teams to impersonate internal IT and deliver ransomware; schedule an employee awareness communication this week and direct the team to review the tenant's external-communications policy before next quarter.
