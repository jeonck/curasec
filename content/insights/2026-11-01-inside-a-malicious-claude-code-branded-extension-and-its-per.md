---
title: "Malicious Claude Code-branded IDE extension installs persistent SSH backdoor"
date: 2026-11-01T17:05:59.848527+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["supply-chain", "developer-tools", "ssh-backdoor"]
cves: []
source: "https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/"
source_name: "Microsoft Security Blog"
status: "active"
---
- **Engineer — Act:** A trojanized Claude Code extension targeting Cursor/VS Code installs a persistent SSH backdoor on developer machines — audit all installed IDE extensions for this package and follow Microsoft's remediation steps to remove backdoor artifacts and rotate any credentials accessible from affected workstations.
- **SOC/IR — Act:** Microsoft's analysis includes detection guidance; sweep developer endpoints for the malicious extension presence and hunt for anomalous outbound SSH connections or new authorized_keys entries on workstations since late October 2026.
- **Leader — Act:** A supply-chain compromise of developer tooling with persistent backdoor access is a same-week risk event — confirm whether engineers use Cursor/VS Code extensions from untrusted sources, assess any exposure, and consider a brief to engineering leadership on extension vetting policy.
