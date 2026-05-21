---
content_sources:
  diagrams:
  - id: best-practices-disk-and-storage-best-practices-practice-flow
    type: flowchart
    source: mslearn-adapted
    description: Disk performance and recovery
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview
    - https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types
    - https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview
    verified: false
  - claim: Core Azure VM guidance on this page should remain traceable to the listed
      sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview
    verified: false
---

# Disk and Storage Best Practices

Managed disk choices should be driven by latency, IOPS, throughput, caching, and recovery needs instead of only capacity.

## Why This Matters

A database VM shows intermittent latency because disk type, VM throughput cap, and host caching were never reviewed together.

<!-- diagram-id: best-practices-disk-and-storage-best-practices-practice-flow -->
```mermaid
flowchart TD
    A[Classify workload] --> B[Select VM controls]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate with Azure evidence]
    D --> E[Record owner and review outcome]
```

## Recommended Practices

### 1. Separate OS and data paths

**Why:** The OS disk should not carry unpredictable application write pressure.

**How:** Place data, logs, and temp-heavy paths on dedicated managed disks with workload-appropriate caching.

**Validation:** Disk layout maps each application path to a managed disk and cache setting.

### 2. Match disk SKU to VM limits

**Why:** A premium disk cannot exceed the aggregate throughput and IOPS allowed by the VM size.

**How:** Check disk SKU limits and VM size limits together before increasing disk performance tier.

**Validation:** Metric evidence shows whether the bottleneck is disk, VM, or guest queue depth.

### 3. Design snapshots and backup separately

**Why:** Snapshots are point-in-time disk copies; backup provides policy, retention, and restore workflow.

**How:** Use snapshots for short-lived operational checkpoints and Azure Backup for recovery objectives.

**Validation:** Restore testing proves that the retained data can boot or attach as expected.

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
    --set tags.reviewArea=disk-and-storage-best-practices tags.owner=platform-team \
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

- [Managed Disks Overview](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview)
- [Disks Types](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types)
- [Backup Azure Vms Introduction](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction)
