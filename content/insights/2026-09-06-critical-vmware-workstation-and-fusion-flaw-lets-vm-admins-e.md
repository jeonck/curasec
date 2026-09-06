---
title: "Critical VMware Workstation/Fusion VM Escape Allows Host Code Execution"
date: 2026-09-06T14:08:28.650854+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Learn"
tags: ["vmware", "vm-escape", "rce"]
cves: ["CVE-2026-59346"]
source: "https://thehackernews.com/2026/09/critical-vmware-workstation-and-fusion.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC on GitHub for this CVSS 9.3 integer-overflow VM escape (CVE-2026-59346) makes exploitation practical even without a KEV listing; patch VMware Workstation and Fusion to the latest Broadcom-released versions immediately, prioritizing developer and security-lab machines where Workstation is commonly deployed.
- **SOC/IR — Plan:** With a public PoC available, build host-side detections for anomalous process spawning from VMware Workstation parent processes, which would indicate a VM-to-host breakout attempt; the local elevated-privilege prerequisite means exploitation is a post-compromise step worth hunting for in dev-heavy environments.
- **Leader — Learn:** A VM escape in desktop virtualization software (Workstation/Fusion, not ESXi) is a meaningful but not board-level event; note the risk for developer workstation fleets and confirm engineering is tracking the patch rollout.
- **Signals:** CVE-2026-59346 — CISA KEV: not listed, EPSS n/a, public PoC on GitHub
