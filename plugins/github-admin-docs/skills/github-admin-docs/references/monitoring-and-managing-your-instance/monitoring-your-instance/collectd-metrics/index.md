---
title: Collectd metrics
intro: 'You can configure monitoring and alerting so that you''re aware of potential issues before they negatively impact application performance or availability.'
versions:
  feature: ghes-collectd-available
children:
  - /about-collectd-metrics
  - /setting-up-external-monitoring-with-collectd
  - /collectd-metrics-for-github-enterprise-server
  - /exporting-and-scraping-prometheus-metrics
shortTitle: Collectd metrics
---

{% ifversion ghes-opentelemetry %}

Collectd metrics are gathered by default and are fully supported in this release. OpenTelemetry metrics are the future foundation for monitoring, available from GitHub Enterprise Server 3.18 onward.

> [!IMPORTANT]
> Collectd metrics are retired in GitHub Enterprise Server 3.23. We recommend migrating to OpenTelemetry metrics before upgrading. See [AUTOTITLE](/admin/monitoring-and-managing-your-instance/monitoring-your-instance/opentelemetry-metrics/migration-guidance).

{% endif %}
