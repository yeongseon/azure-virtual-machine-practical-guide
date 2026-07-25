---
description: Azure VM best practices for production workloads, with a shared baseline and topic-specific guidance for sizing, storage, networking, security, patching, monitoring, backup, and cost.
---

# Best Practices

Use this section as the production review layer for Azure Virtual Machines. Start with the shared baseline, then open the topic page that matches the design decision or risk you are actively reviewing.

## Why This Matters

Azure VM incidents are usually not caused by a single bad setting. They come from mismatched decisions across compute sizing, storage performance, network exposure, patch orchestration, monitoring coverage, and recovery design.

The goal of this section is to separate the **shared baseline** from **topic-specific reviews** so each page answers a different production question.

## Recommended Practices

### Start with the shared baseline

- Read [Production Baseline](production-baseline.md) first for controls that apply to almost every production VM.
- Use the topic pages only after the baseline is in place.
- For platform mechanics, follow the linked `docs/platform/*.md` pages instead of repeating them here.

### Pick the page that matches the current decision

| Decision area | Open this page | Use it when | Deep technical background |
|---|---|---|---|
| Minimum production controls | [Production Baseline](production-baseline.md) | You need a go-live checklist for every VM | [How Azure VM Works](../platform/how-azure-vm-works.md) |
| VM family, quotas, and image governance | [Sizing and Image Selection](sizing-and-image-selection.md) | You are choosing a series, SKU, or source image | [Compute Model](../platform/compute-model.md) |
| Private access and east-west traffic | [Networking Best Practices](networking-best-practices.md) | You are reviewing subnets, NSGs, Bastion, or accelerated networking | [Networking Basics](../platform/networking-basics.md) |
| Disk layout, caching, and throughput limits | [Disk and Storage Best Practices](disk-and-storage-best-practices.md) | You are debugging or preventing storage bottlenecks | [Disks and Storage](../platform/disks-and-storage.md) |
| Privileged access and host hardening | [Security Best Practices](security-best-practices.md) | You are reviewing management-path exposure and identity controls | [Identity and Access](../platform/identity-and-access.md) |
| Patch orchestration and maintenance windows | [Patching and Maintenance Best Practices](patching-and-maintenance-best-practices.md) | You are standardizing monthly update workflows | [VM Lifecycle](../platform/vm-lifecycle.md) |
| Guest + host observability | [Monitoring Best Practices](monitoring-best-practices.md) | You are designing alerts, logs, and evidence capture | [How Azure VM Works](../platform/how-azure-vm-works.md) |
| Restore and failover readiness | [Backup and DR Best Practices](backup-and-dr-best-practices.md) | You need proof that recovery objectives are realistic | [Backup and Recovery Basics](../platform/backup-and-recovery-basics.md) |
| Spend reduction without reliability regressions | [Cost Optimization Best Practices](cost-optimization-best-practices.md) | You are rightsizing or applying purchase discounts | [Compute Model](../platform/compute-model.md) |
| Repeated design mistakes | [Common Anti-Patterns](common-anti-patterns.md) | You want a review board list of what to reject quickly | [Availability and Resiliency](../platform/availability-and-resiliency.md) |

### Keep shared content centralized

- Shared baseline controls live in [Production Baseline](production-baseline.md).
- Topic pages should add only guidance that is specific to that design area.
- If a page mostly needs platform explanation, link to the platform page instead of duplicating it.

## Common Mistakes / Anti-Patterns

- Treating every best-practices page as a full end-to-end VM design guide.
- Repeating the same CLI snippets and review rationale across multiple pages.
- Using a topic page to restate platform documentation instead of adding decision guidance.

## Validation Checklist

- [ ] The shared baseline is reviewed before topic-specific tuning begins.
- [ ] Each production question maps to a single best-practices page.
- [ ] Topic pages link to platform deep dives instead of duplicating them.
- [ ] The selected guidance matches the current risk: sizing, storage, networking, security, patching, monitoring, recovery, or cost.

## See Also

- [Production Baseline](production-baseline.md)
- [Platform](../platform/index.md)
- [Operations](../operations/index.md)

## Sources

- [Azure virtual machines documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/)
- [Availability options for Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/virtual-machines/availability)
