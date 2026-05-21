---
content_sources:
  diagrams:
  - id: platform-index-azure-vm-architecture
    type: flowchart
    source: self-generated
    description: Azure VM Architecture
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-machines/overview
    - https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview
    - https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview
    justification: Synthesized for this guide from the referenced Microsoft Learn
      documentation.
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/azure/virtual-machines/overview
    verified: false
  - claim: Core Azure VM guidance on this page should remain traceable to the listed
      sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/azure/virtual-machines/overview
    verified: false
---

# Platform Fundamentals

This section explores the core operating principles of the Azure Virtual Machine platform. We focus on how the infrastructure behaves and the underlying components that power your virtualized workloads.

## Section Contents

| Page | Description |
|------|-------------|
| [How Azure VM Works](how-azure-vm-works.md) | Exploration of hosts, hypervisors, guest OS, and management/data planes. |
| [Compute Model](compute-model.md) | Understanding VM size families, vCPU/memory ratios, and burstable series. |
| [VM Lifecycle](vm-lifecycle.md) | Managing states: create, start, stop, deallocate, redeploy, and reimage. |
| [Disks and Storage](disks-and-storage.md) | Differentiating OS, data, and temp disks, plus managed disk caching. |
| [Networking Basics](networking-basics.md) | Core components: VNet, subnet, NIC, NSG, and Public IP addressing. |
| [Identity and Access](identity-and-access.md) | Securing workloads with RBAC, managed identities, and Key Vault integration. |
| [Availability and Resiliency](availability-and-resiliency.md) | Designing for uptime with Availability Sets, Zones, Scale Sets, and SLAs. |
| [Backup and Recovery Basics](backup-and-recovery-basics.md) | Introduction to Azure Backup, snapshots, and disaster recovery strategies. |

## Azure VM Architecture

<!-- diagram-id: platform-index-azure-vm-architecture -->
```mermaid
graph TD
    User(User/API) --> MP(Management Plane)
    MP --> Fabric(Azure Fabric Controller)
    Fabric --> Host(Physical Host)
    Host --> Hyp(Hypervisor)
    Hyp --> VM1(VM Instance)
    Hyp --> VM2(VM Instance)

    subgraph "Infrastructure"
    Host
    Hyp
    end
```

!!! note
    Understanding the distinction between "Stop" and "Deallocate" is crucial for cost management and resource allocation within the Azure platform. See [VM Lifecycle](vm-lifecycle.md) for details.

## See Also

- [How Azure VM Works](how-azure-vm-works.md)
- [Compute Model](compute-model.md)
- [VM Lifecycle](vm-lifecycle.md)

## Sources
- [Azure VM Architecture](https://learn.microsoft.com/en-us/azure/virtual-machines/overview)
- [Sizes for Virtual Machines](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview)
- [Managed Disks Overview](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview)
