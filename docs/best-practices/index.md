# Best Practices

프로덕션 환경에서의 권장 설계와 운영 판단 기준을 다루는 섹션입니다. 이론이 아닌 **실전 판단 기준** 중심입니다.

## Documents

| Document | What You'll Learn |
|----------|------------------|
| [Production Baseline](production-baseline.md) | 프로덕션 VM 최소 기준 체크리스트 |
| [Sizing and Image Selection](sizing-and-image-selection.md) | 워크로드 기반 sizing, marketplace vs custom image |
| [Networking](networking-best-practices.md) | Public IP 최소화, Bastion, NSG 최소 권한 |
| [Disk and Storage](disk-and-storage-best-practices.md) | OS/data 분리, tier 선택, temp disk 주의 |
| [Security](security-best-practices.md) | Least privilege, managed identity, JIT access |
| [Patching and Maintenance](patching-and-maintenance-best-practices.md) | Patch window, 테스트/운영 분리, maintenance event |
| [Monitoring](monitoring-best-practices.md) | Guest + Azure metrics, boot diagnostics, alerting |
| [Backup and DR](backup-and-dr-best-practices.md) | Backup policy, restore drill, RPO/RTO |
| [Cost Optimization](cost-optimization-best-practices.md) | Deallocate, reserved instances, 불필요 리소스 정리 |
| [Common Anti-Patterns](common-anti-patterns.md) | 흔한 실수와 피해야 할 패턴 |
