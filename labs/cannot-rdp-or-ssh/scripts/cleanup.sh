#!/usr/bin/env bash
set -euo pipefail

: "${RG:?Set RG to the lab resource group name before running this script.}"

if ! command -v az >/dev/null 2>&1; then
  printf 'Azure CLI is required but was not found on PATH.\n' >&2
  exit 1
fi

az group delete --name "$RG" --yes --no-wait
