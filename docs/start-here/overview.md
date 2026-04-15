---
content_sources:
  diagrams:
  - id: start-here-overview-resource-hierarchy
    type: flowchart
    source: mslearn-adapted
    description: Resource Hierarchy
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-machines/overview
    - https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility
---

# Azure VM Overview

Azure Virtual Machines (VMs) provide on-demand, high-scale, and secure Infrastructure-as-a-Service (IaaS) compute. This service allows you to run virtualized environments in the cloud with complete control over the operating system and its configurations.

## Key Characteristics

| Component | Description | Included Resources |
| :--- | :--- | :--- |
| **Compute** | Scalable CPU and RAM configurations | Virtual Machine (SKU) |
| **Storage** | Persistent virtual hard disks | OS Disk, Data Disks |
| **Networking** | Connectivity and security boundaries | NIC, Public IP, NSG, VNet |
| **Identity** | Managed access control | Role-Based Access Control (RBAC), Managed Identity |

## Resource Hierarchy

<!-- diagram-id: start-here-overview-resource-hierarchy -->
```mermaid
graph TD
    Sub[Subscription] --> RG[Resource Group]
    RG --> VM[Virtual Machine]
    VM --> NIC[Network Interface]
    VM --> OSD[OS Disk (Managed Disk)]
    VM --> DSK[Data Disks (Managed Disks)]
    NIC --> VNET[Virtual Network]
    NIC --> NSG[Network Security Group]
    NIC --> PIP[Public IP Address]
```

## Shared Responsibility

Azure manages the underlying physical infrastructure, while you handle everything inside the virtualized environment.

| Area | You Manage | Azure Manages |
| :--- | :---: | :---: |
| Physical Hardware | | ✔ |
| Virtualization Layer | | ✔ |
| Operating System | ✔ | |
| Applications & Data | ✔ | |
| Network Security (NSG) | ✔ | |

!!! note
    While Azure manages the host hardware, you are responsible for patching the guest OS unless you use specialized services like Azure Automanage.

## Scope of This Guide

- **Included:** Practical configuration, deployment, security, and maintenance of Azure VMs.
- **Excluded:** Azure Kubernetes Service (AKS) deep dives, App Service dev-ops, or non-compute services.

## See Also

- [VM vs Other Compute Options](vm-vs-other-compute.md)
- [Platform Fundamentals](../platform/index.md)
- [Best Practices](../best-practices/index.md)

## Sources

- [Azure Virtual Machines Overview](https://learn.microsoft.com/en-us/azure/virtual-machines/overview)
- [Shared responsibility in the cloud](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility)
