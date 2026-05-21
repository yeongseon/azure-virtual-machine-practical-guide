---
content_sources:
  diagrams:
  - id: best-practices-sizing-and-image-selection-practice-flow
    type: flowchart
    source: mslearn-adapted
    description: Size and image fit
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-machines/sizes
    - https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage
    - https://learn.microsoft.com/en-us/azure/virtual-machines/resize-vm
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes
    verified: false
  - claim: Core Azure VM guidance on this page should remain traceable to the listed
      sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes
    verified: false
---

# Sizing and Image Selection

VM sizing and image selection should match workload pressure, OS lifecycle, regional availability, and future resizing constraints.

## Why This Matters

A team needs to move a workload from a proof-of-concept VM to a supportable production SKU and image.

<!-- diagram-id: best-practices-sizing-and-image-selection-practice-flow -->
```mermaid
flowchart TD
    A[Classify workload] --> B[Select VM controls]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate with Azure evidence]
    D --> E[Record owner and review outcome]
```

## Recommended Practices

### 1. Choose size from workload shape

**Why:** CPU count alone hides memory, disk, and network caps.

**How:** Compare vCPU, memory, data disk count, temporary storage, accelerated networking support, and local regional availability.

**Validation:** The selected family has headroom for CPU, memory, disk throughput, and NIC throughput.

### 2. Use supported images and generations

**Why:** Old images can miss security, Trusted Launch, or Gen2 capabilities.

**How:** Prefer current marketplace images or a governed Azure Compute Gallery image with patch ownership.

**Validation:** Image publisher, offer, SKU, and version are recorded before deployment.

### 3. Plan resize paths

**Why:** Some resizes require deallocation or can be blocked by cluster capacity.

**How:** Document an alternate size family and test resize in the target region before a critical window.

**Validation:** A rollback size and validation command are included in the change plan.

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
    --set tags.reviewArea=sizing-and-image-selection tags.owner=platform-team \
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

- [Sizes](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes)
- [Cli Ps Findimage](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage)
- [Resize Vm](https://learn.microsoft.com/en-us/azure/virtual-machines/resize-vm)
