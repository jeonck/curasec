---
title: "Caper: Sandbox Pre-Execution Approval for Autonomous Coding Agents"
date: 2026-11-02T21:42:19.798907+00:00
verdict: "Learn"
verdict_engineer: "Learn"
verdict_soc: "Learn"
verdict_leader: "Learn"
tags: ["ai-agents", "agentic-security", "llm-security"]
cves: []
source: "https://arxiv.org/abs/2610.40753"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Learn:** Novel research showing that command-text-only approvers for coding agents miss harmful behavior hidden inside invoked tools; the sandbox pre-execution approach (6.7% harmful-outcome rate vs ≥14.8% for alternatives) is worth evaluating when architecting agent approval pipelines in CI/CD.
- **SOC/IR — Learn:** Provides a useful mental model for how malicious behavior can be concealed inside tool invocations by coding agents, which may inform future hunt hypotheses as agentic systems proliferate in enterprise environments—no immediate detection work available from this paper.
- **Leader — Learn:** Benchmark evidence that current coding-agent guardrails have high harmful-outcome rates is useful context for AI-agent governance discussions, but this is academic research with no policy deadline or vendor exposure requiring near-term action.
