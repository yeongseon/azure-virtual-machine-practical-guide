---
description: Azure VM networking guidance for private administration, accelerated networking, latency-aware placement, and safer connectivity boundaries.
content_validation:
  status: verified
  last_reviewed: 2026-07-25
  reviewer: agent
  core_claims:
    - claim: Accelerated Networking improves VM networking performance by reducing latency, jitter, and CPU utilization.
      source: https://learn.microsoft.com/en-us/azure/virtual-network/accelerated-networking-overview
      verified: true
    - claim: You can enable Accelerated Networking only on supported VM sizes, and the VM must be stopped and deallocated before enabling it.
      source: https://learn.microsoft.com/en-us/azure/virtual-network/accelerated-networking-overview
      verified: true
    - claim: Availability Zones are physically separate zones within a region with distinct power, network, and cooling.
      source: https://learn.microsoft.com/en-us/azure/virtual-machines/availability
      verified: true
---

# Networking Best Practices

Networking decisions define who can reach the VM, how traffic behaves under load, and how hard it will be to prove root cause during connectivity incidents.

## Why This Matters

VM networking debt often stays hidden until one of three moments: an audit finds public management exposure, an application tier starts dropping packets under load, or a failover test proves that the network path was never really designed for recovery.

## Recommended Practices

### Keep administration private by default

- Prefer Bastion, VPN, or ExpressRoute over direct public SSH or RDP exposure.
- Treat public management ports as an exception that requires explicit expiry and review.
- Keep the management path separate from the application path when possible so incident response can continue during frontend failures.

### Use Accelerated Networking deliberately

- Check whether the selected VM size supports Accelerated Networking before standardizing it.
- Enable it for traffic-sensitive workloads where latency, jitter, or host CPU overhead matter.
- Remember that enabling it on an existing VM requires the VM to be stopped and deallocated.

### Design for failure domains and latency together

- Use zonal placement or scale-set distribution when the workload needs resilience to single-zone failure.
- When low-latency east-west traffic matters, review placement strategy alongside availability requirements instead of treating them as separate topics.
- Validate NSGs, routes, DNS, and load balancer dependencies as one connectivity system.

### Link to platform detail instead of duplicating it

- For network building blocks, see [Networking Basics](../platform/networking-basics.md).
- For higher-level resilience choices, see [Availability and Resiliency](../platform/availability-and-resiliency.md).

## Common Mistakes / Anti-Patterns

### Anti-Pattern 1: Defaulting to public management ports

This turns routine scanning into a standing exposure and makes later hardening much more disruptive.

### Anti-Pattern 2: Assuming a larger VM automatically fixes network symptoms

If the real issue is missing Accelerated Networking, bad route design, or load-balancer behavior, resizing alone only adds cost.

### Anti-Pattern 3: Treating availability placement and latency placement as unrelated

Zone strategy, load balancing, and proximity expectations affect each other. Reviewing only one of them creates surprise tradeoffs later.

## Validation Checklist

- [ ] The administration path is private by default.
- [ ] Accelerated Networking support was checked for the selected VM size.
- [ ] The team knows whether the VM should be zonal, regional, or part of a scale set.
- [ ] NSGs, routing, DNS, and load-balancer dependencies were reviewed together.
- [ ] The final networking design is documented in terms responders can validate during an outage.

## See Also

- [Production Baseline](production-baseline.md)
- [Security Best Practices](security-best-practices.md)
- [Networking Basics](../platform/networking-basics.md)

## Sources

- [Azure Accelerated Networking Overview and Benefits](https://learn.microsoft.com/en-us/azure/virtual-network/accelerated-networking-overview)
- [Availability options for Azure Virtual Machines](https://learn.microsoft.com/en-us/azure/virtual-machines/availability)
