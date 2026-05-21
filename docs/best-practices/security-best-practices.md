---
content_sources:
  diagrams:
  - id: best-practices-security-best-practices-practice-flow
    type: flowchart
    source: mslearn-adapted
    description: Defense in depth
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch
    - https://learn.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-overview
    - https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch
    verified: false
  - claim: Core Azure VM guidance on this page should remain traceable to the listed
      sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch
    verified: false
---

# Security Best Practices

VM security should protect the management path, boot chain, identity, network boundary, and secrets independently.

## Why This Matters

A regulated workload must satisfy audit controls for privileged access, tamper-resistant boot, and data protection.

<!-- diagram-id: best-practices-security-best-practices-practice-flow -->
```mermaid
flowchart TD
    A[Classify workload] --> B[Select VM controls]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate with Azure evidence]
    D --> E[Record owner and review outcome]
```

## Recommended Practices

### 1. Remove direct public administration

**Why:** Open RDP and SSH increase exposure and make access review harder.

**How:** Use Bastion, JIT access, private connectivity, and least-privilege RBAC for operator access.

**Validation:** NSG and Defender for Cloud evidence shows management access is time-bound or private.

### 2. Use platform security features where supported

**Why:** Trusted Launch, Secure Boot, and vTPM reduce boot-chain and firmware risk for supported images.

**How:** Select compatible Gen2 images and VM sizes, and record exceptions for unsupported workloads.

**Validation:** The VM security profile shows the intended launch configuration.

### 3. Keep credentials out of scripts and images

**Why:** Secrets embedded in custom scripts or images persist beyond one deployment.

**How:** Use managed identity, Key Vault references, and extension protected settings instead of literal credentials.

**Validation:** No deployment artifact contains passwords, keys, or private SSH material.

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
    --set tags.reviewArea=security-best-practices tags.owner=platform-team \
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

- [Trusted Launch](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch)
- [Just In Time Access Overview](https://learn.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-overview)
- [Overview](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
