---
title: "Cursor, Codex, Gemini CLI, Antigravity hit by sandbox escapes"
date: 2026-07-21T12:43:35.631021+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["ai-coding-tools", "sandbox-escape", "cve"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/"
source_name: "BleepingComputer"
status: "archived"
---
- **Engineer — Plan:** Patches are available for Cursor, Codex, and Gemini CLI; update all three and audit any AI agent file-write permissions to ensure automated pipelines don't blindly execute AI-generated scripts. No active exploitation is reported and no KEV/PoC signals present, so this is patch-cycle priority rather than emergency.
- **SOC/IR — Learn:** The attack class — an AI agent writing files that trusted host tools later execute — is a novel indirect execution path worth understanding for future detection work, but this disclosure provides no IOCs, no ATT&CK mapping, and no evidence of in-the-wild exploitation to act on now.
- **Leader — Plan:** Multiple widely-used AI coding assistants were found to have sandbox escapes; inventory which tools developers are using, confirm patched versions are deployed, and this quarter establish a policy requiring approved-tool lists and update cadence for AI development tooling before broader enterprise rollout.
