---
title: "TEEVisor: SGX Enclaves Nested Inside AMD SEV-SNP CVMs"
date: 2026-10-12T21:14:27.524617+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["confidential-computing", "sgx", "amd-sev"]
cves: []
source: "https://arxiv.org/abs/2610.12695"
source_name: "arXiv cs.CR"
status: "archived"
---
- **Engineer — Learn:** TEEVisor's nested TEE architecture addresses real SGX limitations (slow transitions, no intra-enclave isolation) with under 5% overhead on AMD EPYC — worth tracking if your team runs SGX workloads in cloud CVMs, but no systems changes required today.
- **SOC/IR — Skip**
- **Leader — Skip**
