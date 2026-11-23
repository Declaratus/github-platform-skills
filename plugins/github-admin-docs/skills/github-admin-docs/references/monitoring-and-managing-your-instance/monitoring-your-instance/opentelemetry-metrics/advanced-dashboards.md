---
title: Advanced dashboards of OpenTelemetry metrics
intro: After enabling OpenTelemetry metrics collection on your GitHub Enterprise Server instance, you have access to additional dashboards with enhanced visualization and monitoring capabilities.
redirect_from:
  - /enterprise/admin/monitoring-and-managing-your-instance/monitoring-your-instance/opentelemetry-metrics/enable-advanced-dashboards
versions:
  feature: ghes-opentelemetry
shortTitle: Advanced dashboards
contentType: how-tos
category:
  - Monitor and audit your enterprise
---

{% ifversion ghes-opentelemetry %}

OpenTelemetry metrics are the foundation for monitoring GitHub Enterprise Server, available from version 3.18 onward. This monitoring stack provides enhanced observability and management capabilities compared to the legacy collectd system.

{% ifversion ghes-collectd-available %}

New installations of version 3.19 and later use OpenTelemetry metrics by default. Upgrades from versions earlier than 3.21 to 3.21 or 3.22 also enable OpenTelemetry and disable collectd, but you can re-enable collectd after the upgrade.

Collectd remains supported in this release but is retired in version 3.23, and upgrading to 3.23 disables it. For the migration timeline and steps to migrate instances that still use collectd, see [AUTOTITLE](/admin/monitoring-and-managing-your-instance/monitoring-your-instance/opentelemetry-metrics/migration-guidance).

{% else %}

Collectd is retired in this release and can no longer be run. Upgrading to version 3.23 disables collectd, and OpenTelemetry metrics become the only metrics stack. For information about post-upgrade checks, see [AUTOTITLE](/admin/monitoring-and-managing-your-instance/monitoring-your-instance/opentelemetry-metrics/migration-guidance).

{% endif %}

{% endif %}

## Prerequisites

* OpenTelemetry metrics are enabled for your GitHub Enterprise Server instance


## Additional dashboards

When OpenTelemetry metrics are enabled, you will have access to advanced Grafana dashboards with enhanced visualization and monitoring capabilities.

* **Elasticsearch** - Detailed metrics for search performance, indexing operations, and cluster health
* **Nomad** - In-depth monitoring of job scheduling, resource allocation, and service orchestration
* **HAProxy** - Load balancer performance metrics, connection statistics, and request routing information
* **Node Exporter** - System-level metrics including CPU, memory, disk, and network statistics for each node
* **Process Exporter** - Detailed process-level metrics for monitoring individual service performance

These dashboards provide more granular insights into your GitHub Enterprise Server instance's performance and can help with advanced troubleshooting and capacity planning.
