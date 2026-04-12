# Azure Virtual Machine 实操指南

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

基于 MS Learn 文档的 Azure VM 平台内部、运营和故障排除实操指南。

## 范围

- ✅ 包含: Azure VM 平台概念、运营、安全、监控、故障排除
- ❌ 不包含: 操作系统或应用程序安装教程

## 主要内容

| 章节 | 目的 |
|---------|---------|
| 从这里开始 (Start Here) | VM 概述、与其他计算选项的比较、学习路径 |
| 平台 (Platform) | Azure VM 工作原理、组件、生命周期 |
| 最佳实践 (Best Practices) | 面向生产的设计和运营指南 |
| 运营 (Operations) | 分步运营流程和配置 |
| 故障排除 (Troubleshooting) | 基于症状的诊断和解决 |
| 参考 (Reference) | 快速查询摘要表 |

## 内容来源

所有内容基于官方 [Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/) 文档。

## 本地构建

```bash
pip install mkdocs-material pymdown-extensions
mkdocs build --strict
mkdocs serve
```

## 相关项目

| 仓库 | 描述 |
|---|---|
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 实操指南 |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 实操指南 |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 实操指南 |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 实操指南 |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 实操指南 |
| [azure-aks-practical-guide](https://github.com/yeongseon/azure-aks-practical-guide) | Azure Kubernetes Service 实操指南 |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 实操指南 |
