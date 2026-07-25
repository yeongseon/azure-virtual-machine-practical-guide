---
description: "Shared production baseline for Azure VMs: sizing evidence, private administration, storage layout, monitoring coverage, backup proof, and governance controls."
content_validation:
  status: verified
  last_reviewed: 2026-07-25
  reviewer: agent
  core_claims:
    - claim: Azure VM sizes are organized into families and types optimized for different CPU, memory, storage, and network requirements.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview
      verified: true
    - claim: Azure VM host metrics, activity logs, and boot diagnostics are available without extra setup, while guest metrics and logs require Azure Monitor Agent and a data collection rule.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/monitor-vm
      verified: true
    - claim: Azure Backup stores VM backups in a Recovery Services vault and uses snapshots as part of the backup process.
      source: https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction
      verified: true
---

# Production Baseline

Use this page for the controls that should exist on almost every production Azure VM before workload-specific tuning starts.

## Why This Matters

A baseline exists to stop predictable incidents early: wrong VM family, exposed management ports, disk layouts that cannot meet throughput targets, missing guest telemetry, and backups that were configured but never restored.

## Recommended Practices

### Standardize the minimum production envelope

- Record the approved VM family, image source, patching owner, and recovery objective for each workload.
- Treat size selection as a combined CPU, memory, storage, and network decision, not as a vCPU-only choice.
- Keep image selection governed so teams know whether they are using Marketplace images, approved custom images, or hardened publisher images.

### Keep the administration path private by default

- Prefer Bastion, VPN, or ExpressRoute for routine administration.
- Require explicit review before allowing public SSH or RDP exposure.
- Use the security page for JIT and privileged-access controls, but make “private first” the baseline expectation.

### Separate storage, observability, and recovery concerns

- Review OS disk, data disk, caching mode, and VM throughput limits together before go-live.
- Enable host-level monitoring immediately, then add guest metrics and logs with Azure Monitor Agent and data collection rules.
- Protect the VM with backup and schedule a restore drill early enough to influence design, not after sign-off.

### Baseline governance for every VM

| Control area | Minimum production question | If the answer is “no” |
|---|---|---|
| Compute envelope | Do we know why this VM family and size were chosen? | Reopen sizing review before scale or purchase commitments. |
| Admin path | Is administration private by default? | Rework access design before security review. |
| Storage layout | Are disk tier and caching aligned to the workload? | Validate with disk metrics before calling performance “done.” |
| Monitoring | Do we have both host and guest evidence? | Add Azure Monitor Agent and DCR coverage. |
| Recovery | Has someone restored this workload or an equivalent backup? | Treat recovery time as unproven. |
| Ownership | Is there a named owner for patching and backup failures? | Add operational ownership before go-live. |

### Use topic pages for deeper review

- For VM family and image decisions, continue to [Sizing and Image Selection](sizing-and-image-selection.md).
- For storage and throughput planning, continue to [Disk and Storage Best Practices](disk-and-storage-best-practices.md).
- For backup drills and failover planning, continue to [Backup and DR Best Practices](backup-and-dr-best-practices.md).

## Common Mistakes / Anti-Patterns

### Anti-Pattern 1: Calling a VM “production ready” after only a successful deployment

Deployment success proves that Azure accepted the template. It does not prove the size is correct, the admin path is safe, or the recovery path works.

### Anti-Pattern 2: Treating host metrics as full observability

Host metrics can show that a VM is under load, but guest telemetry is still required to understand which service, process, or application component is failing.

### Anti-Pattern 3: Enabling backup without proving restore speed

Backup policy compliance is not the same as recovery readiness. The baseline should assume recovery is unproven until a restore drill exists.

## Validation Checklist

- [ ] VM family, image source, and patching owner are documented.
- [ ] Administration uses a private path or has an approved exception.
- [ ] Disk layout and caching were reviewed with workload expectations.
- [ ] Host metrics are available and guest monitoring is configured.
- [ ] Backup protection exists and restore evidence is scheduled or captured.
- [ ] Topic-specific reviews were completed for any higher-risk area.

## See Also

- [Best Practices](index.md)
- [Sizing and Image Selection](sizing-and-image-selection.md)
- [Backup and DR Best Practices](backup-and-dr-best-practices.md)

## Sources

- [Virtual machine sizes overview](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview)
- [Monitor Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/virtual-machines/monitor-vm)
- [About Azure VM backup](https://learn.microsoft.com/en-us/azure/backup/backup-azure-vms-introduction)
