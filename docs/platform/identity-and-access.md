---
hide:
- toc
content_sources:
  diagrams:
  - id: platform-identity-and-access-managed-identity-and-key-vault
    type: flowchart
    source: mslearn-adapted
    description: Managed Identity and Key Vault
    based_on:
    - https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles
    - https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview
    - https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-just-in-time-access
---

# Identity and Access

Azure Role-Based Access Control (RBAC) helps you manage who has access to Azure resources, what they can do with those resources, and what areas they have access to.

## RBAC Roles

| Role | Permissions | Scope |
| --- | --- | --- |
| **Owner** | Full access to all resources and management. | Subscription, Resource Group, Resource |
| **Contributor** | Can create/manage all resource types but not grant access. | Subscription, Resource Group, Resource |
| **VM Contributor** | Can manage VM resources, but not virtual networks or storage accounts outside VM resource scope. | Subscription, Resource Group, Resource |
| **Reader** | Can view existing resources but not modify. | Subscription, Resource Group, Resource |

## Managed Identity and Key Vault

Managed identities provide an identity for applications to use when connecting to resources that support Microsoft Entra authentication.

<!-- diagram-id: platform-identity-and-access-managed-identity-and-key-vault -->
```mermaid
graph LR
    VM[Virtual Machine] --> MI[Managed Identity]
    MI --> AKV[Azure Key Vault]
    AKV --> Sec[Secrets/Certs]
    Sec --> VM
```

!!! tip
    Use **System-assigned managed identity** for single-resource identity and **User-assigned managed identity** when multiple resources need the same identity.

!!! warning
    Just-In-Time (JIT) VM access reduces exposure to brute force attacks by providing controlled access only when needed.

!!! note
    RDP/SSH access does not require a public IP. Use Azure Bastion (recommended), VPN/ExpressRoute, or private IP connectivity from a connected network.

## See Also

- [Connect to VM](../operations/connect-to-vm.md)
- [Production Baseline](../best-practices/production-baseline.md)
- [Glossary](../reference/glossary.md)

## Sources
- [Azure RBAC built-in roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles)
- [What are managed identities?](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
- [JIT VM access](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-just-in-time-access)
