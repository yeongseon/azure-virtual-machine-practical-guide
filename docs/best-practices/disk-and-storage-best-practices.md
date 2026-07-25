---
description: Azure VM disk and storage guidance for throughput limits, caching choices, disk tier selection, and layout decisions that prevent storage bottlenecks.
content_validation:
  status: verified
  last_reviewed: 2026-07-25
  reviewer: agent
  core_claims:
    - claim: Azure virtual machines have IOPS and throughput limits based on the VM type and size, and the attached disks also have their own limits.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-performance
      verified: true
    - claim: Cached and uncached disk traffic follow different performance paths, and host caching changes which VM storage limits apply.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-performance
      verified: true
    - claim: Disk traffic uses a prioritized network channel in Azure to help disks maintain expected performance during network contention.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-performance
      verified: true
---

# Disk and Storage Best Practices

Disk design for Azure VMs is a throughput and layout problem, not just a disk SKU problem.

## Why This Matters

Teams often buy faster disks and still see poor results because the VM size, caching path, or data layout is the real constraint. Storage reviews need to account for all of those layers together.

## Recommended Practices

### Review VM limits before choosing disk tiers

- Compare required IOPS and throughput against both the disk limits and the VM limits.
- Treat storage design as a combined VM-and-disk envelope so you know which layer will cap the workload first.
- Recheck the envelope after resizing because the bottleneck can move.

### Use caching intentionally

- Decide whether the workload benefits from cached or uncached paths before standardizing host caching.
- Validate write-heavy or log-heavy workloads carefully because the wrong caching mode can hide or amplify latency problems.
- Keep the expected caching behavior documented so responders know what “normal” looks like.

### Separate roles in disk layout

- Keep OS, data, transaction-heavy paths, and temporary data separated when the workload profile justifies it.
- Avoid mixing critical sustained data with temporary or scratch usage assumptions.
- Pair disk design with backup and restore planning so the layout also supports recovery operations.

### Use platform detail for storage mechanics

- For storage building blocks, see [Disks and Storage](../platform/disks-and-storage.md).
- For operations around snapshots and images, see [Snapshots and Images](../operations/snapshots-and-images.md).

## Common Mistakes / Anti-Patterns

### Anti-Pattern 1: Assuming Premium SSD automatically fixes latency

If the VM is capped first, the disk label changes cost more than outcomes.

### Anti-Pattern 2: Enabling the same caching mode on every disk

OS disks, data disks, and transaction-heavy paths can have very different read/write behavior.

### Anti-Pattern 3: Ignoring VM storage caps during rightsizing

Downsizing can silently turn a previously acceptable storage layout into a throttled one.

## Validation Checklist

- [ ] Required IOPS and throughput were compared to both disk and VM limits.
- [ ] Caching mode was chosen based on workload behavior, not copied from a template.
- [ ] OS, data, and scratch responsibilities are separated where needed.
- [ ] Storage metrics exist to confirm the design under real load.
- [ ] Recovery planning considered the chosen disk layout.

## See Also

- [Production Baseline](production-baseline.md)
- [Backup and DR Best Practices](backup-and-dr-best-practices.md)
- [Disks and Storage](../platform/disks-and-storage.md)

## Sources

- [Virtual machine and disk performance](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-performance)
