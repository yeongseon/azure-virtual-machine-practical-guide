# Backup and Recovery Basics

Protecting your data from loss and corruption is crucial for enterprise workloads on Azure. Azure Backup and Site Recovery provide integrated disaster recovery and backup.

## Backup and DR Methods

| Method | SLA | RPO / RTO | Use Case |
| --- | --- | --- | --- |
| **Snapshots** | N/A | Flexible / Slow | Quick development point-in-time recovery. |
| **Azure Backup** | Varies | Hours / Days | Long-term retention and backup policy. |
| **ASR** | 99.9% | Minutes / Hours | Full region/datacenter disaster recovery. |

## Backup Architecture

Azure Backup works by installing an agent or using VM extensions to transfer data to the Recovery Services vault.

```mermaid
graph LR
    VM[Virtual Machine] --> Agent[Backup Agent/Extension]
    Agent --> RS-Vault[Recovery Services Vault]
    RS-Vault --> Policy[Backup Policy]
    Policy --> Schedule[Backup Jobs]
```

!!! note
    **RPO (Recovery Point Objective)** is the maximum period of data loss, while **RTO (Recovery Time Objective)** is the time taken to restore services.

!!! tip
    A **Recovery Services vault** stores all backup data and can be configured with locally-redundant (LRS), geo-redundant (GRS), or zone-redundant storage (ZRS).

## Sources
- [Azure Backup overview](https://learn.microsoft.com/en-us/azure/backup/backup-overview)
- [Azure Site Recovery overview](https://learn.microsoft.com/en-us/azure/site-recovery/site-recovery-overview)
- [RPO and RTO definitions](https://learn.microsoft.com/en-us/azure/reliability/reliability-definitions)
