# AGENTS.md

Guidance for AI agents working in this repository.

## Project Overview

**Azure Virtual Machine Practical Guide** — a documentation hub for designing, operating, and troubleshooting Azure Virtual Machines — compute models, disks, networking, availability, backup, and identity.

- **Live site**: <https://yeongseon.github.io/azure-virtual-machine-practical-guide/>
- **Repository**: <https://github.com/yeongseon/azure-virtual-machine-practical-guide>

## Repository Structure

```text
.
├── .github/
│   └── workflows/              # GitHub Pages deployment
├── docs/
│   ├── assets/                 # Images, icons
│   ├── best-practices/         # Production patterns and anti-patterns
│   ├── javascripts/            # Mermaid zoom JS
│   ├── operations/             # Day-2 operational execution
│   ├── platform/               # Architecture and design decisions
│   ├── reference/              # CLI cheatsheet, decision guides
│   ├── start-here/             # Overview, learning paths
│   ├── stylesheets/            # Custom CSS
│   └── troubleshooting/        # Diagnosis and resolution
└── mkdocs.yml                  # MkDocs Material configuration
```

## Content Categories

| Section | Purpose |
|---|---|
| **Start Here** | Entry points, learning paths, overview |
| **Platform** | Architecture, design decisions — WHAT and HOW it works |
| **Best Practices** | Production patterns — HOW to use the platform well |
| **Operations** | Day-2 execution — HOW to run in production |
| **Troubleshooting** | Diagnosis and resolution |
| **Reference** | Quick lookup — CLI, decision guides |

## Documentation Conventions

### File Naming

- All files: `topic-name.md` (kebab-case)
- Index files: `index.md` in each directory

### CLI Command Style

```bash
# ALWAYS use long flags for readability
az vm create --resource-group $RG --name $VM_NAME --image $IMAGE --location $LOCATION

# NEVER use short flags in documentation
az vm create -g $RG -n $VM_NAME  # ❌ Don't do this
```

### Variable Naming Convention

| Variable | Description | Example |
|----------|-------------|---------|
| `$RG` | Resource group name | `rg-vm-demo` |
| `$VM_NAME` | Virtual machine name | `vm-app-001` |
| `$IMAGE` | VM image | `Ubuntu2204` |
| `$SIZE` | VM size | `Standard_D2s_v3` |
| `$LOCATION` | Azure region | `koreacentral` |
| `$SUBSCRIPTION_ID` | Subscription identifier placeholder | `<subscription-id>` |

### PII Removal (Quality Gate)

**CRITICAL**: All CLI output examples MUST have PII removed.

Patterns to mask:

- UUIDs: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
- Subscription IDs: `<subscription-id>`
- Tenant IDs: `<tenant-id>`
- Object IDs: `<object-id>`
- IP addresses: Use RFC 5737 ranges (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24)
- SSH keys: NEVER include private keys
- Passwords: NEVER include

### Admonition Indentation Rule

For MkDocs admonitions (`!!!` / `???`), every line in the body must be indented by **4 spaces**.

```markdown
!!! warning "Important"
    This line is correctly indented.

    - List item also inside
```

### Mermaid Diagrams

All architectural diagrams use Mermaid. Every documentation page should include at least one diagram. Test with `mkdocs build --strict`.

### Nested List Indentation

All nested list items MUST use **4-space indent** (Python-Markdown standard).

### Tail Section Naming

Every document ends with these tail sections (in this order):

| Section | Purpose | Content |
|---|---|---|
| `## See Also` | Internal cross-links within this repository | Links to other pages in this guide |
| `## Sources` | External authoritative references | Links to Microsoft Learn (primary) |

- `## See Also` is required on every page.
- `## Sources` is required when external references are cited.
- Order is always `## See Also` → `## Sources` (never reversed).

### Canonical Document Templates

#### Platform docs

```text
# Title
Brief introduction (1-2 sentences)
## Main Content
### Subsections
## See Also
## Sources
```

#### Best Practices docs

```text
# Title
Brief introduction
## Why This Matters
## Recommended Practices
## Common Mistakes / Anti-Patterns
## Validation Checklist
## See Also
## Sources
```

#### Operations docs

```text
# Title
Brief introduction
## Prerequisites
## When to Use
## Procedure
## Verification
## Rollback / Troubleshooting
## See Also
## Sources
```

#### Troubleshooting docs

```text
# Title
## Symptom
## Possible Causes
## Diagnosis Steps
## Resolution
## Prevention
## See Also
## Sources
```

#### Reference docs

```text
# Title
Brief introduction
## Topic/Command Groups
## Usage Notes
## See Also
## Sources
```

## Build & Preview

```bash
# Install MkDocs dependencies
pip install mkdocs-material mkdocs-minify-plugin

# Build documentation (strict mode catches broken links)
mkdocs build --strict

# Local preview
mkdocs serve
```

## Git Commit Style

```text
type: short description
```

Allowed types: `feat`, `fix`, `docs`, `chore`, `refactor`

## Related Projects

| Repository | Description |
|---|---|
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service practical guide |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions practical guide |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps practical guide |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring practical guide |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking practical guide |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage practical guide |
