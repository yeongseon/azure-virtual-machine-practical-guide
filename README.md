# Azure Virtual Machine Practical Guide

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

📘 Documentation site: <https://yeongseon.github.io/azure-virtual-machine-practical-guide/>

[![Docs](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/docs.yml/badge.svg)](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/docs.yml)
[![CI](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/validate-content-sources.yml/badge.svg)](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/validate-content-sources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A practical guide covering Azure VM platform internals, operations, and troubleshooting — grounded in MS Learn documentation.

## What's Inside

| Section | Description | Status |
|---------|-------------|--------|
| [Start Here](https://yeongseon.github.io/azure-virtual-machine-practical-guide/start-here/) | VM overview, comparison with other compute options, and common usage scenarios | Comprehensive |
| [Platform](https://yeongseon.github.io/azure-virtual-machine-practical-guide/platform/) | Deep dive into Azure VM internals: compute models, lifecycle, disks, and networking | Comprehensive |
| [Best Practices](https://yeongseon.github.io/azure-virtual-machine-practical-guide/best-practices/) | Production-ready design for sizing, security, patching, and cost optimization | Comprehensive |
| [Operations](https://yeongseon.github.io/azure-virtual-machine-practical-guide/operations/) | Day-2 execution guide for managing disks, snapshots, patching, and monitoring | Comprehensive |
| [Tutorials](https://yeongseon.github.io/azure-virtual-machine-practical-guide/tutorials/) | Hands-on lab guides for high availability, disk encryption, and disaster recovery | Comprehensive |
| [Troubleshooting](https://yeongseon.github.io/azure-virtual-machine-practical-guide/troubleshooting/) | Diagnosis playbooks for boot failures, connectivity issues, and performance bottlenecks | Published |
| [Reference](https://yeongseon.github.io/azure-virtual-machine-practical-guide/reference/) | Quick-lookup for VM size families, disk types, and availability options | Comprehensive |

**Status legend**: **Lab-validated** = Comprehensive + reproducible labs prove the guidance · **Comprehensive** = Full section, MSLearn-verified, production-ready · **Published** = Core content in place, still expanding · **In progress** = Partial content, active development · **Planned** = Placeholder, content not yet started

## Tutorials

Explore practical lab guides to master Azure VM management:
- **HA Deployment**: Setting up highly available virtual machines
- **Security & Backup**: Implementing disk encryption and automated backups
- **Customization**: Automating configuration with custom script extensions
- **Access Control**: Managing secure access with Azure Bastion and JIT
- **Disaster Recovery**: Setting up VM replication with Azure Site Recovery (ASR)

## Quick Start

```bash
git clone https://github.com/yeongseon/azure-virtual-machine-practical-guide.git
cd azure-virtual-machine-practical-guide

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt

mkdocs serve
```

Visit `http://127.0.0.1:8000` to browse the documentation locally.

## Contributing

Contributions welcome! Please see our [Contributing Guide](https://yeongseon.github.io/azure-virtual-machine-practical-guide/contributing/) for:

- Repository structure and content organization
- Document templates and writing standards
- Local development setup and build validation
- Pull request process

## Related Projects

| Repository | Description |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines practical guide |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking practical guide |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage practical guide |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service practical guide |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions practical guide |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services practical guide |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps practical guide |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service (AKS) practical guide |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure Architecture practical guide |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring practical guide |

## Disclaimer

This is an independent community project. Not affiliated with or endorsed by Microsoft. Azure and Azure Virtual Machines are trademarks of Microsoft Corporation.

## License

[MIT](LICENSE)
