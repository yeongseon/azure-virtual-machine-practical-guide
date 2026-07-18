# Azure Virtual Machine 실무 가이드

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

📘 문서 사이트: <https://yeongseon.github.io/azure-virtual-machine-practical-guide/>

[![Docs](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/docs.yml/badge.svg)](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/docs.yml)
[![CI](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/validate-content-sources.yml/badge.svg)](https://github.com/yeongseon/azure-virtual-machine-practical-guide/actions/workflows/validate-content-sources.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

MS Learn 문서를 기반으로 Azure VM 플랫폼 내부, 운영 및 트러블슈팅을 다루는 실무 가이드입니다.

## 주요 내용

| 섹션 | 설명 | 상태 |
|---------|-------------|--------|
| [시작하기](https://yeongseon.github.io/azure-virtual-machine-practical-guide/start-here/) | VM 개요, 다른 컴퓨팅 옵션과의 비교 및 일반적인 사용 시나리오 | Comprehensive |
| [플랫폼](https://yeongseon.github.io/azure-virtual-machine-practical-guide/platform/) | Azure VM 내부 심층 분석: 컴퓨팅 모델, 수명 주기, 디스크 및 네트워킹 | Comprehensive |
| [베스트 프랙티스](https://yeongseon.github.io/azure-virtual-machine-practical-guide/best-practices/) | 사이징, 보안, 패치 및 비용 최적화를 위한 운영 환경용 설계 | Comprehensive |
| [운영](https://yeongseon.github.io/azure-virtual-machine-practical-guide/operations/) | 디스크, 스냅샷, 패치 및 모니터링 관리를 위한 운영 가이드 | Comprehensive |
| [튜토리얼](https://yeongseon.github.io/azure-virtual-machine-practical-guide/tutorials/) | 고가용성, 디스크 암호화 및 재해 복구를 위한 핸즈온 랩 가이드 | Comprehensive |
| [트러블슈팅](https://yeongseon.github.io/azure-virtual-machine-practical-guide/troubleshooting/) | 부팅 실패, 연결 문제 및 성능 병목 현상에 대한 진단 플레이북 | Published |
| [참조](https://yeongseon.github.io/azure-virtual-machine-practical-guide/reference/) | VM 크기 제품군, 디스크 유형 및 가용성 옵션 빠른 조회 | Comprehensive |

**상태 범례**: **Lab-validated** = 포괄적인 지침과 함께 이를 증명하는 재현 가능한 랩 제공 · **Comprehensive** = Microsoft Learn 기반의 검증을 마친 운영 환경에 즉시 적용 가능한 완성된 섹션 · **Published** = 핵심 콘텐츠는 포함되어 있으나 계속 확장 중 · **In progress** = 일부 콘텐츠 포함, 현재 활발히 작성 중 · **Planned** = 플레이스홀더 상태, 아직 콘텐츠 작성이 시작되지 않음

## 튜토리얼

Azure VM 관리를 마스터하기 위한 실무 랩 가이드를 살펴보세요:
- **고가용성 배포 (HA Deployment)**: 고가용성 가상 머신 설정
- **보안 및 백업 (Security & Backup)**: 디스크 암호화 및 자동 백업 구현
- **사용자 지정 (Customization)**: 사용자 지정 스크립트 확장을 통한 구성 자동화
- **액세스 제어 (Access Control)**: Azure Bastion 및 JIT를 통한 보안 액세스 관리
- **재해 복구 (Disaster Recovery)**: Azure Site Recovery (ASR)를 사용한 VM 복제 설정

## 빠른 시작

```bash
git clone https://github.com/yeongseon/azure-virtual-machine-practical-guide.git
cd azure-virtual-machine-practical-guide

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt

mkdocs serve
```

로컬에서 `http://127.0.0.1:8000`에 접속하여 문서를 확인하세요.

## 기여하기

기여는 언제나 환영합니다! 다음 사항은 [기여 가이드](https://yeongseon.github.io/azure-virtual-machine-practical-guide/contributing/)를 참조하세요:

- 저장소 구조 및 콘텐츠 구성
- 문서 템플릿 및 작성 표준
- 로컬 개발 환경 설정 및 빌드 검증
- 풀 리퀘스트(PR) 프로세스

## 관련 프로젝트

| 저장소 | 설명 |
|---|---|
| [azure-virtual-machine-practical-guide](https://github.com/yeongseon/azure-virtual-machine-practical-guide) | Azure Virtual Machines 실무 가이드 |
| [azure-networking-practical-guide](https://github.com/yeongseon/azure-networking-practical-guide) | Azure Networking 실무 가이드 |
| [azure-storage-practical-guide](https://github.com/yeongseon/azure-storage-practical-guide) | Azure Storage 실무 가이드 |
| [azure-app-service-practical-guide](https://github.com/yeongseon/azure-app-service-practical-guide) | Azure App Service 실무 가이드 |
| [azure-functions-practical-guide](https://github.com/yeongseon/azure-functions-practical-guide) | Azure Functions 실무 가이드 |
| [azure-communication-services-practical-guide](https://github.com/yeongseon/azure-communication-services-practical-guide) | Azure Communication Services 실무 가이드 |
| [azure-container-apps-practical-guide](https://github.com/yeongseon/azure-container-apps-practical-guide) | Azure Container Apps 실무 가이드 |
| [azure-kubernetes-service-practical-guide](https://github.com/yeongseon/azure-kubernetes-service-practical-guide) | Azure Kubernetes Service 실무 가이드 |
| [azure-architecture-practical-guide](https://github.com/yeongseon/azure-architecture-practical-guide) | Azure Architecture 실무 가이드 |
| [azure-monitoring-practical-guide](https://github.com/yeongseon/azure-monitoring-practical-guide) | Azure Monitoring 실무 가이드 |

## 면책 조항

이 프로젝트는 독립적인 커뮤니티 프로젝트입니다. Microsoft와 제휴하거나 보증을 받지 않았습니다. Azure 및 Azure Virtual Machines는 Microsoft Corporation의 상표입니다.

## 라이선스

[MIT](LICENSE)
