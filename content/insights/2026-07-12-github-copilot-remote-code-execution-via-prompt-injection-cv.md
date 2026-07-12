---
title: "GitHub Copilot RCE via Prompt Injection (CVE-2025-53773)"
date: 2026-07-12T11:56:34.126082+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["prompt-injection", "rce", "ai-tooling"]
cves: ["CVE-2025-53773"]
source: "https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/"
source_name: "HN (cve)"
status: "active"
---
- **Engineer — Plan:** GitHub Copilot is broadly deployed on developer workstations; a public PoC exists for this RCE-via-prompt-injection path, but EPSS is 0.03 and it is not KEV-listed. Check for an available Copilot update and audit whether your pipelines or editors process untrusted file content through Copilot without sandboxing.
- **SOC/IR — Learn:** Prompt injection as an RCE delivery mechanism in AI coding assistants is a novel developer-endpoint attack class worth adding to your threat model, but the summary provides no IOCs or ATT&CK-mappable TTPs to act on for detection tuning today.
- **Leader — Plan:** If your organization deploys GitHub Copilot to developers (very common), a demonstrated RCE path represents a developer-workstation supply-chain risk; confirm with engineering whether a patched version is available and assess exposure this quarter before exploitation pressure rises.
- **Signals:** CVE-2025-53773 — CISA KEV: not listed, EPSS 0.03, public PoC on GitHub
