---
title: "Attackers Abuse MSP360 RMM in Dual-RMM Phishing Campaign"
date: 2026-10-01T17:21:52.102295+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["rmm-abuse", "phishing", "living-off-the-land"]
cves: []
source: "https://thehackernews.com/2026/09/attackers-abuse-msp360-to-deploy.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Plan:** No exploitable CVE here, but the tactic relies on uncontrolled RMM installs reaching endpoints; audit endpoints for unauthorized MSP360 or ScreenConnect installations and enforce an allowlist policy for approved RMM tools via EDR or software-control policy.
- **SOC/IR — Plan:** The dual-RMM pattern (MSP360 dropping ScreenConnect) is a concrete detection target; build or tune rules to alert on MSP360 installations from non-IT asset-management contexts and correlate with ScreenConnect process spawns, and hunt for both tools installed since September 2026.
- **Leader — Learn:** The campaign illustrates a maturing trend of threat actors using legitimate RMM tools to bypass controls; worth noting for the next review of acceptable-use and third-party remote-access policy, but no immediate board-level action required absent evidence of a breach in your sector.
