---
title: "GitLab CVSS 10 File-Read Flaw Exploited in the Wild After PoC Release"
date: 2026-09-12T14:04:45.501336+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["gitlab", "path-traversal", "cve"]
cves: ["CVE-2026-85706"]
source: "https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** CVE-2026-85706 is CISA KEV-listed with a public GitHub PoC and confirmed in-the-wild probes — patch GitLab to the fixed release immediately and audit server-side files (secrets, keys, configs) for unauthorized reads since public disclosure.
- **SOC/IR — Act:** Active exploitation probes are underway; hunt for unauthenticated requests containing path traversal sequences against the GitLab commits API in web/proxy logs going back to the disclosure date, and tune SIEM rules to alert on anomalous API access patterns.
- **Leader — Act:** Confirm with engineering this week that all self-hosted GitLab instances are patched; if using GitLab.com, request a written statement from GitLab on remediation status — unauthenticated source-code and secret exposure at CVSS 10 with active probes is a material risk worth verifying before it surfaces as a customer or board question.
- **Signals:** CVE-2026-85706 — CISA KEV: listed, EPSS n/a, public PoC on GitHub, reported by 2 collected sources
