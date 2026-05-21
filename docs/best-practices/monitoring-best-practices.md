---
content_sources:
  diagrams:
  - id: best-practices-monitoring-best-practices-practice-flow
    type: flowchart
    source: mslearn-adapted
    description: Evidence pipeline
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-machines/monitor-vm
    - https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-overview
    - https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/virtual-machines/monitor-vm
    verified: false
  - claim: Core Azure VM guidance on this page should remain traceable to the listed
      sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/virtual-machines/monitor-vm
    verified: false
---

# Monitoring Best Practices

VM monitoring must connect platform metrics, guest telemetry, logs, and change history so incident responders can narrow scope quickly.

## Why This Matters

An application team needs to determine whether latency comes from Azure host health, guest resource pressure, or application code.

<!-- diagram-id: best-practices-monitoring-best-practices-practice-flow -->
```mermaid
flowchart TD
    A[Classify workload] --> B[Select VM controls]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate with Azure evidence]
    D --> E[Record owner and review outcome]
```

## Recommended Practices

### 1. Collect both platform and guest signals

**Why:** Platform metrics alone do not show process, filesystem, or application pressure inside the guest.

**How:** Use VM insights or Azure Monitor Agent for guest telemetry and keep platform metrics for host-level evidence.

**Validation:** Dashboards show CPU, memory, disk, network, heartbeat, and dependency signals.

### 2. Alert on symptoms and causes separately

**Why:** A high CPU alert does not prove customer impact, and an availability alert does not identify cause.

**How:** Pair service-level alerts with infrastructure saturation and backup/patch failure alerts.

**Validation:** Alert names identify severity, owner, metric, threshold, and response runbook.

### 3. Retain change evidence

**Why:** VM incidents often follow resize, disk, NSG, route, extension, or patch changes.

**How:** Use Activity Log and resource change analysis with metric timelines during triage.

**Validation:** Incident timelines include both telemetry and control-plane events.

### CLI review example

```bash
az vm show \
    --resource-group $RG \
    --name $VM_NAME \
    --query "{name:name,size:hardwareProfile.vmSize,zone:zones,security:securityProfile.securityType}" \
    --output json

az vm list-sizes \
    --location $LOCATION \
    --query "[?name=='Standard_D4s_v5' || name=='Standard_E4s_v5'].{name:name,cores:numberOfCores,memory:memoryInMb,maxDataDiskCount:maxDataDiskCount}" \
    --output table

az vm update \
    --resource-group $RG \
    --name $VM_NAME \
    --set tags.reviewArea=monitoring-best-practices tags.owner=platform-team \
    --output json
```

| Element | Purpose |
|---|---|
| `$RG` | Resource group containing the VM resources. |
| `$VM_NAME` | Target virtual machine name. |
| `$LOCATION` | Azure region for regional resource discovery or creation. |
| `--resource-group` | Scopes the command to the intended resource group. |
| `--name` | Identifies the resource being created, read, updated, or deleted. |
| `--query` | Filters the response so operators capture only the needed evidence. |
| `--output` | Controls the output format for logs, scripts, or human review. |
| `--location` | Selects the Azure region for regional resources or SKU lookup. |
| `--set` | Updates one or more resource properties or tags. |
| Expected result | Command succeeds and returns the requested Azure resource state or operation result. |

## Common Mistakes / Anti-Patterns

- Treating a VM as only a compute resource while ignoring disk, network, identity, and recovery controls.
- Reusing a proof-of-concept SKU, image, or public access path in production without a fresh review.
- Marking the design complete without captured Azure evidence and an owner for follow-up changes.

## Validation Checklist

- [ ] Workload owner, criticality, and support model are recorded.
- [ ] VM size, disk tier, network path, access model, and recovery controls match the workload objective.
- [ ] Azure CLI or portal evidence is captured after the change.
- [ ] Exceptions are documented with an expiration date or follow-up issue.

## See Also

- [Production Baseline](production-baseline.md)
- [Operations](../operations/index.md)
- [Troubleshooting](../troubleshooting/index.md)

## Sources

- [Monitor Vm](https://learn.microsoft.com/en-us/azure/virtual-machines/monitor-vm)
- [Vminsights Overview](https://learn.microsoft.com/en-us/azure/azure-monitor/vm/vminsights-overview)
- [Alerts Overview](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview)
