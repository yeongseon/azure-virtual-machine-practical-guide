# Azure Virtual Machine 実務ガイド

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

📘 ドキュメントサイト: <https://yeongseon.github.io/azure-virtual-machine-practical-guide/>

[![Docs](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/docs.yml/badge.svg)](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/docs.yml)
[![CI](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/validate-content-sources.yml/badge.svg)](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/validate-content-sources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

MS Learn ドキュメントに基づいた、Azure VM のプラットフォーム内部、運用、およびトラブルシューティングに関する実務ガイドです。

## 主な内容

| セクション | 説明 | ステータス |
|---------|-------------|--------|
| [ここから開始](https://yeongseon.github.io/azure-virtual-machine-practical-guide/start-here/) | VM の概要、他のコンピューティングオプションとの比較、および一般的な使用シナリオ | Comprehensive |
| [プラットフォーム](https://yeongseon.github.io/azure-virtual-machine-practical-guide/platform/) | Azure VM 内部の深掘り：コンピューティングモデル、ライフサイクル、ディスク、およびネットワーク | Comprehensive |
| [ベストプラクティス](https://yeongseon.github.io/azure-virtual-machine-practical-guide/best-practices/) | サイジング、セキュリティ、パッチ適用、およびコスト最適化のための本番対応設計 | Comprehensive |
| [運用](https://yeongseon.github.io/azure-virtual-machine-practical-guide/operations/) | ディスク, スナップショット, パッチ適用, および監視を管理するための運用ガイド | Comprehensive |
| [チュートリアル](https://yeongseon.github.io/azure-virtual-machine-practical-guide/tutorials/) | 高可用性、ディスク暗号化、および災害復旧のためのハンズオンラボガイド | Comprehensive |
| [トラブルシューティング](https://yeongseon.github.io/azure-virtual-machine-practical-guide/troubleshooting/) | 起動の失敗、接続の問題、および性能のボトルネックに関する診断プレイブック | Published |
| [リファレンス](https://yeongseon.github.io/azure-virtual-machine-practical-guide/reference/) | VM サイズファミリー、ディスクの種類、および可用性オプションのクイックルックアップ | Comprehensive |

**ステータスの凡例**: **Lab-validated** = 包括的 + 再現可能なラボでガイダンスを証明済み · **Comprehensive** = セクション全体が完成し、MSLearn で検証済みの本番対応レベル · **公開済み** = 主要なコンテンツは揃っているが、現在も拡張中 · **進行中** = 部分的なコンテンツ、アクティブに開発中 · **計画中** = プレースホルダー、コンテンツは未着手

## チュートリアル

Azure VM 管理をマスターするための実務ラボガイドを探索してください：
- **高可用性デプロイ (HA Deployment)**: 高可用な仮想マシンのセットアップ
- **セキュリティとバックアップ (Security & Backup)**: ディスク暗号化と自動バックアップの実装
- **カスタマイズ (Customization)**: カスタムスクリプト拡張機能による構成の自動化
- **アクセス制御 (Access Control)**: Azure Bastion と JIT による安全なアクセス管理
- **災害復旧 (Disaster Recovery)**: Azure Site Recovery (ASR) による VM レプリケーションのセットアップ

## クイックスタート

```bash
git clone https://github.com/yeongseon/azure-virtual-machine-practical-guide.git
cd azure-virtual-machine-practical-guide

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt

mkdocs serve
```

`http://127.0.0.1:8000` にアクセスして、ローカルでドキュメントを閲覧してください。

## 貢献

貢献を歓迎します！以下の詳細については、[貢献ガイド](https://yeongseon.github.io/azure-virtual-machine-practical-guide/contributing/) を参照してください：

- リポジトリの構造とコンテンツの構成
- ドキュメントテンプレートと執筆基準
- ローカル開発環境のセットアップとビルド検証
- プルリクエストのプロセス

## 関連プロジェクト

| リポジトリ | 説明 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 実務ガイド |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 実務ガイド |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 実務ガイド |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 実務ガイド |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 実務ガイド |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services 実務ガイド |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 実務ガイド |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service 実務ガイド |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure アーキテクチャ実務ガイド |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure モニタリング実務ガイド |

## 免責事項

これは独立したコミュニティプロジェクトです。Microsoft との提携や承認を受けているものではありません。Azure および Azure Virtual Machines は Microsoft Corporation の商標です。

## ライセンス

[MIT](LICENSE)
