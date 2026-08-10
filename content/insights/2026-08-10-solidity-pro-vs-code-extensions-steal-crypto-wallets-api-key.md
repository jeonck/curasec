---
title: "Malicious Solidity Pro VS Code Extensions Harvest Wallets and Credentials"
date: 2026-08-10T11:57:16.674621+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Learn"
tags: ["supply-chain", "vs-code-extension", "credential-theft"]
cves: []
source: "https://thehackernews.com/2026/08/solidity-pro-vs-code-extensions-steal.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** If any developers on your team installed helper-beeps.solidity-pro or web3devtoolsx.solidity-pro, treat the workstation as compromised: remove the extensions, rotate all API keys and credentials accessible from that machine, and audit browser-stored secrets. Extend extension allow-listing policies to block unvetted publishers.
- **SOC/IR — Act:** Sweep developer endpoints for the presence of either extension directory (helper-beeps.solidity-pro, web3devtoolsx.solidity-pro) and review outbound network activity from developer machines for credential exfiltration since these extensions were available; the specific extension IDs give you a concrete hunt anchor.
- **Leader — Learn:** A targeted supply-chain attack against Solidity/web3 developers via marketplace extensions; notable as a recurring pattern but operationally relevant only if your org employs blockchain developers, in which case delegate an extension audit to your engineering team.
