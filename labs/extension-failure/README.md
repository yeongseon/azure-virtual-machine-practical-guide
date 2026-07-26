# Lab substrate: VM extension failure

Authoring-only substrate skeleton for a deterministic Azure VM extension failure. This lab deploys a Linux virtual machine and attaches a Custom Script extension that exits with a non-zero status so the extension reaches a visible failed state.

This scaffold does **not** include committed live evidence. Real deployment, reproduction, and evidence capture stay deferred until a later validation run against Azure.

## Purpose

- Provide a minimal Bicep substrate for reproducing a VM extension provisioning failure.
- Keep the failure deterministic by using an inline shell command that always exits `42`.
- Standardize the evidence artifact names for a future live run: `evidence/az-vm-extension-show.json` and `evidence/activity-log.txt`.

## Prerequisites

- Azure CLI with the `bicep` integration available locally.
- Permission to create and delete a resource group, virtual machine, NIC, NSG, VNet, public IP, and VM extension.
- A temporary lab-only administrator password supplied at deploy time.

## Deploy the substrate

Set the variables first:

```bash
export RG="rg-vm-extension-failure"
export LOCATION="koreacentral"
export VM_NAME="vmextlab-vm"
export EXTENSION_NAME="failingCustomScript"
```

```bash
az group create --name "$RG" --location "$LOCATION"
az deployment group create --resource-group "$RG" --template-file labs/extension-failure/main.bicep --parameters @labs/extension-failure/parameters.json --parameters location="$LOCATION" vmName="$VM_NAME" extensionName="$EXTENSION_NAME" adminPassword="<temporary-lab-password>"
```
| Command | Purpose |
| --- | --- |
| `az group create` | Create the resource group that will hold the lab substrate. |
| `--name` | Set the resource group name. |
| `--location` | Set the Azure region for the resource group. |
| `az deployment group create` | Start a resource-group-scope ARM/Bicep deployment for the failing VM extension lab. |
| `--resource-group` | Target the resource group that will receive the deployment. |
| `--template-file` | Point Azure CLI at `labs/extension-failure/main.bicep`. |
| `--parameters` | Supply the parameter file plus explicit overrides for location, VM name, extension name, and the temporary lab password. |

Expected result: the deployment reaches a failed terminal state because the Custom Script extension intentionally exits with code `42` after the VM itself provisions successfully.

## Reproduce the failure symptom

Once the substrate exists, run the capture script from the repository root:

```bash
export RG="rg-vm-extension-failure"
export VM_NAME="vmextlab-vm"
export EXTENSION_NAME="failingCustomScript"
bash labs/extension-failure/scripts/reproduce.sh
```
| Command | Purpose |
| --- | --- |
| `bash labs/extension-failure/scripts/reproduce.sh` | Query the failed extension state and related activity-log entries, then write the live artifacts into `labs/extension-failure/evidence/`. |

Expected symptom:

- `provisioningState` for the extension reports `Failed`.
- `instanceView.statuses` includes a Custom Script execution failure with the non-zero exit code.
- The activity log shows the VM extension write operation ending in failure for the same VM.

## Evidence artifacts to capture

During a live run, `scripts/reproduce.sh` writes these artifacts:

- `evidence/az-vm-extension-show.json` — direct CLI surface for the failing extension instance.
- `evidence/activity-log.txt` — recent activity-log entries for the extension failure window.

Do not commit fabricated placeholders for those files. Only commit them after an actual deploy-and-reproduce session.

## Cleanup

```bash
export RG="rg-vm-extension-failure"
bash labs/extension-failure/scripts/cleanup.sh
```
| Command | Purpose |
| --- | --- |
| `bash labs/extension-failure/scripts/cleanup.sh` | Delete the lab resource group without waiting for the long-running operation to finish. |

## See Also

- [Troubleshooting overview](../../docs/troubleshooting/index.md)
- [Evidence placeholder](evidence/README.md)

## Sources

- [Azure custom script extension for Linux virtual machines](https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/custom-script-linux)
- [Use Bicep to create virtual machines](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/quickstart-create-virtual-machine)
- [Azure VM extensions and features](https://learn.microsoft.com/en-us/azure/virtual-machines/extensions/overview)
