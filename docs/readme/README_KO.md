<div align="center">
  <img src="../../docs/logo.png" alt="VoiceStudio" width="88" />
  <h1>VoiceStudio</h1>
  <p>
    <a href="https://trendshift.io/repositories/28176?utm_source=repository-badge&amp;utm_medium=badge&amp;utm_campaign=badge-repository-28176" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/repositories/28176" alt="Trendshift의 VoiceStudio 인기 순위 배지" width="220" height="48" /></a>
  </p>
  <p><strong>내 기기에서 돌아가는 보이스 스튜디오: 646개 언어로 음성 복제, 보이스 디자인, 더빙, 받아쓰기, 음성 전사, 내레이션.</strong><br />
  내 컴퓨터와 휴대폰에서 실행됩니다. 계정도 API 키도 필요 없으며, 사용자가 허락하지 않는 한 어떤 데이터도 기기 밖으로 나가지 않습니다.</p>
  <p>
    <a href="https://voicestudio.sh/?utm_source=github&utm_medium=readme&utm_campaign=project">웹사이트</a> ·
    <a href="https://github.com/debpalash/VoiceStudio/releases/latest">내려받기</a> ·
    <a href="#시작하기">시작 안내</a> ·
    <a href="#문서">문서</a> ·
    <a href="https://discord.gg/bzQavDfVV9">Discord</a> ·
    <a href="../../README.md">English</a> ·
    <a href="README_CN.md">简体中文</a> ·
    <a href="README_JA.md">日本語</a> ·
    <a href="README_RU.md">Русский</a>
  </p>
  <p>
    <a href="https://github.com/debpalash/VoiceStudio/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/debpalash/VoiceStudio/ci.yml?branch=main" alt="CI 상태" /></a>
    <a href="https://github.com/debpalash/VoiceStudio/releases/latest"><img src="https://img.shields.io/github/v/release/debpalash/VoiceStudio" alt="최신 릴리스" /></a>
    <a href="../../LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-blue" alt="AGPL-3.0 라이선스" /></a>
    <a href="https://supermetry.com"><img src="https://app.supermetry.com/px/zfjiv7psp4ed.svg?c=VoiceStudio&style=stats" alt="조회수" /></a>
  </p>
  <p>
    <sub>전략 스폰서</sub><br />
    <a href="https://supermetry.com/?utm_source=voicestudio&utm_medium=sponsor&utm_campaign=strategic-sponsor&utm_content=readme-logo"><picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/sponsors/supermetry-dark.svg" /><img src="../../docs/sponsors/supermetry.svg" alt="Supermetry" height="48" /></picture></a>
  </p>
</div>

![앱 둘러보기: 음성 복제, 보이스 디자인, 더빙, 모델 관리](../../docs/media/electron/voicestudio.gif)

## 할 수 있는 일

| 만들기 | 제작하기 | 연결하기 |
| :--- | :--- | :--- |
| 목소리를 복제하거나 직접 디자인 | 타이밍을 맞춘 음성으로 영상 더빙 | 에이전트를 위한 로컬 API와 MCP |
| 플로팅 위젯으로 받아쓰기 | 스토리, 오디오북, 일괄 작업 | 재사용 가능한 레시피와 감시 폴더 |

기본 엔진인 **VoiceStudio**(k2-fsa/OmniVoice 기반)로 시작하거나, 모델 관리자에서 수십 가지 다른 엔진 중 하나를 고르세요. [기능 및 엔진 카탈로그](../../docs/feature-catalog.md)를 참고하세요.

<details>
<summary><strong>스크린샷</strong></summary>

<table>
  <tr>
    <td><img src="../../docs/media/electron/voice-cloning.png" alt="기본 제공 데모 음성이 열린 음성 복제 워크스페이스" width="100%" /></td>
    <td><img src="../../docs/media/electron/dubbing.png" alt="영상 더빙 워크스페이스" width="100%" /></td>
  </tr>
  <tr><td align="center">음성 복제</td><td align="center">영상 더빙</td></tr>
  <tr>
    <td><img src="../../docs/media/electron/voice-design.png" alt="보이스 디자인 워크스페이스에서 목소리를 묘사하기" width="100%" /></td>
    <td><img src="../../docs/media/electron/models.png" alt="로컬 음성 모델 설치 및 관리" width="100%" /></td>
  </tr>
  <tr><td align="center">보이스 디자인</td><td align="center">로컬 모델</td></tr>
</table>

</details>

## 지원 플랫폼

| 플랫폼 | 다운로드 | 가속 | 상태 |
| :--- | :--- | :--- | :--- |
| **macOS** (Apple Silicon) | `.dmg` · [가이드](../../docs/install/macos.md) | Metal (MPS) | 안정 |
| **Windows 10/11** (x64) | `.exe` · [가이드](../../docs/install/windows.md) | NVIDIA CUDA · [AMD ROCm (선택)](../../docs/install/windows-rocm.md) · CPU | 안정 |
| **Linux** (x64) | `.AppImage` · `.deb` · `snap` · [Nix](../../docs/install/nix.md) · [가이드](../../docs/install/linux.md) | NVIDIA CUDA · CPU | 안정 |
| **Docker** | [`ghcr.io/debpalash/voicestudio`](../../docs/install/docker.md) | NVIDIA CUDA · AMD ROCm | 안정 |
| **Android** 10+ | `.apk` · [가이드](../../docs/mobile.md#install) | 기기에서 실행, 오프라인 지원 | 프리뷰 |
| **iPhone / iPad** (iOS 17+) | `.ipa` (사이드로드) · [가이드](../../docs/mobile.md#install) | 기기에서 실행, 오프라인 지원 | 프리뷰 |
| **Windows on ARM** | `.exe` · [가이드](../../docs/install/windows.md) | CPU (x64 백엔드를 에뮬레이션으로 실행) | 실험적 |
| **Intel Mac** | `.dmg` · [이유](../../docs/install/macos.md) | 앱 UI만 지원, 원격 백엔드에 연결 | 제한적 |

데스크톱과 휴대폰 설치 파일은 [최신 릴리스](https://github.com/debpalash/VoiceStudio/releases/latest)에 있고, Docker 이미지는 GHCR에서 받을 수 있습니다. GPU가 없나요? CPU만으로도 모든 기능을 쓸 수 있으며, 속도만 느립니다. 선택 기능인 네이티브 GGUF 엔진은 AMD GPU를 포함해 Vulkan도 사용할 수 있습니다([OmniVoice](../../docs/engines/omnivoice-gguf.md#vulkan-acceleration), [CosyVoice](../../docs/engines/cosyvoice-gguf.md)). 엔진과 하드웨어별 속도는 [성능](../../docs/performance.md) 문서를 참고하세요.

## 시작하기

**macOS / Linux**

```sh
curl -fsSL https://voicestudio.sh/install | sh
```

**Windows** (PowerShell)

```powershell
irm https://voicestudio.sh/install.ps1 | iex
```

위 표에서 설치 파일을 내려받아도 됩니다. 그런 다음 **음성 복제**를 열고, 목소리를 고르거나 깨끗한 참조 녹음을 추가한 뒤 텍스트를 입력하고 생성하세요. 모델을 내려받기 전에는 항상 먼저 확인을 요청합니다.

> [!NOTE]
> macOS에서 "VoiceStudio가 손상되었기 때문에 열 수 없습니다"라는 메시지는 Gatekeeper가 앱을 차단했다는 뜻이지, 다운로드한 파일이 손상되었다는 뜻이 아닙니다. [Gatekeeper 해결 방법](../../docs/install/macos.md#gatekeeper-quarantine)을 참고하세요.

<details>
<summary><strong>다른 설치 방법</strong>: 특정 버전, 최신 main, 제거, 소스에서 설치, 코딩 에이전트로 설치</summary>

```sh
curl -fsSL https://voicestudio.sh/install | sh -s -- --version X.Y.Z   # 특정 릴리스
curl -fsSL https://voicestudio.sh/install | sh -s -- --main            # 최신 main 빌드
curl -fsSL https://voicestudio.sh/install | sh -s -- --uninstall       # 데이터는 남기고 앱만 제거
```

`voicestudio.sh`에 접속할 수 없다면 저장소에서 스크립트를 바로 실행하세요:
`curl -fsSL https://raw.githubusercontent.com/debpalash/VoiceStudio/main/scripts/install.sh | sh`.
요구 사항과 동작: [설치 스크립트 가이드](../../docs/install/script.md).

**소스에서 설치**

```bash
git clone https://github.com/debpalash/VoiceStudio.git
cd VoiceStudio
bun run dev
```

[Electron 설정](../../electron/README.md)을 참고하세요.

**코딩 에이전트로 설치** (Claude Code, Codex, Cursor 등): 다음 내용을 붙여 넣으세요.

```text
Install the VoiceStudio app on this device and verify it works, following
https://github.com/debpalash/VoiceStudio/blob/main/docs/install/agent.md
```

0.5.3 이하 버전(Tauri 앱)에서 업그레이드하나요? [새 앱을 별도로 설치](../../docs/electron-migration.md)하세요.

</details>

## 문서

| 필요한 것 | 여기서 시작 |
|---|---|
| 설치 도움말 | [문제 해결](../../docs/install/troubleshooting.md) · [모델 다운로드](../../docs/downloading-models.md) |
| 가이드 | [다중 화자 더빙](../../docs/dubbing/multi-speaker-guide.md) · [표현력 있는 음성](../../docs/expressive-speech.md) · [더빙 내보내기](../../docs/dubbing/export.md) |
| 모델과 음질 | [엔진 가이드](../../docs/engines/README.md) · [whisper.cpp ASR](../../docs/engines/whisper-cpp.md) · [벤치마크](../../docs/benchmarks.md) |
| 연동 | [로컬 API](../../docs/speech-platform.md) · [MCP](../../docs/mcp.md) · [예제](../../examples/README.md) |
| 휴대폰 앱 | [iOS 및 Android](../../docs/mobile.md) |
| 개발 | [기여하기](../../.github/CONTRIBUTING.md) (첫 PR 전에 [CLA 서명](../../.github/CONTRIBUTING.md#contribution-licensing) 필요) · [변경 기록](../../CHANGELOG.md) |

에이전트 스킬: `npx skills add debpalash/VoiceStudio` (오디오 작업에는 **voicestudio**, 저장소 관리에는 **voicestudio-maintainer**).

## 후원사

VoiceStudio는 무료이며, 뒤에 유료 클라우드도 없습니다. 후원사 덕분에 개발이 계속됩니다. 후원금은 메인테이너의 작업 시간, 테스트 하드웨어, 코드 서명과 릴리스 인프라에 쓰입니다.

<p>
    <a href="https://supermetry.com/?utm_source=voicestudio&utm_medium=sponsor&utm_campaign=strategic-sponsor&utm_content=readme-logo"><picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/sponsors/supermetry-dark.svg" /><img src="../../docs/sponsors/supermetry.svg" alt="Supermetry" height="48" /></picture></a>
</p>

**여기에 귀사의 로고를 올려 보세요.** Development, Company, Strategic 후원 자리는 월 100달러부터 열려 있으며, Community 후원사(25달러)는 이름과 링크가 실립니다. 후원으로 얻는 것은 기능이 아니라 크레딧입니다.

<a href="https://github.com/sponsors/debpalash"><img src="https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors&logoColor=white" alt="GitHub Sponsors로 후원하기" /></a>
[Ko-fi](https://ko-fi.com/debpalash) · [PayPal](https://paypal.me/palashCoder) · [등급과 혜택](../../SPONSORS.md) · [로고 게재 신청](https://github.com/debpalash/VoiceStudio/issues/new?template=sponsor.yml)

## 팀

### 핵심 팀

<table>
<tr>
<td align="center" width="200"><a href="https://github.com/debpalash"><img src="https://github.com/debpalash.png?size=160" width="80" height="80" alt="Palash Debnath"></a><br><b>Palash Debnath</b><br><sub>창시자 · 핵심 팀</sub><br><sub><a href="https://palash.dev">palash.dev</a> · <a href="https://github.com/debpalash">GitHub</a> · <a href="https://x.com/idebpalash">X</a></sub></td>
<td align="center" width="200"><a href="https://github.com/velixio"><img src="https://github.com/velixio.png?size=160" width="80" height="80" alt="Shimul Debnath"></a><br><b>Shimul Debnath</b><br><sub>핵심 팀</sub><br><sub><a href="https://shimul.me">shimul.me</a> · <a href="https://github.com/velixio">GitHub</a> · <a href="https://x.com/shimuldn">X</a></sub></td>
</tr>
</table>

### 기여자

<a href="https://github.com/kevin9327"><img src="https://github.com/kevin9327.png?size=96" width="44" height="44" alt="@kevin9327" title="@kevin9327"></a> <a href="https://github.com/jaketame"><img src="https://github.com/jaketame.png?size=96" width="44" height="44" alt="@jaketame" title="@jaketame"></a> <a href="https://github.com/psiberfunk"><img src="https://github.com/psiberfunk.png?size=96" width="44" height="44" alt="@psiberfunk" title="@psiberfunk"></a> <a href="https://github.com/rudycelekli"><img src="https://github.com/rudycelekli.png?size=96" width="44" height="44" alt="@rudycelekli" title="@rudycelekli"></a> <a href="https://github.com/paoloantinori"><img src="https://github.com/paoloantinori.png?size=96" width="44" height="44" alt="@paoloantinori" title="@paoloantinori"></a> <a href="https://github.com/Chang-Jin-Lee"><img src="https://github.com/Chang-Jin-Lee.png?size=96" width="44" height="44" alt="@Chang-Jin-Lee" title="@Chang-Jin-Lee"></a> <a href="https://github.com/swadhinbiswas"><img src="https://github.com/swadhinbiswas.png?size=96" width="44" height="44" alt="@swadhinbiswas" title="@swadhinbiswas"></a> <a href="https://github.com/BichengWang"><img src="https://github.com/BichengWang.png?size=96" width="44" height="44" alt="@BichengWang" title="@BichengWang"></a> <a href="https://github.com/nirmalchatur"><img src="https://github.com/nirmalchatur.png?size=96" width="44" height="44" alt="@nirmalchatur" title="@nirmalchatur"></a> <a href="https://github.com/Shivendra-Coherent"><img src="https://github.com/Shivendra-Coherent.png?size=96" width="44" height="44" alt="@Shivendra-Coherent" title="@Shivendra-Coherent"></a> <a href="https://github.com/marreiradigital"><img src="https://github.com/marreiradigital.png?size=96" width="44" height="44" alt="@marreiradigital" title="@marreiradigital"></a> <a href="https://github.com/nvtoan0201-swe"><img src="https://github.com/nvtoan0201-swe.png?size=96" width="44" height="44" alt="@nvtoan0201-swe" title="@nvtoan0201-swe"></a>

코드, 버그 제보, 번역, 아이디어를 보내 주신 모든 분께 감사드립니다. [전체 기여자](https://github.com/debpalash/VoiceStudio/graphs/contributors) · [기여하기](../../.github/CONTRIBUTING.md)

## 라이선스와 책임 있는 사용

앱에는 [AGPL-3.0](../../LICENSE)이 적용되며, 그 조건에 따른 상업적 사용도 가능합니다. 모델 가중치, 음성, 생성 결과물에는 각각의 라이선스가 있으며, 모델 관리자에서 모델별로 확인할 수 있습니다([목록](../../docs/licensing/model-inventory.md)). 목소리는 반드시 그 주인의 허락을 받은 경우에만 복제하세요. 자세한 내용: [LICENSE-NOTICE.md](../../LICENSE-NOTICE.md).
