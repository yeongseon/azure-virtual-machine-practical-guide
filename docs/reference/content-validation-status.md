---
content_sources:
  diagrams:
  - id: reference-content-validation-status-summary
    type: pie
    source: self-generated
    description: Summary
    based_on:
    - https://learn.microsoft.com/en-us/azure/virtual-machines/overview
    - https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/overview
    - https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview
    - https://learn.microsoft.com/en-us/azure/virtual-machines/availability
    - https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/overview
    - https://learn.microsoft.com/en-us/azure/reliability/reliability-virtual-machines
    justification: Synthesized for this guide from the referenced Microsoft Learn
      documentation.
---

# Content Source Validation Status

This page tracks the source validation status of all documentation content, including diagrams and text content. All content must be traceable to official Microsoft Learn documentation.

## Summary

*Generated: 2026-04-10*

| Content Type | Total | ✅ MSLearn Sourced | ⚠️ Self-Generated | ❌ No Source |
|---|---:|---:|---:|---:|
| Mermaid Diagrams | 90 | 50 | 40 | 0 |
| Text Sections | — | — | — | — |

!!! warning "Validation Required"
    All mermaid diagrams now include source metadata. Self-generated diagrams remain acceptable only when they clearly cite the Microsoft Learn articles they were synthesized from.
    
    1. Linked to an official MSLearn URL, OR
    2. Marked as `self-generated` with clear justification

<!-- diagram-id: reference-content-validation-status-summary -->
```mermaid
pie title Content Source Status
    "MSLearn Adapted" : 50
    "Self-Generated" : 40
```

## Validation Categories

### Source Types

| Type | Description | Allowed? |
|---|---|---|
| `mslearn` | Content directly from or based on Microsoft Learn | ✅ Yes |
| `mslearn-adapted` | MSLearn content adapted for this guide | ✅ Yes (with source URL) |
| `self-generated` | Original content created for this guide | ⚠️ Requires justification |
| `community` | From community sources (Stack Overflow, GitHub) | ❌ Not for core content |
| `unknown` | Source not documented | ❌ Must be validated |

### Diagram Validation Status

#### Diagram Inventory (90 total)

| File | Diagrams | Source Type | MSLearn URL | Status |
|---|---:|---|---|---|
| All Mermaid diagrams | 90 | mixed (`mslearn-adapted`, `self-generated`) | See document frontmatter | ✅ Validated |

## How to Validate Content

### Step 1: Add Source Metadata to Frontmatter

Add `content_sources` to the document's YAML frontmatter:

```yaml
---
title: How Azure Virtual Machines Work
content_sources:
  diagrams:
    - id: architecture-overview
      type: flowchart
      source: mslearn
      mslearn_url: https://learn.microsoft.com/en-us/azure/virtual-machines/
      description: "Azure VM architecture overview"
    - id: request-flow
      type: sequence
      source: self-generated
      justification: "Synthesized from multiple MSLearn articles for clarity"
      based_on:
        - https://learn.microsoft.com/en-us/azure/virtual-machines/
  text:
    - section: "## Summary"
      source: mslearn-adapted
      mslearn_url: https://learn.microsoft.com/en-us/azure/virtual-machines/
---
```

### Step 2: Mark Diagram Blocks with IDs

Add an HTML comment before each mermaid block to identify it:

```markdown
<!-- diagram-id: architecture-overview -->
```mermaid
flowchart TD
    A[Client] --> B[Azure VM]
```
```

### Step 3: Run Validation Script

```bash
python3 scripts/validate_content_sources.py
```

### Step 4: Update This Page

```bash
python3 scripts/generate_content_validation_status.py
```

## Validation Rules

!!! danger "Mandatory Rules"
    1. **Platform diagrams** (`docs/platform/`) MUST have MSLearn sources
    2. **Architecture diagrams** MUST reference official Microsoft documentation
    3. **Troubleshooting flowcharts** MAY be self-generated if they synthesize MSLearn content
    4. **Self-generated content** MUST have `justification` field explaining the source basis

## Official MSLearn Architecture References

Use these official sources for diagram validation:

| Topic | MSLearn URL |
|---|---|
| Azure Virtual Machines Overview | https://learn.microsoft.com/en-us/azure/virtual-machines/ |
| VM Sizes | https://learn.microsoft.com/en-us/azure/virtual-machines/sizes |
| VM Networking | https://learn.microsoft.com/en-us/azure/virtual-network/ |
| VM Storage | https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types |
| VM Backup | https://learn.microsoft.com/en-us/azure/backup/ |
| VM Security | https://learn.microsoft.com/en-us/azure/security/fundamentals/virtual-machines-overview |

## See Also

- [Tutorial Validation Status](validation-status.md)
- [Reference Index](index.md)
