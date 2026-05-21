---
content_sources:
  diagrams:
  - id: troubleshooting-playbooks-index-diagnostic-entry-map
    type: flowchart
    source: self-generated
    description: Diagnostic Entry Map
    based_on:
    - https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/welcome-virtual-machines
    justification: Synthesized for this guide from the referenced Microsoft Learn
      documentation.
content_validation:
  status: pending_review
  last_reviewed: '2026-05-22'
  reviewer: ai-agent
  core_claims:
  - claim: This document has source metadata and is queued for text-level Microsoft
      Learn verification.
    source: https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/welcome-virtual-machines
    verified: false
  - claim: Core Azure VM guidance on this page should remain traceable to the listed
      sources before it is marked verified.
    source: https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/welcome-virtual-machines
    verified: false
---

# Playbooks

These are the canonical VM troubleshooting playbooks. Use the root playbooks first when you need scenario-driven guidance for the most common production failures, then branch into the nested library for older or more specialized flows.

## Diagnostic Entry Map

<!-- diagram-id: troubleshooting-playbooks-index-diagnostic-entry-map -->
```mermaid
flowchart TD
    A[VM incident] --> B{Primary symptom}
    B --> C[VM Boot Failures]
    B --> D[Disk Performance Issues]
    B --> E[Network Connectivity Issues]
    B --> F[RDP and SSH Connection Failures]
    B --> G[Specialized legacy playbooks]
```

## Recommended First-Line Playbooks

| Playbook | When to use it |
|---|---|
| [VM Boot Failures](vm-boot-failures.md) | The VM does not complete boot or never becomes remotely usable. |
| [Disk Performance Issues](disk-performance-issues.md) | Latency, queue depth, or throughput bottlenecks affect the workload. |
| [Network Connectivity Issues](network-connectivity-issues.md) | East-west, north-south, or dependency traffic fails after network changes. |
| [RDP and SSH Connection Failures](rdp-ssh-connection-failures.md) | Administrative sign-in or Bastion-based access fails. |
| [Boot Diagnostics and Serial Console](boot-disk/boot-diagnostics-and-serial-console.md) | You need low-level evidence or recovery access after boot failure. |

## Legacy / Specialized Playbooks

### Connectivity

- [Cannot RDP or SSH](connectivity/cannot-rdp-or-ssh.md)
- [DNS and Connectivity Issues](connectivity/dns-and-connectivity-issues.md)
- [Extension Failures](connectivity/extension-failures.md)

### Performance

- [Slow Performance](performance/slow-performance.md)
- [High CPU / Memory / Disk](performance/high-cpu-memory-disk.md)
- [Nested Disk Performance Playbook](performance/disk-performance-issues.md)

### Boot and Disk

- [VM Won't Start](boot-disk/vm-wont-start.md)
- [Boot Diagnostics and Serial Console](boot-disk/boot-diagnostics-and-serial-console.md)
- [Backup Failures](boot-disk/backup-failures.md)

## See Also

- [Troubleshooting](../index.md)
- [First 10 Minutes](../first-10-minutes/index.md)
- [Decision Tree](../decision-tree.md)

## Sources

- [Troubleshoot Azure virtual machines](https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/welcome-virtual-machines)
