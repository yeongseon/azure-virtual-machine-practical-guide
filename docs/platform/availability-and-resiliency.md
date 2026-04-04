# Availability and Resiliency

To ensure high availability, Azure provides various tools and strategies to mitigate failures, ranging from hardware faults to entire datacenter outages.

## Availability Options

| Option | SLA | Protection Scope | Cost Impact |
| --- | --- | --- | --- |
| **Single VM** | 99.9% (Premium SSD) | No built-in redundancy; single-instance SLA only. | Base cost |
| **Availability Sets** | 99.95% | Fault and update domain faults. | No extra cost |
| **Availability Zones** | 99.99% | Entire datacenter failure. | Potential data transfer cost |
| **VMSS** | Depends on config | Automatic scaling and high availability. | Scale-out costs |

## Availability Zone vs Availability Set Architecture

Availability Zones are separate datacenters in one region. Availability Sets distribute VMs across fault and update domains within a datacenter; they do not protect against full datacenter failures.

```mermaid
graph TD
    Region[Azure Region]
    Region --> AZ1[Zone 1 Datacenter]
    Region --> AZ2[Zone 2 Datacenter]
    Region --> AZ3[Zone 3 Datacenter]

    Region --> DC1[Single Datacenter]
    DC1 --> ASet[Availability Set]
    ASet --> FD1[Fault Domain 1]
    ASet --> FD2[Fault Domain 2]
    ASet --> UD1[Update Domain 1]
    ASet --> UD2[Update Domain 2]
```

!!! note
    **Fault Domains (FD)** protect against physical hardware failures, while **Update Domains (UD)** protect against scheduled maintenance.

!!! tip
    **Virtual Machine Scale Sets (VMSS)** allow you to create and manage a group of load-balanced VMs automatically.

## See Also

- [Backup and DR Best Practices](../best-practices/backup-and-dr-best-practices.md)

## Sources
- [Azure VM availability options](https://learn.microsoft.com/en-us/azure/virtual-machines/availability)
- [Availability Sets overview](https://learn.microsoft.com/en-us/azure/virtual-machines/availability-set-overview)
- [Availability Zones overview](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)
