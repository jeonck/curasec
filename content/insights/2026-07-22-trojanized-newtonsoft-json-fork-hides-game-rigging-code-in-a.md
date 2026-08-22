---
title: "Trojanized Newtonsoft.Json NuGet Typosquat Targets Gaming Platform"
date: 2026-07-22T12:46:13.866991+00:00
verdict: "Plan"
verdict_engineer: "Plan"
verdict_soc: "Learn"
verdict_leader: "Skip"
tags: ["supply-chain", "nuget", "typosquatting"]
cves: []
source: "https://thehackernews.com/2026/07/trojanized-newtonsoftjson-fork-hides.html"
source_name: "The Hacker News"
status: "archived"
---
- **Engineer — Plan:** Audit all .NET project lockfiles and build manifests for the package name 'Newtonsoftt.Json.Net'; also review whether dependency pinning and hash verification are enforced in your NuGet pipeline. No KEV or broad exploitation signals, but the package targets a massively common library, raising accidental-install risk.
- **SOC/IR — Learn:** The technique — a fully functional trojanized fork to evade cursory inspection — is a useful evolution in supply-chain tradecraft, but the summary provides no IOCs, ATT&CK mappings, or detection signatures to act on now.
- **Leader — Skip**
