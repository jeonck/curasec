---
title: "Transcript-Bound Hybrid PQC Combiners Proven Downgrade-Resilient"
date: 2026-09-21T18:11:48.094978+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["post-quantum-cryptography", "hybrid-kem", "tls"]
cves: []
source: "https://arxiv.org/abs/2609.21273"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** Formal proof that hybrid ML-KEM combiners without transcript binding can be fully downgraded by an active attacker; engineers designing or auditing custom hybrid PQC handshakes (TLS, SSH, IKE) should verify their key schedule binds the session key to a transcript hash, not just the raw KEM output.
- **SOC/IR — Skip**
- **Leader — Skip**
