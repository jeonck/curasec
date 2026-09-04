---
title: "CISA KEV: Langflow RCE, Tomcat, and N-central Actively Exploited"
date: 2026-08-05T13:01:27.566949+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Plan"
tags: ["cisa-kev", "rce", "langflow"]
cves: ["CVE-2026-9198"]
source: "https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Act:** All three CVEs are CISA KEV-listed with confirmed active exploitation; CVE-2026-9198 in Langflow is a CVSS 9.8 unauthenticated RCE with a public PoC — patch Langflow, Apache Tomcat, and N-central to current vendor-recommended versions immediately, prioritizing any internet-exposed instances.
- **SOC/IR — Act:** Active exploitation of Langflow (unauthenticated RCE) and Tomcat creates immediate hunt obligations — sweep logs for exploitation attempts against these services since August 5, check for post-exploitation indicators (new processes, outbound connections) on hosts running any of the three products.
- **Leader — Plan:** Three simultaneous KEV additions including a critical AI-workflow tool (Langflow) warrant confirming your team's KEV remediation SLA is on track and verifying whether N-central (an RMM platform) is in scope — RMM compromise can enable broad lateral movement across managed endpoints.
- **Signals:** CVE-2026-9198 — CISA KEV: listed, EPSS 0.02, public PoC on GitHub
