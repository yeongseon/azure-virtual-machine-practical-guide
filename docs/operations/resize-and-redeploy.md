# Resize and Redeploy

Resizing and redeploying allow you to resolve performance bottlenecks or host-level issues. Both operations trigger a VM reboot but serve different operational purposes.

## Resize vs. Redeploy Matrix

| Feature | Resize | Redeploy |
| :--- | :--- | :--- |
| **Primary Goal** | Change CPU/RAM/IOPS | Move to new hardware |
| **Downtime** | Yes (Reboot) | Yes (Move + Reboot) |
| **Data Impact** | Temp Disk Data Lost | Temp Disk Data Lost |
| **Target** | New Size SKU | New Host Machine |

## Operation Decision Tree

```mermaid
flowchart TD
    A[Performance Issue?] --> B{Cause?}
    B -->|Need more RAM/CPU| C[Resize VM]
    B -->|Host Errors/Hang| D[Redeploy VM]
    C --> E[Verify Size in Region]
    D --> F[Move to New Node]
    E --> G[Apply New SKU]
    F --> H[Reboot on New Host]
    G --> I[Done]
    H --> I
```

!!! note
    When resizing, if the current host does not support the new SKU, the VM must be Deallocated (Stopped) first to release hardware resources.

## Sources

* [Resize a Windows VM](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/resize-vm)
* [Redeploy virtual machine to new Azure node](https://learn.microsoft.com/en-us/azure/virtual-machines/redeploy-to-new-node)
* [Resize a Linux VM with Azure CLI](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/resize-vm)
