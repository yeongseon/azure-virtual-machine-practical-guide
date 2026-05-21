---
content_sources:
  diagrams:
  - id: best-practices-cost-optimization-best-practices-practice-flow
    type: flowchart
    source: mslearn-adapted
    description: Cost without reliability loss
    based_on:
    - https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-best-practices
    - https://learn.microsoft.com/en-us/azure/virtual-machines/auto-shutdown-vm
    - https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-best-practices
    verified: false
  - claim: Core Azure VM guidance on this page should remain traceable to the listed
      sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-best-practices
    verified: false
---

# Cost Optimization Best Practices

VM cost optimization should remove waste while preserving required performance, security, and recovery controls.

## Why This Matters

A fleet review shows many oversized VMs, unused disks, and always-on development machines.

<!-- diagram-id: best-practices-cost-optimization-best-practices-practice-flow -->
```mermaid
flowchart TD
    A[Classify workload] --> B[Select VM controls]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate with Azure evidence]
    D --> E[Record owner and review outcome]
```

## Recommended Practices

### 1. Right-size with telemetry

**Why:** Downsizing from a spreadsheet can create performance incidents.

**How:** Use CPU, memory, disk, and network trends before changing VM size or disk tier.

**Validation:** The proposed size has enough headroom for peak and failover load.

### 2. Use commitment and scheduling appropriately

**Why:** Reserved capacity and savings plans help steady workloads, while auto-shutdown helps non-production.

**How:** Classify VMs as always-on, scheduled, burst, or interruptible before choosing a cost lever.

**Validation:** Tags identify workload class and the selected cost control.

### 3. Clean up orphaned resources

**Why:** Detached disks, unused public IPs, snapshots, and stale images can persist after VM deletion.

**How:** Run periodic inventory queries and require owners for retained artifacts.

**Validation:** Monthly review output lists deleted or justified retained resources.

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
    --set tags.reviewArea=cost-optimization-best-practices tags.owner=platform-team \
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

- [Cost Mgt Best Practices](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-best-practices)
- [Auto Shutdown Vm](https://learn.microsoft.com/en-us/azure/virtual-machines/auto-shutdown-vm)
- [Spot Vms](https://learn.microsoft.com/en-us/azure/virtual-machines/spot-vms)
