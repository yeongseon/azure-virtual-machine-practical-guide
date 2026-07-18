# Azure Virtual Machine 实操指南

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

📘 文档站点: <https://yeongseon.github.io/azure-virtual-machine-practical-guide/>

[![Docs](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/docs.yml/badge.svg)](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/docs.yml)
[![CI](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/validate-content-sources.yml/badge.svg)](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/validate-content-sources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

基于 MS Learn 文档的 Azure VM 平台内部、运营和故障排除实操指南。

## 内容概览

| 章节 | 描述 | 状态 |
|---------|-------------|--------|
| [从这里开始](https://yeongseon.github.io/azure-virtual-machine-practical-guide/start-here/) | VM 概述、与其他计算选项的比较以及常见使用场景 | Comprehensive |
| [平台](https://yeongseon.github.io/azure-virtual-machine-practical-guide/platform/) | 深入了解 Azure VM 内部：计算模型、生命周期、磁盘和网络 | Comprehensive |
| [最佳实践](https://yeongseon.github.io/azure-virtual-machine-practical-guide/best-practices/) | 针对尺寸选择、安全、补丁和成本优化的生产级设计 | Comprehensive |
| [运营](https://yeongseon.github.io/azure-virtual-machine-practical-guide/operations/) | 管理磁盘、快照、补丁和监控的日常运营指南 | Comprehensive |
| [教程](https://yeongseon.github.io/azure-virtual-machine-practical-guide/tutorials/) | 高可用性、磁盘加密和灾难恢复的动手实验指南 | Comprehensive |
| [故障排除](https://yeongseon.github.io/azure-virtual-machine-practical-guide/troubleshooting/) | 针对启动失败、连接问题和性能瓶颈的诊断实战手册 | Published |
| [参考](https://yeongseon.github.io/azure-virtual-machine-practical-guide/reference/) | VM 尺寸系列、磁盘类型和可用性选项的快速查询 | Comprehensive |

**状态说明**：**实验室验证** = 全面内容 + 可重现的实验室证明了该指导 · **全面** = 完整章节，经 MSLearn 验证，可用于生产环境 · **已发布** = 核心内容已到位，仍处于扩展中 · **进行中** = 部分内容，处于活跃开发中 · **已计划** = 占位符，内容尚未开始

## 教程

探索掌握 Azure VM 管理的实操实验指南：
- **高可用性部署 (HA Deployment)**：设置高可用性虚拟机
- **安全与备份 (Security & Backup)**：实现磁盘加密和自动化备份
- **自定义 (Customization)**：使用自定义脚本扩展自动化配置
- **访问控制 (Access Control)**：通过 Azure Bastion 和 JIT 管理安全访问
- **灾难恢复 (Disaster Recovery)**：使用 Azure Site Recovery (ASR) 设置 VM 复制

## 快速入门

```bash
git clone https://github.com/yeongseon/azure-virtual-machine-practical-guide.git
cd azure-virtual-machine-practical-guide

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt

mkdocs serve
```

访问 `http://127.0.0.1:8000` 在本地浏览文档。

## 参与贡献

欢迎贡献！请参阅我们的 [贡献指南](https://yeongseon.github.io/azure-virtual-machine-practical-guide/contributing/) 了解以下内容：

- 仓库结构和内容组织
- 文档模板和写作标准
- 本地开发设置和构建验证
- 拉取请求 (PR) 流程

## 相关项目

| 仓库 | 描述 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 实操指南 |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 实操指南 |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 实操指南 |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 实操指南 |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 实操指南 |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services 实操指南 |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 实操指南 |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service 实操指南 |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure Architecture 实操指南 |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 实操指南 |

## 免责声明

这是一个独立的社区项目。与 Microsoft 无关，也不受其认可。Azure 和 Azure Virtual Machines 是 Microsoft Corporation 的商标。

## 许可证

[MIT](LICENSE)
