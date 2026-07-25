---
description: Azure VM monitoring guidance for combining host and guest evidence, using Azure Monitor Agent, and building alerts that help during real incidents.
content_validation:
  status: verified
  last_reviewed: 2026-07-25
  reviewer: agent
  core_claims:
    - claim: VM host metrics, activity logs, and boot diagnostics are available without additional setup.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/monitor-vm
      verified: true
    - claim: Guest data collection for Azure VMs requires Azure Monitor Agent and a data collection rule, and VM insights can automate initial onboarding.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/monitor-vm
      verified: true
    - claim: Azure Monitor provides platform metrics automatically for Azure VMs.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/monitor-vm
      verified: true
---

# Monitoring Best Practices

Useful VM monitoring answers two questions fast: what changed, and is the problem on the host, in the guest, or in the workload running inside it?

## Why This Matters

Host-only visibility is not enough for application issues, and guest-only visibility is not enough for platform events. The fastest incident response comes from combining both.

## Recommended Practices

### Build a layered evidence model

- Start with host metrics, activity logs, and boot diagnostics because Azure provides them without extra setup.
- Add guest metrics and logs with Azure Monitor Agent and data collection rules so responders can drill into process- or OS-level behavior.
- Use the same evidence model in normal operations and incident response so alerts map to real investigations.

### Use VM insights as an onboarding accelerator

- Use VM insights when you want predefined performance charts and easier onboarding for guest monitoring.
- Extend beyond the defaults when the workload needs application-specific counters, Windows events, Syslog, or text-log collection.
- Treat “enabled monitoring” as the starting point, not the finished design.

### Alert on evidence that changes decisions

- Prefer alerts that trigger a specific response: resize review, disk investigation, guest service restart, or backup validation.
- Pair host signals with guest evidence whenever the workload impact depends on what runs inside the VM.
- Keep the activity log in scope for control-plane changes such as resize, restart, redeploy, or extension update.

## Common Mistakes / Anti-Patterns

### Anti-Pattern 1: Depending on guest tools alone

Guest data will not explain every platform event, especially if the guest is unhealthy or not responding.

### Anti-Pattern 2: Depending on host metrics alone

Platform CPU or disk signals can identify pressure, but not always the service or process causing it.

### Anti-Pattern 3: Enabling VM insights and stopping there

Default charts are helpful, but production monitoring still needs workload-specific alerts and evidence retention decisions.

## Validation Checklist

- [ ] Host metrics, activity logs, and boot diagnostics are available.
- [ ] Guest monitoring uses Azure Monitor Agent and a defined DCR.
- [ ] Alerts map to an explicit operator action.
- [ ] VM insights defaults were reviewed against workload-specific needs.
- [ ] Incident responders can correlate platform and guest evidence quickly.

## See Also

- [Production Baseline](production-baseline.md)
- [Patching and Maintenance Best Practices](patching-and-maintenance-best-practices.md)
- [How Azure VM Works](../platform/how-azure-vm-works.md)

## Sources

- [Monitor Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/virtual-machines/monitor-vm)
