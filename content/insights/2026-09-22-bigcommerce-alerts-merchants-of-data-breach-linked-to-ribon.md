---
title: "BigCommerce merchants hit by credential breach via Ribon third-party apps"
date: 2026-09-22T15:30:54.753130+00:00
verdict: "Act"
verdict_engineer: "Plan"
verdict_soc: "Plan"
verdict_leader: "Act"
tags: ["supply-chain", "ecommerce", "data-breach"]
cves: []
source: "https://www.bleepingcomputer.com/news/security/bigcommerce-alerts-merchants-of-data-breach-linked-to-ribon-apps/"
source_name: "BleepingComputer"
status: "active"
---
- **Engineer — Plan:** If you run BigCommerce storefronts with third-party apps, audit installed apps for Ribon-linked integrations and review your CSP headers and script-injection monitoring; no CVE or patch available, but credential hygiene for marketplace apps is the control surface here.
- **SOC/IR — Plan:** Add detection coverage for unexpected third-party script injections in e-commerce environments; hunt for new or modified script tags in storefront page responses if BigCommerce is in scope for your estate.
- **Leader — Act:** If your organization operates BigCommerce storefronts, confirm whether Ribon apps are installed and request BigCommerce's incident report; this may trigger PCI DSS or customer notification obligations if payment-adjacent data was exposed.
