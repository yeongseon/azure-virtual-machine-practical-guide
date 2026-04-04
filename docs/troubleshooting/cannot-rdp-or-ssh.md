# Cannot RDP or SSH

Connectivity issues often stem from Network Security Group (NSG) misconfigurations, guest OS firewalls, or routing errors. Follow this guide to diagnose and resolve access failures.

## Connectivity Diagnosis Matrix

| Symptom | Check | Resolution |
| :--- | :--- | :--- |
| Connection timeout | NSG Inbound Rules | Allow TCP 3389 (RDP) or 22 (SSH). |
| Connection refused | Guest OS Firewall | Use Serial Console to disable local firewall. |
| Access Denied | VM Agent Status | Reset password or check agent health. |
| Intermittent drops | Network Path | Check Route Table or NVA constraints. |

!!! warning
    Opening RDP or SSH ports directly to the Internet is a security risk. Use Azure Bastion or a VPN for secure administrative access.

## Connectivity Flowchart

```mermaid
graph TD
    A[Connection Failed] --> B{IP Reachable?}
    B -- No --> C[Check NSG & Public IP]
    B -- Yes --> D{Port 3389/22 Open?}
    D -- No --> E[Add NSG Inbound Rule]
    D -- Yes --> F{Agent Responding?}
    F -- No --> G[Reinstall VM Agent]
    F -- Yes --> H[Check Guest OS Firewall]
    C --> I[Test Connectivity]
    E --> I
    G --> I
    H --> I
```

!!! tip
    If standard tools fail, Azure Bastion provides browser-based access over SSL (port 443), bypassing many local network restrictions.

## Sources
- [Troubleshoot RDP connections to an Azure VM](https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/troubleshoot-rdp-connection)
- [Troubleshoot SSH connections to an Azure Linux VM](https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/troubleshoot-ssh-connection)
- [Azure Bastion documentation](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview)
