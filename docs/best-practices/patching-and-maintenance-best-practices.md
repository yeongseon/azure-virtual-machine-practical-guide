---
description: Azure VM patching and maintenance guidance for Update Manager, automatic guest patching, maintenance windows, and safer monthly change execution.
content_validation:
  status: verified
  last_reviewed: 2026-07-25
  reviewer: agent
  core_claims:
    - claim: Azure Update Manager can monitor Windows and Linux update compliance across Azure, on-premises, and other cloud machines from a single pane.
      source: https://learn.microsoft.com/en-us/azure/update-manager/overview
      verified: true
    - claim: Automatic VM guest patching applies Critical and Security patches, follows availability-first orchestration, and installs them during off-peak hours for IaaS VMs.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/automatic-vm-guest-patching
      verified: true
    - claim: Automatic VM guest patching is supported only for VMs created from supported platform images.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/automatic-vm-guest-patching
      verified: true
---

# Patching and Maintenance Best Practices

Patching Azure VMs is an availability and evidence problem, not just a compliance checkbox.

## Why This Matters

Monthly updates are where design debt shows up: unsupported images, unclear ownership, no maintenance window discipline, and no fast way to prove what changed when something breaks.

## Recommended Practices

### Decide who orchestrates patching

- Use Azure Update Manager when you need one service to assess compliance, schedule updates, and govern patching across mixed estates.
- Use automatic guest patching only when the VM image and workload fit the platform-managed model.
- Keep ownership explicit: who approves the window, who validates the workload, and who handles rollback decisions.

### Design maintenance as a production change event

- Define maintenance windows that match the workload’s real off-peak period, not a generic midnight assumption.
- Capture pre-patch and post-patch evidence so responders can separate “patch regression” from “existing issue.”
- Make reboot behavior part of the review, especially for single-instance workloads.

### Validate image support and orchestration fit

- Check whether the VM was created from a supported platform image before relying on automatic guest patching.
- Use custom images only when you also own the patching and image-refresh process.
- Review whether the workload needs platform-managed patching, customer-defined maintenance, or a different operational model.

### Link to platform and operations detail

- For lifecycle background, see [VM Lifecycle](../platform/vm-lifecycle.md).
- For execution steps, see [Patching](../operations/patching.md).

## Common Mistakes / Anti-Patterns

### Anti-Pattern 1: Enabling auto patching without proving the image is supported

This creates false confidence and leaves teams surprised when the expected behavior never happens.

### Anti-Pattern 2: Scheduling patches without workload validation

If no one checks the application path, patching can succeed technically while the service still fails operationally.

### Anti-Pattern 3: Treating every maintenance event as stateless

Single-instance or tightly coupled workloads need explicit drain, reboot, and rollback thinking.

## Validation Checklist

- [ ] The patch orchestration owner is named.
- [ ] The chosen method matches the VM image and workload needs.
- [ ] Maintenance windows reflect real service behavior.
- [ ] Pre-patch and post-patch evidence is captured.
- [ ] Reboot and rollback expectations are documented.

## See Also

- [Monitoring Best Practices](monitoring-best-practices.md)
- [VM Lifecycle](../platform/vm-lifecycle.md)
- [Patching](../operations/patching.md)

## Sources

- [Azure Update Manager Overview](https://learn.microsoft.com/en-us/azure/update-manager/overview)
- [Automatic Guest Patching for Azure Virtual Machines and Scale Sets](https://learn.microsoft.com/en-us/azure/virtual-machines/automatic-vm-guest-patching)
