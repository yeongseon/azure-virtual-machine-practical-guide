---
description: Azure VM sizing and image selection guidance for choosing the right family, avoiding burst-credit surprises, and governing Marketplace or custom images.
content_validation:
  status: verified
  last_reviewed: 2026-07-25
  reviewer: agent
  core_claims:
    - claim: Azure VM sizes are categorized into families and types optimized for different workload requirements such as CPU, memory, storage, and network bandwidth.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview
      verified: true
    - claim: B-series virtual machines use CPU credits and are throttled back to their base CPU performance when credits are exhausted.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview
      verified: true
    - claim: Marketplace images are identified by publisher, offer, SKU, and version, and some images require purchase terms to be accepted before programmatic deployment.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage
      verified: true
---

# Sizing and Image Selection

Choose VM size and image together. A good SKU on the wrong image, or a good image on the wrong SKU, still creates avoidable operations debt.

## Why This Matters

Sizing mistakes usually show up as noisy symptoms: high CPU, paging, queue buildup, throttled burstable cores, or expensive redesign after purchase commitments were already made. Image mistakes appear later as unsupported patching flows, licensing surprises, or untracked golden-image drift.

## Recommended Practices

### Size by workload shape, not by habit

- Start with the workload’s CPU-to-memory ratio, expected network demand, and storage profile.
- Use general-purpose families for balanced application tiers, compute-optimized families for CPU-heavy workloads, and memory-optimized families for large caches or database tiers.
- Treat burstable B-series as a deliberate choice for low-duty or intermittent workloads, not as the default “cheap production VM.”

### Separate pilot sizing from long-term commitments

- Use early telemetry to prove whether the pilot SKU is still right after real traffic arrives.
- Delay Reservations or Savings Plans until usage is stable enough that the chosen size is likely to remain valid.
- Revisit the decision when guest telemetry shows sustained CPU pressure, memory pressure, or disk queue buildup.

### Govern image provenance

- Record image publisher, offer, SKU, and version for every approved build path.
- Check whether Marketplace images include purchase-plan requirements before automating deployment.
- Keep custom images on the same patching and support review path as Marketplace images; “golden image” is not the same as “automatically maintained image.”

### Use platform docs for series mechanics

- For how Azure VM families are organized, see [Compute Model](../platform/compute-model.md).
- For OS and lifecycle considerations, see [VM Lifecycle](../platform/vm-lifecycle.md).

## Common Mistakes / Anti-Patterns

### Anti-Pattern 1: Sizing by vCPU count alone

This ignores memory ratio, network limits, and storage behavior. It often leads to teams “fixing” the wrong bottleneck.

### Anti-Pattern 2: Using B-series for always-busy production services

Burstable credits are useful only when the workload actually spends time below baseline. Constant pressure turns burstable economics into throttling risk.

### Anti-Pattern 3: Treating image choice as a one-time deployment variable

If no one owns image provenance, patching expectations, and licensing terms, the image becomes an audit and maintenance problem later.

## Validation Checklist

- [ ] The selected VM family matches the workload’s CPU, memory, and network profile.
- [ ] Burstable SKUs are used only where the workload pattern supports CPU credits.
- [ ] The approved image path records publisher, offer, SKU, and version.
- [ ] Marketplace terms were reviewed for any image that requires a purchase plan.
- [ ] The sizing decision will be revalidated with real guest and host telemetry.

## See Also

- [Production Baseline](production-baseline.md)
- [Disk and Storage Best Practices](disk-and-storage-best-practices.md)
- [Compute Model](../platform/compute-model.md)

## Sources

- [Virtual machine sizes overview](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview)
- [Find and use marketplace purchase plan information using the CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage)
