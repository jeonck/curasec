---
title: "Docker Hub flaw allowed user impersonation and image tampering via PAT"
date: 2026-10-13T18:14:34.078200+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["docker-hub", "supply-chain", "container-security"]
cves: ["CVE-2026-105445"]
source: "https://www.bleepingcomputer.com/news/security/docker-hub-flaw-let-attackers-impersonate-users-tamper-with-images/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** Docker Hub patched this server-side, but any org using Docker Hub PATs should audit token activity for unauthorized access and verify image digests for unexpected modifications, particularly for images pulled before the patch window.
- **SOC/IR — Plan:** No IOCs or active exploitation reported, but review Docker Hub audit logs for anomalous PAT usage; build or tune detections for unauthorized container registry access as this TTP (token-based impersonation enabling image tampering) could resurface.
- **Leader — Plan:** This is a supply-chain risk event — confirm Docker has fully remediated the server-side flaw, review your organization's PAT governance policy for Docker Hub, and flag this class of risk (registry impersonation enabling tampered images) as a standing vendor-risk consideration.
- **Signals:** CVE-2026-105445 — CISA KEV: not listed, EPSS n/a, no public PoC found
