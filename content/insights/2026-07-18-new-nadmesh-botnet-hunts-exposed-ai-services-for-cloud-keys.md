---
title: "NadMesh Botnet Targets Exposed AI Services to Steal Cloud Keys and K8s Tokens"
date: 2026-07-18T11:51:11.203777+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Plan"
verdict_leader: "Plan"
tags: ["botnet", "cloud-credentials", "ai-infrastructure"]
cves: []
source: "https://thehackernews.com/2026/07/new-nadmesh-botnet-hunts-exposed-ai.html"
source_name: "The Hacker News"
status: "active"
---
- **Engineer — Act:** Actively scanning for internet-exposed instances of ComfyUI, Ollama, n8n, Open WebUI, Langflow, and Gradio to harvest AWS keys and Kubernetes tokens — exactly the stack teams deploy fast without firewall controls. Audit now for public exposure of these service ports, restrict to internal networks, and rotate AWS/K8s credentials on any host that ran them exposed.
- **SOC/IR — Plan:** The TTPs are concrete enough to build detections around: Shodan-driven scanning targeting AI service endpoints, followed by credential exfiltration. Build hunts for unusual outbound traffic or credential API calls originating from AI service hosts; the summary appears truncated so IOCs are not yet available to act on directly.
- **Leader — Plan:** A claimed harvest of 3,811 AWS keys illustrates the systemic risk of teams rapidly standing up AI infrastructure without security review. Raise with engineering and DevSecOps leadership to establish a deployment standard for AI tooling that includes network isolation requirements before services go live.
