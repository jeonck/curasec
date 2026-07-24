---
title: "Clop ransomware actively exploiting internet-exposed Windchill and FlexPLM"
date: 2026-07-24T12:43:46.515834+00:00
verdict: "Act"
verdict_engineer: "Act"
verdict_soc: "Act"
verdict_leader: "Act"
tags: ["clop-ransomware", "plm-software", "data-theft"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/clop-ransomware-targets-windchill-flexplm-in-data-theft-attacks/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Act:** Clop is actively targeting internet-exposed PTC Windchill and FlexPLM instances — both are common in manufacturing, aerospace, and retail/apparel supply chains. Immediately audit whether any Windchill or FlexPLM deployments are internet-reachable and restrict or take them offline; review recent access logs for anomalous data staging or egress activity.
- **SOC/IR — Act:** Clop's pattern of mass data theft before extortion demands a proactive hunt in any organization running these PLM products — look for large exfiltration events from Windchill or FlexPLM hosts in your SIEM and baseline normal egress volumes now. Pull the BleepingComputer article for any published IOCs or TTPs and build detection coverage against Clop's known staging and exfil behaviors in EDR telemetry.
- **Leader — Act:** Clop has a documented track record of bulk data theft followed by public dumps, which can trigger SEC disclosure obligations and customer notification requirements. If your organization is in manufacturing, automotive, aerospace, or retail/apparel, confirm this week whether Windchill or FlexPLM is in the environment and request an exposure assessment from engineering before Clop publishes any victim list.
