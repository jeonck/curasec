---
title: "Spark RAT Campaign Abuses Vulnerable OPSWAT Driver via BYOVD in Cambodia"
date: 2026-08-27T21:01:55.123618+00:00
verdict: "Plan"
verdict_engineer: "Learn"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["byovd", "rat", "edr-evasion"]
cves: []
source: "https://thehackernews.com/2026/08/spark-rat-targets-cambodia-abuses.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Learn:** The BYOVD technique exploiting a vulnerable OPSWAT driver to kill security tools is a notable evasion class worth understanding, but current targeting is regionally focused on Cambodia with no enrichment signals (no KEV, no PoC, no high EPSS) to justify immediate action in most environments.
- **SOC/IR — Plan:** Build or tune detections for vulnerable OPSWAT driver loads and anomalous security-tool process terminations consistent with BYOVD; Spark RAT is open-source and signatures should be available to add to EDR and SIEM rule sets this quarter.
- **Leader — Skip**
