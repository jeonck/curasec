---
title: "BTCPay Server outdated instances actively exploited to drain hot wallets"
date: 2026-11-02T20:44:36.815553+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["active-exploitation", "crypto", "open-source"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/btcpay-server-warns-of-hot-wallet-thefts-targeting-outdated-instances/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Active hot wallet draining is confirmed on outdated BTCPay Server instances; if you run BTCPay Server for crypto payment processing, update to the latest release immediately and audit wallet transaction history for unauthorized withdrawals.
- **SOC/IR — Learn:** Active exploitation is confirmed but the item provides no IOCs, TTPs, or log patterns to hunt with; file for awareness pending a technical follow-up with indicators.
- **Leader — Plan:** If your organization accepts cryptocurrency payments via self-hosted BTCPay Server, confirm which version is running and assign ownership of the update; hot wallet draining is a direct financial-loss risk, not just a security posture issue.
