---
title: "LoRAScan: Runtime detection of backdoored LoRA adapters via activation spikes"
date: 2026-08-10T13:39:41.207792+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["llm-security", "supply-chain", "ai-ml"]
cves: []
source: "https://arxiv.org/abs/2608.06795"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** Identifies a real supply-chain risk for teams consuming third-party LoRA adapters: a backdoored adapter can alter model output on hidden triggers without modifying base model weights. LoRAScan's inference-time monitoring approach is worth evaluating if your ML pipelines pull adapters from untrusted registries or Hugging Face.
- **SOC/IR — Learn:** No active exploitation, IOCs, or ATT&CK-mappable TTPs to act on; this is foundational research on a threat class. Worth filing as context if your org is building detections around AI/ML pipeline integrity, but no hunt or rule work warranted today.
- **Leader — Learn:** Surfaces an emerging supply-chain risk category for AI workloads—untrusted fine-tuned adapters as a malware vector—useful background for shaping AI vendor-risk policy before it becomes a control requirement.
