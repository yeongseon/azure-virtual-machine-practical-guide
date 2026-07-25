---
description: Azure VM security guidance for reducing management-port exposure, using just-in-time access, and keeping privileged administration on a safer path.
content_validation:
  status: verified
  last_reviewed: 2026-07-25
  reviewer: agent
  core_claims:
    - claim: Just-in-time VM access in Defender for Cloud reduces exposure by locking down inbound traffic to selected management ports and opening access only when needed.
      source: https://learn.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-overview
      verified: true
    - claim: When just-in-time access is enabled in Azure, Defender for Cloud ensures deny-all inbound rules exist for the selected ports in network security groups and Azure Firewall rules.
      source: https://learn.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-overview
      verified: true
---

# Security Best Practices

For Azure VMs, strong security starts with the management path. If administration is exposed or poorly controlled, other hardening steps become much less valuable.

## Why This Matters

Attackers do not need an exotic platform failure if open management ports, broad inbound rules, or weak privileged-access patterns already exist. Security reviews should reduce routine exposure before they add advanced controls.

## Recommended Practices

### Reduce the standing attack surface

- Keep inbound management ports closed unless access is actively needed.
- Use Bastion, VPN, or ExpressRoute for day-to-day administration so public exposure is not the default.
- Review NSG intent around management ports as part of every production change.

### Use JIT for exception-based access

- Use Defender for Cloud just-in-time access where the environment already depends on Defender for Servers Plan 2.
- Keep the approval window and source IP scope as small as the operating model allows.
- Treat JIT as a compensating control for necessary management access, not as permission to leave the architecture public-first.

### Separate platform security detail from review guidance

- Use this page for review decisions.
- For deeper platform background, continue to [Identity and Access](../platform/identity-and-access.md).
- For network boundary detail, continue to [Networking Basics](../platform/networking-basics.md).

## Common Mistakes / Anti-Patterns

### Anti-Pattern 1: Leaving SSH or RDP open “for convenience”

Convenience-based exposure becomes standing risk, and cleanup usually happens only after an alert or audit.

### Anti-Pattern 2: Treating JIT as a substitute for private administration

JIT reduces exposure, but it still works best when the management path is already tightly bounded.

### Anti-Pattern 3: Reviewing NSGs without reviewing operator workflow

If responders do not know how access is granted during incidents, they create emergency exceptions that bypass the intended design.

## Validation Checklist

- [ ] Public management access is disabled by default or has an approved exception.
- [ ] JIT is used where the operating model supports Defender for Cloud controls.
- [ ] NSG rules for management ports were reviewed explicitly.
- [ ] The incident workflow for administrative access is documented.
- [ ] Platform-specific identity and access choices were reviewed in the linked platform docs.

## See Also

- [Networking Best Practices](networking-best-practices.md)
- [Identity and Access](../platform/identity-and-access.md)
- [Networking Basics](../platform/networking-basics.md)

## Sources

- [Understand just-in-time virtual machine access](https://learn.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-overview)
