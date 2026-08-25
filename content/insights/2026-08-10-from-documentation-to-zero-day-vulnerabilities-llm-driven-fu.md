---
title: "PDFuzzer: LLM-Driven Fuzzing Finds 31 Zero-Days in PDF Readers"
date: 2026-08-10T13:39:41.207792+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["fuzzing", "pdf-security", "llm-research"]
cves: []
source: "https://arxiv.org/abs/2608.06641"
source_name: "arXiv cs.CR"
status: "archived"
---
- **Engineer — Learn:** PDFuzzer's LLM-guided API-sequence approach found zero-days ranging from info leakage to arbitrary code execution in Adobe Acrobat, Foxit, and PDF-XChange Editor; no CVEs, patches, or exploitation signals are present yet, so watch for vendor advisories following coordinated disclosure.
- **SOC/IR — Learn:** No active exploitation, IOCs, or TTPs to hunt for; the finding that PDF reader JavaScript engines can be exploited via chained API calls is worth noting as a future detection surface if exploitation emerges.
- **Leader — Skip**
