---
description: Repository map for the Azure Virtual Machine Practical Guide — major sections, when to use each, and fast reader journeys for common goals.
---

# Repository Map

Use this page when you want a quick map of the guide before diving into a specific section. It shows the major documentation areas, what each one is for, and a few fast paths for common reader goals.

## Section Guide

| Section | Use When | Start With |
|---|---|---|
| [Start Here](index.md) | You need orientation, service-fit context, or a role-based way to begin reading. | [Overview](overview.md) |
| [Platform](../platform/index.md) | You want to understand how Azure VMs work: lifecycle, disks, networking, identity, and availability. | [Platform Hub](../platform/index.md) |
| [Best Practices](../best-practices/index.md) | You are designing for production and want guardrails for sizing, security, monitoring, patching, and cost. | [Best Practices Hub](../best-practices/index.md) |
| [Operations](../operations/index.md) | You are running VMs day to day and need execution guidance for create, connect, patch, resize, backup, or monitor tasks. | [Operations Hub](../operations/index.md) |
| [Tutorials](../tutorials/index.md) | You want hands-on lab-style practice for high availability, security, Bastion, extensions, or disaster recovery. | [Tutorials Hub](../tutorials/index.md) |
| [Troubleshooting](../troubleshooting/index.md) | You are diagnosing an active issue such as boot failures, connectivity problems, or performance degradation. | [Troubleshooting Hub](../troubleshooting/index.md) |
| [Reference](../reference/index.md) | You need a quick lookup for VM sizes, disk types, availability options, networking components, or monitoring signals. | [Reference Hub](../reference/index.md) |
| [Contributing](../contributing/index.md) | You are updating the guide itself and need repository standards, structure, or validation workflow details. | [Contributing](../contributing/index.md) |

## How the Guide Is Organized

- **Start Here** answers, “Where should I begin?”
- **Platform** explains core VM concepts and service behavior.
- **Best Practices** turns those concepts into production design guidance.
- **Operations** covers day-2 execution after a VM is deployed.
- **Tutorials** give you reproducible labs to practice real tasks.
- **Troubleshooting** helps you move from symptom to evidence to fix.
- **Reference** is the quick-lookup layer for facts, tables, and terminology.

## Reader Journeys

### I'm new to Azure Virtual Machines

1. Read [Overview](overview.md).
2. Read [Learning Paths](learning-paths.md).
3. Read [VM vs Other Compute](vm-vs-other-compute.md).
4. Continue to the [Platform Hub](../platform/index.md).

### I'm planning a production VM deployment

1. Start at [Scenario Router](scenario-router.md).
2. Review the [Platform Hub](../platform/index.md) for sizing, disks, networking, and availability.
3. Move to the [Best Practices Hub](../best-practices/index.md) for production baseline decisions.
4. Use the [Reference Hub](../reference/index.md) for supporting limits and comparison tables.

### I'm operating VMs in production

1. Start at the [Operations Hub](../operations/index.md).
2. Use the [Best Practices Hub](../best-practices/index.md) to validate your production baseline.
3. Keep the [Reference Hub](../reference/index.md) handy for quick lookups.

### I'm responding to an incident

1. Open the [Troubleshooting Hub](../troubleshooting/index.md).
2. If needed, jump to [First 10 Minutes](../troubleshooting/first-10-minutes/index.md).
3. Follow the relevant playbook or use [Quick Diagnosis Cards](../troubleshooting/quick-diagnosis-cards.md).
4. Return to [Operations](../operations/index.md) or [Best Practices](../best-practices/index.md) to harden the environment after recovery.

## See Also

- [Start Here](index.md)
- [Overview](overview.md)
- [Learning Paths](learning-paths.md)
- [Scenario Router](scenario-router.md)
- [Platform Hub](../platform/index.md)
- [Best Practices Hub](../best-practices/index.md)
- [Operations Hub](../operations/index.md)
- [Troubleshooting Hub](../troubleshooting/index.md)
- [Reference Hub](../reference/index.md)

## Sources

- [Azure Virtual Machines overview](https://learn.microsoft.com/en-us/azure/virtual-machines/overview)
- [Choose an Azure compute service](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/compute-decision-tree)
- [Troubleshoot Azure VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/troubleshooting/)
