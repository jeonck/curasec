---
title: "Multipath TCP: Linux CVE-2026-98432 with Public PoC, Detection Guidance"
date: 2026-11-02T20:44:36.815553+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Skip"
tags: ["linux-kernel", "mptcp", "cve"]
cves: ["CVE-2026-98432"]
source: "https://isc.sans.edu/diary/rss/33482"
source_name: "SANS ISC"
status: "active"
---
- **Engineer — Plan:** CVE-2026-98432 affects Linux MPTCP implementation with a public PoC on GitHub, but EPSS is 0.00 and it is not KEV-listed, so active exploitation pressure is low; audit whether MPTCP is enabled on your Linux hosts and schedule kernel patching this cycle.
- **SOC/IR — Plan:** The SANS ISC diary covers detection approaches for MPTCP traffic; with a public PoC now available, build or review detections for anomalous MPTCP subflow activity on Linux endpoints and edge devices before exploitation pressure rises.
- **Leader — Skip**
- **Signals:** CVE-2026-98432 — CISA KEV: not listed, EPSS 0.00, public PoC on GitHub, reported by 2 collected sources
