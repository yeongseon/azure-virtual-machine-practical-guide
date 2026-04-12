# Azure Virtual Machine 実務ガイド

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

MS Learn ドキュメントに基づいた、Azure VM のプラットフォーム内部、運用、およびトラブルシューティングに関する実務ガイドです。

## スコープ

- ✅ 含まれるもの: Azure VM プラットフォームの概念、運用、セキュリティ、モニタリング、トラブルシューティング
- ❌ 含まれないもの: OS 固有またはアプリケーションインストールのチュートリアル

## 主な内容

| セクション | 目的 |
|---------|---------|
| ここから開始 (Start Here) | VM 概要、他のコンピューティングオプションとの比較、学習パス |
| プラットフォーム (Platform) | Azure VM の仕組み、コンポーネント、ライフサイクル |
| ベストプラクティス (Best Practices) | 本番環境に対応した設計と運用ガイドライン |
| 運用 (Operations) | ステップバイステップの運用手順と構成 |
| トラブルシューティング (Troubleshooting) | 症状ベースの診断と解決 |
| リファレンス (Reference) | クイックルックアップサマリーテーブル |

## コンテンツソース

すべてのコンテンツは、公式 [Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/) ドキュメントに基づいています。

## ローカルビルド

```bash
pip install mkdocs-material pymdown-extensions
mkdocs build --strict
mkdocs serve
```

## 関連プロジェクト

| リポジトリ | 説明 |
|---|---|
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 実務ガイド |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 実務ガイド |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 実務ガイド |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 実務ガイド |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 実務ガイド |
| [azure-aks-practical-guide](https://github.com/yeongseon/azure-aks-practical-guide) | Azure Kubernetes Service 実務ガイド |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 実務ガイド |
