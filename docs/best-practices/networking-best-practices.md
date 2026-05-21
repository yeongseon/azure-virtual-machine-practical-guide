---
content_sources:
  diagrams:
  - id: best-practices-networking-best-practices-practice-flow
    type: flowchart
    source: mslearn-adapted
    description: Network path control
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
    - https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview
    - https://learn.microsoft.com/en-us/azure/bastion/bastion-overview
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
    verified: false
  - claim: Core Azure VM guidance on this page should remain traceable to the listed
      sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview
    verified: false
---

# Networking Best Practices

VM networking design should make traffic paths explicit, private by default, and easy to prove during an incident.

## Why This Matters

A workload needs inbound application traffic, private administration, and predictable outbound access without exposing RDP or SSH to the internet.

<!-- diagram-id: best-practices-networking-best-practices-practice-flow -->
```mermaid
flowchart TD
    A[Classify workload] --> B[Select VM controls]
    B --> C[Apply topic-specific guardrails]
    C --> D[Validate with Azure evidence]
    D --> E[Record owner and review outcome]
```

## Recommended Practices

### 1. Separate workload and management paths

**Why:** Management ports are high-value targets and should not be the public entry point.

**How:** Use Bastion, VPN, ExpressRoute, or private jump hosts instead of internet-exposed RDP or SSH.

**Validation:** Effective NSG rules show no broad inbound management exposure.

### 2. Use Standard networking components consistently

**Why:** Load balancer and public IP SKU mismatches cause deployment and connectivity surprises.

**How:** Use Standard public IPs and Standard Load Balancer for modern public endpoints; explicitly allow required inbound flows with NSGs.

**Validation:** Public endpoints, load balancers, and NICs use compatible SKUs and rules.

### 3. Validate routes and DNS before cutover

**Why:** Most VM connectivity incidents involve NSG, UDR, DNS, or asymmetric routing mistakes.

**How:** Capture effective routes, effective security rules, and DNS resolution evidence before changing traffic.

**Validation:** Connectivity evidence exists for both source-to-VM and VM-to-dependency paths.

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
    --set tags.reviewArea=networking-best-practices tags.owner=platform-team \
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

- [Virtual Networks Overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview)
- [Network Security Groups Overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)
- [Bastion Overview](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview)
