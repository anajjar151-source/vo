<div align="center">
  <img src="../../docs/logo.png" alt="VoiceStudio 标志" width="88" />
  <h1>VoiceStudio</h1>
  <p>
    <a href="https://trendshift.io/repositories/28176?utm_source=repository-badge&amp;utm_medium=badge&amp;utm_campaign=badge-repository-28176" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/repositories/28176" alt="VoiceStudio 在 Trendshift 上的热度排名徽章" width="220" height="48" /></a>
  </p>
  <p><strong>本地语音工作室：支持 646 种语言的声音克隆、声音设计、配音、听写、转录与有声朗读。</strong><br />
  在你自己的电脑和手机上运行。无需账号，无需 API 密钥；未经你同意，任何数据都不会离开设备。</p>
  <p>
    <a href="https://voicestudio.sh/?utm_source=github&utm_medium=readme&utm_campaign=project">官网</a> ·
    <a href="https://github.com/debpalash/VoiceStudio/releases/latest">下载</a> ·
    <a href="#开始使用">快速上手</a> ·
    <a href="#文档">文档</a> ·
    <a href="https://discord.gg/bzQavDfVV9">Discord</a> ·
    <a href="../../README.md">English</a> ·
    <a href="README_JA.md">日本語</a> ·
    <a href="README_KO.md">한국어</a> ·
    <a href="README_RU.md">Русский</a>
  </p>
  <p>
    <a href="https://github.com/debpalash/VoiceStudio/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/debpalash/VoiceStudio/ci.yml?branch=main" alt="CI 构建状态" /></a>
    <a href="https://github.com/debpalash/VoiceStudio/releases/latest"><img src="https://img.shields.io/github/v/release/debpalash/VoiceStudio" alt="最新版本" /></a>
    <a href="../../LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-blue" alt="AGPL-3.0 许可证" /></a>
    <a href="https://supermetry.com"><img src="https://app.supermetry.com/px/zfjiv7psp4ed.svg?c=VoiceStudio&style=stats" alt="访问量" /></a>
  </p>
  <p>
    <sub>战略赞助商</sub><br />
    <a href="https://supermetry.com/?utm_source=voicestudio&utm_medium=sponsor&utm_campaign=strategic-sponsor&utm_content=readme-logo"><picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/sponsors/supermetry-dark.svg" /><img src="../../docs/sponsors/supermetry.svg" alt="Supermetry" height="48" /></picture></a>
  </p>
</div>

![应用导览：声音克隆、声音设计、配音和模型管理](../../docs/media/electron/voicestudio.gif)

## 你可以做什么

| 创作 | 制作 | 连接 |
| :--- | :--- | :--- |
| 克隆声音或设计专属声音 | 用精准对时的语音为视频配音 | 面向智能体的本地 API 与 MCP |
| 使用悬浮窗口听写 | 故事、有声书与批量任务 | 可复用的配方与监视文件夹 |

从默认的 **VoiceStudio**（由 k2-fsa/OmniVoice 驱动）开始，或在模型管理器中从数十种其他引擎中挑选。参见[功能与引擎目录](../../docs/feature-catalog.md)。

<details>
<summary><strong>截图</strong></summary>

<table>
  <tr>
    <td><img src="../../docs/media/electron/voice-cloning.png" alt="使用内置演示声音的声音克隆工作区" width="100%" /></td>
    <td><img src="../../docs/media/electron/dubbing.png" alt="视频配音工作区" width="100%" /></td>
  </tr>
  <tr><td align="center">声音克隆</td><td align="center">视频配音</td></tr>
  <tr>
    <td><img src="../../docs/media/electron/voice-design.png" alt="在声音设计工作区中描述声音" width="100%" /></td>
    <td><img src="../../docs/media/electron/models.png" alt="安装和管理本地语音模型" width="100%" /></td>
  </tr>
  <tr><td align="center">声音设计</td><td align="center">本地模型</td></tr>
</table>

</details>

## 支持平台

| 平台 | 下载 | 加速 | 状态 |
| :--- | :--- | :--- | :--- |
| **macOS**（Apple Silicon） | `.dmg` · [指南](../../docs/install/macos.md) | Metal（MPS） | 稳定 |
| **Windows 10/11**（x64） | `.exe` · [指南](../../docs/install/windows.md) | NVIDIA CUDA · [AMD ROCm（可选）](../../docs/install/windows-rocm.md) · CPU | 稳定 |
| **Linux**（x64） | `.AppImage` · `.deb` · `snap` · [Nix](../../docs/install/nix.md) · [指南](../../docs/install/linux.md) | NVIDIA CUDA · CPU | 稳定 |
| **Docker** | [`ghcr.io/debpalash/voicestudio`](../../docs/install/docker.md) | NVIDIA CUDA · AMD ROCm | 稳定 |
| **Android** 10+ | `.apk` · [指南](../../docs/mobile.md#install) | 设备端运行，可离线 | 预览版 |
| **iPhone / iPad**（iOS 17+） | `.ipa`（侧载） · [指南](../../docs/mobile.md#install) | 设备端运行，可离线 | 预览版 |
| **Windows on ARM** | `.exe` · [指南](../../docs/install/windows.md) | CPU（x64 后端在模拟层中运行） | 实验性 |
| **Intel Mac** | `.dmg` · [原因](../../docs/install/macos.md) | 仅应用界面，需连接远程后端 | 受限 |

桌面端和手机安装包都在[最新发行版](https://github.com/debpalash/VoiceStudio/releases/latest)中，Docker 镜像则发布在 GHCR。没有 GPU？应用在 CPU 上也能完整使用，只是速度较慢。原生 GGUF 引擎还能通过 Vulkan 使用 AMD、Intel 和 NVIDIA GPU；在 Windows 和 Linux 上，OmniVoice GGUF 会自动选择 GPU 和模型量化（[OmniVoice](../../docs/engines/omnivoice-gguf.md#vulkan-acceleration)、[CosyVoice](../../docs/engines/cosyvoice-gguf.md)）。各引擎在不同硬件上的速度：[性能说明](../../docs/performance.md)。

## 开始使用

**macOS / Linux**

```sh
curl -fsSL https://voicestudio.sh/install | sh
```

**Windows**（PowerShell）

```powershell
irm https://voicestudio.sh/install.ps1 | iex
```

也可以从上表下载安装包。然后打开**声音克隆**，选择声音或添加一段清晰的参考录音，输入文本并生成。下载任何模型之前，应用都会先征求你的同意。

> [!NOTE]
> 在 macOS 上看到“VoiceStudio 已损坏，无法打开”，是 Gatekeeper 拦截了应用，并不是下载文件损坏。参见 [Gatekeeper 修复方法](../../docs/install/macos.md#gatekeeper-quarantine)。

<details>
<summary><strong>更多安装方式</strong>：指定版本、当前 main、卸载、从源码安装、通过编码智能体安装</summary>

```sh
curl -fsSL https://voicestudio.sh/install | sh -s -- --version X.Y.Z   # 安装指定版本
curl -fsSL https://voicestudio.sh/install | sh -s -- --main            # 构建当前 main
curl -fsSL https://voicestudio.sh/install | sh -s -- --uninstall       # 卸载应用，保留数据
```

如果无法访问 `voicestudio.sh`，可直接从仓库运行脚本：
`curl -fsSL https://raw.githubusercontent.com/debpalash/VoiceStudio/main/scripts/install.sh | sh`。
前置要求与脚本行为：[安装脚本说明](../../docs/install/script.md)。

**从源码安装**

```bash
git clone https://github.com/debpalash/VoiceStudio.git
cd VoiceStudio
bun run dev
```

参见 [Electron 设置](../../electron/README.md)。

**通过编码智能体安装**（Claude Code、Codex、Cursor 等），粘贴：

```text
Install the VoiceStudio app on this device and verify it works, following
https://github.com/debpalash/VoiceStudio/blob/main/docs/install/agent.md
```

从 0.5.3 或更早版本（Tauri 应用）升级？请[单独安装新应用](../../docs/electron-migration.md)。

</details>

## 文档

| 需求 | 从这里开始 |
|---|---|
| 安装帮助 | [故障排查](../../docs/install/troubleshooting.md) · [模型下载](../../docs/downloading-models.md) |
| 指南 | [多说话人配音](../../docs/dubbing/multi-speaker-guide.md) · [富有表现力的语音](../../docs/expressive-speech.md) · [导出配音](../../docs/dubbing/export.md) |
| 模型与音质 | [引擎指南](../../docs/engines/README.md) · [whisper.cpp ASR](../../docs/engines/whisper-cpp.md) · [性能基准](../../docs/benchmarks.md) |
| 集成 | [本地 API](../../docs/speech-platform.md) · [MCP](../../docs/mcp.md) · [示例](../../examples/README.md) |
| 手机应用 | [iOS 与 Android](../../docs/mobile.md) |
| 开发 | [参与贡献](../../.github/CONTRIBUTING.md)（首次提交 PR 前请[签署 CLA](../../.github/CONTRIBUTING.md#contribution-licensing)）· [更新日志](../../CHANGELOG.md) |

智能体技能：`npx skills add debpalash/VoiceStudio`（音频工作用 **voicestudio**，仓库维护用 **voicestudio-maintainer**）。

## 赞助者

VoiceStudio 免费使用，背后没有付费云服务。赞助者让它持续发布新版本：赞助资金用于维护者时间、测试硬件、代码签名和发布基础设施。

<p>
    <a href="https://supermetry.com/?utm_source=voicestudio&utm_medium=sponsor&utm_campaign=strategic-sponsor&utm_content=readme-logo"><picture><source media="(prefers-color-scheme: dark)" srcset="../../docs/sponsors/supermetry-dark.svg" /><img src="../../docs/sponsors/supermetry.svg" alt="Supermetry" height="48" /></picture></a>
</p>

**你的标志可以出现在这里。** 开发、企业和战略赞助席位开放中，每月 100 美元起；社区赞助者（25 美元）可获得署名链接。赞助换来的是鸣谢，而不是功能。

<a href="https://github.com/sponsors/debpalash"><img src="https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors&logoColor=white" alt="通过 GitHub Sponsors 赞助" /></a>
[Ko-fi](https://ko-fi.com/debpalash) · [PayPal](https://paypal.me/palashCoder) · [赞助等级与权益](../../SPONSORS.md) · [申请展示标志](https://github.com/debpalash/VoiceStudio/issues/new?template=sponsor.yml)

## 团队

### 核心团队

<table>
<tr>
<td align="center" width="200"><a href="https://github.com/debpalash"><img src="https://github.com/debpalash.png?size=160" width="80" height="80" alt="Palash Debnath"></a><br><b>Palash Debnath</b><br><sub>创始人与核心团队</sub><br><sub><a href="https://palash.dev">palash.dev</a> · <a href="https://github.com/debpalash">GitHub</a> · <a href="https://x.com/idebpalash">X</a></sub></td>
<td align="center" width="200"><a href="https://github.com/velixio"><img src="https://github.com/velixio.png?size=160" width="80" height="80" alt="Shimul Debnath"></a><br><b>Shimul Debnath</b><br><sub>核心团队</sub><br><sub><a href="https://shimul.me">shimul.me</a> · <a href="https://github.com/velixio">GitHub</a> · <a href="https://x.com/shimuldn">X</a></sub></td>
</tr>
</table>

### 贡献者

<a href="https://github.com/kevin9327"><img src="https://github.com/kevin9327.png?size=96" width="44" height="44" alt="@kevin9327" title="@kevin9327"></a> <a href="https://github.com/jaketame"><img src="https://github.com/jaketame.png?size=96" width="44" height="44" alt="@jaketame" title="@jaketame"></a> <a href="https://github.com/psiberfunk"><img src="https://github.com/psiberfunk.png?size=96" width="44" height="44" alt="@psiberfunk" title="@psiberfunk"></a> <a href="https://github.com/rudycelekli"><img src="https://github.com/rudycelekli.png?size=96" width="44" height="44" alt="@rudycelekli" title="@rudycelekli"></a> <a href="https://github.com/paoloantinori"><img src="https://github.com/paoloantinori.png?size=96" width="44" height="44" alt="@paoloantinori" title="@paoloantinori"></a> <a href="https://github.com/Chang-Jin-Lee"><img src="https://github.com/Chang-Jin-Lee.png?size=96" width="44" height="44" alt="@Chang-Jin-Lee" title="@Chang-Jin-Lee"></a> <a href="https://github.com/swadhinbiswas"><img src="https://github.com/swadhinbiswas.png?size=96" width="44" height="44" alt="@swadhinbiswas" title="@swadhinbiswas"></a> <a href="https://github.com/BichengWang"><img src="https://github.com/BichengWang.png?size=96" width="44" height="44" alt="@BichengWang" title="@BichengWang"></a> <a href="https://github.com/nirmalchatur"><img src="https://github.com/nirmalchatur.png?size=96" width="44" height="44" alt="@nirmalchatur" title="@nirmalchatur"></a> <a href="https://github.com/Shivendra-Coherent"><img src="https://github.com/Shivendra-Coherent.png?size=96" width="44" height="44" alt="@Shivendra-Coherent" title="@Shivendra-Coherent"></a> <a href="https://github.com/marreiradigital"><img src="https://github.com/marreiradigital.png?size=96" width="44" height="44" alt="@marreiradigital" title="@marreiradigital"></a> <a href="https://github.com/nvtoan0201-swe"><img src="https://github.com/nvtoan0201-swe.png?size=96" width="44" height="44" alt="@nvtoan0201-swe" title="@nvtoan0201-swe"></a>

感谢所有贡献代码、报告、翻译和想法的人。[查看全部贡献者](https://github.com/debpalash/VoiceStudio/graphs/contributors) · [参与贡献](../../.github/CONTRIBUTING.md)

## 许可证与负责任使用

[AGPL-3.0](../../LICENSE) 覆盖本应用，包括在其条款下的商业用途。模型权重、声音和生成内容各有其许可证，模型管理器会为每个模型列出（[清单](../../docs/licensing/model-inventory.md)）。只有在声音所有者许可的情况下才能克隆其声音。详情：[LICENSE-NOTICE.md](../../LICENSE-NOTICE.md)。
