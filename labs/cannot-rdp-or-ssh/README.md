# Lab substrate: cannot RDP or SSH

Authoring-only substrate skeleton for a deterministic Azure VM admin-path connectivity failure. This lab deploys a Linux virtual machine with a public IP and subnet-level NSG where a high-priority rule blocks inbound SSH on TCP 22 even though the VM itself provisions successfully.

This scaffold does **not** include committed live evidence. Real deployment, reproduction, and evidence capture stay deferred until a later validation run against Azure.

## Purpose

- Provide a minimal Bicep substrate for reproducing an NSG-driven management-port failure.
- Keep the failure deterministic by applying a higher-priority deny rule on TCP 22 while leaving the VM healthy.
- Standardize the evidence artifact names for a future live run: `evidence/connection-test.txt` and `evidence/effective-nsg.json`.

## Prerequisites

- Azure CLI with the `bicep` integration available locally.
- Permission to create and delete a resource group, virtual machine, NIC, NSG, VNet, and public IP.
- A current source IP or CIDR that can be used for the post-fix scoped allow rule.

## Deploy the substrate

Set the variables first:

```bash
export RG="rg-vm-adminpath-failure"
export LOCATION="koreacentral"
export VM_NAME="vmconlab-vm"
export SOURCE_CIDR="198.51.100.10/32"
```

```bash
az group create --name "$RG" --location "$LOCATION"
az deployment group create --resource-group "$RG" --template-file labs/cannot-rdp-or-ssh/main.bicep --parameters @labs/cannot-rdp-or-ssh/parameters.json --parameters location="$LOCATION" vmName="$VM_NAME" managementSourcePrefix="$SOURCE_CIDR" adminPassword="<temporary-lab-password>"
```
| Command | Purpose |
| --- | --- |
| `az group create` | Create the resource group that will hold the lab substrate. |
| `--name` | Set the resource group name. |
| `--location` | Set the Azure region for the resource group. |
| `az deployment group create` | Start a resource-group-scope ARM/Bicep deployment for the admin-path connectivity failure lab. |
| `--resource-group` | Target the resource group that will receive the deployment. |
| `--template-file` | Point Azure CLI at `labs/cannot-rdp-or-ssh/main.bicep`. |
| `--parameters` | Supply the parameter file plus explicit overrides for location, VM name, and the scoped management source prefix. |

Replace the RFC 5737 example `SOURCE_CIDR` with your current public source CIDR before the post-fix redeploy. Otherwise the scoped allow rule will not match your real client IP.

Expected result: the deployment reaches a successful terminal state for the VM, but inbound TCP 22 remains blocked by the intentional NSG deny rule.

## Reproduce the failure symptom

Once the substrate exists, run the capture script from the repository root:

```bash
export RG="rg-vm-adminpath-failure"
export VM_NAME="vmconlab-vm"
bash labs/cannot-rdp-or-ssh/scripts/reproduce.sh
```
| Command | Purpose |
| --- | --- |
| `bash labs/cannot-rdp-or-ssh/scripts/reproduce.sh` | Query the effective NSG rules and run the direct TCP 22 check, then write the live artifacts into `labs/cannot-rdp-or-ssh/evidence/`. |

Expected symptom:

- The direct TCP 22 test times out or reports a filtered port.
- The effective NSG payload shows the deny rule winning for inbound TCP 22.
- The VM itself still exists and reports a healthy control-plane state.

## Evidence artifacts to capture

During a live run, `scripts/reproduce.sh` writes these artifacts:

- `evidence/connection-test.txt` — client-side TCP 22 connection result.
- `evidence/effective-nsg.json` — effective NSG payload for the deployed NIC.

This authoring PR commits only honest placeholders for those files. Replace them with real artifacts only after an actual deploy-and-reproduce session.

## Cleanup

```bash
export RG="rg-vm-adminpath-failure"
bash labs/cannot-rdp-or-ssh/scripts/cleanup.sh
```
| Command | Purpose |
| --- | --- |
| `bash labs/cannot-rdp-or-ssh/scripts/cleanup.sh` | Delete the lab resource group without waiting for the long-running operation to finish. |

## See Also

- [Troubleshooting overview](../../docs/troubleshooting/index.md)
- [Evidence placeholder](evidence/README.md)

## Sources

- [Quickstart: Create a Linux virtual machine by using Bicep](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-bicep)
- [Network security groups overview](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)
- [Troubleshoot SSH connections to an Azure Linux VM](https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/troubleshoot-ssh-connection)
