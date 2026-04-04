# Azure Virtual Machine Practical Guide

A practical guide covering Azure VM platform internals, operations, and troubleshooting — grounded in MS Learn documentation.

## Scope

- ✅ Included: Azure VM platform concepts, operations, security, monitoring, troubleshooting
- ❌ Excluded: OS-specific or application installation tutorials

## Sections

| Section | Purpose |
|---------|---------|
| Start Here | VM overview, comparison with other compute options, reading paths |
| Platform | How Azure VMs work, components, lifecycle |
| Best Practices | Production-ready design and operational guidelines |
| Operations | Step-by-step operational procedures and configuration |
| Troubleshooting | Symptom-based diagnosis and resolution |
| Reference | Quick-lookup summary tables |

## Content Source

All content is grounded in official [Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/) documentation.

## Local Build

```bash
pip install mkdocs-material pymdown-extensions
mkdocs build --strict
mkdocs serve
```
