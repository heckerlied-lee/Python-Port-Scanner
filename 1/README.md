# ⚡ High-Speed Multi-Threaded Port Scanner

파이썬(Python)의 `socket`과 `threading` 라이브러리를 활용하여 제작한 **초고속 멀티스레드 포트 스캐너**입니다. 
로컬 환경(127.0.0.1)의 1번부터 65535번 포트를 전수조사하여 열려 있는 시스템 관문을 탐지합니다.

## ✨ 핵심 기능 (Features)
- **Multi-threading 지원:** 500개의 스레드를 동시에 가동하여 65,535개 전체 포트를 수초 내에 스캔 완료
- **동적 타임아웃 최적화:** 로컬 환경에 맞춘 0.1초 타임아웃 설정으로 누수 없는 정확한 탐지
- **직관적인 UI:** [OPEN] 상태의 포트를 실시간으로 화면에 출력

## 🖥️ 실행 화면 예시 (Usage Example)
```text
==================================================
포트조사 가동
대상 IP : 127.0.0.1
시작 시간: 2026-10-12 21:20:00
==================================================
🔍 127.0.0.1의 모든 포트를 검사 중입니다. 잠시만 기다려주세요...

[OPEN] 포트   135번이 열려 있습니다!
[OPEN] 포트   445번이 열려 있습니다!
[OPEN] 포트  8080번이 열려 있습니다!

==================================================
조사완료.
==================================================
```

## ⚠️ 경고 및 면책 조항 (Disclaimer)

### 🇰🇷 국문 (Korean)
- 본 툴은 **교육 및 개인 인프라 보안 진단 목적**으로만 제작되었습니다.
- 허가받지 않은 타인의 자산(서버, IP 등)을 대상으로 스캔을 수행하는 행위는 **불법**이며, 모든 법적 책임은 실행자에게 있습니다.
- 코드 내에 `target_host = "127.0.0.1"`로 안전 구역이 고정되어 있습니다.

### 🇺🇸 영문 (English)
- This tool is developed strictly for **educational purposes and authorized security assessment** of personal infrastructure.
- Performing port scanning against unauthorized external assets, servers, or IP addresses is strictly **illegal** and violates computer crime laws. The user assumes all legal liabilities for any misuse of this program.
- The destination host is safely hardcoded to `127.0.0.1` (localhost) inside the script to prevent unauthorized activities.
