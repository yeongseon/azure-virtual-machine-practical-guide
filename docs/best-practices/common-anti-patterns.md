---
description: "Common Azure VM anti-patterns that create repeated incidents: public management paths, unsupported patching assumptions, storage bottlenecks, and unproven recovery."
content_validation:
  status: verified
  last_reviewed: 2026-07-25
  reviewer: agent
  core_claims:
    - claim: Just-in-time VM access is designed to reduce exposure of management ports such as RDP and SSH.
      source: https://learn.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-overview
      verified: true
    - claim: Azure virtual machines and attached disks have separate performance limits, so either layer can become the bottleneck.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/disks-performance
      verified: true
    - claim: Azure Backup takes snapshots for Azure VMs and transfers backup data to a Recovery Services vault as part of the backup process.
      source: https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction
      verified: true
---

# Common Anti-Patterns

Use this page as a review-board shortcut. If one of these patterns appears, stop and reopen the design before scaling it out.

## Why This Matters

Most repeated Azure VM incidents are not new platform failures. They are familiar shortcuts that were accepted as temporary and quietly became the operating model.

## Recommended Practices

### Reject these patterns early

| Anti-pattern | Why it keeps recurring | Better direction |
|---|---|---|
| Public SSH or RDP as the default | Fast for setup, expensive for security and incident handling | Use private administration and JIT where needed |
| Sizing by average CPU only | Easy to measure, weak predictor of real bottlenecks | Review memory, storage, and network together |
| Premium disk upgrade as the first storage fix | Looks decisive, often misses the VM cap or caching issue | Validate the full storage path first |
| Auto patching without image or reboot review | Sounds “managed,” but can still misfit the workload | Match patching mode to image and maintenance design |
| Backup policy without restore proof | Green dashboards feel reassuring | Run restore drills and document evidence |
| Commit discounts before design stabilizes | Creates visible savings quickly | Rightsize first, then commit |

### Use the topic pages as remediation paths

- For exposed management paths, open [Security Best Practices](security-best-practices.md).
- For weak sizing logic, open [Sizing and Image Selection](sizing-and-image-selection.md).
- For storage bottlenecks, open [Disk and Storage Best Practices](disk-and-storage-best-practices.md).
- For unproven recovery, open [Backup and DR Best Practices](backup-and-dr-best-practices.md).

## Common Mistakes / Anti-Patterns

### Anti-Pattern 1: Accepting “temporary” public access without an expiry

Temporary exceptions become permanent architecture surprisingly often.

### Anti-Pattern 2: Solving symptoms in isolation

Changing only the VM size, only the disk tier, or only the NSG often leaves the real design issue untouched.

### Anti-Pattern 3: Confusing compliant settings with proven operations

Configured monitoring, backup, or patching is weaker evidence than tested monitoring, restore, and maintenance workflows.

## Validation Checklist

- [ ] Reviewers can identify which anti-patterns are present before approving go-live.
- [ ] Each detected anti-pattern maps to a topic-specific remediation page.
- [ ] Exceptions have a named owner and expiry.
- [ ] Evidence exists for restore, monitoring, and maintenance workflows.

## See Also

- [Security Best Practices](security-best-practices.md)
- [Disk and Storage Best Practices](disk-and-storage-best-practices.md)
- [Backup and DR Best Practices](backup-and-dr-best-practices.md)

## Sources

- [Understand just-in-time virtual machine access](https://learn.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-overview)
- [Virtual machine and disk performance](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-performance)
- [About Azure VM backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction)
