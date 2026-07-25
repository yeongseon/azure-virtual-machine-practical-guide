---
description: Azure VM cost optimization guidance for rightsizing first, choosing savings plans or reservations carefully, and using auto-shutdown only where operations allow it.
content_validation:
  status: verified
  last_reviewed: 2026-07-25
  reviewer: agent
  core_claims:
    - claim: Savings plans are commitment-based discounts that apply automatically each hour to eligible usage within the plan scope.
      source: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-overview
      verified: true
    - claim: Savings plans differ from reservations because savings plans apply across eligible usage while reservations are tied to specific resource characteristics.
      source: https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-overview
      verified: true
    - claim: Auto-shutdown can reduce VM costs by shutting down VMs during off hours when they are not needed.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/auto-shutdown-vm
      verified: true
---

# Cost Optimization Best Practices

The safest way to lower Azure VM spend is to remove waste without damaging performance, patchability, or recovery objectives.

## Why This Matters

Cost programs fail when they optimize only the compute line item. VM bills also reflect wrong sizing, idle time, premium storage choices, and purchase commitments made before the workload is understood.

## Recommended Practices

### Rightsize before committing

- Use recent host and guest evidence before buying Reservations or Savings Plans.
- Treat long-term commitments as a follow-up to stable usage, not as the first optimization step.
- Recheck rightsizing after application changes, patching shifts, or architecture simplification.

### Choose the commitment model that matches volatility

- Use Savings Plans when the compute footprint is eligible but likely to vary across services, regions, or SKUs.
- Use Reservations when the resource pattern is predictable enough that a narrower commitment is acceptable.
- Keep the storage, licensing, and network portions of the bill visible, because compute discounts do not solve those lines automatically.

### Use scheduling and shutdown controls carefully

- Use auto-shutdown for labs, training, and other environments that truly can be off outside business hours.
- Do not assume that non-production always means safe-to-shutdown; some shared utility VMs still support active workflows.
- Review orphaned disks, public IPs, backup retention, and other “attached-to-VM” costs during the same review.

## Common Mistakes / Anti-Patterns

### Anti-Pattern 1: Buying commitments before rightsizing

This locks waste into the contract instead of removing it.

### Anti-Pattern 2: Calling a VM “idle” because average CPU is low

Low CPU alone does not prove the workload is overprovisioned or safe to schedule off.

### Anti-Pattern 3: Optimizing compute while ignoring storage and operational side effects

The VM might be cheaper per hour but more expensive overall if disks, backup, or operations toil increase.

## Validation Checklist

- [ ] Rightsizing evidence was reviewed before purchase commitments.
- [ ] The team intentionally chose between Savings Plans and Reservations.
- [ ] Auto-shutdown is used only where the operating model allows it.
- [ ] Storage and other attached costs were reviewed with compute spend.
- [ ] Reliability and recovery objectives stayed intact after the cost change.

## See Also

- [Production Baseline](production-baseline.md)
- [Sizing and Image Selection](sizing-and-image-selection.md)
- [Compute Model](../platform/compute-model.md)

## Sources

- [What are savings plans?](https://learn.microsoft.com/en-us/azure/cost-management-billing/savings-plan/savings-plan-overview)
- [Auto-shutdown a VM](https://learn.microsoft.com/en-us/azure/virtual-machines/auto-shutdown-vm)
