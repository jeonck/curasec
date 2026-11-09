---
title: "Cutpurse: Explanation APIs Add Less Model-Extraction Risk Than Assumed"
date: 2026-11-09T22:16:08.330867+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Skip"
verdict_leader: "Skip"
tags: ["ml-security", "model-extraction", "research"]
cves: []
source: "https://arxiv.org/abs/2611.09375"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** If you expose LIME or similar explanation APIs for tabular classifiers, this research suggests the extraction risk lies in bin-edge coordinates rather than attribution rankings — and those edges are reproducible from public data, so restricting the API alone may not be sufficient defense.
- **SOC/IR — Skip**
- **Leader — Skip**
