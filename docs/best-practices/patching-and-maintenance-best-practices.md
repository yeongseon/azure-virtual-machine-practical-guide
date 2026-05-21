---
content_sources:
  diagrams:
  - id: best-practices-patching-and-maintenance-best-practices-practice-flow
    type: flowchart
    source: mslearn-adapted
    description: Patch control
    based_on:
    - https://learn.microsoft.com/en-us/azure/update-manager/overview
    - https://learn.microsoft.com/en-us/azure/virtual-machines/automatic-vm-guest-patching
    - https://learn.microsoft.com/en-us/azure/virtual-machines/maintenance-and-updates
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/update-manager/overview
    verified: false
  - claim: Core Azure VM guidance on this page should remain traceable to the listed
      sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/update-manager/overview
    verified: false
---

# Patching and Maintenance Best Practices

Patch strategy should define who owns guest updates, how maintenance windows are enforced, and how rollback evidence is collected.

## Why This Matters

A VM fleet needs consistent monthly patching without losing service during application-specific maintenance windows.

<!-- diagram-id: best-practices-patching-and-maintenance-best-practices-practice-flow -->
```mermaid
flowchart TD
    A[Classify workload] --> B[Select VM controls]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate with Azure evidence]
    D --> E[Record owner and review outcome]
```

## Recommended Practices

### 1. Choose an orchestration mode intentionally

**Why:** Automatic updates, platform orchestration, and manual patching have different blast-radius tradeoffs.

**How:** Map each VM group to a patch ownership model and maintenance window.

**Validation:** Patch mode and assessment results are visible for each production VM.

### 2. Test before broad rollout

**Why:** Guest patch failures can break boot, drivers, or application dependencies.

**How:** Patch a canary VM or non-production image before applying the same update wave to production.

**Validation:** The canary result and rollback plan are attached to the change record.

### 3. Track pending reboot and compliance state

**Why:** A VM can report successful patch installation while still needing a reboot.

**How:** Monitor patch assessment state, pending reboot signals, and service health after maintenance.

**Validation:** Post-patch verification includes instance view, application health, and alert checks.

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
    --set tags.reviewArea=patching-and-maintenance-best-practices tags.owner=platform-team \
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

- [Overview](https://learn.microsoft.com/en-us/azure/update-manager/overview)
- [Automatic Vm Guest Patching](https://learn.microsoft.com/en-us/azure/virtual-machines/automatic-vm-guest-patching)
- [Maintenance And Updates](https://learn.microsoft.com/en-us/azure/virtual-machines/maintenance-and-updates)
