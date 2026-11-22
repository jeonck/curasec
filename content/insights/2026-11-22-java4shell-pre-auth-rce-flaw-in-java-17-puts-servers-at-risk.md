---
title: "Java4Shell: pre-auth RCE in Java 17 (CVE-2026-114938)"
date: 2026-11-22T16:05:35.915127+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["rce", "java", "cve"]
cves: ["CVE-2026-114938"]
source: "https://www.aikido.dev/blog/java-17-rce-vulnerability-cve-2026-114938"
source_name: "HN (cve)"
status: "active"
---
- **Engineer — Act:** Pre-auth RCE in Java 17 with a public PoC on GitHub makes exploitation practical now even without KEV listing; patch Java 17 to the fixed version immediately and prioritize any internet-facing services running it.
- **SOC/IR — Act:** Public PoC availability means active exploitation attempts are likely imminent; build or tune detections for anomalous Java process spawning and unexpected child processes, and begin hunting for exploitation evidence since the PoC dropped.
- **Leader — Plan:** A pre-auth RCE across Java 17 with public PoC carries Log4Shell-scale potential for enterprise exposure; direct engineering to inventory and patch Java 17 instances this week, and prepare a leadership brief to deploy if CISA adds it to KEV or active exploitation is confirmed.
- **Signals:** CVE-2026-114938 — CISA KEV: not listed, EPSS 0.46, public PoC on GitHub, reported by 2 collected sources
