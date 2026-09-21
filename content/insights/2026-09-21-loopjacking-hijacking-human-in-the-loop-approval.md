---
title: "Loopjacking: AI Agent Approval Bypass in Agno and LangGraph"
date: 2026-09-21T18:11:48.094978+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Plan"
tags: ["ai-agents", "approval-bypass", "agentic-security"]
cves: []
source: "https://arxiv.org/abs/2609.21081"
source_name: "arXiv cs.CR"
status: "active"
---
- **Engineer — Plan:** Confirmed post-approval state-substitution in Agno AgentOS ≤3.0.9 and LangGraph Agent Server ≤0.14.0 — if you ship AI agent workflows with human-in-the-loop gates, audit these dependencies and upgrade to patched releases; review approval-to-execution binding in any custom agent code.
- **SOC/IR — Learn:** Novel attack class showing that human approval gates in agentic systems can be bypassed via state mutation or misrepresentation; no IOCs or ATT&CK-mapped TTPs to hunt for today, but worth understanding as AI agent deployments expand detection scope.
- **Leader — Plan:** If your organization is deploying AI agents with human-approval checkpoints, this research establishes that approval binding is an unsolved control problem in major frameworks — use it to drive a policy review of agentic AI deployments and require vendors to document their approval-integrity guarantees this quarter.
