#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
LAB_DIR=$(cd "$SCRIPT_DIR/.." && pwd)
EVIDENCE_DIR="$LAB_DIR/evidence"

: "${RG:?Set RG to the lab resource group name before running this script.}"
: "${VM_NAME:?Set VM_NAME to the deployed virtual machine name before running this script.}"
: "${EXTENSION_NAME:?Set EXTENSION_NAME to the deployed extension name before running this script.}"

if ! command -v az >/dev/null 2>&1; then
  printf 'Azure CLI is required but was not found on PATH.\n' >&2
  exit 1
fi

mkdir -p "$EVIDENCE_DIR"

SUBSCRIPTION_ID=$(az account show --query id --output tsv)

az vm extension show \
  --resource-group "$RG" \
  --vm-name "$VM_NAME" \
  --name "$EXTENSION_NAME" \
  --output json > "$EVIDENCE_DIR/az-vm-extension-show.json"

az monitor activity-log list \
  --resource-group "$RG" \
  --resource-id "/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RG/providers/Microsoft.Compute/virtualMachines/$VM_NAME/extensions/$EXTENSION_NAME" \
  --offset 2h \
  --max-events 20 \
  --output table > "$EVIDENCE_DIR/activity-log.txt"

printf 'Captured evidence:\n'
printf '  %s\n' "$EVIDENCE_DIR/az-vm-extension-show.json"
printf '  %s\n' "$EVIDENCE_DIR/activity-log.txt"
