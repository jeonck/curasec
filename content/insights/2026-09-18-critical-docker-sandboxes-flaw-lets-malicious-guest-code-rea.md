---
title: "Critical Docker Sandboxes VM Escape Exposes macOS Host Files (CVE-2026-77179)"
date: 2026-09-18T14:58:07.079452+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["container-escape", "docker", "macos"]
cves: ["CVE-2026-77179"]
source: "https://thehackernews.com/2026/09/critical-docker-sandboxes-flaw-lets.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** A public PoC exists for this container escape on macOS; any engineer running Docker Sandboxes should update to the patched version immediately and audit shared directories for unexpected access. Until patched, avoid running untrusted code inside Docker Sandboxes VMs.
- **SOC/IR — Learn:** No active exploitation signals and no KEV listing; primarily an engineer patching concern. Worth noting the attack pattern (VM guest escaping to host filesystem via shared directory traversal) for future detection development.
- **Leader — Skip**
- **Signals:** CVE-2026-77179 — CISA KEV: not listed, EPSS 0.00, public PoC on GitHub
