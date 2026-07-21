---
title: "EncForge Ransomware Targets AI Training Data and Model Files"
date: 2026-07-21T12:43:35.631021+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["ransomware", "ai-security", "langflow"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/jadepuffer-agentic-attacks-now-target-ai-model-data-with-ransomware/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If you run Langflow, vector databases, or store model checkpoints and training datasets, audit whether those assets are covered by offline/immutable backups and restrict write access to AI model storage paths — ransomware operators are now specifically targeting these artifacts.
- **SOC/IR — Learn:** EncForge represents a new ransomware class deliberately targeting AI infrastructure assets; no IOCs or ATT&CK mappings are available yet, so file this as context for future detections around ML pipeline directories and vector DB processes.
- **Leader — Plan:** AI training datasets and model checkpoints are now explicit ransomware targets — verify that backup and recovery programs extend to these assets, and add AI model data to the next ransomware tabletop scope if not already present.
